# Validation de livraison — `qc-pri-ma-013`

**Statut :** livrable pédagogique rédigé; revue humaine encore requise. Rapport établi le 8 octobre 2026 après les assertions et calculs ci-dessous; revue humaine toujours requise.

## Périmètre

- 2 fichiers existants `authoring/` complètement remplacés et 12 nouveaux fichiers, tous sous la racine `kristals/qc-pri-ma-013/`.
- Aucune inclusion ni modification de la gouvernance, du registre, de la documentation canonique, des autres Kristals ni des fichiers protégés `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, `kristal.workspace.json` et `AGENTS.md`.
- Pas de prétention de conformité PFEQ, de validation expérimentale ou de certification.

## Contrôles exécutés

- **627 assertions préarchivage exécutées et réussies** : fichier et chemins, 12 sections et YAML frontmatter identique, préalables, objectifs, famille v1.2 conservée, 10 items complets, liens, droits/documentation, accessibilité et deux contextes de maîtrise.
- **16 cas paramétriques testés exhaustivement**, dont égalités, comparaison et ordre. Recalculs entiers + vérification indépendante avec `fractions.Fraction` et `math.lcm`. Valeurs de tous les cas et seed stable vérifiées.
- **22 identités et comparaisons numériques fixes** recalculées exactement dans les leçons et preuves; aucune approximation décimale utilisée comme contrôleur.
- **Fusion simulée avec la source maître :** seulement deux remplacements `authoring/`, 12 ajouts, autres fichiers de la source locale inchangés octet par octet. Aucun fichier de gouvernance ou registre global inclus.
- **Après archivage :** 14 entrées sans chemin absolu ni parent, manifestes exacts, parse JSON et CRC ZIP contrôlés lors de la génération, sans défaillance.
- **Limite explicite :** ce contrôle automatique établit la cohérence numérique et le format mais n'a pas validé pédagogiquement les libellés des items ni testé leur usage avec des élèves.

## Limites, revue humaine et propositions non appliquées

1. **Revue pédagogique mathématique :** vérifier difficulté, sens des termes, lisibilité des représentations, cohérence des remédiations, clarté des tâches et du critère de classement.
2. **Revue technique et d'accessibilité :** vérifier les bandelettes tactiles, braille mathématique, supports visuels et compatibilité des traces d'observation; l'exactitude du code ne démontre pas l'équité d'usage.
3. **Revue d'évaluation :** évaluer l'authenticité des deux contextes, la fidélité de cotation par plusieurs adultes et le calibrage du seuil pour une utilisation réelle.
4. **Proposition à discuter sans modifier les fichiers communs :** versionner un schéma commun `parametres.cas` avec contrôleur et hash de variantes, et un champ de statut pour les deux preuves autonomes de maîtrise.
5. **Non effectué :** aucun élève évalué, aucun test biomécanique, aucune revue juridique exhaustive, aucune validation par l'autorité scolaire, aucune publication du canon.
