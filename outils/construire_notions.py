"""Render all discovery cards through Spek without importing any assessment text."""
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import sys
from types import SimpleNamespace

from compiler_activite import ROOT, bytes_digest, write_json


def projection(course, by_id):
    cid = course['id']
    path = ROOT / 'kristals' / cid / 'authoring/CONTRAT_PEDAGOGIQUE.json'
    raw = path.read_bytes()
    source = json.loads(raw)
    if source['kristal_id'] != cid:
        raise ValueError('Contrat de cours incompatible : ' + cid)
    words = {
        'title': course['titre'],
        'subtitle': course['discipline'] + ' · Ekole Québec',
        'objective': source['objectif_observable'],
        'concepts': ' · '.join(source['concepts']),
        'limits': 'Fiche de découverte issue du référentiel candidat. La leçon, les activités et les évaluations sont distinctes.',
    }
    prerequisites = source.get('prerequis_bloquants', [])
    if prerequisites:
        words['prior'] = 'Notions préalables : ' + ' · '.join(by_id[key]['titre'] for key in prerequisites)
    categories = {'objective': 'context', 'concepts': 'information', 'limits': 'qualification'}
    if prerequisites:
        categories['prior'] = 'information'
    reference = f'ekole:discovery:{cid}:{bytes_digest(raw)}'
    return {
        'format': 'spek.educational-projection/1', 'producer': 'ekole', 'complete': True,
        'scope': {'audience': 'student', 'data_classification': 'public_demo',
                  'export_status': 'authorized_local_preview', 'dataset_ref': reference,
                  'reader_policy_ref': 'ekole:discovery-local-preview', 'pedagogical_review': 'not_submitted'},
        'document': {
            'article': {'id': cid, 'title_key': 'title', 'subtitle_key': 'subtitle', 'abstract_key': 'objective'},
            'units': [{'id': key, 'kind': kind, 'realization_key': key,
                       'epistemic_status': 'limitation' if key == 'limits' else 'method',
                       'evidence_refs': [], 'external_ref': reference + ':' + key}
                      for key, kind in categories.items()],
            'evidence': [],
            'sections': [{'id': 'notion', 'layout': 'portal-page', 'heading_key': 'title',
                          'slots': {'lead': ['objective'], 'information': ['concepts', *(['prior'] if prerequisites else [])],
                                    'limits': ['limits']}}],
        },
        'realizations': {'format': 'kristal.layout-realizations/0.1',
                         'entries': {key: {'fr': {'text': value, 'status': 'fixture',
                                                 'provider': 'ekole-course-candidate'}}
                                     for key, value in words.items()}},
    }


def build(stage, spek_root):
    sys.path.insert(0, str(spek_root))
    from spek.cli import build as spek_build
    from spek.education import import_educational

    pack = json.loads((ROOT / 'pack.json').read_bytes())
    by_id = {course['id']: course for course in pack['cours']}
    if len(by_id) != len(pack['cours']):
        raise ValueError('Cours dupliqué dans le pack')
    for course in by_id.values():
        cid = course['id']
        article, realizations = import_educational(projection(course, by_id), 'ekole')
        folder = stage / 'notions' / cid
        source, phrases = folder / 'article.json', folder / 'realizations.json'
        write_json(source, article)
        write_json(phrases, realizations)
        with redirect_stdout(io.StringIO()):
            spek_build(SimpleNamespace(source=source, realizations=phrases, production=False,
                       layouts=ROOT / 'outils/spek-layouts', state_snapshot=None, languages='fr',
                       formats='html', out=folder / 'spek-html'))
    print(f'{len(by_id)} fiches de découverte vérifiées par Spek')


if __name__ == '__main__':
    build(Path(sys.argv[1]), Path(sys.argv[2]))
