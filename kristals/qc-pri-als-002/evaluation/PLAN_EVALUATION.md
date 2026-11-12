# Plan d'évaluation local — `qc-pri-als-002`

**Famille inchangée :** `qc-pri-als-002-ev-01` · **objectif unique :** `obj-1` — Employer un lexique anglais ciblé dans des échanges authentiques. · **critère immuable :** `crit-1` — Nommer et utiliser correctement des mots nouveaux dans un mini-dialogue. · **Mode privilégié :** `observation_ou_production`. Toutes les tâches correspondent au même objectif et au même critère, y compris lorsque seule une composante de cet objectif est entraînée. Ces items sont **`a_revoir`**; ne pas les annoncer comme validés ou certifiés.

## Plan de couverture et administration

| ID complet (suffixe) | Usage | Difficulté | Représentation / tâche fixée | Évidence observée | Variation permise |
|---|---|---|---|---|---|
| `q-001` | diagnostic/formatif | initial | table d'objets, demander *pencil* | mot + demande intelligible | aucune |
| `q-002` | formatif | initial | contraste règle/gomme, demander *eraser* | référent + mot + tour | aucune |
| `q-003` | formatif | initial | collation, demander *apple* et *water* | catégorie et mini-demande | aucune |
| `q-004` | formatif | initial | plan fictif, proposer *park* | lieu + proposition | aucune |
| `q-005` | formatif | intermédiaire | réparation d'une demande incohérente au kiosque | corriger *ruler* → *sandwich* | aucune |
| `q-006` | formatif | intermédiaire | donner du matériel, nommer *notebook* et *eraser* | fonction de réponse + noms | aucune |
| `q-007` | formatif | intermédiaire | boîte de classe, dialogue à deux tours | deux référents appropriés | aucune |
| `q-008` | formatif | intermédiaire | choix de lieu, réponse à relance | *store* puis *library* | aucune |
| **`q-009`** | **preuve A** | **transfert** | **bureau de prêt pour une affiche fictive**; mots *pencil, notebook, ruler* | **3 noms distincts en 2 tours, cohérence, autonomie, intelligibilité** | **une seule variante A préapprouvée décrite dans l'item, à revue humaine** |
| **`q-010`** | **preuve B** | **transfert** | **kiosque fictif d'une rencontre**; mots *apple, water, banana* | **mêmes 4 critères dans un autre contexte et à autre occasion** | **une seule variante B préapprouvée décrite dans l'item, à revue humaine** |
| `q-011` | transfert formatif | transfert | club fictif, fournir *pencil, notebook, eraser* | changer de partenaire et de rôle | aucune |
| `q-012` | rappel différé | intermédiaire | nouvelle carte de quartier, *school*, *park* | récupération lexicale et relance | aucune |

Tous les items JSON portent explicitement `objectif_id: obj-1`, `critere_id: crit-1` et `family_id: qc-pri-als-002-ev-01`. Leur difficulté et représentation servent la couverture et ne constituent pas une note unique. q-001 à q-008, q-011 et q-012 **préparent ou consolident** les microcomposantes sans remplacer les deux preuves. **Poids décisionnel de maîtrise :** q-009 et q-010 sont **tous deux obligatoires**; aucun total sur 12 ou pourcentage ne se substitue à cette conjonction.

## Protocole spécifique des preuves

1. **Avant la preuve :** les 12 mots du corpus ont été enseignés; laisser un intervalle de pratique entre le modelage et la collecte; utiliser des scènes **non étiquetées en anglais** et des accessoires factices. Les scripts/corrigés de la banque sont réservés à l'évaluateur. Ne pas afficher la cible avant réponse.
2. **Preuve A, q-009 :** l'élève joue la personne qui prépare une affiche. Scène fictive d'un bureau de prêt : trois objets marqués comme nécessaires (crayon, cahier, règle); un quatrième (gomme) n'est pas marqué. Le partenaire ouvre « Hi! What do you need for your poster? », puis pose seulement « Anything else? ». Deux interventions de l'élève sont exigées; l'élève nomme *pencil*, *notebook*, *ruler* en anglais en demandant. L'interlocuteur réagit naturellement.
3. **Preuve B, q-010 :** sur **une autre occasion**, l'élève joue une commande au kiosque d'une rencontre fictive. Les trois produits sélectionnés par des marques graphiques sont pomme, eau, banane; un sandwich est non sélectionné. « Hello! What would you like? » puis « Anything else? ». Deux interventions de l'élève contiennent *apple*, *water*, *banana* convenablement intégrés. Il n'y a ni nourriture ingérée, ni vraie commande.
4. **Deux manifestations indépendantes :** A et B ne doivent pas être enregistrées comme un seul essai recyclé; date/occasion, contexte, aide et réalisation sont notés séparément. Deux fois la même tâche, une réussite avec aide lexicale ou la répétition immédiate du modèle ne suffisent pas.
5. **Décision :** par preuve, trois mots **différents** du corpus exigé, correctement reliés aux référents + expressions de demande + une relance pertinente + intelligibilité, **sans aide sémantique ou mot soufflé**. Voir les niveaux précis dans `GRILLE_MAITRISE.md`. Deux preuves satisfaisantes = maîtrise pédagogique **locale**; items demeurent « à revoir » tant qu'ils ne sont pas évalués par des spécialistes.

## Réponses et variabilité bornée

- **Mode `fixe`** q-001–008, q-011 et q-012 : rôles, stimuli, mots attendus et rubrique figés; variantes libres **interdites** pour une comparaison d'items. Les reformulations anglaises équivalentes sont recevables selon la rubrique : elles ne changent pas le stimulus.
- **Mode `scenario_controle`** q-009/q-010 : jeu de rôle fixe par défaut; **seule** variante de reprise à soumettre à revue humaine : A remplacer crayon par gomme tout en conservant cahier + règle, scène bureau de prêt différente; B remplacer banane par sandwich tout en conservant eau + pomme, scène comptoir d'une exposition imaginaire. Valeurs possibles, contraintes et corrigés des quatre scénarios sont explicités dans `BANQUE_ITEMS.json` et dans le contrat v1.2. Aucune substitution libre, aucun tirage aléatoire, aucune génération IA de corrigés, `seed: null`.
- Variabilité **de la réponse** : ordre des noms, « I'd like » / « Can I have » / « I need » et politesse peuvent différer; *some water* / *water, please* recevables. La reconnaissance du référent et la pertinence de l'acte de parole priment sur l'accent et les articles non essentiels. Un mot anglais hors corpus peut être compris, mais **ne compte pas** dans les trois noms ciblés. Une traduction française seule ou un geste seul (sans choix d'un nom anglais par l'élève) ne fournit pas la preuve demandée.

## Cotation, rétroaction, revue et droits

La grille commune cote séparément : **L** trois noms cibles distincts et exacts, **C** adaptation au contexte, **T** interaction à deux tours, **I** intelligibilité/autonomie du message. Les quatre dimensions doivent atteindre le niveau 2 dans chaque contexte; ne pas convertir une somme en note de maîtrise. Si échec, la rétroaction localise la dimension et prescrit une tâche différente, puis deux nouvelles situations évaluées à nouveau.

**Accessibilité et sécurité :** lecteur humain ou présentation écrite, description alternative des cartes, objets fictifs sûrs, temps de traitement, clavier/CAA avec sélection lexicale contrôlée par l'élève. Documenter tout support et sa neutralité; pas de mesure d'accent natif, de débit, de handicap moteur ou de goûts alimentaires. Aucune localisation ou identité réelle. Sans essais réels, ne pas prétendre que l'accessibilité ou la fidélité intercorrecteurs est démontrée.

**Contrôle du contenu :** expressions et dessins décrits sont originaux, sans texte tiers ni images sous droits reproduits; droits d'utilisation pour des illustrations créées ultérieurement à vérifier. L'évaluateur doit examiner la clarté des scènes, la langue pragmatique, le niveau adapté, la naturalité des reformulations, l'équité, les cartes accessibles et les risques de divulgation avant une administration certificative.
