# PLAN D’ÉVALUATION — `qc-pri-ma-018`

**Objectif `obj-1` :** Établir et expliquer des égalités ou relations numériques correctes.  
**Critère `crit-1` :** Compléter des égalités ouvertes en explicitant la relation choisie.  
**Famille :** `qc-pri-ma-018-ev-01` · **Mode de référence :** `paramétrique_controle` (cinq gabarits et cinq items fixes).

## Table de couverture et critères

| Item | Obj. | Crit. | Famille | Difficulté | Représentation | Relation évaluée | Preuve |
|---|---|---|---|---|---|---|---|
| `001` | `obj-1` | `crit-1` | `qc-pri-ma-018-ev-01` | initial | notation_symbolique | egalite_additive | non |
| `002` | `obj-1` | `crit-1` | `qc-pri-ma-018-ev-01` | initial | schema_en_barres_et_notation | compensation_addition | non |
| `003` | `obj-1` | `crit-1` | `qc-pri-ma-018-ev-01` | initial | notation_symbolique | inconnue_a_gauche | non |
| `004` | `obj-1` | `crit-1` | `qc-pri-ma-018-ev-01` | intermediaire | notation_symbolique | partie_manquante | non |
| `005` | `obj-1` | `crit-1` | `qc-pri-ma-018-ev-01` | intermediaire | notation_symbolique | reparation_egalite | non |
| `006` | `obj-1` | `crit-1` | `qc-pri-ma-018-ev-01` | intermediaire | droite_graduee_et_notation | soustraction_quantite_retiree | non |
| `007` | `obj-1` | `crit-1` | `qc-pri-ma-018-ev-01` | transfert | materiel_jetons_et_equation | plateaux_jetons | oui, plateaux_jetons |
| `008` | `obj-1` | `crit-1` | `qc-pri-ma-018-ev-01` | transfert | situation_textuelle_et_equation | jardin_recoltes | oui, jardin_recoltes |
| `009` | `obj-1` | `crit-1` | `qc-pri-ma-018-ev-01` | transfert | notation_et_schemas_equivalents | equivalence_par_meme_ajout | non |
| `010` | `obj-1` | `crit-1` | `qc-pri-ma-018-ev-01` | transfert | notation_et_bandes | compensation_diminution | non |

Tous les items exigent au moins le **résultat** et une **justification de relation**, suivis de la **vérification par substitution**. `q-008` ajoute l’écriture de l’égalité issue du texte. Les `q-007` et `q-008` sont les deux manifestations de maîtrise dans deux contextes disjoints; utiliser sur des occasions séparées, sans indice de contenu ni accès au corrigé.

## Réponses, poids et règle de jugement

- Corrigés et rétroactions complets : `BANQUE_ITEMS.json`; aucune réponse n’est validée uniquement par IA. Pour les paramètres, calculer la solution par l’algorithme spécifié et contrôler les deux membres indépendamment.
- Chaque preuve de maîtrise : 3 dimensions jugées séparément (exactitude, relation explicite, vérification). Sur `q-008`, la modélisation de la situation par une égalité vraie est également indispensable.
- Pour les deux preuves : **satisfaisant** signifie case juste, explication valide des relations et deux membres effectivement contrôlés, sans aide de contenu. Aucune moyenne ou somme des autres items ne compense l’absence d’une de ces dimensions.
- Les items `q-001` à `q-006`, `q-009`, `q-010` servent à la formation, aux variantes et à la reprise; si un élève échoue à une preuve, proposer un nouveau scénario comparable à valider avant usage, pas le même item mémorisé.

## Génération et limites de variation

- Modes fixes `q-001`, `q-003`, `q-005`, `q-007`, `q-008` : énoncés, réponses, contextes et critères verrouillés; aucune substitution improvisée. Scénarios de maîtrise contrôlés, contexte fictif.
- Modes paramétriques `q-002`, `q-004`, `q-006`, `q-009`, `q-010` : domaines finis, formules de quotients/reste (`seed // n`, `seed % n`), seed stable et exemple calculé dans `items[].parametres`. Chaque instance suit le même contrat et conserve un résultat entier non négatif et unique.
- **Un générateur n’est pas déployé** par ce document JSON : toute implémentation future doit produire exactement les instances de référence, tester exhaustivement les domaines et journaliser le seed. Modifier les domaines ou les textes requiert une nouvelle revue.
- Une solution algébrique exacte n’est pas suffisante si l’élève n’explique pas la relation choisie; une explication vague sans contrôle de l’égalité reste insuffisante.

## Accessibilité et équité

- Les signes `+`, `−`, `=` et `□` doivent être lisibles et expliqués; un lecteur d’écran peut lire « case à remplir ». Utiliser des descriptions textuelles des schémas; ne jamais coder des quantités par une couleur seule.
- Fournir jetons/dessins/barres si nécessaires; autoriser justification orale transcrite, écrite ou schématisée sans changer les trois exigences mathématiques. Pas de pénalité de vitesse, écriture ou orthographe.
- Les contextes de plateaux et de jardin sont fictifs et ne requièrent aucune connaissance extérieure; vérifier compréhension lexicale, sans donner la stratégie numérique.
- Calculatrice non requise pour les petits nombres; si adaptation accordée, la justification de la relation et la vérification par substitution restent exigées.

## Sécurité, droits, statut et contrôle

- Aucun contenu violent, donnée personnelle ou collecte de croyances. Supports numériques utilisables hors ligne.
- Textes et schémas descriptifs originaux produits pour ce Kristal; aucune figure tierce incorporée. Les fichiers de gouvernance sont cités comme normes internes, non reproduits dans le ZIP.
- Chaque item porte `validation_status: a_revoir`. Les calculs de domaines sont contrôlés techniquement; la revue humaine des rubriques, des niveaux de difficulté, du langage et des adaptations est **à faire**.
- Le verdict de maîtrise est consigné en contexte d’évaluation seulement, jamais inscrit au canon du Kristal.
