# Plan d'évaluation — `qc-pri-ma-024` (v1.2)

**Identité liée pour chaque item :** objectif `obj-1`, critère `crit-1`, famille `qc-pri-ma-024-ev-01`. **Objectif immutable :** Identifier et construire des angles, des droites et des symétries simples. **Preuve :** Compléter une figure symétrique puis justifier la transformation. **Type privilégié :** `paramétrique_controle`, instrumenté par six items paramétriques à graine entière fixe et quatre items fixes de notions préalables/cibles.

## Matrice de couverture

| Item complet | Difficulté | Représentation | Objet observé / attendu | Usage |
|---|---|---|---|---|
| `qc-pri-ma-024-q-001` | initial | angle sur grille | 90° au sommet, deux rayons perpendiculaires | formatif |
| `qc-pri-ma-024-q-002` | initial | droites équations `x=c`, `y=c` | parallélisme et perpendicularité | formatif |
| `qc-pri-ma-024-q-003` | initial | trois angles d'un sommet | 45° aigu, 90° droit, 135° obtus | formatif |
| `qc-pri-ma-024-q-004` | intermédiaire | axe et deux points | image du point fixe sur l'axe et d'un point mobile | formatif |
| `qc-pri-ma-024-q-005` | intermédiaire | point et axe vertical | reflet `V(x;y)=(12−x;y)`, distance | entraînement paramétrique |
| `qc-pri-ma-024-q-006` | intermédiaire | point et axe horizontal | reflet `H(x;y)=(x;12−y)`, distance | entraînement paramétrique |
| `qc-pri-ma-024-q-007` | intermédiaire | triangle et axe vertical | trois images, ordre des arêtes et justification | entraînement paramétrique |
| `qc-pri-ma-024-q-008` | transfert | rectangle et axe horizontal | quatre images, invariance de la figure et justification | préparation au transfert |
| `qc-pri-ma-024-q-009` | transfert | **panneau triangulaire**, axe vertical | **preuve autonome A** : trois images et justification | maîtrise A |
| `qc-pri-ma-024-q-010` | transfert | **frise en ligne brisée**, axe horizontal | **preuve autonome B** : quatre images et justification | maîtrise B |

Chaque ligne est liée également dans le JSON aux références `obj-1`, `crit-1`, `qc-pri-ma-024-ev-01`. La majorité des items évaluent explicitement les distances et les perpendiculaires, pas seulement un dessin ressemblant.

## Paramétrage borné et contrôlé

- **Pas de tirage non reproductible**. Pour q-005 à q-010, `seed` est un entier fixé; les coordonnées sont calculées par `mod` et division entière `//` avec les formules inscrites **dans chaque item** (`parametres.algorithme_generation`). Le domaine est `seed ∈ {0,…,2147483647}` et la grille `0..12` pour les deux coordonnées. Les décalages sont 0..1 ou 0..2 selon la figure, et les formes restent strictement d'un côté de l'axe pour les six familles paramétriques.
- **Correcteur géométrique** : axe `x=6` → `(x;y)↦(12−x;y)`; axe `y=6` → `(x;y)↦(x;12−y)`; relier les images dans l'ordre des étiquettes. **Validation indépendante** : chaque paire a son milieu sur l'axe, le segment image est perpendiculaire à l'axe et la distance point-axe est égale à la distance image-axe. Deux seeds par item sont sauvegardées dans les exemples de contrôle. La notation algébrique n'est pas un prérequis pour l'élève; elle rend le correcteur contrôlable.
- Les exercices q-001 à q-004 sont entièrement fixes; `seed=null`, `parametres=null`. Les six paramétriques portent des seeds et instances explicites, y compris les épreuves A et B; **aucune génération IA libre**. Si un système extérieur veut varier les seeds, il doit appliquer les filtres documentés et recontrôler les réponses avant usage; le ZIP n'affirme pas cette exécution future.

## Conditions des deux preuves de maîtrise

L'apprenant doit produire **deux constructions autonomes distinctes** q-009 et q-010, dans les univers « panneau » et « frise », avec orientations d'axes et topologies de figures différentes. Ne pas redonner les coordonnées des images, ni faire une démonstration simultanée, ni déduire la maîtrise d'une moyenne de points. L'évaluateur consigne séparément pour chaque contexte : axe, points-images, ordre de connexion, justification de perpendicularité et d'égalité des distances, corrections spontanées, aides offertes. **La preuve exige un tracé ou une désignation précise des points**, et non uniquement réciter la formule.

## Cotation et sécurité / accessibilité

Rubrique à niveaux M1–M5 dans `evaluation/GRILLE_MAITRISE.md`; 0=absent/erroné, 1=partiel, 2=exact et autonome. La réussite requiert M1, M2, M3, M4, M5 = 2 sur **chaque** preuve, ou nouveau contrôle ciblé si une observation est invalide, et deux contextes réussis. Le plan évite une note générale qui compenserait une construction fausse.

Grille haute lisibilité et légendes x/y, couleurs non indispensables, axes explicitement nommés, verbalisation/écriture/saisie par scribe non directif équivalentes. La tâche ne dépend pas d'une motricité fine parfaite. Pas de collecte d'informations personnelles ni de captation exigée; matériel scolaire sans risque inhabituel, révision locale des besoins d'accès. Les calculs seront vérifiés par test technique; leur validité didactique et psychométrique appelle une revue humaine.
