# Validation de livraison — qc-pri-fr-024

**Archive :** `qc-pri-fr-024_livraison_v1.2.zip`  
**Base :** frame v1.2 de `initbundle(1).zip`, racine interne de la source `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`.  
**Périmètre :** exclusivement 14 chemins sous `kristals/qc-pri-fr-024/`, dont deux remplacements complets et douze créations. **Statut :** `a_revoir`, non certifié, non homologué, non publié.

## Fichiers produits

- Remplacements : `authoring/PARCOURS.md` (YAML natif conservé + douze sections développées), `authoring/CONTRAT_PEDAGOGIQUE.json` (famille native conservée et champs de génération complétés).
- Ajouts : six modules de contenu; plan, banque de dix items, grille de maîtrise; références; manifeste; ce rapport.

## Contrôles effectivement exécutés

*Le bilan ci-dessous est produit par un script local de validation utilisant `zipfile`, `json`, `yaml`, des assertions de schéma/identité et un contrôle arithmétique ciblé.*

- ✅ manifest_exact_14_and_order
- ✅ all_files_nonempty
- ✅ no_unlisted_files
- ✅ ids_titles_objectives_constant
- ✅ source_yaml_keys_and_identity
- ✅ twelve_section_preservation
- ✅ original_contract_keys_preserved
- ✅ family_minimum_fields
- ✅ no_strict_prerequisites
- ✅ json_parseable
- ✅ bank_format_ids
- ✅ ten_unique_sequence
- ✅ items_minimal_schema
- ✅ all_items_usable_fixed
- ✅ independent_distinct_proofs
- ✅ factual_check_q009
- ✅ source_rights_accessibility_sections
- ✅ relative_markdown_links (links checked: 0 broken: [])
- ✅ relative_code_references_resolve (21 refs, 0 missing)
- ✅ source_graph_edges_checked
- ✅ archive_path_safety

**Contrôles post-empaquetage :** exécution consignée ci-dessous.

## Revue de contenu manuelle limitée (effectuée par rédaction, **pas** essai terrain)

- Cohérence de première lecture des scripts et réponses préparés : correspondance des heures (9 h/10 h et 11 h 20), des acteurs (adulte qui découpe), du sens des restrictions (*ne...pas*, *seuls*, *si*), de l'ordre, du lieu et des causes. **Cette lecture n'est pas une validation indépendante humaine**.
- Deux contextes de maîtrise volontairement distincts : q-007 (service collectif d'échange de livres) et q-008 (atelier de maquette). Tous les items restent `a_revoir`.
- Matériel original sans image externe, audio ni texte protégé reproduit; provenance de méthode et statut des droits documentés dans `../sources/REFERENCES_CONTENU.md`. Aucun nom propre personnel ni collecte de données privées dans les stimuli.

## Limites non résolues et revue humaine nécessaire

1. **Aucun pilote avec des élèves**, aucun calibrage intercorrecteur, aucune démonstration empirique que 2/3 est le seuil optimal dans les cinq dimensions.
2. **Aucun audio fourni ni testé** : la lisibilité à l'oral, la durée, les pauses et les effets de différentes voix doivent être testés; faire revoir la fidélité des scripts en français québécois par des spécialistes.
3. **Accessibilité** : vérifier, avec le personnel compétent, adaptations pour les personnes malentendantes ou sourdes et outils de communication; les substitutions textuelles/signées changent potentiellement le construit évalué.
4. **Droits/publication** : autorisation institutionnelle de distribution, politique de captation de voix et procédures de confidentialité non évaluées juridiquement. Aucun droit de tiers reproduit à notre connaissance; la titularité des productions nouvelles reste à établir.
5. **Couverture des connaissances et biais** : faire relire les dix items pour clarté, équivalence de difficulté, variétés linguistiques, contexte culturel et longueur des messages; valider questions et rubriques humainement avant toute qualification.
6. **Infrastructure/framework** : aucune exécution des commandes `check`, `build-v9`, `check-ai` du workspace maître; aucun canon, registre ou dérivé technique construit ou modifié; seul le delta pédagogique a été vérifié.

## Propositions de changement de structure (non appliquées)

- Ajouter un référentiel central de **scripts audios revus** (identifiant, version, durée, licence, lecteur, transcript réservé au correcteur), avec contrôles d'équivalence de débit/prosodie.
- Séparer formellement « preuves orales auditives » et « adaptations linguistiques signées » pour gérer l'équivalence des critères sans confondre accès et objectif mesuré.
- Ajouter à l'outillage de gouvernance un validateur automatique des champs `family_id`, `critere_id`, des preuves croisées et des versions d'items, et un protocole de cotation intercorrecteurs.

**Fusion :** décompresser la maîtresse, entrer dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, puis extraire **à cet endroit** le présent ZIP. Ne rien extraire au-dessus de ce niveau et ne pas remplacer d'autres Kristals. L'archive ne contient pas la maîtresse.

- ✅ zip_first_path_correct
- ✅ zip_exact_files
- ✅ zip_no_parent_traversal
- ✅ zip_nonempty_entries
- ✅ zip_content_identical
- ✅ zip_embedded_json_valid
