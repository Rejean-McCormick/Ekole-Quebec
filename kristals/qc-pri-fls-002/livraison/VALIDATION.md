# Journal de validation et limites — qc-pri-fls-002

**Kristal :** « Vocabulaire et expressions usuelles en français » · **Discipline :** Français, langue seconde · **Objectif :** `obj-1` · **Preuve :** `crit-1` · **Famille :** `qc-pri-fls-002-ev-01`.

## Portée exacte du delta
**Archive de livraison :** `qc-pri-fls-002_livraison_v1.2.zip` ; **base du workspace :** v1.2 ; **racine interne du ZIP :** `kristals/qc-pri-fls-002/` ; **fichiers livrés :** 14, pas de workspace complet.

**Remplacements attendus (2) :** `authoring/PARCOURS.md`, `authoring/CONTRAT_PEDAGOGIQUE.json`. **Ajouts attendus (12) :** six fichiers de contenu, trois fichiers d’évaluation, une référence, le manifeste et ce rapport. Aucun fichier `AGENTS.md`, `kristal.workspace.json`, `ALIGNEMENT.md`, `docs/`, `canon/`, `state/`, `runtime/`, `registry/`, `governance/` ni aucune autre feuille n’est empaqueté.

## Contrôles réellement exécutés par le script de construction
Le script a exécuté **26 assertions préalables**, toutes réussies avant génération de ce rapport :
- OK — YAML source préservé à l’identique.
- OK — YAML parsable.
- OK — 12 sections numérotées identiques.
- OK — Identité et objectif textuels.
- OK — Contrat JSON natif inchangé sur tous les champs.
- OK — Famille possède ses 13 paramètres requis.
- OK — IDs/famille et absence de prérequis conservés.
- OK — Graphe sans liens sortants pour ce Kristal.
- OK — Banque au format JSON attendu.
- OK — 12 numéros consécutifs, uniques.
- OK — Couverture 8 fixes et 4 scénarios.
- OK — Toutes les rubriques et réponses complètes.
- OK — Tous les items liés à obj-1 / crit-1 / famille.
- OK — Statuts des items non certifiés.
- OK — Tous les scénarios sélectionnés par seed stable.
- OK — Chaque variante a le stimulus et le corrigé correspondant.
- OK — Les deux variantes de chaque scénario complètes.
- OK — Deux contextes de maîtrise vraiment distincts.
- OK — Grille explicite autonomie et deux preuves.
- OK — Sources et provenance / droits explicités.
- OK — Accessibilité détaillée.
- OK — Diagnostic ×2, guidage ×3, autonomie ×4, transferts ×2.
- OK — Au moins 2 exemples et 2 contre-exemples.
- OK — Parcours sans TODO/placeholders.
- OK — Liens relatifs du parcours vers les fichiers présents.
- OK — Liste manifeste exactement 14 chemins demandés.

Les contrôles vérifient la **cohérence structurelle** et la sélection fermée des variantes. Ils ne certifient pas automatiquement la justesse de tous les choix linguistiques, ni la validité psychométrique des rubriques. Les 12 exemples de réponses ont été relus lors de leur rédaction; ils restent expressément soumis à une revue humaine.

## Contrôles d’archive / fusion
- Le script exécute en plus, après assemblage, une vérification de la liste interne des **14 fichiers** non vides (premier chemin sous le bon Kristal), de l’absence de chemins absolus et remontants, des CRC du ZIP, et de la validité des 3 JSON.
- Il effectue une **simulation d’extraction** dans un exemplaire décompressé du bundle maître et compare les empreintes SHA-256 des fichiers d’origine : seuls les 2 fichiers autorisés sont remplacés, les 12 autres s’ajoutent et les fichiers non concernés restent inchangés.
- Si ces vérifications ne réussissent pas, le script doit échouer et ne pas considérer l’archive comme livrable. Voir aussi le journal de vérification extérieur si disponible.

## Points non résolus / à revoir humainement
1. Revue linguistique : naturel des formulations du français québécois et des autres variétés francophones, contextualisation de *tu/vous*, distinction pédagogique entre cooccurrence et collocation.
2. Revue didactique FLS : accessibilité réelle pour différents niveaux de français, stabilité de la grille et équivalence entre prestations orales, écrites et assistées.
3. Essais avec apprenants : aucune expérimentation réalisée; seuil de deux expressions et critères de niveau 2 à confirmer, sans confusion avec une note unique.
4. Protection des données : politique locale d’autorisation et de stockage des traces vocales à établir avant utilisation.
5. Droits : tous les nouveaux textes présentés comme originaux; droit de redistribuer et d’intégrer le bundle maître à vérifier auprès de son propriétaire selon ses conditions.
6. **Validation des items :** `a_revoir`; aucune certification, publication ou homologation officielle revendiquée.

## Propositions de structure non appliquées
- Ajouter ultérieurement au schéma commun un champ optionnel `preuves_requises` et un schéma de traçabilité des aides lexicale/d’accès, uniquement après décision centrale versionnée.
- Normaliser la sélection des variantes fermées et les rubriques d’observation communes dans un registre versionné plutôt que dupliquer l’algorithme dans chaque famille.
- Conserver l’information oral/écrit/communication assistée dans le LMS comme mode de preuve, sans changer les métadonnées canoniques.

**Aucune modification centrale proposée n’a été appliquée.**
