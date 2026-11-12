# Plan d’évaluation — qc-pri-ma-002 (v1.2)

**Ancrage immuable :** `obj-1` = Lire, écrire, ordonner et comparer des nombres naturels dans un champ adapté. `crit-1` = Placer et comparer des nombres en expliquant le critère de comparaison. Famille `qc-pri-ma-002-ev-01`; **mode privilégié natif `paramétrique_controle`**.

## Table de traçabilité complète

| Item | Objectif | Critère | Famille | Niveau | Représentation | Couverture | Mode |
|---|---|---|---|---|---|---|---|
| `qc-pri-ma-002-q-001` | `obj-1` | `crit-1` | `qc-pri-ma-002-ev-01` | initial | chiffres + positions | lire/écrire/décomposer | fixe |
| `qc-pri-ma-002-q-002` | `obj-1` | `crit-1` | `qc-pri-ma-002-ev-01` | initial | tableau M/C/D/U | composer + zéro | paramétrique compose |
| `qc-pri-ma-002-q-003` | `obj-1` | `crit-1` | `qc-pri-ma-002-ev-01` | initial | deux cartes | première différence centaines | paramétrique hundreds |
| `qc-pri-ma-002-q-004` | `obj-1` | `crit-1` | `qc-pri-ma-002-ev-01` | intermediaire | quatre cartes | ordre croissant et justification | fixe |
| `qc-pri-ma-002-q-005` | `obj-1` | `crit-1` | `qc-pri-ma-002-ev-01` | intermediaire | 3 chiffres/4 chiffres | comparaison de longueur | paramétrique digits |
| `qc-pri-ma-002-q-006` | `obj-1` | `crit-1` | `qc-pri-ma-002-ev-01` | intermediaire | droite graduée | encadrement entre centaines | paramétrique between |
| `qc-pri-ma-002-q-007` | `obj-1` | `crit-1` | `qc-pri-ma-002-ev-01` | intermediaire | relations symboliques | égalité et comparaison | fixe |
| `qc-pri-ma-002-q-008` | `obj-1` | `crit-1` | `qc-pri-ma-002-ev-01` | intermediaire | trois cartes | ordre croissant/décroissant | paramétrique order3 |
| `qc-pri-ma-002-q-009` | `obj-1` | `crit-1` | `qc-pri-ma-002-ev-01` | transfert | bibliothèque fictive / flèche | preuve autonome 1 | paramétrique shelf |
| `qc-pri-ma-002-q-010` | `obj-1` | `crit-1` | `qc-pri-ma-002-ev-01` | transfert | inventaire fictif / tableau M-C-D-U | preuve autonome 2 | paramétrique inventory |

## Couverture et décision

- **Numération / lecture et écriture :** q-001, q-002, q-010 ; **relation des symboles :** q-003, q-005, q-007 ; **ordre :** q-004, q-008, q-009, q-010 ; **placement :** q-006, q-009 ; **justifications :** toutes les tâches de comparaison.
- **Niveaux :** 3 initiaux, 5 intermédiaires, 2 transferts; ce classement n'est pas une assignation d'année scolaire.
- **Deux preuves de maîtrise :** q-009 (étiquettes de bibliothèque, flèche croissante non nécessairement équidistante) et q-010 (codes d'inventaire, ordre et tableau de position), à administrer de manière autonome. q-009 et q-010 doivent réussir **séparément**, avec explications; une note moyenne ne suffit pas.
- **Règle de correction :** comparaisons entières exactes, ordres contrôlés, décomposition de positions reconstituée. La justification doit comparer les longueurs significatives ou le **premier rang différent**, ou présenter une décomposition arithmétique équivalente.

## Variabilité strictement permise

- Sept items `parametrique`, seed entière stable s dans [0,8 999], formules, domaines, affichage et exemples conservés **item par item dans BANQUE_ITEMS.json**. **Aucun tirage IA.** Un même s régénère un résultat identique. Trois items fixes avec seed et paramètres nuls.
- Une paire d'instances à même structure mais seeds différentes peut renforcer le contrôle; elle ne remplace pas l'indépendance des deux contextes.
- Contrôles numériques : recomposition à partir des rangs, comparaisons `<`, `>`, `=`, encadrement strict et tri d'entiers; vérifier toutes les seeds avant usage. Les démonstrations sont seulement des exemples, pas des preuves finales.

## Rubrique, accès et sécurité

- Quatre dimensions observables de 0 à 2 : **représenter le nombre**; **classer et placer**; **symboliser et justifier la comparaison**; **agir de façon autonome et transférer**. Se référer à `GRILLE_MAITRISE.md` pour la décision sur chaque contexte.
- Présentation accessible : nombres en gros caractères, lecture des consignes, signes agrandis, tableau M/C/D/U tactile, objets de base dix; expliquer par dictée ou communication assistée lorsque cela conserve l'objectif de lecture/écriture et la compréhension de valeur de position.
- **Sécurité et éthique :** données fictives sans déplacement physique ni information personnelle; pas de pénalité sur la vitesse, graphie manuscrite ou langage oral si la même compétence numérique est observable; assurer confidentialité de la trace.
- **Limites :** contrôle arithmétique automatisé des corrigés ≠ validation pédagogique ou d'accessibilité avec des élèves. Tous les items portent `validation_status=a_revoir` ; aucune certification, approbation PFEQ ou examen sommatif qualifié.
