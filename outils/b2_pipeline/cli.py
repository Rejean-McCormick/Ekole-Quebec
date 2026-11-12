"""CLI stdlib: inspect, create a private draft, validate, review, publish or Spek preview."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from .core import (GateError, atomic_json, read_json, source_info, source_scaffold,
                   validate_draft, review_receipt, publish)
from .pilot import curated_multiplication
from .spek_bridge import educational_preview
from .spek_source import candidate_crosswalk


def parser_create():
    p=argparse.ArgumentParser(prog='python -m b2_pipeline',description='B2: édition et publication Élève contrôlées')
    p.add_argument('--source',type=Path,required=True,help='Dépôt source Ekole/Québec, lecture seule')
    p.add_argument('--work',type=Path,required=True,help='Espace privé pour les brouillons et validations')
    p.add_argument('--course',default='qc-pri-ma-008',help='Identifiant du cours, par défaut le pilote')
    subs=p.add_subparsers(dest='command',required=True)
    subs.add_parser('inspect',help='Lire les sources et signaler le statut de validation')
    subs.add_parser('spek-audit',help='Lister les correspondances Spek historiques non validées')
    subs.add_parser('scaffold',help='Créer un brouillon à rédiger, jamais public')
    subs.add_parser('pilot',help='Créer le pilote éditorial de multiplication NON approuvé')
    subs.add_parser('validate',help='Contrôler le brouillon sans le publier')
    review=subs.add_parser('review',help='Signer une revue locale déclarative')
    review.add_argument('--reviewer',required=True)
    review.add_argument('--statement',required=True)
    review.add_argument('--acknowledge-unverified',action='store_true')
    spek=subs.add_parser('spek-preview',help='Générer une projection Spek local preview uniquement')
    spek.add_argument('--out',type=Path,required=True)
    publication=subs.add_parser('publish',help='Exporter vers les publications Élève v3')
    publication.add_argument('--out-root',type=Path,required=True)
    publication.add_argument('--apply',action='store_true',help='Écrire réellement, sinon afficher un diagnostic')
    publication.add_argument('--replace',action='store_true')
    return p


def main(argv=None):
    args=parser_create().parse_args(argv)
    try:
        source_root=args.source.resolve()
        work=args.work.resolve()
        # Les brouillons et attestations de relecture contiennent des données
        # privées. Ils ne doivent jamais être écrits dans le dépôt de contenu,
        # même si --work désigne un sous-dossier inexistant ou un lien symbolique.
        if work == source_root or work.is_relative_to(source_root):
            raise GateError('Espace --work interdit dans le dépôt source : choisissez un dossier privé séparé')
        source=source_info(source_root,args.course)
        draft_path=work/'brouillons'/(args.course+'.json')
        if args.command=='inspect':
            print(json.dumps({'course_id':args.course,'titre':source['course']['titre'],
                              'objectif_expert':source['contract'].get('objectif_observable'),
                              'validation_source':source['contract'].get('statut'),
                              'source_provenance':source['hashes']},ensure_ascii=False,indent=2))
            return 0
        if args.command=='spek-audit':
            print(json.dumps(candidate_crosswalk(args.source,args.course),ensure_ascii=False,indent=2))
            return 0
        if args.command in ('pilot','scaffold'):
            if draft_path.exists():raise GateError('Brouillon déjà présent : aucun écrasement implicite')
            draft=curated_multiplication(source) if args.command=='pilot' else source_scaffold(source,args.course)
            validate_draft(draft,source,complete=args.command=='pilot')
            atomic_json(draft_path,draft)
            print('Brouillon privé créé :',draft_path)
            return 0
        draft=read_json(draft_path)
        validate_draft(draft,source)
        if args.command=='validate':
            print('STRUCTURE VALIDE — aucune validation pédagogique automatiquement accordée')
        elif args.command=='review':
            receipt=review_receipt(draft,args.reviewer,args.statement,source,args.acknowledge_unverified)
            review_path=work/'revues'/(args.course+'.json')
            atomic_json(review_path,receipt)
            print('Revue déclarative locale enregistrée :',review_path)
        elif args.command=='spek-preview':
            projection=educational_preview(draft,source)
            target=args.out.resolve()
            if target.is_relative_to(args.source.resolve()):raise GateError('Écrire les aperçus Spek hors du dépôt source')
            atomic_json(target,projection)
            print('Projection Spek LOCAL DEMO seulement :',target)
        elif args.command=='publish':
            out=args.out_root.resolve()
            if out==args.source.resolve() or out.is_relative_to(args.source.resolve()):
                raise GateError('Publication dans la source de référence interdite pour cette branche')
            result=publish(args.source,work,args.course,out,apply=args.apply,replace=args.replace)
            print(('Publié sur copie : ' if args.apply else 'Publication possible après revue (DRY RUN) : '),
                  args.course,'modules',len(result['modules']))
        return 0
    except (GateError,FileNotFoundError,ValueError,json.JSONDecodeError) as exc:
        print('B2 REFUSÉ :',str(exc),file=sys.stderr)
        return 2
