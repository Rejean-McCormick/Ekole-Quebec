# Plan d'évaluation — `qc-pri-st-014` — Eau et cycle de l’eau

**Famille :** `qc-pri-st-014-ev-01` (type préservé `generee_sous_contraintes`) ; **objectif immuable :** `obj-1` — Expliquer par un schéma les principaux changements d’état et déplacements de l’eau. **Preuve/critère immuable :** `crit-1` — Construire une représentation commentée du cycle de l’eau.

## Table de couverture et traçabilité

**Toutes les lignes suivantes se rattachent explicitement à `obj-1`, `crit-1` et `qc-pri-st-014-ev-01`.** Les identifiants complets ci-dessous correspondent exactement aux entrées de `BANQUE_ITEMS.json`.

| Item complet | Difficulté | Représentation | Ce qui est effectivement vérifié | Décision |
|---|---|---|---|---|
| `qc-pri-st-014-q-001` | initial | flèche + texte | évaporation L→G, gaz invisible | diagnostic formatif |
| `qc-pri-st-014-q-002` | initial | schéma gaz/gouttes + phrase | condensation et distinction d'avec chute | formatif |
| `qc-pri-st-014-q-003` | initial | deux flèches terrain/nuage | précipitation contre ruissellement | formatif |
| `qc-pri-st-014-q-004` | intermédiaire | description d'observation | observation, inférence, condensation | formatif |
| `qc-pri-st-014-q-005` | intermédiaire | modèle à lieux précisés | cycle annoté complet, états, circulation | formatif |
| `qc-pri-st-014-q-006` | intermédiaire | branches de trajets | écoulement et infiltration | formatif |
| `qc-pri-st-014-q-007` | intermédiaire | critique de trois erreurs | étiquettes exactes, justification | formatif |
| `qc-pri-st-014-q-008` | transfert | schéma du jardin ramifié | 4 mécanismes, limites du modèle | préparation au transfert |
| `qc-pri-st-014-q-009` | transfert | production autonome côte / estuaire | **preuve A**, M1–M5, modèle commenté | maîtrise A |
| `qc-pri-st-014-q-010` | transfert | production autonome montagne / sol | **preuve B**, M1–M5, nouveau modèle ramifié | maîtrise B |

## Séquence de passation

1. **Entrée :** `q-001`–`q-003`; comparer aux diagnostics D1/D2. Le préalable `qc-pri-st-005` peut être reconnu acquis par diagnostic équivalent. `qc-pri-st-001` reste une recommandation non bloquante.
2. **Construction :** `q-004`–`q-007`, retour descriptif sans verdict global.
3. **Pré-transfert :** `q-008`, nouvelle carte de jardin, justification de la bifurcation.
4. **Deux preuves séparées :** `q-009` côte et `q-010` montagne, idéalement à des moments distincts; production nouvelle sur page vierge, aucun indice sur emplacement de flèches ni correctif pendant l'épreuve. Après chacune, relever les deux commentaires de l'élève.

## Mode généré sous contraintes, sans génération libre

Le champ natif de famille **`type=generee_sous_contraintes` est inchangé**. Le contenu livré forme un **catalogue fermé de scénarios entièrement rédigés et corrigés**, pas un générateur IA :

- `q-001` à `q-008` sont **fixes**, graines et paramètres `null`; l'évaluateur n'invente ni situation ni correction.
- `q-009` est `scenario_controle`, scénario unique `SCENARIO-COTE-01`, **seed=14009**, choix du catalogue `index=seed % 1 = 0` ; aucun autre scénario candidat. Tous les emplacements, processus, grille M1–M5 et corrigé sont prédéfinis.
- `q-010` est `scenario_controle`, scénario unique `SCENARIO-MONTAGNE-01`, **seed=14010**, choix `index=seed % 1 = 0` ; autre contexte, nouveau schéma. Ce petit algorithme explicite l'absence d'aléa caché; les paramètres ne modifient jamais le contenu scientifique.
- Graine de métadonnées de famille : **14014**, conservée séparément des graines d'instances; aucune sélection aléatoire, aucun texte ou corrigé généré librement. Pour un éventuel catalogue enrichi, il faut vérifier les scénarios ajoutés humainement et documenter nouvelle version et algorithme *avant* de les accepter.

## Correcteurs, variabilité et qualité de preuve

Les réponses modèles ne fixent **ni disposition spatiale, ni esthétique, ni trajet unique obligatoire**. Les corrections sont déterministes pour les étiquettes factuelles (L→G évaporation; G→L condensation; nuage→surface précipitation; sol→ruisseau ruissellement; surface→sol infiltration). Les schémas alternatifs reçoivent une évaluation **critériée** s'ils respectent les mêmes lois physiques et justifient les liens. Un modèle qui dit « vapeur blanche » ou « pluie qui monte par précipitation » est factuellement incorrect.

**Accessibilité — variations d'accès autorisées seulement :** papier, format numérique, flèches tactiles, schéma dicté à scribe sans conseils, oral transcrit, police/contraste/temps ajustés. Les étiquettes, les directions obligatoires, les mécanismes et les deux contextes ne peuvent pas être modifiés par l'adulte pendant une preuve. Les productions orales doivent décrire une structure de lieux et de flèches vérifiable, pas seulement réciter les quatre mots.

## Sécurité et éthique

Toutes les observations peuvent être fictives ou fournies sous forme descriptive. Ne pas faire chauffer ou bouillir de l'eau, observer au bord d'un plan d'eau ni utiliser appareil électrique, lame ou source de vapeur chaude. Une photo d'enfant n'est pas une preuve nécessaire. Aucune note sur la calligraphie, la motricité fine, l'aisance orale ou l'esthétique. Considérer une réponse tactile ou assistée si les liens scientifiques sont observables.

## Couverture et réserves

Les 4 notions sont chacune représentées à plusieurs reprises, les distinctions observation/modèle/inférence sont vérifiées, et deux transferts autonomes sont demandés. **Aucune banque n'est certifiée**; revoir faits, complexité, durée, équité des schémas ouverts, constance des évaluateurs et adéquation des adaptations avant usage décisionnel institutionnel.
