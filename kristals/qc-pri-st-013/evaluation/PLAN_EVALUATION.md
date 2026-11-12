# Plan d’évaluation — `qc-pri-st-013`

**Objectif immuable `obj-1` :** Comparer roches et sols à partir de caractéristiques observables.  
**Critère immuable `crit-1` :** Établir un tableau comparatif d’échantillons sans risque.  
**Famille native :** `qc-pri-st-013-ev-01` · `type: generee_sous_contraintes` · `validation_status: a_revoir`.

## Cible et conditions

L'élève compare des fiches d’échantillons **fictifs** (ou des objets propres scellés préparés par l’adulte) : structure/cohésion, granularité visible, traces organiques et limites des observations. Un tableau de comparaison, deux différences ou ressemblances justifiées, et une prudence sur l’inconnu constituent les traces. On n’évalue ni la capacité de manier un tamis ni l’identification précise des minéraux, ni le PFEQ.

**Avant la preuve :** diagnostic D1/D2, enseignement M/N, guidage G1–G3, autonomie A1–A4; corriger avant d’évaluer sans souffler le contenu des deux épreuves de maîtrise. Lecture des données, tableau agrandi, dictée fidèle ou synthèse vocale autorisés; pas d’aide sur le raisonnement.

## Cartographie exhaustive de la banque

Tous les items `q-001` à `q-010` ont **objectif `obj-1`, critère `crit-1`, famille `qc-pri-st-013-ev-01`**; le tableau précise l’usage, le niveau et la représentation.

| Item | Niveau | Mode | Représentation et opération | Évidence spécifique |
|---|---|---|---|---|

| `qc-pri-st-013-q-001` | initial | fixe | fiche textuelle, observation/inférence | séparer donnée et histoire supposée |
| `qc-pri-st-013-q-002` | initial | fixe | terminologie et échelle | quatre définitions, relief ≠ rugosité |
| `qc-pri-st-013-q-003` | initial | fixe | deux fiches de sols | granularité qualitative, limite de mesure |
| `qc-pri-st-013-q-004` | intermediaire | scenario_controle | 2 fiches roche/sol, tableau | 3 critères comparables et limite |
| `qc-pri-st-013-q-005` | intermediaire | fixe | deux sols, tableau | similitude, différence, « non indiqué » |
| `qc-pri-st-013-q-006` | intermediaire | fixe | paysage décrit, sol | relief ≠ propriétés de sol, hypothèse |
| `qc-pri-st-013-q-007` | intermediaire | fixe | deux affirmations abusives | couleur seule insuffisante |
| `qc-pri-st-013-q-008` | transfert | scenario_controle | 2 protocoles fictifs | procédure sûre de substitution |
| `qc-pri-st-013-q-009` | transfert | fixe | jardin, trois fiches et tableau | preuve 1 : ≥3 critères, 2 comparaisons, limite |
| `qc-pri-st-013-q-010` | transfert | fixe | sentier, trois fiches et tableau | preuve 2 : ≥3 critères, 2 comparaisons, limite |

## Barème descriptif et conditions de maîtrise

- Items 001–008 : formatifs, chaque `criteres` de la banque s’applique à la correction; feedback descriptif et essai corrigé; ne pas inférer la maîtrise d’un cumul de bonnes réponses.
- Items 009–010 : deux manifestations **séparées**, q-009 au jardin scolaire, q-010 sur un sentier municipal. Ils ne partagent pas les données ni la réponse. Cinq dimensions `C1–C5` détaillées dans `GRILLE_MAITRISE.md`. Évaluation critériée, pas pourcentage unique.
- Couverture : roche (002/004/007/009/010), sol (002/003/004/005/009/010), granulométrie (002/003/004/005/009/010), relief (002/006/010), observation/inférence (001/006/007/009/010), sécurité (008/009/010), tableau comparatif (004/005/009/010). Les deux épreuves comportent chacune trois fiches et un tableau complet.

## Variabilité, reproductibilité et sécurité

- Items **fixes** : stimulus et corrigé entièrement verrouillés; aucun tirage libre.
- `q-004` et `q-008` : **scénarios contrôlés** du corpus *deux variantes a/b* explicitement rédigées et corrigées dans `parametres.variantes`; algorithme entier `index = seed % 2`; `index 0 → a`, `index 1 → b`. Sources de variantes fictives. Seeds 13004/13005 et 13008/13009; les versions affichées dans `stimulus`/`reponse_attendue` correspondent à 13004 et 13008. Contrôle des variantes exécuté par script de livraison et consigné dans `../livraison/VALIDATION.md`. On ne fabrique pas de nouvelles combinaisons hors de ce corpus.
- Les **deux preuves** ne varient pas pendant la revue initiale; n’autoriser leur substitution qu’après validation d’équivalence par un humain (même difficulté, informations suffisantes, mêmes critères).
- Ne jamais utiliser de LLM comme générateur ou correcteur auto-validant. Examiner les réponses équivalentes par la grille; ne pas imposer une orthographe parfaite si la comparaison scientifique est claire.
- **Sécurité :** observations de descriptions textuelles, sans récolte, poussière, grattage, goût, odeur ou manipulation de terre libre. En cas d'échantillons matériels, nettoyage/préparation/sécurisation par un adulte et maintien sous couvercle transparent. Fiches seules = solution toujours valide.
- **Accessibilité :** textes lisibles par lecteur d’écran, sens jamais codé uniquement par couleur, versions orales à données identiques, tableaux accessibles au clavier, réponse dictée ou enregistrée. Respecter temps additionnel si nécessaire, sans indices sur le contenu.
- **Contrôle humain requis :** exactitude des scénarios, faisabilité de la grille, jugement d’équivalence et sécurité en classe. Aucun examen certifié, aucune homologation PFEQ.
