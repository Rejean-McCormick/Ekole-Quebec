# Plan d'évaluation — `qc-pri-ma-016-ev-01`

**Objectif immuable :** `obj-1` — Comparer et calculer avec des décimaux en utilisant les valeurs de position.  
**Critère immuable :** `crit-1` — Résoudre deux calculs décimaux et justifier la plausibilité des réponses.  
**Famille :** `qc-pri-ma-016-ev-01` ; mode privilégié `paramétrique_controle`. **Statut :** banque locale à revoir, non certifiée.

## Champ évalué et niveaux

- **Sens des nombres** : distinguer unités/dixièmes/centièmes, comparer en considérant les valeurs et non la longueur de la graphie; comprendre les zéros terminaux et l'égalité.
- **Calculs** : aligner les rangs, additionner/soustraire jusqu'à deux décimales avec échanges si nécessaire, garder l'unité et le sens de la situation.
- **Justification** : fournir une estimation chiffrée plausible, un encadrement justifié ou un contrôle inverse cohérent, pas « c'est correct ».
- **Transfert** : résoudre deux opérations successives sans guidage dans des contextes différents; la pertinence de l'opération choisie compte autant que l'algorithme.

## Matrice complète des items

| Item | Objectif / critère / famille | Niveau | Représentation dominante | Mode | Preuve et portée |
|---|---|---|---|---|---|
| `q-001` | `obj-1` / `crit-1` / `qc-pri-ma-016-ev-01` | initial | tableau de rangs | fixe | zéros terminaux, comparaison égale |
| `q-002` | idem | initial | comparaison et centièmes | fixe | distinguer 0,08 de 0,8 |
| `q-003` | idem | initial | contre-exemple et droite | fixe | critiquer comparaison incorrecte |
| `q-004` | idem | intermédiaire | colonnes, addition | paramétrique | calcul, alignement, estimation |
| `q-005` | idem | intermédiaire | colonnes, soustraction | paramétrique | échange, contrôle inverse |
| `q-006` | idem | intermédiaire | contrôle d'erreur | fixe | remédier à un mauvais alignement |
| `q-007` | idem | intermédiaire | comparaison paramétrique | paramétrique | symbole et justification par rang |
| `q-008` | idem | intermédiaire | série calculée fixe | fixe | addition et soustraction en chaîne |
| **`q-009` (P1)** | idem | transfert | prix fictifs, deux opérations | **paramétrique** | **preuve autonome 1 : marché fictif** |
| **`q-010` (P2)** | idem | transfert | distances, deux opérations | **paramétrique** | **preuve autonome 2 : parcours de marche fictif** |
| `q-011` | idem | transfert | mesure, seuil | paramétrique | comparaison d'une somme au seuil |
| `q-012` | idem | transfert | erreur réaliste et justification | fixe | comparer une estimation à une réponse |

Chaque objet de la banque possède les champs `objectif_id`, `critere_id`, `family_id`, difficulté, consigne, stimulus, solution ou rubricage, feedback, mode, seed et paramètres. **12 items au total, 6 paramétriques.** Les items initiaux servent surtout au diagnostic formatif; `q-009` et `q-010` sont seuls les deux **preuves de sortie** fixées par ce plan.

## Variation admissible, solution et reproductibilité

- **Aucun hasard libre.** Les six paramétriques utilisent `seed` entier stable et des formules explicites en **centièmes entiers**, arrondis seulement à l'affichage sous la forme `u,cc` (par exemple 2,50). Les domaines des variables, l'instance principale et trois variantes calculées par item figurent dans `BANQUE_ITEMS.json`.
- Calcul indépendant réalisé en **entiers** et en arithmétique décimale exacte `Decimal` sur les instances et tests de domaine; pas d'évaluation par modèle libre comme juge.
- Les contextes de P1/P2 ne varient pas librement : seul le jeu de valeurs bornées peut varier selon la formule fixée. Variation de wording ou unité non autorisée sans nouvelle revue.
- Les types `fixe`, `parametrique` ont leur sens du schéma `qc.learning-item-bank/1.0`; le contrat original de famille conserve `type: paramétrique_controle`.

## Rubrique, autonomie et décision

Sur P1 et P2, consigner séparément quatre dimensions : **(R1)** identification des quantités/choix et position des rangs, **(R2)** exactitude des deux calculs avec unités, **(R3)** plausibilité numérique des **deux** résultats, **(R4)** absence d'indice conceptuel. Une dimension est « atteinte » seulement si ses manifestations décrites dans `GRILLE_MAITRISE.md` sont toutes présentes; une preuve n'est satisfaisante que si R1–R4 le sont. La maîtrise exige **P1 et P2 satisfaisantes à des moments distincts**, pas une moyenne ni un seul score global. Une reprise corrigée guidée n'est pas une preuve autonome.

## Accessibilité et sécurité

- Consigne lue à haute voix possible, écrit agrandi, tableau de rangs vierge, matériel manipulable ou tactile, lecture par synthèse vocale, réponse orale dictée à scribe neutre; garder les mêmes critères de raisonnement.
- Pendant P1/P2 : autoriser adaptation de **modalité**, pas indice sur l'opération ou le calcul. Documenter l'aide matérielle utilisée sans recueillir d'information médicale.
- Argent et marche sont **fictifs**; pas d'achat, déplacement, effort physique ni révélation de budget personnel demandés. Prix en dollars fictifs et distances en kilomètres, pas de temps en heures décimales.
- Éviter dépendance à la vision des couleurs, connaissances sur un commerce précis ou motricité fine. Examiner l'énoncé et la durée avec des élèves avant qualification.

## Limites d'usage

Items non certifiés (`a_revoir`); vérification numérique n'est pas validation de pertinence didactique, de biais ni d'intégration au LMS. Relecture humaine et essai terrain requis. Ne déduire aucune conformité officielle PFEQ.
