# Validation de livraison — `qc-pri-us-011`

**Statut :** rédaction complète, **banque à revoir**, pas de publication ni certification; les validations sont exclusivement celles réellement exécutées et enregistrées ici.

## Contenu de la livraison

- **2 remplacements** des `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json` préexistants, avec conservation des invariants identifiants, objectifs, preuve, liens et famille.
- **12 nouveaux fichiers** dans `contenu/`, `evaluation/`, `sources/`, `livraison/`.
- Aucun fichier du registre, de gouvernance, des autres Kristals ou des structures protégées n'est modifié ou inclus.

## Contrôles automatisés et résultats

- **573 assertions de préarchivage exécutées et réussies** avec `/mnt/data/verify_us011.py`; aucune erreur signalée. Contrôles : 14 chemins et 14 fichiers non vides, absence de placeholders, YAML conservant les champs canoniques et 12 sections, contrat natif enrichi sans perte de champs, JSON strict, 10 items uniques et numérotés, liens `obj-1`, `crit-1` et `qc-pri-us-011-ev-01`, deux contextes de maîtrise avec preuves distinctes.
- **Qualité des corrigés :** contrôle formel des 10 réponses, de l'association aux fiches S0–S4, de critères d'évaluation exploitables et du caractère déterministe des scénarios. Un jugement humain reste nécessaire sur l'argumentation et la justesse des inférences.
- **Vérification source/overlay :** seules les deux entrées authoring préexistantes sont remplacées; les 12 autres sont des ajouts. Le script simule la superposition au dossier local original du Kristal et vérifie par SHA-256 que ses autres fichiers sources restent inchangés. Les chemins de delta garantissent qu'aucun autre dossier du maître n'est écrasé.
- **Droits :** les pages institutionnelles S0–S4 ont été consultées et identifiées, et aucune archive, image, musique ni photographie tierce n'est incorporée. Aucune consultation juridique exhaustive entreprise.
- **Accessibilité :** critères et adaptations explicités dans les parcours, items, plan et grille; aucune observation d'accessibilité réelle effectuée.
- **Contrôle ZIP final :** nombre, ordre, arborescence, JSON, tailles et intégrité CRC testés après fabrication par le même script; le résultat effectif est affiché à l'exécution.

## Limites non résolues

- Les fiches S1–S4 sont des synthèses historiques institutionnelles reformulées, non des archives du XIXe siècle. L'attribution et l'absence de citations fabriquées doivent être revues par un spécialiste de l'histoire sociale.
- Aucun essai sur des élèves, aucune validation humaine des barèmes et des éventuels biais culturels, aucune étude psychométrique ni mesure de fiabilité intercorrecteurs.
- Aucun audit juridique exhaustif sur la réutilisation future de matériaux externes; aucun objet média externe intégré actuellement.
- La simplification des liens entre technologies, migrations, quartiers et inégalités comporte un risque d'attribution d'une cause unique; les réserves sont présentes mais à valider humainement.
- La maîtrise déclarée ici n'est pas une homologation PFEQ ni une certification scolaire.

## Revue humaine nécessaire

1. Relecture historique : faits, années, portée des fiches, risques d'anachronisme; contrôler S1–S4 et les différences entre lieux et périodes.
2. Relecture équité : récits des migrants, vie urbaine, travail et discriminations sans stéréotypes ni réduction abusive des expériences.
3. Évaluation : fidélité d'application des critères M1–M5, absence d'indices fournis en passation, autonomie et indépendance des deux preuves.
4. Accessibilité : lecteurs d'écran, compréhension des sources, formats de réponse adaptés et confidentialité des traces d'élèves.

## Propositions de structure, non appliquées

- Envisager une extension centrale versionnée `source_evidence_id` et `evidence_role` (fait / inférence / limite) pour éviter que des synthèses soient prises pour des sources primaires.
- Prévoir un catalogue central des scénarios historiques approuvés, versionnés et dotés d'une révision scientifique avant la génération encadrée.
- Ajouter au schéma de preuves des champs séparés pour les deux effets et leurs attributions, sous validation centrale future uniquement.
