# Plan d'évaluation — qc-pri-st-009

**Format de banque :** `qc.learning-item-bank/1.0`. **Famille immuable :** `qc-pri-st-009-ev-01`. **Cible de chaque item :** `obj-1` (« Relier des phénomènes lumineux ou sonores à leurs sources et propriétés. ») **et** `crit-1` (« Démontrer une variation de lumière ou de son par une manipulation sûre. »). **Mode famille :** `generee_sous_contraintes`, implémenté par items `fixe` ou `scenario_controle` sur corpus fermé.

## Administration et collecte

1. **Avant :** diagnostic D1–D3, non nécessairement noté; enseigner et pratiquer avant de recueillir des preuves. Source d'illustration ou de situation non réutilisée à l'identique entre pratique guidée et maîtrise.
2. **Pendant :** items q-001 à q-008 pour identifier connaissances, explications et qualité de conception. Réponses orales, dessins annotés, tableau A/B ou texte sont équivalents pour les propriétés scientifiques évaluées.
3. **Après :** q-009 et q-010 sont les **deux manifestations requises** de maîtrise, respectivement ombres dans un théâtre de table et vibrations d'un instrument doux. Chaque épreuve exige une modification contrôlée, un avant/après effectivement observé, une inférence et un respect des consignes de sécurité. Pas de réussite inférée d'un total sur q-001 à q-008.
4. **Conserver les traces dans l'environnement d'apprentissage**, avec consentements et minimisation des données; les documents canoniques ne stockent aucune voix, image ou donnée d'élève. Une fiche « état A/état B, faits, interprétation, aide, sécurité » suffit; ne pas demander d'enregistrement audio/vidéo obligatoire.

## Matrice d'items (liens complets)

| Item | Objectif | Critère | Famille | Difficulté | Représentation | Ce qui est observé/justifié |
|---|---|---|---|---|---|---|
| `qc-pri-st-009-q-001` | obj-1 | crit-1 | qc-pri-st-009-ev-01 | initial | vignette écrite A/B | Distinguer fait et inférence de l'ombre. |
| `qc-pri-st-009-q-002` | obj-1 | crit-1 | qc-pri-st-009-ev-01 | initial | scénario lampe/miroir | Identifier source émettrice, réflexion et effet. |
| `qc-pri-st-009-q-003` | obj-1 | crit-1 | qc-pri-st-009-ev-01 | initial | tableau matériaux | Prévoir/interpréter des transmissions sans absolu erroné. |
| `qc-pri-st-009-q-004` | obj-1 | crit-1 | qc-pri-st-009-ev-01 | initial | chaîne à flèches | Identifier source/milieu/récepteur du son. |
| `qc-pri-st-009-q-005` | obj-1 | crit-1 | qc-pri-st-009-ev-01 | intermédiaire | description d'un objet vibrant | Relier vibration et atténuation sonore. |
| `qc-pri-st-009-q-006` | obj-1 | crit-1 | qc-pri-st-009-ev-01 | intermédiaire | plan expérimental A/B | Isoler une seule variable et une observation attendue. |
| `qc-pri-st-009-q-007` | obj-1 | crit-1 | qc-pri-st-009-ev-01 | intermédiaire | scénario lumière corpus S-L | Interpréter le changement d'éclairement, limite ambiante. |
| `qc-pri-st-009-q-008` | obj-1 | crit-1 | qc-pri-st-009-ev-01 | transfert | scénario son corpus S-S | Distinguer mouvement observable et son entendu, conclure prudemment. |
| `qc-pri-st-009-q-009` | obj-1 | crit-1 | qc-pri-st-009-ev-01 | transfert | **manipulation théâtre d'ombre** + fiche A/B | **Preuve de maîtrise 1** : varier lumière, source/obstacle/ombre. |
| `qc-pri-st-009-q-010` | obj-1 | crit-1 | qc-pri-st-009-ev-01 | transfert | **manipulation mini-instrument** + fiche A/B | **Preuve de maîtrise 2** : varier vibration/son, propagation. |

La présence du même critère de famille sur les items de compréhension signifie qu'ils **préparent** l'observation de `crit-1`; seuls q-009/q-010 sont des démonstrations finales complètes.

## Variabilité déterminée, pas génération libre

- `fixe` q-001 à q-006 : énoncés, données et corrigés verrouillés; `seed=null`, `parametres=null`.
- `scenario_controle` q-007 à q-010 : sélectionner **exclusivement** une variante déjà décrite dans `BANQUE_ITEMS.json`. Chaque scénario donne son code, son action, ses constantes, son observation cible, son interprétation; le contenu imprimé de l'item correspond à **A**. Variantes B documentées mais **non actives tant qu'une revue humaine n'a pas approuvé leur usage**. Aucun paramétrage hors corpus, aucune variation de sécurité, de niveau, de nombre de conditions ou d'explication.
- Reproductibilité d'une variante : clé fixe = `seed` de l'item et `variante_id=A` stockées avec le résultat; algorithme : `item_id + variante_id` sélectionne l'entrée du catalogue, sans hasard. Si le moteur ne permet pas ce mappage exact, utiliser l'énoncé fixe A seulement. Aucun contenu inventé par modèle génératif ne peut modifier la tâche ou son corrigé.
- Sécurité : l'enseignant prépare et vérifie chaque matériel, amplitude modérée, surfaces stables, pas de laser, soleil direct, prise secteur, flamme ni son fort. Toujours consigner si la différence A/B n'est pas observée; **ne jamais imposer un faux constat**.

## Grille, décision et accessibilité

- q-001 à q-008 : corriger qualitativement avec les critères, rétroactions et limites de chaque item; ne pas traduire automatiquement en note sommative.
- q-009 et q-010 : cinq axes notés 0 à 3 définis dans `GRILLE_MAITRISE.md` (sécurité, contrôle, observations, explication, autonomie/adaptation). Deux preuves **dans des contextes différents**; chaque axe ≥2 sur chacune, sans incident de sécurité et sans indice de contenu; sinon remédiation et nouveaux essais dans des scénarios sûrs équivalents validés.
- **Accessibilité :** présenter consignes dans la modalité appropriée; fournir contraste et version textuelle/tactile; dispositif visuel de vibration lorsque l'ouïe est limitée; médiateur moteur agissant seulement selon les choix de l'élève; documenter les adaptations sans changer les critères cognitifs. Une description de vidéo seule n'est pas substituée automatiquement à l'exigence de « démontrer par manipulation » sans décision humaine motivée et situation adaptée réelle.
- **Biais et limites :** ne pas mesurer « bonne audition », vitesse de lecture, habileté de préhension, intensité vocale; observer relation causale. Résultats matériels variables selon éclairage et montage — prévoir contrôle de faisabilité et décision « non observable, reprendre », pas « faux ».
- **Statut :** `a_revoir`. Révision scientifique, pédagogique, sécurité locale, accessibilité et essai auprès de participants restent requis. Aucun item certifié.
