# Références et provenance — qc-pri-ma-030

## A. Sources effectivement consultées et vérifiées dans le ZIP maître

1. `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` — gouvernance active; méthode diagnostic → enseignement → pratique → maîtrise dans deux contextes; aucune homologation PFEQ à déduire.
2. `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` — champs minimaux des familles, modes fixes/paramétriques/scénarios, reproductibilité et nécessité d'une revue humaine.
3. `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` — préservation de l'appellation « Mathématique », pas de code officiel inventé.
4. `registry/GRAPHE_PEDAGOGIQUE_202.json` — aucun lien **sortant** de `qc-pri-ma-030` en `requires`, `recommends_before` ou `reinforces`. Des liens **entrants** existent (notamment `qc-pri-ma-031 requires qc-pri-ma-030`, `qc-pri-st-003 reinforces qc-pri-ma-030`) et ne sont pas modifiés.
5. `kristals/qc-pri-ma-030/authoring/PARCOURS.md` — en-tête YAML, 12 sections, `obj-1`, `crit-1`, identité et familles d'origine.
6. `kristals/qc-pri-ma-030/authoring/CONTRAT_PEDAGOGIQUE.json` — structure et métadonnées de base de la famille `qc-pri-ma-030-ev-01`.
7. `kristals/qc-pri-ma-030/authoring/ALIGNEMENT.md` et `BRIEF_REDACTION.md` — limites de la conversion Québec et objectifs de rédaction locaux.

Ces références désignent des **fichiers internes réellement lus** ; aucune source externe ni citation de page externe n'est alléguée. Aucune traduction ou reproduction substantielle d'un manuel tiers n'est intégrée.

## B. Raisonnements mathématiques dérivés (à revérifier pédagogiquement)

- Pour une liste finie de `n` observations dont chacune appartient à exactement une catégorie exclusive et dont les catégories couvrent les observations admissibles, la somme des effectifs est égale à `n`. Justification : chaque observation contribue exactement `1` à une unique case, donc la somme additionne `n` unités. **La somme seule ne prouve pas une bonne affectation**, car des erreurs de cases peuvent se compenser.
- Un effectif est un nombre entier naturel, zéro compris. Une catégorie prévue mais non observée a effectif zéro.
- Un tableau peut être relu indépendamment par les indices des observations, indépendamment de l'ordre de présentation; permuter les occurrences ne change pas les effectifs.
- La recette P-030/1 transforme une graine entière et des catégories fixes en observations brutes finies. Le corrigé peut être recompté sur cette liste sans réutiliser les formules qui ont calculé ses effectifs.

## C. Productions originales de ce delta

Tous les exemples de crayons, symboles, trajets, boutons, coquillages, jetons, étiquettes, codes, sports et véhicules, les consignes, les listes d'observations, les corrections de position, le générateur P-030/1, les feedbacks, la grille et les plans ont été rédigés pour ce Kristal. Les situations sont **fictives**, les couleurs toujours nommées, les noms d'animaux ou de véhicules fournis dans les stimuli; aucune donnée d'élève n'est collectée.

## D. Statut des droits, vérifications et limites

- Textes créés dans cette livraison, sans incorporation d'images ou de citations tierces; aucune licence de publication particulière n'est déduite des documents source.
- Les documents internes du workspace sont utilisés comme instructions et métadonnées; leurs droits et une éventuelle autorisation de diffusion restent gouvernés par le projet, non par cette liste de références.
- Corrigés calculés localement et comparés à un comptage indépendant des occurrences; aucun générateur IA libre n'est utilisé comme correcteur final.
- Revue humaine toujours requise sur clarté, ergonomie, accessibilité pratique et conditions locales de diffusion. Aucune revendication de reconnaissance PFEQ ou d'homologation.
