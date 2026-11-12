# Journal de livraison et qualification — `qc-pri-ad-005` v1.2

## Portée de l'intervention

Livraison d'un **delta de 14 fichiers** exclusivement sous `kristals/qc-pri-ad-005/`. Deux remplacements complets (`authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`) conservent leurs métadonnées préexistantes; 12 fichiers de contenu, évaluation, sources et livraison sont ajoutés. Aucun fichier canonique, graphe, registre, fichier d'agent, de workspace ni autre Kristal ne doit figurer dans l'archive.

## Contrôles de construction et d'intégrité

- Les tests automatisés sont exécutés après rédaction et paquetage. Le résultat détaillé (PASS/FAIL et compteur) est conservé dans le journal technique d'exécution, non joint au ZIP pour respecter les 14 fichiers. Les vérifications portent sur noms/chemins, nombre de fichiers, tailles non nulles, intégrité ZIP et absence de traversal ou racine supplémentaire; JSON strict; format, ID, frontmatter YAML, 12 sections, champs originaux de la frame, 12 items sans doublon, lien `obj-1`/`crit-1`/famille, variété des contextes `q-011` et `q-012` et `requires qc-pri-ad-004`.
- Vérifications éditoriales manuelles du texte : définition des quatre notions, deux exemples commentés, deux contre-exemples avec réparation, deux diagnostics, trois guidages à indices dégressifs, quatre tâches autonomes, deux contextes de transfert, rétroactions ciblées, rappel différé et adaptation d'accès. Les réponses en art dramatique sont des **productions observables avec rubriques**, et non des corrigés artistiques uniques.
- Les douze tâches sont déterminées et **non paramétriques** : elles ne demandent aucun solveur mathématique. Aucun test de correcteur indépendant ou validation de scène par expérimentation humaine n'est simulé.

## Limites non résolues — revue humaine obligatoire

1. Faire relire l'exactitude didactique, les niveaux de critères, les contextes et l'équité des attentes par un spécialiste de l'art dramatique.
2. Essayer avec un public du primaire : compréhension du langage, faisabilité des durées, espaces et passages libres, adaptations, sécurité des accessoires et de la mobilité.
3. Vérifier en contexte les deux évaluations de maîtrise et la fiabilité entre observateurs (concordance des cotes 0–3). Les items restent `a_revoir` et ne sont ni certifiés, ni publiés, ni homologués.
4. Obtenir la confirmation locale des règles de protection des données et de consentement avant toute captation facultative. Aucune captation n'est requise par le matériel.
5. Contrôler les liens et la fusion dans le workspace destinataire lors de l'intégration; le ZIP n'exécute pas de tests LMS ou framework de production.

## Propositions (aucun changement effectué dans les bases centrales)

- Envisager une convention transversale pour consigner les deux preuves et les adaptations d'accès par dimension dans les traces runtime sans ajouter des données personnelles dans le canon.
- Envisager un champ d'état distinct pour « test technique réussi » vs « revue pédagogique humaine réalisée » afin de ne pas confondre livraison fusionnable et cours publiable.
- Garder le graphe et les IDs inchangés; toute modification future des relations, du canon ou de la gouvernance exige la procédure centralisée versionnée.
