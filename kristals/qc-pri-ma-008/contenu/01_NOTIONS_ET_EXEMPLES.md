# 01 — Notions et exemples | qc-pri-ma-008

## But de la leçon

Comprendre **ce qu'on compte** avant de calculer : combien de groupes égaux? combien d'objets dans **chaque** groupe? combien d'objets au total? Le résultat numérique n'est pas suffisant si le dessin, l'opération ou l'unité ne correspond pas à l'histoire.

### Notion A — Groupes égaux et itération

Une multiplication d'entiers naturels `a × b` peut représenter **a groupes de b objets**. La somme itérée correspondante contient `a` termes de valeur `b`. Dans cette convention de lecture, `3 × 4` signifie `4 + 4 + 4 = 12`. Le signe `×` n'est pas le signe `+`; on ne doit pas simplement additionner 3 et 4. Pour zéro groupe, le total est 0; la plupart des activités ici utilisent au moins deux groupes pour rendre le modèle visible.

**Exemple résolu 1 — Paniers de poires.** Quatre paniers contiennent chacun trois poires.

- **Concret :** prendre 4 petites assiettes et placer 3 jetons sur chacune.
- **Schéma :** `[● ● ●]  [● ● ●]  [● ● ●]  [● ● ●]` (quatre groupes séparés).
- **Addition :** `3 + 3 + 3 + 3 = 12`.
- **Multiplication :** `4 × 3 = 12 poires`.
- **Vérification :** dénombrer 4 groupes de 3, soit 12 jetons. Si un panier contenait 4 poires, les groupes ne seraient plus tous égaux.

### Notion B — Tableau rectangulaire (rangées et colonnes)

Un **tableau** (array) est un arrangement en lignes et en colonnes, avec le même nombre de points dans chaque ligne et le même nombre dans chaque colonne. Pour `3 × 5`, on trace trois lignes de cinq points :

```text
● ● ● ● ●
● ● ● ● ●
● ● ● ● ●
```

Lignes : `5 + 5 + 5 = 15`; colonnes : `3 + 3 + 3 + 3 + 3 = 15`. On voit que `3 × 5 = 5 × 3 = 15`, même si **trois paquets de cinq crayons** et **cinq paquets de trois crayons** sont deux organisations différentes.

### Notion C — Propriété distributive

Quand on sépare **la taille de chaque groupe**, on additionne les deux produits : `a × (b + c) = a × b + a × c` pour les nombres utilisés ici. Cette égalité fonctionne parce que chacun des `a` groupes apporte `b` objets **et** `c` objets.

**Exemple résolu 2 — Cinq rangées de six places.** Une salle a 5 rangées identiques de 6 places. Chaque rangée est séparée en 4 places à gauche et 2 à droite.

```text
● ● ● ● | ● ●
● ● ● ● | ● ●
● ● ● ● | ● ●
● ● ● ● | ● ●
● ● ● ● | ● ●
```

- **Tableau entier :** `5 × 6 = 30 places`.
- **Deux sous-tableaux :** `5 × (4 + 2) = (5 × 4) + (5 × 2) = 20 + 10 = 30 places`.
- **Contrôle :** cinq rangées de six = `6 + 6 + 6 + 6 + 6 = 30`. Les deux moyens donnent le même total.

**Exemple résolu 3 — Trois équipes de huit.** `3 × 8 = 3 × (5 + 3) = 15 + 9 = 24 personnes`. Schéma acceptable : trois rectangles, chacun contenant huit points séparés en cinq et trois.

### Contre-exemples : lire avant de calculer

1. **Groupes inégaux :** trois paniers contiennent respectivement 2, 3 et 4 poires. Ce n'est **pas** `3 × 3` comme représentation de la situation, même si `2 + 3 + 4 = 9` et `3 × 3 = 9` donnent par hasard le même total. On doit conserver les quantités originales (`2 + 3 + 4`). Pour créer des groupes égaux de trois, il faudrait redistribuer les poires; cela changerait le modèle de la situation initiale.
2. **Facteurs additionnés :** quatre paniers de trois poires ne font pas `4 + 3 = 7`; il y a quatre **fois trois** poires, soit 12.
3. **Distribution incomplète :** `4 × (5 + 2) = 4 × 5 + 2 = 22` est incorrect : les 2 objets supplémentaires existent dans **chacun** des quatre groupes. Correction : `4 × 5 + 4 × 2 = 20 + 8 = 28`.

### Erreurs d'orientation

Si l'on raconte « 4 groupes de 3 », on écrit `4 × 3`; en comptant les mêmes objets par colonnes, on pourrait écrire `3 × 4`. Le total est le même, mais on explicite le changement de point de vue. Une représentation ne doit pas changer silencieusement la quantité **par groupe** demandée dans le contexte.

**Auto-vérification :** peux-tu dire à voix haute « nombre de groupes », « objets par groupe » et « total avec son unité » en montrant ton dessin?
