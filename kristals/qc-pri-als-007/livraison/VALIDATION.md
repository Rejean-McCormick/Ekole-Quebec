# Validation de livraison — `qc-pri-als-007` (v1.2)

**État :** delta réalisé et contrôlé techniquement; `validation_status: a_revoir` pour tous les items. **Archive cible :** `qc-pri-als-007_livraison_v1.2.zip`. **Périmètre :** un seul Kristal, `qc-pri-als-007`.

## Contrôles réellement exécutés

- Script `qa_als007.py` exécuté localement : **165 assertions de préparation** réussies, avec levée d'exception en cas d'échec (identité, YAML, JSON, liens, items, preuves, corrigés, couverture, droits, accessibilité et fusion simulée).
- YAML du parcours analysé avec PyYAML; les **12 sections numérotées 1 à 12** sont présentes et ordonnées; toutes les propriétés du frontmatter initial ont été comparées.
- JSON du contrat, de la banque et du manifeste analysés par `json.loads`; les champs et les familles v1.2 d'origine ont été comparés récursivement pour tout attribut invariant; seules les valeurs de suivi d'état ont évolué.
- **12 items** `q-001` à `q-012` continus, sans doublon, rattachés à `obj-1`, `crit-1` et `qc-pri-als-007-ev-01`; chaque texte, correction, preuve textuelle et choix de repères A–D a été vérifié automatiquement (inclusion littérale, cohérence référentielle). Les preuves `q-011` et `q-012` ont chacune trois associations, un détail distinct et des contextes séparés.
- Contrôle documentaire de la présence de deux diagnostics, trois exercices guidés, quatre pratiques autonomes et deux transferts; contrôle du plan, de la grille, de la provenance, des modalités d'accessibilité et de la sécurité **sur les textes écrits**.
- `registry/GRAPHE_PEDAGOGIQUE_202.json` interrogé : pas d'arête `requires` sortant de ce Kristal; ordre conseillé `qc-pri-als-002` confirmé et non bloquant. Fichiers communs et de référence confirmés présents dans le ZIP maître.
- Simulation des chemins de fusion à partir de la liste des membres du ZIP maître : **2 remplacements** (`authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`), **12 ajouts**, aucune autre modification de workspace requise.
- Le contrôle final de l'archive (`zipfile.testzip`, comptage et ordre des 14 membres, racine, absence de traversal, contenu non vide, JSON interne parsable, exactitude du manifeste) est exécuté lors de la création; l'archive n'est livrée que s'il réussit.

## Limites non résolues et revue humaine requise

1. **Anglais naturel et niveau :** faire relire la naturalité, les ambiguïtés possibles et la charge lexicale de chaque mini-texte par une personne compétente en ALS; essayer en conditions de classe.
2. **Validité des seuils :** les seuils 2/3 associations, détail exact, preuve et sens global sont une instrumentation **interne proposée**, non calibrée empiriquement; vérifier fidélité intercorrecteurs et risque de devinette.
3. **Accessibilité réelle :** essais sur impression, contraste, lecture assistée/lecteur d'écran et réponses par pointage; documenter séparément toute lecture orale du texte anglais, car elle change l'interprétation de la compréhension écrite.
4. **Droits :** les stimuli sont rédigés pour ce projet sans usage déclaré d'images, noms tiers, données personnelles ou extraits reproduits. Revue éditoriale de similarité/licence recommandée avant diffusion publique.
5. **Observation des acquis :** aucune passation auprès d'apprenants ni mesure de l'effet pédagogique n'a été réalisée; aucune qualification « publié », « certifié » ou « homologué ».

## Propositions non appliquées à la structure centrale

- Ajouter ultérieurement un champ de traçabilité des modalités de lecture (texte imprimé, agrandi, texte vocalisé) dans le système de passation **sans modifier** le schéma v1.2 actuel.
- Définir dans un futur contrat central un protocole commun de revue humaine des items linguistiques et de vérification des versions de corpus, avec des critères d'équivalence d'accessibilité.

## Fusion

Extraire l'archive maître, entrer dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, puis y extraire le delta dont le premier dossier interne est `kristals/qc-pri-als-007/`. Ne pas créer un second dossier parent. Aucun registre global, aucune gouvernance, aucun fichier du canon, des docs, de l'état, du runtime ou d'un autre Kristal n'est inclus.
