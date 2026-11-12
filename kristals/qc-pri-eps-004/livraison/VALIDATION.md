# Validation de livraison — `qc-pri-eps-004`

**État :** contenu rédigé, banque d’items instrumentée, contrôles techniques effectués; **revue humaine et essai sur le terrain requis**. Il ne s'agit ni d'un cours publié, ni d'une épreuve certifiée, ni d'une homologation PFEQ.

## Périmètre de la livraison

- Base de fusion : `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` ; archive : `qc-pri-eps-004_livraison_v1.2.zip`.
- Exactement **14 chemins** sous `kristals/qc-pri-eps-004/` : remplacement complet des 2 fichiers d'`authoring/`, ajout des 12 fichiers nouveaux.
- Les fichiers `kristal.workspace.json`, `AGENTS.md`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, `docs/`, `canon/`, `state/`, `runtime/`, `registry/`, `governance/` et tous les autres Kristals ne sont pas livrés ni réécrits.
- **Relations conservées :** `requires = []`, `recommends_before = [qc-pri-eps-001]`, famille `qc-pri-eps-004-ev-01`, `obj-1`/`crit-1` et objectif/preuve inchangés.

## Contrôles exécutés, résultats

- **188 assertions de prévalidation réussies** via `verify_eps004.py` : comparaison du YAML source, ses métadonnées et 12 sections, conservation des champs natifs JSON, relations du graphe, objectif/preuve, contrat de famille et sécurité.
- JSON `CONTRAT_PEDAGOGIQUE.json`, `BANQUE_ITEMS.json`, `MANIFEST.json` analysés par `json.loads`; frontmatter `PARCOURS.md` analysé par `yaml.safe_load`.
- Dix items identifiés sans doublon de `q-001` à `q-010` ; chacun lié à `obj-1`, `crit-1`, `qc-pri-eps-004-ev-01` et contient consigne, situation, preuve/rubrique, feedback, statut `a_revoir`, sécurité et limites de variation.
- Deux tâches de maîtrise séparées : `q-008` (lancers de sacs souples au poste de tri) et `q-009` (conduite d'une balle mousse au poste de livraison) ; chaque tâche exige deux séries mesurées avec réglage de geste par l'élève.
- Les contenus vérifiés mentionnent les deux contre-exemples, deux diagnostics, trois tâches guidées, quatre autonomes, deux transferts et rappels différés.
- **Contrôles finaux effectués par le même vérificateur :** test CRC du ZIP; 14 entrées exactement, ordre et racine correcte, interdiction de `../` et de chemin absolu; fusion simulée par superposition sur une extraction complète du ZIP maître et comparaison des fichiers préexistants protégés. Ces contrôles sont requis pour accepter ce livrable; le script interrompt la livraison s'ils échouent.

## Points effectivement évalués et limites

- **Corrigés :** chaque tâche motrice possède une preuve attendue descriptive, une règle de comptage et cinq critères communs; cette vérification est structurelle et de cohérence, **pas une mesure empirique de fidélité interjuges**.
- **Sécurité :** contrôles textuels de supervision, matériel souple, stabilité, arrêt en cas de danger. Les postes **n'ont pas été essayés physiquement**; vérifier les objets, allergies, dimensions et trajectoires pour le lieu réel.
- **Accessibilité :** posture assise, repères alternatifs et matériel adapté prévus. Leur caractère équivalent pour chaque élève demande une décision professionnelle individuelle et, au besoin, l'avis de spécialistes.
- **Droits :** sources externes référencées par nom et URL; aucun dessin, barème tiers ou visuel reproduit. Analyse de licences détaillée et vérification éditoriale humaine non menées.
- **Liens :** les chemins inclus et identifiants sont vérifiés; un import dans LMS, les ressources externes futures et le Framework canonique v9 ne sont **pas** testés.

## Revue humaine avant qualification

1. Enseignant d'EPS : sûreté de la conduite de séance, interprétabilité des critères et alternatives lorsque les progrès de mesure sont fluctuants.
2. Équipe de soutien/adaptation : accessibilité sensorielle, motrice et communications alternatives, stabilité du poste en fauteuil et prévention des blessures.
3. Évaluateurs indépendants : lecture commune des rubriques et accord interobservateur après essais avec élèves volontaires selon procédures autorisées.
4. Responsable des contenus et des droits : licences éventuelles du matériel de classe et pertinence culturelle/linguistique.

## Propositions de structure (non appliquées)

- Envisager, **par proposition centralisée versionnée**, un schéma facultatif de `fiche_observation` (séries, modalités et contexte) distinct du canon et du contrat d'évaluation.
- Évaluer à l'échelle du programme un champ de description d'adaptation approuvée et un état « non observable », sans créer une dépendance obligatoire vers `qc-pri-eps-001`.
- Aucune modification effectuée aux métadonnées globales, au graphe ou aux IDs gelés.
