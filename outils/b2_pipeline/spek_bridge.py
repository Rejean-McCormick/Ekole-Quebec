"""Projection Spek v0.5 `spek.educational-projection/1` for LOCAL DEMO only.

Spek's static exports are public: no student records, no solutions, no internal notes.
This bridge uses only the B2 **curated student draft** and never imports expert sections.
"""
from __future__ import annotations
from .core import validate_draft, GateError


def educational_preview(draft,source):
    validate_draft(draft,source)
    cid=draft['course_id']
    units=[];entries={}
    slots={'objective':['u.objective'],'prerequisites':['u.prerequisites'],
           'steps':[],'reflection':['u.reflection'],'limits':['u.limits']}
    texts={
        'objective':('objective','Je sais représenter des groupes égaux pour comprendre la multiplication.'),
        'prerequisites':('prerequisite','Je peux compter des objets et faire de petites additions.'),
        'reflection':('reflection','Comment mon dessin m’aide-t-il à compter les objets ?'),
        'limits':('qualification','Proposition locale non approuvée pour un usage scolaire. Demande à ton enseignant de vérifier.'),
    }
    for i,mod in enumerate(draft['modules'],1):
        # Les six titres et instructions viennent d'un brouillon rédigé spécifiquement pour l'enfant.
        passage=next((b['text'] for b in mod['blocks'] if b['type'] in ('instruction','challenge')),
                     mod['blocks'][0]['text'])
        texts[f'step{i}']=('step',mod['titre']+' — '+passage)
        slots['steps'].append(f'u.step{i}')
    for key,(kind,value) in texts.items():
        ident='u.'+key
        units.append({'id':ident,'kind':kind,'realization_key':key,
                      'epistemic_status':'limitation' if kind=='qualification' else 'method',
                      'evidence_refs':[],'external_ref':f'ekole:b2:{cid}:{ident}'})
        entries[key]={'fr':{'text':value,'status':'fixture','provider':'manual_demo_fixture','channel':'legacy'}}
    for key,value in {
        'title':draft['titre'], 'subtitle':'Parcours de multiplication — 3e année',
        'abstract':'Une proposition de fiche construite à partir d’un brouillon élève relu localement.',
        'h.path':'Six étapes pour représenter des groupes égaux',
    }.items():
        entries[key]={'fr':{'text':value,'status':'fixture','provider':'manual_demo_fixture','channel':'legacy'}}
    return {
        'format':'spek.educational-projection/1', 'producer':'ekole','complete':True,
        'scope':{'audience':'student','data_classification':'public_demo',
                 'export_status':'authorized_local_preview',
                 'dataset_ref':f'ekole:b2:{cid}:local-demo',
                 'reader_policy_ref':'ekole:b2:preview:anonymous-only',
                 'pedagogical_review':'not_submitted'},
        'document':{
            'article':{'id':f'urn:demo:ekole:b2:{cid}', 'title_key':'title',
                       'subtitle_key':'subtitle','abstract_key':'abstract'},
            'units':units,'evidence':[],
            'sections':[{'id':'path','layout':'learning-path',
                         'heading_key':'h.path','slots':slots}]},
        'realizations':{'format':'kristal.layout-realizations/0.1',
                        'note':'Compilation Spek locale non autorisée pour une diffusion scolaire.',
                        'entries':entries},
    }
