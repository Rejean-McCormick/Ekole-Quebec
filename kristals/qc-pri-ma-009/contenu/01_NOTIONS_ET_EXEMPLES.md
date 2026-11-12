# 01 — Notions et exemples commentés

**Cible (`obj-1`) :** Représenter le partage et le groupement pour résoudre des divisions.

## Les quatre notions

1. **Partage équitable :** une quantité totale `N` d'objets entiers est répartie entre `d` personnes/boîtes; on cherche combien chaque destinataire reçoit **également**, puis combien restent non distribués. Le nombre de destinataires `d` est connu.
2. **Groupement :** une quantité totale `N` est rangée par groupes **de taille `d`**; on cherche le nombre de groupes complets `q` et les objets ne formant pas un groupe complet.
3. **Quotient entier `q` :** nombre d'objets par destinataire dans un partage; nombre de groupes complets dans un groupement. Il peut valoir zéro lorsque `N<d` (non requis comme réponse de départ; utilisé en enrichissement).
4. **Reste `r` :** nombre d'objets qui ne peuvent être répartis également ou placés dans un groupe complet sans changer les règles. Il est entier, `0 ≤ r < d`. Le reste 0 signifie qu'il n'y a rien de non distribué.

**Convention commune :** `N = d × q + r`, avec `N ≥ 0`, `d ≥ 1`, `q ≥ 0` et `0 ≤ r < d`. Les valeurs sont des entiers. Le diviseur `d` ne peut pas être 0 : on ne peut ni partager entre zéro destinataire ni fabriquer des groupes de taille zéro. L'identité multiplicative est la **vérification**, pas une réponse sans explication.

## Exemple résolu A — Partage (matériel → schéma → notation)

**Situation.** On répartit 26 craies entre 4 équipes, en donnant le même nombre à chaque équipe. Combien par équipe et combien à part?

- **Matériel imaginaire :** donner une craie à chacune des quatre équipes six fois, soit 24 craies, puis mettre 2 craies de côté.
- **Schéma textuel :** Équipe A : `●●●●●●`, B : `●●●●●●`, C : `●●●●●●`, D : `●●●●●●`; reste `●●`.
- **Calcul :** `26 ÷ 4 = 6` reste `2`, puisque `4 × 6 + 2 = 26` et `2 < 4`.
- **Interprétation :** chaque équipe reçoit **6 craies** et **2 craies restent**. Le quotient est en craies par équipe.

## Exemple résolu B — Groupement (groupes complets)

**Situation.** Une personne prépare des trousses contenant 7 fiches chacune, avec 45 fiches disponibles. Combien de trousses complètes et combien de fiches libres?

- **Essai multiplicatif :** `7 × 6 = 42`; `7 × 7 = 49` dépasserait le stock.
- **Schéma :** six boîtes `[7][7][7][7][7][7]`, puis `3` fiches hors boîte.
- **Calcul :** `45 ÷ 7 = 6` reste `3`; `45 = 7 × 6 + 3`, `3 < 7`.
- **Interprétation :** **6 trousses complètes**, **3 fiches restantes**. Le quotient se compte en trousses, pas en fiches par personne.

## Deux contre-exemples commentés

**Contre-exemple 1 — Un reste trop grand.** « `29 ÷ 6 = 3` reste `11` » reconstruit bien `6×3+11=29`, **mais n'est pas une division terminée**, car `11 ≥ 6` : on peut former un quatrième groupe. Correction : `29 = 6×4+5`, donc quotient `4`, reste `5`.

**Contre-exemple 2 — Une fausse égalité due à l'oubli du reste.** « `33 ÷ 8 = 4` exactement, car `8×4=33` » est faux : `8×4=32`. Il reste `1`, donc `33 = 8×4+1`, `1<8`. La réponse « quatre paquets complets, une carte restante » conserve le sens du problème.

## Comparer les deux sens sans les confondre

Pour `27 ÷ 5 = 5` reste `2` : **partage** = 27 jetons entre 5 enfants : 5 jetons chacun, 2 restants; **groupement** = pochettes de 5 jetons : 5 pochettes, 2 jetons restants. L'écriture est identique, la question, l'unité du quotient et la représentation diffèrent.

**Auto-contrôle oral :** « Qui ou quoi représente `d`? Que compte `q`? Pourquoi `r` ne permet-il pas une part/un groupe de plus? »
