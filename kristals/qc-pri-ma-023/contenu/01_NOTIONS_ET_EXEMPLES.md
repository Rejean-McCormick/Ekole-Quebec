# 01 — Notions et exemples exacts

**Objectif `obj-1` :** Classer des figures planes à partir de propriétés observables. **Critère `crit-1` :** Trier de nouvelles figures et expliquer un cas de non-appartenance.

## Vocabulaire opératoire (sur les contours)

1. **Figure plane** : forme géométrique contenue dans un plan, qu'elle ait un contour droit (un polygone) ou courbe (un cercle). Les figures utilisées ici sont des contours fermés simples. On n'affirme pas que toute figure plane est un polygone.
2. **Polygone simple non dégénéré** : contour fermé obtenu avec *au moins trois segments rectilignes* reliés bout à bout, sans croisement entre côtés non consécutifs et sans trois sommets consécutifs alignés. Les exemples utilisent l'ordre des sommets écrit. On relie le dernier au premier.
3. **Côté** : chacun des segments rectilignes du contour d'un polygone, entre deux sommets consécutifs. Une partie de cercle, même courbe et fermée, n'est pas un « côté » polygonal.
4. **Sommet** : point de rencontre de deux côtés consécutifs d'un polygone. Une figure à n côtés dans notre corpus a n sommets. Un cercle n'a ni côté polygonal ni sommet.
5. **Parallèles** : deux droites distinctes du plan qui ne se rencontrent pas, même prolongées. Deux côtés sont parallèles si leurs droites supports le sont. Dans un quadrilatère ABCD, les **seules paires opposées candidates** sont (AB,CD) et (BC,DA); elles peuvent être 0, 1 ou 2 à être parallèles. Être « éloignés », de même longueur ou inclinés ne suffit pas.

**Lecture d'une représentation :** A(0,0)→B(4,0)→C(4,2)→D(0,2)→A donne quatre segments (AB,BC,CD,DA). Sur quadrillage : lire les coordonnées comme *pas horizontaux/verticaux*, tracer proprement et nommer les sommets; par manipulation : quatre bandes aux extrémités articulées. Un segment horizontal est parallèle à un autre horizontal de ligne différente. Pour les côtés obliques, on peut comparer leurs déplacements exacts (vecteurs) sans utiliser l'impression visuelle.

**Vérification exacte réservée à la correction :** pour deux côtés de vecteurs non nuls u=(ux,uy), v=(vx,vy), les supports sont parallèles exactement si `ux*vy - uy*vx = 0`; on ne demande pas aux enfants de mémoriser cette formule. Ce test traite sans erreur les côtés verticaux et obliques.

## Exemple résolu A — tri par côtés

T : A(0,0), B(4,0), C(1,3) → A. Ses côtés sont AB, BC, CA : **3**; ses sommets A, B, C : **3**.  
R : A(0,0), B(4,0), C(4,2), D(0,2) → A. **4 côtés, 4 sommets.**  
C : cercle de centre O(0,0), rayon 2. **0 côté polygonal, 0 sommet** (mais bien une figure plane).

**Consigne :** « Range selon *a quatre côtés polygonaux*. » **Réponse :** R appartient au groupe; T et C n'y appartiennent pas. **Justification de non-appartenance :** « T a trois côtés, pas quatre. » On ne déduit pas le classement de l'apparence ou de la couleur.

## Exemple résolu B — tri par paires de côtés parallèles

R : A(0,0), B(4,0), C(4,2), D(0,2). AB // CD (horizontaux), BC // DA (verticaux) : **2 paires**.  
Q : A(0,0), B(5,0), C(4,2), D(1,2). AB // CD (horizontaux), BC non // DA (déplacements (-1,2) et (-1,-2) non proportionnels) : **exactement 1 paire**.  
I : A(0,0), B(4,0), C(3,3), D(0,2). Ni AB // CD ni BC // DA : **0 paire**.

**Consigne :** « Groupe 2 : quadrilatères avec *exactement deux paires* de côtés opposés parallèles. » **Réponse :** R seul. **Pourquoi Q est exclu :** Q n'a qu'une paire (AB // CD). Pour le vérifier, tracer les droites supports de BC et DA ou comparer les directions.

## Trois contre-exemples commentés

- **« Le cercle a un côté courbe. » Faux dans ce lexique.** Son contour est courbe : aucun *segment* ne forme un côté polygonal. Il reste une figure plane.
- **« Q est un parallélogramme, car ses deux côtés horizontaux sont parallèles. » Faux.** Un quadrilatère ayant 2 paires parallèles doit aussi avoir BC // DA; Q n'a qu'une paire.
- **« R tourné n'a plus deux paires parallèles. » Faux.** Par quart de tour, les horizontales deviennent verticales et inversement; les deux parallélismes demeurent. La position sur la page n'est pas une propriété de classement.

## À ne pas supposer

La figure dessinée sans coordonnées peut paraître faussement symétrique. Pour la correction on utilise l'ordre des sommets et les coordonnées, jamais une estimation visuelle. « Une paire » est ambigu : les tâches disent **exactement une paire** ou **au moins une paire**. Aucun nom de trapèze n'est nécessaire car sa définition peut varier selon les conventions.
