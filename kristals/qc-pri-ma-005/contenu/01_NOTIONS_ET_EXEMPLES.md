# MA-005 — Notions exactes, exemples et contre-exemples

## Définir et représenter
**Ordre de grandeur :** approximation dont l'échelle est plausible (dizaines, centaines, milliers); elle aide à détecter un résultat absurde, mais n'est pas un calcul exact. **Arrondi :** remplacer un entier non négatif par le multiple d'un rang annoncé (10, 100 ou 1000) le plus proche; quand on est exactement au milieu, dans ce parcours, on choisit le multiple supérieur. **Approximation :** une valeur proche de la valeur réelle, annoncée avec `≈`, en précisant la règle. **Vérification :** calculer l'exact, puis différence signée `estimation − exact` et écart absolu `|estimation − exact|`.

Sur une droite graduée, 346 est entre 300 et 400; il est à 46 de 300 et à 54 de 400, donc 346 ≈ 300 à la centaine. **Même rang, convention :** 350 ≈ 400; 349 ≈ 300. Pour 375 à la dizaine : 375 ≈ 380.

## Deux exemples résolus et commentés
**E1 — Une boîte de 374 étiquettes, rang des dizaines.** 374 ≈ 370 (chiffre des unités 4 < 5), valeur exacte 374; différence 370−374=−4, écart absolu 4 étiquettes, **sous-estimation** de 4. Le choix du rang doit être annoncé.

**E2 — Estimer le total de 248 et 163 crayons à la dizaine.** 248 ≈ 250, 163 ≈ 160; estimation du total ≈ 250+160 = 410 crayons. Calcul exact 248+163=411 crayons. Différence signée = 410−411=−1, écart absolu = 1 crayon. Cette stratégie est défendable; arrondir seulement le total exact à la dizaine conduirait aussi à 410, mais ce sont **deux opérations différentes** et on doit dire laquelle on utilise.

**E3 — Cas limite.** 275 arrondi à la dizaine = 280; 350 arrondi à la centaine = 400. Le cas « chiffre suivant = 5 » est réglé ici *vers le haut*, pour les entiers non négatifs.

## Deux contre-exemples expliqués
**CE1 :** « 374 ≈ 400 à la dizaine » : 400 n'est pas l'arrondi à la dizaine le plus proche; 370 l'est. 400 est l'arrondi à la *centaine*. Erreur : confusion des rangs.

**CE2 :** « 410 = 411 » après estimation de 248+163 : l'égalité est fausse. Écrire « estimation 410, somme exacte 411, écart 1 » et employer ≈ dans l'énoncé de l'approximation.

**CE3 :** « Écart = −1 crayon » : cela désigne une différence signée, **pas** l'écart absolu; écart absolu 1.

**Indicateurs de correction :** rang, stratégie, estimation, résultat exact, différence signée, écart absolu et sens de l'écart. Toute correction doit préserver l'unité.
