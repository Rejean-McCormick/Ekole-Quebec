# 09 — Alignement polymorphe Kristal ↔ Moodle

## Décision

**Moodle consomme des projections, pas le canon Kristal.** Un Kristal peut être un graphe, un registre d'évènements, une machine à états, un objet métier, une preuve, une unité pédagogique ou toute structure hybride. `native_model.kind` reste libre, et n'est jamais déduit d'une activité Moodle. La classification pédagogique (`familles[].type`) ne définit pas la forme sémantique native.

| Couche | Détenteur d'autorité | Peut produire une vue Moodle ? |
| --- | --- | --- |
| Identité, frontière, payload natif, épistémologie, Logical Artifact/State v9 | Kristal | Lecture/projection uniquement |
| Projections de navigation, composition, requêtes | Kristal/consommateurs autorisés | Oui, sans changer les états canoniques |
| Cours, sections, quiz, devoirs, permissions, inscriptions, notes, suivi | Moodle | Oui : état opérationnel Moodle |
| Correspondances, diff, contrôles, provenance de synchronisation | `local_uckk` | Oui, mais aucune écriture via ce paquet |

La projection est **1 à 0..n** : plusieurs vues Moodle possibles pour un Kristal ; plusieurs Kristals peuvent contribuer à un même cours. Aucun cours par Kristal n'est obligatoire.

## Faits établis pour le paquet fourni

- **202 workspaces `stub`**, **202 `native_model.kind=undecided`** : aucune forme canonique métier ou qualification v9 n'est établie.
- **2 183 items** dans les banques ; ils ne sont **pas** convertis en questions Moodle, ni exposés publiquement.
- **4 familles d'évaluation** observées : `observation_ou_production`, `réponse_argumentée`, `paramétrique_controle`, `generee_sous_contraintes` ; ces types décrivent des usages pédagogiques, pas des topologies Kristal.
- **252 relations** : 134 `requires`, 99 `recommends_before`, 19 `reinforces` ; aucun verrou d'accès n'est créé. `requires` requiert une règle d'équivalence par diagnostic et une décision pédagogique avant d'utiliser Availability API.
- Les données pédagogiques v1.2 demandent une revue humaine et ne prouvent pas un State Snapshot v9 / une publication v10.

## Contrat d'interface

Source : `kristals/<id>/kristal.workspace.json` + `authoring/CONTRAT_PEDAGOGIQUE.json` + chemins `contenu/*` + `evaluation/BANQUE_ITEMS.json` + catalogue et graphe. Tous les chemins sont relatifs au pack local.

Sortie privée : `plans/moodle_projection_dry_run.json` (`ekole.kristal-moodle-projection-plan/1.0`) avec :

- `kristal_id`, `state_ref`, `identity.workspace_status` ;
- `semantic_state.native_kind` opaque, engagements v9/v10 **non établis** ;
- chemins et empreintes SHA-256 de fichiers auteur (**jamais** présentés comme engagements sémantiques) ;
- candidats de vues `course`, `resource`, `activity`, `navigation`, `none` et ressources `page`/`book` ;
- mappage d'évaluation par famille en **candidats à revoir**, sans conversion du corrigé ;
- relations du graphe sans effets Moodle automatiques ;
- champs de mapping Moodle uniquement si un opérateur les a renseignés.

Le tableau `courses` est conservé **pour compatibilité** avec le plan Ekole historique. Chaque entrée est `candidate_only=true` ; ce tableau ne signifie pas 202 cours à créer et le format de cours reste non décidé (`null`).

## Commandes locales, sans connexion Moodle

Depuis la racine Ekole :

```powershell
py -3 tools\ekole.py verify
py -3 tools\ekole.py moodle-plan
py -3 tools\kristal_moodle_bridge.py --audit-only
py -3 tools\kristal_moodle_bridge.py --bindings moodle\contracts\bindings.example.json
py -3 -m unittest discover -s tests -v
```

`bindings.example.json` est vide : **pas de faux ID Moodle**. Pour une projection sélectionnée, ajouter au dictionnaire `bindings` une **liste** de cibles pour le `kristal_id` (ou un objet unique pour rétrocompatibilité) ; chaque cible précise `projection_kind`, un `moodle_course_id` existant si besoin, un `moodle_category_id` pour `course`, et la revue `reviewed_by` + `approval_ref`. Plusieurs cibles Moodle pour un Kristal sont supportées, ainsi que le partage d’un cours entre plusieurs Kristals. Le pont vérifie ces champs mais reste en dry-run ; il refuse `write_authorized=true`.

Le fichier candidat `moodle/local_uckk_candidate/classes/local/kristal/projection_plan_reader.php` peut être intégré au dépôt réel `local/uckk/classes/local/kristal/` après revue. Il lit le plan en mémoire, refuse les plans non sûrs, n'ouvre ni transaction ni connexion externe. **Il n'est pas installé** dans l'archive `vendor/reference-only/uckk-moodle-source.zip` ; cette référence demeure intacte.

## Garde-fous avant toute matérialisation dans Moodle

1. Identifier la forme native avec les Shape Probes du kit, sans aplatissement en schéma pédagogique universel. Qualifier séparément l'État v9 et sa provenance si une publication canonique est visée.
2. Examiner les 202 livraisons et modes d'accessibilité ; approuver les items et corrigés avant conversion, vérifier les preuves distinctes et modalités de correction. Ne pas attribuer d'année scolaire depuis la vague de production.
3. Résoudre chaque correspondance vers les IDs réels de la base Moodle existante : ne jamais dériver un `courseid` de l'ID Kristal. Vérifier conflits avant création et appliquer une logique idempotente par mapping explicite.
4. Tester l'adaptateur dans une installation de test Moodle 5.2 / `local_uckk` (Access API, File API, Gradebook, Backup/Restore, tâches, événements). Les corrigés restent côté enseignant et ne sont pas dans la projection publique.
5. Seulement après comparaison, revue, et validation autorisée, réaliser une opération Moodle distincte et journalisée via `local_uckk`. Ce paquet **n'implémente aucune commande `apply`**.

## Limites explicites

Le pont vérifie l'identité, les fichiers, les types pédagogiques et les relations. Il ne prouve pas l'équivalence des activités, la qualité des contenus, la publication/activation v10, le support serveur Moodle, la validité du curriculum ni l'accessibilité effective. Les SHA de fichiers servent à constater la version des inputs, pas à inventer des Logical Commitments.
