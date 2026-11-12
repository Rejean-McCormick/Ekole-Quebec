# 01 — Notions, représentations et exemples résolus

**Kristal :** `qc-pri-ma-001` · **Objectif :** `obj-1` · **Preuve :** `crit-1`

## La question à laquelle répond le dénombrement
« Combien y en a-t-il **en tout**? » Ici on compte des objets **séparés et reconnaissables**. Une même pièce compte une seule fois, qu'elle soit grande ou petite. La collection peut être sur une table, sur une feuille ou dans des cases.

**Correspondance terme à terme :** lorsque l'on compte, un objet reçoit un unique mot-nombre prononcé dans l'ordre habituel : un, deux, trois, etc.; aucun mot-nombre n'est attribué à deux pièces. Une façon de rendre cela visible est de déplacer chaque pièce de la zone « à compter » vers la zone « compté ». Quand on compare deux collections, on peut également apparier leurs pièces une à une.

**Cardinalité :** après avoir compté correctement tous les éléments, le **dernier** mot-nombre énoncé est le total. Les points `● ● ●` valent trois points, même si on commence par le point de droite plutôt que celui de gauche. Zéro décrit une collection vide : `∅` et aucun point visible = 0.

**Groupement :** partager une collection en paquets disjoints, de sorte que chaque objet soit dans un seul paquet. Le cardinal total est la somme des tailles de tous les paquets, reste compris. Des paquets de cinq peuvent aider, mais deux paquets inégaux sont tout aussi valides; pas de multiplication attendue.

**Représentations équivalentes :** une collection de six objets concrets ↔ `● ● ● | ● ● ●` ↔ `6`. Le séparateur `|` divise des groupes; **il n'est pas un objet**. La présence du symbole `●` sert seulement à figurer un élément. Ne pas compter les espaces, en-têtes ou traits de séparation.

## Exemple résolu 1 — 4 boutons

Matériel : `● ● ● ●` (chaque rond = un bouton distinct).

1. Je touche le premier bouton et je dis « un », puis les suivants « deux », « trois », « quatre »; je marque chacun pour ne pas le reprendre.
2. Le dernier mot est **quatre**; il y a **4 boutons en tout**. Ma représentation montre quatre ronds et ma notation est `4`.
3. **Contrôle autrement :** je sépare ces quatre boutons en deux paires `● ● | ● ●`. Chaque groupe en a 2, donc 2 + 2 = **4**, résultat identique. Aucun bouton ne reste seul.

## Exemple résolu 2 — 8 cubes mêlés

Matériel : `■ ■ ■ | ■ ■ ■ ■ ■`; les couleurs éventuelles ne changent pas les unités.

1. Je compte **un cube par mot-nombre** en faisant glisser un cube vers le bord de la table : 1, 2, 3, 4, 5, 6, 7, 8.
2. Je note `8` et je dessine huit carrés, pas sept ni neuf.
3. **Contrôle autrement :** je constate 3 cubes dans le premier groupe et 5 dans l'autre. 3 + 5 = **8**. Les deux groupes sont disjoints et couvrent tout le matériel.

## Contre-exemples corrigés

- **CE-1 — compter deux fois :** cinq objets `● ● ● ● ●`; un enfant désigne le troisième deux fois et dit 1, 2, 3, 4, 5, 6, puis « six ». **Non :** cinq objets distincts, donc cardinal **5**. Correction : marque ou déplace chaque objet juste après l'avoir compté; on obtient 1…5.
- **CE-2 — mauvais total :** on pointe correctement `● ● ● ● ●`, en disant 1…5, puis on déclare « quatre en tout ». **Non :** le dernier mot-nombre du comptage correct est **5**; le total est 5, pas 4. Correction : entourer toute la collection et redire « il y en a cinq en tout ».
- **CE-3 — groupes superposés :** six jetons, annoncés comme `4 + 3 = 7` parce qu'un jeton se trouve dans **les deux** groupes. **Non :** la somme ne permet un contrôle que si les groupes ne se chevauchent pas. Séparer en 4 et 2 donne **6**.
- **CE-4 — faux zéro :** un gobelet fermé contient trois billes mais la table est vide. Si la collection désignée est « billes **dans le gobelet** », la quantité n'est pas zéro. Définir précisément la collection avant de compter. Dans les tâches ci-dessous, tout le matériel à compter est toujours visible ou manipulable.

## Vérification conceptuelle rapide

1. On déplace les cinq pièces et on les compte à nouveau dans un autre ordre. **Le cardinal reste 5**, car on n'a ni ajouté ni retiré de pièce.
2. Un cercle contient 2 points, un autre 4, sans chevauchement. **6 points en tout** = 2 + 4; chaque point apparaît exactement une fois.
3. Le plateau est vide. **0 objet**. On n'invente pas un point pour pouvoir commencer à compter.

## Vocabulaire à stabiliser

- **Pièce / élément / unité :** ce qu'on compte, défini avant la tâche.
- **En tout / total / cardinal :** taille de toute la collection.
- **Groupe disjoint :** sous-ensemble de pièces qui n'apparaissent dans aucun autre groupe.
- **Contrôler autrement :** refaire une vérification réellement différente (nouvel ordre méthodique, groupement disjoint, ou appariement dans des cases), et pas simplement répéter le total annoncé.
