# Plan d'évaluation — `qc-pri-eps-001-ev-01`

- **Kristal :** `qc-pri-eps-001`, « Conscience corporelle et schéma corporel ».
- **Objectif immuable (`obj-1`) :** Identifier ses segments corporels et coordonner un mouvement simple.
- **Critère immuable (`crit-1`) :** Exécuter un mouvement ciblé en décrivant ses repères corporels.
- **Mode disciplinaire :** `observation_ou_production` instrumenté par items `fixe` ou `scenario_controle` (corpus fermé). Pas de QCM forcé, pas de note sur apparence ou aptitudes brutes.
- **Contrat famille :** voir `authoring/CONTRAT_PEDAGOGIQUE.json`; grilles détaillées dans `evaluation/GRILLE_MAITRISE.md`.

## Couverture de la banque

Chaque item est lié à `obj-1`, `crit-1` et `qc-pri-eps-001-ev-01` dans la banque. Représentations et couverture :

| Item | Difficulté | Tâche, notion dominante | Représentation | Variation contrôlée |
|---|---|---|---|---|
| q-001 | initial | Coude et main, segments du corps | Silhouette / pointage | Aucune |
| q-002 | initial | Avant / après, perception de position | Deux images + geste | Aucune |
| q-003 | initial | Posture et appui sûr | Postures illustrées / geste | Aucune |
| q-004 | intermédiaire | Latéralité et effet miroir | Deux silhouettes / explication | Aucune |
| q-005 | intermédiaire | Segment, départ, arrivée | Nuage → étoile, geste | Aucune |
| q-006 | intermédiaire | Critère de contrôle vs amplitude | Comparaison argumentée + geste | Aucune |
| q-007 | intermédiaire | Initiation autonome du trajet | Support « maison » | Aucune |
| q-008 | intermédiaire | Repère d'articulation et direction | Silhouette + geste | Aucune |
| q-009 | transfert | Mobilisation nouvelle des repères | Planche de deux symboles | Deux cartes fermées; `seed` stable |
| q-010 | transfert | Transfert d'une posture illustrée | Carte avant/après + geste | Deux cartes fermées; `seed` stable |
| q-011 | transfert | **Preuve A : atelier de repères colorés** | Marques de couleurs inédites / mouvement et repères | Deux paires approuvées; `seed` stable |
| q-012 | transfert | **Preuve B : cartographie gestuelle** | Deux symboles sur carte inédite / mouvement et repères | Deux paires approuvées; `seed` stable |

Les items 11 et 12 sont réservés à une évaluation **autonome** dans deux contextes différents; les variantes ne doivent pas avoir été utilisées en guidage. Items 1 à 10 : formation et entraînement, sans possibilité de remplacer une des deux preuves par une simple moyenne.

## Barème d'observation non numérique

- **C1** : segment nommé/désigné précisément, repère corporel pertinent (côté ou articulation).
- **C2** : mouvement volontaire et ciblé, coordination possible **pour cet élève**, posture / appui et espace sûrs; amplitude et rapidité non cotées.
- **C3** : deux repères pertinents (départ et arrivée, ou articulation plus direction dans une tâche où c'est explicitement accepté).
- **C4** : autonomie de décision : pas d'indice sur « quoi, où, comment » après le départ. Soutien technique non directif et mode alternatif de communication admis.
- Chaque axe : **0** non observable / preuve impossible à interpréter; **1** avec indice ciblé ou partiel; **2** démontré seul avec aménagement stable. Une condition dangereuse entraîne l'arrêt et une observation différée, jamais une pénalité corporelle.

## Variabilité, qualité du corrigé et générateur

- `fixe` : phrase, stimulus et grille stables; seules adaptations motrices/sensorielles nécessaires sont documentées à part et ne changent pas le savoir testé.
- `scenario_controle` : deux variantes fermées par item q-009 à q-012; `i = seed % len(variantes)`, `stimulus` et `reponse_attendue` proviennent de la même variante indexée. Les exemples de graines et contraintes sont dans `BANQUE_ITEMS.json` et vérifiés par tests logiciels; pas de générateur IA libre.
- Un corrigé de performance décrit les **observables admis**, pas une forme physique idéale. Les énoncés ne supposent pas qu'un élève peut se tenir debout, saisir des objets, voir les couleurs ou distinguer auditivement une instruction. Les repères peuvent être nommés ou tactiles.

## Conditions de passation et sûreté

Adulte responsable présent; surface sans obstacle, posture et distance adaptées, aucune douleur, étirement, chute, saut, charge ou contact physique non consenti. Autoriser pauses et modalité motrice volontaire accessible; les paramètres individuels sont décidés avec les personnes responsables **avant** la preuve. Consignes courtes, pictogrammes et aide à la communication. Aucune collecte d'informations médicales, mesures corporelles, photographies ou vidéo obligatoire. En cas d'inaccessibilité, noter « observation non interprétable » puis adapter, jamais « échec » automatique.

**Séparation évaluation/enseignement :** q-011 et q-012 non montrés lors de la leçon; deuxième preuve à un autre poste, après délai raisonnable; retenir seulement les traces d'observation autorisées. Les rubriques, la sécurité et l'équité nécessitent revue et essai humain avant emploi sommatif. Références externes : `sources/REFERENCES_CONTENU.md`.
