# 01 — Notions, exemples résolus et contre-exemples

**Objectif `obj-1` :** Représenter des interactions alimentaires et environnementales d’un habitat. **Preuve `crit-1` :** Construire un réseau simple et prédire l’effet d’un changement de ressource. Le thème vise une **représentation justifiée**, pas une étude biologique de terrain.

## Définitions précises

1. **Habitat :** milieu de vie d'un organisme, comprenant les conditions et éléments vivants ou non vivants dont il dépend. Une mare peut offrir eau, abri, nourriture et espace. Un habitat n'est **pas** identique à une seule relation alimentaire.
2. **Ressource :** élément disponible dont des êtres vivants peuvent avoir besoin : eau, nourriture, abri, espace, lumière pour les producteurs photosynthétiques. Dans les scénarios, une ressource alimentaire est une **matière consommée**, par exemple les plantes mangées par un herbivore; l'eau n'est pas traitée comme un maillon « mangé ».
3. **Chaîne alimentaire :** suite orientée d'organismes « nourriture → consommateur », où chaque flèche représente le transfert de matière et d'énergie par consommation. **Une flèche pointe vers celui qui consomme**, jamais vers le consommé; elle n'exprime pas simplement « influence sur ».
4. **Réseau alimentaire :** combinaison de chaînes alimentaires reliées. Un organisme peut avoir plusieurs ressources ou plusieurs consommateurs; un réseau de classe peut être incomplet, car il n'inclut que les liens documentés.
5. **Impact :** conséquence d'un changement de disponibilité d'une ressource ou d'une condition de l'habitat. *Constater* une ressource en baisse ne suffit pas à affirmer un effet mesuré sur les autres organismes. Une bonne **prédiction** est conditionnelle et indique la relation qui la justifie.

**Langage du raisonnement scientifique :** donnée fournie (« la carte précise X est mangé par Y »), observation (dans une illustration/mesure, on constate X), modèle (graphe traduit les cartes), inférence (selon le modèle, Y dépend de X), prédiction (« si X se raréfie et si aucune autre ressource ne compense, Y pourrait manquer de nourriture »), conclusion empirique (exigerait un suivi effectif). Ne pas appeler « observation » une ligne d'un récit fictif.

## Conventions pour tous les schémas

- **F :** ressource alimentaire (= organisme ou matière organique représentée sur les cartes); **C :** consommateur; **R :** ressource environnementale non alimentaire (eau, abri, lumière). Les cartes de classe définissent qui mange quoi.
- **Trait plein fléché `A → B` :** A est consommé par B. **Note `R : eau`** : condition non alimentaire; ne pas dessiner `eau → escargot` comme si c'était une chaîne.
- **Lien absent :** signifie « pas documenté dans le jeu de cartes », et non « impossible dans la nature ».
- L'effet de la raréfaction est décrit par « **pourrait** » ou « **risque de** » sous une condition « si les autres aliments ne compensent pas ». Un réseau seul ne donne pas le nombre d'animaux ni les délais.

## Exemple résolu 1 — Prairie fictive, deux chemins vers le rapace

**Jeu de cartes (hypothèses didactiques de cette activité, non inventaire réel) :**

- C1. Dans le modèle, le trèfle est mangé par la sauterelle.
- C2. Le trèfle est mangé par le campagnol.
- C3. La sauterelle est mangée par un petit oiseau insectivore.
- C4. Le petit oiseau est mangé par le rapace.
- C5. Le campagnol est mangé par le rapace.

**Construction et corrigé :** `trèfle → sauterelle → petit oiseau → rapace` et `trèfle → campagnol → rapace`. Ensemble exact d'arêtes : `{trèfle→sauterelle, trèfle→campagnol, sauterelle→petit oiseau, petit oiseau→rapace, campagnol→rapace}`. La bifurcation se situe au trèfle; les deux chaînes convergent vers le rapace.

**Changement imposé :** la quantité de trèfle disponible diminue. **Effet direct plausible :** sauterelle et campagnol pourraient disposer de moins de la ressource représentée. **Effet indirect plausible :** le petit oiseau pourrait trouver moins de sauterelles; le rapace pourrait être touché par la modification de ses proies. **Limite :** les cartes ne précisent pas leurs autres nourritures ni la période; les effectifs ne peuvent donc pas être chiffrés ou affirmés en baisse.

## Exemple résolu 2 — Mare fictive, une ressource alternative

**Jeu de cartes :** (M1) algues microscopiques consommées par zooplancton; (M2) algues consommées par escargots aquatiques dans ce modèle simplifié; (M3) zooplancton consommé par de petits poissons; (M4) escargots consommés par les mêmes petits poissons dans le modèle; (M5) petits poissons consommés par un héron.

**Réseau exact :** `algues → zooplancton → petits poissons → héron` et `algues → escargots aquatiques → petits poissons`. Les deux ressources du poisson convergent vers lui.

**Changement :** le zooplancton se raréfie. **Prédiction conditionnelle :** les poissons pourraient recevoir moins de nourriture provenant du zooplancton; les escargots constituent une autre ressource indiquée, donc on **ne peut pas** conclure que les poissons disparaîtront. Un éventuel effet sur le héron est **indirect et incertain**; suivre les poissons, les escargots et les hérons serait nécessaire.

**Point critique :** la mare comporte aussi de l'eau, indispensable à son habitat, mais aucune flèche alimentaire `eau → poisson` n'est ajoutée.

## Contre-exemple 1 — Flèche inversée et donnée inventée

**Proposition incorrecte :** « La sauterelle mange le trèfle, donc `sauterelle → trèfle` », puis « le rapace mange des escargots » sans carte correspondante. **Deux erreurs :** sens inversé et lien non documenté. **Correction :** `trèfle → sauterelle`, conserver seulement les cinq arêtes C1–C5. Dans une enquête réelle, on devrait apporter la trace des aliments du rapace avant d'ajouter un lien.

## Contre-exemple 2 — Effet certain non justifié

**Proposition incorrecte :** « Comme le zooplancton diminue, tous les poissons et tous les hérons vont mourir ». **Pourquoi :** aucune quantité, aucune durée, et une autre ressource poisson (escargots) existe dans la carte. **Correction :** « Si le zooplancton diminue *et si* les escargots ou autres ressources ne compensent pas, les poissons pourraient avoir moins d'aliments; les hérons pourraient être touchés indirectement. » Cela **ne prouve aucune diminution réelle**.

## Discussion courte avec preuves

« Quelles flèches sont justifiées par les cartes ? Quels éléments sont des observations, lesquels sont des hypothèses ? » La validité s'apprécie en pointant la carte et la flèche, pas au dessin le plus décoratif. Aucune manipulation de faune ou de plantes n'est nécessaire.
