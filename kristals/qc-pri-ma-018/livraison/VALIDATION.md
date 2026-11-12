# Journal de validation — `qc-pri-ma-018` (v1.2)

**Objet :** delta fusionnable de 14 fichiers; base d'entrée : `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. **Statut :** rédaction complète, tests techniques et arithmétiques exécutés, **revue pédagogique humaine requise**. Aucun statut « certifié », « homologué » ou « publié ».

## Contrôles réellement réalisés pendant la construction

1. **Lecture effective des sources** : contrat v1.2, générateur, charte de conversion, graphe 202, parcours, contrat JSON, alignement et brief locaux présents dans l’archive source.
2. **Identité et invariants :** même ID `qc-pri-ma-018`, titre « Relations et égalités numériques », discipline `MA`, objectif `obj-1`, critère `crit-1`, famille `qc-pri-ma-018-ev-01`, preuve et concepts; aucune relation entrante/sortante dans le graphe central; tableaux de préalables et ordre vides maintenus.
3. **YAML :** enveloppe initiale conservée, révision éditoriale portée à `0.3.0`, exactement 12 sections numérotées; les autres métadonnées canoniques conservées. Le statut reste `en_rédaction`.
4. **Contrat JSON :** champs/famille v1.2 préservés, informations minimales de génération ajoutées dans l’objet famille, JSON strict parsable; `validation_status = a_revoir`.
5. **Banque :** 10 ID distincts, q-001 à q-010, tous liés explicitement à `obj-1`, `crit-1` et `qc-pri-ma-018-ev-01`; cinq items fixes et cinq paramétriques, 2 preuves dans les contextes indépendants jetons/jardin.
6. **Générateurs :** énumération exhaustive de toutes les combinaisons autorisées : q-002 = 351, q-004 = 1053, q-006 = 299, q-009 = 630, q-010 = 1596 cas, soit 3929 cas, avec solution entière non négative unique par coefficient unitaire et égalité testée des deux membres. Instanciations seed calculées, exemples de référence et vérifications comparés aux stimuli.
7. **Corrigés pédagogiques :** substitution exacte contrôlée pour les générateurs; les exemples fixes, guidés, pratiques et transferts ont été calculés et revérifiés dans le script de validation pour les égalités numériques listées; les grilles demandent une justification indépendante de la réponse.
8. **Droits/accessibilité/sécurité :** inspection éditoriale des supports produits (énoncés originaux, aucune pièce tierce insérée, alternative textuelle, modalités orales/dessinables, pas de données privées); ceci ne vaut **ni audit juridique ni test utilisateur d'accessibilité**.
9. **Condition de fusion :** 14 fichiers dans le manifeste, tous non vides, seuls deux remplacements `authoring/` du Kristal ciblé et douze créations; contrôle des chemins, JSON et simulation de superposition intégrale exécutés par le script de validation externe après génération du ZIP (résultat indiqué en sortie du script; ne signifie pas un test du Framework v9).

## Revue humaine requise / limites non résolues

- Vérifier clarté des scénarios et consignes, acceptabilité des modèles de réponses, niveaux de difficulté, critères observables pour l'âge et la diversité des apprenants; essayer les tâches auprès d'élèves réels.
- Tester concrètement lecteurs d'écran, sortie audio, matériel manipulable et déroulement LMS; aucune exécution sur dispositif d'assistance ni collecte de données d'apprentissage.
- Ne pas confondre validation arithmétique du générateur et validité psychométrique ou certification des items.
- Les cas limites hors plages de paramètres ne sont pas couverts; toute modification des domaines exige retests et revue humaine.
- Aucune exécution du CLI local `kristal.py check/build-v9/check-ai`, aucun audit canon, aucune homologation PFEQ, aucune publication/activation.

## Propositions (aucun changement apporté aux structures centrales)

- Proposer au niveau central un schéma optionnel décrivant `preuve_maitrise` et les métadonnées de contexte pour les familles d'items.
- Ajouter ultérieurement au dispositif de livraison un validateur commun de seed, de domaines, de contraintes et de dérivation de corrigé indépendant de l’IA.
- Mettre en place un journal d’essais apprenants et un protocole de revue humaine des rubriques avant qualification.

**Fichiers interdits :** aucun fichier `registry/`, `governance/`, `docs/`, `canon/`, `state/`, `runtime/`, `AGENTS.md`, `kristal.workspace.json`, ni aucun autre Kristal n'est inclus ou modifié.
