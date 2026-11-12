# Validation — `qc-pri-st-014`

**Statut :** rédaction complète, banque d'items à revoir; qualification pédagogique et scientifique humaine requise, aucune homologation PFEQ. Ce rapport distingue les vérifications informatiques de la réalité terrain.

## Étendue de la livraison

Les deux documents `authoring/` sont des remplacements complets avec identifiants, objectifs, liens et famille v1.2 conservés; 12 autres fichiers sont ajoutés. Aucune modification du `registry/`, des `governance/`, des `docs/`, du `canon/`, de `state/`, de `runtime/`, de `AGENTS.md`, `kristal.workspace.json` ou d'un autre Kristal.

## Contrôles réalisés

- **509 assertions préarchivage réussies**, script Python réellement exécuté sur la livraison et la source maîtresse.
- Les fichiers YAML et JSON ont été parsés; **frontmatter du PARCOURS.md identique octet pour octet à la source** et ses 12 sections conservées et remplies.
- Tous les invariants du contrat ont été comparés à la source; 1 famille native préservée et enrichie; `requires` et `recommends_before` recoupés avec le graphe.
- Banque de 10 items à champs complets et identifiants uniques. Les 8 items fixes ont des paramètres/graines `null`. Les 2 scénarios fermés de maîtrise ont des graines stables 14009 et 14010, une seule entrée admissible par catalogue et une sélection calculée `seed % 1 = 0`.
- Corrigés scientifiques relus par contrôle de correspondance des termes, états et flèches **documenté dans la banque**, sans protocole de validation terrain ni contrôle automatisé exhaustif de toutes réponses ouvertes. Les consignes, critères et rétroactions sont présents et inspectés.
- Sécurité, accessibilité, références factuelles externes, droits et deux contextes de maîtrise vérifiés au niveau documentaire.
- Fusion réelle simulée **dans un répertoire temporaire** en partant des fichiers sources du Kristal : 2 remplacements, 12 ajouts; les autres fichiers sources restent strictement identiques.
- Après archivage : vérification ZIP de 14 chemins, non vides, sans chemin absolu/traversée, CRC via `testzip()`, JSON relus dans le ZIP et manifeste concordant.


## Non résolu / limites

- Aucun essai en classe, aucune revue interévaluateurs et aucun étalonnage des seuils M1–M5.
- L'explication du nuage et de la neige est volontairement simplifiée; revue scientifique pour éviter les généralisations abusives selon le niveau scolaire.
- Les représentations alternatives (tactile, dictée, audio) restent à vérifier avec des personnes ayant des besoins d'accès particuliers.
- Aucune manipulation de chaleur, rive ou matériel dangereux testée; les activités proposées n'en nécessitent pas.
- Les sources externes ont été vérifiées pour les mécanismes, pas pour valider un programme scolaire précis ni pour autoriser la reproduction de leurs images.

## Revue humaine avant décision ou publication

1. Vérifier exactitude de chaque flèche, distinction condensation/précipitation et cas de neige ou d'infiltration.
2. Faire relire les consignes, variantes d'accès et durées par un enseignant de science au primaire.
3. Contrôler la constance de cotation M1–M5 sur deux productions autonomes inédites.
4. Vérifier les droits de toute future illustration ou ressource externe et la protection des données d'élèves.

## Propositions de structure, sans édition des bases centrales

- Introduire à l'avenir un schéma commun de graphe de processus (`source`, `destination`, `état_initial`, `état_final`, `type_flux`) vérifiable automatiquement dans les items de science; proposition à transmettre au mainteneur, pas de modification du registre.
- Rendre explicite dans une prochaine évolution du contrat de famille la distinction entre `catalogue fermé` et `générateur paramétrique`, avec vérification du corrigé après variation.
- Prévoir une grille type de schémas tactiles et d'annotation non directive afin de documenter l'équivalence des preuves accessibles.
