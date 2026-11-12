# Validation de livraison — qc-pri-fr-005 (delta v1.2)

**Archive visée :** `qc-pri-fr-005_livraison_v1.2.zip` ; **racine interne :** `kristals/qc-pri-fr-005/` ; **statut :** contrôles techniques locaux effectués, **revue humaine requise**. Aucun statut « publié », « homologué » ou « certifié ».

## Inventaire livré

- **2 fichiers existants remplacés sans perdre leurs propriétés structurantes :** `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`.
- **12 fichiers nouveaux :** six dans `contenu/`, trois dans `evaluation/`, un dans `sources/`, deux dans `livraison/`.
- Le manifeste énumère **14 chemins complets**, sans entrée libre à la racine. Le ZIP est prévu pour décompression **dans** le dossier `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` du workspace source.

## Contrôles effectivement automatisés au moment de l'empaquetage

Un programme local (`verify_delivery.py`, **outil de préparation hors du ZIP**) a inspecté les **octets du ZIP final**, les versions sources dans `initbundle(1).zip`, les fichiers de gouvernance et l'entrée correspondante du graphe :

| Contrôle | Résultat attendu et constaté | Portée réelle |
|---|---|---|
| Structure et chemins | **PASS** : 14 fichiers non vides, premier chemin sous `kristals/qc-pri-fr-005/`, aucune entrée absolue ou `../`, aucun second workspace, pas de fichier réservé. | Contrôle d'empaquetage, pas test de déploiement. |
| Manifeste et JSON | **PASS** : `MANIFEST.json`, `CONTRAT_PEDAGOGIQUE.json`, `BANQUE_ITEMS.json` parsables en JSON strict; liste manifeste identique à la liste ZIP. | Test syntaxique et de concordance, pas validation contre un schéma JSON officiel indépendant. |
| YAML et sections | **PASS** : frontmatter YAML parsable, mêmes clés et valeurs d'identité canoniques (hormis révision éditoriale `0.3.0`), douze sections numérotées dans le même ordre. | Vérification de structure; la rédaction est nouvelle. |
| Identité et graphe | **PASS** : `qc-pri-fr-005`, titre, objectif `obj-1`, critère `crit-1`, absence de `requires`, conseil `qc-pri-fr-003`, famille `qc-pri-fr-005-ev-01`; métadonnées originales du contrat conservées et champs réglementaires ajoutés à la famille existante. | Comparaison avec l'archive locale; aucun fichier global modifié. |
| Items | **PASS** : 12 IDs consécutifs `q-001`–`q-012` sans doublons, champs requis présents, niveaux autorisés, modes fixes, 12 chaînes d'indice retrouvées **littéralement** dans leur stimulus, réponses contenant les indices. | La correspondance de chaînes ne démontre pas à elle seule la pertinence linguistique de chaque clé. |
| Contextes / couverture | **PASS** : A/B/C comptent chacun 4 items, A (récit) et B (avis) ont des stimuli différents; chaque notion est échantillonnée trois fois. | Deux manifestations **prévues**, non administrées à de vrais élèves. |
| Matériel et liens | **PASS** : deux diagnostics, trois guidages, quatre pratiques autonomes, deux transferts identifiables; fichiers internes annoncés présents; références de gouvernance et d'alignement présentes dans l'archive source. | Pas de navigation LMS ni audit exhaustif de tous les hyperliens web externes. |
| Droits / données / sécurité | **Revue documentaire seulement** : textes rédigés ici, aucun élément tiers incorporé intentionnellement; noms et scènes fictifs. | **Aucun** scan de similitude, audit légal, contrôle de données réelles ou essai d'accessibilité auprès d'utilisateurs n'a été réalisé. |

## Vérifications rédactionnelles effectuées, sans certification

- Relire les douze paires **question/réponse/indice** de la banque et vérifier que la citation ciblée correspond au sens de la question; comparer lieu d'arrivée et lieu de l'action, personne qui agit et personne mentionnée, moment cité et heure inventée.
- Séparer compréhension de textes et écoute du décodage, de l'orthographe et de la performance orale; prévoir lecture neutre et transcription fidèle sans pointer les réponses.
- Contrôler qu'aucun exemple d'enseignement ou exercice d'entraînement ne reprend les **stimuli des deux contextes probatoires A et B**.
- Aucun générateur paramétrique n'a été mis en place : modes `fixe` seulement, `seed=null`, `parametres=null`, variation de modalité seulement.

## Limites non résolues et revue humaine nécessaire

1. **Expertise pédagogique et linguistique fr-CA :** faire relire tous les textes, les situations à double acteur, les variations acceptables de citation, l'équilibre de difficulté A/B et le niveau de lecture/écoute. Ce contrôle n'a pas été réalisé auprès d'un expert indépendant.
2. **Étalonnage du seuil :** la règle 4/4 exacte + 4/4 indices dans deux genres est un **choix interne proposé**, non un seuil empiriquement validé; recueillir des observations d'élèves et documenter toute modification future.
3. **Accessibilité en usage réel :** vérifier lecture d'écran, mise en page, diction des textes, compréhension de la consigne, équivalence des adaptations avec des utilisateurs et un spécialiste; seulement des précautions documentaires ont été appliquées.
4. **Droits et provenance :** contenus originaux produits ici mais vérification d'originalité, de similitudes éventuelles, et revue légale à effectuer avant diffusion. Les pages EEF/IES/CAST n'ont pas été ouvertes directement; seules leurs références dans le document de gouvernance ont été consultées.
5. **Tests de plateforme :** aucune intégration LMS, aucune commande canon/build/publish/activate ni déploiement du delta dans un workspace de production n'a été exécuté. `kristal.workspace.json`, `canon/`, `registry/`, `governance/`, `state/` et `runtime/` restent intacts.
6. **Variation future :** si de nouveaux stimuli sont proposés, effectuer contrôles sémantiques, rubrication, revue des droits et pilotage séparés avant tout usage sommatif. La validation de chaînes actuelle ne permet pas un tirage IA libre fiable.

## Journal des changements et propositions sans modification centrale

- Conservé : identité v1.2, objectif observable, preuve de maîtrise, liens, family ID, champs natifs du contrat, référence d'alignement et 12 rubriques de `PARCOURS.md`.
- Ajouté : contenus enseignables, diagnostic, exercices avec corrigés, deux transferts, banque fixe de 12 items, évaluation et grille, provenance et manifeste.
- **Proposition de structure, non appliquée :** un schéma JSON officiel pour `BANQUE_ITEMS.json` et `MANIFEST.json`, un validateur des citations sémantiques et un stockage externe des preuves apprenants. Aucun registre, graphe, fichier de gouvernance ou canon n'a été modifié dans le ZIP.

**Qualification interne :** **delta techniquement vérifié et prêt pour revue humaine**, pas cours publié ni items certifiés.
