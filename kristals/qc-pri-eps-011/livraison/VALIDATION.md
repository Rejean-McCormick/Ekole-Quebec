# VALIDATION DE LIVRAISON — qc-pri-eps-011

**Base :** workspace `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis`, version pédagogique 1.2. **Périmètre :** uniquement `kristals/qc-pri-eps-011/` (14 fichiers).

## Contrôles effectivement exécutés avant fabrication du ZIP
Test réalisé par script de validation local, sur les fichiers présents et sur les métadonnées natives extraites de l’archive maîtresse. Les contrôles de structure/exactitude logique ne remplacent pas un examen scientifique ou une revue avec élèves.

| Résultat | Contrôle exécuté |
|---|---|
| Réussi | 01_source_native_presente |
| Réussi | 02_exactement_14_chemins_requis |
| Réussi | 03_les_14_fichiers_existent |
| Réussi | 04_les_14_fichiers_non_vides_apres_validation |
| Réussi | 05_yaml_entete_preserve_mot_a_mot |
| Réussi | 06_yaml_analyse_et_metadata_identique |
| Réussi | 07_douze_sections_numerotees |
| Réussi | 08_identite_objectif_critere_invariants |
| Réussi | 09_metadonnees_contrat_toutes_preservees |
| Réussi | 10_valeurs_canon_du_contrat_preservees |
| Réussi | 11_unique_famille_native_preservee |
| Réussi | 12_champs_nat_famille_preserves |
| Réussi | 13_champs_minimum_gouvernance_complets |
| Réussi | 14_aucun_prerequis_strict_ajoute |
| Réussi | 15_format_banque_exact |
| Réussi | 16_identifiants_famille_coherents |
| Réussi | 17_nombre_items_12 |
| Réussi | 18_numerotation_sans_trous_doublons |
| Réussi | 19_champs_communs_12_items |
| Réussi | 20_justifications_et_retours_non_vides |
| Réussi | 21_identites_items_toutes_associees |
| Réussi | 22_difficultes_et_modes_permis |
| Réussi | 23_statuts_non_certifies |
| Réussi | 24_toutes_notions_couvertes |
| Réussi | 25_deux_preuves_distinctes |
| Réussi | 26_contextes_differents |
| Réussi | 27_autonomie_et_2_preuves_dans_grille |
| Réussi | 28_plan_relie_les_12_items |
| Réussi | 29_diagnostics_et_guidages_et_pratiques |
| Réussi | 30_deux_transferts_distincts |
| Réussi | 31_sources_faits_tracables |
| Réussi | 32_acces_protections_explicites |
| Réussi | 33_liens_locaux_documents_existants |
| Réussi | 34_manifest_liste_complete_exacte |
| Réussi | 35_sans_lien_vers_autre_contenu_de_kristal |
| Réussi | 36_scenario_11_jeu_AB_complet |
| Réussi | 38_scenario_11_100_seeds |
| Réussi | 40_scenario_11_instance_seed_paire |
| Réussi | 37_scenario_12_jeu_AB_complet |
| Réussi | 39_scenario_12_100_seeds |
| Réussi | 41_scenario_12_instance_seed_paire |

**Bilan avant ZIP : 41 contrôles réussis.** L’algorithme des deux scénarios A/B a été vérifié sur 100 graines consécutives par scénario, soit 200 sélections; ce test démontre la règle de sélection, pas la qualité humaine des réponses.

## Contrôles prévus puis exécutés sur l’archive finale
- [x] 14 entrées exactement, chaque entrée un fichier régulier et non vide.
- [x] Le premier chemin et tous les autres commencent par `kristals/qc-pri-eps-011/`.
- [x] Aucun chemin absolu ni segment `../`, aucun répertoire englobant, pas de fichier central ou d’un autre Kristal.
- [x] Concordance de la liste du manifeste avec les chemins internes et analyse JSON native (`MANIFEST.json`, `CONTRAT_PEDAGOGIQUE.json`, `BANQUE_ITEMS.json`).
- [x] CRC de l’archive vérifié par `ZipFile.testzip()` après réouverture.

## Contrôles de contenu réellement effectués et limites
- Vérification textuelle et structurale : identifiant, objectif et preuve inchangés; contenus des items non vides et réponses assorties de critères et feedback; toutes notions présentes. Examen du raisonnement de chaque corrigé rédigé lors de la production, **sans pilote externe ni validation médicale professionnelle**.
- Sécurité : scénarios sans performance réelle, eau explicitement potable lorsqu’il est demandé d’en boire, recours à un adulte et alternatives si ressource manquante. Contrôle automatisé partiel de mots clés, **pas** un audit de sécurité expert.
- Droits : liens vers pages officielles, scénarios textuels originaux, aucune image/audio de tiers incluse; provenance documentaire consignée. Aucune vérification juridique exhaustive des conditions de réutilisation des sites externes (contenu non reproduit).
- Accessibilité : modalités orales, écrites, textes de remplacement et communication assistée décrites; **aucun essai d’accessibilité par utilisateurs** ni audit WCAG d’une interface.
- Références entre fichiers : chemins locaux cités examinés; graphes et bases centrales lus sans altération. Les liens web étaient consultables au moment de la recherche, leur pérennité n’est pas garantie.

## Revue humaine nécessaire avant qualification
1. Faire relire par une personne compétente en éducation à la santé au primaire les nuances de repos, hygiène, eau potable, prévention et conduite à tenir avec les règlements scolaires.
2. Vérifier que le niveau de vocabulaire, la durée et la charge des 12 tâches conviennent aux élèves concernés; expérimenter et calibrer la grille D/E/S/A.
3. Examiner l’accessibilité réelle des supports, la neutralité culturelle/économique et le traitement des élèves ayant des besoins particuliers ou accès limité aux ressources.
4. Réviser les 2 variantes A/B et les réponses observées avant toute évaluation sommative. Aucune qualification de type « homologué », « certifié » ou « publié » revendiquée.

## Propositions de structure — non appliquées
- Dans une version centrale ultérieure, prévoir une propriété structurée `sensibilite_sante_et_vie_privee` pour les productions d’EPS.
- Ajouter une représentation machine des modalités d’accessibilité et des limites de génération, après décision centralisée, sans modifier `governance/`, `registry/` ni `kristal.workspace.json` ici.

## Statut
**Contrôles techniques réussis; revue pédagogique humaine requise.** Pas d’alignement PFEQ affirmé. L’archive n’est pas qualifiée comme cours validé.
