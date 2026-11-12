# Rapport d'alignement — Ekole / Kristal polymorphe / Moodle

Date de préparation : 2026-10-09

## Résultat de l'audit hors ligne

| Contrôle | Résultat |
| --- | ---: |
| Workspaces pédagogiques Kristal | 202 |
| États auteur de type `stub` | 202 |
| Formes natives `undecided` | 202 |
| Éléments en banques pédagogiques | 2 183 |
| Familles `observation_ou_production` | 93 |
| Familles `réponse_argumentée` | 40 |
| Familles `paramétrique_controle` | 33 |
| Familles `generee_sous_contraintes` | 36 |
| Relations `requires` | 134 |
| Relations `recommends_before` | 99 |
| Relations `reinforces` | 19 |
| Correspondances vers de vrais IDs Moodle renseignées | 0 |
| Cours Moodle créés par cette opération | 0 |
| Évaluations Moodle créées par cette opération | 0 |
| États v9 qualifiés par cette opération | 0 |

## Contrôles exécutés

- `python tools/ekole.py verify` : **PASS**, 3 104 vérifications, 202 Kristals, 2 183 items.
- `python tools/ekole.py moodle-plan` : **PASS**, sortie `plans/moodle_projection_dry_run.json`.
- `python -m unittest discover -s tests -v` : **PASS**, 13 tests, dont multi-projection et rejet d'écritures non autorisées.
- Contrat `moodle/contracts/kristal-moodle-projection.schema.json` : **PASS** (JSON Schema 2020-12).
- `php -l` sur le lecteur `local_uckk` candidat : **PASS** ; lecture PHP du plan : **PASS** (202 Kristals, 252 relations).
- `kristals(10).zip` : 2 828 fichiers non-répertoires, identiques aux mêmes chemins dans le pack Ekole fourni (aucune différence de bytes).

## Principe conservé

Kristal reste la source de vérité de son identité et de sa forme native. Les catégories, sections et activités Moodle sont des matérialisations applicatives dérivées. Une projection peut être multiple (0..n) ; un cours peut agréger plusieurs sources Kristal. Aucune décision de cours, année, type d'évaluation, statut d'autorité ou verrou d'accès n'est imposée par le pont.

## Fichiers nouveaux/modifiés

- `tools/kristal_moodle_bridge.py` : générateur/auditeur polymorphe hors ligne.
- `tools/ekole.py` : `moodle-plan` relié au générateur polymorphe.
- `plans/moodle_projection_dry_run.json` : plan candidat avec `state_ref`, formes ouvertes, SHA des fichiers, 202 fiches et graphe.
- `moodle/contracts/` : exemples de bindings et schéma du plan.
- `moodle/local_uckk_candidate/...` : lecteur PHP à intégrer après revue dans le `local_uckk` existant.
- `tests/test_kristal_moodle_bridge.py` : tests automatiques.
- `docs/05_MOODLE_MAP.md`, `docs/09_KRISTAL_MOODLE_POLYMORPHE.md`, présent rapport et `README.md` mis à jour.

## Ce qui reste hors du périmètre

Ni ce pack ni son lecteur PHP ne disposent d'une connexion active au Moodle déployé. Il n'existe donc pas de `courseid/categoryid` avérés pour Ekole, ni d'installation effective dans `local_uckk`, ni de conversion certifiée des banques de questions. Les formes natives `undecided` n'ont pas été artificiellement « cristallisées ». Les contrôles pédagogiques, sécurité enfant, accessibilité et qualification Kristal v9/v10 restent nécessaires avant toute publication ou activation.
