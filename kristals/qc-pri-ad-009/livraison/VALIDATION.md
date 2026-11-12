# Rapport de livraison locale — `qc-pri-ad-009` v1.2

**Livrable :** `qc-pri-ad-009_livraison_v1.2.zip` ; **racine de superposition :** `kristals/qc-pri-ad-009/`. **État :** travaux rédigés, tests structurels locaux; items `a_revoir`. Aucun statut « certifié », « homologué », « publié », ni qualification Framework.

## Modifications effectuées

- **2 remplacements complets** : `authoring/PARCOURS.md` (front matter YAML original inchangé; douze sections nourries de consignes et critères) et `authoring/CONTRAT_PEDAGOGIQUE.json` (champs et références v1.2 conservés; champs de famille ajoutés; statut de rédaction mis à jour).
- **12 nouveaux fichiers** : six leçons, plan et banque de 12 items, grille analytique, références, manifeste et présent rapport.
- **Deux preuves autonomes** : `q-009` scène de bibliothèque imaginaire, `q-010` théâtre d'objets de traversée de rivière. Rubrique M1–M4, niveau 2 dans chacune des deux situations, sans note unique. Les items ne font intervenir aucune IA comme correcteur automatique.
- Le ZIP **n'inclut pas** `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, `AGENTS.md`, `kristal.workspace.json`, ni les dossiers centraux `docs`, `canon`, `state`, `runtime`, `registry`, `governance`, ni aucune autre feuille.

## Contrôles effectivement exécutés sur les données et le ZIP

- Ouverture et lecture des documents de référence et de la frame dans l'archive fournie; concordance de l'ID, titre, discipline, objectif exact, critère exact, préalables et famille avec le registre source.
- Vérification programmatique de la conservation du front matter YAML octet pour octet, des 12 sections `## 1.` à `## 12.`, de la structure des champs d'origine du contrat JSON et des 13 champs gouvernés de la famille.
- Analyse JSON stricte du contrat, de la banque et du manifeste; vérification des `item_id` numérotés 001–012, uniques, `obj-1`, `crit-1`, famille `qc-pri-ad-009-ev-01`, valeurs des modes/difficultés, consignes, stimuli, productions attendues, critères et feedback non vides.
- Vérification des deux contextes de maîtrise distincts et des quatre dimensions observables attendues; confirmation de l'absence de mode paramétrique sans solveur et de toute génération aléatoire dans la banque.
- Vérification statique de la présence d'exemples et contre-exemples, de 2 diagnostics, 3 activités guidées, 4 autonomes, 2 transferts, feedback sur erreurs et rappel différé; présence textuelle des garde-fous de sécurité, consentement, droits et accessibilité.
- Simulation de superposition par comparaison au workspace v1.2 source : **2 fichiers préexistants remplacés et 12 absents ajoutés** dans l'unique dossier ciblé.
- Sur l'archive ZIP effectivement écrite : **14 entrées non vides**, toutes exactement sous `kristals/qc-pri-ad-009/`, liste réelle identique au manifeste, premier chemin conforme, aucun chemin absolu, `../`, dossier enveloppant, fichier externe ou autre ID; intégrité CRC vérifiée (`testzip`).

## Limites : contrôles non exécutés / qualification humaine requise

- Les **réponses artistiques** sont ouvertes; les analyses attendues illustrent des productions acceptables mais ne les réduisent pas à un corrigé unique. La grille n'a **pas** été étalonnée sur des élèves ni validée par un jury de spécialistes.
- La **qualité du contenu** et la sécurité ont fait l'objet d'une inspection du texte et de garde-fous écrits; aucun atelier physique, captation réelle ni test auprès d'élèves n'a été effectué.
- Les fichiers n'intègrent aucune image, pièce, musique ou citation externe; cela ne vaut **pas audit juridique des licences** de l'ensemble du workspace. Aucune source externe n'a été vérifiée en direct.
- L'accessibilité a été examinée **dans les consignes textuelles** (soutiens non invasifs, choix de support, absence d'exigence de captation); **aucun audit d'interface, test d'usage ou WCAG** n'a été réalisé.
- Les liens ont été vérifiés de manière **statique** et les références à l'autre Kristal restent des relations du graphe. Aucune navigation LMS, aucune extraction dans un véritable déploiement, aucun `check`/`build-v9`/`check-ai` du Framework, publication ou homologation n'a été exécuté.

## Décisions à la revue humaine

1. Faire revoir par un professionnel d'art dramatique la formulation des consignes, le réalisme des deux scénarios, les exemples de retour non jugeant et le poids des 4 dimensions; discuter la façon de documenter V1/V2 sans enregistrer les élèves.
2. Faire essayer les tâches avec des élèves en conservant leurs adaptations d'expression, et faire observer deux correcteurs pour examiner la constance de la grille; les items restent `a_revoir` jusqu'à ce contrôle.
3. Vérifier avec l'équipe LMS les champs de banque supplémentaires (`family_id`, `critere_id`, `representation`, `preuve_maitrise`) **avant import**; aucune modification centrale n'est incluse ici.
4. **Proposition non appliquée au schéma central :** prévoir dans une version future un mécanisme explicite « deux preuves distinctes » et un champ « aide de fond / soutien d'accessibilité neutre » dans le suivi d'observation, plutôt qu'un score unique.

**Instruction de fusion :** extraire la frame maîtresse, entrer dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, puis extraire ce ZIP **à cet endroit**. Aucun second préfixe `Frames_202_.../` n'est présent dans la livraison.
