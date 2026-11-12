"""Réalisations thématiques des mécaniques existantes, compilées par Ekole et Spek."""
from copy import deepcopy
import json

from compiler_activite import ROOT, activity_sources, bytes_digest, project_source


def variants(themes):
    path = ROOT / 'activites/invitations-mila/canon/domain/activity.json'
    source = activity_sources(path.read_bytes())
    for theme in themes:
        item = deepcopy(source)
        item['id'] = 'division-' + theme['id']
        item['trame'] = theme['scenario']
        item.pop('character', None)
        capacity, groups = theme['capacity'], theme['groups']
        if type(capacity) is not int or type(groups) is not int or not (2 <= capacity <= 5 and 2 <= groups <= 5):
            raise ValueError('Quantités hors limites pour ' + theme['id'])
        item['tasks'] = {
            'pratique': {'invitations': capacity * groups, 'per_sheet': capacity, 'stock': groups - 1},
            'bilan': {'invitations': capacity * groups + 1, 'per_sheet': capacity, 'stock': groups - 1},
        }
        for locale, words in item['realizations'].items():
            objects, containers = theme['grouping'][locale]
            words.update(french(theme['name'], objects, containers) if locale == 'fr-CA'
                         else english(theme['name_en'], objects, containers))
        # The original contract and the resulting full realized text are both fingerprinted.
        fingerprint = bytes_digest(json.dumps(item, ensure_ascii=False, sort_keys=True).encode('utf-8'))
        activity, projection = project_source(item, fingerprint)
        yield theme['id'], activity, projection


def french(name, objects, containers):
    return {
        'title': name + ' · Les groupes', 'heading': 'Préparer la répartition',
        'objective': 'Forme des groupes égaux pour trouver combien de contenants il faut.',
        'prerequisite': 'Compte les objets d’un groupe et compare deux nombres.',
        'context': f'On doit ranger {{invitations}} objets ({objects}). La capacité de chaque contenant '
                   f'({containers}) est de {{per_sheet}}. Nombre de contenants en stock : {{stock}}.',
        'group': 'Ajoute un contenant à la fois et observe les groupes.',
        'compare': 'Compare le nombre de contenants nécessaires au stock.',
        'reflection': 'Comment sais-tu si le dernier contenant est plein ?',
        'needed': 'Combien de contenants faut-il en tout ?',
        'missing': 'Combien de contenants manquent dans le stock ?',
        'explain': 'Explique pourquoi le dernier groupe utilise un contenant même s’il est incomplet.',
        'criterion': 'La réponse relie le reste à l’utilisation d’un contenant supplémentaire.',
        'add_sheet': 'Ajouter un contenant', 'undo_sheet': 'Retirer un contenant',
        'placement': '{placed} objets sur {total} rangés',
        'incorrect': 'Représente les groupes et compare-les au stock.',
        'next': 'Vérifie que chaque objet a une place.',
    }


def english(name, objects, containers):
    return {
        'title': name + ' · Making groups', 'heading': 'Organize the groups',
        'objective': 'Make equal groups to find how many containers you need.',
        'prerequisite': 'Count the objects in a group and compare two numbers.',
        'context': f'There are {{invitations}} items to pack ({objects}). Each container ({containers}) '
                   f'holds {{per_sheet}}. There are {{stock}} containers in stock.',
        'group': 'Add one container at a time and look at the groups.',
        'compare': 'Compare the number of containers you need with the number in stock.',
        'reflection': 'How can you tell whether the last container is full?',
        'needed': 'How many containers do you need altogether?',
        'missing': 'How many more containers do you need?',
        'explain': 'Explain why the last group needs a container even if it is incomplete.',
        'criterion': 'The explanation connects the remainder to the need for one extra container.',
        'add_sheet': 'Add a container', 'undo_sheet': 'Remove a container',
        'placement': '{placed} out of {total} objects packed',
        'incorrect': 'Draw the groups and compare them with the stock.',
        'next': 'Check that every object has a place.',
    }


def course_projection(theme, course, family):
    ref = f'ekole:univers:{theme["id"]}:{course["id"]}'
    title = course['titre']
    phrases = {
        'title': title, 'theme': theme['name'], 'scene': theme['frames'][family],
        'objective': course['objectif'],
        'limits': 'Contexte de travail proposé. Retrouve la leçon et les exercices dans le parcours Ekole.',
    }
    return {
        'format': 'spek.educational-projection/1', 'producer': 'ekole', 'complete': True,
        'scope': {'audience': 'student', 'data_classification': 'public_demo',
                  'export_status': 'authorized_local_preview', 'dataset_ref': ref,
                  'reader_policy_ref': 'ekole:univers-local', 'pedagogical_review': 'not_submitted'},
        'document': {
            'article': {'id': course['id'], 'title_key': 'title', 'subtitle_key': 'theme', 'abstract_key': 'objective'},
            'units': [{'id': key, 'kind': kind, 'realization_key': key, 'evidence_refs': [],
                       'epistemic_status': 'limitation' if key == 'limits' else 'method',
                       'external_ref': ref + ':' + key}
                      for key, kind in [('scene', 'context'), ('objective', 'information'), ('limits', 'qualification')]],
            'evidence': [],
            'sections': [{'id': 'scene', 'layout': 'portal-page', 'heading_key': 'theme',
                          'slots': {'lead': ['scene'], 'information': ['objective'], 'limits': ['limits']}}],
        },
        'realizations': {'format': 'kristal.layout-realizations/0.1',
                         'entries': {key: {'fr': {'text': text, 'status': 'fixture', 'provider': 'ekole-univers'}}
                                     for key, text in phrases.items()}},
    }


def authored_variants(themes):
    for (key, source_id), realizations in {
        ('jardinage', 'semis-a-comparer'): {
            'fr-CA': {
                'title': 'Deux bacs au jardin', 'context': 'Après une semaine, le plant près de la clôture mesure 5 cm et celui près de l’allée 8 cm.',
                'transfer': 'Au jardin, on veut comparer deux jeunes plants en pots qui reçoivent des durées de lumière différentes.',
                'observations': ['Le plant près de la clôture mesure 5 cm.', 'Le plant près de l’allée mesure 8 cm.',
                                 'L’allée fait pousser le plant plus vite.'],
            },
            'en': {
                'title': 'Two garden beds', 'context': 'After one week, the plant near the fence is 5 cm tall and the plant by the path is 8 cm tall.',
                'transfer': 'The garden team wants to compare two young potted plants that get different lengths of time in the light.',
                'observations': ['The plant near the fence is 5 cm tall.', 'The plant by the path is 8 cm tall.',
                                 'The path makes the plant grow faster.'],
            },
        },
        ('jazz', 'recit-du-spectacle'): {
            'fr-CA': {
                'title': 'Le programme du festival', 'context': 'Il manque le nom du groupe sur le programme. Léo ajoute le nom, puis imprime le programme. Les bénévoles distribuent les copies.',
                'transfer': 'Au kiosque, les fiches du programme se mélangent. Une bénévole les numérote selon l’heure des concerts. Son collègue peut les remettre dans l’ordre.',
                'orders': ['Ajouter le nom → imprimer → distribuer', 'Distribuer → imprimer → ajouter le nom',
                           'Imprimer → distribuer → ajouter le nom'],
                'causes': ['Les fiches se mélangent.', 'La bénévole numérote les fiches.', 'Les concerts sont prévus.'],
                'question': 'Qu’est-ce qui permet au collègue de remettre les fiches dans l’ordre ?',
                'why': 'Explique comment le collègue utilise les numéros.',
                'criterion': 'La justification relie les numéros à l’ordre chronologique des concerts.',
            },
            'en': {
                'title': 'The festival programme', 'context': 'The band’s name is missing from the programme. Léo adds the name and prints the programme. The volunteers hand out the copies.',
                'transfer': 'The programme cards get mixed up at the kiosk. A volunteer numbers the cards by concert time. Her colleague can put them back in order.',
                'orders': ['Add the name → print → hand out copies', 'Hand out copies → print → add the name',
                           'Print → hand out copies → add the name'],
                'causes': ['The cards get mixed up.', 'The volunteer numbers the cards.', 'The concerts are scheduled.'],
                'question': 'What lets the colleague put the cards back in order?',
                'why': 'Explain how the colleague uses the numbers.',
                'criterion': 'The explanation connects the numbers to the chronological order of the concerts.',
            },
        },
    }.items():
        if key not in themes:
            continue
        path = ROOT / 'activites' / source_id / 'canon/domain/activity.json'
        source = activity_sources(path.read_bytes())
        source['id'] = source_id + '-' + key
        source['trame'] = themes[key]['scenario']
        for locale, words in source['realizations'].items():
            realization = realizations[locale]
            words.update({field: realization[field] for field in ('title', 'context', 'transfer')})
            questions = words['questions']
            if 'observations' in realization:
                questions['pratique']['choisir']['options'] = dict(zip('abc', realization['observations'], strict=True))
            else:
                questions['pratique']['choisir']['options'] = dict(zip('abc', realization['orders'], strict=True))
                questions['bilan']['choisir'].update(prompt=realization['question'],
                                                       options=dict(zip('abc', realization['causes'], strict=True)))
                questions['bilan']['justifier'].update(prompt=realization['why'],
                                                        criteria={'raison': realization['criterion']})
        fingerprint = bytes_digest(json.dumps(source, ensure_ascii=False, sort_keys=True).encode('utf-8'))
        activity, projection = project_source(source, fingerprint)
        yield key, activity, projection
