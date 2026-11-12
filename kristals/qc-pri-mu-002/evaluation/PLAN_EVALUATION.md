# Plan d'évaluation — `qc-pri-mu-002`

**Identifiants constants pour tous les items 001–010 :** `obj-1`, `crit-1`, famille `qc-pri-mu-002-ev-01`. **Objectif :** Reproduire et créer des motifs avec pulsation et durées. **Preuve :** Reproduire puis inventer un motif rythmique stable.

## Noyau et modes d'épreuve

- **Mode commun de la famille v1.2 :** `observation_ou_production` ; les dix items de `BANQUE_ITEMS.json` utilisent le **mode `fixe`**, avec `seed: null`, `parametres: null` : stimuli figés, rubriques observables, aucune génération de motifs par IA.
- **Notation locale et explicitée** : une case par pulsation, `A` = attaque d'un battement, `H` = prolongement sans nouvelle attaque du son/geste précédent pendant un battement, `R` = un battement silencieux. Les créations sont issues d'un **catalogue de six permutations valides** de `A,A,H,R`, avec `H` immédiatement après `A` (et jamais seul au début). Une tenue continue de deux battements et un repos distinct sont obligatoires.
- **Équivalence d'accès** : impulsions sonores douces, gestes continus accessibles, cartes tactiles/visuelles, présentation avec rythme neutre. Si la performance sensorimotrice n'est pas accessible, ne pas conclure à une maîtrise non observée; faire décider humainement d'une adaptation équivalente.

## Matrice item → cible, difficulté, représentation et contrôle

**Tous les codes ci-dessous complètent l'ID `qc-pri-mu-002-q-...`**; chaque ligne lie explicitement `obj-1 / crit-1 / qc-pri-mu-002-ev-01` (référence identique dans la banque JSON).

| Item complet | Niveau | Représentation | Réponse / observables | Fonction |
|---|---|---|---|---|
| `qc-pri-mu-002-q-001` | initial | 4 cases + description | `A H R A` : attaques 1,4, tenue 2, repos 3, 4 pulsations | Repérage conceptuel |
| `qc-pri-mu-002-q-002` | initial | A A vs A H | 2 attaques vs 1, durées 1+1 vs 2 | Discrimination |
| `qc-pri-mu-002-q-003` | initial | R A A H + performance | attaques 2,3; repos 1; tenue 4 | Imitation courte |
| `qc-pri-mu-002-q-004` | intermédiaire | notation erronée | `H A R A` invalide; correction H après A | Correction raisonnée |
| `qc-pri-mu-002-q-005` | intermédiaire | A R A H, deux tours | attaques 1,3; repos 2; tenue 4; tempo | Reproduction |
| `qc-pri-mu-002-q-006` | intermédiaire | R A H A | attaques 2,4; tenue 2–3; repos 1 | Explication de durée |
| `qc-pri-mu-002-q-007` | intermédiaire | termes et groupes de battements | « quadruple » ≠ « simple »; division binaire | Modèle musical exact |
| `qc-pri-mu-002-q-008` | transfert | création « galerie de lumière » | motif parmi six permutations valides et deux reprises | Transfert formatif |
| `qc-pri-mu-002-q-009` | transfert | **preuve A**, phare imaginaire | reproduire `A H R A` deux fois; inventer autre permutation deux fois | **Maîtrise A** |
| `qc-pri-mu-002-q-010` | transfert | **preuve B**, train imaginaire | reproduire `R A A H` deux fois; inventer un troisième motif distinct deux fois | **Maîtrise B** |

## Couverture et maîtrise

Les items 001–003 couvrent pulsation, durée et silence; 004–007 testent règle de tenue, reprise et distinction théorique de mesure simple; 008 travaille le transfert. **Seuls 009 et 010, ensemble**, couvrent l'ensemble du critère `crit-1` en contexte de maîtrise : écoute / perception, reproduction de la durée, création personnelle, stabilité et autonomie. Ils ne sont pas interchangeables avec un QCM ou un unique total.

**Administration :** pour chaque preuve, exposer le modèle fixe une fois avant l'essai, permettre de préparer un plan de quatre cases et donner uniquement un départ neutre, puis observer deux tours de reproduction et deux tours de création. Ne pas frapper le modèle en même temps que l'élève et ne pas corriger pendant la performance. L'élève garde un rythme personnel assez lent pour sa modalité choisie; la pulsation est évaluée par régularité relative, non BPM imposés. L'adulte note chaque événement en case et toute aide fournie.

## Variabilité autorisée et validation

- **Permis :** intensité basse, timbre/outil sûr choisi, posture, tempo personnel régulier, visualisation ou repères tactiles non directifs, pauses entre essais, dispositif d'accès préautorisé.
- **Interdit :** remplacer les modèles `A H R A` ou `R A A H`, changer quatre temps en trois dans ces items, supprimer la tenue ou le repos, fournir les attaques durant la prestation ou classer un son selon les goûts / capacités physiologiques.
- **Contrainte du catalogue original de six motifs :** `A A H R`, `A H A R`, `A H R A`, `A R A H`, `R A A H`, `R A H A`. Toute réponse d'invention valide est l'une de ces suites, et non une improvisation à corrigé imprévisible; l'élève choisit librement parmi les possibilités sans voir la liste en épreuve.
- **Pas de piste commerciale ni de captation exigée.** Stimuli constitués de mots, cases et démonstrations musicales originales de l'enseignant. Consentement et protections auditives adaptées à l'environnement.

## Sécurité et accessibilité

Privilégier un volume bas, des pauses auditives et une gestuelle temporelle douce; adapter canaux visuels ou tactiles avant la prestation sans fournir les réponses. Aucun instrument coûteux, son dangereux ni enregistrement obligé. L’équivalence d’accès doit être évaluée humainement.

## Revue humaine nécessaire

La grille `evaluation/GRILLE_MAITRISE.md` exige M1–M5 observés séparément dans **deux contextes**. Les seuils éditoriaux doivent être évalués pour fiabilité intercorrecteurs, inclusivité et juste équilibre entre perception sonore et expression temporelle gestuelle. Les dix items sont à statut `a_revoir`, ni homologués ni certifiés.
