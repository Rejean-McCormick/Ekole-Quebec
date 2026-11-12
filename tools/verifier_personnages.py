#!/usr/bin/env python3
"""Vérification locale des références des quatre dépôts, sans génération d'images."""
from pathlib import Path
import argparse
import json
import sys


def verify(root, require_images=False):
    parent=root.parent
    sys.path.insert(0,str(parent/'ekole'))
    sys.path.insert(0,str(parent/'Kontexte/src'))
    import personnages
    from kontexte.models import validate_role
    pack=json.loads((root/'pack.json').read_text(encoding='utf-8-sig'))
    loaded=personnages.load(root,pack)
    if loaded is None:raise ValueError('Catalogue personnages non déclaré dans pack.json')
    folder,data=loaded;assets={a['id']:a for a in data['assets']}
    roles=[]
    for p in sorted((parent/'Kontexte/data/roles').glob('*.json')):
        role=validate_role(json.loads(p.read_text(encoding='utf-8')))
        if role.get('visual_id')!='role-'+role['id']:raise ValueError('Référence visuelle absente : '+role['id'])
        roles.append(role)
    if not roles:raise ValueError('Catalogue Kontexte absent')
    if {r['visual_id'] for r in roles}!={a['id'] for a in assets.values() if a['type']=='role'}:
        raise ValueError('Rôles Kontexte et catalogue visuel différents')
    for r in roles:
        if assets[r['visual_id']]['role_id']!=r['id']:raise ValueError('Association de rôle incohérente')
    refs=[]
    for p in sorted((parent/'Ekole_Avatars_Decoupes/plans').glob('*.json')):
        plan=json.loads(p.read_text(encoding='utf-8'))
        if plan.get('format')!='ekole.planche/1':raise ValueError('Format de plan invalide')
        for item in plan['images']:
            aid=item['visual_id'];refs.append(aid)
            if aid not in assets or item['fichier']!=assets[aid]['fichier']:raise ValueError('Plan désaligné : '+str(p))
    if set(refs)!=set(assets) or len(refs)!=len(set(refs)):
        raise ValueError('Plans incomplets ou références dupliquées; relancer decouper.py --preparer')
    public=personnages.public_inventory(loaded);ready=sum(a['disponible'] for a in public['assets'])
    if require_images and ready!=len(assets):raise ValueError(f'{len(assets)-ready} images absentes ou non prêtes')
    return {'compagnons':len(data['compagnons']),'roles':len(roles),'images_prevues':len(assets),'images_pretes':ready,'references_de_decoupe':len(refs)}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--exiger-images',action='store_true');args=parser.parse_args()
    try:print(json.dumps(verify(Path(__file__).resolve().parents[1],args.exiger_images),ensure_ascii=False,indent=2))
    except (ValueError,OSError,KeyError,ImportError) as exc:parser.exit(1,'Alignement invalide : '+str(exc)+'\n')
