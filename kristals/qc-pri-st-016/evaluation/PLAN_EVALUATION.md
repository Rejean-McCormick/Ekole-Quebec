# Plan d'évaluation — `qc-pri-st-016`

**Cadre unique :** `obj-1` « Expliquer par un modèle simple des phénomènes Terre-Soleil-Lune. »; `crit-1` « Utiliser un modèle pour expliquer un phénomène astronomique simple. »; famille native `qc-pri-st-016-ev-01` **type `generee_sous_contraintes`**. Pas d'évaluation PFEQ. Tous les items **à revoir** et à essayer.

## Ce que mesure l'épreuve (pas une récitation)

Une production observable présente **(1) objets et source lumineuse**, **(2) déplacement et représentation**, **(3) observation**, **(4) inférence/explication**, **(5) conclusion et limite du modèle**. Les supports (texte, schéma, objets) sont équivalents si les mêmes informations sont exprimées. Les phénomènes étudiés sont la rotation/jour-nuit, l'orbite/phases et leurs contrastes.

## Tableau de couverture et liens obligatoires

| Item lié à `obj-1`, `crit-1`, `qc-pri-st-016-ev-01` | Difficulté | Représentation | Cible / critères distinctifs | Variabilité |
|---|---|---|---|---|
| `q-001` | initial | globe+rayons décrits | jour/nuit, rotation, observation vs cause | fixe |
| `q-002` | initial | deux maquettes textuelles | rotation vs orbite, limite | fixe |
| `q-003` | initial | deux disques décrits | phase visible, rôle de la lumière et orbite | fixe |
| `q-004` | initial | trois flèches du système solaire | hiérarchie corps/orbites + jour/nuit | fixe |
| `q-005` | intermédiaire | stations A/B, contexte décrit | cause du jour/nuit selon côté de lampe | scénario contrôlé, 2 variantes |
| `q-006` | intermédiaire | observatoires lunaires A/B | rapport vue terrestre / phase, limite | scénario contrôlé, 2 variantes |
| `q-007` | intermédiaire | affirmation fausse + modèle | phases vs éclipse, alignement | fixe |
| `q-008` | intermédiaire | carnet observation/raisonnement | observation, inférence, conclusion, limite | fixe |
| `q-009` | transfert | planète et satellite fictifs | généraliser rotation+phases avec deux mécanismes | fixe |
| `q-010` | transfert | stand de musée | sens et limites d'une maquette non à l'échelle | fixe |
| `q-011` | transfert, **preuve 1** | station météo, lampe à droite, K/L | expliquer deux changements jour/nuit **sans indice** | fixe |
| `q-012` | transfert, **preuve 2** | atelier mobile, phases A/B | expliquer deux apparences lunaires **sans indice** | fixe |

Chaque item garde `item_id` complet et les champs `objectif_id`, `critere_id`, `family_id` dans `BANQUE_ITEMS.json`. Les douze tâches proposent questions complètes, stimulus accessible, réponse critériée, feedback, limites et statut.

## Consignes de correction

La banque donne des **corrigés-repères justifiés** : en sciences, plusieurs formulations, gestes ou schémas exacts sont acceptables, mais une proposition fausse (Soleil autour de Terre en 24 h; phases causées habituellement par ombre de Terre; échelle réelle de la maquette) ne peut recevoir le niveau satisfaisant sur la relation causale. Aucune reconnaissance automatique par texte libre/IA ne constitue une validation de fond. La grille indépendante prévoit des indicateurs observables par dimension, avec appréciation individuelle puis confrontation des deux preuves.

**Conditions d'autonomie :** lecture neutre de la consigne autorisée; matériel sûr/description textuelle admise; aucun indice causal ni feedback avant que la preuve soit remise. Refaire une preuve différente après remédiation si la première échoue. Deux preuves `q-011` et `q-012` **séparées** sont requises pour décider la maîtrise; ni note unique ni total de points cumulés.

## Encadrement reproductible des scénarios 005–006

- Deux alternatives **préécrites** et corrigées dans `parametres.corpus_verrouille` pour chacune des tâches `q-005`, `q-006`.
- Sélection **déterministe et vérifiable** : `index = somme des points de code Unicode de (seed + "|" + item_id) modulo 2` (indices 0 et 1). Les deux corrigés explicites se trouvent avec les stimuli dans les paramètres; l'item principal contient la version sélectionnée.
- **Contraintes :** source lumineuse et orientation définies, mécanisme physique invariant, aucune question nécessitant une date/orientation absente, pas de texte libre généré ni de modification de scénario sans revue scientifique/pédagogique. Les variantes ne sont **pas** considérées certifiées du fait du calcul.
- La stabilité du tirage peut être vérifiée par un script indépendant du barème. **Aucun modèle IA utilisé comme correcteur fiable**.

## Sécurité, droits et accessibilité

- **Sécurité :** ne jamais observer directement le Soleil ni le pointer avec un instrument improvisé; lampes LED froides supervisées, non dirigées vers les yeux, gros objets stables; voie textuelle disponible sans éclairage réel, sans mesure dangereuse.
- **Accessibilité :** tous les schémas sont décrits; pas d'information uniquement portée par couleur, figure, précision graphique ou lecture de chiffres; police agrandie, contraste, aide à la lecture **de la consigne uniquement**, scribe pour transcription non interprétative. Pour une tâche de représentation, les positions et liens doivent rester entièrement exprimés.
- **Droits :** stimuli, scénarios et corrigés originaux. Les liens NASA dans `sources/REFERENCES_CONTENU.md` servent à vérifier **les faits**, sans reproduction d'images ni reprise de paragraphes.
- **Revue humaine requise :** contrôle des ambiguïtés géométriques, valence des distracteurs, adaptation à l'âge, passation réelle, intercorrecteurs, critères de sécurité locale. Les scénarios fictifs n'impliquent aucune donnée d'élève.
