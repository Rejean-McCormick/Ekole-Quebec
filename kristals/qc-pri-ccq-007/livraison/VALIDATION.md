# Validation et journal des modifications — `qc-pri-ccq-007`

## Statut

Contenus et épreuves rédigés; qualification pédagogique humaine requise. Aucune certification, publication, homologation ou conformité PFEQ revendiquée.

## Delta limité au périmètre

- **Remplacements complets de deux fichiers v1.2 :** `authoring/PARCOURS.md` (front matter préservé, douze sections développées) et `authoring/CONTRAT_PEDAGOGIQUE.json` (clés sources conservées, attributs de famille complétés).
- **12 ajouts :** six fichiers de contenu, trois d'évaluation, une bibliographie, un manifeste et cette validation.
- Aucune modification de `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, `AGENTS.md`, `kristal.workspace.json`, `canon/`, `docs/`, `state/`, `runtime/`, `registry/`, `governance/` ni d'un autre Kristal.

## Contrôles techniques exécutés

Le script local de contrôle a exécuté **294 assertions avec succès** avant fermeture de l’archive, dont :

- Concordance parfaite du front matter YAML avec le fichier source (identifiants, titre, objectif, préalable, famille, alignement, métadonnées conservées).
- Présence et ordre des **12 sections** de `authoring/PARCOURS.md`.
- Conservation de toutes les clés sources du contrat et des clés imbriquées de `generation` ; présence des **13 champs** exigés par `GENERATEUR_ET_EXAMENS.md`.
- Conformité du seul lien `requires` sortant vers `qc-pri-ccq-006` dans le graphe v1.2.
- JSON parsable, **10 items** avec IDs uniques `q-001` à `q-010`, famille `qc-pri-ccq-007-ev-01`, critère `crit-1`, corrigé et critères pour chacun.
- Vérification des deux preuves indépendantes `q-009` (bibliothèque fictive) et `q-010` (jardin fictif), dans deux contextes différents, reliées à la grille.
- Présence de deux exemples, deux contre-exemples, deux diagnostics, trois activités guidées, quatre pratiques autonomes et deux transferts.
- Manifeste de **14 chemins exacts**, avec deux recouvrements d'origine et douze chemins nouveaux, sans fichiers protégés.

**Portée des tests :** contrôles programmatiques de structure et de cohérence textuelle, **pas** évaluation de qualité culturelle auprès d'élèves ni validation de concordance intercorrecteurs. Une vérification d'intégrité CRC du ZIP et des chemins internes est ensuite exécutée au conditionnement.

## Limites et revue humaine

- Une relecture par des spécialistes de CCQ doit contrôler la nuance, l'absence de présupposés sur les identités, la progression et les consignes.
- Réaliser un essai d'âge approprié et d'accessibilité : compréhension du vocabulaire, durée, lisibilité et fidélité du mode audio.
- La grille n'est ni étalonnée ni évaluée par mesure de concordance entre correcteurs. Une double correction pilote est recommandée.
- La présence de deux tâches de maîtrise est vérifiée structurellement, **pas** une maîtrise réelle par des élèves.
- Les références UNESCO sont des ressources générales, pas une approbation de ce Kristal.

## Propositions de changement de structure (non appliquées)

1. Dans une prochaine version centrale, publier un schéma JSON des champs facultatifs de traçabilité des observations et des adaptations d'accessibilité.
2. Définir centralement un format de corpus fictif versionné et une méthode de double correction pilote, sans dépendance obligatoire pour le présent delta.
3. Conserver toute évolution de graphe ou de qualification dans un processus versionné distinct. Aucune proposition n'a été appliquée aux bases centrales.
