# PLAN D’ÉVALUATION — `qc-pri-us-009`

**Objectif invariant `obj-1` :** Comparer des situations de rencontre et d’échange entre populations.  
**Critère invariant `crit-1` :** Analyser une situation à partir de deux points de vue documentés.  
**Famille invariante :** `qc-pri-us-009-ev-01` ; type du contrat v1.2 : `generee_sous_contraintes`.  
**Mise en œuvre :** banque fermée de 12 tâches d’analyse; aucune improvisation factuelle ni tirage IA. Les deux éventuelles permutations contrôlées conservent les textes intégraux et un seed fixe.

## Couverture item par item

**Tous les items suivants référencent `obj-1`, `crit-1` et `qc-pri-us-009-ev-01`**; les critères textuels et les réponses figurent dans `BANQUE_ITEMS.json`.

| Item | Situation et statut | Difficulté | Représentation | Cible / preuve évaluée |
|---|---|---|---|---|
| `qc-pri-us-009-q-001` | Livres entre deux classes (fiction) | initial | 2 fiches datées + réponse argumentée | proposition/accord conditionnel |
| `qc-pri-us-009-q-002` | Paix de 1701 : le contexte (historique_1701) | initial | 2 fiches datées + réponse argumentée | paix et alliance; contextualiser |
| `qc-pri-us-009-q-003` | Marché en plein air (fiction) | initial | 2 fiches datées + réponse argumentée | échange et équité inconnue |
| `qc-pri-us-009-q-004` | Baie-James : opposition et négociation (historique_1975) | intermediaire | 2 fiches datées + réponse argumentée | conflit → négociation |
| `qc-pri-us-009-q-005` | Salle polyvalente (fiction) | intermediaire | 2 fiches datées + réponse argumentée | conflit d’usage non violent |
| `qc-pri-us-009-q-006` | Paix de 1701 : commerce et diplomatie (historique_1701) | intermediaire | 2 fiches datées + réponse argumentée | échange / alliance sur des temporalités distinctes |
| `qc-pri-us-009-q-007` | Jardins solidaires (fiction) | intermediaire | 2 fiches datées + réponse argumentée | fait accompli / événement conditionnel |
| `qc-pri-us-009-q-008` | Convention 1975 : source et interprétation (historique_1975) | intermediaire | 2 fiches datées + réponse argumentée | loi vs perspective institutionnelle |
| `qc-pri-us-009-q-009` | Accès à la rive (fiction) | intermediaire | 2 fiches datées + réponse argumentée | désaccord et hypothèse de compromis |
| `qc-pri-us-009-q-010` | Foire de voisinage (fiction) | transfert | 2 fiches datées + réponse argumentée | échange / contraintes d’accès |
| `qc-pri-us-009-q-011` | PREUVE A — Grande Paix de Montréal, 1701 (historique_1701) | transfert | 2 fiches datées + réponse argumentée | preuve A : comparaison de deux perspectives sur 1701 |
| `qc-pri-us-009-q-012` | PREUVE B — Convention de la Baie-James, 1975 (historique_1975) | transfert | 2 fiches datées + réponse argumentée | preuve B : comparaison de deux perspectives sur 1975 |

## Rubrique commune et pondération

Échelle 0–2 dans **quatre dimensions** : D1 source/contexte; D2 fidélité des **deux** points de vue, un indice de chacun; D3 comparaison argumentée (une convergence + une divergence reliées au contexte et aux notions); D4 prudence épistémique (fait/interprétation, limite, absence de généralisation). Maximum descriptif 8 par item, **sans déduire la maîtrise d'une moyenne**.

**Preuves finales séparées :** q-011 (Grande Paix de Montréal de 1701) et q-012 (Convention de 1975). Contextes historiques distincts et sources institutionnelles différentes. Dans **chacune** : D2 = 2, D3 = 2, D1 ≥ 1, D4 ≥ 1, sans aide cognitive. Si l’une échoue, remédiation ciblée puis nouvelle preuve historique équivalente **à faire revoir**, pas compensation.

## Nature des sources et validité

- Les tâches simulées A/B sont des sources **internes au scénario fictif**, utiles pour l’argumentation; elles ne sont pas des preuves d'un fait réel ou d'une situation historique. Toutes sont étiquetées et originalement rédigées.
- Les tâches historiques utilisent des résumés pédagogiques contemporains de sources reconnues, pas des transcriptions d’acteurs historiques. Pour 1701 : musée Pointe-à-Callière et Répertoire du patrimoine culturel; pour 1975 : Gouvernement de la Nation crie et Légis Québec. Voir `sources/REFERENCES_CONTENU.md` pour URL, portée et limites.
- La source juridique confirme des parties et une date, sans prouver les motivations subjectives; la perspective crie est explicitement institutionnelle et **ne représente pas chaque membre d’une nation ni les perspectives inuites**.
- La revue humaine doit confirmer les paraphrases, la lisibilité, le degré de complexité, les biais et la suffisance des deux points de vue avant tout usage décisionnel.

## Variabilité et reproductibilité

- q-001–005, q-007, q-009–012 : fixes; aucune substitution de faits, dates, lieux ou acteurs.
- q-006 et q-008 : `scenario_controle` dont l’unique variable est **l’ordre de présentation** des deux fiches sans en modifier le texte, avec seed pair stable. Les exemples livrés montrent l’ordre A→B. Même rubrique factuelle quelle que soit la présentation. Aucune permutation aléatoire au moment du rendu.
- Tout ajout d’un nouveau texte historique **requiert vérification des faits, de la provenance et du corrigé** et nouvelle révision humaine; aucun moteur de génération libre ne peut remplacer ce contrôle.

## Accessibilité, sécurité, équité

Consignes lisibles et numérotées; texte brut compatible avec lecteur d’écran; aucune image indispensable; versions audio lues fidèlement et dictée des réponses possibles; conserver l'identité des sources; ne jamais donner d’indice du fond en évaluation autonome. N'évaluer ni opinion politique, ni origine, ni qualité de l'accent, ni capacité d'écriture non ciblée. Éviter l’incarnation imposée de peuples autochtones. Revue de sensibilité historique et culturelle indispensable.

## Suivi

Les items sont `a_revoir` : outils techniques testés, **non essayés avec des élèves et non certifiés**. Diagnostic, exercices formatifs et deux preuves ne sont pas interchangeables. La grille décisionnelle est `evaluation/GRILLE_MAITRISE.md`.
