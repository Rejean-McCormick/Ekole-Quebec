"""Vérifier les leçons candidates et leur rendu Spek en mémoire."""
from collections import Counter
from html import escape
import sys

from b2_pipeline.core import read_json, source_info, source_scaffold, student_publication
from construire_ecole import ROOT, SPEK
from exporter_lecons_relues import spek_projection


def verify():
    sys.path.insert(0, str(SPEK))
    from spek.core import compile_inputs
    from spek.document import project_document
    from spek.education import import_educational
    from spek.render import article_html

    pack = read_json(ROOT / 'pack.json')
    seeds = read_json(ROOT / 'data/lecons-candidates.json')
    candidates = seeds['courses']
    courses = {course['id'] for course in pack['cours']}
    path_courses = [cid for path in pack['parcours'] for cid in path['cours_ids']]
    if (seeds['format'] != 'ekole.lesson-seeds/1' or set(candidates) != courses
            or set(path_courses) != courses or len(path_courses) != len(courses)):
        raise ValueError('Les leçons et les parcours doivent couvrir une fois chaque cours du pack.')

    layout = read_json(ROOT / 'outils/spek-layouts/portal-page.json')
    totals = Counter()
    for path in pack['parcours']:
        grade = int(path['id'].split('-')[-1])
        for cid in path['cours_ids']:
            try:
                source = source_info(ROOT, cid)
                source['grade'] = grade
                draft = source_scaffold(source, cid)
                rows = candidates[cid]
                if len(rows) != 6 or any(set(row) != {'titre', 'blocks'} for row in rows):
                    raise ValueError('Six étapes préremplies attendues.')
                for module, row in zip(draft['modules'], rows):
                    module.update(row)
                public = student_publication(draft, source)
                projection = spek_projection(public, draft, 'verification', reviewed=False)
                article, realizations = import_educational(projection, 'ekole')
                compiled = compile_inputs(article, realizations, [layout], languages=('fr',))
                document = project_document(compiled, 'fr')
                headings = [section.heading for section in document.sections]
                if headings != [module['titre'] for module in public['modules']]:
                    raise ValueError('Titres des étapes Spek incompatibles avec la projection élève.')
                page = article_html(compiled, 'fr', formats=('html',))
                if any(escape(heading, quote=False) not in page for heading in headings):
                    raise ValueError('Titre d’étape absent de la page HTML.')
            except ValueError as exc:
                raise ValueError(f'{cid} : {exc}') from exc
            totals[grade] += 1

    for grade, count in sorted(totals.items()):
        print(f'Année {grade} · {count} leçons')
    print(f'{len(courses)} leçons, {6 * len(courses)} étapes et rendus Spek vérifiés en mémoire.')


if __name__ == '__main__':
    verify()
