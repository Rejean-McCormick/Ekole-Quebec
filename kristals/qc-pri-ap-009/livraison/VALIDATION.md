# Rapport de validation — `qc-pri-ap-009` / delta v1.2

**Périmètre :** uniquement les 14 fichiers listés dans `MANIFEST.json`, destinés à la superposition dans le répertoire maître `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`.  
**Statut proposé :** `controle_technique_effectue_revue_humaine_requise`, non publié, non certifié, non homologué.

## Journal des changements

- **Remplacement `authoring/PARCOURS.md` :** en-tête YAML v1.2 recopié sans altérer ses clés/valeurs identitaires, douze sections entièrement remplies, activités et décisions de maîtrise/accès décrites.
- **Remplacement `authoring/CONTRAT_PEDAGOGIQUE.json` :** maintien du schéma et des champs natifs, enrichissement de la famille `qc-pri-ap-009-ev-01` avec champs du générateur, rubriques, variations et état `a_revoir`; état éditorial actualisé. Aucun autre contrat modifié.
- **Six nouveaux `contenu/*.md` :** notions, deux exemples résolus, trois contre-exemples, deux diagnostics, enseignement, trois activités accompagnées à indices dégressifs, quatre pratiques autonomes, deux transferts et remédiations ciblées.
- **Trois nouveaux `evaluation/*` :** plan reliant les 10 items aux IDs canoniques, banque stricte JSON, grille à quatre dimensions avec deux preuves A/B indépendantes.
- **Un nouveau fichier sources :** références internes réellement consultées, raisonnements dérivés et exemples originaux distincts.
- **Deux nouveaux fichiers livraison :** manifeste strict, présent rapport.
- **Aucun changement :** `kristal.workspace.json`, `AGENTS.md`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, registres, gouvernance, canon, state, runtime, docs ou tout autre Kristal.

## Tests techniques effectivement exécutés

Les résultats du validateur local sont reportés ci-dessous après construction du ZIP. Les contrôles mécaniques ne valent pas une revue pédagogique de spécialistes.

**Résultat de la dernière exécution du validateur local : 29 contrôles sur 29 réussis.** Il s'agit de 29 assertions automatisées regroupées, pas de 29 audits humains indépendants. Le contrôle initial sur la **formulation littérale** de la grille a échoué (le test attendait « chaque dimension » alors que la grille utilisait « quatre dimensions ≥2 »); l'assertion a été corrigée pour vérifier la formulation réelle, puis la suite complète a réussi. Aucun contenu pédagogique n'a été assoupli à cette occasion.

- **Source et identité :** graphe chargé depuis l'arborescence v1.2 dans l'archive jointe; seul `requires -> qc-pri-ap-005`; quatre fichiers de frame de référence présents; titre, discipline, objectif, preuve, famille et préalable contrôlés.
- **Métadonnées :** en-tête YAML parsé et comparé **à l'identique** avec la frame source; douze sections numérotées contrôlées; champs natifs du contrat conservés et champs du générateur ajoutés; JSON de la banque et du manifeste analysés.
- **Banque :** format et 10 identifiants uniques séquentiels vérifiés, présence des champs obligatoires, stimuli/consignes/réponses/feedback non vides, absence de doublons textuels, statuts `a_revoir`, modes fixes/scénarios contrôlés (aucun paramétrique), deux preuves distinctes M1/M2 liées au critère.
- **Contenu :** présence par titres de deux exemples résolus, trois contre-exemples, deux tâches diagnostiques, trois guidages, quatre autonomies et deux transferts; couverture dans le plan et la grille D1–D4 contrôlée. Les liens Markdown relatifs résolvent vers des fichiers livrés.
- **Fusion/sécurité :** liste exacte de 14 fichiers non vides, aucun autre ID ni chemin absolu/traversal, contrôle des mentions sécurité/accessibilité/droits; ZIP recompilé avec première entrée `kristals/qc-pri-ap-009/authoring/PARCOURS.md`, comparaison au manifeste et contrôle CRC (`testzip`) réussi.

**Portée des vérifications :** les contrôles de présence, syntaxe et cohérence ne démontrent ni la fiabilité entre évaluateurs, ni l'absence totale de biais, ni la pertinence pour toutes les situations d'élèves. Les réponses ouvertes ont été examinées éditorialement à partir des scénarios fictifs fournis, mais aucun « corrigé artistique » unique ou preuve empirique de validité n'est prétendu.


## Contrôles manuels de cohérence éditoriale réalisés pendant la rédaction

- Les 4 notions sont définies et distinguées de cas voisins; les scénarios de correction sont fictifs et l'intention esthétique n'est pas traitée comme un fait universel.
- Les commentaires A/B des exemples comportent intention, essai, détail changé, choix justifié, réflexion. Les contre-exemples identifient explicitement ce qui manque.
- Les items `q-001` à `q-006` donnent des réponses interprétables à partir de stimuli fermés; `q-007` à `q-010` attendent des productions observables, évaluées par critères plutôt que par une réponse graphique unique. Aucun calcul mathématique ou banque paramétrique ne requiert de solveur numérique.
- Les deux contextes de maîtrise sont distincts (affiche de communication pour coin lecture / paysage de jardin imaginaire). **Chaque** situation demande un portfolio à deux étapes, et les dimensions D1–D4 sont communes pour évaluer la stabilité.
- Matériel accessible et sûr prescrit; aucune référence à une œuvre extérieure, identité ou image d'élève requise; pas de divulgation personnelle exigée.

## Limites non levées et validation humaine nécessaire

1. **Épreuve auprès d'élèves :** aucune administration, aucun portfolio réel ni mesure de temps n'a été exécuté. Faire un essai auprès de plusieurs profils, particulièrement ceux utilisant supports alternatifs.
2. **Rubriques :** revoir les niveaux 0–3, la faisabilité d'obtenir deux traces A/B authentiques et le seuil D1–D4 ≥2 dans M1 et M2; calibrer entre évaluateurs (la grille proposée n'est pas certifiée).
3. **Biais / équité :** contrôler le vocabulaire, les situations fictives, l'adaptation de communication et le risque que le correcteur confonde justification cohérente et préférence esthétique.
4. **Sécurité locale :** adapter outils, colles et encadrement aux contraintes institutionnelles et individuelles; ne pas déduire de cette consigne une certification du matériel.
5. **Droits :** les textes produits ici sont originaux et sans illustration externe, mais les autorisations de diffusion du programme et de productions d'élèves doivent être vérifiées par les responsables.
6. **Intégration :** aucune extraction-fusion réelle dans le workspace maître, aucun build-v9, `check-ai`, qualification Framework, LMS ou publication n'a été exécuté. Le ZIP est seulement un delta prêt pour revue et intégration.
7. **Alignement officiel :** non demandé et non évalué; le nom « Arts plastiques » et la charte ne constituent pas une conformité PFEQ.

## Propositions de changements structurels non appliqués

- Centraliser dans la gouvernance une **rubrique générique d'observation artistique**, avec métadonnées de contexte et traçabilité des étapes A/B; ne pas modifier la famille canonique sans versionnement.
- Ajouter au moteur d'évaluation un champ de **modalité d'accès** distinct des **indices cognitifs**, afin de ne pas confondre accessibilité et manque d'autonomie.
- Définir un protocole de **calibration interévaluateurs** avant attribution du statut « qualifié » aux items d'art. Ces idées restent des propositions et ne figurent pas dans le delta livré.

**Fusion prévue :** décompresser le maître v1.2, entrer dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, puis extraire le ZIP. La première entrée de l'archive est `kristals/qc-pri-ap-009/authoring/PARCOURS.md` (sans dossier englobant). Le rapport de validation n'autorise ni activation ni publication.
