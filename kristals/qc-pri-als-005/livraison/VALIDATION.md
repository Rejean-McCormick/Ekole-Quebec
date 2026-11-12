# Validation technique et revue nécessaire — `qc-pri-als-005`

**État** : textes et items rédigés; contrôles techniques exécutés et réussis; revue humaine requise. Nul statut homologué, publié, certifié ou PFEQ n'est revendiqué.

## Champ de la livraison

- Un seul Kristal `qc-pri-als-005`, sans modification d'autres Kristals ni des fichiers centraux.
- Remplacements autorisés : `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json` seulement; 12 ajouts dans `contenu/`, `evaluation/`, `sources/` et `livraison/`.
- Objectif `obj-1`, preuve `crit-1`, préalables `qc-pri-als-001` et `qc-pri-als-002`, famille `qc-pri-als-005-ev-01` préservés.

## Contrôles techniques réellement exécutés

- **547 assertions préarchivage réussies** : structure du delta, champs natifs du contrat, frontmatter YAML (mêmes clés et 12 titres), graphes, préalables et famille inchangés, couverture des concepts et scénarios, correction formelle des 10 items fixes, liens, rubriques, sécurité et accès.
- **Test d'identité et de préalables** : comparaison directe avec les fichiers source de l'archive v1.2; deux arêtes sortantes `requires` préservées; aucune dépendance conseillée introduite.
- **10 items** consécutifs `q-001` à `q-010`, uniques, avec réponses attendues, critères et feedback; tous `a_revoir`. Les items 009 et 010 décrivent deux contextes de maîtrise différents, à quatre tours alternés.
- **Contrôle des corrigés** : vérification structurelle des répliques P1/P3, des réponses É2/É4, de l'initiative/question, de la congruence du thème et des cinq dimensions M1–M5. Les variations orales restent à juger humainement; aucune preuve de fiabilité interévaluateurs.
- **Fusion testée** par copie dans un dossier temporaire : les deux seuls originaux remplacés sont `PARCOURS.md` et `CONTRAT_PEDAGOGIQUE.json`; **12 ajouts**; les **34 autres fichiers initiaux protégés** sont identiques après simulation par SHA-256.
- **Provenance** : références internes réellement lues; pages British Council et Cambridge consultées; aucun média tiers intégré; les décisions de seuil sont des créations locales.
- **Intégrité ZIP finale** : 14 entrées directes sous `kristals/qc-pri-als-005/`, sans wrapper, JSON parseables, manifeste concordant, aucune traversée ou entrée vide; contrôle CRC exécuté après création.

## Limites non levées

- Aucun test avec des enfants, aucun jugement de fidélité entre évaluateurs, aucun étalonnage du seuil M1–M5.
- Aucun essai réel de technologies d'amplification ou d'adaptation orale; un professionnel doit déterminer les accommodations ou preuves équivalentes selon le contexte.
- Les exemples et les scripts anglais sont originaux, mais les variations dialectales, la clarté en situation et le risque de biais nécessitent une revue humaine.
- Aucun audit de droit approfondi ni homologation curriculum du Québec; aucune musique, vidéo ou image ajoutée.

## Revue humaine requise

1. **Anglais oral** : naturel des 10 scripts, correspondance question/réponse, intelligibilité évaluée équitablement sans modèle d'accent natif.
2. **Pédagogie** : progression de l'écoute aux quatre tours, distinction entre réponse, question et initiative de l'élève, second contexte réellement transférable.
3. **Évaluation** : stabilité des scripts partenaire et consentement de l'élève, validité M1–M5 et du seuil deux preuves; adaptation avant usage certificatif.
4. **Accessibilité et données** : audition, expression orale, communication assistée, recours à des identités fictives, absence de captation obligatoire.

## Propositions de structure (non appliquées)

- Enrichir éventuellement les schémas communs par `counted_turns`, `partner_script` et `accessibility_decision_ref`, pour rendre auditable la notion de quatre tours et l'équivalence des adaptations.
- Créer un protocole commun d'entraînement du partenaire humain pour éviter les indices involontaires; aucune modification de `governance/`, `registry/`, `canon/` ou autre dossier protégé dans cette livraison.
