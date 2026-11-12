# 06 — Remédiation, transfert et rappel différé | `qc-pri-ma-021`

## Tableau de remédiation ciblée

| Indice d'erreur | Diagnostic immédiat | Intervention courte et nouvel essai vérifiable |
|---|---|---|
| `(x ; y)` inversés | Demander de placer `(2 ; 5)` puis `(5 ; 2)` | Mettre des étiquettes « colonne x » et « rangée y »; nouveau point `(4 ; 1)` = colonne 4, rangée 1, puis retirer les étiquettes. |
| Est/ouest ou nord/sud inversés | `O1` depuis `(4 ; 3)` mal évalué | Fixer `N↑`; calculer `O1=(3 ; 3)` puis demander `S1` depuis `(3 ; 3)` = `(3 ; 2)` sans soutien. |
| Fin correcte mais points sautés | `E3` depuis `(1 ; 1)` noté comme saut direct | Inscrire `(2 ; 1),(3 ; 1),(4 ; 1)`; nouvel essai `(2 ; 2), N2` = `(2 ; 2),(2 ; 3),(2 ; 4)`. |
| Sortie de la grille | Depuis `(6 ; 3)`, `E1,O1` accepté | Arrêter au premier pas illégal `(7 ; 3)`; nouveau problème `(1 ; 4), O1` interdit; trouver `E1` = `(2 ; 4)` légal. |
| Étape/obstacle ignoré | Un trajet passe par le mauvais endroit | Placer un repère « escale », rayer les points interdits, reprendre en contrôlant chaque nœud; nouvel essai plus court avant toute nouvelle preuve. |
| « gauche » pris pour « ouest » | Changer l'orientation d'un pion | Énoncer les flèches cardinales fixes, relire `E/O/N/S` et réessayer sans orientation corporelle implicite. |

Toute intervention fait perdre le caractère autonome à la tentative corrigée; enregistrer une **nouvelle** tentative sur une variante distincte avant de conclure.

## Transfert 1 — bibliothèque, signalisation lisible par autrui

Départ `(1 ; 2)`, passage requis `(4 ; 2)`, rayon final `(4 ; 4)`. Décrire oralement ou par écrit `E3, N2` et l'exécuter sur un plan de lieux. La route minimale a cinq pas; trace `(1 ; 2),(2 ; 2),(3 ; 2),(4 ; 2),(4 ; 3),(4 ; 4)`. Le critère n'est pas de connaître une vraie bibliothèque, mais de communiquer une suite exacte de points dans une grille stable.

## Transfert 2 — robot fictif en jardin quadrillé

Départ `(2 ; 5)`, destination `(5 ; 5)`. Points interdits `(3 ; 5),(4 ; 5),(3 ; 4),(4 ; 4),(3 ; 6),(4 ; 6)` : le robot ne peut ni entrer ni passer sur ces points. `S2, E3, N2` donne `(2 ; 5),(2 ; 4),(2 ; 3),(3 ; 3),(4 ; 3),(5 ; 3),(5 ; 4),(5 ; 5)` et respecte les limites et obstacles. Le trajet minimum a 7 pas car les colonnes 3 et 4 aux hauteurs 4, 5 et 6 bloquent la traversée directe, imposant d'atteindre au plus la rangée 3 avant de passer à l'est. Exécution sur **schéma ou plateau**, jamais sur un robot physique non contrôlé.

## Rappel différé (post-décision, jamais une seule note)

- **J+2 :** grille neutre 6 × 6, nord en haut; depuis `(3 ; 2)`, suivre `N2, O1`. Trace `(3 ; 2),(3 ; 3),(3 ; 4),(2 ; 4)`. Noter sans indice la présence des étapes, le bon axe et la convention.
- **J+7 :** nouveau repérage : depuis `(5 ; 4)`, passer par `(2 ; 4)`, puis atteindre `(2 ; 2)` en 5 pas. Solution `O3, S2`; trace `(5 ; 4),(4 ; 4),(3 ; 4),(2 ; 4),(2 ; 3),(2 ; 2)`.
- Si l'acquis ne se maintient pas : identifier la composante manquante (repère, séquence, contrainte), reprendre la remédiation ciblée et chercher deux nouvelles preuves en contextes distincts, plutôt qu'une répétition de la même fiche.

**Accessibilité/sécurité :** livrets à police adaptable, contrastes et descriptions en mots des points; pion tactile, dictée à un scribe neutre ou commandes orales; pas d'obligation de marcher, d'utiliser un appareil ou de distinguer les couleurs. Les obstacles sont fictifs. La modalité peut changer, pas le sens mathématique ni la condition d'autonomie.
