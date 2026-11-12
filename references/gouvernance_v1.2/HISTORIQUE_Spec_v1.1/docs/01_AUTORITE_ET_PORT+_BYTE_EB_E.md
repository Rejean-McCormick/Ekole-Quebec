# 01 — Autorité, portée, statut et décisions gelées

## 1.1 Portée

- Ordre **primaire**, années **1 à 6**, cycles **1 (1re–2e), 2 (3e–4e), 3 (5e–6e)**.
- 14 intitulés disciplinaires reproduits du portail PFEQ; il s'agit d'un **catalogue de variantes**, pas de 14 disciplines suivies simultanément par chaque enfant.
- Les Kristals couvrent l'apprentissage, la pratique, le réinvestissement et les preuves de maîtrise. Les notes officielles, décisions scolaires et dossiers d'élèves sont **hors périmètre canonique**.
- L'offre scolaire locale et les variantes de programmes sont paramétrées dans les assemblages, jamais présumées universelles.

## 1.2 Statuts des affirmations

| Statut | Définition | Publier comme officiel ? |
|---|---|---|
| `officiel_verifie` | Transcription vérifiée d'un document gouvernemental identifié et applicable | Oui, avec référence précise |
| `extraction_scolqc` | Assertion dans ScolQc, non encore contre-vérifiée pour cette édition | Non, jusqu'à vérification |
| `pedagogique_valide` | Proposition de parcours revue et approuvée pédagogiquement | Non : contenu de notre projet |
| `proposition` | Hypothèse ou brouillon IA/éditorial | Non |
| `à_vérifier` | Donnée non vérifiée ou source insuffisante | Non |
| `contredit` | Désaccord explicite entre sources/éditions | Non, jusqu'à arbitrage |

**On ne transforme jamais une projection pédagogique en prescription ministérielle.** La validation technique ne donne pas une autorité institutionnelle.

## 1.3 Décisions fermes v1.0

- Catalogue initial = **202 IDs gelés**; sujets provisoires modifiables sans renommer l'ID.
- Une feuille n'est **pas** obligatoirement une année : les attentes annuelles sont des **affectations versionnées** à une même feuille.
- Le contenu primaire est rédigé en **français**; lorsque le programme est Anglais, langue d'enseignement/Anglais, langue seconde, les activités peuvent utiliser l'anglais conformément à la compétence visée. Le champ `langue_contenu` explicite la langue réelle.
- La filiation `prérequis` doit être vérifiée et **acyclique**. L'assemblage par année doit être reproductible.
- Rien n'est publié comme **examen validé** par simple génération IA.
- Sources officielles et curriculum résident dans **ScolQc**; les feuilles ne stockent que des **références versionnées**, pas un double catalogue officiel.
- `BUILD != PUBLISH != ACTIVATE` : les versions brouillon, validées, publiées et activées sont distinctes.

## 1.4 Questions volontairement non tranchées

- Alignement de chacune des 202 unités sur les attentes officielles et les années : **à renseigner une par une**.
- La granularité finale : scissions/ajouts autorisés par procédure de changement, jamais silencieusement.
- Durée réelle, nombre d'exercices, seuil de maîtrise, pondération d'une épreuve : **définis par discipline, tâche et validation**, pas à l'échelle du catalogue.
- Compatibilité technique de l'export Moodle : à tester, pas promise.
- Licence effective de chaque source non originale : à vérifier avant republication.

## 1.5 Provenance des choix

**Venant des archives de l'utilisateur :** `A-Kristal-ScolQc` sépare curriculum, progression et évaluation; le Framework v9 sépare artefact logique, état, dérivation et matérialisation; l'Authoring Kit sépare canonical et derived; UCKK montre la fédération parents/enfants sans copier les cours.  
**Choix nouveaux de cette norme :** IDs de microparcours, modèles Markdown, relation `requires` acyclique, découpage des activités, protocole parallèle, grille de validation et stratégie d'examens.

## 1.6 Sources publiques de contrôle

- PFEQ primaire : https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire
- Cadres d'évaluation : https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/epreuves-ministerielles-evaluation-apprentissages/cadres-evaluation/primaire-secondaire
- Culture et citoyenneté québécoise : https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/culture-citoyennete-quebecoise
- Français, langue d'enseignement : https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/francais-langue-enseignement

La mention d'une page ici ne prouve pas l'alignement d'une feuille à une section précise de la PDA.

## 1.7 Référentiel officiel central (ajout v1.1)

La page [REFERENCES_OFFICIELLES_QC.md](../REFERENCES_OFFICIELLES_QC.md) est le registre unique de **découverte** des documents ministériels et des codes administratifs éventuellement vérifiés. `A-Kristal-ScolQc` demeure la source de vérité curriculaire intégrée. Les codes du projet ne sont **pas** des codes ministériels. Voir [doc 16](16_NOMENCLATURE_OFFICIELLE_ET_REGISTRE.md).
