# Pont pédagogique vers Moodle — projection non destructive

| Ekole | Moodle | Règle |
| --- | --- | --- |
| Vues de disciplines | catégorie / catégorie parente | séparer organisation scolaire et arbre réellement configuré |
| Kristal éducatif | zéro, une ou plusieurs projections candidates, éventuellement cours Moodle | plan de projection, pas création automatique |
| Six modules `contenu/` | sections de cours, ressources Page ou Livre | dépend du format et des choix validés |
| `BANQUE_ITEMS.json` | banque de questions / quiz / devoir | conversion par type après revue et validation manuelle |
| Grille / deux preuves | rubriques, achèvements, suivi | pas d'inférence de réussite depuis une seule note |
| Préalables `requires` | disponibilité / diagnostic | diagnostic équivalent possible; ne pas verrouiller automatiquement |
| Métadonnées année | champs personnalisés, cohortes | non renseignés tant qu'aucune affectation justifiée |
| Métadonnées accessibles | activités/ressources selon contraintes | droits Moodle sous Access API, non sous Kristal |

La documentation fournie `DevDocMoodle.txt` couvre notamment Navigation, Output, Access, Availability, Enrolment, Competency, Completion, Question, Grading, External Functions et les formats de cours. Le snapshot `uckk-moodle` contient déjà `docs/12...`, `14...` et `15...` sur le contrat Faculty/Atlas/Moodle; réutiliser `local_uckk` et ne pas introduire une deuxième extension sans décision explicite.

## Mise à jour — pont polymorphe

La liste `courses` du plan historique représente des **candidats non sélectionnés**, non des cours imposés. La source est typée par Kristal (`state_ref`, `native_model.kind` ouvert) et la forme Moodle est choisie indépendamment. Voir `09_KRISTAL_MOODLE_POLYMORPHE.md`. L'adaptateur `tools/kristal_moodle_bridge.py` ne publie aucun item et ne construit aucun engagement v9/v10.
