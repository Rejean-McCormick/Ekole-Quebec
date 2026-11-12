# Validation réelle et limites — `qc-pri-ma-031` (2026-10-08)

## Périmètre et sources

Source utilisée : archive maîtresse `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` disponible dans `initbundle(1).zip`. Fichiers de gouvernance, graphe et quatre fichiers source de `qc-pri-ma-031` lus avant création. Conformité PFEQ non évaluée ni revendiquée.

## Contrôles effectués automatiquement avant empaquetage

- **75 assertions réussies** avant fermeture ZIP, incluant parsing JSON strict, parsing YAML, conservation de l'identité et des métadonnées v1.2, graphe, conformité des familles, identifiants, deux manifestations de maîtrise, cohérence des plans et structure du manifeste.
- **12 variantes paramétriques** testées exhaustivement (4 items × 3 variantes) : domaines, divisibilité par l'échelle, hauteurs, totaux, correction des fausses phrases et contenu des corrigés. Sélection reproductible par index = seed mod 3; aucun tirage aléatoire externe.
- **5 tableaux fixes** recalculés pour leurs totaux; erreur de graduation examinée. La qualité linguistique et l'absence de variantes ambiguës requièrent toujours une revue humaine.
- **12 sections pédagogiques** repérées dans l'ordre original; 2 diagnostics, 3 guidés, 4 autonomes et 2 transferts présents; 10 items numérotés distincts.

## Vérifications spécifiques après construction du ZIP

Les contrôles de chemin unique, CRC, absence de contenu vide, fichiers exactement attendus, absence de chemins absolus ou `../`, manifeste, JSON et conservation des fichiers protégés sont exécutés après le premier empaquetage. Leur résultat final est inscrit ci-dessous par le script de construction.

## Limites non résolues

- Aucune expérimentation avec des élèves, aucune mesure de durée réelle ou fidélité intercorrecteurs.
- Aucun support graphique illustré fourni : les modèles sont textuels ou à tracer, avec alternatives tactiles proposées, mais leur mise en oeuvre doit être vérifiée.
- Les variantes ont des corrigés arithmétiques calculables; cela ne suffit pas à valider les inférences et rubriques sans revue experte.
- Le niveau d'âge, l'équité des contextes et la conformité réelle aux besoins d'accessibilité exigent une validation humaine.
- Les URLs de référence ont été consultées; le statut des droits externes n'est pas certifié, et aucune image/texte externe n'a été reproduit.

## Revue humaine indispensable

Valider la clarté des tableaux et axes, la pertinence des échelles 1/2, la distinction entre critique locale et généralisation, la faisabilité des adaptations, la décision non compensatoire de maîtrise et la concordance avec les contraintes de publication du système Kristal.

## Proposition hors périmètre, non appliquée

Envisager dans une future mise à jour de gouvernance un schéma JSON formalisant `variantes_catalogue`, le couple `(seed,index)`, la table des réponses acceptées et la traçabilité des accommodations; aucune modification de `registry/`, `governance/`, autres Kristals ou métadonnées centrales n'a été faite.


## Contrôles de l’archive terminée

**86 assertions réussies** (y compris contrôles ZIP), **12 variantes finies** vérifiées, **14 fichiers**, **2 remplacements**, **12 ajouts**, **0 fichier protégé inclus**. Tous les JSON embarqués sont analysables; CRC sans erreur.

## Statut

**Contrôlé techniquement, à revoir humainement, non certifié, non publié, non homologué.**
