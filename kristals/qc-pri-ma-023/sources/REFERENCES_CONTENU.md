# 09 — Références, statut des preuves et droits

## 1. Sources réellement consultées dans l’archive maître v1.2

Source de travail : archive `/mnt/data/initbundle(1).zip`, contenant le dossier **`Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`**. Les fichiers ci-dessous ont été lus tels que fournis localement, et non vérifiés comme éditions officielles sur un site tiers :

- `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` : frontières, absence de verrou strict, deux preuves, maîtrise et règles de production.
- `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` : champ de famille, génération déterministe, revues.
- `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` : nomenclature « Mathématique », absence d'affirmation PFEQ.
- `governance/Norme_Pedagogique_Autonome_v1.2/REFERENCES_EVIDENCE.md` : liste interne des pistes EEF, IES/WWC et CAST. **La présence des liens a été constatée dans l'archive, pas leur contenu externe**.
- `registry/GRAPHE_PEDAGOGIQUE_202.json` : depuis `qc-pri-ma-023`, uniquement `recommends_before` vers `qc-pri-ma-021`, aucun `requires` sortant; autres relations entrantes non modifiées.
- `kristals/qc-pri-ma-023/authoring/PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md` : métadonnées, intentions et familles v1.2 préservées; `AGENTS.md` : politique de proposition et non-canonicité.

**Statut :** documents sources de conception vérifiés *en lecture locale*, sans audit scientifique indépendant de leur contenu. On n'affirme aucune approbation externe.

## 2. Raisonnement géométrique dérivé, vérifiable sans source secondaire

- Définition opératoire : un polygone simple du corpus a un contour fermé composé de segments droits, un sommet par jonction. Le cercle est une figure plane non polygonale, donc sans côté *polygonal*.
- La condition de parallélisme entre deux directions non nulles `u=(ux,uy)` et `v=(vx,vy)` est `ux*vy - uy*vx = 0`, sous réserve de distinguer les droites supports distinctes; dans le corpus convexe deux côtés opposés non colinéaires au même support ne surviennent pas. Cette égalité est une déduction algébrique, pas une citation littérale.
- La translation, la rotation de 90° × t et la dilatation de facteur positif 1 ou 2 préservent la non-colinéarité des côtés, le nombre de sommets et les paires parallèles. Les exemples restent des polygones convexes simples à coordonnées entières.
- Un vérificateur indépendant normalisant les vecteurs entiers par PGCD doit retrouver le nombre de paires pour les modèles et les graines admissibles. Les limites exactes et les tests exécutés figurent dans `livraison/VALIDATION.md`.

## 3. Matériel et œuvres originales de cette livraison

Sont conçus pour ce Kristal : définitions d'enseignement et reformulations, gabarits de coordonnées T/R/L/TR/TR2/I/P/K, exemples et contre-exemples, 2 diagnostics, 3 guidages, 4 pratiques autonomes, remédiations, mosaïque/jardin fictifs, algorithme de génération et d'évaluation, 12 items et leurs corrigés, grilles et plans. Aucun dessin tiers, photo, icône récupérée, extrait protégé ou donnée personnelle n'a été incorporé.

**Droits :** rédaction originale réalisée pour cette livraison; aucune licence formelle du corpus source ou de l'œuvre résultante n'est inventée. La réutilisation du workspace maître reste régie par les droits de son détenteur. Les liens mentionnés vers EEF/IES/CAST sont bibliographiques internes, **pas des licences d'utilisation d'images**.

## 4. Limites et vérifications humaines à effectuer

**Revue humaine requise :** les tests techniques ci-dessous ne remplacent aucune qualification pédagogique.

- Le raisonnement/mathématique et les variations entières peuvent être testés automatiquement; l'adéquation pédagogique d'âge, la charge de lecture, l'accessibilité tactile effective et la clarté des exercices exigent une revue/essai humains.
- Le format texte de coordonnées offre une alternative au visuel, mais une représentation quadrillée/tactile reste à préparer par l'enseignant·e ou le système; ces fichiers ne contiennent pas des images finalisées.
- Les références internationales mentionnées dans la norme locale ne sont pas présentées comme contrôlées sur leurs sites au moment de la livraison; aucune conformité PFEQ n'est revendiquée.
