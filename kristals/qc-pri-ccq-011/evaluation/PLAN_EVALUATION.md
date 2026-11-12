# Plan d'évaluation — qc-pri-ccq-011

## Contrat inchangé

- **Objectif `obj-1` :** Présenter de manière respectueuse différentes perspectives de Premiers Peuples.
- **Critère `crit-1` :** Comparer deux documents contextualisés sans généralisation ni appropriation.
- **Famille `qc-pri-ccq-011-ev-01` :** mode natif `observation_ou_production`; déclinaisons `fixe` ou `scenario_controle` selon le JSON; aucune génération libre de prises de position autochtones.
- **Couverture :** 12 items distincts, 7 fiches documentaires vérifiées et stables, dont deux épreuves indépendantes `q-011`/`q-012`. Aucun item ne demande croyance, identité, accord ou vécu intime.

## Tableau d’alignement, complexité, représentation

| Item | Liens immuables | Difficulté | Documents / représentation | Usage |
|---|---|---|---|---|
| 001 | `obj-1` / `crit-1` / `qc-pri-ccq-011-ev-01` | initial | FPCC-L + FPCC-V | exercice contrôlé |
| 002 | `obj-1` / `crit-1` / `qc-pri-ccq-011-ev-01` | initial | APN-L + APN-C | exercice contrôlé |
| 003 | `obj-1` / `crit-1` / `qc-pri-ccq-011-ev-01` | initial | ITK-T + ITK-R | exercice contrôlé |
| 004 | `obj-1` / `crit-1` / `qc-pri-ccq-011-ev-01` | intermediaire | ITK-T + CNM-H | exercice contrôlé |
| 005 | `obj-1` / `crit-1` / `qc-pri-ccq-011-ev-01` | intermediaire | FPCC-L + APN-L | exercice contrôlé |
| 006 | `obj-1` / `crit-1` / `qc-pri-ccq-011-ev-01` | intermediaire | FPCC-V + CNM-H | exercice contrôlé |
| 007 | `obj-1` / `crit-1` / `qc-pri-ccq-011-ev-01` | intermediaire | APN-L + ITK-R | exercice contrôlé |
| 008 | `obj-1` / `crit-1` / `qc-pri-ccq-011-ev-01` | intermediaire | APN-C + CNM-H | exercice contrôlé |
| 009 | `obj-1` / `crit-1` / `qc-pri-ccq-011-ev-01` | transfert | FPCC-V + ITK-T | exercice contrôlé |
| 010 | `obj-1` / `crit-1` / `qc-pri-ccq-011-ev-01` | transfert | FPCC-L + CNM-H | exercice contrôlé |
| 011 | `obj-1` / `crit-1` / `qc-pri-ccq-011-ev-01` | transfert | FPCC-V + APN-C | preuve indépendante |
| 012 | `obj-1` / `crit-1` / `qc-pri-ccq-011-ev-01` | transfert | ITK-R + APN-C | preuve indépendante |

Chaque item contient deux dossiers indépendamment compréhensibles dans le champ `stimulus` (auteurs, type de document, région, repère de date et URLs, résumés originaux, limites). Réponse : comparaison orale, texte dicté ou texte écrit; une grille à cinq critères en `GRILLE_MAITRISE.md` demeure identique.

## Progression des difficultés

- `q-001`–`q-003` **initiale** : deux publications de la même organisation, identifier et comparer une question plus restreinte (l’enseignant corrige après la tâche).
- `q-004`–`q-008` **intermédiaire** : distinguer deux organisations et des peuples différents, ou mettre en regard droits, programmes, histoire et recherches.
- `q-009`–`q-010` **transfert préparatoire** : comparer des champs distincts sans inventer de culture commune.
- `q-011` **preuve A** : langues communautaires en C.-B. et charte des Premières Nations (FPCC-V + APN-C); **preuve B `q-012`** : participation inuit à la recherche et charte de Premières Nations (ITK-R + APN-C). Paires et questions propres, contextes géographiques et enjeux différents; administration séparée, ni aide ni retour entre les deux si leur indépendance risquerait d’être faussée.

## Corrigés et notation

Les réponses modèles sont des **exemples de formulations acceptables**, pas des chaînes exactes requises. Pour chaque item, évaluer C1 source-contextes, C2 faits exacts, C3 comparaison justifiée, C4 pluralité/continuité, C5 respect et limite; niveaux 0 à 2 en fonction des comportements visibles. Interdire pénalité sur accent, maîtrise orale accessoire, croyance, appartenance ou choix personnel.

**Barème pour preuve A et B :** chaque dimension doit obtenir 2/2 **dans les deux épreuves**; on ne compense pas un stéréotype par plusieurs bonnes phrases. En cas de réponse incomplète, correction descriptive, remédiation puis nouvelle preuve avec dossier préalablement vérifié; aucune certification automatisée.

## Contraintes de variation et de sécurité

- Mode `fixe`: aucune variation. Mode `scenario_controle`: les deux fiches de l'item et la consigne sont verrouillées; aucun choix aléatoire, seed `null`, paramètres documentés dans chaque item. Une substitution future exige une sélection manuelle d’une paire provenant du corpus de 7 fiches puis vérification humaine du nouveau corrigé et des droits.
- Fiches institutionnelles paraphrasées, sans inventer de personne porte-parole, de citation ou de pratique rituelle; éviter les images ou enregistrements tiers. Date de publication inconnue explicitement signalée.
- Sécurité psychosociale : aucun élève sollicité sur son origine, ses croyances, ses pratiques ou celles de ses proches; pas de simulation de rite ni de débat sur la légitimité d'une identité.
- Accessibilité : supports texte en format numérique lisible par lecteur d'écran, source lue à voix haute, temps adapté, texte dicté ou réponse orale; équivalence des critères cognitifs, correction humaine.

## Procédure de qualification (non exécutée ici)

Une revue humaine de documents par personnes compétentes, notamment des personnes concernées lorsque possible et correctement rémunérées, est nécessaire avant publication; pilotage avec élèves et vérification des licences avant intégration au LMS. `validation_status: a_revoir` pour chaque item.
