"""Source inspection for the historic Spek 3e-year candidate document.

The candidate data is NOT the upstream publication authorization.
"""
from __future__ import annotations
from pathlib import Path
from .core import GateError,read_json,file_hash


def find_spek(root:Path):
    for doc,cov in [
        ('spek/document.json','spek/coverage.json'),
        ('site/eleve/spek-stage2/spek/fr/document.json','site/eleve/spek-stage2/reports/coverage.json'),
        ('historique/clients/site/eleve/spek-stage2/spek/fr/document.json',
         'historique/clients/site/eleve/spek-stage2/reports/coverage.json'),
    ]:
        dp,cp=root/doc,root/cov
        if dp.is_file() and cp.is_file():return dp,cp
    raise GateError('Pas de projection Spek source et rapport de couverture : fournir les originaux historiques')


def candidate_crosswalk(root,cid):
    docpath,covpath=find_spek(root)
    source=read_json(docpath);audit=read_json(covpath)
    if source.get('demonstration') is not True or source.get('source_verified') is not False:
        raise GateError('Statut Spek historique inattendu : une revue manuelle des métadonnées est requise')
    if audit.get('status')!='local_candidate_not_approved':
        raise GateError('Statut du rapport de couverture inattendu')
    sections={s['id']:s for s in source.get('sections',[]) if isinstance(s,dict)}
    refs=[]
    for w in audit.get('weeks',[]):
        goals=[g for g in w.get('goals',[]) if g.get('candidate_kristal_id')==cid]
        if goals:
            sid=w.get('id') or w.get('week_id') or (f"week-{w['week']}" if isinstance(w.get('week'),int) else None)
            if sid not in sections: # report older format may have `week` number
                sid=next((k for k in sections if any(g.get('goal_id') in str(sections[k]) for g in goals)),None)
            refs.append({'week':sid,'candidate_goals':[
                {'goal_id':g.get('goal_id'),'notion':g.get('notion'),
                 'status':g.get('status','candidate_requires_teacher_review')} for g in goals]})
    return {'course_id':cid,'spek_source':{'path':str(docpath.relative_to(root)), 'sha256':file_hash(docpath),
                        'demonstration':True,'source_verified':False},
            'spek_coverage':{'path':str(covpath.relative_to(root)),'sha256':file_hash(covpath),
                             'status':audit.get('status'),'gates':audit.get('gates')},
            'associations':refs,'conclusion':'Correspondances candidates, non validées pédagogiquement.'}
