"""Project the existing Québec portal utterances into the Spek portal layout."""
from compiler_activite import bytes_digest, loads


def projection(path):
    raw = path.read_bytes()
    source = loads(raw.decode('utf-8-sig'))
    if (source['format'] != 'ekole.portal-page/0.1'
            or source['access'] not in ('public', 'information_publique_sans_donnees_personnelles')):
        raise ValueError('Page du portail inadmissible : ' + path.name)
    slug, title = source['slug'], source['titre']
    if slug != path.stem:
        raise ValueError('Nom de page du portail incohérent')
    ref = f'ekole:portal:{slug}:{bytes_digest(raw)}'
    words = {
        'title': title, 'subtitle': 'Portail Ekole · Aperçu local', 'heading': title,
        'limits': 'Texte candidat fourni dans Ekole Québec. Relecture éditoriale et décision de diffusion requises.',
    }
    utterances = []
    for item in source['utterances']:
        key = item['id']
        if key in words:
            raise ValueError('Énoncé dupliqué : ' + key)
        words[key] = item['fr-CA']
        utterances.append(key)
    if len(utterances) < 2:
        raise ValueError('La page doit avoir au moins deux énoncés')
    unit_kinds = {utterances[0]: 'context', **dict.fromkeys(utterances[1:], 'information'),
                  'limits': 'qualification'}
    return {
        'format': 'spek.educational-projection/1', 'producer': 'ekole', 'complete': True,
        'scope': {'audience': 'general', 'data_classification': 'public_demo',
                  'export_status': 'authorized_local_preview', 'dataset_ref': ref,
                  'reader_policy_ref': 'ekole:portal-local-preview', 'pedagogical_review': 'not_submitted'},
        'document': {
            'article': {'id': source['id'], 'title_key': 'title', 'subtitle_key': 'subtitle',
                        'abstract_key': utterances[0]},
            'units': [{'id': key, 'kind': kind, 'realization_key': key,
                       'epistemic_status': 'limitation' if key == 'limits' else 'method',
                       'evidence_refs': [], 'external_ref': ref + ':' + key}
                      for key, kind in unit_kinds.items()],
            'evidence': [],
            'sections': [{'id': 'info', 'layout': 'portal-page', 'heading_key': 'heading',
                          'slots': {'lead': utterances[:1], 'information': utterances[1:], 'limits': ['limits']}}],
        },
        'realizations': {'format': 'kristal.layout-realizations/0.1',
                         'entries': {key: {'fr': {'text': value, 'status': 'fixture',
                                                 'provider': 'ekole-portal-candidate'}}
                                     for key, value in words.items()}},
    }
