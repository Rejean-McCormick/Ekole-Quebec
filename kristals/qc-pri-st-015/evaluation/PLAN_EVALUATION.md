# Plan d'évaluation — `qc-pri-st-015-ev-01`

**Autorité v1.2 :** `obj-1` = « Décrire des phénomènes météorologiques à partir de mesures et observations. »; `crit-1` = « Interpréter une courte série de relevés météorologiques. »; **famille** `qc-pri-st-015-ev-01`; mode natif `generee_sous_contraintes`. **12 items** individuels. Tous les relevés sont fictifs et tous les corrigés du fichier JSON sont des solutions de référence construites, **à revoir humainement**.

## Table de couverture et contraintes

| Item | Difficulté | Représentation | Travail observable (`obj-1`, `crit-1`, `qc-pri-st-015-ev-01` pour **chaque** ligne) | Variabilité admissible |
|---|---|---|---|---|
| `q-001` | initial | notation + deux instants | Température, changement avec °C | Valeurs verrouillées; reformulation neutre |
| `q-002` | initial | liste horodatée | Vent maximal + km/h + heure | Valeurs verrouillées |
| `q-003` | initial | courtes données temporelles | Pluie maximale et signification de zéro | Valeurs verrouillées |
| `q-004` | initial | nuages/pluie | Contre-exemple nuages ≠ pluie | Valeurs verrouillées |
| `q-005` | intermédiaire | propositions + mesures | Fait mesuré, inférence et prévision distinctes | Valeurs verrouillées |
| `q-006` | intermédiaire | tableau comparatif | Deux évolutions chiffrées + limite | Valeurs verrouillées |
| `q-007` | intermédiaire | intervalles contigus | Cumul disjoint de pluie avec unité | Valeurs verrouillées |
| `q-008` | intermédiaire | tableau avec `—` | Distinguer mesure absente et `0 mm` | Valeurs verrouillées |
| `q-009` | intermédiaire | fenêtres qui se recoupent | Refuser un cumul non justifié | Valeurs verrouillées |
| `q-010` | intermédiaire | tableau horodaté calculé | Température maximum, variation, vent, prévision non prouvée | Seed entier 0–4095; algorithme fermé du JSON, exemple seed 1010 |
| `q-011` | transfert / **preuve A** | cour d'école, série horaire | Plusieurs mesures, contre-exemple, limite et autonomie | Seed entier 0–4095; algorithme fermé du JSON, exemple 1011 |
| `q-012` | transfert / **preuve B** | jardin communautaire, matinées successives | Variation, somme de fenêtres, vent, contre-exemple et autonomie | Seed entier 0–4095; algorithme fermé du JSON, exemple 1012 |

**Liaison formelle :** chaque item porte `objectif_id: obj-1`, `critere_id: crit-1`, `family_id: qc-pri-st-015-ev-01`, contrôlés en JSON. Différences : `initial` lecture directe; `intermediaire` calcul, contrôle d'unités et refus d'inférences; `transfert` interprétation autonome pluridonnée avec justification.

## Détails des variations déterministes

- `q-001` à `q-009` : `mode = fixe`, `seed = null`, `parametres = null`; aucune donnée n'est remplacée. Le correcteur accepte une formulation équivalente **si** la période, l'unité, le sens et la preuve demeurent exacts.
- `q-010` à `q-012` : `mode = parametrique`. **Ne pas générer un texte neuf par IA.** La variable `s` est un entier dans `[0,4095]`; l'algorithme figurant sous `parametres.algorithme` produit les valeurs, les périodes et un corrigé reproductible. Les exemples calculés incluent la graine fournie et sa suivante. Le programme de vérification énumère toutes les graines autorisées, contrôle les limites des grandeurs, les maxima, les écarts, les totaux et les contre-exemples; cela ne remplace pas une revue humaine de clarté et d'authenticité pédagogique.
- Il est interdit de faire varier une période, une unité, un instrument, les relations temporelles, la règle de décision, les lieux des deux preuves ou de substituer à `—` un zéro. Les familles ne génèrent aucune prédiction réelle; toutes les données sont **simulées**.

## Conditions de passation

1. Diagnostic `02` ; enseignement `03` ; activités progressives `04` ; quatre tâches autonomes formatives `05`. Les items `q-001..010` soutiennent ajustement et diagnostic d'erreurs; ils ne remplacent pas les preuves.
2. **Preuve A (`q-011`, cour d'école)** puis **preuve B (`q-012`, jardin communautaire)**, contextes distincts : lieux, rythme horaire vs jours, types de comparaison. Fournir l'un ou l'autre dans un ordre équilibré; au besoin une pause et un autre moment de passation. Ne pas donner les corrigés/algorithmes aux apprenants durant la passation.
3. Pour chacune des deux preuves, exiger données exactes, bonne unité, intervalle clairement nommé, interprétation appuyée, limite honnête, **autonomie sans indice de contenu**. Voir seuils critériés dans `GRILLE_MAITRISE.md`. La réussite à un seul item ou une somme de points **ne vaut jamais à elle seule** maîtrise.
4. Feedback après passation : identifier la colonne et l'intervalle qui manquent, demander révision et proposer une **nouvelle graine différente** du même item pour une nouvelle preuve, plutôt que révéler immédiatement le résultat.

## Mesures de sûreté et d'accessibilité

- Aucun relevé extérieur imposé, sortie pendant intempérie, appareil dangereux, application météo, accès Internet, géolocalisation, photographie ni donnée nominative requis. Toutes les données ont une nature fictive explicitement annoncée.
- Offrir tableaux en texte linéaire, gros caractères, lecture audio, synthèse vocale, impression tactile et réponse écrite/orale/dictée; l'orthographe n'est pas évaluée. Les informations cruciales sont en **texte**, pas seulement en couleur ou icône.
- Le correcteur utilise la **preuve scientifique**, non le style, le statut social ni la familiarité avec un lieu. Autres adaptations doivent préserver la comparabilité et être documentées.
- Une épreuve sommative locale exigerait validation humaine de la lisibilité, de la durée, de la rubrique et d'éventuels biais avant utilisation. Ne pas utiliser les résultats pour une alerte de sécurité météorologique.

## Revue des erreurs et sécurité du générateur

- Contrôles numériques prévus **et effectivement consignés** dans `livraison/VALIDATION.md`; pas de qualificatif « certifié ».
- Vérifier manuellement : confusion `0 mm`/`—`; « couvert » n'implique pas la pluie; somme seulement d'intervalles **disjoints**; différence entre une mesure et une prévision; lecture correcte des signes en °C; deux contextes de maîtrise réellement différents.
- Toute génération hors algorithme et hors domaine est **refusée** jusqu'à validation de la nouvelle instance et de son corrigé.
