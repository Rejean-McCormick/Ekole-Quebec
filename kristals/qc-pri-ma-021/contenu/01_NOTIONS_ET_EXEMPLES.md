# 01 — Notions et exemples | `qc-pri-ma-021`

## Matériel et convention (à annoncer avant tout exercice)

Tracer 6 colonnes de **points** numérotées `x=1,2,3,4,5,6` de gauche à droite et 6 rangées de points `y=1,2,3,4,5,6` de bas en haut. Le nord (`N`) est vers le haut, l'est (`E`) à droite, le sud (`S`) vers le bas et l'ouest (`O`) à gauche. Le point `(1 ; 1)` est au coin inférieur gauche. On note **(colonne x ; rangée y)**, jamais l'inverse. Un pas relie deux points voisins horizontalement ou verticalement : aucun déplacement diagonal ni hors du carré `1…6`.

Une légende textuelle sans image est suffisante : `N: y+1`, `S: y-1`, `E: x+1`, `O: x-1`. Le regard de l'exécutant n'inverse pas ces règles. Cette convention est un **choix pédagogique interne**, non une prescription officielle.

| Concept | Définition vérifiable | Test rapide |
|---|---|---|
| Orientation | Sens cardinal de l'espace, fixé ici par une flèche nord et les axes. | De `(3 ; 3)`, `O1` donne `(2 ; 3)` quelle que soit la posture du pion. |
| Coordonnées simples | Paire ordonnée entière `(x ; y)` indiquant un **point**, d'abord colonne puis rangée. | `(2 ; 5)` est distinct de `(5 ; 2)`. |
| Déplacement | Translation d'un point à son voisin; `E3` désigne trois `E1` consécutifs, non un bond. | `E2, N1` depuis `(2 ; 2)` finit à `(4 ; 3)` et visite 3 nouveaux points. |
| Parcours | Suite ordonnée de positions définie par un départ, un repère et des commandes. | Si deux personnes ont les mêmes données, elles doivent visiter les mêmes points dans le même ordre. |

**Table des commandes** : `E1: (x,y)→(x+1,y)` ; `O1: (x,y)→(x-1,y)` ; `N1: (x,y)→(x,y+1)` ; `S1: (x,y)→(x,y-1)`. Une commande est interdite si l'étape intermédiaire sort de la grille ou rencontre un point fermé.

## Exemple résolu A — plan de la bibliothèque

**Question :** Un pion est à `(2 ; 2)`. Décris et suis `E2, N1`.

1. Je fixe nord vers le haut; `E` fait avancer la colonne. Départ `(2 ; 2)`.
2. `E1` : `(3 ; 2)`; encore `E1` : `(4 ; 2)`.
3. `N1` : `(4 ; 3)`. J'ai gardé x=4 et augmenté y de 1.
4. **Réponse communicable** : `départ (2 ; 2), nord en haut, E2 puis N1, arrivée (4 ; 3)`. **Trace** : `(2 ; 2) → (3 ; 2) → (4 ; 2) → (4 ; 3)`.
5. **Vérification indépendante de l'arrivée** : x=`2+2=4`, y=`2+1=3`; toutes les coordonnées sont dans 1…6.

## Exemple résolu B — trouver puis exécuter un itinéraire avec arrêt

**Question :** Sur la même grille, partir de `(5 ; 5)`, passer **d'abord** par `(3 ; 5)`, puis arriver à `(3 ; 2)` en un minimum de pas.

1. Entre `(5 ; 5)` et `(3 ; 5)`, y ne change pas : `O2` (visite `(4 ; 5)`, `(3 ; 5)`).
2. De `(3 ; 5)` à `(3 ; 2)`, x ne change pas : `S3` (visite `(3 ; 4)`, `(3 ; 3)`, `(3 ; 2)`).
3. **Instructions** : `départ (5 ; 5), nord en haut, O2 puis S3`. **Trace complète** : `(5 ; 5) → (4 ; 5) → (3 ; 5) → (3 ; 4) → (3 ; 3) → (3 ; 2)`.
4. **Justification de minimalité** : 2 changements de colonne et 3 changements de rangée exigent au moins 5 pas; le trajet en fait exactement 5, sans sortir des limites. L'ordre respecte l'arrêt demandé.

## Contre-exemples (diagnostiquer, corriger, vérifier)

- **C1 — coordonnées permutées :** annoncer `(5 ; 2)` alors que le point marqué est en colonne 2, rangée 5. Cela localise **un autre point**. Correction : `(2 ; 5)`; dire « colonne, puis rangée ».
- **C2 — arrivée égale, parcours différent :** depuis `(2 ; 2)`, `E2, N1` visite `(3 ; 2),(4 ; 2),(4 ; 3)` tandis que `N1, E2` visite `(2 ; 3),(3 ; 3),(4 ; 3)`. Même arrivée `(4 ; 3)`, **pas le même parcours**. Si un passage obligatoire est `(4 ; 2)`, seul le premier le respecte.
- **C3 — sortie dissimulée :** depuis `(6 ; 3)`, `E1, O1` semble revenir au départ, mais le premier pas donne `(7 ; 3)` hors grille. La route entière est **invalide**, même si le bilan des déplacements vaut zéro.
- **C4 — « gauche » sans repère :** « avance à gauche » dépend de l'orientation de la personne. Remplacer par « `O1` dans la grille dont le nord est en haut ».

**Autocontrôle** : le destinataire connaît-il le départ ? sait-il où se trouve le nord ? la notation `(x ; y)` est-elle définie ? chaque pas et chaque point intermédiaire sont-ils légaux ? les étapes doivent-elles être exécutées dans cet ordre ?
