#!/usr/bin/env python3
"""Vérification locale du dépôt nettoyé; Python standard, aucun accès réseau."""
from pathlib import Path
import hashlib
import json
import sys


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(root):
    pack=json.loads((root/'pack.json').read_text(encoding='utf-8'))
    expected=json.loads((root/'CONTROLE_COURS_SHA256.json').read_text(encoding='utf-8'))
    if len(pack['cours'])!=202 or len(pack['parcours'])!=6 or len(expected)!=202:
        raise ValueError('Catalogue des cours ou parcours incomplet')
    for name,value in expected.items():
        current=root/'cours'/name;original=root/'historique/clients/site/data/cours'/name
        if digest(current)!=value or digest(original)!=value:raise ValueError('Empreinte de cours différente : '+name)
    shared=json.loads((root/'outils/kristal-partage.json').read_text(encoding='utf-8'))
    source=root/shared['source']
    if digest(source)!=shared['source_sha256']:raise ValueError('Outil partagé modifié sans mise à jour de son épinglage')
    for name,value in shared['templates'].items():
        if digest(source.parent/'_templates'/name)!=value:raise ValueError('Modèle partagé modifié : '+name)
    if len(shared['entrypoints'])!=205 or len(set(shared['entrypoints']))!=205:raise ValueError('Liste des points d’entrée incohérente')
    for name in shared['entrypoints']:
        path=root/name
        if b'# ekole.shared-kristal/1' not in path.read_bytes()[:200]:raise ValueError('Point d’entrée absent : '+name)
        if (path.parent/'_templates').exists():raise ValueError('Modèles partagés répliqués : '+name)
    variant=shared['variant_preserved']
    if digest(root/variant['path'])!=variant['sha256']:raise ValueError('Variante autonome modifiée')
    for rel in ['historique/clients/site/eleve/spek-stage2/spek/fr/document.json','historique/clients/site/eleve/spek-stage2/reports/coverage.json']:
        if not (root/rel).is_file():raise ValueError('Source B2/Spek absente : '+rel)
    if not (root/'.gitattributes').is_file():raise ValueError('Configuration Git LFS absente')
    media=[]
    for path in root.rglob('*'):
        if path.is_file() and path.suffix.lower() in ('.png','.jpg','.jpeg','.webp','.gif','.avif','.tif','.tiff','.heic','.bmp','.psd','.xcf'):
            with path.open('rb') as f:head=f.read(128)
            if head.startswith(b'version https://git-lfs.github.com/spec/v1'):
                raise ValueError('Média non téléchargé : '+str(path.relative_to(root))+'; exécuter git lfs pull')
            media.append(path)
    return {'cours':202,'parcours':6,'points_entree_partages':205,'modeles_partages':len(shared['templates']),
            'variante_autonome_preservee':True,'medias_presents':len(media),'octets_medias':sum(p.stat().st_size for p in media)}

if __name__=='__main__':
    try:print(json.dumps(verify(Path(__file__).resolve().parents[1]),ensure_ascii=False,indent=2))
    except (ValueError,OSError,KeyError) as exc:
        print('Vérification refusée : '+str(exc),file=sys.stderr);raise SystemExit(1)
