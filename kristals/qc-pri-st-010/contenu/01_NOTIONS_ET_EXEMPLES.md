# 01 — Notions, exemples commentés et contre-exemples

**Objectif immuable `obj-1` :** Construire un circuit très simple et distinguer circuit fermé et ouvert. **Preuve `crit-1` :** Dessiner puis vérifier le fonctionnement d’un montage à basse tension.

## Vocabulaire exact

1. **Composant :** élément du circuit ayant un rôle défini. Source : un boîtier fermé contenant deux piles AA de 1,5 V en série fournit environ 3 V nominalement. Récepteur : ampoule miniature **incandescente adaptée à 3 V** qui convertit une partie de l'énergie électrique en lumière et chaleur. Commande : interrupteur. Liaison : fil dont le conducteur métallique est protégé par une gaine isolante. On ne substitue pas librement une DEL à l'ampoule : elle nécessite un choix de polarité et généralement une limitation de courant adaptés.
2. **Conducteur :** matériau traversé plus facilement par le courant dans ce contexte; métal de l'âme du fil, connecteur métallique approprié. **Isolant :** gaine plastique du fil; elle protège et n'assure pas à elle seule la liaison électrique. Les propriétés dépendent des conditions; on ne dit pas que « tout métal attire un aimant » ni que toute matière est toujours isolante.
3. **Circuit électrique :** ensemble formant une **boucle** de connexions de la borne positive de la source vers le récepteur puis vers la borne négative. Pour ce montage simple et intact, le circuit **fermé** comporte un chemin complet et l'ampoule peut s'allumer; l'**ouvert** comporte une coupure et elle ne s'allume pas. Une ampoule éteinte ne suffit pas, à elle seule, pour prouver que le circuit est ouvert (pile épuisée, ampoule endommagée, mauvais contact).
4. **Sécurité :** prévenir court-circuit, surchauffe, fuite, ingestion et contact avec le secteur. Un **court-circuit** est un chemin conducteur reliant directement les deux bornes en contournant l'ampoule : il peut faire chauffer les piles et le fil; **ne jamais le réaliser, même brièvement**.
5. **Observation, modèle, inférence :** observation = « l'ampoule s'est allumée »; modèle = « une boucle comprenant une source et un récepteur fonctionnels permet un courant »; inférence = « le changement de position du commutateur a probablement fermé la boucle ». Une prédiction (« elle devrait s'allumer ») n'est pas une observation.

## Matériel et protocole commun (adulte responsable)

**Aucun élève ne manipule ni n'installe les piles.** Un adulte monte/inspecte un kit pédagogique de basse tension comprenant un support fermé avec deux piles **AA alcalines neuves et identiques**, une ampoule à filament miniature **nominale 3 V dans sa douille**, des fils à gaine intacte avec connecteurs protégés et un interrupteur prévu pour le kit. Aucun branchement mural, secteur, adaptateur improvisé, chargeur, pile bouton ou batterie lithium. Montage sur surface sèche, mains sèches. L'adulte vérifie que la liaison passe obligatoirement par l'ampoule (jamais de fil directement entre les deux bornes) **avant** d'autoriser la fermeture du circuit. Arrêter à la moindre anomalie (chaleur, odeur, fuite, fil abîmé). Un enfant n'utilise le commutateur ou les fiches sécurisées qu'en présence de l'adulte.

## Modèle graphique original

```
  (+) [BOÎTIER DE PILES 3 V] (-)
   |                         |
   |                         |
 [INTERRUPTEUR] ---------- [AMPOULE 3 V]
```

Les traits représentent des **connexions**. Pour tester : interrupteur fermé = boucle continue; interrupteur ouvert = coupure. Les positions des symboles n'indiquent pas les distances réelles. Le support de piles, l'ampoule et le commutateur sont en série, non reliés directement l'un à l'autre en dérivation du récepteur.

## Deux exemples originaux résolus

**Exemple A — Éclairage d'une maquette de cabane.** Sur le modèle ci-dessus, l'interrupteur est d'abord ouvert. **Prédiction :** lampe éteinte. **Observation de référence** (pour du matériel contrôlé en bon état, une fois le montage physiquement testé par l'enseignant) : lampe éteinte. L'enseignant ferme l'interrupteur : l'ampoule s'allume. **Interprétation :** la coupure a été supprimée; la boucle traverse maintenant le récepteur. **Vérification :** ouvrir de nouveau, la lampe s'éteint. Ne jamais fabriquer les observations d'une séance réelle : écrire *à constater* si elle n'a pas eu lieu.

**Exemple B — Déplacement d'une ampoule sur une planche de démonstration.** L'adulte repositionne la douille à un autre endroit **hors tension**, sans modifier la boucle. **Prédiction :** quand le commutateur est fermé et les connexions sont correctes, la lampe s'allume malgré la nouvelle position. **Modèle :** c'est la continuité des connexions et non la forme dessinée du rectangle qui compte. L'adulte effectue le contrôle si le matériel est disponible; sans test, noter « prédiction non encore vérifiée ».

## Deux contre-exemples expliqués

**Contre-exemple 1 — Liaisons des deux bornes sans ampoule.** Une esquisse relie (+) directement à (−) par un seul fil. **Incorrect et interdit :** ce chemin court-circuite la source, risque de surchauffe et ne teste pas la notion de récepteur. On **barre le dessin**, on ne réalise jamais ce montage. Correctif : insérer l'ampoule, vérifier les connexions, puis l'interrupteur sous supervision.

**Contre-exemple 2 — « La lampe reste éteinte, donc l'interrupteur est ouvert ».** Ce n'est pas certain : pile usée, douille mal connectée ou ampoule défectueuse peuvent aussi empêcher l'allumage. **Correctif :** observation = « lampe éteinte »; prédiction/inférence = « il y a peut-être une coupure »; le contrôle des composants revient à l'adulte. Ne jamais insister en multipliant des manipulations hasardeuses.

## Magnétisme : distinction utile, hors évaluation

Un aimant peut exercer une attraction sur certains matériaux ferromagnétiques, indépendamment d'un circuit alimenté. Une pile fournit l'énergie d'un circuit; **un aimant posé sur la table ne remplace pas une pile**. Démonstration éventuelle exclusivement par l'adulte avec un aimant encapsulé de grande taille; aucun petit aimant libre. Le champ magnétique créé par un courant ne fait pas partie de la preuve `crit-1`.

**Sources et statut :** définitions synthétisées de Science Buddies et des consignes Santé Canada; schémas, exemples et contre-exemples originaux. Voir `../sources/REFERENCES_CONTENU.md`.
