# Sources, dérivations et créations originales — `qc-pri-ma-027`

## Sources internes de l'archive maîtresse v1.2 effectivement lues

1. `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` — objectif par feuille, préalables avec diagnostic équivalent, pratiques dégressives, double preuve, correction mathématique contrôlée, pas d'homologation PFEQ.
2. `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` — douze champs obligatoires de famille, modes contrôlés, seeds, vérification des solutions, nécessité de revue.
3. `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` — discipline affichée « Mathématique », sans assignation officielle année/cycle ni conformité au PFEQ.
4. `registry/GRAPHE_PEDAGOGIQUE_202.json` — **deux arêtes `requires`** de `qc-pri-ma-027` vers `qc-pri-ma-023` et `qc-pri-ma-025`, aucune autre arête sortante pour cet ID. Les autres Kristals ne sont pas copiés ou modifiés.
5. `kristals/qc-pri-ma-027/authoring/PARCOURS.md` et `CONTRAT_PEDAGOGIQUE.json` — titre, YAML et structure native, objectif « Calculer et interpréter… », preuve « Trouver le périmètre… », notions et famille, valeurs préservées.
6. `kristals/qc-pri-ma-027/authoring/ALIGNEMENT.md` et `BRIEF_REDACTION.md` — limites de conversion, rédaction de notions et évaluations mathématiques; lus **sans les livrer ni les modifier**.

## Sources externes vérifiées lors de cette livraison

- **Alloprof**, « Le périmètre et l'aire des figures planes », https://www.alloprof.qc.ca/bv/mathematiques/le-perimetre-et-l-aire-des-figures-planes-m1478 (consulté le 8 octobre 2026). Le document définit le périmètre comme la longueur du contour et distingue les unités linéaires de celles d'aire. **Note :** la page consultée est catégorisée « Secondaire »; elle sert ici uniquement de référence pour une définition générale, pas de prescription de niveau scolaire ni de PFEQ.
- **CAST**, *Universal Design for Learning Guidelines*, version 3.0 (2024), « Expression & Communication », https://udlguidelines.cast.org/action-expression/expression-communication/ (consulté le 8 octobre 2026). Appui général à plusieurs moyens d'action et d'expression, pas validation scientifique des seuils locaux de maîtrise.

Aucun passage important, illustration, tableau, code ou énoncé d'une ressource externe n'est reproduit. Les références ne sont ni des attestations de droits d'exploitation du contenu source ni des preuves d'alignement ministériel.

## Dérivations mathématiques exactes, vérifiables indépendamment

- **Rectangle :** longueur du bord `W+H+W+H=2(W+H)`. Augmenter W de d change **deux côtés** : `P₂−P₁=2d`.
- **Rectangle avec les deux dimensions doublées :** `2(2W+2H)=2×2(W+H)` : le périmètre double, alors que l'aire quadruple. Les deux quantités sont distinctes.
- **Figure en L construite uniquement par retrait au coin supérieur droit :** pour `0<w<W` et `0<h<H`, six bords `W, H−h, w, h, W−w, H`; leur somme vaut `2(W+H)`. L'encoche modifie la forme mais pas la longueur totale du contour. **Ne pas généraliser ce résultat à une encoche latérale ou à un trou intérieur.**
- **Élargissement d'un L à encoche fixe :** remplacer W par W+d prolonge les côtés W et W−w, donc effet `2d`.
- Les **21 variantes paramétriques** utilisent ces seules constructions, des entiers strictement positifs, des unités indiquées et des opérations entières. Chaque jeu de données, énoncé et solution figure dans la banque; le contrôle numérique indépendant est documenté dans `livraison/VALIDATION.md`.

## Productions originales / droits

Sont originaux dans cette livraison : exemples de cartes, encadrements, jardins, tapis et L géométriques; consignes D1/D2, G1/G2/G3, A1–A4, T1/T2, tous les énoncés des dix items et leurs trois variantes quand applicables; schémas décrits par les côtés, grilles, feedbacks et règles de sélection. Les calculs arithmétiques et formules élémentaires ne sont pas revendiqués comme propriété exclusive.

Aucune image externe, police, œuvre littéraire, photographie d'enfant ni musique n'est intégrée. Si une illustration ou une ressource tierce est ajoutée ultérieurement, ses droits devront être établis séparément. Les conditions juridiques applicables à la redistribution du dossier source ne sont pas déterminées dans ce rapport; une revue de droits demeure possible.

**Statut des sources :** internes vérifiées directement, externes consultées, dérivations explicitées et compositions originales. Aucune homologation PFEQ, aucune preuve d'efficacité individuelle ni contrôle clinique ou matériel effectués.
