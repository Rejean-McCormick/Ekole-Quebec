# Plan d'évaluation | qc-pri-ma-008

**Autorité :** blueprint natif v1.2, famille unique `qc-pri-ma-008-ev-01`. **Objectif :** `obj-1` — Représenter la multiplication comme groupes égaux et calculer des produits. **Critère :** `crit-1` — Résoudre un problème de groupes égaux avec dessin et calcul. **Statut :** banque d'items `a_revoir`; ni certifiée, ni publiée.

## Stratégie et couverture

Le diagnostic D1–D3 est sans note. Les items `q-001` à `q-008`, `q-011`, `q-012` exercent les notions d'itération, groupes égaux/inégaux, tableau et distributivité, avec feedback immédiat. Les items **`q-009` et `q-010` sont les deux preuves autonomes requises**, chacune dans un contexte distinct (atelier et jardin), avec dessin et calcul. L'élève ne voit pas les réponses au moment de produire sa trace; les items complémentaires ne compensent pas un échec sur une preuve essentielle.

## Table de couverture exhaustive

| Item | Alignement immuable | Difficulté | Représentation / notion | Usage | Variabilité permise |
|---|---|---|---|---|---|
| `qc-pri-ma-008-q-001` | `obj-1` / `crit-1` / `qc-pri-ma-008-ev-01` | initial | groupes_et_addition | formative | fixe : aucune |
| `qc-pri-ma-008-q-002` | `obj-1` / `crit-1` / `qc-pri-ma-008-ev-01` | initial | tableau | formative | fixe : aucune |
| `qc-pri-ma-008-q-003` | `obj-1` / `crit-1` / `qc-pri-ma-008-ev-01` | intermediaire | groupes_egaux | formative | parametrique : domaine + seed + calculs documentés dans BANQUE_ITEMS.json |
| `qc-pri-ma-008-q-004` | `obj-1` / `crit-1` / `qc-pri-ma-008-ev-01` | intermediaire | contre_exemple_et_addition | formative | fixe : aucune |
| `qc-pri-ma-008-q-005` | `obj-1` / `crit-1` / `qc-pri-ma-008-ev-01` | intermediaire | distributivite_dessin | formative | fixe : aucune |
| `qc-pri-ma-008-q-006` | `obj-1` / `crit-1` / `qc-pri-ma-008-ev-01` | intermediaire | tableau_et_equivalence | formative | parametrique : domaine + seed + calculs documentés dans BANQUE_ITEMS.json |
| `qc-pri-ma-008-q-007` | `obj-1` / `crit-1` / `qc-pri-ma-008-ev-01` | intermediaire | deux_representations | formative | fixe : aucune |
| `qc-pri-ma-008-q-008` | `obj-1` / `crit-1` / `qc-pri-ma-008-ev-01` | transfert | tableau_distributivite | formative | parametrique : domaine + seed + calculs documentés dans BANQUE_ITEMS.json |
| `qc-pri-ma-008-q-009` | `obj-1` / `crit-1` / `qc-pri-ma-008-ev-01` | transfert | groupes_dessines_calcul_atelier | atelier, preuve A | parametrique : domaine + seed + calculs documentés dans BANQUE_ITEMS.json |
| `qc-pri-ma-008-q-010` | `obj-1` / `crit-1` / `qc-pri-ma-008-ev-01` | transfert | tableau_dessine_calcul_jardin | jardin, preuve B | parametrique : domaine + seed + calculs documentés dans BANQUE_ITEMS.json |
| `qc-pri-ma-008-q-011` | `obj-1` / `crit-1` / `qc-pri-ma-008-ev-01` | intermediaire | contre_exemple_corrige | formative | fixe : aucune |
| `qc-pri-ma-008-q-012` | `obj-1` / `crit-1` / `qc-pri-ma-008-ev-01` | transfert | tableau_distributivite | formative | fixe : aucune |

## Contrat de variation

- Les items `fixe` gardent texte, données, corrigé et critères exacts; `seed: null`, `parametres: null`.
- Les cinq items `parametrique` (`q-003`, `q-006`, `q-008`, `q-009`, `q-010`) documentent dans chaque entrée de banque la **seed**, les formules par quotient entier et modulo, les domaines de chaque variable, les contraintes, la formule de solution, les exemples calculés et l'instance figée visible. L'algorithme n'utilise ni hasard implicite ni sortie IA comme correcteur. Modifier la seed exige de recalculer les réponses, de vérifier dessin/unité et de conserver la trace de la variante utilisée.
- **Autonomie :** `q-009`/`q-010` sont présentés sans amorce graphique ni indication sur le choix des facteurs; possibilité de lecture orale neutre ou de traçage assisté sous dictée exacte, mais non d'aide conceptuelle.
- La correction d'un paramétrique est la multiplication entière `g × n` ou `g × (b+c)`, vérifiée par addition répétée; on inspecte manuellement la correspondance entre les nombres et la langue de chaque histoire.

## Critères et décision

**Barème analytique commun par preuve de maîtrise :** 1 point chacun (1) groupes égaux fidèles au texte; (2) opération avec facteurs interprétés correctement; (3) produit exact **avec unité**; (4) vérification/explication pertinente. Pour **chaque** preuve, 4/4 critères essentiels sont requis sans aide de fond, puis observer si les deux contextes restent corrects. Il ne s'agit pas d'une moyenne ni d'une note officielle. Voir `evaluation/GRILLE_MAITRISE.md`.

**En cas d'erreur :** distinguer groupement, rangées, calcul ou vérification; remédier au maillon fautif et proposer des **nouvelles instances seedées** dans les deux contextes, après revalidation des nombres et corrigés. Les entrées brutes restent `a_revoir` jusqu'à une revue humaine.

## Sécurité, équité, accessibilité, droits

- Objets et scénarios fictifs non dangereux; aucune donnée personnelle, identité, vécu, coûts réels ou jugement de conduite n'entre dans la note.
- Texte simple et lecture orale neutre possible; matériel manipulable, dessin en gros points, tableau tactile ou production structurée sous dictée. L'évaluation porte sur la pensée multiplicative, non la lisibilité de l'écriture ou la finesse motrice.
- Ne pas attribuer la maîtrise sur la seule rapidité ni sur le seul résultat. Ne pas afficher les corrigés à l'élève avant ses tentatives.
- Tous les scénarios, dessins ASCII et textes évaluatifs sont originaux, sans citation d'œuvres protégées. Les références pédagogiques de conception sont distinguées dans `sources/REFERENCES_CONTENU.md`.

## Points de revue humaine

Vérifier la compréhension des consignes chez les élèves visés, la progressivité réelle de la difficulté, la présentation accessible et la qualité diagnostique des distracteurs/contre-exemples avant un examen sommatif ou une diffusion publique. La présente banque ne remplace pas les essais élèves ni le contrôle de publication Framework.
