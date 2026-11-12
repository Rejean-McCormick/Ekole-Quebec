# Plan d'évaluation · `qc-pri-eps-010`

**Objectif invariant :** `obj-1` — Planifier des occasions d’activité physique variées et réalistes. **Critère invariant :** `crit-1` — Élaborer un plan hebdomadaire flexible d’activités plaisantes. **Famille :** `qc-pri-eps-010-ev-01`. **Statut :** banque rédigée, non certifiée (`a_revoir`). Le mode de la famille demeure `observation_ou_production`; les items sont fixes ou à scénario fermé. Une tâche évalue un produit **observable**, pas la dépense énergétique.

## Couverture contrôlée des items

| Item | Difficulté | Représentation et production | Critères principaux | Variabilité |
|---|---|---|---|---|
| q-001 | initial | Horaires, quatre cartes; deux choix commentés | réalisme, surveillance | aucune |
| q-002 | initial | Avis de fermeture; activité et plan B | contexte, flexibilité, matériel | aucune |
| q-003 | initial | Préférences et matériel; deux occasions | variété, motivation explicite | aucune |
| q-004 | intermédiaire | Comparaison de deux brouillons | sécurité, alternative | aucune |
| q-005 | intermédiaire | Réécriture d'un plan dangereux | sécurité, variété, contexte | aucune |
| q-006 | intermédiaire | Planning de trois jours conditionnels | continuité, météo | aucune |
| q-007 | intermédiaire | Deux fiches complètes A/B | variation contrôlée, correction | corpus fermé, seed documentée |
| q-008 | intermédiaire | Plan de groupe accessible | inclusion, matériel, variété | aucune |
| q-009 | transfert | Sortie conditionnelle; alternative | supervision, sécurité, continuité | aucune |
| q-010 | transfert | Replanification de salle occupée | lieu, motif, adaptation | aucune |
| q-011 | transfert | **Preuve 1**, calendrier scolaire de sept jours | R, V, F, S + autonomie | aucune |
| q-012 | transfert | **Preuve 2**, centre communautaire de sept jours | R, V, F, S + autonomie | aucune |

**Chaque ligne** est liée à `obj-1` / `crit-1` / `qc-pri-eps-010-ev-01`. Les champs individuels `objectif_id`, `critere_id` et `family_id` sont présents dans le JSON. `q-011` et `q-012` sont obligatoirement deux administrations séparées, dans des situations différentes; les exercices guidés ne les remplacent pas.

## Protocole d'administration

1. Expliquer le but de planifier; donner **la totalité** de la fiche fictive. Il n'y a ni questionnaire personnel, ni test de vitesse, ni preuve que l'élève a pratiqué l'activité.
2. Pour `q-001`–`q-010`, observer les justifications, offrir le feedback prescrit et réenseigner un critère au besoin. Ces items ne certifient pas à eux seuls la maîtrise.
3. Pour les preuves `q-011` et `q-012`, retirer modèles, amorces et indices de contenu. Donner un calendrier vierge lundi-dimanche sans lignes préremplies de solutions et laisser une période suffisante. Une lecture à voix haute **verbatim**, un agrandissement ou une dictée **fidèle** sont des adaptations d'accès, pas un guidage cognitif.
4. Observer sans proposer activité, créneau, plan B ou justification; recueillir séparément les tableaux et raisons. Remplir `GRILLE_MAITRISE.md` quatre critères R/V/F/S, chacun 0–2.
5. Décider sur les **deux profils** : chacun ≥1 partout, R et S = 2, et une adaptation justifiée; ne pas moyenner deux profils pour masquer un risque. Si manque, remédier précisément et reprendre dans **un troisième cas inédit** validé humainement avant usage (la banque actuelle n'en certifie pas).

## Variabilité, corrigés et contrôles

`q-007` seul a deux **variantes contrôlées**. Variables : `variant_id ∈ {A,B}`. Fonction de sélection : entier `NN` à deux chiffres final dans `EPS010-007-NN`; `NN mod 2 = 0` → A, sinon B. Seed initiale `EPS010-007-08` → A; essai `EPS010-007-09` → B. Chaque stimulus, réponse attendue, limite matérielle et contrainte sont rédigés intégralement dans `parametres.variantes`. Aucune synthèse automatique d'autres scénarios n'est autorisée. Pour tout autre item, `seed=null`, `parametres=null`, réponses évaluées sur éléments **présents dans le dossier** et règles de la grille. Les solutions sont exemples de productions pertinentes; une autre proposition est recevable seulement si elle satisfait **toutes** les contraintes de la fiche. Contrôle technique ≠ validation humaine du jugement pédagogique.

## Sécurité, équité et limites

Permettre versions assises, roulantes, de faible intensité, sans équipement payant et supervision adaptée, sans demander une justification médicale. Ne jamais pénaliser un jour libre ou le repos, ni attribuer une note à la musculature, au poids, à l'endurance, à la vitesse ou à la participation motrice réelle. Si une activité décrite contrevient à un lieu fermé, une météo dangereuse ou une surveillance nécessaire, **S=0 pour cette preuve** jusqu'à correction; une correction après feedback devient formative et ne remplace pas la preuve autonome initiale. Aucun travail à domicile, contact externe, photo, capteur ou partage de données familiales exigés. Revue humaine obligatoire de l'accessibilité, du langage et des scénarios avant usage sommatif.
