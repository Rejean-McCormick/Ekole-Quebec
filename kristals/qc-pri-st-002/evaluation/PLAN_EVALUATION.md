# Plan d'évaluation — `qc-pri-st-002`

**Objectif :** `obj-1` — Formuler une prédiction motivée et concevoir un test simple et sûr. **Critère :** `crit-1` — Proposer un protocole avec paramètres observables et mesures prévues. **Famille native :** `qc-pri-st-002-ev-01` — type `generee_sous_contraintes` (sélection contrôlée de corpus **fixes**, aucune IA libre ni paramétrisation aléatoire).

## Traçabilité exhaustive des items

Chaque ligne correspond explicitement à **`obj-1` / `crit-1` / `qc-pri-st-002-ev-01`**. Le barème est **critérié** : la prévision n'est pas évaluée selon son accord avec un résultat non mesuré. La preuve finale est un plan d'investigation, **non** la réalisation d'une expérience.

| Item complet | Difficulté | Mode, représentation et tâche | Dimension évaluée | Rôle |
|---|---|---|---|---|
| `qc-pri-st-002-q-001` | initial | fixe, question écrite/orale | Question observable et grandeur mesurable | formatif |
| `qc-pri-st-002-q-002` | initial | fixe, phrases à discuter | Observation/hypothèse/conclusion prématurée | formatif |
| `qc-pri-st-002-q-003` | initial | fixe, variables et instrument | X, Y, contrôles, unités | formatif |
| `qc-pri-st-002-q-004` | intermédiaire | fixe, réparation d'un test | Variables confondantes et comparaison | formatif |
| `qc-pri-st-002-q-005` | intermédiaire | fixe, tableau vierge | Conditions, unités, répétitions | formatif |
| `qc-pri-st-002-q-006` | intermédiaire | fixe, réécriture de protocole | Prévention et arrêt de sécurité | formatif |
| `qc-pri-st-002-q-007` | intermédiaire | scénario contrôlé R7 | Contrôle imparfait et limite causale | formatif |
| `qc-pri-st-002-q-008` | transfert | scénario contrôlé R8 | Plan complet sur une fenêtre en carton | formatif |
| `qc-pri-st-002-q-009` | transfert | scénario contrôlé A, plan d'étalement | **Maîtrise A indépendante** : toutes dimensions M1–M6 | preuve A |
| `qc-pri-st-002-q-010` | transfert | scénario contrôlé B, plan d'ombre | **Maîtrise B indépendante** : toutes dimensions M1–M6 | preuve B |

## Administration et deux preuves

1. **Avant chaque preuve**, lire ou présenter le stimulus fixe, proposer un support vierge « question → prédiction → X → Y → constantes → étapes → mesures → sécurité » et organiser une réponse écrite, schématique, orale ou dictée à un scribe neutre. Le support est **structurel**, il ne suggère ni variable ni valeur de Y. Pas de démonstration ni de rétroaction directive pendant la preuve.
2. **A :** échantillons de papier ordinaire/essuie-tout, comparaison de diamètre maximal d'une goutte à **20 s**, en mm, deux essais par papier; aucune manipulation obligatoire.
3. **B :** lampe LED à piles, objet et écran fixe; comparer distance lampe–objet **10/20 cm**, objet–écran **20 cm fixe**; mesurer largeur de l'ombre en cm après stabilisation, deux essais par distance; aucune manipulation obligatoire. Scénario distinct en optique, pas variante cosmétique du papier.
4. À chaque preuve, relever les **six indicateurs** : M1 hypothèse, M2 variables, M3 comparaison, M4 mesures/traces, M5 sécurité, M6 autonomie. Comparer les deux jugements séparément; ne pas compenser M5=0 par d'autres points. Un seul plan réussi ne suffit pas.

## Variabilité permise, contrôle déterministe et limites

- **Pas d'item mode `parametrique` :** les valeurs de conditions et les corrigés sont fixés pour chaque item; `seed=null` et `parametres=null` dans la banque. La famille contient une clé documentaire de sélection fixe et un ordre lexicographique reproductible, mais ne prétend **pas** avoir exécuté un tirage.
- **Variations autorisées sans altération de la mesure :** mode de lecture, braille/pictogrammes si fournis, scribe neutre, temps flexible, présentation de tableau, clavier, dispositif de communication, dessin à main levée. Conserver dimensions, variables, unités et conditions A/B.
- **Génération sous contraintes :** seulement sélection d'un item du corpus connu, aucun remplacement de phénomène, aucune substitution de valeurs, aucune correction automatique par IA. Une nouvelle scène requiert une rédaction, une solution et une revue humaine.
- **Cas limites :** contours d'eau irréguliers : définir « diamètre maximal visible »; lumière dispersée : placer lampe/objet/écran sur même axe et mesurer après stabilisation. Une hypothèse opposée mais motivée est acceptable : **ce qui est noté est la testabilité du plan**, pas la prédiction d'un effet prouvé.

## Sécurité, accessibilité et validité

Nul besoin d'exécuter un test. Si l'enseignant décide d'une illustration matérielle : adulte supervise, très petite eau sur plateau avec nettoyage immédiat, lampe **LED à piles** et faible intensité, jamais de laser, secteur, chaleur, vision directe vers lampe ou objet instable. Toute condition risquée remplace l'exécution par une planification fictive. Accessibilité par schéma, dictée, textes simples, visualisation de variables; aucun handicap moteur ne doit devenir un critère caché.

**Statut :** `a_revoir` dans les dix items, rubriques non étalonnées, non publiées/certifiées. La validité des scénarios, les biais de langage et l'uniformité intercorrecteurs doivent être examinés humainement avant usage décisionnel.
