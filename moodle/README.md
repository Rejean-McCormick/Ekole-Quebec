# Pont Kristal polymorphe → `local_uckk` (candidat)

- Plan calculé : `plans/moodle_projection_dry_run.json`, sans correction ou données personnelles.
- Contrat : `contracts/kristal-moodle-projection.schema.json`.
- Mapping explicite : `contracts/bindings.example.json` (vide par défaut).
- Proposition de lecteur PHP pur : `local_uckk_candidate/classes/local/kristal/projection_plan_reader.php`.

Ne pas placer `plans/`, `kristals/` ou les banques dans le webroot ou les pages publiques. Le répertoire `local_uckk_candidate` **n'est pas un plugin installable autonome** : intégrer au `local_uckk` existant après revue du contrat et tests Moodle. Aucun schéma de base n'est modifié et aucune API de création de cours n'est appelée.

Voir `docs/09_KRISTAL_MOODLE_POLYMORPHE.md` pour la procédure.
