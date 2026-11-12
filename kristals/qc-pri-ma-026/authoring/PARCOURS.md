---
format: qc.learning-path/1.0
id: qc-pri-ma-026
titre: Temps et durées
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Lire des horaires et déterminer des durées entre deux événements.
objectifs_secondaires: []
criteres_reussite:
- Calculer une durée et vérifier le sens du résultat dans un horaire.
prealables_declares: []
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-026-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-026`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Temps et durées  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**Statut de livraison :** leçon et banque préparées, **à revoir** avant toute qualification; la valeur YAML `en_rédaction` demeure.  
**Références internes :** `obj-1`, `crit-1`, `qc-pri-ma-026-ev-01`.

## 1. Intention et frontières

- `obj-1` — **Résultat vérifiable immuable :** Lire des horaires et déterminer des durées entre deux événements.
- `crit-1` — **Production autonome immuable :** Calculer une durée et vérifier le sens du résultat dans un horaire.
- Concept central : **durée écoulée** entre un début et une fin, distincte de l'heure indiquée par l'horloge; notions exactes : **heure, minute, calendrier, durée**.
- Lire les heures en notation 24 h (p. ex. `09 h 05`, `14 h 40`), et les dates écrites « 28 février 2024 ». Les exemples utilisent des horaires **fictifs**; le jour civil est conventionnellement de 24 h dans ces problèmes, sans changement d'heure légal.
- Aucune arête `requires` ou `recommends_before` sortante : diagnostic de compétence plutôt que blocage. Le graphe contient une arête entrante de transfert `reinforces` venant d'un autre Kristal : aucun prérequis implicite.
- Ne pas confondre durée écoulée, heure de fin, retard ni temps disponible jusqu'à une échéance. L'algorithme ne convertit pas des heures locales réelles en zones horaires : la traversée d'un changement d'heure n'est pas enseignée ici.

## 2. Notions et représentations

**Heure** : (a) unité de durée égale à 60 minutes (`1 h = 60 min`); (b) instant lu sur une horloge et écrit `HH h MM` de `00 h 00` à `23 h 59` en notation 24 h. Ainsi « 10 h 30 » est un instant, « 1 h 30 » peut être une durée selon le contexte. **Minute** : unité de durée, 60 secondes; les minutes affichées sur l'horloge vont de 00 à 59 (ce ne sont pas des centièmes d'heure). **Calendrier** : système pour situer les dates et leur succession (mois de 28, 29, 30 ou 31 jours; 2024 bissextile, 2025 non bissextile). **Durée** : quantité de temps non négative écoulée entre un événement de début et de fin; `fin − début`, exprimable en minutes, puis en heures et minutes.

Représentations à coordonner : deux positions sur une horloge à aiguilles ou un cadran à 24 h, frise graduée avec bonds jusqu'à l'heure ronde, tableau début/fin/date, calcul symbolique en minutes (`60 × heures + minutes`) et calendrier pour les jours. À minuit, le jour change : `23 h 50 → 00 h 10` le lendemain = 20 min, et non « −23 h 40 ».

Exemple résolu A : atelier fictif `09 h 35 → 11 h 10`; `09 h 35→10 h 00 = 25 min`, `10 h 00→11 h 00 = 60 min`, `11 h 00→11 h 10 = 10 min`; total **95 min = 1 h 35**. Vérification : `09 h 35 + 1 h 35 = 11 h 10`.

Exemple résolu B (calendrier) : rendez-vous fictif du **28 février 2024 à 23 h 40** au **29 février 2024 à 00 h 25** : `20 + 25 = 45 min`. Vérification : année 2024 bissextile, le lendemain du 28 février est le 29 février; ajouter 45 min à 23 h 40 donne 00 h 25 le lendemain.

Contre-exemple A : `09 h 50 → 10 h 20 = 70 min` en soustrayant `20−50` comme une base 100. Faux : 10 min jusqu'à 10 h puis 20 min = **30 min**. Contre-exemple B : `31 décembre 2025 à 23 h 50 → 1er janvier 2026 à 00 h 05 = −23 h 45`. Faux : la date change et la durée est **15 min**. Les deux contre-exemples sont développés dans `contenu/01_NOTIONS_ET_EXEMPLES.md`.

## 3. Préparation / diagnostic

- Aucune inscription antérieure à vérifier. Donner `diag-1` : « Le cours commence à 08 h 45 et finit à 09 h 15. Combien de minutes? Montre des bonds. » Réponse 30 min (15 + 15).
- Donner `diag-2` : « Une activité finit le 1er mars 2024 à 00 h 10 et commence le 29 février 2024 à 23 h 50. Quelle durée? » Réponse 20 min; l'élève doit identifier la date suivante et justifier le passage de minuit.
- Observer trois gestes : situer les deux instants, distinguer base 60/base 100, vérifier l'ordre des événements et l'unité. Le choix des aides dépend des erreurs; `diag-2` difficile n'interdit pas l'entrée au cours.
- Si les deux tâches sont exactes, expliquées et autonomes, offrir les deux preuves distinctes `q-011` et `q-012` sans imposer une reprise du parcours; sinon remédier au geste précis en cause.

## 4. Enseignement guidé

- `teach-1` : faire lire un horaire, identifier début et fin, annoncer l'unité attendue. Utiliser une frise : `13 h 45 → 14 h 00 → 14 h 25` = `15 + 25 = 40 min`.
- **Modelage explicité :** (1) comparer dates puis heures, (2) compter les bonds positifs jusqu'à la fin, (3) additionner des minutes, (4) convertir chaque groupe complet de 60 minutes en 1 h, (5) vérifier en avançant depuis le début jusqu'à la fin.
- Montrer avec une horloge mobile : avancer l'aiguille des minutes de 13 h 45 à 14 h 00 (15 min), puis jusqu'à 14 h 25 (25 min). L'horloge est un **support**, pas une preuve substituée au calcul.
- Représentation algébrique secondaire : même jour `D = (60H_f + M_f) − (60H_d + M_d)`; avec dates, `D = 1440 × (ordinal(fin.date) − ordinal(début.date)) + 60(H_f − H_d) + (M_f − M_d)` en minutes. Appliquer seulement quand la fin chronologique suit le début.
- Faire expliquer pourquoi `14 h 25` est une heure de fin et `40 min` une durée. Faire corriger un calcul volontairement fautif en base 100.

## 5. Pratique accompagnée

Trois essais à indices **dégressifs** (corrigés et formulations détaillées dans `contenu/04_PRATIQUE_ACCOMPAGNEE.md`).

1. `guided-1` (`10 h 50 → 11 h 20`) : frise déjà segmentée `10 h 50 → 11 h → 11 h 20`; solution `10 + 20 = 30 min`; question explicite « où passe-t-on l'heure? ».
2. `guided-2` (`14 h 15 → 15 h 05`) : donner seulement « trouve le prochain HH h 00 »; solution `45 + 5 = 50 min`; l'élève construit la frise.
3. `guided-3` (`30 avril 2025 à 23 h 55 → 1er mai 2025 à 00 h 20`) : ne fournir qu'une consigne de vérification finale, pas de frise; `5 + 20 = 25 min`, passage au mois suivant. Décrire oralement ou graphiquement la démarche.

Feedback immédiatement après chaque essai : isoler la **première** erreur (unité, date, addition ou minute-base-100) et fournir un nouvel essai isomorphe, pas le corrigé seul.

## 6. Pratique autonome

Quatre tâches sans aide de démarche (voir `contenu/05_PRATIQUE_AUTONOME.md`) : `A1` `08 h 25→09 h 00` = 35 min; `A2` `11 h 40→13 h 05` = 85 min = 1 h 25; `A3` `31 janvier 2025 à 23 h 45→1er février 2025 à 00 h 15` = 30 min; `A4` contrôle de plausibilité : `15 h 10→16 h 00` = 50 min, et un rendez-vous à 15 h 50 tombe **pendant** l'activité, non après. Chaque réponse comporte un calcul, une unité et une vérification dans l'horaire.

Conditions : nouvel horaire, aucun indice, outils de représentation facultatifs; supports d'accessibilité autorisés sans procédure prescrite. La trace de performance est conservée par le système d'apprentissage, non dans le canon.

## 7. Feedback et erreurs typiques

- `error-1` : unités mal interprétées (`1 h 20` lu « 1,20 h ») → écrire `60 + 20 = 80 min`, puis reconstruire 1 h 20.
- Soustraire séparément les minutes en base 100 → compter des bonds jusqu'au prochain `HH h 00`, recontrôler par addition.
- Oublier le changement de jour/mois/année → tracer deux cases « date de départ / date de fin » et compter le passage à minuit.
- Confondre durée et heure de fin → encadrer les instants dans l'horaire, entourer la **quantité** en minutes.
- Résultat numériquement exact mais impossible dans l'horaire → comparer la fin calculée et la prochaine activité/fermeture.
- La correction requiert une **ré-explication** et un essai sur des valeurs différentes; les aides n'entraînent aucune baisse silencieuse du critère.

## 8. Évaluation formative et preuves

- Famille unique `qc-pri-ma-026-ev-01`, `objectif_ref: obj-1`, `critere_ref: crit-1`; 12 items `q-001` à `q-012` avec stimuli, solutions, critères et rétroactions dans `evaluation/BANQUE_ITEMS.json`. Six sont paramétriques contrôlés avec seed entier, domaine fini, formule, sortie déjà instanciée et exemples testés.
- Couverture : heures/minutes et conversion (`q-001` à `q-006`), calendrier et minuit (`q-007` à `q-009`), contrôle de plausibilité (`q-010`), deux manifestations de maîtrise (`q-011` et `q-012`).
- **Preuve 1 indépendante** `q-011` : horaire d'atelier de bibliothèque, même jour, calcul + vérification avant la réservation suivante. **Preuve 2 indépendante** `q-012` : observation scientifique fictive, deux dates distinctes, calcul + vérification avant l'heure de fermeture. Aucun indice pendant ces deux passations.
- Grille qualitative à quatre dimensions (lecture, calcul, validation, autonomie), chacune graduée; conditions de maîtrise : les deux preuves satisfaisantes, chacune avec lecture et calcul exacts, contrôle pertinent et sans aide méthodologique. Pas de décision sur score isolé.
- Banque *non certifiée* : `validation_status = a_revoir`; correcteurs arithmétiques testés localement ne remplacent pas la revue humaine des consignes.

## 9. Remédiation / enrichissement

- Heure/minute : manipuler 60 jetons-minute pour former une heure puis reconvertir `75 min → 1 h 15`; vérifier avec addition.
- Passage d'heure : frise `11 h 55 → 12 h 00 → 12 h 10` pour éliminer la fausse base 100; contre-essai `16 h 40→17 h 15` = 35 min.
- Passage de date : bande calendrier 28/29 février 2024/1er mars 2024, puis 31 décembre 2025/1er janvier 2026; contre-essai corrigé sur autre date.
- Vérification : chercher une contrainte de l'horaire (fin avant fermeture, pause suffisante, simultanéité) et utiliser `début + durée = fin`.
- Enrichissement : calcul de temps de plusieurs étapes et d'intervalles sur plus d'un jour, sans heure d'été/hiver; deux transferts contextuels complets dans `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 10. Accessibilité

- Supports équivalents : horaire en tableau accessible, caractères agrandis et contrastés, lecture orale des chiffres/dates, bande de temps tactile, horloge physique, calculette de base si l'on évalue le raisonnement temporel plutôt que le calcul mental.
- Autoriser réponse dictée, écrite, orale ou à l'aide d'une frise annotée; conserver des traces de l'intervalle calculé, de l'unité, de la vérification et de l'autonomie.
- Éviter décorations ou stéréotypes culturels; afficher explicitement **début**, **fin**, dates et la convention « heure locale fictive uniforme, aucun changement d'heure ».
- Les outils de lecture et de manipulation autorisés ne sont pas des indices de méthode; un adulte ne doit ni découper l'intervalle pour l'élève ni confirmer la réponse pendant la preuve.

## 11. Critères de sortie

1. `crit-1` démontré : **Calculer une durée et vérifier le sens du résultat dans un horaire.** Deux productions autonomes en contextes réellement distincts (`q-011`/`q-012`) avec calcul correct et unité explicite.
2. Expliquer ou représenter la méthode (frise, addition de bonds ou calcul en minutes); vérifier l'égalité `début + durée = fin` et une contrainte pratique de l'horaire.
3. Maîtriser la différence **instant / durée**, y compris le franchissement de minuit et du calendrier.
4. Deux preuves cohérentes et suffisamment espacées pour ne pas être des essais mémorisés; révision ciblée si une preuve échoue. Décision documentée selon `evaluation/GRILLE_MAITRISE.md`, pas moyenne de notes.
5. **Rappel différé** : à J+2, `07 h 50→08 h 35` = 45 min; à J+7, `31 décembre 2025 à 23 h 55→1er janvier 2026 à 00 h 20` = 25 min. Pour chaque rappel, demander `début + durée = fin`, corriger et refaire une nouvelle donnée après erreur. Espacement proposé, non prouvé pour ce groupe.

## 12. Références pédagogiques et limites

- Autorité interne consultée : contrat v1.2, générateur/examens, charte Québec, `registry/GRAPHE_PEDAGOGIQUE_202.json`, métadonnées de ce Kristal.
- Principes de design cités par le workspace : `governance/Norme_Pedagogique_Autonome_v1.2/REFERENCES_EVIDENCE.md`; ne pas les présenter comme des validations empiriques de ce Kristal. `sources/REFERENCES_CONTENU.md` distingue explicitement sources lues, dérivations mathématiques et œuvres originales.
- `ALIGNEMENT.md` conserve l'appellation Mathématique : aucune homologation PFEQ/PDA et aucun code scolaire officiel attribué.
- Limites : horaires fictifs, temps civil uniforme de 24 h; pas de fuseaux, changements d'heure légaux, secondes ni calcul de fréquence. Validation technique et contrôles mathématiques effectués; tests utilisateurs, revue humaine, vérification framework/canon et publication **non réalisés**.
