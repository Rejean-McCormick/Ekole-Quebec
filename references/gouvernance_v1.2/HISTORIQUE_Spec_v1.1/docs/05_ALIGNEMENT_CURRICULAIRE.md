# 05 — Contrat d'alignement PFEQ / ScolQc / PDA / évaluation

## 5.1 Principe

Il n'existe **pas de vérité curriculaire implicite**. Chaque correspondance entre un objectif créé par nous et une prescription doit porter : `document officiel`, `édition/variante`, `localisateur`, `unité référencée`, `type de correspondance`, `applicabilité`, `statut`, `relecteur`.

Un simple lien vers la page d'accueil d'un programme ne suffit **pas** à qualifier un objectif. Les 202 intitulés ne sont pas déjà alignés.

## 5.2 Chaîne de preuves

```text
autorité MEQ
  -> document (PFEQ / PDA / cadre d'évaluation)
  -> édition/version applicable
  -> composante localisée dans le document
  -> unité sémantique ScolQc si existante
  -> mapping explicite vers notre objectif / critère
```

Dans ScolQc, préserver les références `source_id`, `source_component_id`, les identifiants `sem:*`, `pda:*` **quand elles existent réellement**. Ne jamais en fabriquer pour combler une lacune. Les sources `semantic_curriculum.json` et `progression_semantics.json` ne sont pas des transcriptions exhaustives de chaque PDA : une entrée manquante peut rester vérifiable directement au PDF officiel.

## 5.3 Règles temporelles

- Tout alignement porte `annee_scolaire`: `2026-2027`, `2027-2028`… ou un intervalle explicitement prouvé.
- Un seul champ `cycle` **ne peut pas** remplacer la preuve d'une attente par année.
- Les états de progression sont strictement : `learn_with_teacher`, `expected_end_of_year`, `reuse` lorsqu'un document officiel ou ScolQc les justifie; ne pas confondre avec la réussite réelle de l'élève.
- Le **français, langue d'enseignement, du primaire** a un profil courant 2026–2027 et un programme actualisé obligatoire à partir de 2027–2028. Les mappings portent l'édition; pas de fusion silencieuse des compétences entre les deux.
- Les variantes `Français, langue seconde — base` et `Français, langue seconde — immersion` restent distinctes. Pour ILSS, les paliers documentés priment sur une affectation forcée par année.

## 5.4 Type de lien et preuve

`map_type` autorisés : `correspondance_exacte`, `couvre_partiellement`, `prerequis_pedagogique`, `reinvestit`, `proposition_a_valider`. **`correspondance_exacte` est interdit** sans un relecteur et un localisateur de source spécifique.

Un même objectif peut s'appuyer sur plusieurs composantes officielles. On conserve chaque mapping, même lorsque les sources divergent. Les relations curriculaires et pédagogiques ne sont jamais fusionnées.

## 5.5 Qualification minimale

Une feuille peut être `partiel` avec certains objectifs sourcés, mais le statut `verifie` exige : tous les résultats évalués reliés à une compétence ou contenu prescrit approprié **ou** explicitement marqués comme enrichissement non prescrit; chaque année revendiquée avec preuve applicable; édition identifiée; relecture humaine.

Ne jamais déduire « matière obligatoire en 1re année » simplement parce qu'une notion ou compétence connexe est enseignée ailleurs. L'assemblage doit vérifier règles et offre effectives.

## 5.6 Fichier obligatoire

[MODELE_ALIGNEMENT.md](../modeles/MODELE_ALIGNEMENT.md) doit accompagner chaque feuille, y compris si les rubriques contiennent la mention explicite `à_vérifier`.

## 5.7 Résolution des programmes et codes officiels (ajout v1.1)

Avant toute affirmation de code officiel ou de discipline, consulter [REFERENCES_OFFICIELLES_QC.md](../REFERENCES_OFFICIELLES_QC.md) et [doc 16](16_NOMENCLATURE_OFFICIELLE_ET_REGISTRE.md). Un `source_id` ScolQc est une clé d'extraction et **pas** un code ministériel. `code_officiel: null` et `statut_code: non_etabli` sont corrects lorsque le code n'a pas été attesté. L'absence de code **ne dispense pas** de préciser l'édition et la cible de progression dans un mapping officiel.
