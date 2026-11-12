# 01 — Notions, exemples résolus et contre-exemples

## Cible et conventions vérifiables

`obj-1` : Identifier et construire des angles, des droites et des symétries simples. `crit-1` : Compléter une figure symétrique puis justifier la transformation. Utiliser un **quadrillage carré d'unité 1**, axes parallèles aux bords, origine et sens des coordonnées explicités : l'abscisse `x` est l'horizontale croissante vers la droite et l'ordonnée `y` est la verticale croissante vers le haut. Tous les points de la banque sont dans le carré `0≤x≤12`, `0≤y≤12`; les axes de réflexion ne sont **pas** forcément les axes de coordonnées `x=0` et `y=0`.

- **Droite** : objet rectiligne prolongé sans fin dans les deux sens; `[AB]` est le segment limité par A et B, `(AB)` désigne leur droite porteuse. Deux points distincts déterminent une seule droite.
- **Angle** : ouverture entre deux demi-droites issues d'un sommet commun. À 90° : angle droit; entre 0° et 90° : aigu; entre 90° et 180° : obtus. Son ouverture n'est pas égale à la longueur des côtés dessinés. On peut le construire au gabarit ou au rapporteur.
- **Parallélisme** : droites distinctes d'un même plan sans point commun. `x=2` et `x=8` sont parallèles; `y=2` et `y=4` aussi. Des **segments** courts sans intersection peuvent appartenir à des droites qui se rencontrent : vérifier le prolongement.
- **Perpendicularité** : droites qui se coupent à angle droit. `x=2` et `y=5` sont perpendiculaires, même si des segments dessinés ne touchent pas physiquement leur intersection.
- **Symétrie axiale** : réflexion de chaque point P en P′ autour d'une droite `d` telle que `PP′` est perpendiculaire à `d` et que le milieu de `[PP′]` appartient à `d`. En particulier, `P` et `P′` sont à distance égale de l'axe. Si `P` est sur l'axe, `P′=P`. La réflexion conserve longueurs et ouvertures mais inverse le sens de la figure.
- **Formules prouvées** pour notre quadrillage : par rapport à `x=6`, `V(x;y)=(12−x;y)` (la moyenne des deux abscisses égale 6, l'ordonnée ne change pas). Par rapport à `y=6`, `H(x;y)=(x;12−y)` (abscisse constante, moyenne des ordonnées égale 6).

## Exemple résolu 1 — Petit triangle, axe vertical

**Énoncé :** axe `x=6`, triangle `A(2;2), B(4;2), C(3;4)`. Construire son image.

1. A se trouve à 4 carreaux à gauche de l'axe; placer `A′(10;2)` à 4 carreaux à droite.
2. B se trouve à 2 carreaux à gauche; `B′(8;2)`.
3. C se trouve à 3 carreaux à gauche; `C′(9;4)`.
4. Relier `A′B′`, `B′C′`, `C′A′` dans le même ordre de correspondance que ABC. Les segments AA′, BB′, CC′ sont horizontaux, donc perpendiculaires à l'axe vertical.
5. Contrôle indépendant : milieux `(6;2)`, `(6;2)`, `(6;4)`; distances horizontales à l'axe respectives `4=4`, `2=2`, `3=3`. L'axe échange chaque sommet avec son image : `V(V(A))=A`.

**Interprétation :** on a renversé gauche/droite sans déplacer le triangle vers le haut ou le bas. Les arêtes correspondantes ont même longueur.

## Exemple résolu 2 — Une ligne brisée et un axe horizontal

**Énoncé :** axe `y=6`, ligne brisée `D(1;3)→E(3;4)→F(5;2)`.

- La distance verticale D–axe est 3 : `D′(1;9)`; E–axe est 2 : `E′(3;8)`; F–axe est 4 : `F′(5;10)`.
- Relier `D′→E′→F′`. Contrôle : `3+9=12`, `4+8=12`, `2+10=12`; mêmes abscisses; segments `DD′`, etc. verticaux, perpendiculaires à `y=6`.
- Le dessin peut être réalisé avec un miroir posé sur l'axe puis vérifié par quadrillage; miroir et pliage sont des aides, non des justifications suffisantes à eux seuls.

## Deux contre-exemples analysés

**C1 — translation trompeuse :** pour axe `x=6`, on propose `A(2;2)→(8;2)` et `B(4;2)→(10;2)`, en déplaçant chaque point de +6. **Erreur :** les vraies images sont `A′(10;2)` et `B′(8;2)`. Pour A les distances seraient 4 à gauche et 2 à droite; pour B elles seraient 2 et 4. **Correction :** utiliser l'écart propre à chaque point, et non un déplacement commun.

**C2 — changement de mauvaise coordonnée :** axe `y=6`, `P(3;4)` est envoyé à `(9;4)`. **Erreur :** cela reflète par `x=6`, pas par `y=6`. **Correction :** `(3;8)`; le segment image est vertical, milieu `(3;6)` sur l'axe, distances `2=2`.

**Cas limite essentiel :** un point `R(6;5)` sur `x=6` a pour image **lui-même**, `(6;5)`. Ne jamais dessiner deux sommets distincts quand ils sont fixés par l'axe.

## Résolution que l'élève peut réutiliser

Tracer et nommer l'axe → repérer chaque sommet → compter la distance **perpendiculaire** → reporter **la même distance** de l'autre côté → relier les images dans l'ordre initial → justifier par milieux, perpendicularité et égalité des distances.
