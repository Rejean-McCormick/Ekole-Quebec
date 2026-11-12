# Validation de livraison — `qc-pri-mu-002` (v1.2)

**État :** delta rédigé; revues musicale, d'accessibilité, de sécurité et de cotation humaines requises. Aucune certification ni homologation PFEQ.

## Inventaire et frontières

- 14 chemins stricts sous `kristals/qc-pri-mu-002/` : deux fichiers `authoring/` remplacent les fichiers du maître, 12 sont ajoutés.
- Aucun fichier central ou d'un autre Kristal livré. Aucun `AGENTS.md`, fichier `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, `kristal.workspace.json`, `docs/`, `canon/`, `state/`, `runtime/`, `registry/` ou `governance/` n'est modifié.
- `obj-1`, `crit-1`, titre, discipline, liens `requires/reinforces`, famille `qc-pri-mu-002-ev-01` et mode `observation_ou_production` préservés de la source.

## Tests réellement exécutés

- **544 assertions préarchivage réussies**, zéro échec. La vérification a été exécutée sur les contenus réellement présents le 8 octobre 2026.
- **Source et identité :** YAML du parcours parsé, 12 sections numérotées dans l'ordre, clés et champs canoniques identiques à ceux de l'archive v1.2, objectif, preuve, concepts, graphe et famille préservés. Contrat JSON et métadonnées de génération préexistantes conservés et enrichis sans rupture.
- **Banque d'évaluation :** 10 items JSON uniques, complets et `a_revoir` ; consignes, stimuli, solutions/rubriques, feedback et niveaux présents. Items 009 et 010 séparés, modèles fixes, exigence de deux répétitions de reproduction et de création.
- **Solutions et contraintes :** énumération indépendante des **six permutations valides de `A,A,H,R`**, vérification des quatre cases, de l'unique `H` après attaque, des deux attaques et d'un silence; au moins quatre choix d'invention B encore disponibles après l'épreuve A. Les réponses musicales humaines n'ont **pas** été testées avec des élèves.
- **Contenus :** contrôles automatiques de la présence de deux exemples commentés, deux contre-exemples, deux diagnostics, trois pratiques guidées dégressives, quatre pratiques autonomes, deux transferts, rappels, sécurité et accessibilité. Vérification de droits documentaire, non avis juridique.
- **Fusion simulée :** extraction des fichiers du dossier source original de ce Kristal dans un espace temporaire, **2 remplacements des fichiers authoring et 12 ajouts**, SHA-256 identique pour tous les autres fichiers sources locaux; aucune autre racine présente dans le delta.
- **Archive ZIP :** test CRC, JSON relus depuis l'archive, 14 chemins et manifeste exacts, aucune entrée supplémentaire ni chemin absolu ou traversée `../`, exécutés lors de la dernière étape du script.

## Incertitudes et limites non résolues

- **Aucun essai sur élèves** : l'efficacité pédagogique, la facilité des gestes, la qualité acoustique, la lecture des symboles, l'équité et la fiabilité de la grille restent à tester.
- **Volume réel non mesuré** : l'adulte devra adapter et surveiller l'environnement sonore. Aucune exposition forte exigée. Une modalité gestuelle équivalente doit être validée humainement selon le besoin, non présumée automatiquement.
- **Notation locale** : `A/H/R` et quatre temps constituent un code d'apprentissage défini ici, pas une représentation universelle des rythmes ni un cycle d'études attribué au PFEQ.
- **Révisions** : les dix items ont `validation_status="a_revoir"`, aucune certification et aucune mise à l'essai instrumentée.

## Revue humaine demandée

1. Enseignant de musique : notion de pulsation et mesure simple, fidélité des événements tenus, clarté des motifs.
2. Référent accessibilité : comparabilité des indices sonores/visuels/tactiles et réalisme des gestes accessibles.
3. Personne responsable sécurité : volume, fatigue sensorielle, consentement aux observations et contexte de classe.
4. Évaluateurs : accord intercorrecteurs sur pulsation à tempo choisi, deux reprises, motifs nouveaux et seuils M1–M5.

## Évolutions structurelles proposées, sans modification centrale

- Proposer pour la prochaine révision du schéma un objet optionnel de **notation musicale locale** (symbole, durée en pulsations, condition de validité) afin de rendre les choix d'accessibilité auditables.
- Proposer un champ d'**équivalence d'accès approuvée** attaché aux observations LMS, et un registre de la modalité perceptive choisie par l'élève, sans stocker d'information médicale.
- Proposer une table canonique de **critères non compensatoires** et de preuves indépendantes sans toucher au graphe, aux autres Kristals ou au canon v9.
