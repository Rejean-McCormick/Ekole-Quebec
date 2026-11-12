"""B2 – editorial transformation boundary; no AI generation or external requests.

Inputs remain expert/private. A public lesson is generated only from a separately
curated student draft with explicit review, never from raw Kristal Markdown.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import secrets
from pathlib import Path

FORMAT = 'ekole.b2.student-draft/1'
REVIEW_FORMAT = 'ekole.b2.editorial-review/1'
PUBLIC_FORMAT = 'ekole.student-publication/1'
STEP_TYPES = {'decouvrir', 'essayer', 'comprendre', 'pratiquer', 'creer', 'reflechir'}
BLOCK_TYPES = {'explanation', 'instruction', 'challenge', 'hint', 'reflection'}
PUBLIC_STATUSES = {'pilote_a_valider'}
PRIVATE_FIELDS = {'answer', 'solution', 'correct_answer', 'rubric', 'teacher_note', 'answer_key',
                  'barème', 'corrige', 'corrigé', 'diagnostic', 'responses', 'grading'}
# Heuristic guard only; not a substitute for editorial review.
SENSITIVE_PATTERNS = [
    r'qc-pri-[a-z]{2,4}-\d{3}', r'sans note certificative', r'préalable interne',
    r'réponse\s+et\s+critères', r'critères?\s+de\s+réussite', r'barème\s*:',
    r'corrigé\s*:', r'pour\s+l[’\']enseignant', r'usage\s*:\s*avant\s+la\s+leçon',
    r'protocole\s+d[’\']évaluation', r'réponse\s+attendue\s*:',
    r'accept(?:er|é|ée)\s+un\s+schéma', r'solution\s*:', r'correction\s*:',
]
SOURCE_FILES = {'course': ('cours/{cid}.json', 'site/data/cours/{cid}.json'),
                'contract': ('kristals/{cid}/authoring/CONTRAT_PEDAGOGIQUE.json',)}


class GateError(ValueError):
    pass


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def digest_object(value) -> str:
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(',', ':')).encode('utf-8')).hexdigest()


def read_json(path: Path):
    if path.is_symlink() or not path.is_file():
        raise GateError(f'Fichier indisponible ou lien symbolique interdit : {path}')
    return json.loads(path.read_text(encoding='utf-8-sig'))


def safe_id(cid: str) -> str:
    if not isinstance(cid, str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,90}', cid):
        raise GateError('Identifiant de cours non conforme')
    return cid


def source_info(root: Path, cid: str):
    cid = safe_id(cid)
    root = root.resolve()
    located = {}
    for key, variants in SOURCE_FILES.items():
        for pattern in variants:
            path = root / pattern.format(cid=cid)
            if path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(root):
                located[key] = path
                break
        if key not in located:
            raise GateError(f'Source manquante : {key} pour {cid}')
    contents = {key: path.read_bytes() for key, path in located.items()}
    course = json.loads(contents['course'].decode('utf-8-sig'))
    contract = json.loads(contents['contract'].decode('utf-8-sig'))
    if course.get('id') != cid or contract.get('kristal_id') != cid:
        raise GateError('Références source incompatibles')
    if not isinstance(course.get('modules'), list) or len(course['modules']) != 6:
        raise GateError('Attendu : six modules du cours de référence')
    hashes = {key: {'path':str(path.relative_to(root)).replace('\\','/'), 'sha256':hashlib.sha256(contents[key]).hexdigest()}
              for key,path in located.items()}
    return {'course': course, 'contract': contract, 'hashes': hashes}


def atomic_json(path: Path, data):
    if path.exists() or path.is_symlink():
        if path.is_symlink(): raise GateError('Écriture vers un lien symbolique interdite')
    path.parent.mkdir(parents=True, exist_ok=True)
    name = path.with_name(path.name + '.tmp-' + secrets.token_hex(6))
    try:
        with name.open('x', encoding='utf-8', newline='\n') as stream:
            json.dump(data, stream, ensure_ascii=False, indent=2)
            stream.write('\n')
        os.replace(name, path)
    finally:
        name.unlink(missing_ok=True)


def source_scaffold(source, cid: str):
    course, contract = source['course'],source['contract']
    return {
        'format': FORMAT, 'course_id': cid, 'titre': course['titre'],
        'language': 'fr-CA', 'audience':'student', 'grade': source.get('grade', 3),
        'editorial_status':'draft',
        'source_provenance': source['hashes'],
        'teacher_brief': {
            'objectif_observable': contract.get('objectif_observable',''),
            'preuve_attendue':contract.get('preuve_attendue',''),
            'sources_reviewed':False,
            'remarque':'Réservé à l’enseignant. Ne jamais publier ce champ.',
        },
        'modules':[
            {'id':m['id'], 'kind': kind, 'titre':'À rédiger pour l’enfant',
             'blocks':[{'type':'instruction','text':'À rédiger et relire avec un enseignant.'}]}
            for m,kind in zip(course['modules'],STEP_TYPES_ORDER)
        ],
        'spek_candidate': None,
    }


STEP_TYPES_ORDER=('decouvrir','essayer','comprendre','pratiquer','creer','reflechir')


def validate_draft(doc, source, complete=True):
    if not isinstance(doc,dict) or doc.get('format')!=FORMAT:raise GateError('Format brouillon inconnu')
    if set(doc)-{'format','course_id','titre','language','audience','grade','editorial_status',
                 'source_provenance','teacher_brief','modules','spek_candidate'}:
        raise GateError('Champ non déclaré dans le brouillon')
    if doc.get('course_id') != source['course']['id']: raise GateError('Mauvais identifiant cours')
    if doc.get('language')!='fr-CA' or doc.get('audience')!='student' or doc.get('grade')!=source.get('grade', 3):
        raise GateError('Audience, langue ou niveau incompatibles')
    if doc.get('editorial_status')!='draft':raise GateError('Un brouillon ne certifie aucune publication')
    if doc.get('source_provenance') != source['hashes']:
        raise GateError('Source du Kristal modifiée : réaligner le brouillon avant revue')
    if not isinstance(doc.get('modules'),list) or len(doc['modules'])!=6:
        raise GateError('Six étapes sont requises')
    for i,(module,original) in enumerate(zip(doc['modules'],source['course']['modules'])):
        if set(module) != {'id','kind','titre','blocks'} or module['id'] != original['id'] or module['kind'] != STEP_TYPES_ORDER[i]:
            raise GateError(f'Structure du module {i+1} incompatible')
        title = module['titre']
        if not isinstance(title,str) or not (1<=len(title.strip())<=90):raise GateError('Titre de longueur invalide')
        blocks=module['blocks']
        if not isinstance(blocks,list) or not 1<=len(blocks)<=7:raise GateError('Nombre de blocs invalide')
        for b in blocks:
            if not isinstance(b,dict) or set(b) != {'type','text'} or b['type'] not in BLOCK_TYPES:
                raise GateError('Bloc non autorisé ou champs additionnels interdits')
            t=b['text']
            if not isinstance(t,str) or not 1<=len(t.strip())<=800:
                raise GateError('Texte de bloc vide ou trop long (800 caractères maximum)')
            if complete and ('à rédiger' in t.lower() or 'à rédiger' in title.lower()):
                raise GateError('Brouillon non finalisé')
            if re.search(r'<[^>]+>|!\[|\]\(\s*(?:https?://|/)',t):
                raise GateError('HTML, images Markdown et liens non revus interdits dans le pilote')
            if any(re.search(pattern,t,flags=re.I) for pattern in SENSITIVE_PATTERNS):
                raise GateError('Signal de texte enseignant ou identifiant interne dans la version élève')
        if any(re.search(pattern,title,flags=re.I) for pattern in SENSITIVE_PATTERNS):
            raise GateError('Titre contenant une référence experte')
    if not isinstance(doc.get('teacher_brief'),dict):raise GateError('Notes enseignant requises dans le brouillon privé')
    if doc.get('spek_candidate') is not None and not isinstance(doc['spek_candidate'],dict):
        raise GateError('Référence Spek invalide')
    return True


def student_publication(draft, source):
    validate_draft(draft,source)
    modules=[]
    for item in draft['modules']:
        # whitelist stricte; teacher_brief/source_provenance/spek_candidate jamais exportés
        paragraphs=[]
        for block in item['blocks']:
            heading={'explanation':'Je découvre','instruction':'À toi de jouer',
                     'challenge':'Mon défi','hint':'Un petit indice','reflection':'Je réfléchis'}[block['type']]
            paragraphs.append('### '+heading+'\n\n'+block['text'])
        modules.append({'id':item['id'],'titre':item['titre'],'texte':'\n\n'.join(paragraphs)})
    return {'format':PUBLIC_FORMAT,'id':draft['course_id'],'titre':draft['titre'],
            'statut_publication':'pilote_a_valider',
            'notice':'Parcours Élève pilote, relu localement. Validation pédagogique institutionnelle non attestée.',
            'modules':modules}


def review_receipt(draft, reviewer: str, statement: str, source, acknowledge_unverified: bool):
    validate_draft(draft,source)
    if not isinstance(reviewer,str) or len(reviewer.strip())<3:raise GateError('Identité du relecteur nécessaire')
    if statement!='Je confirme avoir relu tout le contenu élève et vérifié les corrigés et données privées.':
        raise GateError('Confirmation éditoriale explicite obligatoire')
    if not acknowledge_unverified:
        raise GateError('Le Kristal et Spek sont des candidats non certifiés. Reconnaissance explicite requise.')
    return {'format':REVIEW_FORMAT,'course_id':draft['course_id'],'status':'reviewed_for_local_pilot_only',
            'reviewer':reviewer.strip(),'declaration':statement,'qualified_source_status':
            source['contract'].get('statut','inconnu'), 'source_provenance':source['hashes'],
            'draft_sha256':digest_object(draft), 'warning':'Attestation déclarative locale : ne vaut ni autorité, ni conformité, ni certification officielle.'}


def publish(root: Path, workspace: Path, cid: str, destination: Path, apply: bool, replace=False):
    src=source_info(root,cid)
    doc=read_json(workspace/'brouillons'/(cid+'.json'))
    review=read_json(workspace/'revues'/(cid+'.json'))
    expected=review.get('draft_sha256')
    if review.get('format')!=REVIEW_FORMAT or review.get('status')!='reviewed_for_local_pilot_only':
        raise GateError('Revue éditoriale explicite absente')
    if expected != digest_object(doc) or review.get('source_provenance') != src['hashes']:
        raise GateError('La revue ne correspond plus au brouillon ou aux sources')
    public=student_publication(doc,src)
    destination=destination.resolve()
    target=destination/'publications'/'eleve'/(cid+'.json')
    if target.exists() and not replace and apply:raise GateError('Fichier public déjà présent : --replace requis')
    if apply:
        if not target.parent.resolve().is_relative_to(destination):
            raise GateError('Dossier de publication sortant de la copie cible')
        if target.is_symlink():raise GateError('Lien symbolique de publication interdit')
        if target.exists():
            backup=workspace/'sauvegardes'/(cid+'-'+secrets.token_hex(6)+'.json')
            atomic_json(backup,read_json(target))
        atomic_json(target,public)
        # La traçabilité reste PRIVÉE, hors chemin statique public.
        audit=workspace/'audits'/(cid+'.json')
        atomic_json(audit,{'course_id':cid,'source':src['hashes'],'review_digest':digest_object(review),
                           'publication_sha256':file_hash(target),'status':'local_pilot_only'})
    return public
