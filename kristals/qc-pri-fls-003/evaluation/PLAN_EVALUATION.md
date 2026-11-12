# PLAN D’ÉVALUATION — `qc-pri-fls-003`

**Objectif `obj-1` :** Distinguer et produire les sons pertinents du français à un niveau intelligible.  
**Critère `crit-1` :** Produire un message oral intelligible après comparaison de modèles.  
**Famille préexistante `qc-pri-fls-003-ev-01`** · mode v1.2 `observation_ou_production` · banque au format `qc.learning-item-bank/1.0`.

## 1. Alignement item par item

| Item | Difficulté | Représentation / contexte | Observables et objet de correction | Rôle |
|---|---|---|---|---|
| `q-001` | initial | deux mots prononcés, choix oral ou image | perception /b,p/ distincte de la production intelligible | formatif |
| `q-002` | initial | trois mots entendus | 2, 2, 3 syllabes selon modèles; ne pas compter les lettres | formatif |
| `q-003` | intermédiaire | dessin et demande orale | partenaire identifie poule/ boule selon la cible | formatif |
| `q-004` | intermédiaire | question vs affirmation contextualisées | intention interrogative transmise, contour libre | formatif |
| `q-005` | intermédiaire | demande à l’école | la salle de musique et la recherche comprises | formatif |
| `q-006` | intermédiaire | phrase pain/bain | distinction lexicale intelligible; réparation | formatif |
| `q-007` | intermédiaire | catalogue A/B cahier bleu / boîte rouge | référent exact et question compréhensible | variation contrôlée |
| `q-008` | intermédiaire | catalogue A/B sous / sur table | relation spatiale entendue et demande | variation contrôlée |
| `q-009` | transfert | P1 piscine fictive, localiser l'accueil | message libre mais intelligible après deux modèles; autonomie | preuve 1 |
| `q-010` | transfert | P2 musée fictif, demander l’heure | question sur début de visite, contexte distinct; autonomie | preuve 2 |

**Chaque item est lié à `obj-1`, `crit-1` et `qc-pri-fls-003-ev-01` dans la banque**, et évalué dans ses limites propres. Les items 1–2 renseignent la perception et la syllabation; seuls des messages oraux contextuels peuvent contribuer directement à la preuve `crit-1`.

## 2. Protocole et modalité

1. Installer le sens des mots rares, à l’oral, sans lire ni traduire de force; la connaissance lexicale n’est pas confondue avec la production phonologique.
2. Une personne maîtrisant le français oral prononce **en direct** les scripts de chaque item, dans une variété naturelle intelligible; aucune piste audio n’est fournie dans l'archive.
3. Dans `q-009` et `q-010`, comparer d’abord deux modèles et laisser un temps de préparation; lors de l’essai coté, cacher les scripts et retirer les indices. Une clarification auto-initiée par l’élève peut être notée sans la confondre avec l’aide de l’enseignant.
4. L'interlocuteur ne connaît pas à l'avance les mots cibles et restitue le message entendu, afin de limiter l’anticipation ou la complaisance. Conserver un résumé observé et non un jugement global d’accent.
5. Évaluer avec la grille à quatre dimensions de `evaluation/GRILLE_MAITRISE.md`; l’intention et l’information essentielles doivent passer dans **deux situations distinctes**, sans imposer une identité sonore avec les modèles.

## 3. Variabilité et reproductibilité

- `q-001..006,009,010` : fixes, dialogues et critères fournis; la **production ouverte** est jugée par une grille, pas par égalité à une chaîne de caractères.
- `q-007` : deux variantes textuellement verrouillées, `seed=104`, sélection `104 % 2 = 0` → scénario A : cahier bleu.
- `q-008` : deux variantes verrouillées, `seed=105`, sélection `105 % 2 = 1` → scénario B : sur la table.
- Chaque item variable intègre `variables`, domaines, contraintes, algorithme, correction de chaque variante, limites de substitution et exemple contrôlé. Aucune IA ne produit ou valide librement des réponses.
- Toute nouvelle variante contextuelle doit faire vérifier par une personne compétente la stabilité du sens, l’équité lexicale et la possibilité réelle d’entendre les contrastes.

## 4. Couverture et décision

- **Phonème** : q001, q003, q006, q008; **syllabe** : q002; **rythme/prosodie** : q004, q005, q007–q010; **intelligibilité en situation** : q003–q010.
- **P1 `q-009`** : localiser l’accueil dans une piscine fictive; **P2 `q-010`** : demander l’horaire d’une visite dans un musée fictif. Ces deux contextes sont distincts du modelage guidé et des exercices sur bibliothèque/autobus.
- Décision de maîtrise : pour **chacune** des preuves P1 et P2, au moins « satisfaisant » dans les dimensions pertinentes de la grille, sans aide pendant l’essai, avec confirmation de compréhension par l'interlocuteur. Aucune moyenne entre une preuve faible et une preuve forte.
- Si une dimension échoue : enseigner cette dimension, puis refaire un **nouveau** contexte non mémorisé; n’exiger ni imitation d’un accent ni répétition d’un mot exact pour toutes les formes recevables.

## 5. Sécurité, droits et accessibilité

- Aucun enregistrement obligatoire, aucune interaction avec des inconnus réels, aucune notation de nationalité, d'accent, de personnalité ou de vulnérabilité. Les lieux et partenaires sont fictifs.
- Autoriser un environnement calme, des supports visuels facultatifs, préparation sans lecture obligatoire, choix d'interlocuteur et pauses. Les modalités écrites sont des supports, **non des preuves suffisantes** d’expression orale.
- En cas de limitation auditive ou vocale nécessitant un aménagement qui modifie l’objectif, prévoir concertation professionnelle; consigner « preuve orale non observable dans la modalité donnée » au lieu de simuler une validation.
- Matériel original produit dans ce lot; modèles oraux humains à préparer; aucune piste audio ni droit de reproduction tiers prétendu. Les items restent `a_revoir` et exigent revue linguistique, expérience utilisateur et accord interobservateurs.
