# 01 — Notions et exemples résolus

**Kristal :** `qc-pri-ma-003` | **Mathématique** | **Objectif `obj-1` :** Décomposer et recomposer des nombres grâce aux valeurs de position.

## Les quatre notions exactes

**Unité (U).** Un objet vaut 1 unité. Le chiffre des unités indique combien d'unités isolées figurent dans l'écriture usuelle. Ex. : dans **243**, le **3** vaut trois unités, et non trois dizaines.

**Dizaine (D).** Une dizaine est un groupement de **10 unités**. `1 D = 10 U`; `4 D = 40 U`. Ce « 4 » est un nombre de groupes de 10. Dans 243, le 4 des dizaines vaut **40**.

**Centaine (C).** Une centaine vaut **10 dizaines = 100 unités**. `1 C = 10 D = 100 U`. Dans 243, le 2 représente **200 unités**, pas deux unités.

**Base dix.** Chaque déplacement d'un rang vers la gauche multiplie la valeur du rang par 10 : unités (1), dizaines (10), centaines (100). Une écriture canonique a de 0 à 9 groupes à chaque rang. Une *décomposition* n'est pas nécessairement canonique : on peut compter 13 unités si on défait une dizaine. Pour tout H, T, U entiers non négatifs, `H C + T D + U U = 100H + 10T + U`.

**Règle d'échange réversible :** remplacer `1 D` par `10 U` conserve la valeur; réciproquement `10 U` redonnent `1 D`. De même, `1 C` ↔ `10 D`. On ne rajoute pas les groupes échangés : on remplace les groupes initiaux.

## Démonstration résolue A — 274, échange d'une dizaine

1. **Matériel :** 2 plaques (100), 7 bandes (10) et 4 jetons (1). Schéma équivalent : `[C]×2 | [D]×7 | [U]×4`.
2. **Première décomposition :** `2 C + 7 D + 4 U = 200 + 70 + 4 = 274`.
3. Défaire **une** bande en **dix** jetons : garder 2 plaques, **6** bandes et **14** jetons.
4. **Seconde décomposition :** `2 C + 6 D + 14 U = 200 + 60 + 14 = 274`. Elle est distincte, mais vaut autant.
5. **Regroupement inverse :** extraire 10 des 14 U → 1 D. Résultat `2 C + 7 D + 4 U`; `200 + 70 + 4 = 274`. Aucun objet perdu ni ajouté.

## Démonstration résolue B — 308, zéro de position et centaine échangée

1. **Matériel :** 3 plaques, 0 bande, 8 jetons. Schéma équivalent : `[C]×3 | [D]×0 | [U]×8`.
2. Première écriture : `3 C + 0 D + 8 U = 300 + 0 + 8 = 308`.
3. Défaire **1 C** en **10 D** : `2 C + 10 D + 8 U = 200 + 100 + 8 = 308`.
4. Inverse : regrouper **10 D** en **1 C** → `3 C + 0 D + 8 U`. Le zéro des dizaines n'est pas « une dizaine invisible »; c'est l'absence de dizaine dans la forme usuelle.

## Contre-exemple A — Changer la valeur pendant un échange

**Énoncé faux :** « `3 C + 5 D + 2 U` devient `3 C + 4 D + 3 U` quand on défait 1 D. »

- Avant : 300 + 50 + 2 = **352**.
- Après (faux) : 300 + 40 + 3 = **343**.
- Correction : `3 C + 4 D + 12 U = 300 + 40 + 12 = 352`. Une dizaine devient **10**, et non **1**, unité. Inverse : 10 des 12 U deviennent 1 D.

## Contre-exemple B — Oublier le zéro intérieur

**Énoncé faux :** « `4 C + 0 D + 6 U` fait 460. »

- `400 + 0 + 6 = **406**`; **460** exigerait `4 C + 6 D + 0 U`.
- Correction : `4 C + 0 D + 6 U = 3 C + 10 D + 6 U = 406`; inverse : 10 D → 1 C.

## Autocontrôle utilisable partout

1. Nommer C, D, U et écrire la valeur de chaque groupe.
2. Additionner avant et après : les deux sommes doivent être identiques.
3. Vérifier que la seconde écriture change réellement les groupements.
4. Faire l'échange inverse à partir de cette seconde écriture et obtenir **exactement** les effectifs C, D, U de la première.

**Accessibilité :** les lettres sont définies et chaque schéma a une description textuelle exhaustive; des blocs peuvent être remplacés par papier quadrillé, jetons, objets palpables ou trois colonnes textuelles. Matériel original proposé; aucune illustration externe reproduite.
