# 01 — Notions, exemples résolus et contre-exemples

**Objectif `obj-1` :** Repérer des sources d’énergie et décrire les transformations observées. **Production `crit-1` :** Construire un schéma simple d’une chaîne énergétique observable.

## Quatre notions précises

**Source.** Pour un système délimité, élément qui fournit l'énergie entrante ou réserve d'énergie disponible. Ex. la pile fournit de l'énergie au circuit d'une lampe. Ce n'est pas une création d'énergie; à l'intérieur de la pile des changements chimiques rendent possible une livraison d'énergie électrique. Selon la frontière étudiée, « Soleil », « pile » ou « roue mise en mouvement » sont des sources pertinentes.

**Transfert.** Passage d'énergie d'un système à un autre. Il faut identifier le donneur et le récepteur; une même forme peut être transmise (air en mouvement → pales en mouvement). Une flèche entre objets ne signifie **pas**, à elle seule, que la forme de l'énergie change.

**Transformation.** Changement de forme d'énergie à l'intérieur d'un dispositif ou lors d'un phénomène. Ex. dans un moteur, énergie électrique reçue → mouvement + échauffement; dans une lampe, électrique → lumière + chaleur. **Énergie lumineuse ≠ énergie électrique**; les transformations n'ajoutent pas de l'énergie au monde.

**Usage.** Finalité utile dans la situation : éclairer, faire tourner un objet, produire un avertissement sonore. L'usage n'est ni une forme d'énergie ni nécessairement l'unique effet (une lampe peut aussi chauffer).

**Observation / modèle.** « La lumière s'allume », « les pales tournent », « un signal sonore se fait entendre » sont des constats dans la scène décrite; « le courant circule », « l'énergie chimique est transformée » sont des explications modélisées. La vérification d'un modèle peut exiger d'autres mesures; aucun schéma simple ne prouve à lui seul l'ensemble des détails internes.

**Gabarit de chaîne lisible (ne pas confondre la flèche et la conversion) :**

`[SOURCE (forme initiale)] --transfert vers--> [RÉCEPTEUR / CONVERTISSEUR : forme reçue → forme(s) produite(s)] --> [EFFET constaté ; USAGE]`

Lorsqu'une forme reste la même, écrire « mouvement transmis » plutôt qu'une transformation imaginaire. Lorsqu'un récepteur produit deux sorties, nommer celle qui sert à l'usage et l'autre plausible sans inventer de mesures de puissance.

## Exemple résolu 1 — Lampe de poche

**Description de la scène :** une lampe de poche à pile fonctionne; quand son interrupteur est activé, on voit de la lumière. Aucun démontage, aucune mesure.

1. **Constat :** lumière émise quand le bouton est activé. **Non constaté directement :** ce qui se passe à l'intérieur de la pile et du circuit.
2. **Source :** réserve d'énergie chimique de la pile (modèle). **Transfert :** énergie électrique fournie dans le circuit vers la lampe.
3. **Transformation :** au dispositif lumineux, énergie électrique → énergie lumineuse, avec une partie thermique possible.
4. **Schéma :** `[pile : réserve chimique] → [transfert d'énergie électrique] → [lampe : électrique → lumière (+ thermique)] → [lumière visible ; usage : éclairer]`.
5. **Conclusion :** la scène est cohérente avec une chaîne dans laquelle la pile alimente la lampe; elle ne démontre pas par observation seule les mécanismes cachés.

## Exemple résolu 2 — Panneau photovoltaïque et petit ventilateur

**Description contrôlée :** sans batterie et relié à son panneau photovoltaïque, un petit ventilateur tourne sous un éclairage suffisant; il cesse quand le panneau est masqué. On **n'assemble pas** ce dispositif en classe; on lit une description d'observation.

1. **Constat :** les pales tournent sous illumination et s'arrêtent quand elle disparaît. **Inférence :** le panneau a fourni de l'électricité au moteur.
2. **Source :** rayonnement lumineux reçu du Soleil (ou de la lumière d'essai décrite); **panneau :** lumière → énergie électrique.
3. **Transfert :** énergie électrique du panneau au moteur. **Moteur :** électrique → énergie de mouvement des pales (+ énergie thermique possible).
4. **Schéma :** `[lumière du Soleil] → [panneau : lumineuse → électrique] → [transfert électrique] → [moteur : électrique → mouvement (+ thermique)] → [pales tournent ; usage : déplacer l'air]`.
5. **Limite :** le schéma est un modèle simplifié; il ne donne ni rendement ni mesure et ne conclut pas que l'énergie est intégralement utile.

## Exemple résolu 3 — Vent et moulinet

**Constat :** dans une scène, un souffle d'air pousse les pales d'un moulinet libre, qui tourne. **Chaîne :** `[air en mouvement] → [transfert de mouvement par interaction air/pales] → [pales tournent]`. Pour ce fragment observé, **le mouvement est transmis**, pas converti en électricité. L'air perd ou redistribue une partie de son énergie cinétique; des pertes par frottement sont possibles. **Usage :** faire tourner une décoration. Sans générateur décrit, on ne met pas de « sortie électrique ».

## Contre-exemples à corriger

**CE1 — La « création » :** « La pile crée de l'énergie et la lampe la transforme en lumière. » **Pourquoi non :** la pile est une réserve chimique; elle rend disponible une énergie qui change de forme. **Réparation :** source/réserve chimique → transfert électrique → lumière et thermique.

**CE2 — Confusion entre transfert et transformation :** « Le vent devient de l'électricité dès qu'il fait tourner un moulinet en carton. » **Pourquoi non :** aucune génératrice n'est indiquée; voir des pales tourner montre un transfert de mouvement. **Réparation :** air en mouvement → pales en mouvement; pour obtenir de l'électricité il faudrait ajouter un convertisseur défini.

**CE3 — Confusion usage/source :** « Pour une sonnette, le bruit est la source d'énergie. » **Pourquoi non :** le bruit entendu est une **sortie** liée à la fonction avertir. La source peut être une pile. **Réparation :** pile → transfert électrique → sonnette : son (+ thermique), usage avertir.

**CE4 — Inférence présentée comme constat :** « J'ai vu l'électricité passer dans le fil fermé d'une lampe. » **Pourquoi non :** la lumière peut être vue; un courant électrique ne se voit pas directement dans un fil opaque. **Réparation :** observation : la lampe s'allume; explication modélisée : transfert électrique.

**Vigilance :** les appareils réels comportent souvent d'autres éléments. Le modèle utilisé sélectionne les transformations essentielles observables ou inférées, sans prétendre décrire toutes les pertes ni toutes les causes.
