# Validation de livraison — `qc-pri-ma-012` / version 1.2

**Statut** : `controle_technique_effectue_revue_pedagogique_humaine_requise`. Ce document rapporte exclusivement des vérifications réellement exécutées sur le delta rédigé; **il ne qualifie pas** le Kristal comme cours approuvé, évalué en classe, certifié ou publié.

## 1. Source et périmètre effectivement vérifiés

- Archive source ouverte : `initbundle(1).zip`, contenant le workspace `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Les huit références demandées ont été lues avant rédaction : contrat pédagogique v1.2, générateur et examens, charte Québec, graphe 202, `PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md`.
- Cible unique : `kristals/qc-pri-ma-012/`. Les deux fichiers remplacés sont `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`. Les 12 autres fichiers du manifeste sont nouveaux.
- La gouvernance, le registre, `kristal.workspace.json`, `AGENTS.md`, `ALIGNEMENT.md`, le canon, le runtime et tous les autres Kristals ne sont ni modifiés ni livrés dans le delta.
- Graphe : aucun `requires`, `recommends_before` ni `reinforces` sortant de `qc-pri-ma-012` ; d'autres Kristals peuvent référencer celui-ci, ce qui n'établit aucun verrou **pour celui-ci**.

## 2. Contrôles réellement exécutés sur le dossier avant emballage

Un script indépendant de la rédaction a exécuté **23 contrôles sur 23 réussis**, à partir de l'archive source et du dossier de production :

1. Liste cible de 14 chemins distincts.
2. Présence et non-vacuité des 14 fichiers.
3. Absence de fichier additionnel dans le dossier à livrer.
4. Front matter YAML du parcours strictement identique **clé et valeur** à la version source.
5. Conservation de l'ordre et du titre des **12 sections** du parcours d'origine.
6. Front matter YAML délimité correctement.
7. Préservation des clés natives et sous-clés du contrat d'évaluation.
8. Identité, format, objectif, concepts, preuve, préalables, ordre et `family_id` inchangés.
9. Présence des treize champs de famille requis par `GENERATEUR_ET_EXAMENS.md`.
10. Contrôle des relations du graphe pour les liens sortants de ce Kristal.
11. Parsing strict des **trois fichiers JSON**.
12. Identité `qc.learning-item-bank/1.0`, ID et famille de la banque.
13. Dix ID d'items uniques, consécutifs de `q-001` à `q-010`.
14. Complétude des consignes, stimuli, réponses, critères, feedback et `validation_status=a_revoir`.
15. Deux tâches de maîtrise autonomes, dans des contextes distincts.
16. Six items paramétriques dotés d'une seed entière et de catalogues bornés.
17. Contrôle numérique indépendant de **18 variantes** cataloguées par `fractions.Fraction(K,N)==fractions.Fraction(a,b)`, bornes, et exemples calculés.
18. Correspondance entre seed, index de catalogue et instance imprimée dans les réponses.
19. Couverture des dix items dans le plan et deux preuves dans la grille.
20. Résolution de **17 liens Markdown internes**, dans le delta ou le workspace source (zéro lien relatif manquant).
21. Vérification numérique indépendante de trois cas fixes pièges : `2/6=1/3`, `10/15=2/3`, `2/4=5/10=1/2`.
22. Présence explicite de mesures d'accessibilité et de la section droits et originalité.
23. Cohérence du manifeste : version 1.2, ID, `archive_root` et liste exacte des 14 chemins.

**Portée des tests numériques** : l'arithmétique, les domaines, les instances de catalogue et trois cas fixes ont été testés. Une inspection éditoriale des 10 corrigés a été faite, mais aucun test de passation auprès d'élèves ni étude psychométrique n'a été réalisé. Les conditions d'égalité des aires/longueurs sont énoncées et vérifiables dans les scénarios textuels; les dessins matériels produits ultérieurement devront être vérifiés humainement.

## 3. Contrôles de l'archive ZIP de fusion

L'archive résultante doit être ouverte à la racine de `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Un script de contrôle de ZIP a été exécuté **après** création pour vérifier : premier chemin sous `kristals/qc-pri-ma-012/`, 14 entrées de fichiers exactement, absence de dossier enveloppe, absence de chemin absolu ou contenant `../`, conformité exacte au manifeste, fichiers non vides, JSON reparsés depuis le ZIP, et vérification CRC ZIP. **Ces contrôles sont à exécuter à nouveau à chaque réempaquetage.**

## 4. Limites non résolues

- **Revue humaine indispensable** : exactitude mathématique perçue des consignes et corrigés, difficulté des variantes, clarté en français du Québec, biais contextuels, accessibilité des supports effectivement fabriqués, temps de passation et acceptabilité du seuil non compensatoire.
- **Essai apprenant non effectué** : aucune donnée d'usage, fiabilité intercorrecteurs, calibration ni épreuve d'évaluation certificative.
- **Droits** : exemples et schémas créés ici; statut juridique de la redistribution du workspace maître à confirmer par son propriétaire. Aucun média tiers incorporé.
- **Générateur** : les variantes proviennent de catalogues fermés; le système n'a pas de générateur extensible ou solveur à intégrer automatiquement. Les tests utilisent des fractions exactes de Python et non un correcteur indépendant déployé dans le LMS.
- **Intégration** : l'extraction/fusion réelle dans une copie complète du workspace et les commandes de qualification canonique ou LMS n'ont **pas** été exécutées. Le ZIP est un **delta fusionnable**, non un build canonique ou une publication.
- **Statut** : `a_revoir`, jamais certifié, publié, homologué ou déclaré conforme au PFEQ.

## 5. Propositions facultatives (AUCUN changement des bases centrales)

1. Introduire, dans une future version de norme validée séparément, un schéma standard de `catalogue_ordonne_v1` avec seed, rendu d'instances et tests de variantes automatiques.
2. Ajouter à l'outillage central, après décision de gouvernance, un validateur machine des preuves à trois représentations et un suivi de deux contextes sans indice.
3. Définir une procédure de revue humaine, d'essai d'items et d'adaptation multimodale avant qualification. **Aucune de ces propositions n'est appliquée** à `registry/` ou `governance/` par la livraison présente.
