# Plan d'évaluation — `qc-pri-fls-006` (v1.2)

**`obj-1` :** Lire un texte français adapté et en identifier sens global et détails. **`crit-1` :** Répondre à des questions sur un texte court inconnu. **Famille unique :** `qc-pri-fls-006-ev-01`. **Type natif :** `observation_ou_production`, exprimé par des réponses à des questions sur passages **écrits**. L'accent, la graphie, la longueur de la réponse et la vitesse brute ne sont pas des critères de lecture-compréhension.

## Plan de couverture

Pour **chaque item du tableau**, liens exacts **`obj-1` / `crit-1` / `qc-pri-fls-006-ev-01`**; chacun est référencé dans la banque JSON avec `objectif_id`, `critere_id` et `family_id`. Les huit premiers éléments sont formatifs ou préparent le transfert; les deux derniers constituent les preuves autonomes complètes.

| Item complet | Niveau | Représentation / situation | Critères et compétence couverte | Usage |
|---|---|---|---|---|
| `qc-pri-fls-006-q-001` | initial | court récit Paul/Sara, texte écrit + repérage | sujet, lieu, personnage, indice | formatif |
| `qc-pri-fls-006-q-002` | initial | recette de fruits en contexte | activité, nombre, rangement | formatif |
| `qc-pri-fls-006-q-003` | initial | visite du musée, chronologie | sujet, date, objet, ordre après | formatif |
| `qc-pri-fls-006-q-004` | intermédiaire | avis d'autobus, texte fonctionnel | horaire, lieu, négation « ne…pas » | formatif |
| `qc-pri-fls-006-q-005` | intermédiaire | matériel d'atelier, contraste | sujet, quantité, absence, lieu, indice | formatif |
| `qc-pri-fls-006-q-006` | intermédiaire | récit gourde/personnages | chercher vs trouver, référent et lieu | formatif |
| `qc-pri-fls-006-q-007` | intermédiaire | avis de club de lecture | règle, quantité, jours et négation | formatif |
| `qc-pri-fls-006-q-008` | transfert | annonce d'atelier culturel | sens global, jour/heure, matériel et durée | préparation transfert |
| `qc-pri-fls-006-q-009` | transfert | **A : récit de bibliothèque** | idée principale + 3 détails + indice textuel + lecture autonome | **preuve de maîtrise A** |
| `qc-pri-fls-006-q-010` | transfert | **B : jardin du quartier** | idée principale + 3 détails + indice textuel + lecture autonome | **preuve de maîtrise B** |

## Conditions de passation et autonomie

1. Proposer le court texte inédit écrit après un enseignement/entraînement distinct. On peut agrandir les caractères, moduler la durée, utiliser un cache-ligne, lire les **questions** ou accepter des réponses orales, écrites, pointées ou dictées à un scribe neutre.
2. Éviter toute reformulation du passage ou indication du mot-réponse. Lire à l'élève la totalité du texte, utiliser une synthèse vocale pour le passage ou offrir un résumé transforme possiblement l'activité en **compréhension orale** : documenter le changement et faire valider l'équivalence de construit par un professionnel au lieu d'affirmer l'autonomie en lecture.
3. Laisser l'élève répondre à une question de **sens global**, aux **trois questions de détails** et montrer l'**indice textuel** d'au moins une réponse; noter exactement les erreurs de compréhension et les aides utilisées.
4. Administrer A et B sur des passages réellement distincts, éventuellement à des séances différentes; ne pas réutiliser les exemples d'enseignement ni les corrigés dévoilés. Aucun algorithme de génération libre.

## Variations permises et limites

Toutes les entrées de `BANQUE_ITEMS.json` sont de mode **`fixe`** : aucun tirage aléatoire, seed `null`, paramètres `null`. Les textes, questions, faits et réponses de référence sont contrôlés et **non variables**; seule la forme de présentation, les aménagements préalables et le canal de réponse peuvent changer. Des paraphrases qui gardent le même fait sont admises. Ne pas accepter une réponse incompatible sous prétexte de créativité ou de vécu personnel.

## Règle de décision

Les critères M1–M4 de `GRILLE_MAITRISE.md` sont observés **pour A et B séparément**; sur chacun, idée globale suffisante, trois détails exacts, un indice juste et autonomie sans indice directif. La décision ne provient pas d'une moyenne compensant l'absence d'un élément essentiel. Les difficultés se remédient par composante, puis la personne passe une épreuve alternative créée et validée humainement, différente des deux textes divulgués.

## Accessibilité, biais et limites de validation

Réponses sans sanction de prononciation ou d'orthographe; lexique de textes courts sans prérequis culturel présumé; situations fictives (bibliothèque et jardin), aucun récit intime demandé. La banque et le seuil sont proposés pour revue humaine, non étalonnés et non certifiés. La source du texte évalué est une production originale interne, non une lecture d'oeuvre protégée.
