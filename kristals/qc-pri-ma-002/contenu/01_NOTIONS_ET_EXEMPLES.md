# 01 — Notions exactes, exemples résolus et contre-exemples

**`obj-1` / `crit-1`.** Champ opérationnel 0 à 9 999, incluant zéro, sauf configuration pédagogique plus étroite. Les textes sont originaux et les nombres des exemples vérifiables.

## 1. Numération en base dix

Un **nombre naturel** (ici 0, 1, 2, …) indique une quantité ou un rang. Les **chiffres** sont les dix signes 0 à 9. Dans notre système décimal positionnel, un chiffre vaut son chiffre multiplié par la valeur de sa position : unités (1), dizaines (10), centaines (100), milliers (1 000). **Dix unités = une dizaine, dix dizaines = une centaine, dix centaines = un millier.** Le 0 est un chiffre indispensable pour indiquer une position sans groupe correspondant.

**Matériel :** 1 cube-unité, barre de dix, plaque de cent et groupe de mille; **schéma :** tableau de positions; **notation :** `3 406 = 3 × 1 000 + 4 × 100 + 0 × 10 + 6 = 3 000 + 400 + 6`. Lire « trois mille quatre cent six ». Ne pas écrire « 3 046 » : ce serait 3 milliers, 0 centaines, 4 dizaines, 6 unités.

## 2. Ordre, symboles et comparaison

**Ordre croissant** : du plus petit au plus grand; décroissant : l'inverse. Sur une droite **graduée régulièrement et croissante vers la droite**, un nombre plus petit est placé à gauche. **`<`** signifie « est plus petit que », **`>`** « est plus grand que », **`=`** « est égal à »; le signe compare des nombres complets, et non les chiffres pris isolément.

**Algorithme exact :** (1) Supprimer tout espace séparateur (mais ne pas changer la valeur), lire le nombre de chiffres significatifs; celui qui comporte le plus de chiffres est plus grand pour des naturels positifs. (2) Si longueur égale, examiner de gauche à droite les chiffres de rang milliers → unités; au **premier rang qui diffère**, le plus grand chiffre donne le plus grand nombre. (3) Si tous les chiffres sont identiques, les nombres sont égaux. Cas particulier : `0` est inférieur à tout naturel positif.

## Exemple résolu E1 — Première différence

**Comparer `3 406` et `3 460`.** Les milliers (3/3) et les centaines (4/4) sont identiques; les dizaines diffèrent **0 < 6**. Ainsi **`3 406 < 3 460`**. Écriture développée : 3 406 = 3 000 + 400 + 6 ; 3 460 = 3 000 + 400 + 60. La différence apparaît avant les unités (6/0) : ne pas commencer par la droite.

## Exemple résolu E2 — Droite numérique

**Sur une droite de 1 200 à 1 300 graduée de 10 en 10, placer 1 240 et 1 270.** Partant de 1 200, avancer 4 graduations pour 1 240, puis 7 pour 1 270; 1 240 est à gauche de 1 270, donc **`1 240 < 1 270`**. Les positions restent exactes si les graduations sont régulièrement espacées, quelle que soit leur longueur physique.

## Exemple résolu E3 — Zéro et égalité

`5 007` signifie 5 milliers et 7 unités, pas 5 milliers et 70 unités. `720 = 720` est une égalité; tout classement doit accepter une répétition de la même valeur. Une écriture `0720` vaut aussi numériquement 720, mais **on privilégie l'écriture canonique sans zéro inutile au début**.

## Contre-exemple C1 — Chiffre dominant hors position

**Faux :** « `925 > 1 003` parce que 9 > 1. » **Correction :** 925 est un nombre à trois chiffres, 1 003 à quatre; **`925 < 1 003`**. Ce n'est pas le premier chiffre considéré sans le nombre de positions qui décide.

## Contre-exemple C2 — Comparer à partir des unités

**Faux :** « `3 406 > 3 460` parce que 6 unités > 0 unité. » **Correction :** la première différence est au rang des dizaines, 0 contre 6, donc **`3 406 < 3 460`**. La différence des unités est sans effet sur l'ordre dès qu'une position supérieure diffère.

## Contre-exemple C3 — Graduations déformées

Placer 1 250 au milieu de 1 200 et 1 300 sur une droite à intervalles **inégaux** ne justifie pas la précision du placement. Corriger en reconstruisant onze repères 1 200, 1 210, …, 1 300 régulièrement espacés.

**Autovérification :** écrire la décomposition, comparer le premier rang différent, prononcer « est plus petit/grand/égal », vérifier le signe et la place sur l'axe. Le matériel, la droite et la notation doivent raconter la même relation.
