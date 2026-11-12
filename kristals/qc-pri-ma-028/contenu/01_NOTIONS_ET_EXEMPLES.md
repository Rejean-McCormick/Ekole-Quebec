# 01 — Notions, exemples et contre-exemples | `qc-pri-ma-028`

## Cible
**`obj-1` :** Mesurer ou calculer une aire en unités carrées adaptées. **`crit-1` :** Déterminer l’aire de figures quadrillées et expliquer la méthode.

## Définitions exactes

**Surface :** région plane couverte par une figure; **aire :** nombre mesurant l'étendue de cette région dans une unité de surface choisie. Une surface n'est ni le contour ni son périmètre : un fil suivant le bord mesure une **longueur**, alors que des carrés placés sans trou ni chevauchement mesurent une **aire**.

**Quadrillage :** réseau régulier de lignes délimitant des cases carrées de même taille. Pour les figures ci-dessous, chaque `#` est une case occupée et `.` une case vide; toutes les rangées d'une même figure ont le même nombre de positions. Une case entière est comptée une seule fois. Si la longueur de son côté n'est pas donnée, l'unité reste la **case carrée**, notée `u²`, et non `cm²`.

**Unité carrée :** aire d'un carré dont le côté mesure 1 unité de longueur. Si côté = 1 cm, aire = `1 cm × 1 cm = 1 cm²`; si côté = 2 cm, aire = `2 cm × 2 cm = 4 cm²`. Pour convertir un dénombrement de cases en cm², multiplier le nombre de cases par l'aire d'une case; ne jamais inventer l'échelle.

**Méthodes équivalentes quand les cases sont entières :** `A = somme des cases # de toutes les rangées`; pour rectangle plein, `A = rangées × colonnes × aire_case`; pour figure composée, somme des surfaces de sous-rectangles **disjoints**; pour rectangle englobant avec cases vides, `A = A_englobant − nombre de cases vides × aire_case`.

## Exemple résolu 1 — Affiche rectangulaire

Une affiche est quadrillée en carrés de **côté 1 cm** :

```text
####
####
####
```

Il y a trois rangées de quatre cases. Méthode de dénombrement : `4+4+4=12 cases`; méthode de multiplication : `3×4=12 cases`. Chaque case a une aire de `1 cm²`, donc `A=12×1 cm²=12 cm²`. Vérification : les deux méthodes donnent 12; l'unité de la réponse est carrée et connue. **Différence essentielle :** le périmètre du rectangle mesure 14 cm, mais ce n'est pas son aire.

## Exemple résolu 2 — Forme en L, deux méthodes

Sur un quadrillage dont la longueur de côté n'est **pas précisée** :

```text
###.
#...
#...
```

Par rangées : `3+1+1=5 u²`. Découpage sans chevauchement : barre horizontale supérieure = `3×1=3 u²`, prolongement vertical **sous** le coin = `1×2=2 u²`, somme `3+2=5 u²`. Vérification par rectangle englobant de 3 colonnes et 3 rangées : `3×3=9` moins 4 cases vides = `5 u²`. **Interdit de répondre « 5 cm² »**, car la dimension des cases est absente.

## Exemple résolu 3 — L'unité change

Une surface comporte six cases carrées disposées en deux rangées de trois. Les cases ont un **côté de 2 cm**. D'abord `2×3=6 cases`; une case vaut `2×2=4 cm²` et non 2 cm². Alors `A = 6×4 = 24 cm²`. Si les cases avaient 1 cm de côté, le même dessin aurait une aire de 6 cm². Le dessin seul ne détermine pas l'aire physique.

## Contre-exemple 1 — Mesurer le bord au lieu de l'intérieur

**Production erronée :** « Le rectangle de quatre colonnes et trois rangées a une aire de 14 cm. » Cela mesure le **périmètre** : `4+3+4+3=14 cm`. **Correction :** compter douze cases de 1 cm² : `A=12 cm²`. Une grandeur d'aire ne s'exprime pas en `cm`.

## Contre-exemple 2 — Faire deux additions avec recouvrement

**Production erronée :** pour le L `###. / #... / #...`, prendre la barre haute de trois cases et la colonne gauche de trois cases et écrire `3+3=6 u²`. **Erreur :** la case du coin supérieur gauche est comptée **deux fois**. **Correction :** `3+3−1=5 u²` ou deux morceaux disjoints `3+2=5 u²`.

## Contre-exemple 3 — Une unité physiquement fausse

**Production erronée :** « six cases de côté 2 cm, donc 12 cm² ». L'élève a multiplié `6×2` comme s'il s'agissait d'une longueur. **Correction :** `6×(2×2)=24 cm²`; dessiner une seule case de 2 cm de côté sur un quadrillage de 1 cm démontre quatre petits cm².

## Vérification indépendante

Avant de valider : (1) repérer les cases occupées, (2) compter par rangées, (3) vérifier par rectangles disjoints ou complément, (4) vérifier la mesure du côté d'une case et choisir u² ou cm². Aucun autre concept (p. ex. aire du cercle) n'est présumé.
