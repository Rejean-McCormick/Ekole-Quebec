"""Build and switch the local Québec catalogue after checking all its pages."""
from pathlib import Path
import argparse
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import uuid

from compiler_activite import KONTEXTE, ROOT, bytes_digest, projections, write_json
from projection_portail import projection as portal_projection
from projection_univers import authored_variants, course_projection, variants
from inkui.adapters.ekole import import_ekole
from b2_pipeline.core import source_info, source_scaffold, validate_draft

ENGINE = Path(os.environ.get('EKOLE_MOTEUR', ROOT.parent / 'ekole')).resolve()
WORKSPACE = ROOT.parent.parent
SPEK_CANDIDATES = (
    WORKSPACE / 'Spek_Semantic-publishing' / 'Spek',
    ROOT.parent / 'Spek',
    ROOT.parent / 'Spek_Semantic-publishing' / 'Spek',
)
SPEK = Path(os.environ.get('EKOLE_SPEK') or next(
    (folder for folder in SPEK_CANDIDATES if (folder / 'spek/__init__.py').is_file()),
    SPEK_CANDIDATES[0],
)).resolve()
LIGHT_CANDIDATES = (
    WORKSPACE / 'Konstellation' / 'Konstellation-Light',
    ROOT.parent / 'Konstellation-Light',
)


def scenario_bank():
    path = KONTEXTE / 'data/trames/catalogue-neutral-v0.2.json'
    catalogue = json.loads(path.read_text(encoding='utf-8-sig'))
    if catalogue['format'] != 'kontexte.catalogue-trames/1':
        raise ValueError('Format de banque Kontexte inconnu')
    return [{key: entry[key] for key in ('id', 'titre', 'famille', 'resultat')}
            for entry in catalogue['scenarios']]


def spek(*args):
    subprocess.run([sys.executable, '-m', 'spek', *map(str, args)], cwd=SPEK, check=True)


def build_pages(folder, projection, languages, layouts=None):
    write_json(folder / 'projection-spek.json', projection)
    inputs, pages = folder / 'spek-input', folder / 'spek-html'
    spek('import-educational', '--adapter', 'ekole', '--input', folder / 'projection-spek.json',
         '--out-dir', inputs)
    layout_args = ('--layouts', layouts) if layouts else ()
    spek('build', '--source', inputs / 'article.json', '--realizations', inputs / 'realizations.json',
         '--languages', ','.join(languages), '--formats', 'html', '--out', pages, *layout_args)
    spek('verify-site', pages)


def page_refs(stage, version, relative, languages):
    root = relative / 'spek-html'
    return {lang: {name: {'path': (Path('versions') / version / root / lang / name).as_posix(),
                         'sha256': bytes_digest((stage / root / lang / name).read_bytes())}
                   for name in ('index.html', 'document.json')}
            for lang in languages}


def build_explorer(stage, version, light):
    candidate = stage / 'curation-konstellation.json'
    site = stage / 'konstellation'
    stage.mkdir(exist_ok=True)
    subprocess.run(['node', str(light / 'scripts/project-ekole-catalogue.mjs'), '--pack', str(ROOT / 'pack.json'),
                    '--graph', str(ROOT / 'integrations/graphe.json'), '--out', str(candidate), '--local', 'YES'],
                   check=True)
    subprocess.run(['node', str(light / 'scripts/build-semantic-preview.mjs'), '--input', str(candidate),
                    '--out', str(site), '--local', 'YES'], check=True)
    names = {'index.html', 'app.js', 'style.css', 'sw.js', 'graph-core.mjs', 'profile.mjs',
             'semantic-display.mjs', 'multilingual-read.mjs', 'assets/uckk-logo.svg', 'assets/logo_k.svg', 'data/catalog.json'}
    catalog = json.loads((site / 'data/catalog.json').read_bytes())
    names.update(entry['path'] for entry in catalog['entries'])
    return {name: {'path': (Path('versions') / version / 'konstellation' / name).as_posix(),
                   'sha256': bytes_digest((site / name).read_bytes())}
            for name in sorted(names) if (site / name).is_file()}


def build_worlds(stage, version):
    compiler = ENGINE / 'legacy/tools/compiler_mondes_v12.py'
    module_spec = importlib.util.spec_from_file_location('ekole_compiler_mondes_v12', compiler)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    pack = json.loads((ROOT / 'pack.json').read_text(encoding='utf-8-sig'))
    worlds = module.compile_mondes(ROOT, check=True, course_ids={course['id'] for course in pack['cours']})
    name = 'micro-mondes-prives.json'
    path = stage / name
    write_json(path, {'items': worlds['items']})
    print(f"{worlds['count']} micro-mondes V12 reconstruits")
    return {'path': (Path('versions') / version / name).as_posix(),
            'sha256': bytes_digest(path.read_bytes())}


def build_corpus(stage, version):
    subprocess.run([sys.executable, str(ROOT / 'outils/construire_notions.py'), str(stage), str(SPEK)],
                   check=True)
    pack = json.loads((ROOT / 'pack.json').read_bytes())
    notions = {course['id']: page_refs(stage, version, Path('notions') / course['id'], ('fr',))
               for course in pack['cours']}
    banks, report = import_ekole(ROOT)
    private = {}
    for bank, row in zip(banks, report['banks']):
        cid = bank['items'][0]['course_ref']
        if cid not in notions or cid in private:
            raise ValueError('Banque absente du pack ou dupliquée : ' + cid)
        if any(item['course_ref'] != cid or item['status'] != 'draft' for item in bank['items']):
            raise ValueError('Statut ou cours incohérent dans une banque')
        relative = Path('banques-privees') / (cid + '.json')
        path = stage / relative
        write_json(path, bank)
        private[cid] = {'path': (Path('versions') / version / relative).as_posix(),
                        'sha256': bytes_digest(path.read_bytes()), 'source': row['source_hash'],
                        'items': row['items']}
    if set(private) != set(notions):
        raise ValueError('Une banque candidate est requise pour chaque cours')
    print(f"{report['bank_count']} banques privées · {report['item_count']} questions candidates")
    return notions, private


def build_lessons(stage, version):
    pack = json.loads((ROOT / 'pack.json').read_bytes())
    seeds = json.loads((ROOT / 'data/lecons-candidates.json').read_bytes())
    if seeds['format'] != 'ekole.lesson-seeds/1':
        raise ValueError('Format des leçons candidates inconnu')
    candidates = seeds['courses']
    all_courses = {c['id'] for c in pack['cours']}
    if set(candidates) - all_courses:
        raise ValueError('Brouillon prérempli hors corpus')
    grades = {cid: int(path['id'].split('-')[-1]) for path in pack['parcours'] for cid in path['cours_ids']}
    for cid in sorted(all_courses):
        src = source_info(ROOT, cid)
        src['grade'] = grades[cid]
        draft = source_scaffold(src, cid)
        if cid in candidates:
            rows = candidates[cid]
            if len(rows) != 6 or any(set(row) != {'titre', 'blocks'} for row in rows):
                raise ValueError('Six étapes préremplies requises pour ' + cid)
            for module, row in zip(draft['modules'], rows):
                module.update(row)
        validate_draft(draft, src, complete=cid in candidates)
    name = 'lecons-candidates.json'
    write_json(stage / name, candidates)
    print(f'{len(candidates)} leçons préremplies et {len(all_courses)} gabarits privés validés')
    return {'path': (Path('versions') / version / name).as_posix(),
            'sha256': bytes_digest((stage / name).read_bytes())}


def build_universe_pages(stage, version, themes):
    sys.path.insert(0, str(SPEK))
    sys.path.insert(0, str(ENGINE))
    from univers import FAMILIES
    from spek.core import compile_inputs
    from spek.document import project_document
    from spek.education import import_educational
    from spek.render import article_html

    pack = json.loads((ROOT / 'pack.json').read_bytes())
    layout = json.loads((ROOT / 'outils/spek-layouts/portal-page.json').read_bytes())
    output = {}
    for theme in themes:
        pages = output[theme['id']] = {}
        for course in pack['cours']:
            cid = course['id']
            family = FAMILIES[cid.split('-')[2]]
            article, realizations = import_educational(course_projection(theme, course, family), 'ekole')
            compiled = compile_inputs(article, realizations, [layout], languages=('fr',))
            relative = Path('univers-spek') / theme['id'] / cid / 'fr'
            folder = stage / relative
            folder.mkdir(parents=True, exist_ok=True)
            (folder / 'index.html').write_bytes(article_html(compiled, 'fr', formats=('html',)).encode('utf-8'))
            write_json(folder / 'document.json', project_document(compiled, 'fr').to_dict())
            pages[cid] = {name: {'path': (Path('versions') / version / relative / name).as_posix(),
                                 'sha256': bytes_digest((folder / name).read_bytes())}
                          for name in ('index.html', 'document.json')}
    print(f"{len(themes)} univers · {sum(len(pages) for pages in output.values())} fiches de cours Spek")
    return output



def build(work, light=None):
    work.mkdir(parents=True, exist_ok=True)
    version = uuid.uuid4().hex
    destination = work / 'versions' / version
    bank = scenario_bank()
    known = {row['id'] for row in bank}
    catalogue = {'format': 'ekole.local-activity-catalogue/1', 'entries': [], 'scenarios': bank, 'portal': []}
    sources = sorted((ROOT / 'activites').glob('*/canon/domain/activity.json'))
    if not sources:
        raise ValueError('Aucune activité à construire')
    with TemporaryDirectory(prefix='build-', dir=work) as temporary:
        stage = Path(temporary) / version
        seen = set()
        def register(activity, projection, theme=None):
            aid = activity['id']
            if aid in seen:
                raise ValueError('Identifiant d’activité dupliqué')
            seen.add(aid)
            if activity['scenario'] not in known:
                raise ValueError('Trame Kontexte inconnue : ' + str(activity['scenario']))
            folder = stage / aid
            write_json(folder / 'activite-privee.json', activity)
            build_pages(folder, projection, ('fr', 'en'))
            relative = Path('versions') / version / aid
            entry = {
                'bundle': (relative / 'activite-privee.json').as_posix(),
                'pages': page_refs(stage, version, Path(aid), ('fr', 'en')),
            }
            if theme:
                entry['theme'] = theme
            catalogue['entries'].append(entry)

        for source in sources:
            activity, projection = projections(source)
            if activity['id'] != source.parents[2].name:
                raise ValueError('Identifiant d’activité incohérent')
            register(activity, projection)
        universe_file = ROOT / 'data/univers.json'
        if universe_file.is_file():
            universe = json.loads(universe_file.read_bytes())
            for theme, activity, projection in variants(universe['themes']):
                register(activity, projection, theme)
            for theme, activity, projection in authored_variants({row['id']: row for row in universe['themes']}):
                register(activity, projection, theme)
            name = 'univers.json'
            write_json(stage / name, universe)
            catalogue['univers_pages'] = build_universe_pages(stage, version, universe['themes'])
            catalogue['univers'] = {'path': (Path('versions') / version / name).as_posix(),
                                     'sha256': bytes_digest((stage / name).read_bytes())}
        for source in sorted((ROOT / 'organisation/pages').glob('*.json')):
            projection = portal_projection(source)
            relative = Path('portail') / source.stem
            build_pages(stage / relative, projection, ('fr',), ROOT / 'outils/spek-layouts')
            catalogue['portal'].append({
                'id': source.stem,
                'title': projection['realizations']['entries']['title']['fr']['text'],
                'pages': page_refs(stage, version, relative, ('fr',)),
            })
        catalogue['worlds'] = build_worlds(stage, version)
        catalogue['notions'], catalogue['banks'] = build_corpus(stage, version)
        catalogue['lessons'] = build_lessons(stage, version)
        if light:
            catalogue['explorer'] = build_explorer(stage, version, light)
        destination.parent.mkdir(exist_ok=True)
        stage.rename(destination)
        candidate = work / f'catalogue-{version}.json'
        try:
            write_json(candidate, catalogue)
            subprocess.run([sys.executable, str(ENGINE / 'launcher.py'), '--contenu', str(ROOT),
                            '--activites-locales', str(candidate), '--verifier'], check=True)
            candidate.replace(work / 'catalogue.json')
        finally:
            candidate.unlink(missing_ok=True)
    variant_count = len(catalogue['entries']) - len(sources)
    print(f'{len(sources)} activités de base, {variant_count} variantes, {len(bank)} trames : {work / "catalogue.json"}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=ROOT / 'dist/ecole-locale')
    parser.add_argument('--konstellation-light', type=Path, help='Checkout Light pour la carte locale')
    args = parser.parse_args()
    light = args.konstellation_light
    if light is None and os.environ.get('EKOLE_KONSTELLATION_LIGHT'):
        light = Path(os.environ['EKOLE_KONSTELLATION_LIGHT'])
    if light is None and shutil.which('node'):
        light = next((folder for folder in LIGHT_CANDIDATES
                      if (folder / 'scripts/project-ekole-catalogue.mjs').is_file()
                      and (folder / 'scripts/build-semantic-preview.mjs').is_file()), None)
    if light is None:
        print('Carte Konstellation ignorée : Node et le dépôt Light sont requis pour cet aperçu.')
    build(args.out.resolve(), light.resolve() if light else None)


if __name__ == '__main__':
    main()
