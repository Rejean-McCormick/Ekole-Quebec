# Plan d'évaluation — qc-pri-ap-002

**Objectif IMMUTABLE `obj-1` :** Expérimenter des gestes, supports et procédés plastiques de façon sûre.  
**Critère IMMUTABLE `crit-1` :** Produire une planche d’essais légendée et comparer les effets.  
**Famille IMMUTABLE :** `qc-pri-ap-002-ev-01` · **Mode privilégié :** `observation_ou_production`.

## Table d'alignement complète

| Item | Objectif | Critère | Famille | Difficulté | Représentation | Couverture principale |
|---|---|---|---|---|---|---|
| `q-001` | `obj-1` | `crit-1` | `qc-pri-ap-002-ev-01` | initial | court essai au crayon et légende | reconnaissance outil/geste/technique/trace |
| `q-002` | `obj-1` | `crit-1` | `qc-pri-ap-002-ev-01` | initial | deux bandes sur papier | densité, espacement et observation |
| `q-003` | `obj-1` | `crit-1` | `qc-pri-ap-002-ev-01` | intermediaire | deux cases de hachures | orientation et variable unique |
| `q-004` | `obj-1` | `crit-1` | `qc-pri-ap-002-ev-01` | intermediaire | feutre/carton, points vs traits | forme des traces et geste |
| `q-005` | `obj-1` | `crit-1` | `qc-pri-ap-002-ev-01` | intermediaire | deux supports et crayon de cire | support, régularité/absence de différence |
| `q-006` | `obj-1` | `crit-1` | `qc-pri-ap-002-ev-01` | intermediaire | situation fictive + reprise matérielle | comparaison avec facteurs contrôlés |
| `q-007` | `obj-1` | `crit-1` | `qc-pri-ap-002-ev-01` | intermediaire | six marques courtes/longues | amplitude et longueur de trace |
| `q-008` | `obj-1` | `crit-1` | `qc-pri-ap-002-ev-01` | intermediaire | pointillage sur carton | espacement et répétition |
| `q-009` | `obj-1` | `crit-1` | `qc-pri-ap-002-ev-01` | transfert | recherche pour marque-page | intention et changement volontaire |
| `q-010` | `obj-1` | `crit-1` | `qc-pri-ap-002-ev-01` | transfert | planche croisée 2 × 2 | comparaison d’une paire et limites |
| `q-011` | `obj-1` | `crit-1` | `qc-pri-ap-002-ev-01` | transfert | planche d’affiche en quatre cases — M1 | preuve autonome A : gestes, traces et comparaisons |
| `q-012` | `obj-1` | `crit-1` | `qc-pri-ap-002-ev-01` | transfert | planche de signet sur deux papiers — M2 | preuve autonome B : gestes × supports et limites |

Les épreuves `q-001` à `q-010` sont formatives/entraînement avec feedback. Les épreuves `q-011` et `q-012` sont deux manifestations de maîtrise indépendantes, sans indices cognitifs et avec des contextes matériels distincts. Les 12 consignes, stimuli, réponses observables et limitations de substitution sont conservés intégralement dans `BANQUE_ITEMS.json`.

## Couverture du parcours et poids de décision

- **Outil, geste, technique, trace :** `q-001`, `q-003`, `q-004`, `q-007`, `q-011`.
- **Comparer et expliquer les effets :** `q-002`, `q-005`, `q-008`, `q-009`, `q-010`, `q-011`, `q-012`.
- **Variation maîtrisée et interprétation prudente :** `q-002`, `q-003`, `q-005`, `q-006`, `q-010`, `q-012`.
- **Transfert créatif et démarche plutôt que goûts :** `q-009`, `q-010`, `q-011`, `q-012`.
- **Sécurité :** observée dans TOUS les items matériels; constat d'incident → arrêt, correction et nouvelle observation.

Aucun total de points unique ne décide la maîtrise. Les deux preuves finales sont examinées individuellement avec la grille `GRILLE_MAITRISE.md`, chacune devant satisfaire les seuils. On ne transforme pas une somme des items formatifs en « cours réussi ». Aucun jugement sur talent, élégance, style, goût ni vitesse manuelle.

## Protocoles de passation et accessibilité

- Responsable vérifie chaque matériel, son étiquette et l'environnement **avant** la passation; fournitures scolaires adaptées, papier propre à bords non coupants. Aucun aérosol, outil tranchant, solvant, produit chauffant, pigment pulvérulent ou produit non identifié. Exclure tout matériel inadapté à une sensibilité connue. L'usage d'un produit avec sceau ACMI AP peut aider au choix, mais sa disponibilité n'est pas un critère de réussite scolaire.
- L'élève peut utiliser une aide de préhension, une feuille fixée, un temps de pause, une dictée de légendes, un support de communication alternatif et un outil accessible. Consigner la nature de l'aide. Le responsable ne doit pas choisir les gestes, énoncer les comparaisons ni produire les légendes en lieu et place de l'élève.
- Traces photographiques seulement avec consentement/politique locale; planche papier seule suffit. Une évaluation formative ne requiert pas de collecte biométrique ni d'informations sensibles.
- Les résultats visuels peuvent varier selon matériaux et capacités; les modèles de réponse donnent des **propriétés à vérifier**, non des œuvres à imiter. Une observation honnête d'absence de contraste est recevable lorsqu'elle est justifiée.
- Suspension de passation si l'environnement ou les fournitures ne sont pas sûrs; une adaptation nécessitant une substitution importante est **revue** avant réutilisation; ne jamais attribuer automatiquement « maîtrise » à un simple dessin numérique sans gestes/choix/effets observables.

## Génération et variabilité permise

- `q-001` à `q-012` sont des **scénarios contrôlés et documentés**, non des données tirées aléatoirement; `seed: null`, `parametres: null`, aucune variation paramétrique prétendue ni IA libre correctrice.
- Variations uniquement de **forme d'accès** : dimension du papier, moyens de communication, prise adaptée, substitution matérielle approuvée conservant les gestes comparables. L'item `q-012` exige **deux supports distincts** même en accessibilité. Aucun ajout de scénario, couleur ou propriété matérielle sans vérifier faisabilité et critères.
- Les exemples de réponse ne sont pas des attentes matérielles garanties : l'observateur compare la **trace véritable** à la description de l'élève.
- Le niveau et le contexte sont **verrouillés** par item. Relecture humaine requise pour biais, sécurité, compatibilité du matériel et clarté de la grille avant tout examen sommatif.

## Consignation et décision

Pour chaque item : date, identification, matériau précis validé, durée/aménagements, observations sur la sécurité et la trace, niveau par dimension, rétroaction. Pour `q-011` et `q-012`, archiver **deux décisions distinctes**; si une preuve est insuffisante, remédier à l'élément concerné et obtenir une nouvelle production autonome dans un contexte analogue mais non identique. Aucun statut « certifié » ni homologation scolaire.
