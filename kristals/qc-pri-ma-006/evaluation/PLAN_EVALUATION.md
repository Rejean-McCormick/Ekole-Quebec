# Plan d’évaluation — qc-pri-ma-006 / qc-pri-ma-006-ev-01

**Objectif inchangé `obj-1` :** Modéliser l’addition et choisir une stratégie efficace pour calculer.  
**Critère inchangé `crit-1` :** Résoudre deux additions distinctes et expliquer la stratégie adoptée.  
**Gouvernance :** `qc.learning-item-bank/1.0` ; famille unique `qc-pri-ma-006-ev-01` ; mode privilégié **`paramétrique_controle`** (banque mixte avec ancrages fixes et deux générateurs bornés). Tout item reste `a_revoir` et exige une validation humaine avant un examen local.

## Correspondance item → objectif, critère et famille

Tous les items suivants portent explicitement **`obj-1`, `crit-1` et `qc-pri-ma-006-ev-01`** dans le JSON; les indices en pratique guidée ne sont pas des preuves de maîtrise autonome.

| ID (suffixe) | Usage et couverture | Difficulté | Représentation | Correction et variation permise |
|---|---|---|---|---|
| q-001 | Réunion simple, sens de la somme | initial | jetons/textes/égalité | Fixe, `4 + 3 = 7`, aucune variation libre |
| q-002 | Augmentation simple | initial | histoire et schéma | Fixe, `12 + 5 = 17` |
| q-003 | Réunion, décomposition à 10, guidée G1 | initial | matériel → symbole | Fixe, `6 + 5 = 11` |
| q-004 | Augmentation, passage à la dizaine, G2 | intermédiaire | ligne et notation | Fixe, `28 + 7 = 35` |
| q-005 | Deux dizaines et report, G3 | intermédiaire | dizaines/unités | Fixe, `37 + 26 = 63` |
| q-006 | Augmentation, décomposition paramétrée reproductible | intermédiaire | texte / dizaines | `seed=6006`, énumération filtrée, `a+b ≤ 59`, exemple fixé dans la banque |
| q-007 | **Preuve A** : bibliothèque, réunion | transfert | scénario texte; schéma/oral permis | Contrôle de scénario figé, `24 + 18 = 42`; non interchangeable avec B |
| q-008 | **Preuve B** : potager, augmentation | transfert | scénario texte; schéma/oral permis | Contrôle de scénario figé, `37 + 25 = 62`; non interchangeable avec A |
| q-009 | Deux termes à deux chiffres, report paramétré | intermédiaire | valeur de position | `seed=9006`, liste bornée filtrée, exemple fixé dans la banque |
| q-010 | Diagnostic d’erreur « dizaine perdue » | transfert | critique d’égalité | Fixe, correction `48 + 15 = 63` |

## Contrôle de la variation

- **Fixe (`q-001` à `q-005`, `q-010`) :** énoncés et réponses verrouillés, aucun tirage.
- **Paramétrique (`q-006`, `q-009`) :** candidats d'entiers naturels énumérés par ordre lexical croissant `(a,b)`; filtres numériques explicites; `index = seed % N` avec indexation zéro; texte d'instance rempli à partir du couple calculé. La graine entière, la liste des domaines, les contraintes, l'algorithme, les exemples calculés et le calcul indépendant `a + b` figurent dans `BANQUE_ITEMS.json`. **Aucun modèle IA ne tire ni corrige librement.** Les paires sont uniques dans chaque liste; l'administrateur doit éliminer les répétitions entre séances ou contextes.
- **Scénario contrôlé (`q-007`, `q-008`) :** scénario fixé en banque. Toute substitution doit préserver exactement le sens (réunion disjointe versus augmentation), le niveau, l'accès linguistique et l'unicité des contextes et être revue humainement. Pas de génération narrative libre.
- **Cas frontières considérés :** somme jamais supérieure à 100 dans le parcours; q-006 impose franchissement à la dizaine sans somme > 59; q-009 impose report d'unités, deux termes positifs et somme ≤ 99. Les items paramétriques excluent volontairement zéro et les sommes sans report, qui sont abordés ailleurs dans le contenu.

## Rubrique et décision de maîtrise

Pour chaque item recueillir **la valeur de la somme, la représentation/identification du sens, la démarche et son explication, l'aide reçue et la lisibilité de la trace**. Corriger le résultat numériquement et évaluer la validité de la stratégie indépendamment de sa conformité à l'exemple proposé.

La maîtrise nécessite **q-007 et q-008 tous deux autonomes et satisfaisants** ou deux remplacements validés de complexité comparable, sur **deux additions et deux contextes distincts**, non un pourcentage de bonne réponses. Pour chaque preuve : modélisation exacte, somme exacte, stratégie cohérente et explication intelligible. Si une seule preuve manque, remédier puis récolter deux nouvelles preuves. Voir `GRILLE_MAITRISE.md`.

## Accessibilité, sécurité et protection

Lire les scénarios à voix haute ou en texte accessible, autoriser papier, clavier, manipulation de jetons neutres, description de schémas ou explication orale transcrite. Ne pas coder la couleur comme seule information. Ne pas récompenser la vitesse ou la calligraphie; ne pas autoriser une aide indiquant la stratégie dans une preuve dite autonome. Aucun identifiant personnel, donnée sensible ni photographie requis. Les objets concrets doivent être adaptés à l'âge et au risque de mise en bouche. Les histoires de bibliothèque et de potager sont fictives et culturellement non exclusives.

## Pondération et statuts

Pour une éventuelle épreuve interne, couverture visée : sens/réunion, augmentation, passage à la dizaine, regroupement et transfert; ne pas imposer aujourd'hui de coefficient chiffré comme preuve psychométrique. Le correcteur compare chaque item à sa réponse/rubrique verrouillée. **Non validé en situation de classe, non certifié et non publié** ; revue humaine des formulations, biais, niveaux de difficulté et durées nécessaire.
