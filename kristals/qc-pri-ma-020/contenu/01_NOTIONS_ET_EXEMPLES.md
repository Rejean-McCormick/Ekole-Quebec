# 01 — Notions, exemples et contre-exemples

## Question directrice

Comment reconnaître si une situation met en jeu des groupes égaux, un rapport constant ou un partage? Une opération est une **traduction de la relation**, pas un mot-clé deviné. On doit pouvoir expliquer ce que chaque nombre représente.

## Les quatre notions

**Groupes égaux.** Si `g` ensembles ont chacun `p` objets de même nature, le total est `T = g × p`. Représentations : `g` paquets de `p` jetons; `g` barres de longueur `p`; un tableau `g | p par groupe | T`; et l'équation avec unité. Ne pas intervertir le sens des facteurs dans la légende, même si le produit est égal.

**Proportion simple.** Si chaque unité a une quantité identique `p` d'une autre grandeur, `T = p × g`; le coefficient `p` est constant. Par exemple, une étagère porte 4 pots : 1 étagère = 4 pots, 3 étagères = 12 pots. Ce modèle est valide uniquement si chaque étagère contient 4 pots. Il ne prétend pas que toutes les relations sont proportionnelles.

**Quotient entier.** Avec `N` objets et une taille de groupe `d` entière, positive, `q = N // d` représente le nombre de groupes complets; dans un **partage en d groupes**, `q` devient le nombre d'objets par groupe. Lire attentivement la question pour choisir l'interprétation de `q`.

**Reste.** `r = N − d × q`. La division euclidienne vérifie `N = d×q + r` et `0 ≤ r < d`. Dans une division euclidienne, un reste ne disparaît pas : selon la question on le garde à part, on demande un contenant supplémentaire, ou on indique qu'une répartition parfaitement égale en entiers est impossible. Ne divise jamais par zéro.

## Deux exemples commentés et vérifiés

**Exemple A — Groupes et tableau (proportion simple).** Chaque boîte contient 7 fiches. Combien de fiches pour 5 boîtes? Concret : dessiner cinq boîtes et placer sept traits dans chacune. Tableau : boîtes `1, 2, 5` → fiches `7, 14, 35`. Équation : `5 × 7 = 35 fiches`. Vérification : `7 + 7 + 7 + 7 + 7 = 35`; quotient de contrôle `35 ÷ 5 = 7 fiches/boîte`. Unité finale : fiches, pas boîtes.

**Exemple B — Quotient, reste et décision.** On dispose de 29 rubans; un bouquet utilise 6 rubans. Combien de bouquets complets? Dessiner quatre cercles contenant chacun six traits, puis cinq traits isolés. `29 = 6 × 4 + 5`; `q=4`, `r=5`, et `0≤5<6`. Réponse : quatre bouquets complets et cinq rubans restants. Si la question était « combien de contenants de six places pour ranger tous les rubans? », réponse : **cinq contenants**, dont un incomplet. Vérification : cinq bouquets complets prendraient `5×6=30>29`, impossible.

**Exemple C — Partage équitable (sans reste).** 36 cartes sont réparties également entre 9 élèves. Neuf parts égales contiennent chacune quatre cartes. Schéma : neuf cases étiquetées 4. `36÷9=4 cartes par élève`; vérification `9×4=36` et reste `0`.

## Deux contre-exemples analysés

**Contre-exemple 1 — Multiplier des groupes inégaux.** Trois tables portent 4, 5 et 6 livres. Écrire `3×5=15` simplement parce qu'il y a trois tables et que l'une porte cinq livres n'est **pas un modèle valide** des groupes de taille constante. Le total réel `4+5+6=15` coïncide ici par hasard. Il serait faux de justifier le calcul par « cinq livres à chaque table ». Modification diagnostique : pour 4, 5 et 8, la même méthode donnerait `3×5=15`, mais le total est `17`. Il faut additionner les groupes réellement inégaux ou construire des regroupements justifiés.

**Contre-exemple 2 — Reste supérieur au diviseur.** Affirmer `29 = 6 × 3 + 11` comme résultat final donne bien une égalité, mais ce n'est **pas** une division euclidienne achevée, car `11≥6`. On peut former un quatrième bouquet : `29 = 6 × 4 + 5`; il reste cinq rubans, strictement moins que six.

**Contre-exemple 3 — Contenants confondus avec paquets complets.** 22 figurines, boîtes de 5 : répondre « cinq boîtes pleines » est faux. `22=4×5+2`: quatre boîtes pleines; cinq boîtes requises si l'on range les 22 figurines.

## Vérification en quatre questions

1. De quelles grandeurs parle-t-on? Quelles unités?
2. Les groupes sont-ils égaux / le rapport est-il constant? Que représente le diviseur?
3. L'égalité est-elle vraie, et si division, `0 ≤ r < d`?
4. La réponse porte-t-elle sur **objets**, **groupes complets**, **objets par groupe** ou **contenants nécessaires**?
