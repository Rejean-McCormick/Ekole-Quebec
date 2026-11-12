# 05 — Pratique autonome | `qc-pri-ma-021`

**Pour l'élève :** sur une grille 6 × 6 de points, nord en haut (`N↑`), les coordonnées sont `(colonne ; rangée)`, les mouvements `E, O, N, S` se font d'un point au voisin. Tu peux écrire, dire ou matérialiser chaque route; **aucune aide sur la stratégie**. Noter le départ, les commandes, la trace de tous les points, l'arrivée et une phrase de vérification. Les solutions qui suivent servent au correcteur (à cacher pendant la passation).

## `independent-1a` — Localiser puis suivre

**Énoncé :** Marque A=`(2 ; 4)`. Depuis A, suis `S2, E3` sans franchir les limites. Donne l'arrivée et tous les points visités.  
**Réponse :** `(2 ; 4),(2 ; 3),(2 ; 2),(3 ; 2),(4 ; 2),(5 ; 2)`; arrivée `(5 ; 2)`. Vérifier : x `2+3=5`, y `4-2=2`.

## `independent-1b` — Produire une route courte

**Énoncé :** Départ `(5 ; 1)`, arrêt obligé `(2 ; 1)`, arrivée `(2 ; 4)`. Donne et exécute une route de **6 pas exactement**, sans diagonale.  
**Réponse :** `O3, N3`; trace `(5 ; 1),(4 ; 1),(3 ; 1),(2 ; 1),(2 ; 2),(2 ; 3),(2 ; 4)`; 6 pas. **Critères :** convention annoncée, arrêt atteint en premier, aucun pas omis, trace et arrivée correctes.

## `independent-1c` — Détecter une route impossible

**Énoncé :** Le point de départ est `(6 ; 2)`. Une fiche propose `E1, O1, N1`. La fiche est-elle utilisable ? Indique le premier problème, puis propose un trajet légal **de 2 pas** vers `(5 ; 3)` et suis-le.  
**Réponse :** la fiche est inutilisable : `E1` tente `(7 ; 2)` hors grille. Une route légale de 2 pas est `O1, N1` : trace `(6 ; 2),(5 ; 2),(5 ; 3)`, arrivée `(5 ; 3)`; l'autre ordre `N1, O1` donne une trace également valide et la même arrivée, mais une trace **différente**.  
**Critères :** repérer le premier pas interdit, proposer deux commandes ordonnées, respecter la grille et donner la trace complète; accepter les deux routes légales si exécutées conformément à l'énoncé.  

## `independent-1d` — Critiquer deux routes

**Énoncé :** Depuis `(2 ; 2)`, route R=`E2, N1`, route T=`N1, E2`. Décris chaque trace. Sont-elles identiques ? Si un guichet est au point `(4 ; 2)`, laquelle passe au guichet ?  
**Réponse :** R : `(2 ; 2),(3 ; 2),(4 ; 2),(4 ; 3)`; T : `(2 ; 2),(2 ; 3),(3 ; 3),(4 ; 3)`; traces différentes, même arrivée, seule R passe par `(4 ; 2)`.

## Deux preuves de maîtrise (épreuves indépendantes, sans indices)

**A — plan de bibliothèque (`q-010`).** Départ `(1 ; 2)`, comptoir obligatoire `(4 ; 2)`, rayon destination `(4 ; 4)`. « Donne un itinéraire en 5 pas exactement puis suis-le, en montrant chaque point, pour qu'une autre personne puisse refaire ton trajet. » **Corrigé minimal :** `E3, N2`; trace `(1 ; 2),(2 ; 2),(3 ; 2),(4 ; 2),(4 ; 3),(4 ; 4)`.

**B — robot de jardin (`q-011`).** Départ `(2 ; 5)`, arrivée `(5 ; 5)`. Les points `(3 ; 5),(4 ; 5),(3 ; 4),(4 ; 4),(3 ; 6),(4 ; 6)` sont bloqués. « Donne une route de 7 pas exactement puis suis-la sans toucher les points bloqués; documente chaque point. » **Corrigé minimal :** `S2, E3, N2`; trace `(2 ; 5),(2 ; 4),(2 ; 3),(3 ; 3),(4 ; 3),(5 ; 3),(5 ; 4),(5 ; 5)`.

**Grille pour chaque preuve :** 1) repère/départ/ordre explicites; 2) chaque point légal et contraintes respectées; 3) arrivée et trace complètes; 4) communication reproductible; 5) exécution autonome, avec justification d'au moins un choix. Voir `evaluation/GRILLE_MAITRISE.md` pour décider avec les **deux** contextes; le seul point final ne constitue pas une réussite.
