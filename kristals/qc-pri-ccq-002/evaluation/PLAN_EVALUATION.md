# Plan d'évaluation — `qc-pri-ccq-002`

**Alignement immuable :** `obj-1` — « Comparer des façons de vivre les relations et les responsabilités partagées. » · `crit-1` — « Proposer des réponses argumentées à une situation relationnelle fictive. » · **famille :** `qc-pri-ccq-002-ev-01` · **type natif :** `observation_ou_production`.

## Tâches et table de couverture

Chaque item est relié à **`obj-1`, `crit-1`, `qc-pri-ccq-002-ev-01`**; le stimulus est fictif et les réponses exemplaires **non exclusives**. « Contrôlé » indique le choix entre deux variantes rédigées et vérifiables, pas une réponse déterministe obligatoire.

| Item | Difficulté | Représentation | Mode | Accent distinct |
|---|---|---|---|---|
| q-001 | initial | vignette texte/orale | fixe | partage d'une feuille de consignes |
| q-002 | initial | vignette texte/orale | fixe | classement, comparaison de méthodes |
| q-003 | initial | description de lieu | fixe | placement et passage libre |
| q-004 | initial | tableau de rôles possible | fixe | règle uniforme et répartition des tâches |
| q-005 | intermédiaire | tableau actions/temps | fixe | outil partagé et vérification |
| q-006 | intermédiaire | proposition écrite/orale | fixe | participation multiforme |
| q-007 | intermédiaire | vignette A ou B contrôlée | scenario_controle | partage du travail et d'un outil |
| q-008 | intermédiaire | vignette A ou B contrôlée | scenario_controle | coordination et contrôle de production |
| q-009 | transfert | texte avec règle | fixe | bénévolat fictif et arrivée tardive |
| q-010 | transfert | vignette A ou B contrôlée | scenario_controle | prise de décision et modes d'expression |
| q-011 | transfert · **preuve 1** | projet de pont de papier, texte ou lecture orale | fixe | négociation de rôles, documents et outils |
| q-012 | transfert · **preuve 2** | site public fictif, vignette A/B | scenario_controle | accès à l'espace, vérifications et répartition |

## Critères et rubrique communs

La grille `GRILLE_MAITRISE.md` décrit quatre dimensions avec niveaux 0–3 : **F** faits et concepts, **C** comparaison/perspectives, **R** organisation/règle/respect, **J** justification/adaptation. Ne pas noter les convictions, identités, expériences familiales, traits supposés, aisance orale, grammaire ou accents. Pour une réponse différente du modèle, vérifier les faits et les critères, pas l'accord avec une décision « morale » imposée.

## Variabilité contrôlée et précautions

- **q-001–006, 009, 011 :** vignettes et prompts fixes; reformulation pédagogique équivalente autorisée, mais pas d'introduction de nouveaux faits et aucun outil de génération libre.
- **q-007, 008, 010, 012 :** deux versions A/B intégralement rédigées chacune, seed entière stable. Algorithme `index = seed % 2`, le stimulus et sa réponse illustrative sont copiés de la **même** variante. Voir `parametres`, `seed` et les deux instances testables de `BANQUE_ITEMS.json`. Aucun classement psychologique ou générateur libre.
- Pour chaque variante, conserver les quatre critères cognitifs; la justification dépend des détails de son récit. Les évaluations sont **à revoir humainement** pour lisibilité et équité avant usage sommatif.
- Modalités d'accès : lecture par l'adulte, réponse dictée/orale/écrite/schéma annoté; aucun débat public obligatoire. Les tâches s'appliquent aux **personnages inventés**, pas au vécu des apprenants.

## Décision de maîtrise et collecte

1. Après entraînement, administrer `q-011` et `q-012` sans indices de raisonnement et **en contextes indépendants** : construction coopérative vs aménagement d'un espace collectif.
2. Deux productions recueillies séparément; inscrire observations par dimension F/C/R/J, les citations factuelles et les conséquences envisagées. Consigner seulement la compétence, jamais un récit de vie.
3. **Seuil qualitatif retenu en interne :** sur chacune des deux productions, F,C,R,J ≥2/3; aucun propos dénigrant un personnage présenté comme une preuve, et aucune invention de faits décisifs. Un propos maladroit peut être repris et apprécié sur la version corrigée. La maîtrise n'est jamais décidée sur une moyenne ou un seul score.
4. Si un critère manque dans une des deux preuves, proposer la micro-remédiation correspondante et un **nouveau** contexte inédit, sans réutiliser le même texte comme preuve indépendante.

## Sécurité, protection et limites

Aucune confidence intime recherchée, aucun témoignage de conflit personnel, intimidation ou conviction. Aucune photo ou enregistrement nominatif requis; consentement et procédure locale hors de ce document si une modalité nécessite un enregistrement. Les corrigés illustrent des raisonnements recevables; leur revue doit notamment contrôler biais, niveaux de langue et âge du public. Pas de prétention de conformité au PFEQ, d'examen certifié ni de validation psychométrique.
