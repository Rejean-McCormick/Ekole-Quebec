# Validation de livraison — `qc-pri-ma-019` v1.2

**Statut final :** `controles_techniques_effectues_revue_humaine_requise`. Le Kristal n'est ni « certifié », ni « publié », ni « homologué ». La frame n'est pas convertie en canon. Le mandat se limite à ce seul dossier.

## Sources réellement consultées et identité protégée

- Source lue dans l'archive transmise `Spec_Kristals_Parcours_Primaire_Qc_v1.1(1).zip`, chemin interne **v1.2** `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` : gouvernance (`CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md`, recueil de références), registre `GRAPHE_PEDAGOGIQUE_202.json`, frame `PARCOURS.md`, contrat original, `ALIGNEMENT.md`, `BRIEF_REDACTION.md`.
- Objectif original inchangé : « Modéliser et résoudre une situation additive en distinguant les données utiles. » Preuve originale inchangée : « Résoudre deux problèmes verbaux nouveaux et expliquer les opérations. » Famille `qc-pri-ma-019-ev-01`; préalables stricts **uniquement** `qc-pri-ma-006` et `qc-pri-ma-007`; aucun ordre conseillé ajouté.
- Bloc YAML de `authoring/PARCOURS.md` conservé **à l'identique**, 12 sections numérotées rédigées. Tous les champs du contrat JSON de base, y compris les valeurs d'architecture historique, conservés; les champs de génération sont ajoutés à la famille native et l'annexe `livraison_contenu` explique le statut présent.

## Contenu livré

- **Six leçons** : quatre définitions, exemples et contre-exemples avec unités, diagnostic en deux tâches, modelage, 3 pratiques guidées avec indices décroissants, 4 exercices autonomes, remédiations et **deux transferts d'entraînement distincts**.
- **12 items** : 7 ancrages fixes (q-001 à q-005, q-009, q-012), 3 items paramétriques (q-006 à q-008, **4 cas autorisés chacun = 12 cas numériques**) et 2 scénarios contrôlés sans indice (q-010 et q-011). Les preuves sont en contextes distincts du matériel d'entraînement : centre de prêt de livres / jardin communautaire.
- Plan d'évaluation lié à `obj-1`, `crit-1` et la famille; grille descriptive de cinq dimensions et exigences de deux manifestations; références/provenance explicites. Tous les items sont `a_revoir`.

## Tests effectivement exécutés pour ce delta

La suite locale `ma019_build/test_build.py` (hors ZIP) a vérifié, avant emballage, **595 assertions réussies** : sources et deux liens de graphe; intégrité exacte du YAML; 12 sections; conservation de tous les champs préexistants; valeurs de famille et 13 champs contractuels; parsage des JSON; banque de 12 IDs uniques numérotés; 12 cas paramétriques bornés, sélection par `seed mod 4`, reconstitution littérale des énoncés/corrigés, résultat et opération inverse pour chaque cas; calculs indépendants de neuf items fixes et expressions de cours contrôlées; présence des deux contextes de maîtrise, différence avec les transferts d'entraînement, grille et renvois internes; fileset préparatoire et chemins du manifeste.

**Contrôles ZIP à réaliser après écriture de cette validation :** vérifier `ZipFile.testzip()`, ordre et présence des **14** entrées avec préfixe `kristals/qc-pri-ma-019/`, absence de chemin absolu/`../`, absence de fichier supplémentaire, concordance exacte manifeste ↔ membres, extraction en répertoire temporaire et comparaison de chaque fichier au contenu source. Ces contrôles sont réalisés séparément par le même script au stade d'assemblage final; ne pas interpréter la phrase présente comme preuve d'exécution sans sa sortie de test.

## Limites et revue humaine nécessaire

- **Revue humaine pédagogique** avant publication : progressivité et niveaux de lecture, pertinence des distracteurs, neutralité culturelle, adaptation réelle pour des élèves utilisant lecture orale ou support tactile, faisabilité de la grille, stabilité de deux preuves autonomes.
- Les énoncés et solutions de q-010/q-011 figurent dans des fichiers de **correction/authoring**; l'adaptateur LMS doit réserver la banque et la grille aux évaluateurs. S'ils ont été vus par l'élève, une variante de preuve inédite doit être conçue **et vérifiée** avant nouvelle décision de maîtrise. Les 12 cas paramétriques ne prétendent pas fournir des preuves de remplacement certifiées.
- Les références EEF, IES/WWC et CAST sont recensées dans la gouvernance existante; leurs ressources externes n'ont pas fait l'objet d'une nouvelle recherche, d'une consultation en ligne ni d'une validation empirique du présent Kristal. Textes et contextes rédigés de manière originale, sans média tiers importé; une revue des droits reste recommandée dans le contexte de déploiement.
- Le test technique n'est pas une étude de compréhension avec des enfants, un essai LMS, ni un audit de conformité PFEQ.

## Fusion et propositions hors périmètre (aucune base centrale modifiée)

- Décompresser l'archive maîtresse; **se placer dans** `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`; extraire ce delta. Les seules substitutions sont `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`, avec 12 nouveaux fichiers.
- Ne pas recopier ici `ALIGNEMENT.md`, `AGENTS.md`, `kristal.workspace.json`, `registry/`, `governance/`, `canon/`, `state/`, `runtime/` ni le contenu d'autres Kristals.
- **Proposition non appliquée :** uniformiser ultérieurement les libellés `statut` d'architecture et `livraison_contenu.statut` au niveau du schéma commun; prévoir un espace LMS distinct pour épreuves/corrigés et une banque sécurisée de versions de reprise. Ces changements demanderaient une décision centrale versionnée, hors de ce delta.
