# Validation et limites — delta `qc-pri-ma-033` v1.2

## Provenance et périmètre

Archive maîtresse consultée : `initbundle(1).zip`, racine `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Les fichiers de gouvernance v1.2, le graphe et les quatre documents `authoring/` demandés ont été lus **avant rédaction**. Cette livraison ne modifie que les deux fichiers `authoring/` autorisés et crée douze fichiers sous le même Kristal. Aucun artefact v9, registre, gouvernance, alignement, agent ou autre Kristal ne doit être écrasé.

## Contrôles techniques et mathématiques exécutés

Les résultats constatés lors de la production sont inscrits ci-dessous **après exécution** (les nombres et preuves détaillés figurent dans les journaux du script local, sans ajout de fichier au ZIP). La formule du manifeste donne les quatorze chemins exigés. Les champs du contrat préexistant restent présents et tous les identifiants canoniques sont inchangés.

### Résultats techniques locaux (contrôles exécutés sur les fichiers livrés)

- **37 contrôles ciblés réussis sur 37** : 33 vérifications du dossier de delta (champs, identité, YAML, 12 sections, liens, références, manifeste, conditions d’évaluation, accessibilité documentée), puis 4 tests sur le ZIP final (nombre de fichiers et ordre, chemins, égalité des octets, CRC et lecture JSON).
- **14 fichiers exactement**, tous non vides, répartis sous `kristals/qc-pri-ma-033/` et tous nommés dans le manifeste; aucune autre entrée, aucun préfixe enveloppant et aucune traversée `../`.
- **3 documents JSON parsables** (`authoring/CONTRAT_PEDAGOGIQUE.json`, `evaluation/BANQUE_ITEMS.json`, `livraison/MANIFEST.json`). YAML initial comparé octet par octet au frontmatter source et parsé séparément; douze sections numérotées de 1 à 12.
- **10 items distincts** de `q-001` à `q-010` sans doublon et avec `obj-1`, `crit-1` et `qc-pri-ma-033-ev-01`. Six items paramétriques × trois tuples autorisés = **18 variantes** recalculées par un oracle arithmétique indépendant du texte des corrigés; aucune divergence, division avec reste ni coïncidence incorrecte pour les distracteurs paramétriques.
- **Deux preuves autonomes distinctes** : `q-009`, bibliothèque (34 livres), et `q-010`, clôture de jardin (22 m). Contrôle arithmétique indépendant également effectué sur les quatre items non paramétriques; échelle de maîtrise et absence de compensation vérifiées au niveau documentaire.
- **Droits et accessibilité** : audit documentaire limité aux mentions de provenance, d’accès et aux créations originales; **pas** d’audit juridique, de test lecteur d’écran, ni d’observation d’élèves. La conformité des chemins de liens internes cités a été contrôlée sur des fichiers existants.

**Statut de conclusion :** contrôle technique local réussi, **à revoir humainement** avant qualification. Aucune garantie d’efficacité pédagogique, aucun examen certifié, aucun déploiement, aucune validation canonique/publication.


## Points qui demandent une revue humaine

1. **Pertinence didactique et charge cognitive :** s'assurer que le passage d'objets regroupés au périmètre ne crée pas d'obstacle disproportionné au regard de l'objectif de communication de démarche.
2. **Essai d'évaluation :** tester les dix items auprès d'élèves, vérifier temps, compréhension linguistique, variantes, biais et fidélité de la cotation sur des réponses originales.
3. **Accessibilité pratique :** essayer descriptions des schémas, matériel et réponse orale, puis vérifier que les cinq traces restent observables sans aide mathématique.
4. **Corrigés argumentatifs :** reconnaître les stratégies équivalentes non anticipées et les formulations valides; la vérification automatisée ne prouve pas que toute réponse humaine sera jugée correctement.
5. **Validation institutionnelle et publication :** aucune conformité PFEQ, certification d'examen, qualification canonique, déploiement LMS ou publication n'a été accomplie.

## Limites techniques connues

Les calculs des variantes sont déterministes et vérifiés sur leurs catalogues finis, mais il n'existe ici **aucun générateur/exécuteur intégré** à un LMS ni de correcteur sémantique fiable des réponses libres. La cotation doit rester conduite selon la grille par un évaluateur responsable. Les fichiers de gouvernance sont *consultés mais exclus* du ZIP et ne doivent pas être changés dans le cadre de cette mission.

## Propositions de modification de structure (non appliquées)

- Centraliser ultérieurement un schéma JSON de variantes paramétriques avec types et contraintes validables automatiquement dans la gouvernance versionnée.
- Introduire un journal versionné d'essais terrain, d'accessibilité et de décisions de revue, distinct du canon mathématique.
- Définir un champ normatif permettant d'exprimer les cinq sous-critères analytiques attachés à `crit-1`, sans changer le critère canonique lui-même.

Ces propositions sont consignées pour une décision centrale éventuelle; **aucun changement aux bases communes n'est effectué dans ce delta.**
