# 01 — Notions et exemples corrigés | `qc-pri-ma-029`

**Obj-1** : Déterminer un volume par comptage ou structuration d’unités cubiques. **Crit-1** : Évaluer le volume d’un assemblage de cubes en montrant le comptage.

## Définitions exactes

- **Espace occupé, ou volume** : mesure de l'étendue d'un corps selon trois dimensions. Un assemblage contient *n* cubes identiques sans chevauchement; son volume est `n cubes unités`. Si l'arête du cube fait 1 cm, le volume est `n cm³`, non `n cm²`.
- **Cube unité** : cube pris comme unité commune. Des cubes de tailles différentes ne peuvent pas être additionnés comme si chacun représentait une même unité. Un cube d'arête 2 cm contient `2 × 2 × 2 = 8 cm³`.
- **Couche** : groupe de cubes à une altitude commune. Une couche rectangulaire complète compte *colonnes × rangées* cubes. Plusieurs couches complètes identiques peuvent être comptées par *colonnes × rangées × nombre de couches*; une couche trouée se compte séparément.
- **Lecture des matrices** : `■` représente exactement un cube, `·` une place libre. Les rangées sont de l'avant vers l'arrière, les caractères de gauche à droite. Deux tableaux de même largeur peuvent représenter deux niveaux superposés. Il faut préciser **tous** les niveaux; une vue oblique d'une face n'atteste pas des cubes cachés.

## Exemple résolu 1 — Boîte pleine

**Données** : 3 colonnes, 2 rangées, 2 couches **entièrement pleines** de cubes d'arête 1 cm. Plan du niveau 1 : `[■■■ / ■■■]`; même plan au niveau 2. Chaque plan porte `3 + 3 = 6` cubes. Deux niveaux : `6 + 6 = 12` cubes, ou `3 × 2 × 2 = 12`. **Réponse** : **12 cubes unités = 12 cm³**. Le compte ne dépend pas de la visibilité des cubes inférieurs.

## Exemple résolu 2 — Petite marche irrégulière

**Données** : niveau 1 `[■■■ / ■■■]` (6 cubes), niveau 2 `[■■■ / ···]` (3 cubes), même taille de cubes d'arête 1 cm. **Calcul** : `6 + 3 = 9`. **Réponse** : **9 cm³**, les places vides du deuxième niveau n'étant pas des cubes. Un produit `3 × 2 × 2 = 12` compterait trois cubes absents.

## Contre-exemple 1 — Surface au lieu de volume

**Erreur** : une face de 3 × 2 carrés serait « 6 cm³ ». **Pourquoi c'est faux** : les 6 carrés décrivent une aire **6 cm²**, sans indiquer la profondeur. Pour obtenir le volume, préciser le nombre de niveaux : si 2 couches complètes, `6 × 2 = 12 cm³`.

## Contre-exemple 2 — Cubes trop grands

**Erreur** : « 3 cubes d'arête 2 cm = 3 cm³ », ou « 3 × 2 = 6 cm³ ». **Pourquoi c'est faux** : chaque cube vaut `2³ = 8 cm³`, donc les trois cubes non chevauchants valent `3 × 8 = 24 cm³`. La quantité *3 cubes de référence* et l'unité *cm³* ne sont pas équivalentes ici.

## Contrôle de représentation

Une photographie ne montrant que le dessus ne permet pas de savoir si la structure cache une deuxième couche, sauf si la consigne la déclare. Pour une réponse unique, utiliser un plan par niveau, préciser les dimensions d'une couche pleine ou montrer toutes les positions occupées. Une légende de cubes de 1 cm d'arête est essentielle avant d'écrire cm³.
