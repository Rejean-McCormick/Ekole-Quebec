# PLAN D’ÉVALUATION — qc-pri-ma-025

**Objectif `obj-1` (inchangé) :** Mesurer et comparer des longueurs, masses ou capacités avec unités adaptées.  
**Critère `crit-1` (inchangé) :** Choisir l’outil et mesurer un objet réel en justifiant l’unité.  
**Famille unique (inchangée) :** `qc-pri-ma-025-ev-01`. **Mode du contrat :** `paramétrique_controle`. La banque comporte aussi des ancrages fixes et des scénarios pratiques contrôlés. **Statut :** non certifié, revue humaine requise.

## Plan par item, objectifs et représentations

| Item | Objectif / critère / famille | Difficulté | Mode | Représentation | Usage |
|---|---|---|---|---|---|
| `qc-pri-ma-025-q-001` | `obj-1` / `crit-1` / `qc-pri-ma-025-ev-01` | initial | fixe | tableau textuel | Entraînement / contrôle |
| `qc-pri-ma-025-q-002` | `obj-1` / `crit-1` / `qc-pri-ma-025-ev-01` | initial | fixe | schema textuel | Entraînement / contrôle |
| `qc-pri-ma-025-q-003` | `obj-1` / `crit-1` / `qc-pri-ma-025-ev-01` | intermediaire | parametrique | regle schema et notation | Entraînement / contrôle |
| `qc-pri-ma-025-q-004` | `obj-1` / `crit-1` / `qc-pri-ma-025-ev-01` | intermediaire | parametrique | balances chiffrees | Entraînement / contrôle |
| `qc-pri-ma-025-q-005` | `obj-1` / `crit-1` / `qc-pri-ma-025-ev-01` | intermediaire | parametrique | schema recipient | Entraînement / contrôle |
| `qc-pri-ma-025-q-006` | `obj-1` / `crit-1` / `qc-pri-ma-025-ev-01` | transfert | parametrique | notations et regle | Entraînement / contrôle |
| `qc-pri-ma-025-q-007` | `obj-1` / `crit-1` / `qc-pri-ma-025-ev-01` | intermediaire | parametrique | materiel tasse et notation | Entraînement / contrôle |
| `qc-pri-ma-025-q-008` | `obj-1` / `crit-1` / `qc-pri-ma-025-ev-01` | intermediaire | fixe | explication orale ou ecrite | Entraînement / contrôle |
| `qc-pri-ma-025-q-009` | `obj-1` / `crit-1` / `qc-pri-ma-025-ev-01` | transfert | fixe | description de graduations | Entraînement / contrôle |
| `qc-pri-ma-025-q-010` | `obj-1` / `crit-1` / `qc-pri-ma-025-ev-01` | transfert | scenario_controle | objet reel balance et trace | Entraînement / contrôle |
| `qc-pri-ma-025-q-011` | `obj-1` / `crit-1` / `qc-pri-ma-025-ev-01` | transfert | scenario_controle | objet reel longueur croquis | Preuve A |
| `qc-pri-ma-025-q-012` | `obj-1` / `crit-1` / `qc-pri-ma-025-ev-01` | transfert | scenario_controle | objet reel capacite eau | Preuve B |

**Couverture :** q-001, q-008 = correspondance grandeur/instrument/unité et distinction zéro-tare-étalonnage; q-002, q-003 = lecture d’une longueur avec origine décalée; q-004 = tare; q-005, q-007, q-009 = capacité/volume de liquide; q-006 = conversion de longueurs et comparaison; q-010 = mesure de masse réelle; q-011 = preuve de longueur réelle; q-012 = preuve de capacité réelle. Les trois grandeurs sont représentées, ainsi que matériel, schéma, notation et justification.

## Corrigés et barème

- **Items calculables q-002 à q-007 et q-009 :** contrôles déterministes; comparer équivalence exacte du nombre et de l’unité; accepter des unités converties de façon juste lorsque cela ne détruit pas la compétence testée. Exiger aussi choix de l'outil, représentation ou justification lorsque demandé. Un nombre seul ne suffit pas à démontrer `crit-1`.
- **Items q-001 et q-008 :** réponses en français équivalentes recevables; comparer les concepts essentiels, pas la formulation mot pour mot.
- **Items réels q-010, q-011, q-012 :** référence indépendante de l’évaluateur réalisée sur le **même objet** et consignée, sans imposer une valeur théorique universelle. Grille de quatre dimensions de `evaluation/GRILLE_MAITRISE.md` : grandeur/outil/unité, préparation/lecture, qualité de la mesure, justification/autonomie. Les tolérances annoncées reposent sur les graduations et la reproductibilité, et peuvent être resserrées/élargies uniquement **avant** l'évaluation avec justification (accessibilité, résolution, pertes de transvasement).
- **Données paramétriques :** q-003, q-004, q-005, q-006, q-007 portent chacune leur domaine, algorithme déterministe sans tirage libre, seed fixe, contraintes, exemple instancié et procédure de test. Un contrôle de cohérence arithmétique indépendant est documenté dans la validation. Le contrat de famille contient les mêmes variables et contraintes. Les variantes de seeds entiers non négatifs doivent passer les mêmes tests avant usage.

## Décision de maîtrise (non compensatoire)

1. Après apprentissage, administrer **q-011** (livre/cahier jamais montré) et **q-012** (récipient plastique gradué jusqu’à un repère, jamais montré), dans des sessions ou moments séparés si possible, **sans indices** sur la grandeur, l’outil, l’unité ni la procédure.
2. Pour **chacune** des deux preuves : niveau « acquis autonome » sur les **quatre dimensions**; un écart de lecture hors tolérance, une grandeur incorrecte ou un outil choisi par l’adulte invalide la preuve. L’évaluateur recueille les valeurs observées et sa référence indépendante.
3. Si une preuve échoue, feedback descriptif et remédiation ciblée; recommencer sur un nouvel objet du même type. **Ne pas moyenner** les performances pour compenser une preuve manquante. Réussir q-010 ne remplace pas q-011 ni q-012.
4. Rappel J+2 et J+7 avec nouveau contexte; le rappel documente la stabilité, pas une validation sans nouvelle mesure.

## Variabilité, biais et sécurité

**Variables admissibles :** seeds entiers non négatifs pour q-003 à q-007; nouveau livre ou cahier à bords nets pour q-011; récipient plastique sain, avec repère lisible et volume ≤500 mL pour q-012; petit lot non dangereux et boîte pour q-010. **Interdit :** remplacement de l’objet réel par une image pour les deux preuves, génération libre des chiffres ou de la solution par IA, changement arbitraire d’unité, hypothèse « 1 mL = 1 g », mesure de liquide chaud, d’objet coupant ou de récipients cassants.

**Accessibilité :** lecture de consigne et transcription orale possibles; règles à grand contraste/tactiles, balances parlantes ou affichage agrandi, repères tactiles et tasse antidérapante; aide motrice uniquement sur indication explicite de l’apprenant. Le choix et la justification doivent lui appartenir. En l’absence de matériel accessible, prêter/adapter le matériel et **reporter la maîtrise**, ne pas la déduire d’un dessin. Les critères cognitifs demeurent identiques.

**Revue humaine obligatoire :** vérifier que les objets réels sont accessibles et sans danger, que la graduation et la tolérance sont acceptables, que le vocabulaire convient, et observer des essais avant qualification. Aucune homologation PFEQ affirmée.
