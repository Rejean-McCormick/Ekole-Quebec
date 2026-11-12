# Traçabilité et droits des contenus — `qc-pri-ma-012`

## 1. Sources vérifiées et portée exacte

**Sources internes lues dans l'archive de base v1.2** (chemins du workspace maître, **non recopiés dans le ZIP de delta**):

1. `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` — frontière de l'autorité pédagogique, diagnostic → pratique → maîtrise à deux manifestations, contrôle des nombres en mathématique.
2. `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` — contrat des familles, mode paramétrique déterministe, seed, critères et statut non certifié.
3. `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` — « Mathématique » comme appellation conservée seulement, pas d'alignement officiel imposé.
4. `registry/GRAPHE_PEDAGOGIQUE_202.json` — aucune relation *entrante* `requires/recommends_before` pour `qc-pri-ma-012`; relations *sortantes d'autres nœuds* `qc-pri-ma-013/requires/qc-pri-ma-012` et `qc-pri-ma-015/requires/qc-pri-ma-012` (non modifiées).
5. `kristals/qc-pri-ma-012/authoring/PARCOURS.md`, `authoring/CONTRAT_PEDAGOGIQUE.json`, `authoring/BRIEF_REDACTION.md`, `authoring/ALIGNEMENT.md` — source des métadonnées, de `obj-1`, de `crit-1` et de la famille `qc-pri-ma-012-ev-01`.

**Sources pédagogiques externes consultées le 8 octobre 2026** (liens vérifiés en ligne; ne signifient pas certification du présent matériel) :

- Australian Association of Mathematics Teachers (AAMT), *Part-whole fractions*, https://resources.aamt.edu.au/Topdrawer/Fractions/Big-ideas/Part-whole-fractions — explique que le dénominateur compte les parts égales du tout, et le numérateur les parts prises; présente les modèles de surface.
- Institute of Education Sciences (IES), *Five recommendations for teaching fractions at the start of middle school*, https://nces.ed.gov/learn/blog/five-recommendations-teaching-fractions-start-middle-school — appui conceptuel à la référence au tout, aux partages équitables et à la diversité des représentations; cité comme ressource pédagogique et **non** comme curriculum québécois.

**Portée limitée des sources** : ni les ressources externes ni l'archive ne valident automatiquement l'efficacité expérimentale de chaque exercice, la maîtrise des apprenants ou la certification des items.

## 2. Raisonnements mathématiques dérivés (contrôlables)

- Pour `0 < a < b`, choisir `a` parmi `b` parts égales produit `a/b` du tout par définition de la fraction dans le modèle partie-tout.
- Dans un ensemble de `N=b×m` objets de même statut et partageables en `b` groupes de `m`, sélectionner `a` groupes revient à sélectionner `K=a×m` objets; `K/N = (a×m)/(b×m) = a/b` pour `m>0`. Exemples de catalogue contrôlés exactement par `fractions.Fraction` lors de la validation.
- Une partition en régions **de surfaces inégales** invalide une interprétation `a/b` fondée uniquement sur le comptage des régions; idem pour une bande de longueurs inégales.
- Deux collections de tailles différentes peuvent partager la même fraction sélectionnée sans contenir le même nombre d'objets choisis.

## 3. Productions originales incluses dans cette livraison

Tous les énoncés, schémas ASCII, situations d'affiche/jardin/jetons/ludothèque, contre-exemples, explications, tâches, catalogues numériques, corrigés et rubriques ont été rédigés pour `qc-pri-ma-012`. Aucun texte pédagogique externe ni image tierce n'est reproduit; la mention d'une source n'en transfère pas les droits. Les métadonnées du workspace sont reprises selon la tâche de préservation demandée, non revendiquées comme création originale.

## 4. Droits, limites et revue requise

- Les droits de redistribution du **workspace source** ne sont pas établis par la présente livraison; fusion et diffusion relèvent du propriétaire du workspace.
- Les exemples utilisent des objets génériques et des schémas textuels originaux, sans emprunt d'illustration, nom d'élève, donnée personnelle ni photographie.
- Les vérifications techniques de JSON/arithmétique ne constituent pas une revue humaine des biais, un essai de classe, une validation institutionnelle ou une autorisation de publication.
- Aucune conformité au PFEQ, approbation ministérielle, homologation ni « certification » n'est affirmée.
