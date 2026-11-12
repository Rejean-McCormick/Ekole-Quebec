# Plan d'évaluation — qc-pri-eps-008 | version de rédaction v1.2

**Objectif immuable :** `obj-1` — Reconnaître une situation à risque et appliquer les consignes de prévention. **Critère immuable :** `crit-1` — Repérer des risques dans un scénario et proposer une action sûre. **Famille immuable :** `qc-pri-eps-008-ev-01`. **Mode privilégié :** `observation_ou_production`. Les réponses sont des **décisions motivées observables**, pas des choix multiples obligatoires ni des performances motrices chronométrées.

## Corpus contrôlé et représentation

La banque compte **12 cartes fixes**, originales, `q-001` à `q-012`. Chaque item est rattaché à `obj-1`, `crit-1` et `qc-pri-eps-008-ev-01`, avec stimulus, consigne, réponse attendue, critères et retour individuel. `mode=fixe` : **aucun tirage**, `seed=null`, `parametres=null`, aucun contexte libre généré par IA. Une autre représentation textuelle, auditive ou en pictogrammes fidèles peut être utilisée **si elle conserve** tous les dangers et indices, le moment de l'action et l'adulte responsable; ne pas remplacer un cas par un autre sans nouvelle validation.

| Item | Complexité | Support / situation fictive | Réponse/production clé | Rôle |
|---|---|---|---|---|
| q-001 | initial | gym, sac sur trajectoire | nommer obstacle, arrêter, alerter | ancrage zone |
| q-002 | initial | réception de ballon et traversée | séparer les zones sous supervision | ancrage espace |
| q-003 | initial | démarrage intense sans préparation | entrée progressive, règle d'arrêt | échauffement |
| q-004 | initial | protection endommagée | ne pas utiliser, alerter | pratique autonome 3 |
| q-005 | intermédiaire | élève tombé avec douleur | arrêter, prévenir, ne pas déplacer | aide |
| q-006 | intermédiaire | surface humide | interdire le passage, alerter | surface |
| q-007 | intermédiaire | passage inaccessible | adapter sous supervision | accessibilité |
| q-008 | intermédiaire | trajectoires de lancer/jeu | suspendre, délimiter et signaler | processus |
| **q-009** | **transfert** | **gymnase : croisement + sacs** | **deux risques, arrêt, proposition et motif** | **preuve de maîtrise A** |
| **q-010** | **transfert** | **cour : sol humide + sac** | **deux risques, arrêt, solution et motif** | **preuve de maîtrise B** |
| q-011 | intermédiaire | absence du signal de l'adulte | ne pas commencer, demander consigne | supervision |
| q-012 | transfert | choc à la tête + étourdissement | arrêter, alerter, pas de reprise | sécurité complémentaire |

**Couverture des notions :** zone (q-001, 002, 006, 007, 008, 009, 010, 011); échauffement (q-003); protection (q-004, 008); aide/supervision (tous, explicitement q-005, 011, 012). La preuve autonome synthétique est centrée sur q-009 et q-010; les autres items étayent les apprentissages, sans réduire l'objectif à une simple définition.

## Rubrique commune (voir `GRILLE_MAITRISE.md`)

Chaque carte produit une trace de : **R** repérage du danger, **S** décision/action sûre et proportionnée, **A** alerte/justification et recours à l'adulte. Niveaux descriptifs : 0 = non démontré/risqué, 1 = partiel, 2 = démontré de façon sûre et explicite. **Critère de sécurité non compensable :** une proposition de poursuivre dans un danger non maîtrisé, de déplacer sans motif un blessé, de réparer soi-même un appareil incertain ou de reprendre après un possible choc à la tête nécessite remédiation; un total chiffré ne compense pas cela.

## Maîtrise : deux contextes indépendants

- **Preuve A :** `q-009`, gymnase (croisement d'itinéraires et sacs).
- **Preuve B :** `q-010`, cour d'école (sol humide et passage obstrué).
- Pour chacune : **R=2 et S=2 et A≥1**, **aucune réponse gravement dangereuse**, et sans aide sur les solutions. L'évaluateur s'assure que les deux risques présents sont repérés et que l'action ne crée pas un nouveau danger. Les deux cartes sont administrées séparément, idéalement à des séances différentes; si une réponse est apprise par cœur, utiliser une nouvelle variante **révisée par un humain**, pas une génération automatique.
- Compléter par un entretien bref de vérification ou par une trace sur `q-004` / `q-012` si nécessaire. Aucune note unique, rapidité, morphologie, habileté brute ou information médicale personnelle ne détermine la maîtrise.

## Variabilité permise et interdite

**Permis sans changer la réponse :** lecture par l'adulte, typographie agrandie, description audio fidèle, supports tactiles/plans accessibles, temps supplémentaire, dictée par un tiers neutre, réponse orale/écrite/assistée, pointage sur un plan clair. Tout cela doit être documenté comme **aménagement d'accès**, distinct d'un indice de correction.

**Interdit sans revue :** remplacer les conditions de sécurité, introduire un nouveau sport/équipement avec règles spécifiques, jouer réellement un accident, supprimer un des dangers des preuves A/B, souffler l'arrêt ou le risque, ajouter une règle de premiers secours, imposer la même capacité motrice, ou produire des variantes libres par IA. Les énoncés restent fictifs; l'enseignant vérifie la compatibilité avec les consignes et installations locales avant tout usage.

## Sécurité, droits, revue

Cartes textuelles originales, sans images tierces ni données personnelles, sans diagnostic médical; si une alerte survient en activité réelle, arrêter et faire intervenir l'adulte selon le protocole local. Validation de structure JSON et contrôle de cohérence **ne valent pas** validation de la grille en situation, revue de la sécurité par professionnel, test d'accessibilité auprès d'élèves, ni homologation officielle. Sources à distinguer : `sources/REFERENCES_CONTENU.md`. Statut de tous les items : `a_revoir`.
