# Plan d'évaluation — `qc-pri-ma-033-ev-01`

**Kristal :** `qc-pri-ma-033` · **Objectif unique :** `obj-1` — « Communiquer un raisonnement mathématique vérifiable, au-delà du résultat. »  
**Critère unique du contrat :** `crit-1` — « Présenter une solution cohérente et repérer l’erreur d’un autre raisonnement. »  
**Famille :** `qc-pri-ma-033-ev-01` · **Mode privilégié :** `paramétrique_controle` · **Statut :** items rédigés, contrôle mathématique automatisé; revue humaine exigée.

## Couverture et décision

Dix tâches échantillonnent des regroupements, retraits, partages exacts, parcours de longueurs, montants entiers, et le piège d'une réponse juste obtenue par une méthode invalide. Les huit premiers items servent de **diagnostic et d'entraînement formatif**; les items **009 et 010** sont les **deux preuves indépendantes** dans des contextes distincts, à administrer sans aides ni corrigés visibles. Ne pas remplacer la maîtrise par une moyenne ni une répétition de contexte. Évaluer les cinq axes de `GRILLE_MAITRISE.md` (validité et unités; représentation; justification; contrôle/conclusion; erreur adverse localisée et réparée).

| Item | Liens obligatoires | Difficulté | Situation et représentation requises | Variabilité |
|---|---|---|---|---|
| `qc-pri-ma-033-q-001` | `obj-1` · `crit-1` · `qc-pri-ma-033-ev-01` | initial | Paquets + objets isolés; groupes, addition répétée ou expression | Paramétrique, catalogue de 3 tuples contrôlés |
| `qc-pri-ma-033-q-002` | `obj-1` · `crit-1` · `qc-pri-ma-033-ev-01` | initial | Rangées de chaises, retrait; schéma de rangées | Paramétrique, 3 tuples |
| `qc-pri-ma-033-q-003` | `obj-1` · `crit-1` · `qc-pri-ma-033-ev-01` | intermédiaire | Répartition exacte; colonnes/paquets, opération inverse | Paramétrique, 3 tuples avec division entière |
| `qc-pri-ma-033-q-004` | `obj-1` · `crit-1` · `qc-pri-ma-033-ev-01` | intermédiaire | Rectangle donnant **par hasard** le bon résultat via une règle non généralisable; contre-test | Fixe, données non modifiables |
| `qc-pri-ma-033-q-005` | `obj-1` · `crit-1` · `qc-pri-ma-033-ev-01` | intermédiaire | Périmètre / aire; quatre côtés étiquetés | Paramétrique, 3 rectangles non confondants |
| `qc-pri-ma-033-q-006` | `obj-1` · `crit-1` · `qc-pri-ma-033-ev-01` | intermédiaire | Retrait d'objets et non de paquets; unités | Paramétrique, 3 tuples |
| `qc-pri-ma-033-q-007` | `obj-1` · `crit-1` · `qc-pri-ma-033-ev-01` | intermédiaire | Flux entrée/sortie; tableau avant/reçu/prêté/après | Fixe, données non modifiables |
| `qc-pri-ma-033-q-008` | `obj-1` · `crit-1` · `qc-pri-ma-033-ev-01` | intermédiaire | Billets, coût et monnaie; tableau de coût | Paramétrique, 3 tuples avec monnaie positive |
| `qc-pri-ma-033-q-009` | `obj-1` · `crit-1` · `qc-pri-ma-033-ev-01` | transfert | **Preuve A — bibliothèque** : regroupement, prêt, critique et vérification inverse | Scénario contrôlé fixé, sans indice |
| `qc-pri-ma-033-q-010` | `obj-1` · `crit-1` · `qc-pri-ma-033-ev-01` | transfert | **Preuve B — jardin** : clôture du contour, distinction aire, critique et contrôle | Scénario contrôlé fixé, sans indice |

## Règles de génération vérifiables

- Pour les items 001, 002, 003, 005, 006 et 008, la banque porte **un stimulus instancié** plus un catalogue fermé de **trois variantes**. Choix reproductible : `index = seed % 3` dans l'ordre exact du catalogue; l'index est basé sur zéro. **Il n'y a aucun tirage libre.** La graine est fixée par item et aucune variable ne sort des valeurs listées.
- Les `parametres` JSON donnent domaines exacts, contraintes, opération de résolution, erreur adversaire déterministe et trois exemples testés. La substitution de toutes les valeurs doit mettre à jour stimulus **et** corrigé, pas seulement un nombre isolé. L'algorithme de calcul repose sur les entiers, sans arrondis; la comparaison des deux valeurs est systématique.
- Exemple 001, catalogue `(4,6,3)` : `4 × 6 + 3 = 27` objets; méthode fautive `4 + 6 + 3 = 13` objets; contrôle `6+6+6+6+3=27`. Exemple 005 `(5,4)` : périmètre `2×(5+4)=18 m`, aire `5×4=20 m²`. Exemple 008 `(4,4,25)` : coût `4×4=16 $`, monnaie `25−16=9 $`, fausse démarche `25−4−4=17 $`.
- Pour les items 004, 007, 009 et 010, **aucune variation** de données, de correction ni de contexte n'est autorisée sans nouvelle version et nouveau contrôle. Toute génération automatisée libre de texte et de corrigés reste exclue.

## Barème analytique local (sans total de maîtrise)

Chaque réponse est évaluée sur cinq dimensions, niveau **0** (absent/incorrect), **1** (partiel ou guidé), **2** (correct, autonome et vérifiable), selon `GRILLE_MAITRISE.md`. Pour un item initial, certains axes peuvent être observés sur une trace courte, mais aucun axe non observé ne reçoit automatiquement 2. La preuve finale complète exige les cinq axes. Un résultat exact avec démarche fausse échoue à l'axe de justification; un autre élève critiqué sans identification du passage erroné échoue à l'axe d'analyse.

## Administration, sécurité et accessibilité

- **Format :** copie écrite annotée, schéma tactile/manipulable étiqueté, tableau, ou explication orale enregistrée avec trace des quantités. Les mêmes critères s'appliquent : calcul, justification, contrôle, conclusion et critique doivent être consultables par un évaluateur.
- **Supports :** consigne lue à voix haute, texte grossi ou espacé, notation avec matériel simple, temps adapté; jamais d'indice mathématique ni de contrôle automatique révélant la réponse pendant une preuve.
- **Sécurité, équité :** contextes fictifs non sensibles, pas de données personnelles ni d'objets dangereux à manipuler. Les valeurs monétaires sont des entiers; pas de connaissance externe de prix attendue. Éviter les indices codés seulement par couleur.
- **Droits :** tous les énoncés, personnages et représentations textuelles ont été créés pour cette livraison; pas d'illustration ni d'extrait externe incorporé. Revue humaine nécessaire pour accessibilité réelle, charge cognitive, biais et durée.

## Décision après deux preuves

Administrer 009 et 010 séparément, sans guidage et dans un ordre contrebalancé si utile. Pour chacune, exiger les cinq axes au niveau 2, de manière cohérente; des formulations différentes du corrigé sont recevables si elles sont équivalentes et justifiées. Une dimension déficiente : feedback spécifique, reprise ciblée et **nouvelle** situation non divulguée; ne pas fusionner les deux travaux en une note moyenne. Le contenu n'est pas un examen certifié ou homologué.
