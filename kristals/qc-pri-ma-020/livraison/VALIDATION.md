# Rapport de validation — qc-pri-ma-020 — livraison v1.2

## Périmètre de livraison

- Seul le Kristal `qc-pri-ma-020` est livré, en delta fusionnable sous `kristals/qc-pri-ma-020/`.
- **Deux remplacements autorisés :** `authoring/PARCOURS.md`, `authoring/CONTRAT_PEDAGOGIQUE.json`.
- **Douze nouveaux fichiers :** six contenus, trois évaluations, une fiche de provenance, un manifeste et ce rapport.
- Le workspace maître, le graphe, la gouvernance, `ALIGNEMENT.md`, `AGENTS.md`, `kristal.workspace.json` et tous les autres Kristals restent intacts.
- Références originales : archive source `Spec_Kristals_Parcours_Primaire_Qc_v1.1(1).zip`, dossier intérieur `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`.

## Vérifications effectivement réalisées

1. **Sources lues :** contrat v1.2, générateur/examens, charte de conversion, graphe, PARCOURS, CONTRAT_PEDAGOGIQUE, ALIGNEMENT et BRIEF_REDACTION du Kristal.
2. **Comparaison de source :** frontmatter YAML conservé exactement, analysé par parseur YAML; douze sections `## 1.` à `## 12.` présentes dans l'ordre; tous les champs d'origine du contrat JSON conservés sans changement, champs de famille gouvernance ajoutés.
3. **Alignement :** titre, objectif `obj-1`, critère `crit-1`, famille `qc-pri-ma-020-ev-01` concordants; le graphe confirme `requires → qc-pri-ma-008` et `recommends_before → qc-pri-ma-009` non bloquant.
4. **Banque :** JSON valide; douze IDs uniques et numérotés; chaque item a son énoncé, corrigé/rubrique, critères, feedback et statut `a_revoir`. Tous reliés à `obj-1`, `crit-1`, `qc-pri-ma-020-ev-01`; deux preuves autonomes explicites dans deux contextes distincts (`q-011`, `q-012`).
5. **Calculs :** treize assertions fixes de résultats (exercices, transferts, deux preuves); six générateurs arithmétiques testés chacun sur **4 096 seeds entières**, soit **24 576 variantes** recalculées à l'aide de formules de contrôle indépendantes. Vérification des bornes, quotients, restes et non-division par zéro; instances retenues et égalités de solution contrôlées. La validité pédagogique de chaque variante n'est pas automatiquement prouvée par ces tests arithmétiques.
6. **Contrôles pré-emballage : 24 923 assertions réussies, 0 échec** sur la version finale des treize fichiers disponibles à ce stade. Celles-ci incluent les 24 576 tests arithmétiques, les tests de structure, liens, champs et les treize exemples fixes. Un contrôle intermédiaire avait repéré une mention absente (« division euclidienne » dans le parcours); la formulation a été précisée avant la relance réussie.
7. **Droits et accessibilité :** déclaration d'origine des énoncés originaux; aucune image ou ressource tierce incorporée; lecture orale, manipulations, tableaux et réponses équivalentes décrits. Il s'agit d'un contrôle documentaire, pas d'un audit humain complet de droits ou d'accessibilité.
8. **ZIP final :** archivage et vérification des 14 entrées non vides, premier chemin `kristals/qc-pri-ma-020/`, noms relatifs propres, aucun doublon, aucun fichier parasite ou d'un autre ID, JSON relus, manifeste exact, intégrité CRC (`testzip`) et extraction isolée comparée octet par octet. Les résultats du contrôle post-emballage sont inscrits dans la sortie du script local; aucune extraction dans le workspace maître réel n'est effectuée.

## Points non résolus — revue humaine requise

- Valider le calibrage didactique au niveau réel des élèves, la clarté des consignes, les durées et les représentations permises.
- Relire les deux tâches de maîtrise sur les livrets et les paniers pour l'équité, l'accessibilité en usage et la non-familiarité; essayer la grille avec de vraies productions d'élèves.
- Vérifier l'intégration technique dans le moteur LMS/framework, la gestion des données d'élèves et le traitement exact de chaque adaptation.
- Les seeds garantissent la reproductibilité des **valeurs** mais les stimuli textuels doivent être instanciés à nouveau lors d'un changement de seed; les instances actuellement livrées sont verrouillées et contrôlées. Aucun moteur de génération en ligne n'a été intégré.
- Aucun item qualifié « certifié », aucune homologation ni alignement détaillé PFEQ revendiqué.

## Propositions futures de structure (non appliquées)

- Versionner dans un schéma central un protocole de génération des items (`instancier(seed)`, calcul solution, contraintes) pour que le LMS ne réimplémente pas les descriptions textuelles.
- Ajouter au registre des évaluations, via processus de gouvernance distinct, des champs de traçabilité d'essais réels, de statut de revue humaine et d'adaptations d'accessibilité.
- Ne pas modifier les bases centrales sans mandat et validation ultérieurs.

**Statut :** `controle_technique_effectue_revue_humaine_requise`.
