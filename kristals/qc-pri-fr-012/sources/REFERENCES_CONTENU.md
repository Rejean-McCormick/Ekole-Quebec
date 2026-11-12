# Références et provenance — qc-pri-fr-012

## 1. Sources effectivement consultées dans l'archive fournie

- `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` : gouvernance active, diagnostic, deux contextes et autonomie, rôle non normatif de la présentation Québec.
- `.../GENERATEUR_ET_EXAMENS.md` : schéma de famille, modes fixe/paramétrique/scénario, limites des items générés, statut non certifié.
- `.../CHARTE_CONVERSION_QC.md` : conservation de l'appellation « Français, langue d’enseignement »; absence d'homologation PFEQ par simple conversion.
- `.../REFERENCES_EVIDENCE.md` : index de références pédagogiques EEF, IES/WWC et CAST figurant dans la norme; liens **répertoriés**, textes externes **non vérifiés indépendamment lors de cette production**.
- `.../registry/GRAPHE_PEDAGOGIQUE_202.json` : `qc-pri-fr-012` → `qc-pri-fr-002` en `recommends_before`; aucune arête `requires` partant de ce Kristal.
- `.../kristals/qc-pri-fr-012/authoring/PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md` : objectif unique, preuve, notions, famille, identité et frontières pédagogiques à conserver.

**Portée de vérification :** présence et lecture directe de ces documents **dans l'archive fournie**. Cela atteste les métadonnées internes, pas l'évaluation indépendante de leurs fondements scientifiques ou une homologation ministérielle.

## 2. Raisonnements linguistiques et vérification éditoriale

- L'orthographe des mots du **corpus ciblé** est explicitée dans cette livraison; les couples `grand/grande`, `petit/petite`, `chant/chanter` servent d'exemples de constance écrite et de justification morphologique. Les exemples ne formulent pas de « règle » prédictive universelle.
- Les graphies `maison, saison, raison, liaison` ont été comparées par suite finale écrite `-aison`; les contre-exemples *maizon*, *sèzon*, *grant*, *beaucou* sont des **erreurs construites artificiellement** pour la remédiation.
- L'assimilation entre sons et lettres varie dans le français oral; l’orthographe lexicale écrite, pas l'accent québécois, est mesurée. Les seuils (5/6, 4/5, deux justifications) sont **des choix de design éditorial**, pas des valeurs étalonnées scientifiquement.
- La vérification mécanique du ZIP, des clés de JSON, des mots cibles présents dans les dictées et des mappings de corrections ne remplace **pas** une relecture humaine experte de chaque graphie et de chaque justification. Aucune consultation indépendante d'un dictionnaire de référence n'est attestée ici.

## 3. Productions originales / droits

- Le cours, les exemples, les scènes fictives (visite, bibliothèque, fête), les textes dictés, les textes erronés, les justifications, les consignes et la grille ont été **rédigés pour cette livraison** à partir des spécifications du workspace.
- Aucune citation littérale longue, extrait d'œuvre tiers, illustration, typographie propriétaire ou photographie n’a été intégré. Les graphies lexicales et les courts titres sont des données linguistiques ordinaires.
- Les documents de gouvernance sont **référencés, pas redistribués** dans ce delta. Le fichier `authoring/PARCOURS.md` reprend obligatoirement sa trame et ses métadonnées du workspace d'origine (remplacement contrôlé d’un fichier existant).
- Révision des droits et de l'adaptation aux usages de diffusion à réaliser avant publication. Ne revendiquer ni licence externe spécifique non examinée ni autorisation ministérielle.

## 4. Points de revue humaine

1. Contrôler les 15 graphies, exemples régionaux et risques de confusion entre orthographe d’usage et accords.
2. Tester avec des élèves la clarté des indices sémantiques et la disponibilité d'un lecteur ou de stimuli auditifs accessibles.
3. Vérifier si les seuils choisis conviennent empiriquement, les ajuster via proposition versionnée plutôt que par changement silencieux.
4. Vérifier les alternatives d'accessibilité, les droits de toute ressource ajoutée plus tard et la gestion des données d'évaluation.
5. Contrôler le caractère réellement indépendant des deux preuves en contexte d'enseignement (pas de révélation préalable de leur corrigé).
