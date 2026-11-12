# Plan d'évaluation — `qc-pri-als-011`

**Objectif IMMUTABLE `obj-1` :** Relire et améliorer un texte anglais court à partir de critères ciblés.  
**Critère IMMUTABLE `crit-1` :** Réviser un court message et expliquer deux améliorations.  
**Famille IMMUTABLE :** `qc-pri-als-011-ev-01`. Type : `observation_ou_production`; banque JSON de mode **fixe** (aucun paramétrage aléatoire). Tous les items portent `obj-1`, `crit-1` et la famille ci-dessus, chacun dans sa propre entrée de `BANQUE_ITEMS.json`.

## Construire les preuves

1. Réaliser une tâche d'apprentissage initiale, une tâche intermédiaire et une nouvelle tâche contextualisée, non une suite de choix multiples.
2. Pour chaque item : rendre **le message révisé en anglais** et **deux explications avant/après**; recueillir la version d'origine, les changements, les justifications, le contexte et les aides utilisées. Les explications peuvent être formulées en français.
3. **Deux manifestations de maîtrise obligatoires et distinctes :** `q-009` (invitation à une amie, message informel), puis `q-010` (retour d'un livre, message à un bibliothécaire). Les recueillir à des moments séparés, sans correction affichée et sans aide donnant la solution; garder la trace de la distance entre les séances et des aménagements.
4. Rendre une **décision sur quatre dimensions** (S, M/T, P, A) par contexte et confronter les deux; ne jamais convertir seulement une note en maîtrise.

## Table d'alignement (1 ligne par item)

| Item | Objectif | Critère | Famille | Difficulté | Représentation / contexte | Deux cibles de révision | Rôle |
|---|---|---|---|---|---|---|---|
| `q-001` | obj-1 | crit-1 | qc-pri-als-011-ev-01 | initial | message à une amie | `I is→I am` ; `we→We` | formative |
| `q-002` | obj-1 | crit-1 | qc-pri-als-011-ev-01 | initial | note de fournitures | `We has→We have` ; `They is→They are` | formative |
| `q-003` | obj-1 | crit-1 | qc-pri-als-011-ev-01 | initial | jeu de cartes | `can brings→can bring` ; `can plays→can play` | formative |
| `q-004` | obj-1 | crit-1 | qc-pri-als-011-ev-01 | intermediaire | objet à récupérer | `bag are→bag is` ; `i→I` | formative |
| `q-005` | obj-1 | crit-1 | qc-pri-als-011-ev-01 | intermediaire | goûter/rendez-vous | `I likes→I like` ; `We meets→We meet` | formative |
| `q-006` | obj-1 | crit-1 | qc-pri-als-011-ev-01 | intermediaire | note sur un animal | `dog are→dog is` ; `i→I` | formative |
| `q-007` | obj-1 | crit-1 | qc-pri-als-011-ev-01 | intermediaire | matériel de classe | `pencils is→pencils are` ; `can uses→can use` | formative |
| `q-008` | obj-1 | crit-1 | qc-pri-als-011-ev-01 | intermediaire | note familiale | `I has→I have` ; `am goes→am going` | formative |
| `q-009` | obj-1 | crit-1 | qc-pri-als-011-ev-01 | transfert | invitation à une amie | `game start→game starts` ; `can brings→can bring` | **preuve 1** |
| `q-010` | obj-1 | crit-1 | qc-pri-als-011-ev-01 | transfert | message au bibliothécaire | `I has→I have` ; `can returns→can return` | **preuve 2** |

Les ID complets dans la banque ajoutent le préfixe `qc-pri-als-011-` aux ID courts du tableau (`q-001`, etc.).

## Critères, couverture et barème qualitatif

- **S — Sens :** ne change pas les données (destinataire, objet, lieu, jour, heure, action) ni la fonction du message.
- **M/T — Mots et structure :** deux corrections ciblées sont pertinentes; le résultat est intelligible et grammaticalement adéquat dans le contexte.
- **P — Processus justifié :** deux modifications différentes nommées avec avant/après et raison; une phrase « c'est mieux » ne suffit pas.
- **A — Autonomie :** pas d'indice de correction lors des deux preuves; documenter toute aide d'accès et vérifier qu'elle ne donne pas de réponse.

Chaque critère reçoit le niveau descriptif de `GRILLE_MAITRISE.md`. **S, M/T, P et A doivent être satisfaisants sur les deux preuves**; un score global n'est pas utilisé comme décision automatique. Les items initiaux explorent I/we/they et ponctuation; les intermédiaires couvrent singularité/pluralité, can et présent en cours; les deux preuves changent à la fois destinataire et fonction pragmatique. Un correcteur humain doit examiner les variantes idiomatiques.

## Variabilité, sécurité, accessibilité et limitations

- **Mode fixe :** `seed=null`, `parametres=null` pour tous les items. Aucune permutation ou génération IA libre de textes/corrigés. Seules sont tolérées des variantes de forme conservant le sens, après revue humaine (espacement, ponctuation, contractions justes, propositions idiomatiques équivalentes).
- **Tâche linguistique :** productions en anglais authentique de niveau court; consignes/explications possibles en français. Aucun critère sur l'accent, la calligraphie ou la vitesse. Texte sélectionnable, lecteur d'écran, temps ajusté, clavier ou scribe fidèle autorisés si l'outil ne suggère pas le mot correct.
- **Sécurité :** personnages, lieux et situations fictifs, aucune donnée personnelle, aucune croyance/identité évaluée; ne pas publier les copies individuelles.
- **Contrôles attendus avant certification :** revue linguistique humaine, correction contradictoire de variantes, essai pilote, validation des droits et de l'interface LMS. **État actuel :** `a_revoir` sur chaque item; banque contrôlée en structure, pas certifiée.
