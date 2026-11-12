# Références et provenance — qc-pri-fr-021

## 1. Sources vérifiées pour ce lot

**Sources internes de l'archive maître v1.2**, effectivement lues avant toute modification :

1. `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` — objet autonome, diagnostic de préalables équivalents, au moins deux preuves dans deux contextes, frontière « non homologation PFEQ ».
2. `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` — champs des familles, mode fixe/contrôlé, revue humaine obligatoire des textes et des rubriques.
3. `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` — appellation « Français, langue d’enseignement » et rôle limité de la conversion des noms de disciplines.
4. `registry/GRAPHE_PEDAGOGIQUE_202.json` — lien strict `requires(qc-pri-fr-021,qc-pri-fr-015)` et lien non bloquant `recommends_before(qc-pri-fr-021,qc-pri-fr-019)`. Liens entrants d'autres Kristals non modifiés.
5. `kristals/qc-pri-fr-021/authoring/PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md` — objectif, preuve, famille, structure YAML et contrat JSON d'origine.

**Sources externes consultées via pages officielles :**

6. Institute of Education Sciences, What Works Clearinghouse, *Teaching Elementary School Students to Be Effective Writers* (publication 2012, révision octobre 2018) : https://ies.ed.gov/ncee/wwc/PracticeGuide/17 (consulté le 8 octobre 2026). Le guide énonce des recommandations d'enseignement du processus d'écriture et de construction des phrases à l'école primaire. Il ne fournit pas les plans ni les corrigés du présent lot et ne certifie pas sa grille.
7. CAST, *Universal Design for Learning Guidelines*, version 3.0 (2024), https://udlguidelines.cast.org/more/about-guidelines-3-0/ (consulté le 8 octobre 2026). Précise des options pour la présentation des informations, les outils de composition et le développement des stratégies. Cette référence soutient une réflexion sur l'accessibilité, sans établir une équivalence officielle ni valider les niveaux 0–2 de notre grille.

## 2. Raisonnements dérivés et décisions de conception

- Relier une case de plan à un paragraphe distinct est une opération pédagogique locale découlant de la preuve « deux paragraphes complets à partir d'un plan », non une exigence quantitative du PFEQ.
- Le minimum de trois phrases fonctionnelles par paragraphe (une d'ouverture + deux de développement), les deux rubriques, les quatre dimensions 0–2 et l'exigence de deux contextes distincts sont des **critères de construction internes**, à tester humainement.
- On considère qu'un connecteur a une valeur seulement si son lien temporel, causal ou additionnel correspond aux informations effectivement rédigées; cela résulte d'une analyse linguistique des textes originaux, pas d'une base empirique de réponses scolaires.
- L'aide à la lecture du plan et les modes de saisie accessibles peuvent faciliter l'expression tout en maintenant le but de production écrite; l'équivalence des aménagements individuels demande une décision pédagogique.

## 3. Contenus originaux, droits et limites

- Tous les plans fictifs (jardin, bibliothèque, exposition, kiosque, journal de bibliothèque, dispositif d'ombres, etc.), phrases modèles, intruses, rubriques et feedback ont été composés spécifiquement pour `qc-pri-fr-021`.
- Aucune image, chanson, vidéo, extrait de livre ou page externe protégée n'a été copiée dans les contenus. Les liens bibliographiques ne redistribuent aucun document tiers. Les métadonnées YAML v1.2 et les objectifs ont été préservés à partir de l'archive du propriétaire selon le mandat de fusion.
- Les autorisations de redistribution de l'archive source restent celles de son titulaire; **aucune vérification juridique exhaustive** n'a été réalisée.
- Ni validation empirique des items, ni accord intercorrecteurs, ni homogénéité culturelle des exemples ni compatibilité LMS/Framework v9 n'ont été testés en situation réelle. Une revue humaine et des essais encadrés restent nécessaires.
