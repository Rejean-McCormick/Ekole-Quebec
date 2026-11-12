# Plan d'évaluation local — `qc-pri-fr-026`

**Objectif invariant `obj-1` :** Présenter une idée structurée et la défendre à l’aide de raisons audibles.  
**Preuve invariante `crit-1` :** Donner un court exposé suivi de réponses pertinentes à deux questions.  
**Famille invariante :** `qc-pri-fr-026-ev-01` · **type** `réponse_argumentée` · **état** `a_revoir`.

## Architecture et couverture

| Item | Fonction, difficulté | Représentation / contexte | Couverture observée | Deux questions si exposé complet? |
|---|---|---|---|---|
| `q-001` | diagnostic, initial | récit dit/oralisé; pause | écoute d'une idée, d'une raison, formulation d'une question; test d'équivalence du préalable | non, test du préalable (pas preuve de maîtrise) |
| `q-002` | diagnostic, initial | projet de panier de feuilles; oral | idées/argument/exemple/deux réponses | oui |
| `q-003` | guidé, initial | cartes ou phrases dites | ordre idée/raison/exemple/conclusion | non, partie de tâche |
| `q-004` | guidé, initial | choix de phrases dites ou imprimées | lien argument/exemple à idée | non, partie de tâche |
| `q-005` | guidé, intermédiaire | plateau d'objets trouvés; mini-exposé | oral + 2 questions, sans indice de contenu au dernier essai | oui |
| `q-006` | autonome d'entraînement, intermédiaire | table de matériel de classe | S/R/E/Q/A | oui |
| `q-007` | autonome d'entraînement, intermédiaire | affiche de livres | S/R/E/Q/A | oui |
| `q-008` | autonome d'entraînement, intermédiaire | séchage en atelier | S/R/E/Q/A | oui |
| `q-009` | autonome d'entraînement, intermédiaire | rangement de jeux | S/R/E/Q/A | oui |
| `q-010` | **M1**, transfert | point de dépôt de travaux en classe, sujet réservé | S/R/E/Q/A, **preuve 1** | oui, questions fixes |
| `q-011` | **M2**, transfert | signalisation d'activités d'un centre communautaire fictif | S/R/E/Q/A, **preuve 2** | oui, questions fixes |
| `q-012` | transfert d'enrichissement, transfert | aménagement d'un centre communautaire, distinct de M2 | S/R/E/Q/A | oui |
| `q-013` | transfert d'enrichissement, transfert | rangement pour atelier de science fictif | S/R/E/Q/A, sans test de connaissances scientifiques | oui |

**Lien explicite de chaque item :** `objectif_id = obj-1`, `critere_id = crit-1`, `family_id = qc-pri-fr-026-ev-01`, y compris les sous-tâches préparatoires. Pour `q-001`, `q-003` et `q-004`, les composantes sont seulement des **indices formatifs** et **ne peuvent pas** être comptées comme expositions certifiant `crit-1`.

## Difficulté, poids, représentation et administration

- **Initial :** compréhension de phrases et écoute de structures avec étayage; **intermédiaire :** argumentation courte sur une situation concrète, partiellement entraînée; **transfert :** contexte inédit, formulation libre dans un corpus fermé et réponses à deux questions sans aide de fond.
- **Durée indicative :** 45–90 s d'exposé complet, adaptable; plus environ 1–3 min de préparation autonome et le temps de traiter deux questions. La durée et l'éloquence ne sont **pas** des critères notés.
- **Aucun poids arithmétique unique :** cinq dimensions S/R/E/Q/A évaluées **séparément** (0, 1, 2). Pour la maîtrise : toutes au niveau 2 dans **chacune de M1 et M2**, deux contextes réellement distincts. Q=2 exige Q1 et Q2 pertinentes séparément. Des résultats formatifs ne compensent pas une preuve manquante.
- **Représentations d'entrée :** lecture orale de consigne, synthèse vocale, cartes de repérage, texte de consigne si accès nécessaire; **sortie :** performance orale vocale ou synthèse vocale pilotée par l'élève. Ne pas transformer la mesure en examen de lecture ou d'écrit.

## Corrigés, variations et contrôles

Tous les sujets sont des **situations fictives originales**; les productions « réponse attendue » dans la banque sont **des exemples de productions recevables**, pas des textes obligatoires. Les variantes recevables doivent maintenir : 1 idée défendable adaptée au contexte; 1 raison liée; 1 exemple précis et compatible; 1 fermeture; **deux réponses directement pertinentes** aux questions fixées; audibilité/intelligibilité accessible. Les propositions contraires sont acceptables **si** elles satisfont les mêmes critères. Pas d'arbitrage des goûts, croyances ou opinions.

- `mode: fixe` pour `q-001` à `q-005` : formulations et stimuli verrouillés; `seed: null`; `parametres: null`.
- `mode: scenario_controle` pour `q-006` à `q-013` : situations, questions et limites explicitement écrites dans `BANQUE_ITEMS.json`; **ce lot utilise une seule variante fixée par item** (aucun tirage exécuté), `seed: null` et `parametres: null`; future banque de substituts nécessiterait une revue humaine et des tests d'équivalence.
- Aucun mode paramétrique ni formule de calcul mathématique. Un moteur IA peut éventuellement proposer des formulations **pour revue humaine**, jamais juger seul la validité d'une performance libre.
- **Vérifications des réponses :** comparer pour chaque tâche l'énoncé, l'exemple de production et chaque réponse aux questions; conserver une justification lisible, y compris les mauvaises options des exercices guidés.

## Sécurité et accessibilité

Thèmes neutres, imaginés et non personnels; aucun enregistrement imposé et aucune question d'identité ou de croyance. Accepter la variation du français québécois. Mettre au point les aides d'accès sans donner la raison, l'exemple ou la réponse. Pour tout usage sommatif local, validation humaine des biais, durée, droits, accessibilité, interprétation de l'audibilité et calibrage inter-évaluateurs **obligatoire avant déploiement**. Une transcription écrite non vocalisée n'atteste pas à elle seule l'objectif oral.

## Critères et décision

Lire `GRILLE_MAITRISE.md` pour les seuils, les deux preuves, les conditions d'autonomie et la remédiation R1–R5. Les performances assistées et les diagnostics éclairent l'enseignement, **pas** la décision finale. **Statut actuel :** banque initiale complète, items `a_revoir`, absence d'essais en classe et de qualification psychométrique.
