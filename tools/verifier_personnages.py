#!/usr/bin/env python3
"""Vérifie le contrat du catalogue Ékole Québec, sans appel d'IA ni images fictives."""
from pathlib import Path
import argparse
import json
import sys


def verify(root: Path, require_images=False):
    parent = root.parent
    sys.path.insert(0, str(parent/'ekole'))
    import personnages
    pack = json.loads((root/'pack.json').read_text(encoding='utf-8-sig'))
    loaded = personnages.load(root, pack)
    if loaded is None:
        raise ValueError('Catalogue personnages non déclaré')
    folder, cat = loaded
    if cat['format'] != 'ekole.personnages/4':
        raise ValueError('Le pack doit utiliser ekole.personnages/4')
    roles={a['role_id'] for a in cat['assets'] if a['type']=='role'}
    if {c['role_id'] for c in cat['compagnons']} != roles:
        raise ValueError('Les 38 compagnons-rôles ne correspondent pas aux rôles')
    if len(roles) != 38 or len(cat['compagnons']) != 380 or len(cat['poses']) != 8 or len(cat['assets']) != len(roles)*2*5*len(cat['poses']):
        raise ValueError('Couverture 38 rôles × 8 poses incomplète')
    # Kontexte est un dépôt voisin optionnel : vérifier l’alignement si disponible.
    role_dir=parent/'Kontexte/data/roles'
    external=[]
    if role_dir.is_dir():
        for p in sorted(role_dir.glob('*.json')):
            info=json.loads(p.read_text(encoding='utf-8'))
            if isinstance(info,dict) and 'id' in info:
                if info.get('visual_id') != 'role-'+info['id']:
                    raise ValueError('Contrat Kontexte incohérent : '+info['id'])
                external.append(info['id'])
        if external and set(external)!=roles:
            raise ValueError('Liste de rôles divergente du dépôt Kontexte voisin')
    public=personnages.public_inventory(loaded)
    ready=sum(a['disponible'] for a in public['assets'])
    if require_images and ready != len(cat['assets']):
        raise ValueError(f'{len(cat["assets"])-ready} images absentes ou non prêtes')
    return {'format':cat['format'], 'roles':len(roles), 'compagnons':len(cat['compagnons']), 'genres_par_role':2, 'origines_par_genre':5, 'poses_par_personnage':len(cat['poses']),
            'images_prevues':len(cat['assets']), 'images_pretes':ready,
            'kontexte_verifie':bool(external)}


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--exiger-images',action='store_true')
    args=ap.parse_args()
    try:
        print(json.dumps(verify(Path(__file__).resolve().parents[1],args.exiger_images),ensure_ascii=False,indent=2))
    except (ValueError,OSError,KeyError,ImportError) as exc:
        ap.exit(1,'Vérification invalide : '+str(exc)+'\n')
