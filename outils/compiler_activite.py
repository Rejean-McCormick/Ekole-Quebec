"""Build private Ekole and filtered Spek projections from an activity Kristal."""
from pathlib import Path
import argparse
import os
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
KONTEXTE = Path(os.environ.get('EKOLE_KONTEXTE', ROOT.parent / 'Kontexte')).resolve()
INKUI = Path(os.environ.get('EKOLE_INKUISITE', ROOT.parent / 'Inkuisite')).resolve()
sys.path.insert(0, str(INKUI))

from inkui.common import bytes_digest, loads, require, write_json
from inkui.exams import build_exam
from inkui.generation import approve_item

LOCALES = {'fr-CA': 'fr', 'en': 'en'}
MODES = ('pratique', 'bilan')


def checked_source(path, expected):
    raw = path.read_bytes()
    require(bytes_digest(raw) == expected, f'Source modifiée : {path.name}')
    return loads(raw.decode("utf-8-sig"))


def activity_sources(raw):
    source = loads(raw.decode('utf-8-sig'))
    require(source['format'] == 'ekole.activity/1' and source['status'] == 'local_demo',
            'Contrat d’activité locale attendu')
    course, scenario = source['course'], source['scenario']
    require(re.fullmatch(r'qc-pri-[a-z]+-\d{3}', course['id']) is not None
            and re.fullmatch(r'[a-z][a-z0-9-]{1,79}', scenario['id']) is not None,
            'Références de cours ou de mission invalides')
    contract = checked_source(ROOT / 'kristals' / course['id'] / 'authoring/CONTRAT_PEDAGOGIQUE.json',
                              course['sha256'])
    require(contract['objectif_id'] == course['objective'], 'Objectif source différent')
    mission_file = scenario['id'] + '.json'
    candidates = [KONTEXTE / prefix / mission_file
                  for prefix in ('data/missions', 'integrations/ekole/missions')]
    matches = [candidate for candidate in candidates if candidate.is_file()]
    require(len(matches) == 1, 'Mission Kontexte absente ou ambiguë')
    mission = checked_source(matches[0], scenario['sha256'])
    require(mission['version'] == scenario['version'] and any(
        step['id'] == scenario['step'] and course['id'] in step['curriculum_ids']
        for step in mission['steps']), 'Étape de mission incompatible')
    require(set(source['realizations']) == set(LOCALES), 'Réalisations fr-CA et en requises')
    characters = source.get('character')
    if characters is not None:
        require(set(characters) == set(LOCALES), 'Une fiche Karacter par langue est requise')
        for locale, excerpt in characters.items():
            require(excerpt['format'] == 'karacter.ekole-character/1' and excerpt['status'] == 'candidate'
                    and excerpt['locale'] == locale and set(excerpt['character']) == {'name', 'role', 'intention'},
                    'Fiche Karacter candidate incompatible')
            fields = excerpt['character']
            require(all(isinstance(fields[key], str) and len(fields[key]) <= maximum
                        for key, maximum in {'name': 100, 'role': 160, 'intention': 450}.items())
                    and bool(fields['name'].strip()), 'Fiche Karacter invalide')
    require(set(source['tasks']) == set(MODES), 'Pratique et bilan requis')
    model = source.get('model', 'grouping')
    require(model in ('grouping', 'questions'), 'Modèle d’activité inconnu')
    if model == 'grouping':
        for case in source['tasks'].values():
            require(all(type(case[key]) is int for key in ('invitations', 'per_sheet', 'stock')),
                    'Les quantités doivent être entières')
            require(1 <= case['per_sheet'] <= case['invitations'] <= 30,
                    'Quantités de la mission incompatibles')
            needed = -(-case['invitations'] // case['per_sheet'])
            require(0 <= case['stock'] < needed, 'Stock de feuilles incompatible')
        bilan = source['tasks']['bilan']
        require(bilan['invitations'] % bilan['per_sheet'] != 0,
                'Le bilan doit permettre de justifier un groupe incomplet')
    else:
        for mode in MODES:
            items = source['tasks'][mode]['items']
            ids = [item['id'] for item in items]
            require(0 < len(ids) <= 12 and len(ids) == len(set(ids)), 'Questions absentes ou dupliquées')
            require(all(re.fullmatch(r'[a-z][a-z0-9-]{0,60}', key) for key in ids),
                    'Identifiant de question invalide')
            for locale in LOCALES:
                require(set(source['realizations'][locale]['questions'][mode]) == set(ids),
                        'Couverture des questions incomplète')
    return source


def grouping_questions(case, words, mode):
    needed = -(-case['invitations'] // case['per_sheet'])
    for key, value in (('needed', needed), ('missing', needed - case['stock'])):
        yield {'id': key, 'kind': 'numeric', 'scoring': {'expected': str(value), 'tolerance': '0'},
               'prompt': words[key]}
    if mode == 'bilan':
        yield {'id': 'explain', 'kind': 'rubric', 'prompt': words['explain'],
               'scoring': {'criteria': [{'id': 'incomplete-group', 'description': words['criterion'],
                                         'max_points': 1}]}}


def authored_questions(case, words, mode):
    for spec in case['items']:
        key, kind = spec['id'], spec['kind']
        localized = words['questions'][mode][key]
        item = {'id': key, 'kind': kind, 'prompt': localized['prompt']}
        if kind in ('single_choice', 'multiple_choice'):
            require(set(spec['options']) == set(localized['options']), 'Options traduites incompatibles')
            item['options'] = [{'id': oid, 'text': localized['options'][oid]} for oid in spec['options']]
            item['scoring'] = {'method': 'all_or_nothing', 'correct_ids': spec['correct_ids']}
        elif kind == 'rubric':
            require(set(spec['criteria']) == set(localized['criteria']), 'Critères traduits incompatibles')
            item['scoring'] = {'criteria': [{'id': cid, 'description': localized['criteria'][cid], 'max_points': value}
                                            for cid, value in spec['criteria'].items()]}
        elif kind == 'numeric':
            item['scoring'] = {key: spec[key] for key in ('expected', 'tolerance')}
        else:
            raise ValueError('Type de question locale inconnu')
        item['points'] = spec.get('points', 1)
        if 'feedback' in localized:
            item['feedback'] = localized['feedback']
        yield item


def compile_exam(source, fingerprint, words, locale, mode):
    case = source['tasks'][mode]
    objective = source['course']['id'] + '/' + source['course']['objective']
    authored = source.get('model') == 'questions'
    specs = authored_questions(case, words, mode) if authored else grouping_questions(case, words, mode)
    items = []
    for spec in specs:
        item = {
            'status': 'draft', 'stimulus': '', 'points': 1,
            'feedback': {'correct': words['correct'], 'incorrect': words['incorrect'], 'next_step': words['next']},
            **spec,
            'id': f'{mode}-{spec["id"]}', 'course_ref': source['course']['id'], 'objective_ref': objective,
            'sources': [{'kind': 'authored_example', 'ref': source['id'], 'content_hash': fingerprint,
                         'locator': f'/tasks/{mode}'}],
        }
        items.append(approve_item(item, 'Ekole · fixture technique locale',
                                 'Essai logiciel en portée demo; contenu à relire pour la classe.',
                                 scope='demo', reviewed_at='2026-11-09T00:00:00Z'))
    return build_exam(
        {'format': 'inkui.bank/1.0', 'id': source['id'], 'title': words['title'], 'items': items},
        {'format': 'inkui.blueprint/1.0', 'id': f'{source["id"]}-{mode}-{locale}',
         'title': words[mode], 'seed': f'{source["id"]}-{source["revision"]}-{mode}',
         'scope': 'demo', 'feedback_policy': 'immediate' if mode == 'pratique' else 'on_release',
         'sections': [{'objective_ref': objective, 'count': len(items)}]})


def projections(path):
    raw = path.read_bytes()
    source = activity_sources(raw)
    return project_source(source, bytes_digest(raw))


def project_source(source, fingerprint):
    ref = f'ekole:activity:{source["id"]}:{source["revision"]}:{fingerprint}'
    runtime = {'format': 'ekole.local-activity-bundle/1', 'id': source['id'],
               'course': source['course']['id'], 'revision': source['revision'],
               'source': fingerprint, 'scenario': source.get('trame'), 'views': {}, 'exams': {}}
    kinds = {'objective': 'objective', 'prerequisite': 'prerequisite', 'context': 'step',
             'group': 'step', 'compare': 'step', 'reflection': 'reflection', 'limits': 'qualification'}
    if source.get('character'):
        kinds['character'] = 'step'
    presentation = ('title', 'subtitle', 'heading', *kinds)
    entries = {key: {} for key in presentation}
    for locale, lang in LOCALES.items():
        words = source['realizations'][locale]
        shown = {key: words[key] for key in presentation if key != 'character'}
        if 'character' in kinds:
            card = source['character'][locale]['character']
            shown['character'] = ' · '.join(card[key] for key in ('name', 'role', 'intention') if card[key])
        authored = source.get('model') == 'questions'
        if authored:
            cases = {'pratique': words['context'], 'bilan': words['transfer']}
        else:
            cases = {mode: words['context'].format(**case) for mode, case in source['tasks'].items()}
        shown['context'] = cases['pratique']
        for key, value in shown.items():
            entries[key][lang] = {'text': value, 'status': 'fixture', 'provider': 'ekole-author-demo'}
        exams = {mode: compile_exam(source, fingerprint, words, locale, mode) for mode in MODES}
        view = {
            'id': source['id'], 'locale': locale, 'revision': source['revision'], **shown, 'cases': cases,
            'labels': {key: words[key] for key in ('pratique', 'bilan', 'submit', 'refresh',
                                                  'restart', 'pending', 'score', 'review')},
        }
        if not authored:
            view['practice'] = {key: source['tasks']['pratique'][key] for key in ('invitations', 'per_sheet')}
            view['labels'].update({key: words[key] for key in ('add_sheet', 'undo_sheet', 'placement')})
        runtime['views'][locale] = view
        runtime['exams'][locale] = exams
    spek = {
        'format': 'spek.educational-projection/1', 'producer': 'ekole', 'complete': True,
        'scope': {'audience': 'student', 'data_classification': 'public_demo',
                  'export_status': 'authorized_local_preview', 'dataset_ref': ref,
                  'reader_policy_ref': 'ekole:local-demo', 'pedagogical_review': 'not_submitted'},
        'document': {
            'article': {'id': source['id'], 'title_key': 'title', 'subtitle_key': 'subtitle', 'abstract_key': 'objective'},
            'units': [{'id': key, 'kind': kind, 'realization_key': key,
                       'epistemic_status': 'limitation' if key == 'limits' else 'method',
                       'evidence_refs': [], 'external_ref': ref + ':' + key} for key, kind in kinds.items()],
            'evidence': [],
            'sections': [{'id': 'path', 'layout': 'learning-path', 'heading_key': 'heading',
                          'slots': {'objective': ['objective'], 'prerequisites': ['prerequisite'],
                                    'steps': [*(['character'] if 'character' in kinds else []),
                                              'context', 'group', 'compare'],
                                    'reflection': ['reflection'], 'limits': ['limits']}}],
        },
        'realizations': {'format': 'kristal.layout-realizations/0.1', 'entries': entries},
    }
    return runtime, spek


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True, help='Dossier local privé, hors du site')
    parser.add_argument('--activity', type=Path,
                        default=ROOT / 'activites/invitations-mila/canon/domain/activity.json')
    args = parser.parse_args()
    runtime, spek = projections(args.activity)
    write_json(args.out / 'activite-privee.json', runtime)
    write_json(args.out / 'spek-projection.json', spek)
    print('Projections locales :', args.out.resolve())


if __name__ == '__main__':
    main()
