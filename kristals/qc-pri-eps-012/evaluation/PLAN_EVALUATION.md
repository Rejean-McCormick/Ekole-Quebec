# Plan d'évaluation — `qc-pri-eps-012`

**Famille unique :** `qc-pri-eps-012-ev-01` ; **objectif unique :** `obj-1` — « Analyser une pratique physique à partir de critères observables et personnels non comparatifs. » ; **critère de preuve :** `crit-1` — « Comparer deux essais personnels et identifier une prochaine adaptation. » ; **type :** `observation_ou_production`. Les items partiels préparent la preuve intégrale, mais ne remplacent jamais deux essais personnels.

## Tableau de liaison exhaustif

| Item | Liens | Difficulté | Représentation / preuve | Dimension dominante | Variabilité permise |
|---|---|---|---|---|---|
| `qc-pri-eps-012-q-001` | `obj-1` / `crit-1` / `qc-pri-eps-012-ev-01` | initial | formule de but oral/texte | O : objectif non comparatif | aucune variation du scénario |
| `qc-pri-eps-012-q-002` | `obj-1` / `crit-1` / `qc-pri-eps-012-ev-01` | initial | deux traces écrites | C : observations précises | formulations équivalentes |
| `qc-pri-eps-012-q-003` | `obj-1` / `crit-1` / `qc-pri-eps-012-ev-01` | initial | justification orale | E : effort non inférable | modalités d'expression |
| `qc-pri-eps-012-q-004` | `obj-1` / `crit-1` / `qc-pri-eps-012-ev-01` | initial | décision de sécurité | S : interruption adaptée | réponses verbales équivalentes |
| `qc-pri-eps-012-q-005` | `obj-1` / `crit-1` / `qc-pri-eps-012-ev-01` | intermédiaire | scénario écrit Lina | C/A : comparaison, adaptation | seul corpus fixe |
| `qc-pri-eps-012-q-006` | `obj-1` / `crit-1` / `qc-pri-eps-012-ev-01` | intermédiaire | plan oral/pictos | O/C/A/S : planification | geste accessible validé |
| `qc-pri-eps-012-q-007` | `obj-1` / `crit-1` / `qc-pri-eps-012-ev-01` | intermédiaire | tableau essai 1/2 | C : conclusion prudente de stabilité | données fixes |
| `qc-pri-eps-012-q-008` | `obj-1` / `crit-1` / `qc-pri-eps-012-ev-01` | intermédiaire | dialogue et feedback | A/S : ajustement respectueux | tournures équivalentes |
| `qc-pri-eps-012-q-009` | `obj-1` / `crit-1` / `qc-pri-eps-012-ev-01` | transfert | **preuve A personnelle : manipulation d'objet** | O/C/E/A/S : cinq dimensions | matériel, support, geste accessible sous supervision |
| `qc-pri-eps-012-q-010` | `obj-1` / `crit-1` / `qc-pri-eps-012-ev-01` | transfert | **preuve B personnelle : séquencement de repères** | O/C/E/A/S : cinq dimensions | gestes à place fixe ou déplacement bref autorisé |

## Critères communs et barème

- **O — Objectif :** personnel, descriptible, contrôlable dans l'activité.
- **C — Comparaison :** un fait observable de chaque essai **personnel**, lien explicite avec l'objectif; stabilité et difficulté peuvent être rapportées correctement.
- **E — Effort :** ressenti personnel facultatif; distinction entre vécu et observation, sans inférence sur quelqu'un d'autre.
- **A — Adaptation :** prochain geste ou choix concret, pertinent au regard des faits et faisable sans danger.
- **S — Sécurité :** espace/matériel contrôlés avec l'adulte, décision d'arrêt ou de report pertinente; aucune prise de risque requise.

Rubrique à **quatre niveaux 0–3**, descriptions exactes dans `GRILLE_MAITRISE.md`. On ne mesure ni vitesse, ni nombre de réussites, ni capacité brute, ni morphologie; aucune valeur médicale sensible. Un seul item n'est jamais un diagnostic définitif de maîtrise.

## Couverture et échantillonnage

- Initial : q001–q004 (objectif, faits, effort, sécurité). Intermédiaire : q005–q008 (comparaison avec objectif, adaptation, stabilité, feedback). Transfert : q009–q010 (deux preuves personnelles de la tâche complète, dans **deux contextes distincts**).
- Preuve A : comparer deux **essais de guidage d'un objet**; preuve B : deux **essais d'enchaînement de gestes**. Les gestes, le matériel et les modalités sont ajustés avec l'adulte; conserver le raisonnement évalué. Plusieurs élèves peuvent avoir des gestes distincts et être évalués avec les mêmes critères analytiques.
- **Maitrise :** q009 **ET** q010 documentés, dans des occasions distinctes; analyse sans aide cognitive pour au moins l'une; niveaux ≥2 pour O/C/A/S dans chaque contexte et niveau ≥2 pour E (distinguer effort vécu/observable suffit); aucune violation de S; feedback suivi d'un réessai si lacune. Pas de moyenne ni « 8/10 = réussi ».
- **Remédiation :** examiner la dimension déficiente, mettre en œuvre `contenu/06_REMEDIATION_ET_TRANSFERT.md`, recueillir une nouvelle preuve après intervention, sans traiter une contre-indication comme un échec.

## Variabilité, contrôle et correction

- Modes utilisés : `fixe` et `scenario_controle`. **Aucun item paramétrique mathématique** n'est revendiqué; `seed` et `parametres` sont `null` car les scènes textuelles sont fixées et les réponses qualitatives sont vérifiées par des rubriques observables.
- Les seules variantes autorisées sont les modalités expressives, gestes adaptés et matériels sûrs spécifiés dans `BANQUE_ITEMS.json` sous supervision. Toute autre variation de scénario requiert une révision explicite et un nouvel item versionné. Ne pas confier à une IA la correction ou la validation automatique des productions.
- Chaque item possède une **réponse témoin / grille justifiée**, une rétroaction, des limites de variation et `validation_status: a_revoir`. Si l'élève donne une analyse cohérente différente de l'exemple, elle est recevable selon les critères.

## Sécurité, accessibilité et confidentialité

- L'adulte prépare et supervise les gestes; l'élève peut interrompre sans pénalité, utiliser aides habituelles, modifier l'amplitude/le support, remplacer un trajet par des gestes à place fixe, répondre oralement, à l'écrit, par cartes ou dictée fidèle.
- L'aide à la mobilité/matérielle et la transcription ne sont **pas** une aide cognitive; noter la différence pour apprécier l'autonomie. Si la personne ne peut essayer sans risque, utiliser les scénarios q001–q008 pour apprendre, **différer q009/q010**, ne jamais inventer une pratique effectuée.
- Aucune comparaison interélèves, image obligatoire, vidéo, durée standard, données intimes, statut de santé ou diagnostic. Une procédure locale de sécurité et une revue d'accessibilité restent à valider par le responsable humain.

**Qualification :** projet d'évaluation interne, à réviser et à tester en contexte réel; aucune certification, homologation ou publication revendiquée.
