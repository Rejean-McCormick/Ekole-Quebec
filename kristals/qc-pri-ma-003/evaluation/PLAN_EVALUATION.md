# Plan d'évaluation — qc-pri-ma-003

**Objectif immuable :** `obj-1` — Décomposer et recomposer des nombres grâce aux valeurs de position.  
**Critère immuable :** `crit-1` — Décomposer un nombre de deux façons puis effectuer un regroupement inverse.  
**Famille unique :** `qc-pri-ma-003-ev-01`. **Statut :** ébauche instrumentée, `a_revoir` (pas qualifiée, non certifiée).

## Planification et couverture

| Item | Liens obligatoires | Difficulté | Représentation | Ce qui varie / sécurité de la réponse |
|---|---|---|---|---|
| `q-001` | obj-1 · crit-1 · qc-pri-ma-003-ev-01 | initial | matériel décrit → notation | fixe 243; échange D/U contrôlé |
| `q-002` | obj-1 · crit-1 · qc-pri-ma-003-ev-01 | initial | tableau C-D-U | fixe 305 avec zéro dizaine; échange C/D |
| `q-003` | obj-1 · crit-1 · qc-pri-ma-003-ev-01 | intermédiaire | groupes et notation | paramétrique DU, seed 3003, domaines bornés |
| `q-004` | obj-1 · crit-1 · qc-pri-ma-003-ev-01 | intermédiaire | non canonique → notation | fixe 471; inverse C/D |
| `q-005` | obj-1 · crit-1 · qc-pri-ma-003-ev-01 | intermédiaire | analyse d'erreur | fixe 402; zéro et correction |
| `q-006` | obj-1 · crit-1 · qc-pri-ma-003-ev-01 | intermédiaire | plaques/bandes → notation | paramétrique CD, seed 6006 |
| `q-007` | obj-1 · crit-1 · qc-pri-ma-003-ev-01 | transfert | livres en caisses/boîtes → écriture | fixe/scénario contrôlé, M1 obligatoire |
| `q-008` | obj-1 · crit-1 · qc-pri-ma-003-ev-01 | transfert | tesselles en plaques/bandes → écriture | fixe/scénario contrôlé, M2 obligatoire |
| `q-009` | obj-1 · crit-1 · qc-pri-ma-003-ev-01 | transfert | réserve de lots → notation | paramétrique CD, seed 9012 |
| `q-010` | obj-1 · crit-1 · qc-pri-ma-003-ev-01 | transfert | notation/tactile | fixe 100, cas limite avec zéros |

**Couverture totale :** 10 tâches, 2 initiales, 4 intermédiaires, 4 de transfert; 3 paramétriques, 5 fixes, 2 scénarios contrôlés. Les dix font produire deux formes et leur inverse; U/D, D/C, zéro de position, non canonique, erreur, cas limite et deux contextes sont effectivement mobilisés. Les deux **manifestations autonomes distinctes** sont M1=`q-007` (bibliothèque; C/D) et M2=`q-008` (mosaïque; D/U), à administrer à des moments distincts sans suggestion mathématique.

## Critères et score descriptif

Chaque item relève des quatre dimensions identiques de [GRILLE_MAITRISE.md](GRILLE_MAITRISE.md) : 1. quantité/positions exactes; 2. deux décompositions distinctes et égales; 3. échange inverse qui revient à la forme de départ; 4. justification mathématique observable. Chacune est annotée 0 / 1 / 2; le total indicatif sur 8 ne suffit **jamais** à conclure à la maîtrise. En M1 et M2, les **quatre dimensions doivent valoir 2 pour chacune**, sans indice de calcul; un nouvel essai après aide est formatif et ne remplace pas une preuve autonome.

## Règles paramétriques reproductibles

- **Aucune génération IA libre.** Instance entière calculée par le système mathématique local `positions-ma003-1.0` : `mod` = reste euclidien, `div` = division entière, seed entier non négatif. Les domaines et la formule exacts figurent dans `BANQUE_ITEMS.json` pour chaque item paramétrique. Pour DU, `H=1+(s mod 7)`, `T=1+((s div 7) mod 8)`, `U=(s div 56) mod 10`; pour CD, `H=1+(s mod 6)`, `T=(s div 6) mod 10`, `U=(s div 60) mod 10`. Parenthèses et priorité tels qu'explicités dans la banque.
- **Solution DU :** `100H+10T+U` = `100H + 10(T−1) + (U+10)`; retour par `10 U → 1 D`, T ≥ 1.
- **Solution CD :** `100H+10T+U` = `100(H−1) + 10(T+10) + U`; retour par `10 D → 1 C`, H ≥ 1.
- Les seeds fixes `3003`, `6006`, `9012` identifient des instances publiables **seulement après revue**. Chaque paramètre contient 3 exemples d'instanciation, dont la graine de l'item, pour reproduction; essais calculés par un second chemin arithmétique dans les tests locaux. La banque contient réponses exactes et contraintes, pas une garantie d'exécution de solveur distant.
- **Variation admise à l'édition future :** seed entier non négatif et contexte de vocabulaire équivalent parmi ceux explicités; tout changement exige nouveau calcul et revue de la consigne/correction. Rejeter groupes négatifs, valeur hors domaine, nombre de chiffres inattendu, seconde forme identique, ou inverse qui ne retrouve pas les trois composantes d'origine.

## Administration, sécurité et accessibilité

- Présenter un item à la fois; lecture audio neutre, caractères agrandis, C-D-U tactile ou matériel de base dix admis; décrire intégralement les stimuli en texte. Le choix de l'échange est parfois prescrit **dans la consigne** pour contrôler la tâche, mais aucune aide additionnelle n'est fournie pour M1/M2.
- Vérifier **individuellement** chaque preuve; ne pas observer un pair et attribuer sa réponse à l'élève. Aucune vitesse, orthographe, qualité esthétique ou coût de matériel dans le barème.
- Privilégier papier ou jetons volumineux appropriés; éviter petits objets pour personnes exposées à un risque d'ingestion. Aucune donnée privée n'est nécessaire. Adaptation d'accès ≠ indice mathématique : noter séparément.
- Vérification humaine encore requise : lisibilité des scénarios, équité du vocabulaire « caisses/boîtes/tesselles », pilote d'élèves, audit d'intégration LMS et validation des options de variantes avant usage sommatif.
