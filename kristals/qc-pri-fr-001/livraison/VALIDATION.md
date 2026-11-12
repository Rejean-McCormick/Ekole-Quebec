# Validation de livraison — qc-pri-fr-001 (base v1.2)

**Nature :** delta fusionnable de contenu pédagogique, **non** publication, homologation, qualification d'un canon v9, ni examen certifié. État éditorial : `a_revoir`; revue de spécialistes et essai en situation non réalisés. Le rapport final de la vérification technique figure dans le contrôle local exécuté pendant la fabrication; les vérifications listées ci-dessous correspondent aux tests automatiques effectivement mis en œuvre sur le dossier et le ZIP.

## 1. Sources et frontières vérifiées

- Archive source locale ouverte : `initbundle(1).zip` / dossier interne `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Fichiers de gouvernance v1.2, graphe, `authoring/PARCOURS.md`, contrat JSON, `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, `AGENTS.md` et workspace consultés.
- Le graphe central contient **aucune arête sortante** de `qc-pri-fr-001`, et une arête entrante `qc-pri-fr-002/requires/qc-pri-fr-001` ; aucun autre Kristal n'est modifié ou inclus.
- **Identité inchangée :** `qc-pri-fr-001`, titre « Conscience phonologique et syllabes », discipline FR / « Français, langue d’enseignement », `obj-1`, `crit-1`, `qc-pri-fr-001-ev-01`, objectifs et preuve exprimés littéralement selon la source, `requires=[]` et ordre conseillé `[]`.
- `PARCOURS.md` conserve tous les champs de son front matter YAML et ses **12 sections**; seul `revision_contenu` est relevé de `0.2.0` à `0.3.0`, sans modifier les métadonnées d'identité. `CONTRAT_PEDAGOGIQUE.json` conserve les champs anciens et l'objet famille v1.2 en les enrichissant avec les 13 paramètres requis, plus une indication éditoriale de progression.

## 2. Tests techniques locaux exécutés

| Contrôle | Méthode / portée | Résultat |
|---|---|---|
| Liste des fichiers | Énumération du dossier et comparaison exacte aux 14 entrées du manifeste | **Réussi** |
| Fichiers non vides | Contrôle de taille > 100 octets pour chacun des 14 contenus | **Réussi** |
| YAML | Analyse avec PyYAML, conservation des clés et valeurs canoniques de la source; 12 titres numérotés 1–12 | **Réussi** |
| JSON | Chargement en analyseur JSON des trois fichiers : contrat, banque, manifeste, avant/après ZIP | **Réussi** |
| Contrat v1.2 | Comparaison des champs anciens avec le JSON d'origine et vérification des 13 champs de famille | **Réussi** |
| Identité/liens | Contrôle des ID, objectif, preuve, famille, absence de prérequis ajoutés et absence de modification d'un autre ID | **Réussi** |
| Banque | 12 IDs séquentiels `q-001` à `q-012`, sans doublons; champs exigés présents, mode fixe, graines et paramètres null, statuts `a_revoir` | **Réussi** |
| Deux preuves | Deux contextes fixés, 5 mots chacun, 10 mots distincts avec découpages et fusion attendus documentés | **Réussi** |
| Nouveauté des mots d'épreuve | Recherche des 10 mots P1/P2 dans les cinq fichiers de notions/diagnostic/enseignement/guidage/remédiation, hors feuille dédiée à l'épreuve | **Réussi** |
| Présence des activités | Comptage structurel : au moins 2 diagnostics, 3 guidages, 4 autonomes, 2 transferts | **Réussi** |
| Archives | ZIP testé pour CRC, première entrée et toutes entrées sous `kristals/qc-pri-fr-001/`, exactement 14 fichiers et aucun chemin absolu, `../`, dossier parent ou répertoire hors liste | **Réussi** |

**Portée réelle des tests :** contrôles structurels, parsing, invariants et cohérence des corrigés **renseignés**. Les réponses phonologiques (p. ex. frontières exactes, voyelles et réalisations dialectales) ont été raisonnées et comparées éditorialement, **mais aucune correction phonétique n'a été validée par un jury de phonologie ni par une étude d'élèves**. Aucun contrôle automatique de la justesse linguistique n'est présenté comme un oracle.

## 3. Revue humaine encore obligatoire

1. **Phonologie du français québécois :** écoute et validation des 12 items par personne compétente, en particulier voyelles de *moto*, *chocolat*, *puma*, *tuba*; reconnaissance de variantes régionales et traitement de la syllabification à l'oral. Vérifier que les partitions de 3 syllabes de *domino*, *salami* et *numéro* restent robustes dans la population visée.
2. **Passation terrain / clarté :** tester D1/D2, les trois guidages, quatre activités et les deux preuves auprès d'utilisateurs autorisés; mesurer interprétation, temps, fatigue et non-contamination des deux listes. Ne pas inférer une fidélité psychométrique de la complétude structurelle.
3. **Accessibilité :** vérifier les adaptations auditives, d'articulation et les réponses gestuelles complémentaires, sans pénaliser l'accent ni abaisser le critère oral; aucune évaluation avec des élèves n'a été effectuée.
4. **Source et droits :** références OQLF et sources internes identifiées; aucun média tiers n'est inclus. Examiner les droits de toute future illustration, voix enregistrée, réutilisation et publication.
5. **Cadre de gestion local :** confirmer les conditions de consentement si un enregistrement est envisagé; anonymisation des observations. L'archive ne recueille aucune donnée personnelle.
6. **Qualification du Framework :** le canon v9, son build, `check` / `check-ai`, les adaptateurs LMS, la publication/activation et la fusion réelle dans la copie maîtresse n'ont **pas** été exécutés : cette livraison est volontairement un delta de 14 fichiers, pas une opération canonique ou une qualification de système.

## 4. Règles de fusion et changements éventuels proposés (non appliqués)

Pour intégrer, décompresser le maître, entrer dans son dossier **`Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`**, extraire ce ZIP à cet emplacement. Seuls `kristals/qc-pri-fr-001/authoring/PARCOURS.md` et `CONTRAT_PEDAGOGIQUE.json` remplaceront des fichiers; les 12 autres sont nouveaux. Aucun registre, governance, docs, canon, AGENTS, workspace, state ou runtime n'est présent dans cette archive.

**Propositions, sans toucher aux bases centrales :** (A) introduire dans une version ultérieure du schéma un champ de graphe pour relier distinctement la « syllabe finale » et la « finale phonémique » afin d'éviter la polysémie; (B) prévoir un inventaire approuvé de stimuli oraux québécois avec versions et variants, entièrement séparé de la source canonique; (C) ajouter au pipeline central une revue phonétique humaine obligatoire et un contrôle automatisé de non-réemploi des mots de preuve. Aucune de ces propositions n'est appliquée ici.

## 5. Statut final

**Contrôles techniques locaux : réussis** sur l'artefact de livraison. **Contrôle scientifique, essais pédagogiques et qualification du Framework : à faire.** Les items conservent `validation_status: a_revoir`. Aucun statut `publié`, `homologué` ou `certifié` n'est revendiqué.
