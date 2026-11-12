# VALIDATION — qc-pri-us-001, delta v1.2

**État :** contenu produit; **43 contrôles techniques exécutés et réussis**; banque non certifiée, revue pédagogique/historique humaine requise. Journal des contrôles automatiques du 8 octobre 2026. Ceci n'est pas un audit de conformité au PFEQ.

## Contenu présent et correspondance avec la base v1.2

- **14 fichiers exactement**, tous sous `kristals/qc-pri-us-001/` : 2 remplacements `authoring/` et 12 nouveaux fichiers `contenu/`, `evaluation/`, `sources/`, `livraison/`.
- `PARCOURS.md` : en-tête YAML d’origine analysé et conservé **à l’identique**, 12 sections 1 à 12, sans section supprimée; définitions, exemples, contre-exemples, deux diagnostics, trois guidages dégressifs, quatre pratiques autonomes, deux transferts, feedback/remédiation, accessibilité, critères et rappel différé présents.
- `CONTRAT_PEDAGOGIQUE.json` : identité, objectif, notions, preuve, absence de prérequis et d’ordre, famille native et règles de génération v1.2 préservées; treize champs minimum du contrat générateur renseignés; seul le statut rédactionnel est actualisé pour signaler une revue à faire.
- Registre vérifié : aucune arête **sortante** `requires`, `recommends_before` ou `reinforces` du Kristal. Aucun registre, gouvernance, canon, runtime, docs ni autre Kristal inclus.

## Contrôles effectivement exécutés (script local indépendant)

1. **Identité et structure :** fichiers non vides, manifeste strict, liste et ordre des 14 chemins, aucune entrée hors préfixe, aucun chemin absolu ou traversée `../`, premier chemin au bon emplacement, aucun dossier enveloppe (réussi).
2. **Parsabilité :** YAML de parcours lu sans erreur; les **3 JSON empaquetés** (`CONTRAT_PEDAGOGIQUE.json`, `BANQUE_ITEMS.json`, `MANIFEST.json`) ont été lus à nouveau après compression (réussi).
3. **Références :** `obj-1`, `crit-1`, famille `qc-pri-us-001-ev-01` dans chacun des 12 items et dans le plan; 12 IDs consécutifs sans doublons; domaines de difficulté valides (réussi).
4. **Qualité minimale des items :** chaque item possède consigne, stimulus, réponse attendue, critères détaillés et rétroaction non vides; **8 scénarios contrôlés** avec variantes A/B, **4 items fixes** (réussi).
5. **Variantes / calculs :** pour les **16 variantes** des 8 scénarios, recalcul indépendant par comptage de graduations répété, comparé aux positions de référence figées; bornes, pas positif et divisibilité testés. Les **8 seeds** retrouvent les variantes sélectionnées et les corrigés affichés. Les **4 corrigés fixes** ont été vérifiés contre des attendus prédéfinis (réussi).
6. **Preuves de maîtrise :** deux contextes distincts représentés, `q-007` (jardin scolaire fictif) et `q-008` (Expo 67 historiquement documentée); grille fondée sur quatre dimensions observables et autonomie, sans inférence depuis une note unique (contrôle de structure réussi; efficacité pédagogique non testée).
7. **Provenance/droits/accessibilité :** références aux **3 pages BAnQ consultées**, scénarios fictifs explicitement étiquetés, absence d’images externes embarquées, limites des droits signalées, alternatives de modalités prévues (présence textuelle contrôlée; expérience d'accessibilité non testée).
8. **Intégrité et fusion :** test CRC du ZIP réussi. Dans une copie temporaire de l'archive maître v1.2 entièrement extraite, l'injection de ce delta change **exactement 2 fichiers** et ajoute **exactement 12**, sans suppression et sans changement des **7 320 autres fichiers originaux**. La racine du ZIP reste `kristals/qc-pri-us-001/` sans double dossier parent (réussi).

Le script a exécuté **43 assertions groupées réussies** au total. Les tests mathématiques contrôlent la cohérence des positions; ils ne remplacent pas un essai de compréhension par des élèves, ni la revue humaine des sources.

## Limites non résolues et revue humaine nécessaire

- **Historique :** confirmer la contextualisation des quatre jalons Expo 67 à partir des pages BAnQ avant diffusion; les cartes ne décrivent qu’un sous-ensemble des préparatifs. La pertinence et l’équilibre des perspectives exigent une revue disciplinaire, particulièrement si des activités plus larges touchent les Premiers Peuples.
- **Pédagogie :** essayer les instructions de graduation, les cas « même année » et les rubriques avec différents lecteurs; contrôler durée réelle, charge de lecture et âge de la projection choisie.
- **Accessibilité :** tester réellement lecteurs d’écran, manipulation tactile, bande graduée et réponse orale transcrite. Les vérifications de présence des adaptations ne constituent pas un audit d'accessibilité.
- **Droits :** aucune licence externe n'est revendiquée et aucun visuel documentaire n'est livré. Si de futurs médias sont ajoutés, revue de leurs droits et crédits à faire.
- **Évaluation :** items et rubriques sont au statut `a_revoir`; aucun essai psychométrique ou validation humaine, aucune certification ni publication revendiquée. Les épreuves ne doivent pas être employées telles quelles pour des décisions sommatives à enjeu élevé.

## Propositions de changement structurel (NON appliquées)

1. Ajouter dans le schéma central une propriété de précision documentaire (`annee`, `mois`, `jour`) pour distinguer **année du fait** et **date d'édition** sans ambiguïté.
2. Normaliser le contrôle de variantes `scenario_controle` avec sélection sur seed, inventaire fermé, provenance explicite et couplage variante↔corrigé comme données vérifiables.
3. Définir dans les adaptateurs une preuve équivalente « axe graphique ↔ tableau positions ↔ oral transcrit » sans changer `obj-1`, `crit-1`, le graphe ni les autres Kristals.

**Décision de livraison :** delta techniquement fusionnable, conditionné à une revue humaine avant qualification ou publication.
