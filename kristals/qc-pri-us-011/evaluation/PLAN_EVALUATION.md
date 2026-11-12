# Plan d'évaluation v1.2 — `qc-pri-us-011`

**Objectif `obj-1` :** Expliquer des conséquences de l’industrialisation sur la vie quotidienne. **Critère `crit-1` :** Relier une transformation technique à deux effets sociaux documentés. **Famille immuable :** `qc-pri-us-011-ev-01`, type natif `generee_sous_contraintes`. La banque propose des tâches sources **fixes** et deux dossiers **scénarios contrôlés sans tirage**. Rien n'est produit par une IA pendant la correction.

## Couverture des dix items

Tous les items ci-dessous relèvent **explicitement** de `obj-1`, `crit-1` et `qc-pri-us-011-ev-01`, même lorsqu'un item initial ne vise qu'une composante formative. La banque JSON contient aussi ces trois liens pour chaque item.

| Item complet | Niveau | Représentation | Observation/critère | Usage |
|---|---|---|---|---|
| `qc-pri-us-011-q-001` | initial | frise écrite/tactile | Distinguer ouverture, agrandissement et constat d'emploi | formatif |
| `qc-pri-us-011-q-002` | initial | fiche S1, explication | Trouver mécanisme et effet, rejeter salaire universel | formatif |
| `qc-pri-us-011-q-003` | initial | tri A–D | Classer changements techniques et sociaux | formatif |
| `qc-pri-us-011-q-004` | intermédiaire | S1/S2, chaîne sourcée | Deux effets distincts, emplois + quartier | formatif |
| `qc-pri-us-011-q-005` | intermédiaire | S3, tableau | Travail ferroviaire et vie urbaine, nuance | formatif |
| `qc-pri-us-011-q-006` | intermédiaire | S4, synthèse | Migration de travail et établissement sans cause unique | formatif |
| `qc-pri-us-011-q-007` | intermédiaire | critique de texte fictif | Corriger anachronisme, « tous » et preuves | formatif |
| `qc-pri-us-011-q-008` | transfert | S1/S2/S3, deux chaînes | Deux milieux et une limite de comparaison | transfert préparatoire |
| `qc-pri-us-011-q-009` | transfert | dossier A, source S1/S2 | **Preuve indépendante A :** hydraulique, deux effets, deux indices et limite | maîtrise A |
| `qc-pri-us-011-q-010` | transfert | dossier B, source S3 | **Preuve indépendante B :** chemin de fer, deux effets, deux indices et limite | maîtrise B |

## Grille, variabilité et critères

Pour 001–008, appliquer les critères item par item; pour 009 et 010, appliquer les cinq critères **M1–M5** de `evaluation/GRILLE_MAITRISE.md`. Chacun a une description de réussite, de preuve et une correction justifiée. Niveau et représentation sont inscrits dans le JSON. Deux effets différents, **documentés**, sont toujours nécessaires pour les preuves finales. Évaluer le raisonnement historique, non le nombre de mots ni la virtuosité d'écriture.

**Variations permises :** présentation en gros caractères, lecteurs d'écran, surlignage accessible, lecture vocale neutre, réponse par texte, tableau, dessin expliqué, oral ou dictée. Document/citations reformulés à l'identique des faits et des référents. Temps de lecture adapté avant passation. Ces aménagements ne peuvent ni fournir la conclusion ni identifier à la place de l'élève les deux effets et leurs sources.

**Variations interdites :** choix libre d'archives, changement de siècle ou de groupe, remplacement d'un contexte par une histoire inventée, chiffres reconstruits, interprétations stigmatisantes, génération de corrigés par IA ou changement de l'objectif. Pour les épreuves 009 et 010, `parametres.scenario_id` fixe le dossier, `seed=null` (pas de tirage). Les variantes futures devront être sourcées, révisées et porter un identifiant de version.

## Deux manifestations de maîtrise, procédures indépendantes

1. **A — dossier du canal de Lachine (`q-009`)** : distribuer le dossier A1/A2 inédit au moment de la passation, lecture neutre autorisée; demander transformation hydraulique, un effet sur travail, un effet sur quartiers, détails de source et réserve. Consigner la prestation dans la grille M1–M5.
2. **B — dossier du chemin de fer (`q-010`)** : lors d'une autre séance ou d'un moment distingué, présenter B1/B2, portant sur l'emploi des porteurs noirs et la vie communautaire près des gares. Ne pas recopier la chaîne du canal. Consigner M1–M5 indépendamment.
3. **Autonomie** : aucune aide sur les conclusions et sur le choix des passages pendant la prestation. Une interruption d'accessibilité ne vaut pas échec; ajuster et reprendre. Deux contextes validés séparément, pas de moyenne globale.
4. **Feedback après chaque essai** : repérer le maillon manquant (technique, effet, preuve, nuance) et prescrire une remédiation ciblée sur une autre fiche, puis nouvelle preuve si besoin.

## Sources, biais et sécurité

Corpus S0–S4 documenté dans `sources/REFERENCES_CONTENU.md`. Les dossiers destinés aux élèves sont des **synthèses pédagogiques originales**, non des reproductions d'archives ou citations verbatim. L'enseignant précise les populations : travail manufacturier à Montréal et porteurs noirs au Canada, dont plusieurs à Montréal; aucun fait non documenté sur les Premiers Peuples ou toutes les familles. Évoquer la discrimination de façon factuelle, sans assignation d'identité ou de rôle et sans sollicitation d'informations personnelles. Aucune exploration d'une usine, d'un canal, d'un rail ou d'un chantier n'est nécessaire.

## Limites et validation

Rubriques et synthèses à **réviser** pour nuance historique, fiabilité interévaluateurs, lecture et équité. Les contrôles JSON ou d'intégrité ne constituent ni un essai auprès d'élèves ni une qualification externe. Les item IDs gardent `validation_status: a_revoir`.
