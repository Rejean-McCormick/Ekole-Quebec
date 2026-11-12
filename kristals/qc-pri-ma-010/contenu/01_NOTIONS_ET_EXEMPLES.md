# 01 — Notions, représentations, exemples et contre-exemples

## Ce que l'on cherche à savoir faire
**Objectif `obj-1` :** Choisir une stratégie de calcul mental et mobiliser une propriété opératoire. La réponse seule ne suffit pas : on compare au moins deux voies et on explique celle qui convient le mieux.

## Trois idées à ne pas confondre

### 1. Commutativité de l'addition : échanger
Avec des nombres naturels `a` et `b`, `a+b=b+a`.
- `19+31=31+19=50` : deux piles de jetons ne changent pas de quantité quand on les inverse.
- **Schéma textuel :** `[19 jetons] + [31 jetons]` ↔ `[31 jetons] + [19 jetons]` ; total identique.
- Cette propriété est aussi vraie pour la multiplication, mais sa maîtrise n'est **pas** exigée ici. Elle **n'est pas vraie** pour la soustraction ni la division en général.

### 2. Associativité de l'addition : regrouper
`(a+b)+c=a+(b+c)`. L'ordre des termes reste le même, mais les parenthèses changent.
- `(26+14)+35=40+35=75` et `26+(14+35)=26+49=75`.
- **Attention :** passer de `25+16+75` à `(25+75)+16` emploie d'abord la **commutativité** pour échanger 16 et 75, puis l'**associativité** pour regrouper.
- **Schéma textuel :** trois boîtes `25 | 16 | 75`; déplacer 75 près de 25, former `100`, puis ajouter 16.

### 3. Compensation : transformer deux termes en sens équilibré
Pour l'addition, si `0≤k≤b`, `a+b=(a+k)+(b−k)` : ce que l'on donne au premier terme, on le prend au second.
Pour la soustraction, `a−b=(a+k)−(b+k)` tant que les nombres sont traités correctement : déplacer les deux termes d'une même distance ne change pas leur écart.
- Addition : `48+37=(48+2)+(37−2)=50+35=85`.
- Soustraction : `154−98=(154+2)−(98+2)=156−100=56`.
- **Représentation de droite numérique :** pour la soustraction, les positions 98 et 154 ont un écart de 56; déplacées de `+2`, les positions 100 et 156 ont toujours un écart de 56. Pour l'addition, deux récipients contiennent 48 et 37 unités : transférer deux unités ne change pas le total.

## Exemples résolus et commentés

**Exemple résolu A — chercher une paire qui fait 100.** Calcul : `25+16+75`.
- Stratégie 1 : `(25+16)+75=41+75=116`.
- Stratégie 2 : échanger 16 et 75, puis regrouper : `(25+75)+16=100+16=116`.
- **Choix expliqué :** la seconde est souvent plus confortable, parce que `25+75` forme exactement 100. Les deux sont justes, sans qu'une préférence non argumentée soit obligatoire.

**Exemple résolu B — déplacer des unités entre les termes.** Calcul : `48+37`.
- Stratégie 1 : `48+30+7=78+7=85`.
- Stratégie 2 : transférer 2 du 37 vers le 48 : `50+35=85`.
- **Choix expliqué :** la seconde obtient un multiple de dix immédiatement; `+2` et `−2` se compensent. Vérification : 50+35=85, 48+37=85.

**Exemple résolu C — soustraction près de 100.** Calcul : `154−98`.
- Stratégie 1 : `154−100+2=54+2=56` (soustraire 2 de trop puis rendre 2).
- Stratégie 2 : `(154+2)−(98+2)=156−100=56` (compensation des deux termes).
- **Choix expliqué :** une ou l'autre convient; si retrancher 100 est familier, la deuxième montre directement l'écart invariant. La transformation `154−98=154−100` serait incorrecte.

## Contre-exemples : corriger le piège, pas seulement le nombre

**Contre-exemple 1 — fausse commutativité de la soustraction.** « `63−18=18−63` » : faux. `63−18=45`; `18−63` ne représente pas la même quantité (et n'est pas une soustraction dans les naturels). La propriété `a+b=b+a` ne permet pas d'inverser `−`.

**Contre-exemple 2 — compensation incomplète.** « `47+36=50+36=86` » : faux; `47+36=83`. En ajoutant 3 au premier terme, il faut retirer 3 au second : `50+33=83`.

**Contre-exemple 3 — soustraction non associative.** « `80−(30−10)=(80−30)−10` » : faux; la gauche vaut `80−20=60`, la droite vaut `50−10=40`. Les parenthèses ont un effet dans une soustraction.

## Comment comparer deux stratégies
1. **Résultat :** chacune conserve-t-elle la valeur de l'expression initiale ?
2. **Justification :** quel échange, regroupement ou ajustement égal la rend valide ?
3. **Confort / fiabilité :** laquelle forme plus vite dix ou cent, avec moins de petites étapes difficiles ?
4. **Vérification :** estimation, décomposition ou seconde stratégie. « C'est plus facile » sans raison mathématique n'est pas suffisant.
