# Plan d’évaluation — Temps et durées

**Périmètre :** `qc-pri-ma-026` · **Objectif immuable `obj-1` :** Lire des horaires et déterminer des durées entre deux événements. **Critère immuable `crit-1` :** Calculer une durée et vérifier le sens du résultat dans un horaire. **Famille immuable :** `qc-pri-ma-026-ev-01`. **Mode privilégié interne :** `paramétrique_controle` avec variantes bornées; des ancrages fixes complètent la banque.

## Plan de vérification et progression

- Préparation formative : deux diagnostics `diag-1` / `diag-2` (fichier `contenu/02_DIAGNOSTIC.md`) hors banque d'évaluation; pas de préalables bloquants.
- Apprentissage : 3 exercices guidés à indices dégressifs et 4 autonomes formatifs (dossiers `contenu/`); aucune note diagnostic ne remplace une preuve.
- Banque de 12 items, 6 fixes et 6 paramétriques, tous liés **explicitement** à `obj-1`, `crit-1` et `qc-pri-ma-026-ev-01`. Étapes : lecture, conversion/intervalle, calendrier, plausibilité, transfert.
- Représentations : tableaux/phrases d’horaire, frise, horloge facultative, calendrier écrit, calcul en minutes; questions au format ouvert avec calcul et justification, pas un QCM.

## Inventaire exhaustif et liens

| Item | Difficulté | Mode | Compétence et représentation | Variation permise | Liens contractuels |
|---|---|---|---|---|---|
| `qc-pri-ma-026-q-001` | `initial` | `fixe` | Lecture simple; addition de contrôle; tableau horaire 24 h | Aucune (fixe) | `obj-1` / `crit-1` / `qc-pri-ma-026-ev-01` |
| `qc-pri-ma-026-q-002` | `initial` | `parametrique` | Durée et temps libre; tableau horaire + intervalle libre | Domaines finis + seed dans banque | `obj-1` / `crit-1` / `qc-pri-ma-026-ev-01` |
| `qc-pri-ma-026-q-003` | `initial` | `fixe` | Passage d’heure (base 60); frise de changement d’heure | Aucune (fixe) | `obj-1` / `crit-1` / `qc-pri-ma-026-ev-01` |
| `qc-pri-ma-026-q-004` | `intermediaire` | `parametrique` | Deux étapes successives; tableau multiévénements + addition de bonds | Domaines finis + seed dans banque | `obj-1` / `crit-1` / `qc-pri-ma-026-ev-01` |
| `qc-pri-ma-026-q-005` | `intermediaire` | `fixe` | Comparaison de créneaux; horaire à deux créneaux | Aucune (fixe) | `obj-1` / `crit-1` / `qc-pri-ma-026-ev-01` |
| `qc-pri-ma-026-q-006` | `intermediaire` | `parametrique` | Passage d’heure paramétré; horaire 24 h + conversion en minutes | Domaines finis + seed dans banque | `obj-1` / `crit-1` / `qc-pri-ma-026-ev-01` |
| `qc-pri-ma-026-q-007` | `intermediaire` | `fixe` | Février bissextile et minuit; calendrier + frise de minuit | Aucune (fixe) | `obj-1` / `crit-1` / `qc-pri-ma-026-ev-01` |
| `qc-pri-ma-026-q-008` | `transfert` | `parametrique` | Minuit avec dates paramétrées; calendrier + dates de fin calculées | Domaines finis + seed dans banque | `obj-1` / `crit-1` / `qc-pri-ma-026-ev-01` |
| `qc-pri-ma-026-q-009` | `transfert` | `parametrique` | Durée supérieure à un jour; calendrier + intervalle supérieur à 24 h | Domaines finis + seed dans banque | `obj-1` / `crit-1` / `qc-pri-ma-026-ev-01` |
| `qc-pri-ma-026-q-010` | `transfert` | `fixe` | Chevauchement et plausibilité; horaire + affirmation à vérifier | Aucune (fixe) | `obj-1` / `crit-1` / `qc-pri-ma-026-ev-01` |
| `qc-pri-ma-026-q-011` | `transfert` | `fixe` | PREUVE A — bibliothèque; preuve A : réservation à la bibliothèque | Aucune (fixe) | `obj-1` / `crit-1` / `qc-pri-ma-026-ev-01` |
| `qc-pri-ma-026-q-012` | `transfert` | `parametrique` | PREUVE B — station d’observation; preuve B : calendrier et fermeture nocturne | Domaines finis + seed dans banque | `obj-1` / `crit-1` / `qc-pri-ma-026-ev-01` |

## Règles paramétriques contrôlées

Chaque item `parametrique` comporte **déjà une instance entièrement lisible**, la réponse correspondante et, dans `parametres`, domaines finis de variables, contraintes, algorithme d'instanciation, algorithme de résolution, graine stable, trois seeds d'exemple recalculées et vérification indépendante. L'ordre de sélection des variables correspond à leur ordre dans `variables` : à chaque étape index `seed % nombre_de_choix`, puis division entière par `nombre_de_choix`. Les domaines permettent un nombre fini de combinaisons vérifiable exhaustivement. Aucune génération de texte arbitraire par IA ni formule de correction implicite.

**Conventions fixes :** calendrier grégorien, heures sur 24 h, dates explicites lorsque minuit est franchi, jour de 1440 min pour les seuls horaires **fictifs**. Les cas de changement d’heure légal ou de fuseaux horaires sont exclus. Les valeurs des domaines peuvent changer **uniquement** sous contrôle des contraintes et après recalcul de la solution; les seed de l'instance fournie ne doivent pas être altérées sans nouvelle validation.

**Calcul de référence A :** construire l'instant de début `S`, puis l'instant de fin `F = S + durée_minutes` (et l'heure de l'événement suivant/fermeture en cas de marge). **Calcul de contre-vérification B, indépendant :** `D = 1440×(ordinal(date_F)−ordinal(date_S)) + 60×(HH_F−HH_S) + (MM_F−MM_S)` et comparaison avec le résultat annoncé. L'indépendance est celle de deux procédures arithmétiques distinctes; un essai humain demeure nécessaire pour les ambiguïtés de contexte.

## Difficultés et compétences effectivement couvertes

- **Initial** `q-001`–`q-003` : heure et minute, intervalle simple et passage d’heure, représentation 24 h.
- **Intermédiaire** `q-004`–`q-007` : plusieurs intervalles, conversion, passage d’heure et du 28 au 29 février bissextile.
- **Transfert** `q-008`–`q-012` : passage de date/mois/année, intervalle supérieur à 24 h, compatibilité avec un autre événement et deux preuves autonomes.
- Les résultats calculés et les marges d'horaire sont des **quantités distinctes**; répondre à l'une ne suffit pas pour l'autre.

## Grille d’observation et modalités

1. **Lecture** : identifier début et fin avec leurs dates, dans le bon ordre.
2. **Exactitude du calcul** : résultat en minutes, conversion d'heures si demandée, absence de base 100 et de résultat négatif injustifié.
3. **Vérification / sens** : démontrer que `début + durée = fin` et interpréter correctement la réservation suivante, la fermeture ou le chevauchement quand elle est donnée.
4. **Autonomie / communication** : stratégie visible sans indice méthodologique, explicable par écrit, oralement ou par schéma.

Les 4 critères sont détaillés dans `evaluation/GRILLE_MAITRISE.md`. Pour les items de soutien, fournir feedback descriptif après passation et recommencer sur de nouvelles données si nécessaire.

## Double preuve obligatoire et décision

- **`q-011` (preuve A, contexte bibliothèque)** : calculer **100 min = 1 h 40**, vérifier `10 h 25 + 1 h 40 = 12 h 05` et **10 min** de marge avant la réservation de 12 h 15. Aucun indice ou découpage fourni.
- **`q-012` (preuve B, contexte station d’observation)** : lire deux **dates différentes**, calculer la durée instanciée, prouver l'avancée au jour suivant, vérifier l'addition, et déterminer la marge avant une fermeture. La graine et l'instance courantes sont verrouillées dans la banque; sans aide méthodologique.
- Les preuves couvrent deux contextes et deux représentations (même jour / changement de date). Demander les preuves lors de séances distinctes si possible; ne pas déduire l'acquisition d'une note unique ou d'une récitation du modèle.
- Une preuve incomplète → identifier le critère non satisfait, remédier (`R1` à `R4`), reprendre une **autre instance vérifiée** et obtenir de nouveau deux preuves satisfaisantes avant décision.

## Sécurité, équité et accessibilité

Situations 100 % fictives, sans déplacement nocturne réel, données personnelles ni sujets sensibles; notation québécoise naturelle et neutre. Lire les énoncés à voix haute, augmenter les caractères, fournir une description linéaire du tableau, une frise tactile, une horloge manipulable ou une calculatrice lorsque cela ne donne **pas** la méthode. Une réponse orale/dictée est recevable si calcul, unité, date et vérification demeurent observables. Ne pas noter orthographe, vitesse de lecture ni habileté graphique.

**Publication :** `a_revoir` pour tous les items. Vérifications numériques et de cohérence techniques ne constituent pas une certification, une étude empirique ni une homologation au PFEQ. Revue humaine des consignes et essai avec apprenants encore à effectuer.
