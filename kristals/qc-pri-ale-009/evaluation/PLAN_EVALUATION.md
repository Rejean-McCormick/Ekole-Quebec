# Plan d'évaluation — qc-pri-ale-009

**Objectif immuable `obj-1` :** Orthographier et ponctuer des phrases anglaises ciblées. **Critère immuable `crit-1` :** Corriger un message en repérant et justifiant les corrections. **Famille :** `qc-pri-ale-009-ev-01`, type natif `réponse_argumentée`.

## Couverture item par item

| Item | Objectif | Critère | Famille | Difficulté | Représentation | Catégories sollicitées | Variabilité |
|---|---|---|---|---|---|---|---|
| `qc-pri-ale-009-q-001` | `obj-1` | `crit-1` | `qc-pri-ale-009-ev-01` | initial | phrase | C | Énoncé fixe |
| `qc-pri-ale-009-q-002` | `obj-1` | `crit-1` | `qc-pri-ale-009-ev-01` | initial | phrase | S / P | Énoncé fixe |
| `qc-pri-ale-009-q-003` | `obj-1` | `crit-1` | `qc-pri-ale-009-ev-01` | initial | phrase | C / S | Énoncé fixe |
| `qc-pri-ale-009-q-004` | `obj-1` | `crit-1` | `qc-pri-ale-009-ev-01` | intermediaire | phrase | C / S / P | Énoncé fixe |
| `qc-pri-ale-009-q-005` | `obj-1` | `crit-1` | `qc-pri-ale-009-ev-01` | intermediaire | phrase | C | Énoncé fixe |
| `qc-pri-ale-009-q-006` | `obj-1` | `crit-1` | `qc-pri-ale-009-ev-01` | intermediaire | phrase | C / P | Énoncé fixe |
| `qc-pri-ale-009-q-007` | `obj-1` | `crit-1` | `qc-pri-ale-009-ev-01` | intermediaire | phrase | C / S | Énoncé fixe |
| `qc-pri-ale-009-q-008` | `obj-1` | `crit-1` | `qc-pri-ale-009-ev-01` | intermediaire | deux phrases | S / C / P | Énoncé fixe |
| `qc-pri-ale-009-q-009` | `obj-1` | `crit-1` | `qc-pri-ale-009-ev-01` | transfert | message multiligne | C / S / P | Scénario figé, aucune permutation |
| `qc-pri-ale-009-q-010` | `obj-1` | `crit-1` | `qc-pri-ale-009-ev-01` | transfert | message multiligne | C / S / P | Scénario figé, aucune permutation |

**Couverture intentionnelle :** orthographe `ai` (`train`), `ay` (`play`), suppression du `e` muet devant `-ing` (`making`, `writing`, `smiling`); majuscules de début de phrase, `I`, prénom, jour; point et point d'interrogation. Les huit premiers items servent à repérer et entraîner; les **items 009 (bibliothèque) et 010 (projet de jardin)** sont les deux manifestations distinctes de maîtrise, chacune intégrant S/C/P et une justification.

## Modalité et barème

1. Fournir le texte **erroné** et la consigne, non le corrigé; faire produire une version intégrale, le repérage et les raisons des corrections.
2. Compter les changements ciblés exactement selon `BANQUE_ITEMS.json` : 009 = **8** (5 C, 2 S, 1 P); 010 = **10** (7 C, 2 S, 1 P). Compter indépendamment une majuscule et le point final, même si la cible est dans le dernier mot. Vérifier les justifications S, C et P en contexte.
3. Pour chaque preuve, seuil d'exactitude des changements ciblés **≥ 80 %**, présence d'au moins une correction adéquate par S/C/P, aucune surcorrection qui modifie le sens, et justification pertinente de **chaque** catégorie. Les deux preuves doivent atteindre les seuils, pas leur moyenne.
4. Absence de guidage, d'autocorrecteur et d'aide rédactionnelle proposant les réponses. Les aides d'accès (lecture du texte, gros caractères, clavier adapté, dictée fidèle) demeurent possibles si elles ne font pas les choix linguistiques.
5. Examiner aussi les explications : la maîtrise **n'est pas déduite d'un seul total**. Appliquer la grille `GRILLE_MAITRISE.md`; insuffisance → remédiation ciblée → nouvelles preuves dans deux contextes non mémorisés.

## Difficultés et sécurité / accessibilité

- **Initial (001–003) :** un ou deux types de changements, textes courts.
- **Intermédiaire (004–008) :** une transformation orthographique et plusieurs conventions; deux phrases pour 008.
- **Transfert (009–010) :** messages authentiques fictifs (bibliothèque et projet de jardin), plusieurs lignes, autonomie intégrale et justification.
- Aucune donnée d'élève réel, aucun partage externe, aucun contenu sensible; les prénoms sont fictifs. Affichage texte non coloré, compatible lecteur d'écran; alternatives de saisie fidèles, sans reconnaissance automatique qui ponctuerait ou capitaliserait à la place de l'élève. Durée souple et consignes réexpliquées sans livrer le corrigé.

## Variations et contrôle

- 001–008 : `fixe`, stimuli et solutions verrouillés.
- 009–010 : `scenario_controle` avec **une seule version approuvée dans la banque** par scénario; `parametres=null`, `seed=null`. Toute variation exige un nouvel item, une nouvelle justification, un corrigé révisé et une validation humaine : aucun tirage libre par IA.
- État de tous les items : `a_revoir`. La correction localement contrôlée n'est ni une certification, ni une validation d'usage sommatif.
