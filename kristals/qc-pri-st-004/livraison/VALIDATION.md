# VALIDATION — livraison `qc-pri-st-004` (v1.2)

**Périmètre :** delta d'un seul workspace, **deux remplacements** (`authoring/PARCOURS.md` et `CONTRAT_PEDAGOGIQUE.json`) et **douze nouveaux fichiers**; aucune base centrale incluse. **Source vérifiée :** dossier `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` à l'intérieur de `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip`.

## Contrôles techniques réellement exécutés

Les contrôles ci-dessous ont été effectués par un script local Python lisant les fichiers du lot et les fichiers d'origine. Les scénarios et corrigés numériques ont aussi été contrôlés par comparaisons arithmétiques explicites, sans prétendre qu'un enseignant a validé pédagogiquement les items.

- [x] Manifeste de 14 chemins exacts sans doublon
- [x] Toutes les entrées référencent le Kristal exact
- [x] Aucun fichier supplémentaire, 14 fichiers non vides
- [x] Métadonnées contractuelles d’origine conservées récursivement
- [x] Objectif, critère, préalable et famille inchangés
- [x] Paramètres gouvernance présents dans la famille
- [x] Front matter YAML valide
- [x] Métadonnées YAML source préservées
- [x] 12 sections numérotées exactement dans PARCOURS
- [x] PARCOURS réfère aux deux contextes de maîtrise
- [x] JSON parsables (banque, contrat, manifeste)
- [x] Format banque et famille conforme
- [x] 13 items, identifiants uniques et numérotation continue
- [x] Champs JSON obligatoires sur tous les items
- [x] Tous liens objectif, critère, famille exacts
- [x] Difficultés, modes et statut des items conformes
- [x] Énoncés, réponses, feedback, limites, traces non vides
- [x] Variations de scénarios contrôlées et explicites
- [x] Aucune correction ou génération IA libre déclarée
- [x] Deux preuves autonomes réellement distinctes
- [x] Scénarios / stimuli distincts
- [x] Plan énumère les 13 items et liens communs
- [x] Grille exige 2 manifestations et autonomie
- [x] 2 diagnostics, 3 guidés, 4 autonomes, 2 transferts
- [x] 2 exemples résolus et 2+ contre-exemples
- [x] Accessibilité et sécurité explicitement décrites
- [x] Droits et nature fictive documentés
- [x] Tous les nombres-clefs présents dans stimulus ET corrigé
- [x] Calculs comparatifs et différences évalués
- [x] Tous les liens locaux de fichiers résolus
- [x] Aucune entrée physique dans dossier interdit
- [x] Contrat graphique vérifié : exactement trois relations sortantes
- [x] Tous les contrôles préarchive réussis

## Vérification ciblée des réponses

- Les 13 stimuli ont des textes distincts et des valeurs-clés présentes dans les réponses de référence; un contrôle indépendant a recalculé les comparaisons : `18−12=6`, `60>50`, `65>45`, `3>1`, `8>5`, `4>2` et `4<5`, `2>1`, `6>4`, `7<11`, `7>3`, `140>105`, `130>100`, `5>3`, `3>1` et, pour l'autre fiche d'ombre, `18−12=6`.
- La précision des descriptions de situations, le caractère prudent des conclusions, l'absence de causalité prouvée avec des données insuffisantes et les limites énoncées ont été **relus éditorialement dans le cadre de cette production**; cela ne constitue pas un essai en classe ni une évaluation indépendante.
- Les données sont **fictives** et aucune expérience n'a été réalisée. Le document `sources/REFERENCES_CONTENU.md` distingue explicitement principes vérifiés, interprétations dérivées et créations originales. Les droits réels de diffusion de l'archive source ne sont pas établis.

## Limites non résolues

1. **Revue humaine non exécutée :** expertise en didactique des sciences, validité du seuil « niveau 2 à chaque critère dans deux contextes », fidélité entre correcteurs, niveaux de langue et charge cognitive.
2. **Aucun test sur apprenants**, aucune étude de biais ou d'équité en situation réelle, et aucune qualification d'item à enjeu.
3. **Aucun moteur de génération exécuté** : le contrat de famille garde le type `generee_sous_contraintes`, mais seules les 13 versions de référence ont été produites; les présentations alternatives nécessitent contrôle humain avant usage. Pas de seed pseudo-random factice ni de correction IA libre utilisée comme oracle.
4. **Licences et diffusion** : droits d'utilisation de l'archive source à confirmer par son détenteur; liens NASA/NRC sont des références vérifiées, pas des autorisations de reproduction.
5. Les chemins `registry/`, `governance/` et `kristal.workspace.json` n'ont été ni modifiés ni inclus; validation Framework/build-v9, LMS, publication et activation **non exécutées**.

## Revue humaine et propositions sans modification de structure

- Faire relire les 13 consignes/rubriques, vérifier l'accessibilité des contenus oraux et la clarté du concept « observation versus explication ».
- Faire coter de manière indépendante les deux tâches de maîtrise par deux personnes, comparer les désaccords, puis affiner les exemples d'ancrage de la grille si nécessaire.
- **Proposition centrale seulement (non appliquée) :** ajouter au schéma de famille un champ optionnel pour distinguer `mode_de_famille` du `mode_item_operationnel` et pour documenter une version approuvée du corpus de scénarios; éventuellement définir un registre central de variantes vérifiées. Aucun nouveau lien de graphe, objectif ou critère n'est demandé ici.
- **Proposition centrale seulement (non appliquée) :** préciser un protocole de conservation des traces d'oral/transcription et de revue des biais dans l'évaluation autonome.

## Fusion et qualification

Extraire `qc-pri-st-004_livraison_v1.2.zip` **à l'intérieur** de `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Ne pas ajouter de dossier parent. Valider la fusion sur une copie de l'archive maîtresse. Le contenu est **rédigé, techniquement contrôlé, à revoir humainement**; ni publié, ni homologué, ni certifié.
