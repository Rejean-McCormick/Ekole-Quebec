# Validation de livraison — qc-pri-ilss-003 (v1.2)

**Livraison :** delta fusionnable de `kristals/qc-pri-ilss-003/` ; **14 fichiers exactement** ; statut **`a_revoir`**, non qualifié, non publié, non homologué et non certifié.

## Contrôles réellement exécutés

Le script d'assurance-qualité `/_qa_ilss003.py` a été exécuté sur les fichiers rédigés **et** sur le ZIP : **78 contrôles / 78 réussis**, dont **68 précontrôles** et **10 contrôles supplémentaires de l'archive**. Les scripts de travail et journaux restent **hors du ZIP**.

1. **Préservation de la source** : YAML d'origine analysé et comparé à l'original (toutes les clés et valeurs préservées), titres/IDs/objectif/preuve/famille confirmés; 12 sections numérotées; contrat JSON garde ses champs racine et leurs valeurs d'origine, ainsi que toutes les clés/valeurs de famille déjà présentes. Les nouveaux paramètres sont additionnels.
2. **Graphe et dépendances** : absence de préalables stricts et d'ordre conseillé dans le contrat local confirmée; aucune dépendance ajoutée. Les liens du registre entrant ou sortant ne sont pas recopiés comme obligations du Kristal.
3. **Couverture de la leçon** : quatre notions explicites, deux exemples résolus, deux contre-exemples, deux diagnostics, trois pratiques guidées, quatre pratiques autonomes, deux transferts; les contrôles automatiques vérifient présence et numérotation, **pas** la validité didactique complète.
4. **Banque** : JSON strict lisible; **12 items** complets avec consigne, stimulus, réponse attendue, critères, feedback, difficulté et statut; IDs `q-001` à `q-012` continus et distincts, `obj-1`/`crit-1`/`qc-pri-ilss-003-ev-01` identiques; 12 modes fixes (seed et paramètres `null`, sans génération IA libre).
5. **Deux preuves autonomes** : q-011 en science et technologie et q-012 en arts plastiques, chacune avec quatre dimensions D1–D4; rubriques explicites et seuils conjoints dans `GRILLE_MAITRISE.md`. Contrôle éditorial de cohérence entre énoncés et traces attendues : q-011 exige **entourer ÉRABLE sur une fiche** et **coller une étiquette ÉRABLE**; q-012 exige **colorier le cercle en bleu** et **fixer l'étiquette CERCLE**; les distracteurs sont explicitement écartés.
6. **Accessibilité, sécurité, droits et liens** : passages sur lecture orale, alternatives matérielles, supervision, absence de données intimes et provenance repérés; références locales `../contenu/`, `../evaluation/`, `../sources/` résolues; absence d'images externes copiées. Le contrôle automatique ne constitue pas un audit légal d'accessibilité ni une licence externe.
7. **Intégrité de l'archive finale** : ZIP ouvert et testé (`testzip()` sans erreur); **première entrée** sous `kristals/qc-pri-ilss-003/`, 14 fichiers non vides correspondant exactement au manifeste, ordre conforme, aucun `../` ni chemin absolu, aucun autre Kristal ni dossier parent enveloppant; bytes du ZIP identiques aux fichiers vérifiés; 3 JSON analysés directement depuis l'archive.

Les catégories 1–7 décrivent les vérifications effectuées; les 78 tests sont des assertions techniques individuelles et ne sont **pas** 78 avis pédagogiques indépendants.

## Limites et points de revue humaine

- **Non exécuté** : essai en classe, enregistrement de réponses réelles, mesure d'accord entre correcteurs, validation psychométrique et intégration LMS/Framework Kristal.
- **À revoir** : faisabilité des supports, sens du vocabulaire selon les élèves et les variétés de français, impartialité des consignes, validité des seuils D1–D4 et calibrage des alternatives tactiles/numériques avec une personne enseignante ILSS et une spécialiste d'accessibilité.
- **Droits** : énoncés/textes pédagogiques originaux; sources externes liées et paraphrasées, sans images, extraits substantiels ou fichiers propriétaires repris. Aucune revue juridique indépendante n'a été conduite.
- **Statut** : la conformité des chemins et JSON permet une **fusion technique**, pas une certification de pédagogie, de sécurité universelle ou de conformité PFEQ.

## Propositions de changement de structure (non appliquées)

- Ajouter ultérieurement un champ commun permettant d'indiquer `oralisation_verbatim` versus `indice_semantique` dans les modalités d'évaluation.
- Ajouter éventuellement une structure standard de preuves longitudinales indépendantes, tout en gardant les observations nominatives **hors du paquet pédagogique**.
- Aucune modification de `governance/`, `registry/`, `AGENTS.md`, `kristal.workspace.json`, `ALIGNEMENT.md`, `docs/`, `canon/`, `state/`, `runtime/` ou d'un autre Kristal.
