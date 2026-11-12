# Validation et journal de livraison — qc-pri-fr-016

**Livraison :** delta fusionnable v1.2 sous `kristals/qc-pri-fr-016/`; aucune modification d'un autre Kristal ni des répertoires globaux. **Source réelle utilisée :** le dossier `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` présent **à l'intérieur** de l'archive fournie `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip` (pas de substitution de métadonnées). **Statut :** rédaction techniquement vérifiée; qualification pédagogique humaine non réalisée.

## Différences produites (journal de changements)

- **Remplacements complets des deux fichiers `authoring/` existants :** frontmatter YAML original du parcours conservé à l'identique (format, identité, titre, objectif, statut et liens); développement des **12 sections**; conservation des clés et de l'identité de la famille du contrat JSON natif, ajout de ses **13 paramètres** v1.2, statuts éditoriaux du contrat/famille ajustés pour indiquer « revue requise ».
- **Douze nouveaux fichiers :** 6 contenus (notions, diagnostic, enseignement, pratique guidée, autonomie, remédiation/transfert), 3 évaluations (plan, 10 items, grille), 1 dossier de sources (références réelles + origine et droits), 2 fichiers de livraison (manifeste et présente validation).
- **Frontières :** aucun `kristal.workspace.json`, `AGENTS.md`, `ALIGNEMENT.md`, aucun registre, aucune gouvernance, aucun autre ID, aucun canon, état, runtime ou dossier docs modifié ou embarqué.

## Contrôles exécutés sur le delta et l'archive

Le lot a été soumis à un script Python local utilisant `json`, `zipfile`, `pathlib`, expressions régulières et `yaml` (PyYAML) :

1. **Identité et structure :** vérification que le manifeste et les chemins livrés donnent **exactement 14 fichiers non vides** sous le seul préfixe `kristals/qc-pri-fr-016/`, sans chemin absolu ni parent `../`.
2. **Schémas existants :** lecture et comparaison à partir du dossier source réel; frontmatter YAML intégralement conservé et parsé; douze sections 1–12 présentes; champs originaux du contrat/famille préservés; ajout des champs attendus; trois JSON correctement analysés.
3. **Cohérence des liens :** comparaison des deux arêtes de `qc-pri-fr-016` avec le **graphe v1.2 réel**; invariants `obj-1`, `crit-1`, famille et prerequisite/ordre; résolution des liens Markdown locaux du delta. Les références à la charte et au graphe central sont descriptives et ne sont **pas** incluses dans ce ZIP.
4. **Banque d'items :** **10 IDs distincts et consécutifs**, champs obligatoires non vides, mode fixe sans paramètre, statut `a_revoir`, niveaux initial/intermédiaire/transfert et deux contextes différents. Les **12 GN corrigés** de la banque ont été comparés à une **liste de solutions verrouillées**, distincte des chaînes du JSON; ce contrôle structurel ne vaut pas certification linguistique.
5. **Qualité, droits, accessibilité :** examen documentaire de la présence des droits, de la provenance originale, de l'accessibilité et de la non-revendication de conformité institutionnelle. Ce sont des contrôles de présence et de cohérence, **pas** un audit juridique ni un essai utilisateur.
6. **Archive finale :** inspection de ses **14 entrées ZIP**, du premier chemin et de toutes les entrées; comparaison octet pour octet avec les fichiers préparés; aucune entrée hors du chemin de fusion.

## Limites non résolues et revue humaine obligatoire

- Les items ont des **corrigés fixes et explicités**, mais leur naturalité, leur validité didactique pour différents apprenants et leur fiabilité intercorrecteurs ne sont **pas encore qualifiées par un réviseur humain**. Aucun item n'est certifié.
- Le lien externe OQLF a été consulté et référencé; les permissions particulières de redistribution des pages externes **n'ont pas été auditées** : aucun extrait ou actif protégé n'est inclus. Le statut de droit des métadonnées sources relève du détenteur du workspace.
- Les adaptations d'accessibilité sont documentées mais **aucune épreuve d'interface, essai avec lecteurs d'écran, LMS, utilisateur, chronométrage ni validation de performance orale** n'a été réalisée.
- Les preuves E9 et E10 figurent aussi dans le document descriptif de transfert : l'intégrateur doit **cacher les corrigés et réserver les stimuli** lors de l'évaluation. Si ces chaînes ont été enseignées avec réponses visibles, elles ne peuvent pas servir à deux nouvelles preuves autonomes; une banque fixe équivalente devra être créée et contrôlée.
- Aucune compilation de framework, aucun `build-v9`, aucune publication, homologation PFEQ ou intégration dans un Moodle n'a été effectuée; ce delta se limite à `authoring/`, `contenu/`, `evaluation/`, `sources/` et `livraison/`.

## Suggestions de structure non appliquées

1. À proposer au registre central **sans le modifier ici** : métadonnée explicite « `preuve_reservee: true` » ou « `exposition_corrige` » pour distinguer un item servant d'exemple d'un item évaluatif réutilisable.
2. À proposer au moteur : champ de traçabilité des **deux manifestations autonomes** par contexte et par date, à stocker en LMS/runtime seulement, pas dans le canon.
3. À proposer à l'outillage : validateur formel de schéma des familles et items, bibliothèque de formes linguistiques contrôlées, vérification d'accessibilité par interface et analyse d'ambiguïté des corrections avant qualification.

**Décision de livraison :** techniquement prêt pour **fusion locale et revue**; **non qualifié comme cours publié**.
