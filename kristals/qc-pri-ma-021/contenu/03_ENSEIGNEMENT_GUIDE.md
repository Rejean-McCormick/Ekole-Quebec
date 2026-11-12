# 03 — Enseignement guidé | `qc-pri-ma-021`

**Objectif communiqué :** « Tu pourras décrire un trajet ou une position avec un repère stable, puis donner des instructions qu'une autre personne peut suivre sans hésitation. »

## Séquence de modelage « je montre, nous décrivons, tu expliques »

1. **Installer les repères (matériel).** Sur une grille 6 × 6 de **points** (pas de cases), placer une flèche `N↑`. Étiqueter 1 à 6 les colonnes de gauche à droite et les rangées de bas en haut. Déposer un pion sur `(2 ; 2)` en disant « colonne 2, rangée 2 ». Demander : « Où se trouve `(2 ; 5)` ? » Attendu : même colonne, trois rangées plus au nord.
2. **Montrer une route pas à pas (matériel).** Depuis `(2 ; 2)`, avancer `E1` jusqu'à `(3 ; 2)`, encore `E1` jusqu'à `(4 ; 2)`, puis `N1` jusqu'à `(4 ; 3)`. À chaque mouvement : dire quelle coordonnée change, en quoi elle change et pourquoi le point reste dans la grille.
3. **Transcrire (schéma).** Relier ou énumérer `(2 ; 2) → (3 ; 2) → (4 ; 2) → (4 ; 3)`. Pour l'accessibilité, lire la liste plutôt que demander exclusivement de voir le dessin.
4. **Coder (notation).** Écrire `départ (2 ; 2); N↑; E2, N1; arrivée (4 ; 3)`. Préciser que `E2` compte deux déplacements **distincts**. Vérifier avec le bilan `x+2`, `y+1` et avec les points effectivement visités.
5. **Contraster (réflexion).** Repartir de `(2 ; 2)` et faire `N1, E2`. La nouvelle trace `(2 ; 2),(2 ; 3),(3 ; 3),(4 ; 3)` montre une route différente. Demander : « Comment détecter une erreur si le bon point d'arrivée est atteint par la mauvaise route ? » Attendu : comparer toutes les positions successives.
6. **Faire reformuler.** Élève raconte une route complète avec départ, flèche nord, commande et trace; retirer les étiquettes d'axes après vérification qu'elles sont comprises.

## Second modèle — route au plus court avec escale

Problème : de `(1 ; 4)` à `(4 ; 2)` en passant **avant l'arrivée** par `(4 ; 4)` et sans sortir du carré. `E3, S2`, trace `(1 ; 4),(2 ; 4),(3 ; 4),(4 ; 4),(4 ; 3),(4 ; 2)`; longueur 5, exactement `|4-1|+|2-4| = 5`, aucune diagonale. On peut prouver la minimalité car les changements de colonne et rangée exigent au moins 5 pas; l'escale est respectée.

## Contrôle de compréhension avant la pratique

- Si je fais `O1` depuis `(4 ; 2)`, où suis-je ? **`(3 ; 2)`** (x diminue).
- À partir de `(6 ; 3)`, puis-je faire `E1` ? **Non** : `(7 ; 3)` est hors des 6 colonnes.
- « Arrive à `(4 ; 3)` » décrit-il les points intermédiaires ? **Non** : cela précise uniquement la destination.
- Si la personne se retourne, `N1` change-t-il de sens ? **Non** : la flèche nord de la grille demeure l'unique référence.

**Passage à la suite :** si une réponse est fausse, refaire un seul déplacement sur le matériel, faire nommer l'axe puis reprendre le même raisonnement sur un nouveau départ, sans donner la route entière.
