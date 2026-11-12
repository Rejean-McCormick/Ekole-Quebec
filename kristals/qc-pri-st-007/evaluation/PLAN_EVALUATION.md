# Plan d'évaluation — Forces et mouvement

**Kristal unique :** `qc-pri-st-007` · **Famille immuable :** `qc-pri-st-007-ev-01` · **Objectif :** `obj-1` — « Décrire l’effet d’une force sur le mouvement ou la forme d’un objet. » · **Critère :** `crit-1` — « Prédire puis observer les effets de forces différentes sur un objet. »

## Nature de l'évaluation

**Privilège de conception :** `generee_sous_contraintes` dans le contrat v1.2. La banque de ce delta comprend **8 `scenario_controle`** (choix déterministe dans un corpus fini de deux traces fictives et deux corrigés indissociables, par item) et **4 `fixe`**. Les items de lecture à traces fixes exercent le jugement; les **deux preuves de maîtrise** (`q-011`, `q-012`) reposent sur de vraies observations non prédéfinies. Le choix d'une trace de scénario n'est pas une simulation de laboratoire et ne vaut pas validation d'un comportement physique réel.

## Correspondance exhaustive des items (tous = `obj-1` + `crit-1` + `qc-pri-st-007-ev-01`)

| Item | Difficulté | Mode | Représentation | Cible évaluée | Preuve autonome sommative? |
|---|---|---|---|---|---|
| `qc-pri-st-007-q-001` | initial | scénario contrôlé | récit + repère | poussée, prédiction vs constat | non |
| `qc-pri-st-007-q-002` | initial | scénario contrôlé | récit + direction | traction et position | non |
| `qc-pri-st-007-q-003` | initial | scénario contrôlé | contours avant/pendant/après | forme sans translation | non |
| `qc-pri-st-007-q-004` | intermédiaire | scénario contrôlé | flèches gauche/droite | friction du contact opposée au glissement | non |
| `qc-pri-st-007-q-005` | intermédiaire | scénario contrôlé | trace d'immobilité | action ≠ déplacement assuré | non |
| `qc-pri-st-007-q-006` | intermédiaire | scénario contrôlé | positions finales comparées | friction comme hypothèse, contrôle des variables | non |
| `qc-pri-st-007-q-007` | intermédiaire | scénario contrôlé | deux photos temporelles textuelles | repère, mouvement et limite sur vitesse | non |
| `qc-pri-st-007-q-008` | transfert | scénario contrôlé | deux gestes sur un objet | forme vs position | non |
| `qc-pri-st-007-q-009` | intermédiaire | fixe | argument à examiner | corriger « pas de déplacement = pas de force » | non |
| `qc-pri-st-007-q-010` | transfert | fixe | deux scènes fictives | poussée sur position vs déformation | non |
| `qc-pri-st-007-q-011` | transfert | fixe | **boîte légère réelle + repères** | **preuve A : prévoir, pousser/tirer, observer** | **oui** |
| `qc-pri-st-007-q-012` | transfert | fixe | **balle en mousse réelle + contours/repères** | **preuve B : prévoir, presser/pousser, observer** | **oui** |

Les 12 objets JSON possèdent explicitement `objectif_id`, `critere_id`, `family_id` et une `reponse_attendue` incluant un corrigé déterminé **ou** une grille de preuve observée. Une explication fiable d'une trace fixe ne saurait remplacer l'observation expérimentale requise par la preuve de maîtrise.

## Critères et pondération descriptive

- **Avant (prédiction)** : l'élève écrit, dicte ou enregistre son hypothèse avant l'essai; l'ordre temporel est authentique.
- **Après (constat)** : il décrit fidèlement un changement ou une stabilité de position et/ou de forme avec repères; une prédiction infirmée n'est pas pénalisée en tant que telle.
- **Notion physique** : il distingue poussée, traction et friction dans les cas observables; sait qu'une force ne garantit ni translation ni déformation visible.
- **Inférence** : il relie le geste à un effet possible sans inventer une intensité, une mesure ou une cause exclusive; signale une limite pertinente.
- **Sécurité et autonomie** : gestes doux, matériel approprié, pas d'aide conceptuelle, modalités accessibles équivalentes documentées.

**Barème d'une preuve pratique :** chaque dimension est appréciée sur quatre niveaux qualitatifs (non démontré, en développement, satisfaisant, solide). **Les critères essentiels sont les cinq dimensions ci-dessus.** La maîtrise demande deux preuves satisfaisantes ou solides dans les deux contextes, sans indice conceptuel, et une sécurité respectée; elle n'est jamais déduite d'un pourcentage d'items.

## Variations autorisées et interdites

- **Items 1–8 :** seuls deux stimuli pré-rédigés par item sont autorisés. Algorithme : `indice = seed % 2` en numérotation `0, 1` ; le corrigé correspondant est sélectionné par le même indice. L'exemple déjà inséré dans le champ `stimulus` est la variante de la `seed` indiquée. Réponse ouverte notée à l'aide des critères; aucun texte généré librement ne modifie les faits.
- **Items 9–12 :** aucun changement par générateur. Sur les items pratiques, la **réponse observée de l'élève** varie naturellement; on n'impose ni forme ni distance prédéfinie. Remplacer un objet ou une manipulation nécessite une équivalence pédagogique justifiée, un repère vérifiable et un protocole sûr validé avant administration.
- **Interdit :** générer un résultat physique aléatoire, un chiffre non mesuré, une intensité non observée, un corrigé prétendant prédire exactement une distance ou un temps, ou inférer la maîtrise d'une réponse QCM isolée.

## Modalités, sécurité et accessibilité

Les scénarios textuels peuvent être lus, audio-décrits ou disposés en tableau contraste fort; une réponse orale avec transcription est recevable. La manipulation peut être exécutée par un partenaire adulte **sur les instructions de l'élève**, sans lui suggérer quoi prévoir ni quoi conclure; consigner ce soutien. Pas de lancers, d'objets lourds, de ressorts, de ficelles enroulées, de poussées vers personnes ou bords; arrêt si le matériel est instable. Ne pas confondre la motricité fine avec la compétence visée. Conserver les traces d'élève hors du workspace canonique.

## Conditions de décision et contrôle qualité

1. Administrer quelques items d'entraînement et corriger les erreurs avant les preuves. 2. Administrer `q-011` (transport d'une boîte légère) et `q-012` (balle en mousse : forme et position) **en contextes distincts et sans indices de contenu**. 3. Appliquer `GRILLE_MAITRISE.md` à chacun, et noter les accommodations. 4. Si un critère échoue, remédier seulement au maillon concerné et utiliser une situation neuve. 5. Prévoir un rappel différé à 2–7 jours. **Tout item reste `a_revoir` tant que les critères, le corpus, le langage et la faisabilité n'ont pas été évalués humainement.**
