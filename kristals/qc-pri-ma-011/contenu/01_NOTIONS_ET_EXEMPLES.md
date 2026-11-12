# 01 — Notions et exemples commentés

**Kristal :** `qc-pri-ma-011` · **Objectif `obj-1` :** Exécuter, vérifier et expliquer une procédure de calcul écrit. **Preuve `crit-1` :** Calculer puis détecter une erreur dans une procédure proposée.

## Comprendre plutôt qu'imiter

- **Algorithme écrit :** une succession d'étapes précises qui donne une réponse correcte *si chaque étape respecte la quantité et sa position*. Écrire 5 sous la colonne des unités ou sous les dizaines n'a pas le même effet. L'algorithme n'est pas une formule magique : les retenues sont des échanges entre dix unités et une dizaine, ou dix dizaines et une centaine.
- **Valeur de position :** 602 = 6 centaines + 0 dizaine + 2 unités. On peut aussi représenter **602 = 5 centaines + 10 dizaines + 2 unités**, puis **5 centaines + 9 dizaines + 12 unités**. Les trois écritures représentent le même nombre : 500+90+12=602.
- **Contrôle inverse :** effectuer une autre opération pour confirmer le résultat : addition `a+b=s` ↔ soustraction `s−b=a`; soustraction `a−b=d` ↔ addition `d+b=a`; multiplication `a×b=p` ↔ division exacte `p÷b=a` quand `b≠0`. Ce contrôle n'est pas une preuve si on y répète exactement la même erreur.
- **Estimation :** évaluer la grandeur avant de poser, comme 268+157 ≈ 270+160 ≈ 430. L'estimation détecte des absurdités, mais **ne remplace pas** le contrôle exact.

## Représentations complémentaires

| Vue | Pour 268 + 157 | Pourquoi utile |
|---|---|---|
| Matériel regroupable | 15 unités sont échangées contre 1 dizaine et 5 unités; puis 12 dizaines contre 1 centaine et 2 dizaines | Rend visibles les échanges, sans changer le total. |
| Tableau de position | C : 2+1+**1 reportée** = 4; D : 6+5+**1 reportée** = 12, on écrit 2; U : 8+7=15, on écrit 5 | Montre où placer le report. |
| Écriture symbolique | `268 + 157 = 425` | Résume l'algorithme une fois le sens compris. |

Une soustraction nécessitant un échange se représente de la même façon en sens inverse : remplacer 1 centaine par 10 dizaines, puis 1 dizaine par 10 unités.

## Exemple résolu A — Addition avec deux retenues

**Question.** 268 + 157. **Copie proposée :** « 8+7=15, j'écris 5 et retiens 1; 6+5+1=12, j'écris 2 et retiens 1; 2+1=3. Réponse : 325. »

1. **Unités :** 8+7=15 unités = 1 dizaine et 5 unités; écrire 5 et reporter 1 dizaine.
2. **Dizaines :** 6+5+1=12 dizaines = 1 centaine et 2 dizaines; écrire 2 et reporter 1 centaine.
3. **Centaines :** 2+1+1=4 centaines. **Résultat : 425**.
4. **Premier faux pas de la copie :** au rang des centaines, le report de 1 centaine a été oublié; `2+1=3` aurait dû être `2+1+1=4`.
5. **Contrôle inverse :** 425−157=268. On a donc retrouvé le premier terme sans recopier l'addition.

## Exemple résolu B — Soustraction à travers un zéro

**Question.** 602−175. **Copie proposée :** « Après avoir fait 12−5=7 et 9−7=2, il reste 6 centaines; j'écris 527. »

1. Écrire `602 = 6 C + 0 D + 2 U`. L'unité 2 ne permet pas de retirer 5 unités.
2. Transformer 1 centaine en 10 dizaines, puis 1 dizaine en 10 unités : **5 C + 9 D + 12 U**.
3. Calculer `12−5=7`, `9−7=2`, `5−1=4` → **427**.
4. **Premier faux pas :** la copie garde 6 centaines même après l'échange. Elle a compté une centaine deux fois.
5. **Contrôle inverse :** 427+175=602. L'échange a été correctement compensé.

## Exemple complémentaire — Multiplication courte

**46×3** : 6×3=18 → écrire 8 unités et reporter 1 dizaine; 4 dizaines×3 + 1 dizaine = 13 dizaines → **138**. Vérifier par `138÷3=46`, ou `46+46+46=138` si la division n'est pas disponible. Ici le report se fait vers les dizaines, exactement comme dans une addition.

## Deux contre-exemples explicités

- **CE-1 — `268 + 157 = 325` : faux.** Le total exact est 425; la quantité `1 C` issue de `12 D` a disparu. L'algorithme n'est pas correct même si les deux premières colonnes sont bonnes.
- **CE-2 — `602 − 175 = 527` : faux.** Après échange, il reste **5 C** avant de retrancher la centaine; le calcul proposé garde incorrectement 6 C. La recomposition `527 + 175 = 702`, et non 602, démasque aussi l'erreur.
- **CE-3 — `507 + 68 = 1187` : faux.** La copie a aligné 68 avec les centaines/dizaines, ce qui correspond à ajouter 680. Il faut aligner les **unités** : `507+68=575`; `575−68=507`.

## À retenir et dire avec ses mots

1. « Chaque chiffre vaut des unités, des dizaines, des centaines… »
2. « Quand je reporte ou j'emprunte, je transforme la quantité sans la changer. »
3. « Je cherche le **premier** pas incorrect et je teste mon résultat par l'opération inverse. »

Les nombres, histoires, tableaux et copies fictives de cette leçon sont des productions originales; aucune reproduction d'exercice externe.
