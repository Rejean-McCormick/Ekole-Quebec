# Validation et journal de livraison — `qc-pri-mu-007` (v1.2)

**Périmètre :** delta fusionnable du seul Kristal `qc-pri-mu-007`. **Archive de base réellement utilisée :** `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip`, dossier intégré `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Ce lot apporte deux remplacements complets d'`authoring/` et douze nouveaux fichiers; il ne livre ni n'altère les fichiers communs.

## Travail réalisé

1. Lecture préalable des trois documents de gouvernance v1.2, des relations du graphe, des quatre fichiers d'auteur source (`PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md`); front matter du PARCOURS repris à l'identique et ses douze sections intégralement rédigées.
2. Contenus rédigés : quatre notions définies, **deux exemples résolus** à deux parties, **quatre contre-exemples**, **deux diagnostics**, **trois pratiques guidées** (indices dégressifs), **quatre pratiques autonomes**, **deux transferts**, tableau de feedback/remédiation et rappel différé.
3. Création d'une banque **JSON stricte à douze items fixes distincts**, tous reliés à `obj-1`, `crit-1`, `qc-pri-mu-007-ev-01`, avec stimuli, réponses observables, critères, rétroactions et limites de variation; **aucune note basée sur goûts ou capacités physiques**.
4. Deux preuves de maîtrise distinctes : **`q-009` atelier sonore / rôle A** et **`q-010` jardin scolaire / rôle B**, sur motifs, nuances et erreurs différents, à des occasions distinctes; grille 0/1/2, cinq dimensions et décision non fondée sur un total.
5. Mise à jour additive des paramètres de la famille native dans `CONTRAT_PEDAGOGIQUE.json`, sans supprimer de champ v1.2, sans modifier `objectif_id`, `objectif_observable`, préalable ou liens; champs éditoriaux de statut mis à jour pour signaler les items rédigés **à revoir**.
6. Références internes et externes distinguées de la création originale; aucune partition ou captation externe incorporée.

## Contrôles techniques réellement exécutés

Contrôle local par Python sur le dossier préparé **puis sur le ZIP final**; les assertions sont reproductibles sur l'archive rendue. Tests exécutés :

- [x] Source d'origine présente; identités et liens confrontés aux documents lus et au graphe, préalable unique `qc-pri-mu-002`, ordre non bloquant `qc-pri-mu-003` et `qc-pri-mu-005`.
- [x] Front matter YAML d'origine conservé et parsable; douze sections numérotées 1 à 12, sans doublon; objectif et preuve intangibles préservés.
- [x] Contrat JSON analysable; champs et métadonnées non éditoriales d'origine conservés; champs minimum de famille ajoutés sans rupture de schéma natif; type `observation_ou_production` inchangé.
- [x] Banque JSON analysable : format, famille, objectif, critère, 12 identifiants uniques et séquentiels; modes `fixe`, seeds et paramètres nuls cohérents; consigne, stimulus, réponse, critères, feedback et règles de variation non vides.
- [x] Alignement interne plan ↔ items et grille; deux contextes de maîtrise distincts et observables, rôle A puis rôle B, sans indice correctif.
- [x] Vérification structurelle des **partitions à quatre battements** et des erreurs scénarisées des deux preuves; corrigés relus en regard des positions fixes (aucun solveur général ou logiciel de reconnaissance sonore testé).
- [x] Présence et cohérence des effectifs pédagogiques annoncés : 2 exemples, 4 contre-exemples, 2 diagnostics, 3 guidées, 4 autonomes, 2 transferts.
- [x] Liens Markdown relatifs existants dans les 14 fichiers livrés; liens vers le graphe et la gouvernance laissés à leur emplacement du workspace maître sans copie.
- [x] Mentions de précautions sonores, accessibilité multimodale, droits et confidentialité; aucune œuvre enregistrée externe livrée.
- [x] ZIP ouvert et relu : 14 entrées physiques **exactement**, chacune non vide et UTF-8; aucun chemin absolu, `../`, dossier englobant ou ID d'un autre Kristal; premier chemin `kristals/qc-pri-mu-007/`; manifeste égal aux 14 entrées; test d'intégrité CRC passé.

## Limites non résolues et contrôles non exécutés

- **Revue humaine de didactique musicale non réalisée** : choix de complexité pour l'âge, précision des nuances, adaptation aux divers moyens de perception/production, égalité de difficulté entre contextes A et B.
- **Essai sur apprenants non exécuté** et **fidélité interévaluateurs non mesurée**; seuil des cinq dimensions × deux preuves proposé comme règle interne, à calibrer.
- **Aucune reconnaissance audio, notation automatisée ni moteur génératif exécuté**. Les 12 items sont fixes; `seed=null` est intentionnel, et les adaptations possibles ne sont pas des variantes instrumentées et validées. Les corrigés sont des règles de battements décrites et vérifiées sur le corpus limité, non une certification d'items.
- **Droits de redistribution du workspace source non vérifiés auprès du détenteur**; liens vers Khan Academy, OMS et Santé Canada cités comme documentation consultée, sans autorisation de reproduction implicite. Autorisations de captation, hébergement et purge à définir par l'établissement **si** de l'audio est recueilli.
- Pas de validation d'un build Framework/JavaScript, pas d'intégration LMS, pas de revue de conformité PFEQ et pas de publication. Les adaptations pour handicaps sensoriels/moteurs nécessitent un examen d'équivalence avant usage à enjeu.

## Changements de structure proposés seulement (rien de central modifié)

1. Ajouter au schéma central un champ facultatif `preuve_en_interaction_temps_reel` distinguant les activités d'entraînement sur piste fixe des preuves coopératives.
2. Prévoir une description structurée `script_ecart_partenaire`, `condition_reprise` et `adaptation_validee`, et versionner un corpus de partitions accessibles validées par des correcteurs humains.
3. Documenter dans un protocole central la traçabilité d'observation de performance et les règles de consentement/rétention audio lorsque la capture est nécessaire.

## Fusion

Décompresser le workspace maître puis se placer **dans** `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` avant d'extraire `qc-pri-mu-007_livraison_v1.2.zip`. L'archive commence à `kristals/qc-pri-mu-007/` et ne contient **ni** `Frames_202_.../` **ni** un dossier au nom de l'archive. **Statut :** rédigé et testé techniquement, à revoir pédagogiquement; ni publié, ni homologué, ni certifié.
