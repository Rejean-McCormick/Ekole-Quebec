# Plan d'évaluation — `qc-pri-ma-021` v1.2

**But unique (`obj-1`) :** Décrire un trajet ou une position au moyen de repères spatiaux stables.  
**Preuve cible (`crit-1`) :** Donner puis suivre un parcours spatial précis sans ambiguïté.  
**Famille et mode natifs :** `qc-pri-ma-021-ev-01`, `paramétrique_controle`; tous les items ont explicitement `objectif_id=obj-1`, `critere_id=crit-1` et `family_id=qc-pri-ma-021-ev-01`. **Status** : `a_revoir`, non certifiés. Les items formatifs peuvent mesurer une composante; seuls `q-010` et `q-011`, combinés, fournissent les deux manifestations complètes recherchées.

## Table d'épreuve / matrice de couverture

| Item | Difficulté | Mode | Représentation | Observable principal | Usage |
|---|---|---|---|---|---|
| q-001 | initial | fixe | coordonnées sur repère verbal/papier | colonne puis rangée | formatif |
| q-002 | initial | fixe | orientation/points tracés | direction cardinale constante | formatif |
| q-003 | initial | parametrique | pion + liste de commandes | trace de 2 segments successifs | formatif |
| q-004 | intermediaire | parametrique | grille + instructions | trace d'un parcours à plusieurs virages | formatif |
| q-005 | intermediaire | fixe | deux listes de points | distinguer arrivée et parcours | formatif |
| q-006 | intermediaire | parametrique | contrôle de limites | identifier route légale/illégale et premier pas en cause | formatif |
| q-007 | intermediaire | fixe | itinéraire via point imposé | construire le chemin minimum | formatif |
| q-008 | transfert | scenario_controle | critique de consigne | lever une ambiguïté de repère | formatif |
| q-009 | transfert | parametrique | point de passage + trace | donner et suivre route minimale déterministe | formatif préparatoire |
| **q-010** | transfert | scenario_controle | plan de bibliothèque | **preuve A complète :** itinéraire communiqué puis suivi via comptoir | **décision A** |
| **q-011** | transfert | scenario_controle | robot de jardin sur grille | **preuve B complète :** trajet sans obstacles communiqué puis suivi | **décision B** |

**Poids de décision** : aucune pondération de « score global » ne remplace la conjonction des deux preuves A et B. Les items 001–009 diagnostiquent et renseignent des feedbacks; ils ne compensent jamais une preuve autonome insuffisante.

## Repère invariant et correcteur

Le correcteur et toutes les consignes utilisent la grille de points `1 ≤ x,y ≤ 6`, `N` vers y croissant, `E` vers x croissant, `O` vers x décroissant et `S` vers y décroissant. Paires `(x ; y)` avec colonne en premier. Les commandes de longueur n sont **décomposées en n pas unitaires**; les points visités sont testés chacun. Une route avec un point interdit ou un passage hors grille est invalide même si le point final calculé par bilan des axes semble acceptable.

**Générateur strict des q-003, q-004, q-006, q-009 (mode `parametrique`) :**

1. `parametres.cas` est une liste ordonnée de **4 variantes fermées et pré-calculées** par item; aucune phrase ni coordonnée librement inventée au moment de la présentation.
2. Le `seed` entier est constant par item; sélection `index = seed % 4`, index commençant à 0. Enregistrer `seed` et `index` dans la trace d'administration; ne sélectionner que les 4 variantes autorisées.
3. Variables : entiers x, y dans `[1,6]`, direction parmi `{N,S,E,O}`, longueur de segment dans `[1,3]`. Pour q-006, une instruction illégale peut essayer **une seule étape** en dehors de `[1,6]` et doit être détectée; toutes les autres étapes sont vérifiées normalement. q-009 ajoute un point de passage obligatoire dans `[1,6]^2`.
4. Algorithme de résolution (pas un générateur IA) : poser `p=(x0,y0)`; pour chaque segment de direction D et longueur n, appliquer **n fois** le vecteur cardinal unitaire; ajouter les positions intermédiaires dans `trace_attendue`, marquer le premier point hors limites ou bloqué; si aucun, `arrivee_attendue` est la dernière position. **Ne pas** réintégrer un point hors limite dans un trajet admissible.
5. Pour q-009, construire explicitement les segments le long de la rangée/colonne vers l'étape obligatoire, puis ceux de l'étape obligatoire vers l'arrivée; la longueur minimale est la somme des différences absolues de coordonnées sur chaque tronçon. Chaque variante contient sa liste de points.
6. **Vérification supplémentaire :** comparer le dernier point au bilan entier indépendant `(x0 + #E − #O ; y0 + #N − #S)` et la longueur de la trace au nombre d'étapes +1; pour q-009 contrôler en plus la longueur de chaque tronçon et le passage par l'étape. Contrôler les 4 variantes et le cas sélectionné, pas seulement la réponse affichée.

Les tableaux complets (variables, bornes, contraintes, seed, cas, traces, limites de variation, réponses) sont inscrits dans chaque item paramétrique de `BANQUE_ITEMS.json`. Les réponses littérales des items correspondent au cas sélectionné par le seed, et un moteur peut prendre une autre variante **uniquement** depuis `parametres.cas` en présentant le stimulus/réponse associés. Toute modification de table ou de sémantique requiert de nouveaux tests et une revue humaine.

## Conditions de passation, accessibilité, sécurité

- Énoncer explicitement le nord et le sens des axes; fournir grille vierge ou description textuelle à tous. Jamais de dessin dont les axes doivent être devinés.
- Réponse orale, écrite, braille, déplacement de pion ou dictée à un scribe neutre admis; le scribe n'élabore ni ne vérifie la route. Pas d'exigence de marche ni de navigation en espace réel.
- Ne pas montrer le corrigé ni fournir de conseils stratégiques durant les preuves A et B; enregistrer le niveau d'aide et ne **pas** créditer comme autonome si une correction intervient.
- Pour A : départ `(1 ; 2)`, guichet `(4 ; 2)` avant arrivée `(4 ; 4)`; route de **5 pas** demandée, chaque point reporté. Pour B : départ `(2 ; 5)`, destination `(5 ; 5)`, blocages `(3 ; 5),(4 ; 5),(3 ; 4),(4 ; 4),(3 ; 6),(4 ; 6)` et **7 pas**. Les décors sont fictifs, sans dépendance à un lieu réel, à la couleur, au vécu de l'enfant ou à un produit commercial.
- Pour les items évaluatifs A et B, ces points, limites et barèmes restent **verrouillés**; seuls forme d'affichage et moyens d'expression équivalents sont adaptables. Refaire une nouvelle épreuve validée, et non répéter un item corrigé, après remédiation.

## Administration et décisions

Ordre : diagnostic → 001–009 selon les besoins → A et B à deux occasions/contextes distincts → retour descriptif → remédiation ciblée si nécessaire → rappel J+2 puis J+7. Documenter, hors canon, la date, le support, le parcours émis, la trace suivie, les erreurs de direction, les interventions et la justification de l'élève. Maîtrise **uniquement** si A et B atteignent chacun tous les critères essentiels au niveau autonome de `GRILLE_MAITRISE.md` (y compris justification suffisante). Ne pas inférer l'acquis d'une note unique, d'une arrivée correcte isolée, de l'âge ou d'un résultat accidentel.

**Points à faire examiner humainement :** calibrage des distances au primaire, stabilité de la compréhension de « point » vs « case », lisibilité des textes alternatifs, pertinence de la contrainte de minimum, équité de supports tactiles/assistés, accord de cotation inter-évaluateurs et essais en situation réelle. Aucun alignement officiel PFEQ n'est revendiqué.
