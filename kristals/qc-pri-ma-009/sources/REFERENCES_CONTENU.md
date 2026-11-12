# Références et provenance — qc-pri-ma-009

## Fichiers réellement consultés dans l'archive source locale

1. `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` : frontières internes, traitement des préalables et deux preuves de maîtrise.
2. `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` : famille d'évaluation, modes fixes et paramétriques, nécessité d'un contrôle reproductible.
3. `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` : discipline « Mathématique » et absence de promesse d'alignement PFEQ.
4. `registry/GRAPHE_PEDAGOGIQUE_202.json` : arête `qc-pri-ma-009 requires qc-pri-ma-008`, aucune autre relation sortante attribuée au présent module.
5. `kristals/qc-pri-ma-009/authoring/PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md` : identité, objectif, preuve, notions et architecture source v1.2. Les chemins indiqués sont **dans le workspace maître**, pas des fichiers livrés ici.

## Raisonnements mathématiques dérivés et contrôlables

La division euclidienne entière est employée dans le cadre limité `N≥0, d≥1`. Le résultat satisfait `N=d×q+r` et `0≤r<d`. Le groupe contenant `q` ensembles de `d` objets utilise `d×q` objets. Il ne reste pas assez d'objets pour un nouveau groupe entier si `r<d`. La solution des items est recalculée par `divmod(N,d)` et les identités/bornes sont testées automatiquement. Cela ne remplace pas un jugement sur le niveau scolaire ou la clarté des problèmes.

## Productions originales et droits

Les scénarios, formulations, nombres, schémas textuels, démarches commentées, corrigés, rubriques et règles de variation ont été rédigés spécialement pour cette livraison; aucun extrait d'ouvrage, d'image ou d'archive extérieure n'est reproduit. Les exemples de bibliothèque, jetons, groupes, gourdes et autocollants sont fictifs; aucun droit de tierce partie n'est revendiqué. Le fait que les références internes mentionnent EEF, IES/WWC ou CAST ne signifie pas qu'une recherche indépendante ni un audit de leurs publications aient été réalisés dans ce mandat.

## Limites et vérifications restantes

Seules les sources internes listées ont été inspectées pour ce projet. Aucune homologation PFEQ, validation curriculaire, licence d'images, revue de droits de matériel externe, revue humaine de la pertinence et de l'accessibilité, ni qualification technique de publication n'a été réalisée. Les tests numériques et de structure figurent dans `livraison/VALIDATION.md`.
