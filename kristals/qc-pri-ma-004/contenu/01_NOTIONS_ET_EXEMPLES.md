# 01 — Notions, représentations, exemples et contre-exemples

**Kristal :** `qc-pri-ma-004` · **Objectif :** `obj-1` · **Critère :** `crit-1`.

## À retenir, exactement

- **Suite numérique :** liste ordonnée de nombres (termes) dont chaque place a un rang; une description de sa régularité permet de poursuivre la liste selon la règle retenue.
- **Motif :** groupe d'éléments ou d'écarts qui se répète. Dans `1, 4, 1, 4, 1, 4`, le motif minimal des valeurs est `[1,4]`. Dans `2, 5, 8, 11`, c'est le saut `+3` qui se répète, non les valeurs elles-mêmes.
- **Pas constant (suite arithmétique) :** différence signée `d = t(n+1) − t(n)` qui garde la même valeur à chaque intervalle. Positif : on augmente; négatif : on diminue. Un motif de valeurs alternées n'a généralement **pas** de pas constant.
- **Règle :** instruction qui contient un début et une opération répétée, par exemple « commencer à 6 et retirer 2 à chaque étape ». Pour `n` à partir de 1, la vérification facultative est `t(n)=a+(n−1)d`.
- **Terme manquant :** nombre absent à un rang donné et reconstitué **sous la règle explicitement énoncée ou testée**. Une suite finie seule peut accepter d'autres continuations; on ne prétend pas déduire une règle unique de trois observations.

## Exemple résolu A — Les jetons (concret → schéma → nombres)

Une personne pose 4 jetons sur la table à l'étape 1, puis en ajoute 3 par étape. Combien à l'étape 5?

| Étape (rang) | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| Jetons | 4 | 7 | 10 | 13 | **16** |

Schéma textuel : `4 --(+3)--> 7 --(+3)--> 10 --(+3)--> 13 --(+3)--> 16`.

**Raisonnement :** chaque ajout forme un groupe de 3 jetons. Au rang 5, il y a quatre ajouts : `4+4×3=16`. **Règle complète :** partir de 4, ajouter 3 à chaque rang. **Vérification :** `7−4=3`, `10−7=3`, `13−10=3`, `16−13=3`. Conserver les jetons puis retirer ce support quand l'élève peut utiliser les flèches seul.

## Exemple résolu B — Case intérieure et pas négatif

La consigne garantit un **pas constant** : `26, 21, __, 11, 6, __`.

1. Calculer les écarts connus : `21−26=−5`; `6−11=−5`.
2. Insérer `21−5=16` : `26,21,16,11,6,…`.
3. Ajouter le dernier terme `6−5=1`.
4. **Règle :** partir de 26 et soustraire 5 à chaque étape; **vérifier** `16−21=−5`, `11−16=−5`, `1−6=−5`.

## Exemple résolu C — Motif de valeurs (pas différent)

`2, 6, 2, 6, __, __` : le motif de valeurs `[2,6]` se répète; solutions `2,6`. Les écarts sont `+4,−4,+4,−4,+4` : il serait incorrect de dire « le pas constant est +4 ». Règle : répéter 2, puis 6, dans cet ordre.

## Contre-exemples corrigés

1. **Règle annoncée « toujours +2 » pour `3,5,8,10`** : faux, car les écarts sont `+2,+3,+2`; corriger en « ce jeu de données ne suit pas un pas constant +2 »; ne pas inventer la prochaine valeur à partir d'un pas non vérifié.
2. **Case `8, __, 18` remplie par 18** en supposant un pas constant : faux; il existe deux intervalles de 8 à 18, soit `10÷2=5` par pas. Le terme intérieur est **13** (`8,13,18`).
3. **Motif `1,3,1,3` appelé « +2 à chaque fois »** : faux au passage `3→1` (`−2`). C'est un motif répété `[1,3]`, non un pas constant.

## Limites conceptuelles et précision

- Toujours indiquer une hypothèse comme « avec un pas constant » ou accepter une **règle explicitée et vérifiée** lorsque plusieurs règles concordent sur les termes affichés.
- Une progression telle que `2,4,6,8` est **compatible** avec `+2`, mais les quatre termes ne prouvent pas que la suite infinie suit cette règle de façon unique.
- Valeurs des activités à pas constant : entiers non négatifs au rang demandé, pas non nul. Pas de nécessité de fractions, de multiplication complexe ou de vitesse de calcul.
