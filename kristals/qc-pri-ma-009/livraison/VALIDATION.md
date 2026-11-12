# Validation de livraison — qc-pri-ma-009 v1.2

## Statut

**Vérification technique exécutée sur les contenus et les calculs; revue pédagogique humaine, essai en classe et qualification Framework encore nécessaires.** Il ne s'agit ni d'une publication, ni d'une homologation PFEQ, ni d'une banque d'items certifiée. Les `validation_status` des 12 items sont `a_revoir`.

## Périmètre et source

- Source lue : archive locale `Spec_Kristals_Parcours_Primaire_Qc_v1.1(1).zip`, sous-dossier **`Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`**, qui contient le workspace et la gouvernance **v1.2**. Ce n'est pas un remplacement inventé.
- Travail exclusif sur `kristals/qc-pri-ma-009/`. Deux fichiers `authoring/` remplacés complètement en préservant le frontmatter v1.2 et tous les champs originaux du contrat JSON; 12 fichiers nouveaux. Aucun autre ID modifié.
- `obj-1` et `crit-1` immuables; unique préalable strict `qc-pri-ma-008`; famille `qc-pri-ma-009-ev-01` et type natif `paramétrique_controle` préservés.
- Le groupe de dossiers `governance/`, `registry/`, `docs/`, `canon/`, `state/`, `runtime/`, `AGENTS.md` et `kristal.workspace.json` reste hors archive.

## Tests réalisés

- [x] Fichier source v1.2 et gouvernance lus.
- [x] Graphe: préalable requires exact.
- [x] Objectif et preuve du contrat inchangés.
- [x] Identité et concepts canoniques.
- [x] Champs de premier niveau et famille natifs conservés.
- [x] Préalable unique conservé.
- [x] Famille unique et champs de gouvernance.
- [x] 12 sections numérotées et frontmatter YAML maintenu.
- [x] Méta YAML principal inchangé.
- [x] Deux contextes probants nommés.
- [x] Au moins 2 exemples et 2 contre-exemples.
- [x] Deux diagnostics.
- [x] Trois exercices guidés.
- [x] Quatre exercices autonomes.
- [x] Deux transferts avec corrigés.
- [x] Rappel différé à J+2 et J+7.
- [x] JSON strict parsable, contrat et banque.
- [x] Format de banque exact.
- [x] 12 items distincts, numérotation séquentielle.
- [x] Champs communs présents et réponses exploitables.
- [x] Tous items liés à obj-1, crit-1 et famille.
- [x] Modes, niveaux et statuts autorisés.
- [x] Deux preuves en deux contextes différents.
- [x] 5 items paramétriques documentés.
- [x] 7 items fixes sans seed.
- [x] 15 exemples paramétriques recalculés indépendamment.
- [x] 10 000 variantes de seed et deux régimes recalculés.
- [x] Identités numériques présentes dans Markdown arithmétiquement exactes.
- [x] Égalités avec reste hors borne uniquement expliquées comme erreurs.
- [x] Contrôles de droits et provenance explicités.
- [x] Adaptations non guidantes explicites.
- [x] 12 fichiers préparés hors manifeste et validation.
- [x] Chemins du manifeste complets au bon préfixe.

**Nombre d'identités numériques explicites examinées dans Markdown :** 31. Les égalités présentées comme « contre-exemples » ne constituent **pas** une preuve de division valide si `r≥d`, même quand `N=d×q+r` est vrai.

## Points à faire vérifier par un humain

- Progression réelle des difficultés, compréhension des consignes, pertinence des unités et du vocabulaire auprès du public cible; qualité de l'évaluation de productions orales et tactiles.
- Équité et accessibilité en conditions locales, adaptation au matériel disponible et aux lecteurs d'écran; mesure du temps et charge cognitive.
- Révision des rubriques, des cinq variantes paramétriques et de toute nouvelle instance avant usage sommatif. Aucun audit indépendant du niveau PFEQ n'est demandé.
- Essai de l'intégration dans le LMS, test de publication/qualification Framework, droits de tout matériel externe éventuellement ajouté ultérieurement. Aucun matériel externe n'est inclus dans le delta.
- Cohérence après fusion avec le workspace cible exact, puisque les tests sont effectués ici sur le ZIP et sur la frame source seulement.

## Propositions de structure non appliquées

1. Envisager ultérieurement un validateur de versions paramétriques inter-Kristals avec dérivation numérique indépendante, journal de seeds et approbation humaine.
2. Envisager un champ versionné distinguant « contexte approuvé » de « valeurs numériques testées » dans les familles d'évaluation.
3. Envisager un journal de preuves de maîtrise par élève **dans le LMS**, pas dans le canon du Kristal.

## Fusion prévue

Extraire ce ZIP **à l'intérieur** du dossier maître `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` : le premier chemin est `kristals/qc-pri-ma-009/authoring/PARCOURS.md`, aucun dossier parent ajouté.
