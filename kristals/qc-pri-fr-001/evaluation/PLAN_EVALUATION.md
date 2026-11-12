# Plan d'évaluation — qc-pri-fr-001, famille qc-pri-fr-001-ev-01

**Objectif invariant `obj-1` :** Segmenter, fusionner et transformer des syllabes et sons de mots entendus.  
**Critère/preuve invariant `crit-1` :** Segmenter puis recomposer oralement cinq mots nouveaux.  
**Famille :** `qc-pri-fr-001-ev-01` ; type source `réponse_argumentée`, réalisé comme **production orale argumentée/observée** et non questionnaire à choix.  
**État :** banque fixe rédigée, `validation_status: a_revoir` pour chaque item; aucune certification d'examen ni décision automatique. **La totalité des items est liée** aux trois identifiants; les items 001–010 préparent le critère, les 011–012 constituent ses épreuves intégrales.

## Matrice de couverture

| Item (suffixe `q-`) | Fonction | Niveau | Représentation et contexte | Indicateurs / attendu-clé |
|---|---|---|---|---|
| 001 | Diagnostic | initial | oral, entretien neutre | *maman* 2 syllabes, *lac* 1 |
| 002 | Diagnostic | initial | syllabes émises séparément | `/ve/+/lo/` → *vélo* ; `/ka/+/fe/` → *café* |
| 003 | Formatif | initial | mots oraux usuels | *moto*, *papa* segmentés et fusionnés |
| 004 | Formatif | intermédiaire | finale entendue, sans écrit | *tapis*: dernière syllabe `/pi/`, phonème `/i/` |
| 005 | Autonome formatif | intermédiaire | deux mots oraux | *bateau*, *dodo*, découper/recomposer |
| 006 | Formatif | intermédiaire | comparaison de deux mots entendus | *sac/lac*: attaques `/s/`, `/l/`, rime `/ak/` |
| 007 | Formatif | intermédiaire | phonèmes isolés oralement | *chat/chou*: `/ʃ/`, puis `/a/` ou `/u/` |
| 008 | Formatif | intermédiaire | substitution d'une syllabe | *papa* → *papi* |
| 009 | Transfert T1 | transfert | bureau de tri sonore fictif | *boule* → *poule*, rime `/ul/` stable |
| 010 | Transfert T2 | transfert | enregistreur fictif | *chocolat* → `/pa.kɔ.la/` après substitution |
| 011 | **Preuve P1** | transfert | **message à une marionnette** | cinq mots nouveaux, chacun segmenté **puis** recomposé |
| 012 | **Preuve P2** | transfert | **radio des mots mystères** | cinq autres mots nouveaux, mêmes actions sans aide |

**Périmètre :** `q-001` à `q-012`, sans doublons; détails des stimuli, consignes, corrigés, rubriques, rétroactions, variations et statuts dans `evaluation/BANQUE_ITEMS.json`.

## Consignes de passation et sécurité

1. L'adulte ne montre ni graphie, ni syllabes, ni symboles phonétiques à l'élève. Dire le **mot entier** dans une voix québécoise naturelle; donner la consigne exacte puis laisser l'élève agir. Les contenus phonétiques du JSON sont des **notes de correction**.
2. Le critère `crit-1` ne se réduit **jamais** aux seules répétitions : pour chaque mot, noter **(a)** segmentation, **(b)** recomposition, **(c)** aide / répétition / autocorrection. La réponse correcte n'est pas une épellation. Ne pas sanctionner timbre, accent ou rythme personnel si l'unité phonologique est conservée.
3. Pour P1 et P2 : listes verrouillées, aucun exemple tiré de la leçon; espacées par une autre activité ou une séance distincte si possible. Les deux situations doivent être réellement distinctes dans leur cadrage et leur matériel; pas de correction d'une liste avant l'autre. Les aides neutres d'accès auditif sont possibles, **les aides donnant une syllabe sont interdites**.
4. Ne pas demander d'informations privées, de lecture, d'écriture, d'enregistrement sans consentement ou d'usage d'un objet potentiellement dangereux. Les contextes marionnette/radio peuvent être joués **sans équipement**.
5. Si un mot suscite une syllabification incertaine chez un locuteur québécois ou a été enseigné auparavant, **ne pas improviser un corrigé** : marquer la forme « à revoir » et faire examiner une autre liste fixe en revue humaine. Aucune IA libre ni transcripteur vocal ne valide seul la correction.

## Critères / pondération et décision

- Items 001–010 : **formatifs**, pas de somme pondérée substituée à la preuve finale. Cibles : frontières syllabiques, fusion, attaque/rime, son final, substitution d'un phonème ou d'une syllabe; rétroaction descriptive et remédiation ciblée.
- Chaque preuve 011–012 : **5 mots** et **2 actions obligatoires par mot**; valider un mot uniquement si **les deux actions sont exactes** dans le bon ordre, sans indice de contenu. **Seuil de design local : 5/5** dans P1 **et** **5/5** dans P2, plus transfert/manipulation observé sur q-009 ou q-010 (ou vérification formative équivalente revue), pour conclure à la maîtrise de `obj-1` selon `evaluation/GRILLE_MAITRISE.md`.
- Pas de moyenne P1/P2, de note d'âge, d'orthographe ou de vitesse, et aucune maîtrise proclamée à partir de P1 seul. Toute aide de contenu = performance accompagnée, **non preuve autonome**. Si une preuve échoue ou si l'oral n'est pas observé adéquatement : « en consolidation » / « observation insuffisante » et nouvel essai **sur une forme inédite validée**.

## Variabilité admise et verrouillage

`mode: fixe` pour tous les 12 items; `seed: null`, `parametres: null`. Le contexte peut être joué par une personne, sans équipement, **mais les mots et les opérations demeurent fixés**. Ne pas ouvrir de famille « paramétrique » sans algorithme, domaines, contraintes et revue des solutions. Les seules variations de passation admissibles ici : timbre/élocution québécois naturel, répétition neutre du mot entier et accès sensoriel adapté. Les règles de saisie de chaque item et ses limites particulières figurent dans la banque.

## Vérifications et limites de qualification

Les productions écrites et les réponses adultes ont été vérifiées par cohérence interne; l'examen de leur naturalité orale en français québécois auprès de personnes compétentes et les essais d'accessibilité **restent à conduire**. Références : `sources/REFERENCES_CONTENU.md`. Éviter tout statut « publié », « homologué » ou « certifié ». La banque est un **corpus fixe contrôlé éditorialement**, pas une génération IA « fiable » attestée.
