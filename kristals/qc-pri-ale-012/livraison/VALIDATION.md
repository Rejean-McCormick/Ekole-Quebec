# Validation technique — `qc-pri-ale-012` (delta v1.2)

## Identification et périmètre

- ZIP demandé : `qc-pri-ale-012_livraison_v1.2.zip`.
- Racine interne : `kristals/qc-pri-ale-012/` ; seul ce Kristal est livré.
- **14 fichiers** : 2 remplacements `authoring/` et 12 nouveaux fichiers. Aucune modification de `ALIGNEMENT.md`, `AGENTS.md`, `kristal.workspace.json`, du graphe, des normes, d'autres ID ou du dépôt maître.
- Gouvernance : norme autonome v1.2; **PFEQ uniquement pour la nomenclature** ; aucune homologation revendiquée.

## Contrôles réellement exécutés, automatiquement

- Lecture de la frame v1.2 et comparaison **brute** de l'en-tête YAML : conservé à l'identique; les 12 sections Markdown attendues existent dans l'ordre et contiennent du texte.
- Parsing strict des deux JSON `authoring/CONTRAT_PEDAGOGIQUE.json` et `evaluation/BANQUE_ITEMS.json`, plus du manifeste; vérification des identifiants, de l'objectif observable, de la preuve, des champs natifs de famille, du `requires` unique `qc-pri-ale-011`, de l'absence d'ordre conseillé, des champs de famille requis par la gouvernance et de l'exactitude du manifeste.
- Banques : **12 items fixes**, IDs séquentiels sans doublons, `obj-1`, `crit-1`, famille `qc-pri-ale-012-ev-01`; champs obligatoires, consignes/stimuli/réponses/feedback non vides, niveaux reconnus, variations de réponses documentées, tous en `a_revoir`.
- Contenus : repérage des 2 exemples, 2 contre-exemples, `D1/D2`, `G1/G2/G3`, `A1/A2/A3/A4`, `T1/T2`, et présence des deux preuves de maîtrise `q-011/q-012` en contextes distincts.
- Liens : recherche automatisée des ID `qc-pri-*` utilisés; seuls l'ID cible et son unique prérequis apparaissent. Références source et aide d'accessibilité repérées textuellement.
- Traçabilité et droits : stimuli écrits originalement pour l'activité, pas d'image ou de texte tiers incorporé volontairement; audit juridique et plagiat non exécutés.
- Correcteurs : **pas de calcul numérique** à contrôler; modèles anglais relus pendant la rédaction pour leurs faits, ordre, accords de base et correspondance avec les brouillons. Les variantes linguistiques ne peuvent être garanties automatiquement; **aucun logiciel de correction grammaticale humain équivalent ni double correcteur** n'a été exécuté.

## Vérification finale du ZIP

- **Précontrôle automatisé : 206/206 vérifications réussies.**
- Archive construite uniquement à partir des 14 chemins du manifeste, sans arborescence englobante, sans autre ID ni fichier supplémentaire. Contrôle post-assemblage effectivement exécuté : **10/10 vérifications réussies** sur le ZIP (racine interne, ordre, nombre de fichiers, sûreté des chemins, intégrité CRC, parsage JSON et conformité du manifeste).

## Revue humaine obligatoire — éléments non qualifiés

- Réviser l'anglais, la précision de chaque proposition de correction, la voix des locuteurs, la qualité des 12 items et l'équité de la grille avec un enseignant et un réviseur linguistique.
- Vérifier les ambiguïtés volontairement non résolues (`it`, `she`, `them`) en administration, et éviter de donner le modèle avant les preuves.
- Calibrer les seuils avec des copies d'élèves et plusieurs correcteurs; vérifier le temps réel, les aménagements et la lecture assistée.
- Tester en contexte LMS la saisie des annotations et l'enregistrement des preuves, sans stocker de données de l'élève dans le canon.
- Une recherche de sources externes a été effectuée pour les principes généraux (Purdue OWL); **pas de test HTTP automatique des URL ni de vérification juridique des droits**.
- Les statuts des items restent `a_revoir` : aucune banque ni épreuve dite certifiée, homologuée ou publiée.

## Propositions (non appliquées) pour le mainteneur du workspace

- Ajouter plus tard un champ standardisé « aide_autorisee » au format d'épreuve, sans changer le registre maintenant.
- Harmoniser un statut technique unique pour les validations de contenu, distinct des rubriques humaines.
- Prévoir dans le LMS une annotation accessible par texte (sans code couleur obligatoire).
- Conserver la possibilité d'une question à l'auteur comme sortie valide lorsque le texte initial est factuellement sous-spécifié.
