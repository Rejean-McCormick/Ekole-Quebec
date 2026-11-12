# 06 — Remédiation, transfert, rappel différé

**Kristal `qc-pri-ma-026` :** `obj-1` et `crit-1`.

**Règle :** corriger le raisonnement puis proposer un **nouvel** intervalle. Ne pas juger seulement l'exactitude du dernier nombre. Horaires fictifs, date civile uniforme de 24 h (pas de fuseau ni changement légal d'heure).

## Micro-remédiations ciblées

### `R1` — Heure, minute, unité

**Indice d'erreur :** « 1 h 20 = 120 minutes » ou « 1 h 20 = 1,20 h ». **Action** : représenter 60 jetons-minute pour 1 h, puis ajouter 20; **1 h 20 = 80 min**. **Nouvel essai** : `2 h 05 = 125 min`, car `120 + 5 = 125`. Vérifier la conversion inverse : `125 = 2×60 + 5`.

### `R2` — Passage d'heure, base 60

**Indice d'erreur :** 11 h 55→12 h 10 noté 55 min ou durée négative. **Action** : frise `11 h 55→12 h 00 = 5 min`, `12 h 00→12 h 10 = 10 min`; **15 min**. **Nouvel essai** : `16 h 40→17 h 15 = 20 + 15 = 35 min`. Vérifier par addition.

### `R3` — Calendrier et minuit

**Indice d'erreur :** croire que 00 h est « plus tôt » malgré une nouvelle date; ou placer le 29 février en 2025. **Action** : tracer `28 février 2024 → 29 février 2024 → 1er mars 2024` (2024 bissextile), comparer avec `28 février 2025 → 1er mars 2025`. **Nouvel essai** : `31 décembre 2025 à 23 h 55 → 1er janvier 2026 à 00 h 20 = 5 + 20 = 25 min`. Vérifier en avançant la date.

### `R4` — Contrôle de vraisemblance

**Indice d'erreur :** durée exacte, mais affirmation de succession incompatible. **Action** : donner deux cases « fin de l'activité » et « heure du rendez-vous »; placer les instants sur une même frise. **Nouvel essai** : visite `13 h 20→14 h 05` = 45 min, puis réservation annoncée « après » à 13 h 55 : faux; 13 h 55 est **10 min avant** la fin et donc pendant la visite.

## Transfert 1 — Horaire d'un centre communautaire (deux créneaux)

**Énoncé :** Dans un centre fictif, un atelier se tient de **09 h 20 à 10 h 05**. Une autre activité débute à **10 h 25**. (a) Calcule la durée de l'atelier. (b) Combien de minutes restent entre l'atelier et l'activité suivante? (c) Un déplacement de 15 minutes entre les salles est-il possible avant l'activité suivante?

**Corrigé raisonné :** (a) `40+5 = 45 min`, vérification `09 h 20+45 = 10 h 05`. (b) `10 h 05→10 h 25 = 20 min`. (c) **Oui**, 15 min de déplacement tiennent dans 20 min; il restera **5 min**. Les trois réponses et la contrainte concrète sont attendues.

## Transfert 2 — Observation de nature, passage d'année

**Énoncé :** Dans une station fictive, une observation démarre le **31 décembre 2025 à 23 h 35** et se termine le **1er janvier 2026 à 00 h 20**. Le local ferme à **00 h 30 le 1er janvier 2026**. (a) Quelle est la durée de l'observation? (b) Se termine-t-elle avant la fermeture, et de combien de temps? (c) Justifie le changement de date.

**Corrigé raisonné :** (a) `25 min` jusqu'à minuit + `20 min` = **45 min**. (b) **Oui**, fin `00 h 20`, soit **10 min avant** `00 h 30`. (c) le 1er janvier vient après le 31 décembre; `23 h 35 + 45 min = 00 h 20` au jour suivant. Une simple durée sans contrôle de fermeture ne complète pas l'objectif.

## Rappel différé

- **J+2** sans modèle sous les yeux : « Départ **07 h 50**, fin **08 h 35**; combien? » **45 min** (`10+35`). Vérification `07 h 50+45=08 h 35`.
- **J+7** : « **31 déc. 2025 23 h 55 → 1er janv. 2026 00 h 20**; combien? » **25 min**, avec date avancée. Vérification `23 h 55+25 = 00 h 20 le lendemain`.
- Après erreur : remédiation `R1`–`R4`, puis **nouveau** rappel; éviter de « réussir » uniquement en reproduisant la réponse donnée.

## Accessibilité et prudence

Les horaires sont donnés aussi en texte linéaire (« début... fin... ») pour lecteurs d'écran; la représentation visuelle ou tactile peut être facultative. Aucun déplacement réel de nuit n'est demandé; toutes les situations sont imaginaires. Une calculatrice ou une horloge mobile peut être un outil de représentation, mais l'évaluateur ne fournit pas de décomposition guidée pendant les preuves de maîtrise.
