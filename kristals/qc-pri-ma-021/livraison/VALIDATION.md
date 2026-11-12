# Validation de livraison — `qc-pri-ma-021` (v1.2)

**Statut :** proposition de contenu pédagogique complète sur le plan des fichiers; **contrôles techniques exécutés**, mais revue mathématique, pédagogique, accessibilité et qualification Framework encore requises. Rédigé le 2026-10-09 dans l'environnement d'exécution; pas de certification.

## Sources et périmètre

- Frame v1.2 lue depuis l'archive source fournie, sous `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/kristals/qc-pri-ma-021/`; gouvernance v1.2 et graphe consultés.
- Deux remplacements de fichiers autorisés (`authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`) et **douze nouveaux fichiers**; exactement 14 fichiers du manifeste, sous `kristals/qc-pri-ma-021/`.
- `kristal.workspace.json`, `AGENTS.md`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, canon, documents, registre, gouvernance, état et les autres Kristals restent absents du ZIP. Aucune prétention de conformité PFEQ, homologation, publication ou activation.

## Contrôles réellement exécutés avant emballage

- **511 assertions réussies** réparties en : all_12_sections=1, all_md_scoped_id=10, allowed_difficulty=11, allowed_item_mode=11, bank_identity=1, canonical_contract_unchanged=9, checkpoint_valid=4, fixed_and_teaching_routes_checked=16, fixed_scenario_schema=7, four_variants_each=4, frontmatter_exact_preservation=1, frontmatter_yaml_parse=1, governance_family_fields=13, graph_no_outgoing=1, independent_endpoint_vector=16, internal_id_scoping=10, item_binding=11, mastery_a_checkpoint=1, mastery_b_obstacle_free=1, mastery_bfs_shortest=2, merge_added_files=12, merge_existing_files=2, minimum_bank_items=1, no_duplicate_ids=11, no_placeholder=10, noncertified_item=11, nonempty_expected_text=12, numbered_section=12, ordered_item_id=11, original_contract_keys_preserved=11, original_family_identity_unchanged=4, original_family_keys_preserved=6, original_generation_keys_preserved=4, param_destination_oracle=16, param_first_error_oracle=16, param_legal_oracle=16, param_step_count=16, param_trace_oracle=16, parametric_exhaustive_coverage=1, parametric_schema=4, planned_bank_items=1, required_item_field=154, seed_index=4, selected_case_exposed=4, shortest_two_segment_bfs=4, stable_ids_in_path=4, stable_seed=4, two_contexts_authoring=1, uncertified_family_status=1, usable_item=11.
- La banque contient **11 items** : fixe=4, parametrique=4, scenario_controle=3; niveaux initial=3, intermediaire=4, transfert=4. Ils portent chacun `obj-1`, `crit-1`, `qc-pri-ma-021-ev-01`, et le statut `a_revoir`.
- **16 variantes paramétriques (4 par famille d'item, 4 items)** : trace et légalités vérifiées par simulateur indépendant de pas unitaires, bilan de vecteurs entiers, contrôle des seeds, identification des **2 cas de sortie**; q-009 : contrôle indépendant de minimalité par recherche en largeur (BFS) via le point obligatoire.
- **16 trajets fixes de cours/diagnostic/pratique/preuves/reprise** recalculés, dont les deux routes de maîtrise; les distances minimales des deux preuves ont été revérifiées par BFS, avec contrôle de la visite du comptoir et de l'évitement des obstacles.
- YAML original **conservé octet pour octet dans le frontmatter** et parsé; douze sections numérotées; objectif, preuve, prérequis, famille et anciens champs JSON conservés. Graphe contrôlé : aucune arête sortante de cet ID; aucune nouvelle arête créée.
- Contrôles de cohérence de périmètre, de références d'identifiants, de présence des documents, de textes vides et de mentions de placeholders. Sources et droits explicitement renseignés; adaptations de présentation et absence d'obligation de déplacement physique précisées dans les documents (contrôle de **présence textuelle**, pas essai d'accessibilité).
- Superposition vérifiée par **comparaison des chemins à la source maître** : exactement 2 chemins déjà existants remplacés et 12 chemins nouveaux ajoutés; pas d'extraction ni de réécriture des autres chemins.

## Contrôles d'emballage

- Une fois le ZIP créé par le script de validation : vérification des **14 entrées**, du premier chemin `kristals/qc-pri-ma-021/authoring/PARCOURS.md`, de la racine unique `kristals/qc-pri-ma-021/`, des chemins sûrs (sans absolus ni `..`), de la liste exacte du manifeste, du CRC de chaque entrée et du parsing JSON strict des trois fichiers JSON (`CONTRAT_PEDAGOGIQUE.json`, `BANQUE_ITEMS.json`, `MANIFEST.json`).
- La réussite de ces contrôles est nécessaire avant remise du lien; aucun résultat non exécuté n'est présenté comme testé.

## Limites, revue humaine et propositions (non appliquées)

1. **Revue pédagogique humaine :** vérifier la clarté « points »/« cases », choix de 6 × 6, difficulté, diversité des situations, compréhension des instructions et absence de surcharge; tester auprès d'élèves avant toute utilisation sommative.
2. **Mathématique et notation :** revoir les formulations des corrigés, l'unicité/équivalence des trajets, le choix de la contrainte de minimalité et les seuils de niveau 2; les tests arithmétiques ne remplacent pas ce jugement.
3. **Rubriques et fidélité :** mener essai avec correcteurs indépendants sur les deux contextes A/B, vérifier fiabilité inter-évaluateurs et modalités de nouvelle preuve après remédiation.
4. **Accessibilité et sécurité :** vérifier en pratique qualité des supports tactiles/braille, lecture d'écran, contraste, transcription orale/scribe, fatigue cognitive et équité; aucun test réel d'accessibilité assistée ni usage de robot physique n'a été fait.
5. **Droits :** texte original et fichiers internes cités; absence de recherche de licences externes. Revue de droit de redistribution de l'archive maîtresse encore nécessaire.
6. **Proposition non appliquée :** formaliser dans la gouvernance un schéma de variantes fermées (`parametres.cas`, seed, oracle de route, trace et validation) et une trace LMS structurée des deux manifestations autonomes. Aucun registre, schéma central, fichier canonique, build-v9 ou activation modifié ici.
