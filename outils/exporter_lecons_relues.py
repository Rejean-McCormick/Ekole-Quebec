"""Prepare an overlay of the reviewed local lessons, with optional Spek previews."""
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse
from shutil import copytree
import sys

from construire_ecole import ENGINE, ROOT, build_pages, bytes_digest, write_json


def spek_projection(public, draft, revision, *, reviewed=True):
    reference = f'ekole:local-lesson:{public["id"]}:{revision}'
    notice = public['notice'] if reviewed else 'Aperçu privé du brouillon élève.'
    subtitle = 'Leçon Ekole · Revue locale' if reviewed else 'Leçon Ekole · Brouillon'
    phrases = {'title': public['titre'], 'subtitle': subtitle, 'abstract': notice, 'limits': notice}
    units = [{'id': 'limits', 'kind': 'qualification', 'realization_key': 'limits',
              'epistemic_status': 'limitation', 'evidence_refs': [], 'external_ref': reference}]
    sections = []
    for index, module in enumerate(draft['modules'], 1):
        name = f'etape-{index}'
        heading = name + '-titre'
        phrases[heading] = module['titre']
        keys = []
        for i, block in enumerate(module['blocks'], 1):
            body = block['text']
            key = f'{name}-bloc-{i}'
            keys.append(key)
            phrases[key] = body
            units.append({'id': key, 'kind': 'context' if i == 1 else 'information',
                          'realization_key': key, 'epistemic_status': 'method',
                          'evidence_refs': [], 'external_ref': reference + ':' + key})
        sections.append({'id': name, 'layout': 'portal-page', 'heading_key': heading,
                         'slots': {'lead': keys[:1], 'information': keys[1:], 'limits': ['limits']}})
    return {
        'format': 'spek.educational-projection/1', 'producer': 'ekole', 'complete': True,
        'scope': {'audience': 'student', 'data_classification': 'public_demo',
                  'export_status': 'authorized_local_preview', 'dataset_ref': reference,
                  'reader_policy_ref': 'ekole:reviewed-local-only' if reviewed else 'ekole:private-candidate-check',
                  'pedagogical_review': 'reviewed' if reviewed else 'not_submitted'},
        'document': {'article': {'id': public['id'], 'title_key': 'title', 'subtitle_key': 'subtitle',
                                  'abstract_key': 'abstract'},
                     'units': units, 'evidence': [], 'sections': sections},
        'realizations': {'format': 'kristal.layout-realizations/0.1',
                         'entries': {key: {'fr': {'text': value, 'status': 'fixture',
                                                 'provider': 'ekole-local-reviewed' if reviewed else 'ekole-local-draft'}}
                                     for key, value in phrases.items()}},
    }


def export(index, target, requested, with_spek):
    sys.path.insert(0, str(ENGINE))
    from activite_locale import Catalogue
    from compiler_activite import INKUI
    from launcher import load_pack

    if target.exists() or target.is_symlink():
        raise ValueError('Choisir un nouveau dossier d’export')
    if not (index.parent / 'tentatives.sqlite3').is_file():
        raise ValueError('Base locale de revue absente')
    pack = load_pack(ROOT)
    courses = {c['id']: c for c in pack['cours']}
    catalogue = Catalogue(index, courses, INKUI, content=ROOT, pack=pack)
    if catalogue.editorial is None:
        raise ValueError('Le build doit inclure l’atelier des leçons')
    selected = catalogue.editorial.export(requested)
    target.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix='lecons-', dir=target.parent) as temporary:
        root = Path(temporary) / 'overlay'
        manifest = {'format': 'ekole.reviewed-local-overlay/1', 'scope': 'local_preview', 'files': {}}
        for cid, (public, draft, revision) in selected.items():
            relative = Path('publications/eleve') / (cid + '.json')
            output = root / relative
            write_json(output, public)
            manifest['files'][relative.as_posix()] = bytes_digest(output.read_bytes())
            if with_spek:
                folder = Path(temporary) / 'builds' / cid
                build_pages(folder, spek_projection(public, draft, revision), ('fr',), ROOT / 'outils/spek-layouts')
                preview = root / 'apercus-spek' / cid
                copytree(folder / 'spek-html', preview)
                for path in sorted(preview.rglob('*')):
                    if path.is_file():
                        manifest['files'][path.relative_to(root).as_posix()] = bytes_digest(path.read_bytes())
        write_json(root / 'manifeste-lecons.json', manifest)
        root.rename(target)
    print(f'{len(selected)} leçons relues exportées vers {target}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--catalogue', type=Path, default=ROOT / 'dist/ecole-locale/catalogue.json')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--spek', action='store_true')
    select = parser.add_mutually_exclusive_group(required=True)
    select.add_argument('--cours', action='append', help='ID à exporter, option répétable')
    select.add_argument('--toutes-relues', action='store_true')
    args = parser.parse_args()
    export(args.catalogue.resolve(), args.out.absolute(), args.cours, args.spek)


if __name__ == '__main__':
    main()
