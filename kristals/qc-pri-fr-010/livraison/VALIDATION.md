# Validation de livraison — `qc-pri-fr-010` (v1.2)

## Portée et condition de fusion

Le ZIP est un **delta** du workspace contenu dans `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip`, au chemin interne `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Décompresser le workspace source; se placer **à l'intérieur** de `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`; décompresser `qc-pri-fr-010_livraison_v1.2.zip` depuis ce répertoire. Il contient **14 fichiers exactement**, tous sous `kristals/qc-pri-fr-010/` : deux remplacements complets (`authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`) et douze nouveaux fichiers. Aucun registre ou dossier central n'est empaqueté ou modifié.

## Tests techniques effectivement exécutés

Le script local de contrôle de livraison a réalisé, avant emballage et sur l'archive finale :

- **Source et filiation :** extraction réelle et lecture des trois documents de gouvernance, du graphe, des quatre fichiers `authoring/` requis et de `kristal.workspace.json`; comparaison du contrat natif aux champs d'origine et conservation des valeurs invariantes.
- **Identité et objectifs :** concordance des IDs `qc-pri-fr-010`, `obj-1`, `crit-1`, `qc-pri-fr-010-ev-01`, du titre, des notions et du texte exact de l'objectif et de la preuve; le graphe source confirme `requires → qc-pri-fr-008` et `recommends_before → qc-pri-fr-009`; absence de `reinforces` sortant.
- **Structure :** vérification des 12 sections numérotées de `PARCOURS.md`, de l'en-tête YAML et de ses champs d'origine; décompte de 6 contenus, 3 évaluations, 2 `authoring/`, 1 source et 2 livrables.
- **Banque :** analyse JSON stricte, 8 IDs consécutifs sans doublon; champs obligatoires, difficulté et mode autorisés; chaque item relié à l'objectif, au critère et à la famille; stimuli distincts; présence des deux extraits exacts **dans** le stimulus; éléments attendus, rétroactions et bornes de variation présents; deux items de maîtrise réservés dans deux genres distincts (`q-007`, `q-008`).
- **Accès et droits :** vérification de l'existence des sections d'adaptation, d'absence de dépendance à une image dans les stimuli et du registre de provenance; ce contrôle **documentaire** ne constitue ni audit de droits de tiers ni essai avec des utilisateurs.
- **Archive :** 14 entrées fichiers non vides; tout chemin commence par `kristals/qc-pri-fr-010/`; première entrée conforme; aucun `../`, chemin absolu, dossier englobant, autre Kristal ni fichier interdit; la liste ZIP concorde exactement avec `MANIFEST.json` et l'archive est testée pour intégrité ZIP.

Les résultats chiffrés ci-dessus ont été enregistrés lors de la construction et sont à corroborer par l'extraction dans le workspace cible. Les tests automatiques vérifient la **présence et la cohérence** des propositions de corrigés; ils ne prouvent pas l'unicité ou l'équité de toutes les appréciations humaines possibles.

## Limites non résolues et revue humaine requise

1. **Items et grille non qualifiés :** tous les items `a_revoir`; relecture linguistique fr-CA, calibration de la grille (y compris avis divergents), échantillonnage et essai auprès d'utilisateurs/enseignants à réaliser. Aucune certification, homologation, validation PFEQ ni publication n'est revendiquée.
2. **Sources et droits :** textes pédagogiques proposés comme productions originales, sans reprise volontaire d'oeuvres tierces; provenance externe et statut contractuel d'utilisation à confirmer par le responsable humain avant redistribution. Les URL institutionnelles sont celles relevées dans les fichiers de gouvernance; l'actualité de leurs pages n'est pas auditée.
3. **Accessibilité réelle :** vérifier avec lecteurs d'écran, outils de synthèse vocale, affichage mobile et diverses réponses dictées/écrites; essais d'équité nécessaires. Les versions sonores sont permises par conception, mais aucun enregistrement audio n'est livré.
4. **Intégration :** aucun test LMS, aucune création de `canon/` ou `runtime/`, aucun test d'activation, aucune vérification du comportement d'un moteur de correction/variation; ce ZIP contient des contenus auteurs et des items fixes, non un examen certifié.
5. **Référence native inhabituelle :** `CONTRAT_PEDAGOGIQUE.json` conserve la valeur d'origine `referentiel_technique: gouvernance/Norme_Pedagogique_Autonome_v1.2`, alors que le répertoire réel se nomme `governance/`; source conservée telle quelle pour ne pas modifier une métadonnée existante en dehors du mandat d'enrichissement. À arbitrer par le propriétaire du schéma avant une éventuelle correction.

## Propositions **sans modification** des bases centrales

- Ajouter au schéma des familles la possibilité de distinguer explicitement `type = réponse_argumentée` de `mode = fixe` et de définir la non-utilisation d'une seed dans les banques fixes.
- Prévoir dans l'outil d'évaluation la consignation structurée de la modalité d'accès, des aides de raisonnement, des **deux extraits textuels annotés** et de leur justification séparée.
- Formaliser un statut séparant « rédaction complète », « contrôles techniques réussis », « rubrique revue par humain » et « qualifié pour usage »; ne pas promouvoir automatiquement des items `a_revoir`.
- Clarifier centralement l'orthographe de la référence `referentiel_technique` héritée, sans correction implicite dans le présent delta.

**Conclusion :** contenu rédigé et archive techniquement contrôlée; **revue humaine et qualification à réaliser**. La liste faisant foi est `livraison/MANIFEST.json`.
