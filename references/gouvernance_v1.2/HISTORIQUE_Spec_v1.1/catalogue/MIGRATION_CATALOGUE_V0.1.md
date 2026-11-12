# Correspondance catalogue initial → norme v1.0

| Attribut du catalogue antérieur | Interprétation v1.0 |
|---|---|
| `id` | Identité métier gelée, ni `artifact_id` ni commitment |
| `discipline` | Nom officiel à conserver sans altération |
| `titre` | Nom de travail non officiel, modifiable |
| `annees_admissibles: null` | Années inconnues, non `[]` |
| `competences_officielles: []` | Dans le catalogue 0.1 : **non peuplées**, ne pas inférer qu'aucune compétence n'existe |
| `prealables: []` | Dans le catalogue 0.1 : **non recherchés**, ne pas inférer qu'aucun prérequis n'existe |
| `eval_blueprint: null` | Aucun plan établi/validé |
| `statut: proposé_non_cristallisé` | Équivalent de réservation éditoriale `réservé`; aucun contenu qualifié |
| `alignement_pfeq: à_vérifier...` | Aucune année/compétence officialisée par le simple catalogue |

**Règle de migration importante :** certaines listes v0.1 sont vides par défaut, non par vérification. Après migration dans les modèles v1.0, utiliser `null` pour `prealables_declares` **tant que la recherche n'a pas été faite** et ne jamais déclarer une couverture curriculaire exhaustive.

## Dépendances utilisées par la norme

- `A-Kristal-ScolQc` (`knowledge-base/sources/semantic_curriculum.json`, `progression_semantics.json`, `curriculum_catalog.json`) : référentiel existant, couverture partielle explicitement documentée.
- `Kristal Framework` : contrat v9, identité logique, state commitments, matérialisation, publications et frontières de provenance.
- `Kristal Authoring Kit` : authoring, contrôle local, dossiers multi-workspaces, build et publication.
- `UCKK-Kristal-v9` : inspiration de fédération parents/enfants sans recopie sémantique.
- PFEQ primaire, PDA et cadres : sources officielles applicables; à consulter dans l'édition appropriée et à relier par composante exacte.
