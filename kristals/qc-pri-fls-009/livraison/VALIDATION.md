# Validation technique et limites — `qc-pri-fls-009`

**Version cible :** v1.2. **Delta :** 14 chemins, 2 remplacements complets et 12 nouveaux fichiers. **Statut :** `a_revoir` (contenu instrumenté, non publié, non certifié, non homologué). **Périmètre :** un seul Kristal, aucune modification des dossiers `registry/`, `governance/`, `docs/`, `canon/`, `state/`, `runtime/` ni d'autres identifiants.

## Contrôles réellement effectués

Les assertions du script local de construction ont été **exécutées et réussies** sur les fichiers de cette livraison, y compris sur un ZIP témoin avant l'écriture du présent compte rendu :

1. **OK** — source lue : governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md.
2. **OK** — source lue : governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md.
3. **OK** — source lue : governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md.
4. **OK** — source lue : registry/GRAPHE_PEDAGOGIQUE_202.json.
5. **OK** — source lue : kristals/qc-pri-fls-009/authoring/PARCOURS.md.
6. **OK** — source lue : kristals/qc-pri-fls-009/authoring/CONTRAT_PEDAGOGIQUE.json.
7. **OK** — source lue : kristals/qc-pri-fls-009/authoring/ALIGNEMENT.md.
8. **OK** — source lue : kristals/qc-pri-fls-009/authoring/BRIEF_REDACTION.md.
9. **OK** — 14 chemins attendus sans double.
10. **OK** — 14 fichiers locaux non vides.
11. **OK** — manifeste exact.
12. **OK** — YAML valide et frontmatter canonique strictement identique.
13. **OK** — 12 sections originales une seule fois.
14. **OK** — identité YAML / discipline / statut / objectif.
15. **OK** — racine du contrat: champs existants préservés sans modification.
16. **OK** — famille native et génération préservées intégralement.
17. **OK** — 13 champs de gouvernance famille présents.
18. **OK** — famille / objectif / préalables / ordre intacts.
19. **OK** — arêtes sortantes du graphe concordantes sans renforcement.
20. **OK** — banque JSON format/id/famille.
21. **OK** — 10 items distincts q-001–q-010.
22. **OK** — tous les items complets et statut à revoir.
23. **OK** — niveaux : 4 initiaux, 4 intermédiaires, 2 transferts.
24. **OK** — corrigés modèles contiennent tous les faits verrouillés.
25. **OK** — deux preuves d’autonomie contextes et genres distincts.
26. **OK** — plan référence tous les items obj-1 crit-1 et famille.
27. **OK** — grille conditions conjonctives et double preuve.
28. **OK** — diagnostic, guidages et 4 autonomes.
29. **OK** — deux exemples commentés, deux contre-exemples et transferts.
30. **OK** — droits : statut d’originalité, limites et aucune image jointe.
31. **OK** — accessibilité : adaptations et limites documentées.
32. **OK** — liens relatifs Markdown résolus.
33. **OK** — JSON strict des trois fichiers.
34. **OK** — ZIP témoin : 14 chemins sûrs, JSON, intégrité, fusion 2 remplacements et 12 ajouts.

## Vérifications de contenu réalisées et portée réelle

- **Relecture locale des corrigés :** chaque item comporte une consigne, un stimulus, une réponse modèle ou règle explicite, des critères et une rétroaction. Les modèles ont été relus pour la conservation des faits de la consigne; une assertion a vérifié la présence des faits verrouillés dans chacun des dix corrigés. **Cela ne mesure pas** la validité pédagogique auprès d'élèves, ni la qualité de toutes les réponses alternatives possibles.
- **Évaluation de l'autonomie :** `q-009` et `q-010` sont deux genres de textes distincts (message personnel et annonce collective), avec grille C1–C4 et seuils indépendants. Aucune décision n'est tirée d'une note unique.
- **Droits et sécurité documentaire :** textes et scénarios rédigés pour cette livraison, aucun média tiers ajouté; pas de données privées requises ni de matériel dangereux. Ce contrôle documentaire **n'est pas une expertise juridique**.
- **Accessibilité :** consignes, mode de présentation, clavier et transcription fidèle prévus; **aucun test réel avec technologie d'assistance ou apprenants n'a été conduit**.
- **Source :** le workspace cible et les huit fichiers exigés ont été lus dans l'archive `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip` qui contient `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. La base autonome `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis.zip` n'était pas nécessaire puisque son dossier est déjà présent dans l'archive fournie.

## Limites non résolues / revue humaine obligatoire

1. Vérifier le niveau de langue FLS, les formulations, la lisibilité, la pertinence et la longueur des dix situations avec des spécialistes et des élèves de divers parcours.
2. Examiner l'équivalence de difficulté entre la preuve individuelle A et la preuve collective B; valider la grille sur réponses authentiques et mesurer l'accord entre correcteurs humains.
3. Tester les accommodements concrets (clavier, lecture de consigne, transcripteur neutre), sans donner d'indices de contenu, et vérifier que l'autonomie demeure observable.
4. Revoir les droits et la protection des données lors de l'intégration LMS, puis procéder aux tests propres au système d'exécution/affichage. Aucune publication ou certification présumée.
5. Vérifier le traitement des productions ouvertes par les évaluateurs : aucun correcteur IA automatique n'est validé par ce delta.

## Propositions de structure (non appliquées)

- Ajouter ultérieurement au registre central **par procédure versionnée** un schéma commun de traçabilité d'accommodements et de preuves autonomes, si ce besoin est approuvé; aucun fichier central modifié.
- Prévoir dans l'adaptateur LMS un champ de provenance de correction humaine et deux traces contextuelles distinctes; **aucune évolution de schéma native** n'est imposée ici.
- Si des banques paramétriques sont introduites plus tard, définir validation de générateur et règle de versionnement séparément; les dix items livrés demeurent **fixes** et non certifiés.

## Instructions de fusion

Depuis la racine du workspace maître **`Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`**, extraire `qc-pri-fls-009_livraison_v1.2.zip` directement. Les deux fichiers `authoring/` autorisés sont remplacés sous `kristals/qc-pri-fls-009/`; les douze autres sont ajoutés au même dossier. Aucune autre arborescence n'est embarquée. Le manifeste [MANIFEST.json](MANIFEST.json) est la liste exhaustive.
