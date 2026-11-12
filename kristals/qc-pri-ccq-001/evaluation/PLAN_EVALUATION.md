# Plan d’évaluation — `qc-pri-ccq-001`

**Objectif invariant :** `obj-1` — Décrire des éléments de l’identité et expliquer leur diversité dans la société.  
**Preuve invariante :** `crit-1` — Analyser un personnage fictif en respectant la pluralité des identités.  
**Famille :** `qc-pri-ccq-001-ev-01` · **Type v1.2 :** `observation_ou_production`.

## Couverture et pondération descriptive

Tous les items servent `obj-1`, `crit-1` et la famille ci-dessus. Il n’existe aucun score lié aux croyances personnelles. Les items q-001 à q-010 sont *formatifs*; q-011 et q-012 sont les deux preuves autonomes obligatoires, de poids qualitatif égal (aucune compensation entre contextes). Les dimensions observées sont D1 faits vérifiés, D2 liens identité-appartenance-expérience, D3 pluralité et respect, D4 prudence face aux inconnues.

| Item | Difficulté | Représentation | Accent / éléments évalués | Contexte / statut |
|---|---|---|---|---|
| `q-001` | initial | tri de phrases | D1, D4 | Léonie; fixe |
| `q-002` | initial | fiche → justification | D1, D2, D3 | Élian; fixe |
| `q-003` | initial | séquence d’expérience | D1, D2, D4 | Iris/Sasha; scénario fermé |
| `q-004` | intermédiaire | comparaison de deux membres | D1, D3 | équipe d’exposition; fixe |
| `q-005` | intermédiaire | reformulation argumentée | D1, D3, D4 | Yan; fixe |
| `q-006` | intermédiaire | carte de quatre rubriques | D1–D4 | Robin/Camil; scénario fermé |
| `q-007` | intermédiaire | observation / cause inconnue | D1, D4 | Édith; fixe |
| `q-008` | intermédiaire | dialogue à reformuler | D1, D3 | Maïa/Alba; scénario fermé |
| `q-009` | intermédiaire | deux hypothèses | D1, D4 | Mina; fixe |
| `q-010` | intermédiaire | commentaire synthétique | D1–D4 | Kim/Eli; scénario fermé |
| `q-011` | transfert | analyse autonome A | D1–D4 | **radio scolaire (Noa)**, inédit, fixe |
| `q-012` | transfert | analyse autonome B | D1–D4 | **jardin collectif (Ari)**, inédit, fixe |

**Codes complets :** préfixer chacun des identifiants `q-xxx` par `qc-pri-ccq-001-`. Les liens `objectif_id`, `critere_id`, `family_id` sont également portés par chaque objet JSON dans `BANQUE_ITEMS.json`.

## Consignes, correction et variabilité

- **Stimulus :** donner intégralement la fiche fictive. Aucune interprétation de la vie réelle ou de l’intimité des élèves.
- **Preuve :** citer au moins deux faits, établir un lien de groupe ou d’expérience, éviter la généralisation et dire ce qui n’est pas documenté.
- **Réponse attendue :** exemples rédigés dans chaque item JSON; accepter d’autres formulations cohérentes et étayées. Ne pas faire d’un texte modèle un mot à mot imposé.
- **Fixes :** q-001, q-002, q-004, q-005, q-007, q-009, q-011, q-012 : faits et exigences inchangés.
- **Scénarios contrôlés :** q-003, q-006, q-008, q-010 : deux variantes pré-écrites chacune; `i = seed modulo 2`; le JSON donne corpus complet, graine, exemple sélectionné et corrigé associé. Aucun générateur libre ni variante inventée par le correcteur.
- **Modalités admissibles :** texte, schéma avec légende, oral confidentiel avec prise de notes; la lecture du stimulus peut être assistée, **sans** indice portant sur la réponse. Les quatre dimensions restent identiques.
- **Limites :** ne pas supposer goûts, genre, origine, croyances, relations familiales ou handicap; ne pas demander leur révélation ni les noter. Un désaccord respectueux sur une hypothèse est accepté si la prudence est explicitée.

## Rubrique et maîtrise

Quatre dimensions, niveaux 0 à 3 définis dans `GRILLE_MAITRISE.md`. L’enseignant ou réviseur relève les **indices**, pas un profil psychologique. Les deux preuves finales doivent chacune atteindre au moins le niveau 2 dans D1–D4 et être réalisées sans guidage sur le contenu, dans les deux contextes distincts. **Pas de score unique ou de moyenne compensatoire.** En cas de dimension insuffisante, remédier puis présenter un troisième cas neuf examiné humainement.

## Sécurité, droits et accessibilité

- Cas originaux, fictifs, non caricaturaux. Aucune reproduction d’image protégée ni utilisation de données réelles d’enfants.
- Option de ne pas prendre la parole publiquement, réponse alternative non numérique et temps supplémentaire. La production orale n’est pas enregistrée sans cadre institutionnel approprié.
- Un élève peut demander de remplacer une vignette sensible sans préjudice; remplacer par une fiche équivalente **approuvée humainement**, pas par une génération libre.
- Examen non certifié; la revue doit contrôler clarté, âge, biais implicites, formulation et faisabilité avec élèves avant toute publication.
