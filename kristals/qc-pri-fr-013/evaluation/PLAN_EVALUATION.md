# Plan d'évaluation — qc-pri-fr-013 · v1.2 (brouillon contrôlé)

| Champ | Contrat intangible |
|---|---|
| Kristal | `qc-pri-fr-013` — **Classes de mots** |
| Discipline | Français, langue d’enseignement |
| Objectif unique | `obj-1` — Identifier la classe grammaticale de mots selon leur fonctionnement en phrase. |
| Critère principal | `crit-1` — Classer des mots en contexte et justifier deux cas ambigus. |
| Famille | `qc-pri-fr-013-ev-01` |
| Mode privilégié | `réponse_argumentée` ; items **fixes**, pas de génération IA libre |
| Notions | nom, déterminant, adjectif, verbe, pronom |
| Préconditions | aucune dépendance `requires` ; diagnostic non bloquant |

## Plan d'instrumentation et traçabilité

Tous les items ci-dessous portent **directement et explicitement** `objectif_id: obj-1`, `critere_id: crit-1`, `family_id: qc-pri-fr-013-ev-01` dans la banque JSON. Pour les items d'entraînement, `crit-1` est exercé par classement ou justification partielle, et **non attesté en totalité**; les items q-009 et q-010 sont les preuves complètes.

| Item | Type / complexité | Représentation | Couverture / tâche | Place dans le dispositif |
|---|---|---|---|---|
| `q-001` | fixe, initial | deux phrases écrites | cinq classes, repères simples | préformative |
| `q-002` | fixe, intermédiaire | paire de phrases | `les` déterminant / pronom, justification | discrimination |
| `q-003` | fixe, intermédiaire | paire de phrases | `marche` nom / verbe | discrimination |
| `q-004` | fixe, initial | phrase à GN étendu | déterminant / adjectif / nom / verbe | compréhension |
| `q-005` | fixe, intermédiaire | petit récit | pronoms sujet et complément | compréhension |
| `q-006` | fixe, intermédiaire | deux phrases | `ferme` nom / verbe, `porte` nom | discrimination |
| `q-007` | fixe, intermédiaire | deux phrases | deux adjectifs, déterminant, nom, verbe, pronom | transfert local |
| `q-008` | fixe, intermédiaire | assertion à réfuter | `porte` nom / verbe, contre-exemple | argumentation |
| `q-009` | fixe, transfert | scène de bibliothèque | 12 classements, cinq classes, 2 cas ambigus A7 et A11 | **preuve A autonome** |
| `q-010` | fixe, transfert | scène de randonnée | 12 classements, cinq classes, 2 cas ambigus B2 et B9 | **preuve B autonome** |
| `q-011` | fixe, transfert | dialogue écrit | `le` déterminant / pronom | maintien/transfert |
| `q-012` | fixe, transfert | oral neutre ou écrit | six classements, justification de pronom et adjectif | accessibilité / rappel |

**Repérage :** l'item fournit une liste numérotée de mots/occurrences (`reperes_eleves`); chaque élément doit être montré en contexte intégral. Le corrigé structuré (`corrige_structure`) est **réservé au correcteur** et non exposé à l'élève. Une même graphie répétée est repérée par position (ex. *le* avant le nom vs *le* devant le verbe). Les réponses libres sont jugées par des règles explicites, jamais sur des mots-clés seuls.

## Critères de correction et poids

La grille commune `GRILLE_MAITRISE.md` est l'autorité locale. Pour chaque preuve A et B, recueillir :

1. **Exactitude** : 12 occurrences correctement classées, en tenant compte des cinq classes (indicateur quantitatif, pas unique décision).
2. **Deux justifications fonctionnelles distinctes** : pour les deux mots ambigus désignés, donner la classe en contexte, citer un indice (introduit un nom / reprend un GN / noyau nominal / variation temporelle) **et** distinguer un autre emploi possible de la même forme. Deux justifications valides sont essentielles; éviter la notation selon la longueur du texte.
3. **Autonomie** : aucune aide sur les indices pendant le travail; lecture neutre, police adaptée et dictée littérale permises; trace de l'accommodement.
4. **Transfert** : stabilité dans un contexte différent (bibliothèque puis randonnée), sans récitation de l'exemple modèle.

**Indicateur opérationnel à examiner par un humain :** sur chacune des deux épreuves, au moins **10 classes justes sur 12**, **les cinq classes représentées sans erreur de catégorie systématique**, et **les deux justifications ambiguës recevables et autonomes**. Une seule réussite ou un score total cumulé ne suffit pas. Si 10/12 est atteint mais qu'un type de classe est systématiquement confondu, ajourner et remédier. Aucune automatisation ne doit attribuer la maîtrise définitive sans vérifier les justifications et les deux contextes.

## Variabilité et contrôle des générateurs

- **Mode effectif : `fixe` pour les 12 items.** Aucune variable échantillonnée, aucun tirage, seed `null` et paramètres `null`. Les mentions de familles adaptables dans le contrat v1.2 ne constituent **pas** une implémentation paramétrique.
- **Variation admise sans changer l'item :** lecture humaine neutre, synthèse vocale fidèle, réponse orale dictée mot pour mot, agrandissement des caractères; les mêmes phrases et repères doivent être conservés.
- **Variation non admise sans nouvelle révision :** remplacer des mots, changer leur ordre, isoler les occurrences du contexte, substituer de nouvelles phrases, ou accepter un corrigé inventé par une IA. Tout changement pourrait modifier la classe grammaticale ou l'ambiguïté; créer une **nouvelle version**, vérifier son corrigé et consigner la revue humaine.
- En cas de test sur d'autres contextes, élaborer un corpus de remplacement **revu et approuvé** en amont; le corpus n'existe pas encore et n'est pas revendiqué comme livré.

## Sécurité, droits, équité et accessibilité

Texte original ne contenant aucune information sur un apprenant réel. Aucun enjeu corporel, convictions, identité ou divulgation personnelle évalué. Le raisonnement grammatical est seul coté; la prononciation, la calligraphie, l'orthographe d'une justification dictée, le débit de lecture ou l'accent québécois ne sont pas notés. Des supports textuels accessibles sans code couleur sont proposés. Les graphies sont conservées pendant la passation; à l'oral, le lecteur doit distinguer chaque occurrence par son contexte et sa phrase, sans indiquer la réponse.

## Revue humaine requise avant qualification

Valider indépendamment les 12 corrigés et indices, tester sur des apprenants représentatifs, contrôler clarté et temps, décider de la robustesse du seuil indicatif de 10/12, vérifier l'accessibilité effective (lecteur d'écran/présentation des repères) et toute politique locale relative aux traces. **Statut : à revoir, non certifié, non homologué et non publié.**
