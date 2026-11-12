# 01 — Notions, exemples, contre-exemples

**Objectif `obj-1` :** Décrire des phénomènes météorologiques à partir de mesures et observations. **Critère `crit-1` :** interpréter une courte série de relevés météorologiques. Le vocabulaire est accessible, mais les termes scientifiques et les unités sont conservés.

## Qu'observe-t-on dans l'atmosphère ?

L'**atmosphère** est l'enveloppe gazeuse autour de la Terre. La **météo** décrit l'état de l'atmosphère en un lieu et un moment précis ou pendant une courte période. Elle n'est pas identique au **climat**, qui est décrit à partir de longues séries d'observations. Dans ce cours, toutes les données chiffrées sont **inventées pour apprendre**, non des relevés officiels.

| Notion | Définition scientifique accessible | Instrument ou trace | Unité / code | Piège à éviter |
|---|---|---|---|---|
| Température de l'air | Indicateur de l'état thermique de l'air à un endroit donné | Thermomètre protégé du soleil direct | °C | Confondre avec ressenti ou température de l'eau |
| Vent | Mouvement de l'air; une mesure de vitesse précise l'importance de son déplacement | Anémomètre; girouette pour la direction | km/h (vitesse); direction nommée si donnée | Un drapeau qui bouge ne donne pas une vitesse exacte; « du nord » = venant du nord |
| Pluie | Eau liquide qui tombe de l'atmosphère vers le sol | Pluviomètre; mesure de quantité accumulée **pour un intervalle défini** | mm; 1 mm = lame d'eau d'1 mm sur la surface réceptrice | La pluie de 2 mm n'est pas une température, ni une durée; `—` n'est pas `0 mm` |
| Nuages | Masses visibles de minuscules gouttelettes d'eau et/ou de cristaux de glace en suspension | Observation visuelle du ciel; photo décrite | Ici `0/10` ciel dégagé à `10/10` entièrement couvert, estimation grossière | Couvert ≠ pluie assurée |

**Vocabulaire du raisonnement :** observation directe = ce que l'on voit (ciel couvert); mesure = valeur instrumentale avec unité et conditions (14 °C, 5 mm pour 9–10 h); inférence = conclusion justifiée par les données (« hausse de 3 °C »); modèle = représentation simplifiée expliquant/organisant, pas un relevé supplémentaire; prévision = proposition sur le temps futur, **non prouvée** par deux mesures passées. **Donnée manquante** `—` : impossible de conclure à zéro.

### Exemple résolu 1 — Deux heures dans la cour (fictif)

Toutes les mesures viennent du même lieu. Les intervalles de pluie sont définis individuellement.

| Heure | Température | Vent | Pluie (heure précédente) | Couverture du ciel |
|---|---:|---:|---:|---:|
| 9 h | 7 °C | 5 km/h | 0 mm (8–9 h) | 2/10 |
| 12 h | 11 °C | 12 km/h | 3 mm (11–12 h) | 8/10 |

**Lecture et solution.** De 9 h à 12 h, `11 − 7 = 4` : la température **a augmenté de 4 °C**. Le vent mesuré est passé de 5 à 12 km/h. Il est noté 3 mm de pluie entre 11 h et 12 h; on ne sait pas ce qui s'est passé entre 9 h et 11 h, donc on ne peut pas donner le cumul de toute la matinée. Le ciel est plus couvert à 12 h, sans preuve que l'augmentation des nuages a causé la pluie.

### Exemple résolu 2 — Trois intervalles sans chevauchement (fictif)

À l'arrêt de bus, pluie relevée pour **8–9 h : 0 mm; 9–10 h : 2 mm; 10–11 h : 1 mm**. Vent aux instants 9 h : 8 km/h; 10 h : 15 km/h; 11 h : 9 km/h. **Solution :** pluie totale sur 8–11 h = `0 + 2 + 1 = 3 mm` (intervalles disjoints). Le vent mesuré le plus rapide est **15 km/h à 10 h**. Ces données ne permettent pas d'affirmer qu'il pleuvra à midi.

### Contre-exemple 1 — Nuageux, donc pluvieux ?

Relevé fictif à 14 h : ciel `9/10`; pluie **0 mm entre 13 h et 14 h**. Phrase erronée : « Il a forcément plu, puisqu'il y avait beaucoup de nuages. » **Correction :** le ciel est très couvert mais aucune pluie n'a été mesurée dans l'intervalle indiqué. Les nuages ne suffisent pas à conclure à la pluie.

### Contre-exemple 2 — Valeur absente ou trop grande conclusion ?

Relevé fictif : lundi `pluie = 4 mm`; mardi `pluie = —`. Phrase erronée : « La pluie a diminué à 0 mm mardi. » **Correction :** le chiffre du mardi est **manquant**, pas nul; on ne connaît pas l'évolution. De même, « cette région est toujours froide » ne découle pas d'une série de deux jours.

### Contre-exemple 3 — Périodes superposées

8–10 h : 4 mm; 9–11 h : 3 mm. **Ne pas** calculer « 7 mm entre 8 h et 11 h » : ces fenêtres se chevauchent entre 9 h et 10 h, on compterait peut-être une partie de la pluie deux fois. Il faut des intervalles disjoints ou les relevés bruts.

## Modèle de réponse complète

> « À [lieu] entre [heures ou dates], [mesure X] est passée de [valeur + unité] à [valeur + unité], donc [variation + unité]. J'observe aussi [autre mesure ou couverture]. Cela me permet de dire [constat], mais non [prévision ou cause non attestée]. »

**Ressources documentaires :** `sources/REFERENCES_CONTENU.md` (sources scientifiques consultées, sans licence d'images importée).
