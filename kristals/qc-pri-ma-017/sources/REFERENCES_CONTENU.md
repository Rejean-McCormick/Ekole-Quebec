# Provenance des contenus — qc-pri-ma-017

## A. Sources effectivement consultées (fichiers présents dans l'archive source)

1. `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` : autorité pédagogique interne, besoin de deux preuves autonomes, mathématique exacte, séparation des étiquettes québécoises et de l'enseignement.
2. `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` : schéma de familles, modes fixe/paramétrique, seed reproductible, contrôles indépendants et limites de certification.
3. `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` : appellation « Mathématique » et séparation de l'identité du Kristal et des codes scolaires.
4. `registry/GRAPHE_PEDAGOGIQUE_202.json` : seules arêtes sortantes de `qc-pri-ma-017` : `requires` vers `qc-pri-ma-013` et `qc-pri-ma-015`. Aucune modification au graphe.
5. `kristals/qc-pri-ma-017/authoring/PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md` : données canoniques du frame, objectif, preuve, notions, ordre et famille conservés.

**Portée de la vérification** : j'ai lu ces documents **dans l'archive fournie**, pas vérifié une publication externe ni audité la totalité des ouvrages mentionnés dans la gouvernance. Les références internes ci-dessus restent dans le workspace maître et ne sont pas empaquetées dans ce delta.

## B. Raisonnements mathématiques dérivés et contrôlés

- Définition : `p %=p/100` (pourcent signifiant pour cent unités de référence); `q = (p/100)×N` est la conséquence de conserver une même proportion pour un tout N.
- Lorsque N>0, égalité de taux `q/N = p/100` équivalente à `100q=pN` (produits croisés). Les corrections de la banque utilisent des fractions rationnelles exactes; l'énumération des corpus finis et l'égalité entière sont consignées comme contrôles dans `livraison/VALIDATION.md`.
- Les fractions `1/10, 1/5, 1/4, 1/2, 3/4` sont exactement égales à `10/100, 20/100, 25/100, 50/100, 75/100`. Les schémas sont des représentations pédagogiques dérivées de ces égalités, pas de statistiques réelles.
- Si N=0 : `q=0` mais `q/N` est indéfini; les items d'évaluation exigent N>0 et des réponses entières.

## C. Produits originaux et droits

Les situations des maquettes, cartons, crayons, pots, feuilles, billets, minutes et classes imaginaires, leurs consignes, commentaires, contre-exemples, tableaux et grilles ont été rédigés spécialement pour ce Kristal. **Aucune image, aucun graphique tiers, aucun texte protégé externe, aucune photographie ou donnée d'élève** n'est reproduit. La licence générale du workspace n'est ni déduite ni modifiée; une revue juridique reste à faire pour la diffusion si elle est exigée par l'organisation.

## D. Limites déclarées

Aucune consultation de sources web n'est revendiquée. Ce cours repose sur des identités arithmétiques élémentaires et des documents de gouvernance internes; aucun alignement détaillé au PFEQ, validation de terrain, évaluation psychométrique ni certification d'items n'est revendiqué. Le statut demeure `a_revoir` jusqu'aux revues humaine et d'usage.
