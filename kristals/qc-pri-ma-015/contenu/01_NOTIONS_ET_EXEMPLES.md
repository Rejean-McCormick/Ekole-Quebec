# 01 — Notions et exemples | qc-pri-ma-015

## Objectif et convention d'unité

**Objectif `obj-1` :** Relier les écritures décimales aux décompositions en dixièmes et centièmes. **Preuve `crit-1` :** Représenter un même décimal par un dessin et une décomposition. **Convention fondamentale :** une grille carrée de 10 rangées × 10 colonnes de même aire représente exactement *une unité*; une bande de dix cases représente un dixième et une case un centième. Les cases ne sont pas des nombres tout seuls : leur valeur dépend du tout fixé. Pour une grandeur comme 1 m, le segment de 1 m joue le rôle d'unité, découpé en cent longueurs de 1 cm.

## Définitions mathématiques vérifiables

- **Écriture décimale :** notation de base 10 à virgule. Ici, pour un entier `N` de 0 à 299, la valeur étudiée est `N/100`, notée avec deux chiffres après la virgule, éventuellement un seul si le dernier est nul. `0,70 = 0,7` et `2,00 = 2` expriment la même quantité. Le mot *décimal* désigne plus généralement un nombre à écriture décimale finie; la borne de deux rangs est un choix de ce cours, non sa définition universelle.
- **Dixième :** `1/10` d'une unité partagée en dix parts égales : `0,1 = 0,10 = 10/100`.
- **Centième :** `1/100` d'une unité partagée en cent parts égales : `0,01`; dix centièmes sont un dixième.
- **Valeur de position :** `1,26` = `1` unité, `2` dixièmes, `6` centièmes = `100/100 + 20/100 + 6/100 = 126/100`.
- **Droite graduée :** axe portant des points de référence (0 et 1, ou 1 et 2) et des intervalles *égaux*. Pour placer `0,47`, avancer de 47 petits intervalles sur 100, ou de 4 dixièmes et 7 centièmes. La place dépend des *distances*, pas du nombre d'étiquettes écrites.

## Lire une grille sans couleur

Sur une grille 10 × 10, les cases sont repérées `(r,c)` avec `r=1…10`, `c=1…10`. On les parcourt de gauche à droite puis de haut en bas. **Grille pour 0,36 :** marquer les 30 cases des rangées 1–3 puis les six cases `(4,1)…(4,6)`. Conserver la hachure « / » pour les cases prises et « . » pour les autres : ce code textuel est équivalent à un dessin, tant que l'unité 100 cases est indiquée.

```
Unité = 100 cases   / = colorié   . = vide
//////////  (10)
//////////  (10)
//////////  (10)
//////....  ( 6)
..........  ( 0) × 6 rangées
```

On dénombre `10+10+10+6 = 36` cases, donc `0,36 = 3/10 + 6/100`. Le dessin n'utilise pas 36 cases distribuées dans une grille de taille inconnue : *toute* la grille vaut 1.

## Exemple résolu E1 — zéro unité, dixièmes puis centièmes

**Énoncé :** représenter `0,47` par dessin et décomposition, puis sur une droite `0–1`. **Méthode :** 47 cases = 4 bandes de dix cases + 7 cases du 5e rang. Faire le dessin (quatre rangées pleines et les sept premières cases du cinquième rang). Écrire : `0,47 = 4/10 + 7/100 = 40/100+7/100 = 47/100`. Pour la droite, diviser de 0 à 1 en 100 petits pas identiques; marquer le 47e pas. **Contrôle :** `4×10+7=47`, strictement inférieur à 100, donc la quantité est entre 0 et 1.

## Exemple résolu E2 — unité entière et fraction d'unité

**Énoncé :** représenter `1,24`. **Méthode :** dessin n°1 entièrement hachuré : `100` cases. Dessin n°2 : les 20 cases de deux bandes et quatre cases supplémentaires. Puis `1,24 = 1 + 2/10 + 4/100 = (100+20+4)/100 = 124/100`. Sur une droite `1–2`, avancer de 24 pas de 1/100 depuis `1`. **Contrôle :** 1 tout et 24 centièmes ne peuvent être illustrés dans une grille de 100 cases sans changer d'unité; il faut deux grilles ou un schéma montrant le tout + le reste.

## Exemple résolu E3 — zéro final et équivalence

`0,70` représente 70 cases d'une grille de 100, soit 7 bandes. `0,70 = 7/10 + 0/100 = 7/10 = 0,7`. Sur la droite, le repère est aux 7/10 de l'unité, pas aux 70 unités. Le zéro placé *à droite* du 7 n'ajoute pas de valeur.

## Contre-exemples dépliés

1. **Faux :** « `0,5 = 5/100` » parce qu'il y a un 5. **Correction :** le premier rang après la virgule est celui des dixièmes : `0,5 = 5/10 = 50/100`. `5/100` est `0,05` et dix fois plus petit.
2. **Faux :** « une grille pleine + 26 cases = `0,26` ». **Correction :** grille pleine = `1`, donc `1,26`.
3. **Faux :** droite `0–1` tracée avec dix intervalles de tailles variables mais étiquetés `0,1`, `0,2`… **Correction :** une graduation est une mesure régulière; les dix segments doivent avoir la même longueur pour représenter des dixièmes égaux.
4. **Faux :** « `0,09` = neuf dixièmes ». **Correction :** 9 cases parmi 100, pas 9 bandes de 10 cases.

## Test d'autoexplication

Sans compter seulement sur la notation : explique pourquoi `0,30` et `0,3` occupent le même point; pourquoi `0,03` n'y est pas; puis démontre avec des cases que `0,9 = 90/100`. L'adulte vérifie unité, alignement case→centième et logique du regroupement; la vitesse de dessin n'est pas notée.
