# Validation — qc-pri-us-002 v1.2

**Périmètre** : delta unique du Kristal `qc-pri-us-002`, deux remplacements complets `authoring/` et douze nouveaux fichiers; aucun changement aux bases communes. **État** : banque `a_revoir`; revue pédagogique humaine indispensable.

## Contrôles effectués

- Lecture des trois règles de gouvernance, des quatre fichiers locaux demandés et du graphe v1.2 depuis l’archive source.
- Conservation des valeurs v1.2 (ID, titre, `obj-1`, texte objectif, `crit-1`, preuve, zéro prérequis, familles et références) et des champs JSON du blueprint; ajouts sans perte des champs natifs.
- Création de cartes A–G fictives avec légendes et flèches explicites, lecture des cases et distances des trajets par un algorithme indépendant; contrôle des obstacles et distances de scénarios.
- Vérification du nombre et de l’unicité des items, de leurs deux variantes fermées le cas échéant, et des deux contextes de maîtrise; conformité des JSON.
- Vérification de la présence des 14 fichiers requis, non vides, sous le bon préfixe, sans chemin dangereux et en ordre, de la cohérence du manifeste et de l’intégrité du ZIP (test CRC).

## Tests réellement exécutés — rapport chiffré

**46 contrôles réussis sur 46**, exécutés par `test_us002.py` sur l’archive assemblée : **40 contrôles avant empaquetage et 6 contrôles sur le ZIP**. Ce décompte porte sur les assertions groupées affichées par le vérificateur, non sur une expertise humaine. Parmi les points effectivement testés :

- Relecture du YAML initial et livré; les **12 sections** sont numérotées, l’en-tête d’origine et ses valeurs sont conservés.
- Préservation récursive de **tous les champs natifs** du JSON de contrat, invariants de titre, objectif, preuve, préalables et famille; vérification du graphe de renforcement.
- **10 items sans doublon**, dont **6 scénarios contrôlés × 2 variantes = 12 variantes** complètes à sélection de graine vérifiée; **2 preuves inédites** sur cartes F/G et non présentes dans les six modules enseignés.
- **16 stimuli cartographiques** parsés en quadrillages (12 variantes et 4 items fixes), **12 parcours** recalculés cellule par cellule, obstacles exclus, **7 parcours minimaux** vérifiés par recherche en largeur (BFS) indépendante des valeurs de réponse.
- Présence des six modules, des deux diagnostics, trois tâches guidées, quatre pratiques autonomes, deux transferts et des propositions d’accessibilité/sécurité; existence des références consultées contrôlée dans le texte.
- **14 fichiers exactement** et non vides à la racine `kristals/qc-pri-us-002/`, ordre identique au manifeste, aucun fichier interdit, aucun chemin externe/traversant, **3 JSON reparsés directement depuis le ZIP**, contrôle CRC et comparaison octet pour octet avec les fichiers produits.

Les scripts de production et de test sont restés **hors du ZIP**. Aucun résultat d’essai auprès d’élèves, ni audit externe de droits, ni contrôle d’un LMS, ni certification ne sont revendiqués.

## Limites non résolues et revue humaine

1. Une personne spécialiste doit vérifier la lisibilité des grilles, la formulation des consignes, le niveau de complexité et l’adéquation à des élèves aux profils variés.
2. La manipulation du quadrillage peut nécessiter supports tactiles ou adaptation en LMS; ces adaptations ne sont pas testées en situation réelle.
3. Les corrections sont des modèles; des trajets alternatifs minimaux doivent être acceptés après vérification par les règles.
4. Les preuves q-009/q-010 utilisent des cartes inédites F/G, distinctes des cartes A–E enseignées. Si ces cartes ont néanmoins été corrigées devant un élève, les remplacer par des situations nouvelles relues humainement.
5. Les titres, distances et lieux sont fictifs; aucune vérification de sentiers, toponymie réelle ou sécurité terrain n’a été faite ou revendiquée.
6. Aucune homologation PFEQ, revue de droits externe ou qualification d’examen n’est revendiquée.

## Propositions de structure, sans changement du workspace

- Définir à l’avenir un format commun de carte-grille à paramètres typés (symboles, nord, voisins, échelle) afin d’éviter les contradictions graphiques.
- Ajouter au pipeline central un validateur des chemins d’items et un journal séparé des deux preuves de maîtrise, sans écrire ces données dans le canon.
- Maintenir une banque de contextes de remplacement, relus humainement, lorsque des cartes ont déjà été enseignées.
