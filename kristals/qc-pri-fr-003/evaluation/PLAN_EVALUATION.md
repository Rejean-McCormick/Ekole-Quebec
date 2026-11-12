# Plan d'évaluation — `qc-pri-fr-003-ev-01`

**Objet `obj-1`** : Décoder des mots inconnus en mobilisant les correspondances apprises.  
**Critère `crit-1`** : Lire à voix haute une série de mots nouveaux et expliquer la stratégie employée.  
**Type native v1.2** : `réponse_argumentée` ; **modes opératoires** `fixe` ou `scenario_controle` à corpus fixé. L'objet évalué est **la lecture orale**, non un QCM, une orthographe produite ou l'explication d'une image.

## Blueprint de couverture

| Item | Usage | Difficulté | Représentation / contexte | Liens invariants | Contrôle |
|---|---|---|---|---|---|
| `q-001` | Diagnostic oral | initial | mots imprimés `lame`, `chou` | obj-1, crit-1, qc-pri-fr-003-ev-01 | `ch`, `ou`, fusion |
| `q-002` | Diagnostic oral | initial | mots imprimés `tapis`, `roue` | obj-1, crit-1, qc-pri-fr-003-ev-01 | consonne finale muette, `ou` |
| `q-003` | Enseignement accompagné G-1 | initial | cartes `rame`, `poche` | obj-1, crit-1, qc-pri-fr-003-ev-01 | indices forts tracés |
| `q-004` | Enseignement accompagné G-2 | intermédiaire | cartes `bouche`, `chute` | obj-1, crit-1, qc-pri-fr-003-ev-01 | indices dégressifs |
| `q-005` | Enseignement accompagné G-3 | intermédiaire | cartes `coude`, `savon` | obj-1, crit-1, qc-pri-fr-003-ev-01 | premier essai sans indice |
| `q-006` | Autonomie A-1 | intermédiaire | mots `cabane`, `salade`, `navire` | obj-1, crit-1, qc-pri-fr-003-ev-01 | finales en e, segmentation |
| `q-007` | Autonomie A-2 | intermédiaire | mots `loupe`, `vache`, `touche` | obj-1, crit-1, qc-pri-fr-003-ev-01 | `ch`/`ou` |
| `q-008` | Autonomie A-3 | intermédiaire | mots `tente`, `ronde`, `pont` | obj-1, crit-1, qc-pri-fr-003-ev-01 | `en`/`on`, finales |
| `q-009` | **Maîtrise M-A, preuve 1** | transfert | cartes de récit, 4 mots nouveaux | obj-1, crit-1, qc-pri-fr-003-ev-01 | oral + stratégie + autonomie |
| `q-010` | **Maîtrise M-B, preuve 2** | transfert | étiquettes d'exposition, 4 autres mots nouveaux | obj-1, crit-1, qc-pri-fr-003-ev-01 | contexte et corpus distincts |
| `q-011` | Transfert T-1 | transfert | inventaire de sciences, 4 étiquettes | obj-1, crit-1, qc-pri-fr-003-ev-01 | application fonctionnelle |
| `q-012` | Transfert T-2 | transfert | liste de bricolage, 4 fournitures | obj-1, crit-1, qc-pri-fr-003-ev-01 | application fonctionnelle distincte |
| `q-013` | Autonomie A-4 | intermédiaire | mots `minute`, `rapide`, `parade` | obj-1, crit-1, qc-pri-fr-003-ev-01 | sans indice |

Chaque item du fichier JSON répète **individuellement** `family_id`, `objectif_id`, `critere_id`. Les items ne sont pas tous des épreuves finales : `q-003` à `q-005` restent formatifs en présence d'indices, sans pouvoir compter comme preuves d'autonomie.

## Conditions d'administration et de correction

1. Avant présentation, l'adulte vérifie que les **correspondances en jeu** ont été enseignées ou diagnostiquées. Un graphème non enseigné n'est pas une preuve d'échec de la compétence enseignée.
2. Mot imprimé isolé, en caractères lisibles, sans image contextuelle au moment de décoder; l'adulte peut lire la **consigne uniquement**. Pour la tâche de transfert, le cadre (récit, exposition, sciences, bricolage) est expliqué avant l'affichage mais ne révèle pas les réponses.
3. L’élève lit **chaque mot à voix haute**, puis explique sa stratégie sur au moins un mot. L’adulte conserve une trace de la forme orale observée, de l’explication et des autocorrections **avant** rétroaction.
4. La réponse attendue contient des indications phonologiques pour **le correcteur**; la transcription API n'est pas demandée à l'élève. Les écarts d'accent du français québécois sans confusion entre les graphèmes pertinents sont examinés favorablement par un humain compétent.
5. Chaque série notée comme autonome exige **aucun indice sur les sons, aucune amorce du mot, aucune réponse montrée**; un rappel de consigne non phonémique est permis. Les items guidés sont évalués sur le progrès et non confondus avec une mesure indépendante.
6. Une autocorrection spontanée avant intervention peut compter. Si l'adulte a donné le son, les mots concernés ne prouvent plus l'autonomie; prévoir une autre liste **humainement revue** plutôt qu'une simple répétition.

## Rubrique, niveaux et décision

Pour chaque mot : `correct`, `incorrect`, `variante_à_qualifier`; la réussite d'une série de quatre mots exige au moins **3/4** formes valides. Pour la stratégie : **justification recevable** si l'élève désigne au moins un graphème réel, en précise la valeur phonique appropriée et explique l'assemblage; « j'ai deviné / j'ai regardé le dessin » n'est pas une justification de décodage. Pour l'autonomie : **aucun indice** pendant l'essai. Les détails et niveaux 0/1/2 figurent dans `evaluation/GRILLE_MAITRISE.md`.

**La maîtrise ne dépend ni du total d'items passés ni d'une note unique** : preuves M-A **et** M-B sur contextes et mots différents, chacune avec ≥ 3/4 mots justes, une justification pertinente, aucune aide, et pas d'erreur graphémique systématique non corrigée. Après une remédiation, administrer une **autre** série approuvée; les mêmes cartes déjà apprises ne comptent plus comme « nouveaux mots ».

## Variation autorisée et contrôle qualité

- **`fixe`** : écriture du mot, ordre des mots et réponse phonologique verrouillés. Changement de présentation (taille, contraste, affichage ligne par ligne) permis sans changer le mot.
- **`scenario_controle`** : possibilité de modifier uniquement un **habillage non révélateur** du contexte (papier vs écran, sans images de réponse), tout en conservant la **même liste** et la même évaluation. Si la liste change, il faut construire et faire vérifier un *nouvel item* (lexique, graphèmes, sonorité, biais, difficulté et réponse), puis l'enregistrer dans une version révisée; aucune substitution IA libre.
- **`parametrique`** : non employé ici; ni seed, ni plage numérique, ni calcul déterministe n'ont de raison d'être. `seed: null`, `parametres: null`. La génération libre ne contrôle pas la validité d'un mot ni d'une variante phonétique.
- **Couverture** : graphèmes simples, `ch`, `ou`, `on`, `an`/`en`, finales écrites non prononcées dans certains mots, fusion et vérification sans devinette. L'épreuve mesure décodage, **pas** connaissance du sens, vitesse, capacité de dessin, traits personnels ou maîtrise du PFEQ.

## Sécurité, droits, accessibilité et statut

Mots ordinaires sans noms propres sensibles, aucun contenu traumatisant, aucune enquête privée. Consentement et stockage local sécurisé si la voix est enregistrée; l’enregistrement **n'est pas exigé** et des notes d'observation peuvent suffire. Grande police, bon contraste, temps flexible, pointage possible; consigne audible permise, mais pas lecture des cibles pendant la preuve. Une impossibilité de lecture vocale déclenche une revue d'adaptation distincte, **sans prétendre atteindre silencieusement** le critère oral. Pas de discrimination fondée sur l'accent du français québécois.

**Statut des 13 items :** `a_revoir`. Les correspondances graphémiques et les réponses ont fait l'objet d'un contrôle rédactionnel explicite; l'administration réelle, la revue linguistique québécoise et la qualification institutionnelle ne sont **pas réalisées**.
