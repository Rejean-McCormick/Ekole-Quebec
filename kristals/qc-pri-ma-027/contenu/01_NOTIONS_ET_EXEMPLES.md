# 01 — Notions et exemples résolus | `qc-pri-ma-027`

## Objectif et règle sûre
**`obj-1` :** Calculer et interpréter le périmètre d’une figure comme longueur du contour. **`crit-1` :** Trouver le périmètre de deux figures et expliquer l’effet d’une modification. Les figures sont des polygones aux segments droits; aucune figure ne dépend d'un dessin à l'échelle.

**Contour :** ligne extérieure fermée séparant la figure de ce qui l'entoure. On part d'un sommet, longe chaque côté extérieur une fois et revient au départ. **Longueur :** mesure d'un segment. **Addition :** réunir les longueurs des côtés du contour, après les avoir mises dans la même unité. **Unité :** `cm`, `m` ou autre unité *de longueur*; `cm²` représente une surface et ne convient pas.

**Représentations** : (1) ficelle le long du contour extérieur d'un support sans le couper; (2) côtés explicitement étiquetés; (3) somme et résultat avec unité. Une diagonale ou un segment de partage *intérieur* n'est jamais ajouté.

## Exemple résolu 1 — Cadre rectangulaire et changement de largeur
Une affiche mesure **7 cm** de largeur et **4 cm** de hauteur. Les côtés extérieurs dans l'ordre sont `7, 4, 7, 4 cm` : `P₁ = 7 + 4 + 7 + 4 = 22 cm`. Après élargissement **de 2 cm** (largeur 9, hauteur 4), les côtés deviennent `9, 4, 9, 4 cm` : `P₂ = 9 + 4 + 9 + 4 = 26 cm`. Effet `26 − 22 = +4 cm`, parce que **deux** bords horizontaux gagnent chacun 2 cm. Une seule augmentation de 2 cm serait une erreur.

## Exemple résolu 2 — Figure en L, encoche rectangulaire
La figure est un grand rectangle de largeur totale `W=10 cm`, hauteur totale `H=6 cm`, dont on a ôté au **coin supérieur droit** un petit rectangle de largeur `w=3 cm` et hauteur `h=2 cm`. En parcourant les six côtés extérieurs à partir du coin inférieur gauche, dans le sens antihoraire (bas, droite inférieure, bord d'encoche horizontal, vertical de l'encoche, haut restant, gauche), on obtient exactement `W, H−h, w, h, W−w, H` soit `10, 4, 3, 2, 7, 6`. Donc `P = 10+4+3+2+7+6 = 32 cm = 2(10+6)`.

**Modification distincte :** élargir le coin ôté de `w=3` à `w=4` sans changer `W,H,h`. La liste devient `10, 4, 4, 2, 6, 6`, donc **32 cm**. L'effet est **0 cm** : l'augmentation du bord intérieur horizontal est compensée par le raccourcissement du bord extérieur supérieur. Ce résultat est propre à cette encoche rectangulaire dans un coin, pas à tous les découpages.

## Contre-exemple 1 — Mesurer l'intérieur
« Un rectangle de 6 cm sur 4 cm donne `6 × 4 = 24 cm²` de périmètre. » **Faux :** ce produit mesure l'aire. Pour le **périmètre**, `6+4+6+4 = 20 cm`. Diagnostiquer en faisant suivre le contour au doigt.

## Contre-exemple 2 — Mauvaise interprétation de modification
« Si on augmente la largeur de 8 à 10 cm et qu'on garde la hauteur de 3 cm, le périmètre augmente de 2 cm. » **Faux :** les deux côtés parallèles à la largeur augmentent chacun de 2; avant `P=22 cm`, après `P=26 cm`, effet `+4 cm`. L'élève doit nommer les **deux** côtés concernés.

## Repères d'autovérification
1. J'ai fermé le tour extérieur et n'ai pas ajouté de segment intérieur. 2. Toutes les mesures sont exprimées dans une même unité. 3. Ma somme contient chaque côté une fois. 4. J'ai écrit une unité linéaire. 5. J'ai relié le changement de périmètre aux *longueurs effectivement modifiées*.
