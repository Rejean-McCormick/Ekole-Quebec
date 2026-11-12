# 01 — Notions, représentations et exemples vérifiés

**Objectif `obj-1` :** Comparer et calculer avec des décimaux en utilisant les valeurs de position.

## Lexique exact

- **Chiffre** : symbole de 0 à 9 dans une écriture. Sa **valeur** dépend de sa position : dans `4,52`, `5` vaut cinq dixièmes, `2` vaut deux centièmes.
- **Nombre décimal (dans ce cours)** : nombre non négatif écrivable avec 0, 1 ou 2 chiffres après la virgule; il vaut un nombre entier de centièmes. Ainsi `3,08 = 308/100` et `3,8 = 380/100`.
- **Rang** : unités, dixièmes (1/10 d'unité), centièmes (1/100 d'unité). `1 dixième = 10 centièmes`; `1 unité = 100 centièmes`.
- **Zéro terminal** : ajouter un zéro à droite de la partie décimale ne change pas la valeur : `2,5 = 2,50`. Mettre un zéro **entre** la virgule et un chiffre change généralement la valeur : `2,05 ≠ 2,5`.
- **Comparer** : déterminer `=`, `<` ou `>` en examinant les rangs de gauche à droite, après harmonisation des écritures.
- **Aligner les rangs** : lors d'une addition ou d'une soustraction, placer unités sous unités et dixièmes sous dixièmes; une virgule sous l'autre, avec des zéros terminaux au besoin.
- **Retenue et échange** : transformer 10 centièmes en 1 dixième, 10 dixièmes en 1 unité, ou l'inverse en soustraction. Chaque échange préserve la quantité.
- **Estimation / plausibilité** : trouver un ordre de grandeur ou des bornes numériques; un résultat peut être exact sans être vraisemblable si les unités ou l'opération ont été mal choisies.

## Représentations utilisables

**Tableau de rangs :**

| Nombre | Unités | Dixièmes | Centièmes |
|---|---:|---:|---:|
| `5,04` | 5 | 0 | 4 |
| `5,4 = 5,40` | 5 | 4 | 0 |
| `0,70` | 0 | 7 | 0 |

Une grille de 100 cases : `0,25` signifie 25 cases sur 100; une droite de 0 à 1 permet de placer `0,2`, `0,20` au même point et `0,02` plus près de zéro. Utiliser une grille tactile ou une description des quantités au besoin.

## Exemple résolu 1 — comparer correctement

Deux bandes mesurent `6,08 m` et `6,8 m`. Écrivons `6,8 = 6,80`. Les unités sont égales (`6`); au rang des dixièmes, `0 < 8`. Donc **`6,08 m < 6,80 m`**. Une estimation confirme : l'une est juste au-dessus de 6 m, l'autre approche 7 m. La seconde mesure dépasse la première de `0,72 m` (calcul en centièmes `680 − 608 = 72`). On compare les mêmes unités, et non le nombre de chiffres.

## Exemple résolu 2 — addition en colonnes

`3,47 L + 2,8 L` : compléter `2,8` en `2,80`. Centièmes : `7 + 0 = 7`; dixièmes : `4 + 8 = 12`, déposer 2 dixièmes et reporter une unité; unités : `3 + 2 + 1 = 6`. **Total `6,27 L`.** En centièmes : `347 + 280 = 627`. Estimation : `3,5 + 2,8 ≈ 6,3`; l'ordre de grandeur convient. Inverse : `6,27 − 2,80 = 3,47`.

## Exemple résolu 3 — soustraction avec échange

`8,20 m − 3,65 m` : en centièmes, `820 − 365 = 455`, donc **`4,55 m`**. Par les rangs, 0 centième ne permet pas de retirer 5 centièmes : échanger 1 dixième en 10 centièmes; le 2 du rang des dixièmes devient 1; 1 dixième ne suffit pas pour retirer 6 dixièmes : échanger 1 unité contre 10 dixièmes, qui deviennent 11; il reste 7 unités. Faire alors `10−5=5` centièmes, `11−6=5` dixièmes, `7−3=4` unités. Vérification : `4,55 + 3,65 = 8,20`. Estimation `8 − 3,5 ≈ 4,5`.

## Exemple résolu 4 — différence et égalité d'écriture

`4,7` et `4,70` sont égaux (`470/100`). En revanche `4,07` est plus petit : `407 < 470` centièmes. Dans les deux cas la comparaison porte sur les valeurs, pas sur la taille des graphies.

## Contre-exemple 1 — « plus de chiffres veut dire plus grand »

**Incorrect :** `5,12 > 5,9`, car `12 > 9`. **Pourquoi :** `12` représente ici *12 centièmes* mais `9` représente *9 dixièmes*. **Correction :** `5,12 < 5,90`. Comparer le rang des dixièmes (`1 < 9`).

## Contre-exemple 2 — addition en alignant les chiffres de droite

**Incorrect :** `2,5 + 0,35 = 0,60` (mélange des rangs). **Correction :** `2,50 + 0,35 = 2,85`. Un contrôle sans colonne suffit : ajouter une quantité positive à `2,5` doit donner plus que `2,5`.

## Contre-exemple 3 — soustraction sans emprunter

**Incorrect :** `7,10 − 2,46 = 5,36` par soustraction chiffre à chiffre sans échange. **Correction :** `710 − 246 = 464` centièmes, soit `4,64`. Test inverse `4,64 + 2,46 = 7,10`; `5,36 + 2,46 = 7,82`, ce qui révèle l'erreur.

## Retour explicite à l'objectif

À chaque nouveau calcul, annoncer l'unité, montrer au moins une représentation (tableau de rangs, grille ou décomposition en centièmes), effectuer le calcul exact et présenter une **vérification chiffrée de plausibilité**.
