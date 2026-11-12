# Plan d'évaluation — `qc-pri-ma-032`

**Objectif principal immuable (`obj-1`) :** Décrire des événements en termes de possibilité et de chance relative.  
**Preuve immuable (`crit-1`) :** Classer des événements et expliquer les conditions du classement.  
**Famille immuable :** `qc-pri-ma-032-ev-01` (mode privilégié `paramétrique_controle`).

## Validité et couverture

Le plan vérifie dans différentes représentations : (1) zéro/toutes/quelques issues favorables, (2) chance relative strictement plus grande/plus petite/égale, (3) distinction probable / certain et improbable / impossible, (4) rôle de l'équiprobabilité, (5) justification des conditions, (6) transfert sans indices. **Tous les items** sont liés simultanément à `obj-1`, `crit-1` et `qc-pri-ma-032-ev-01`.

| Item | Objectif | Critère | Famille | Difficulté | Représentation | Couverture spécifique | Mode |
|---|---|---|---|---|---|---|---|
| `qc-pri-ma-032-q-001` | `obj-1` | `crit-1` | `qc-pri-ma-032-ev-01` | initial | objets_et_tableau | Sac R/B : majorité, rareté, impossible, certain; effectifs explicités | parametrique |
| `qc-pri-ma-032-q-002` | `obj-1` | `crit-1` | `qc-pri-ma-032-ev-01` | initial | tableau_d_effectifs | Boîte A/B équilibrée : égalité des chances, zéro, totalité | parametrique |
| `qc-pri-ma-032-q-003` | `obj-1` | `crit-1` | `qc-pri-ma-032-ev-01` | initial | cases_et_denombrement | Sac uniforme L : certitude et impossibilité malgré le hasard du jeton | parametrique |
| `qc-pri-ma-032-q-004` | `obj-1` | `crit-1` | `qc-pri-ma-032-ev-01` | intermediaire | objets_et_comparaison | Tickets T/S : faible chance non nulle, rareté, majorité | parametrique |
| `qc-pri-ma-032-q-005` | `obj-1` | `crit-1` | `qc-pri-ma-032-ev-01` | intermediaire | roue_textuelle_a_secteurs_egaux | Roue P/O : majorité parmi secteurs égaux, issue absente | parametrique |
| `qc-pri-ma-032-q-006` | `obj-1` | `crit-1` | `qc-pri-ma-032-ev-01` | intermediaire | roue_et_tableau | Roue M/N : chances égales, impossible, certain | parametrique |
| `qc-pri-ma-032-q-007` | `obj-1` | `crit-1` | `qc-pri-ma-032-ev-01` | transfert | ensemble_numerique_et_comptage | Cartes numérotées : événements construits par propriétés numériques | parametrique |
| `qc-pri-ma-032-q-008` | `obj-1` | `crit-1` | `qc-pri-ma-032-ev-01` | transfert | tableau_a_trois_categories | Trois étiquettes : comparaison et univers entier sans catégorie D | parametrique |
| `qc-pri-ma-032-q-009` | `obj-1` | `crit-1` | `qc-pri-ma-032-ev-01` | initial | critique_d_une_affirmation | Critique : très probable ne signifie pas certain | fixe |
| `qc-pri-ma-032-q-010` | `obj-1` | `crit-1` | `qc-pri-ma-032-ev-01` | transfert | sac_de_jetons_et_argumentation | PREUVE A : sac de classe, 4 catégories et comparaison | fixe |
| `qc-pri-ma-032-q-011` | `obj-1` | `crit-1` | `qc-pri-ma-032-ev-01` | transfert | roue_equitable_et_argumentation | PREUVE B : roue de jeu, 4 catégories et comparaison | fixe |
| `qc-pri-ma-032-q-012` | `obj-1` | `crit-1` | `qc-pri-ma-032-ev-01` | transfert | cas_limite_secteurs_inegaux | Cas limite de roue : secteurs inégaux, hypothèse explicitée | fixe |

## Procédure d'utilisation

1. **Diagnostic non certificatif** : items 001–003 ou les deux activités `contenu/02_DIAGNOSTIC.md`; n'implique aucun prérequis bloquant.
2. **Contrôle formatif** : items 004–009, avec feedback ciblé et possibilité de correction sur cas changé.
3. **Deux manifestations autonomes** : `q-010` (sac de jetons du local) et `q-011` (roue fictive de jeu) en deux séances ou sur deux supports distincts, sans indice mathématique. Les deux exigeant classement + explication; confronter preuves avec `evaluation/GRILLE_MAITRISE.md`. **Ne pas déduire la maîtrise d'un nombre de bonnes réponses ou d'une moyenne.**
4. **Extension** : `q-012` met en lumière une condition non vérifiée dans les comparaisons fondées sur le nombre de secteurs. L'usage d'angles est une extension guidée : ne pas pénaliser l'élève pour ne pas connaître les angles si ce contenu n'est pas enseigné.

## Barème descriptif, poids et décisions

- **Classement exact** : impossible = 0 cas; certain = totalité des cas; possible non certain = quelques cas. Reconnaître la majorité et l'égalité lorsqu'elles apparaissent.
- **Comparaison justifiée** : compte les cas favorables pour chaque événement sur **le même total** si les chances élémentaires sont égales.
- **Conditions explicites** : explique pourquoi les issues sont accessibles de façon équivalente dans le modèle (jetons identiques après mélange, roue non biaisée à secteurs égaux, cartes de même taille).
- **Autonomie** : pas d'indice de classement ni de correction pendant les deux preuves; l'aide d'accès n'enlève pas l'autonomie.
- **Décision** : les quatre dimensions doivent être satisfaisantes sur chacune des deux preuves, sauf difficulté d'expression sans impact sur la qualité du raisonnement. Le plan fournit des observations, **pas** une note de passage numérique.

## Génération paramétrique contrôlée

- **Huit gabarits** : items 001–008; mode `parametrique`, seeds entières fixes (3201…3208) et listes de domaines finis propres à chaque item. Chaque entrée fournit `variables`, `domaines_discrets_ordonnes`, `contraintes`, `algorithme_de_generation`, `algorithme_de_correction`, `formules`, `variables_instanciees`, `exemples_verifies` et `limites_de_variation`.
- **Algorithme** : décomposition de la seed en bases successives correspondant aux tailles des domaines; aucun appel à un générateur aléatoire ni variation libre d'une IA. Une répétition de tuple sous des seeds distinctes est permise et documentée.
- **Contrôle du sens** : comparaison dans un univers fixe, `N>0`, `0≤k≤N`; tests combinatoires exhaustifs des domaines finis, y compris égalité, événement absent et événement total. La notation fractionnaire est facultative pour l'élève; le correcteur s'appuie sur des valeurs exactes.
- **Variations interdites** : modifier l'équiprobabilité, transformer un tirage simple en succession sans remise, remplacer une roue égale par une roue inégale dans un gabarit paramétrique, introduire un scénario incompris ou une préférence personnelle.
- **Cas fixes** : items 009–012 sans variables ni seed (`null`); pour l'item 012, les angles et les réponses restent figés.

## Accessibilité, équité et sécurité

- Texte descriptif de toutes les cases et effectifs; couleur associée à une lettre, aucune réponse exigeant discrimination visuelle chromatique. Supports manipulables ou agrandis, écran/voix ou réponse orale observée admis.
- Distinguer **aide d'accès** (lecture de consigne, support tactile, transcription) d'**indice conceptuel** (montrer les issues favorables) et noter ce qui a été fourni.
- Situations entièrement fictives sans pari, argent, classement d'élèves, données personnelles ni manipulation dangereuse; ne pas utiliser des résultats d'essais réels comme preuve de la probabilité théorique.
- Révision humaine nécessaire pour lisibilité du vocabulaire, validité des hypothèses, accessibilité en situation et qualité des rubriques, avant toute utilisation sommative. Tous les items `validation_status = a_revoir`.
