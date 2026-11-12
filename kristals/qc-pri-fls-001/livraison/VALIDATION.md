# VALIDATION — livraison qc-pri-fls-001 (v1.2)

## Périmètre et autorité
- Archive source réellement lue : `initbundle(1).zip` → workspace `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`.
- Sources lues : contrat pédagogique v1.2, générateur et examens, charte de conversion, graphe, `PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, `AGENTS.md`.
- Delta limité au dossier `kristals/qc-pri-fls-001/`. Seuls les deux fichiers `authoring/` existants sont remplacés; les 12 autres sont des ajouts.
- Objectif/critère/famille inchangés : `obj-1`, `crit-1`, `qc-pri-fls-001-ev-01`; aucun préalable ni ordre conseillé. Deux arêtes **entrantes** dans le graphe, sans modification.

## Tests exécutés (automatiques)
- Avant empaquetage : **4411 assertions satisfaites**, dont **4000 essais de sélection reproductible** sur les 4 catalogues fermés (`indice_session = 0..999` pour chaque item). Une assertion est ici un appel explicite au test de condition, pas un audit pédagogique.
- Vérification du YAML : en-tête initial conservé octet pour octet; **parse YAML avec PyYAML et équivalence des données**; 12 sections présentes.
- JSON : parsing effectif des contrats et banque; conservation de toutes les clés d'origine et des valeurs canoniques; paramètres exigés du générateur présents.
- Évaluations : 12 IDs consécutifs sans doublon, 8 items fixes et 4 scénarios fermés; scripts et corrigés du corpus appariés, six scripts de maîtrise distincts et absents des documents d'enseignement; deux contextes (postal fictif, jardinage fictif), chacun avec 3 consignes et corrigés narratifs.
- Couverture : deux diagnostics, trois pratiques guidées, quatre autonomes, deux transferts; plan lié à tous les IDs; champs `obj-1`, `crit-1`, famille présents.
- Provenance et droit : sources internes et CAST attribuées; contenu nouveau identifié comme original. Aucun matériel tiers intégré. La revue contractuelle des droits reste humaine.
- Sécurité/accessibilité : contrôles textuels confirmant les adaptations d'accès, objets sécuritaires, transcription masquée lors de l'écoute et non-notation de l'accent; **aucun essai sur élèves ni audit d'accessibilité en situation**.

## Contrôles de paquet prévus et exécutés au moment de la création
- 14 entrées, non vides, dans l'ordre prescrit; première entrée `kristals/qc-pri-fls-001/authoring/PARCOURS.md`.
- Aucun préfixe englobant, chemin absolu ou composant `..`; JSON du ZIP parsables; manifeste liste exactement les chemins du ZIP.
- Test CRC intégral `ZipFile.testzip()`; simulation de fusion sur copie du dossier source et vérification SHA-256 des fichiers non autorisés.

## Limites non résolues — revue humaine obligatoire
1. Essai auprès d'apprenants FLS et spécialistes du français québécois : vérification de l'intelligibilité des scripts oraux, du débit, de la variété orale et de l'équité des objets/scènes.
2. Validation des rubriques, seuil qualitatif 2/3 sur les deux contextes et conditions de répétition; ce sont des choix internes non étalonnés.
3. Validation de l'accessibilité individualisée (audition, gestes alternatifs, communication augmentée); une preuve par texte écrit ne suffit pas à attester l'écoute.
4. Vérification des droits de diffusion finaux et des dispositifs d'enregistrement éventuels. Aucun audio livré, aucune réponse d'élève observée.
5. Aucune qualification comme « publié », « homologué » ou « certifié »; pas de tests Framework v9, build canonique ni activation.

## Propositions structurelles hors delta (aucune modification globale)
- Proposer au mainteneur une colonne structurée `modalite_de_reception`, `repetitions_identiques` et `modalite_de_reformulation` au journal d'évaluation local, sans changer le registre ou le schéma central v1.2.
- Prévoir un coffre de variantes relues humainement et une méthode de sélection reproductible commune aux Kristals de langues.
