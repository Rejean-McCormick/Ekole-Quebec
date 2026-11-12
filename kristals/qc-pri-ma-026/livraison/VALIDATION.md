# Rapport de validation réellement réalisée — `qc-pri-ma-026`

**Archive attendue :** `qc-pri-ma-026_livraison_v1.2.zip`  
**Statut :** `a_revoir`, **non certifié**, non publié, non homologué; exigences structurelles vérifiées localement.  
**Source lue :** `initbundle(1).zip`, dossier `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, fichiers communs et fichiers natifs du seul Kristal cible.

## Contrôles exécutés (script Python local)

1. Présence/lecture des trois textes de gouvernance, du graphe et des quatre fichiers authoring/ demandés; identité `qc-pri-ma-026`, `obj-1`, `crit-1`, titre **Temps et durées**, discipline **Mathématique**, famille `qc-pri-ma-026-ev-01` confirmés contre l’archive.
2. **Métadonnées conservées :** toutes les clés de l’en-tête YAML initial `PARCOURS.md` conservées (types et valeurs), 12 sections numérotées présentes. Les champs et familles du JSON source sont conservés; seuls `statut`, `review_status` et les champs ajoutés de famille/génération documentent la nouvelle préparation en attente de revue.
3. Graphe : aucune relation sortante `requires`, `recommends_before` ou `reinforces`; une relation entrante non bloquante vers cet ID. Pas de préalables créés.
4. **12 items** numérotés `q-001` à `q-012`, distincts et non vides, liés tous à `obj-1`, `crit-1`, à la même famille, avec énoncé, corrigé, critères, feedback, mode et difficulté; **6 paramétriques**, **6 fixes**. Deux contextes de maîtrise indépendants : A bibliothèque (`q-011`) et B station d'observation (`q-012`).
5. **Calculs paramétriques** : vérification exhaustive des **333 combinaisons** des six domaines finis (`q-002`: 81; `q-004`: 36; `q-006`: 27; `q-008`: 27; `q-009`: 81; `q-012`: 81), par addition de `timedelta` et contrôle de différence date-ordinale/heure/minute. Contrôle séparé des **18 jeux d'exemples** (`seed`, `seed+1`, `seed+8` pour 6 modèles) et des instanciations de livraison. Horaires calculés en dates grégoriennes et journées fictives uniformes.
6. Corrigés fixes : six intervalles recalculés avec horodatages explicites, leurs éventuelles marges d'horaire revérifiées. Diagnostics et pratiques principales revérifiés par exemples manuels et calcul indépendant dans le script. Limite : aucune évaluation psychométrique des rubriques.
7. **Trois JSON stricts** rechargés par parseur : contrat, banque et manifeste; en-tête YAML rechargé; numérotation et types de modes vérifiés; contenu de chaque chemin du manifeste comparé aux fichiers présents.
8. **ZIP** : 14 entrées/fichiers **non vides**, chaque chemin relatif commence par `kristals/qc-pri-ma-026/`, aucune entrée absolue, `..`, aucun parent `Frames_202...`, aucun autre ID/registre; première entrée à la racine du Kristal. Test CRC par `testzip()` et lecture des JSON contenus. Comparaison du manifeste à la liste exacte des 14 fichiers.
9. **Accessibilité et droits (contrôles textuels)** : versions textuelles des horaires, dates explicites lors des changements de jour, modalités équivalentes et conventions affichées; aucun média tiers ni données personnelles; scénarios déclarés originaux. Ces contrôles textuels ne constituent ni un test utilisateurs ni un avis juridique.

## Limites qui demandent une revue humaine

- Lisibilité et charge cognitive de chaque énoncé, correction des variantes de français québécois, pertinence de la progressivité et robustesse de la grille chez différents élèves.
- Passation réelle des deux preuves indépendantes, juste niveau d’aide, adaptation aux élèves ayant des besoins particuliers, biais culturels; épreuve locale à essayer avant usage à enjeu.
- Variations futures : toute modification du seed/domaine doit produire un **nouveau corrigé** et subir les mêmes vérifications; le générateur n'est **pas un service d'examen certifié**.
- Documentation des méthodes EEF/IES/CAST uniquement lue dans le workspace; vérification des pages externes non faite. Aucun audit officiel du PFEQ/Progression, aucune licence tierce à certifier.
- Aucun test de build canonique, publication, hébergement, intégration LMS ni procédure Framework `build-v9` exécuté; le livrable est strictement un **delta pédagogique** Markdown/JSON.

## Modifications de structure proposées, **non appliquées**

- Ajouter un outil central de vérification des schémas natifs v1.2 et des seeds/modèles paramétriques avec contrôleur en date-ordinale indépendant.
- Ajouter une trace par passation distincte pour `q-011` et `q-012` hors du contenu canonique, avec indication des aménagements et de l'autonomie.
- Ajouter à l'avenir un champ facultatif de qualification humaine et de tests élèves avant toute activation.

**Fusion :** extraire le ZIP depuis le répertoire maître `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`; les 2 chemins authoring remplacent les existants et les 12 autres chemins s'ajoutent. Aucun élément global du workspace n'est inclus.
