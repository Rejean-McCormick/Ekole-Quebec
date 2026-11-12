# 01 — Notions et exemples | qc-pri-ma-022

**Objectif immuable (`obj-1`) :** Reconnaître et décrire des solides grâce à leurs éléments constitutifs.  
**Preuve (`crit-1`) :** Associer une description à un solide et justifier à l’aide de ses propriétés.  
**Champ travaillé :** polyèdres convexes simples. Une surface courbe (boule, cylindre, cône) n'est pas une face polygonale dans les exercices de ce cours; la traiter séparément évite de compter des « arêtes courbes » comme les segments étudiés.

## Comprendre les mots

- **Solide :** objet géométrique qui occupe une région de l'espace. Sa représentation peut être une maquette, un dessin en perspective ou un patron.
- **Face d'un polyèdre :** région polygonale plane de sa surface, par exemple un carré du cube ou un triangle d'une pyramide. Ce n'est pas le « côté » d'un dessin plat.
- **Arête d'un polyèdre :** segment commun à deux faces, pas une diagonale dessinée dans une face. Chaque arête est comptée **une seule fois**, bien qu'elle borde deux faces.
- **Sommet :** point où se rencontrent au moins trois arêtes du polyèdre considéré. Un point placé au milieu d'une arête n'est pas un sommet du solide.
- **Patron :** assemblage plan de toutes les faces d'un polyèdre, reliées selon des arêtes, qui se replie **sans chevauchement ni trou** pour reconstituer la surface du solide. Avoir les bonnes faces est nécessaire, mais **ne suffit pas** : leur disposition doit permettre le pliage.

## Tableau de vérification des propriétés

| Solide (modèle de ce cours) | Faces F | Arêtes A | Sommets S | Composition des faces |
|---|---:|---:|---:|---|
| Cube | 6 | 12 | 8 | 6 carrés congruents |
| Pavé droit **non cubique** | 6 | 12 | 8 | 6 rectangles, dont au moins une face non carrée; faces opposées identiques |
| Prisme droit à base triangulaire | 5 | 9 | 6 | 2 triangles congruents et 3 rectangles |
| Pyramide à base carrée | 5 | 8 | 5 | 1 carré et 4 triangles |
| Tétraèdre (pyramide triangulaire) | 4 | 6 | 4 | 4 triangles (pas nécessairement équilatéraux) |

**Attention au vocabulaire :** un carré est aussi un rectangle au sens mathématique. On oppose ici « cube » à « pavé droit **non cubique** »; un cube est un cas particulier de pavé droit. Deux solides peuvent avoir les mêmes nombres F/A/S : **il faut parfois observer la forme et les dimensions des faces**. Les propriétés numériques ne suffisent jamais à distinguer cube et pavé droit non cubique.

## Deux exemples entièrement résolus

### Exemple 1 — Boîte à prisme triangulaire
Une maquette a deux faces triangulaires parallèles et trois faces rectangulaires reliant ces triangles. **Qui est-ce?**

1. Deux triangles congruents sont les bases d'un **prisme droit à base triangulaire**, et non d'une pyramide.
2. Compter les faces : 2 + 3 = **5**.
3. Chaque triangle a trois sommets, situés sur des bases distinctes : **6 sommets**.
4. Les deux contours triangulaires apportent 3 + 3 arêtes et les trois segments joignant les bases ajoutent 3 arêtes : **9 arêtes**.
5. Réponse justifiée : *prisme droit à base triangulaire, parce qu'il possède deux faces triangulaires opposées et trois faces rectangulaires; F=5, A=9, S=6.*

### Exemple 2 — Modèle de toit pyramidal
Une maquette porte un carré comme base; quatre triangles rejoignent un même point au-dessus de cette base.

1. Le carré est une **face de base**; les quatre triangles sont les faces latérales : **5 faces**.
2. Les quatre coins du carré et la pointe sont **5 sommets**.
3. Quatre segments du carré et quatre segments reliant ses coins à la pointe sont **8 arêtes**.
4. Réponse : *pyramide à base carrée*, justifiée par **une seule base carrée**, **quatre faces triangulaires**, F=5, A=8, S=5. Ce n'est pas un prisme triangulaire (également 5 faces, mais 9 arêtes et 6 sommets).

## Patrons : explications manipulables

**Patron valide du cube :** tracer **quatre carrés égaux alignés**; attacher un carré au-dessus et un autre au-dessous du **deuxième carré** de la bande. Les six carrés sont reliés par cinq segments communs; une fois pliés, chacun ferme une face différente. On peut vérifier avec six carrés cartonnés identiques (pliage d'une copie, sans colle nécessaire).

**Patron de la pyramide à base carrée :** tracer un carré; attacher **un triangle adapté à chaque côté**, orienté vers l'extérieur. Pour une pyramide régulière, les quatre triangles sont isocèles congruents, avec deux côtés égaux suffisamment longs pour rejoindre le sommet au pliage. Le carré central devient la base et les quatre triangles se rejoignent à la pointe.

**Patron du prisme droit triangulaire :** construire une bande de **trois rectangles** dont une dimension commune représente la longueur du prisme et dont les autres dimensions correspondent aux **trois côtés du triangle de base**; placer deux triangles congruents aux bords libres opposés, dans une disposition qui ferme chaque extrémité sans chevauchement. Utiliser un triangle équilatéral et trois rectangles congruents pour un premier essai.

## Contre-exemples corrigés

1. « Un solide qui a cinq faces est nécessairement une pyramide à base carrée. » **Faux** : le prisme droit triangulaire a lui aussi cinq faces. Il possède 9 arêtes et 6 sommets; la pyramide en a 8 et 5. Chercher les triangles opposés ou la base carrée.
2. « Dessiner six carrés en rectangle de 2 rangées et 3 colonnes donne un patron de cube. » **Faux** : ce rectangle plein crée une boucle de carrés 2 × 2; au pliage, les faces se superposent / ne peuvent occuper six orientations distinctes. Tester le pliage, pas seulement le nombre de carrés.
3. « La diagonale tracée sur une face du cube est une arête. » **Faux** : elle sépare artificiellement une face dessinée; les arêtes sont les segments entre deux faces du solide.
4. « Une pyramide à base carrée et un prisme triangulaire sont identiques parce qu'ils ont cinq faces. » **Faux** : leurs bases, formes de faces, arêtes et sommets diffèrent.

## Stratégie réutilisable

Décrire **(a)** les formes des faces et leurs relations (bases opposées? faces se rejoignant à une pointe?), **(b)** F, A, S en évitant les doubles comptes, **(c)** le nom précis, **(d)** deux propriétés justifiant le choix; **(e)** s'il existe une autre possibilité avec les mêmes nombres, chercher un critère discriminant. Pour un patron, tester *formes + adjacence + pliage*, pas uniquement F.

**Supports :** maquettes cartonnées ou blocs, schémas en texte à lire à voix haute, formes avec textures et arêtes en relief; les corrigés ne dépendent pas de la couleur ni de la vision d'une perspective.
