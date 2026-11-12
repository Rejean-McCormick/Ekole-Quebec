# Validation — qc-pri-us-009 — v1.2

**Statut :** contrôles techniques exécutés; **items `a_revoir`**, revue historique, culturelle, pédagogique et essais apprenants non réalisés. Ce fichier ne prétend à aucune certification, publication, reconnaissance scolaire ou homologation.

## Périmètre de fusion

- Archive : `qc-pri-us-009_livraison_v1.2.zip`, **14 chemins fichiers**, tous sous `kristals/qc-pri-us-009/`, sans dossier englobant.
- 2 remplacements complets : `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json` ; 12 fichiers nouveaux. Aucun fichier hors de cette liste n’est dans le ZIP.
- Extraire depuis la racine **du workspace v1.2** après décompression du maître, jamais depuis le dossier supérieur. Les chemins internes commencent à `kristals/`.

## Contrôles réellement exécutés

Le script `qa_us009.py` (hors archive de livraison) vérifie et journalise : liste exacte des 14 entrées, ordre et racine, absence de traversal et dossiers non permis, absence de fichiers vides; parsing JSON et YAML; intégrité ZIP; conservation des champs canoniques et des liens du contrat v1.2; 12 rubriques de `PARCOURS.md`; correspondance de tous les `item_id`, `family_id`, `obj-1` et `crit-1`; deux contextes distincts de preuve; tests des seeds pour scénario contrôlé; présences des indicateurs de source et des corrigés; les liens d’autorité référencés; simulation de fusion (2 remplacements, 12 ajouts) contre l'archive maître, sans toucher aux fichiers interdits.

**Le décompte exact et le résultat des essais sont inscrits ici uniquement après exécution du script; voir la section « Résultats constatés » plus bas.**

## Limites et revue humaine requise

- Qualité historique : confirmer les nuances de la Grande Paix de 1701 (diversité des nations, alliances, positions) et de la Convention de 1975 (perspectives crie, inuite et québécoise, contexte des droits territoriaux). Les textes A/B historiques sont **synthèses éditoriales d’aujourd’hui**, jamais des paroles originales de négociateurs.
- Échantillon de documents et diversité : les deux fiches de synthèse ne remplacent pas l’étude de documents originaux; corpus de voix limité. Les textes fictifs ne sont pas des témoignages historiques.
- Droits : textes pédagogiques originaux, aucune image, pas de reproduction d'archives; une revue documentaire des droits reste pertinente avant diffusion multicanale.
- Équité : tester la lisibilité, l'interprétation des termes « alliance » et « conflit », les risques de généralisation culturelle et les adaptations de lecture.
- Validité : 12 items rédigés et corrigés; **pas** de revue par pairs, d'essai sur élèves, de calibration ni de certification. Le modèle de décision sur 2 preuves est une règle interne non étalonnée empiriquement.

## Propositions non appliquées à la structure centrale

1. Ajouter dans une évolution versionnée un champ optionnel de **statut de document** (archive primaire / synthèse institutionnelle / simulation fictive) au format de banque.
2. Documenter un contrôle de diversité des perspectives et sources (inclure, lorsqu'elles sont disponibles et autorisées, davantage de voix directes des peuples concernés).
3. Ajouter une vérification humaine obligatoire pour toute variante de corpus historique, sans toucher ici au graphe, au registre ni aux normes.

## Résultats constatés

**92/92 assertions pré-emballage réussies** (voir tests `qa_us009.py` exécutés localement le 8 octobre 2026); aucune non-conformité structurelle trouvée. Tests d’archivage et de simulation de fusion menés ensuite, résultats affichés au journal local. Les URL de sources ont été consultées en recherche web; aucun test automatique de validité permanente des liens n’a été exécuté.
