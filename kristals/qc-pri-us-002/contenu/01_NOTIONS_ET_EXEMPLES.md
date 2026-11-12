# 01 — Notions, cartes et exemples résolus

> **Identité du module :** `qc-pri-us-002` · `obj-1` · `crit-1` · famille `qc-pri-us-002-ev-01`. **Plan fictif** : toutes les cartes, lieux et distances des exercices sont créés pour l’enseignement et ne décrivent pas un territoire existant.

## Définitions exactes et règles

- **Carte** : représentation sélectionnée et réduite d’un espace selon un titre, des conventions graphiques et un but. Elle ne donne pas nécessairement tous les renseignements sur le terrain; ici, les plans sont des **schémas inventés**.
- **Orientation** : manière de situer les directions. Sur **nos** cartes, la flèche `N ↑` fixe le nord en haut, le sud en bas, l’est à droite et l’ouest à gauche. Ce n’est pas une règle universelle valable pour toute carte : on vérifie sa flèche/rose.
- **Symbole** : signe ou lettre figurant un lieu ou une caractéristique; son sens dépend de la **légende du document précis**, pas de sa ressemblance avec un objet.
- **Légende** : clé de lecture des symboles du plan. `X` ne signifie pas toujours la même chose d’une carte à l’autre.
- **Échelle simple** : relation annoncée entre une distance sur le schéma et la distance représentée. Pour nos quadrillages : « un déplacement entre deux cases voisines par un côté = k mètres ». Une route de n déplacements mesure **n × k mètres**, dans le modèle; ce n’est pas une distance à vol d’oiseau ni une garantie sur une route réelle.
- **Repère de case** : une coordonnée comme `C2` signifie **colonne C, ligne 2**, et non ligne C. Deux cases se touchent par un côté si leur différence est d’une colonne OU d’une ligne, jamais les deux.
- **Parcours justifié** : une suite de cases à partir d’un lieu, vers un autre, passant uniquement par des cases permises, accompagnée d’une explication qui renvoie au titre, à la légende, à la flèche nord et à l’échelle quand c’est utile.
- **Limite d’un document** : un plan fictif ne permet pas d’affirmer qu’une route est sûre, accessible, ouverte ou réalisable dans le monde réel. L’énoncé n’évalue que sa lecture dans les règles du plan.

## Carte A — Plan modèle

**Plan fictif du parc des Érables** (carte schématique *inventée*, non géographique).
Flèche N ↑ : le nord est vers le haut; l’est se trouve à droite (→). Colonnes A, B, C, D de gauche à droite; lignes 1 à 4 de haut en bas.
```text
   A  B  C  D
1  .  .  B  .
2  E  .  X  .
3  .  .  .  P
4  .  M  .  .
```
Légende : `E` = école; `B` = bibliothèque; `P` = parc; `M` = musée; `X` = bassin infranchissable; `.` = passage libre. Échelle du plan : **un déplacement entre deux cases voisines par un côté = 100 m**.
Règle de parcours : partir de la première case citée, passer uniquement entre cases voisines horizontalement ou verticalement; diagonales interdites; symbole de lieu traversable; case interdite non traversable. Les noms et distances ne décrivent aucun lieu réel.

### Exemple résolu 1 — De l’école à la bibliothèque

1. Lire le **titre** : ce schéma représente le parc des Érables fictif.
2. Lire la **légende** : `E` est l’école en `A2`; `B` est la bibliothèque en `C1`; `X` en `C2` est un bassin impraticable.
3. Lire **N ↑** : aller vers le haut, c’est aller vers le nord; vers la droite, c’est l’est.
4. Tracer `A2 → B2 → B1 → C1` : est, nord, est; toutes les transitions sont horizontales ou verticales et aucune ne touche `X`.
5. Compter **3 déplacements** : `3 × 100 m = 300 m` sur ce plan. Il faut au moins deux mouvements vers l’est et un vers le nord; le trajet choisi est donc minimal.
6. Conclusion vérifiable : selon le **plan fictif**, la bibliothèque est accessible depuis l’école en **300 m de trajet sur quadrillage**; cela ne permet pas d’affirmer combien de minutes il faudrait en réalité.

### Exemple résolu 2 — Le nord et le trajet d’une station

**Plan fictif du quartier des Pins** (carte schématique *inventée*, non géographique).
Flèche N ↑ : le nord est vers le haut; l’est se trouve à droite (→). Colonnes A, B, C, D de gauche à droite; lignes 1 à 4 de haut en bas.
```text
   A  B  C  D
1  .  H  .  .
2  .  X  X  .
3  S  .  .  B
4  .  .  .  .
```
Légende : `S` = station; `H` = hôpital; `B` = bibliothèque; `X` = zone fermée; `.` = passage libre. Échelle du plan : **un déplacement entre deux cases voisines par un côté = 150 m**.
Règle de parcours : partir de la première case citée, passer uniquement entre cases voisines horizontalement ou verticalement; diagonales interdites; symbole de lieu traversable; case interdite non traversable. Les noms et distances ne décrivent aucun lieu réel.

1. Le titre annonce un quartier fictif; `S` signifie station en `A3` et `B` bibliothèque en `D3`.
2. De `A3` vers `D3`, on reste sur la ligne 3 et les colonnes vont de A à D : direction **est**.
3. Le trajet `A3 → B3 → C3 → D3` comporte **3 déplacements**, soit `3 × 150 = 450 m`.
4. La zone `X` interdit l’accès aux cases `B2` et `C2`; elle ne gêne pas ce trajet sur la ligne 3.
5. Contrôle : le symbole `B` dans cette carte veut dire bibliothèque seulement parce que la légende le dit.

### Contre-exemple 1 — La légende ignorée

**Réponse fautive :** « Sur la carte A, `X` est une école; allons par `C2`. » **Pourquoi c’est faux :** `X` y signifie bassin infranchissable, et `E` signifie école. **Correction :** relire la légende puis contourner `C2` par `B2 → B1 → C1`.

### Contre-exemple 2 — Échelle et cases confondues

**Réponse fautive :** « `A2 → B2 → B1 → C1` passe par quatre cases; donc 4 × 100 = 400 m. » **Pourquoi c’est faux :** quatre cases successives impliquent **trois** déplacements. **Correction :** compter les passages entre cases, donc **300 m**.

### Contre-exemple 3 — Nord supposé sans vérification

**Réponse fautive :** « Le nord est toujours en haut; inutile de regarder la flèche. » **Correction :** le nord en haut n’est établi, sur nos schémas, que parce qu’il est indiqué par `N ↑`. D’autres représentations peuvent être orientées autrement.

### Contre-exemple 4 — Raccourci interdit

**Réponse fautive :** « Pour aller de `A2` à `B1`, je traverse en diagonale : un seul déplacement. » **Correction :** aucune diagonale n’est autorisée; `A2 → A1 → B1` ou `A2 → B2 → B1` exige **deux** déplacements.

## Mini-méthode mémorisable

**T**itre → **L**égende → **N**ord → **R**epères (cases) → **P**arcours (cases permises) → **É**chelle → **J**ustification. On accepte une autre route correcte et aussi courte, si toutes ses étapes sont vérifiables.
