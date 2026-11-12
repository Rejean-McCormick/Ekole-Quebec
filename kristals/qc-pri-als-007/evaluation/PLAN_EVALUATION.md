# Plan d’évaluation — `qc-pri-als-007`

**Famille immuable :** `qc-pri-als-007-ev-01` (type du contrat v1.2 : `observation_ou_production`). **Objectif `obj-1` :** Extraire le sens d’un court texte écrit anglais adapté. **Critère `crit-1` :** Associer des phrases à des informations et repérer un détail précis.

## Couverture des items (tous reliés à `obj-1`, `crit-1`, `qc-pri-als-007-ev-01`)

| Item | Contexte du texte | Difficulté | Représentation | Cible du détail | Utilisation |
|---|---|---|---|---|---|
| `q-001` | Étagères de jeux | initial | avis / texte anglais en 3 repères | Quel jour le magasin est-il fermé? | évaluation formative |
| `q-002` | Carte d’invitation | initial | avis / texte anglais en 3 repères | De quelle couleur doit être la tasse? | évaluation formative |
| `q-003` | Potager de classe | initial | avis / texte anglais en 3 repères | Où sont les pots? | évaluation formative |
| `q-004` | Menu de la collation | initial | avis / texte anglais en 3 repères | À quelle heure ferme le comptoir? | évaluation formative |
| `q-005` | Soins au chat | intermediaire | avis / texte anglais en 3 repères | De quelle couleur est le bol d’eau? | évaluation formative |
| `q-006` | Avis de pluie | intermediaire | avis / texte anglais en 3 repères | Quelle couleur de manteau est demandée? | évaluation formative |
| `q-007` | Trajet en train | intermediaire | avis / texte anglais en 3 repères | Où Nora est-elle assise? | évaluation formative |
| `q-008` | Match de soccer | intermediaire | avis / texte anglais en 3 repères | De quelle couleur sont les chandails des joueurs? | évaluation formative |
| `q-009` | Club d’ordinateur | transfert | avis / texte anglais en 3 repères | À quelle heure finit le club? | évaluation formative |
| `q-010` | Nettoyage de plage | transfert | avis / texte anglais en 3 repères | Où a lieu le rendez-vous? | évaluation formative |
| `q-011` | Musée : information aux visiteurs | transfert | avis / texte anglais en 4 repères | Où doit-on retrouver le guide? | preuve autonome A |
| `q-012` | Club de nature : sortie | transfert | avis / texte anglais en 4 repères | À quelle heure finit la marche? | preuve autonome B |

## Énoncé, correction et pondération

La banque JSON contient **12 stimuli complets originaux**, avec questions de correspondance, un détail précis et une demande de sens global. Chaque stimulus est figé en anglais écrit; les repères A/B/C/D font partie de la présentation et non d'un index de réponse communiqué à l'élève. Les critères et corrigés textuels sont intégrés à chaque item. Il n'y a **pas** de paramètre génératif ni de seed dans les 12 modes fixes : `seed: null`, `parametres: null`. Toute variation textuelle exige une nouvelle validation humaine du corrigé, du sens, du vocabulaire et de la difficulté.

**Observation formative par item :** (i) associations correctes (2 ou 3), (ii) détail exact, (iii) preuve directement retrouvée dans l'anglais écrit, (iv) sens global cohérent. Les réponses peuvent être exprimées en français, anglais, lettre, pointage ou copie; la précision de l'orthographe et de l'accent n'est pas évaluée. La correction exige un lien entre la valeur et la **phrase entière**, plutôt qu'un mot choisi au hasard.

**Conditions de maîtrise :** seules `q-011` (annonce aux visiteurs du musée) et `q-012` (sortie nature) servent de preuves finales prévues : au moins 2/3 associations exactes dans **chacun** des deux contextes, détail exact avec preuve écrite montrée, idée globale cohérente, aucun indice révélant la réponse. Réussite des **deux** preuves, et observation du processus; un score compensatoire global n'est pas admis. Les items `q-001` à `q-010` situent et entraînent, mais ne remplacent pas les deux preuves.

## Variabilité et équité

- **Corpus contrôlé :** A/B/C/D et les mots anglais sont conservés; les seules variantes admises sans création d'un nouvel item sont des modalités **équivalentes de réponse** (oral en français, pointage, surlignage, frappe) et la présentation agrandie/contrastée. L'ordre des repères reste stable dans cette livraison.
- **Sécurité :** annonces et personnages fictifs, pas de photographie personnelle, ni adresse, ni déplacement réel demandé; aucune connaissance de la ville, du musée ou du milieu de vie n'est requise.
- **Accessibilité :** consignes françaises lisibles à haute voix; corps de texte anglais écrit disponible aussi en caractères agrandis, et tout visuel accompagné de texte. Éviter dépendance à la couleur, minutage normatif, lecture orale forcée, lexique exclusif à un groupe culturel.
- **Construct évalué :** lecture d'un **texte anglais écrit**, non compréhension à l'écoute ni production orale. Un lecteur d'écran ou une lecture vocale de l'anglais peut être requis comme accommodement : l'indiquer dans la trace, expliquer la limite interprétative et chercher une preuve écrite accessible complémentaire.
- **Validation humaine avant usage qualifiant :** vérifier naturalité de l'anglais, sens des alternatives et des détails, niveau de difficulté, biais, lisibilité réelle auprès du public et interprétation des accommodements.

## Traçabilité

Chaque `item_id` `qc-pri-als-007-q-001` … `-012` porte `objectif_id: obj-1`, `critere_id: crit-1`, `family_id: qc-pri-als-007-ev-01`, `validation_status: a_revoir`. Les corrigés structurés indiquent l'association et la preuve exacte. Grille décisionnelle : `evaluation/GRILLE_MAITRISE.md`. Ne pas utiliser une IA générative libre comme vérificateur de réponses; le jugement de la preuve par pointage/surlignage reste contrôlé par une personne.
