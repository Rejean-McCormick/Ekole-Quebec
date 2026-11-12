# Validation de livraison — `qc-pri-fr-007` v1.2

**Contrôles exécutés localement le 2026-10-08.** Le rapport décrit les vérifications automatisées ou par comparaison de chaînes réellement exécutées sur ce delta. **Statut :** `controles_techniques_locaux_ok_revue_humaine_requise`. Ni publication, ni certification, ni alignement PFEQ revendiqués.

## Contrôles exécutés avant empaquetage

- **OK** — Original JSON root fields preserved ; détail : set()
- **OK** — Original JSON field identifiers unchanged
- **OK** — Single family and preserved original fields
- **OK** — Original generation keys retained
- **OK** — All 13 family fields present
- **OK** — Type and fixed targets
- **OK** — All original front matter keys and values preserved ; détail : []
- **OK** — 12 numbered pathway sections in order ; détail : ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
- **OK** — 10 distinct item ids and ordered numbering
- **OK** — 10 items meet strict required schema
- **OK** — Bank one correct ID/family, obj-1/crit-1
- **OK** — No parameters, unvalidated, fixed item statements
- **OK** — All item stimuli and expected responses substantive
- **OK** — 2 distinct contexts for comprehensive proofs
- **OK** — 4 independent activities and 3 guided activities
- **OK** — Two transfer contexts and two diagnostic tasks
- **OK** — Objective criterion and no blocking prerequisite
- **OK** — Graph original read-only and single recommended link
- **OK** — Manifest exact 14 files
- **OK** — Target file set and nonempty
- **OK** — JSON files strict and reparsable
- **OK** — Link targets exist for local paths
- **OK** — 10 response anchors genuinely present in source stimuli ; détail : []
- **OK** — 10 response explanations include intended source anchor/decision

Ces contrôles incluent la conservation littérale des métadonnées d'origine (`PARCOURS.md` et contrat JSON), la présence des preuves et des corrigés, les liens locaux et le contrôle de **dix indices textuels prévus dans les stimuli**. Le rapprochement ancre/réponse est un **test de cohérence partielle**, pas une revue humaine de tous les sens acceptables.

## Contrôles du ZIP exécutés et réussis

- **OK** — archive ouverte avec succès, exactement 14 entrées; premier chemin `kristals/qc-pri-fr-007/authoring/PARCOURS.md`.
- **OK** — chaque entrée possède le préfixe `kristals/qc-pri-fr-007/`, sans chemin absolu, `../`, répertoire englobant ni fichier étranger.
- **OK** — chaque fichier interne est non vide; la liste ordonnée correspond exactement à celle du manifeste.
- **OK** — vérification CRC (`testzip`) sans erreur; les trois fichiers JSON du ZIP sont parsables.
- **OK** — le manifeste embarqué est cohérent avec les chemins effectifs.

## Livrables et changements

- **Remplacements complets** : `authoring/PARCOURS.md` (YAML original préservé, 12 sections alimentées) et `authoring/CONTRAT_PEDAGOGIQUE.json` (champs et famille d'origine préservés, 13 propriétés minimales de famille complétées, statut rédactionnel mis à jour).
- **Ajouts** : six fichiers dans `contenu/` (notions, deux modelages, deux diagnostics, G1–G3, A1–A4, deux transferts, remédiation, rappel différé); trois dans `evaluation/` (plan, dix items fixes, grille); un dans `sources/`; deux dans `livraison/`, dont ce rapport.
- Le ZIP ne contient aucun autre Kristal, ni registre, ni gouvernance, ni canon, ni runtime, ni `AGENTS.md`, ni `ALIGNEMENT.md`.

## Limites non résolues et revue humaine impérative

1. **Exactitude pédagogique/linguistique :** une personne enseignante francophone doit relire les dix stimuli, toutes les nuances de pronoms et de restrictions, les réponses alternatives, la charge cognitive, la durée et les risques d'ambiguïté. Le contrôle de chaînes ne suffit pas.
2. **Épreuve empirique :** aucun élève n'a passé les items; ni fiabilité intercorrecteurs, ni comparabilité psychométrique, ni difficulté observée. Tester Q009 et Q010, calibrer les rubriques et revoir les seuils si nécessaire.
3. **Accessibilité en conditions réelles :** formats alternatifs **prévus dans le texte**, mais non testés avec lecteur d'écran, synthèse vocale ou besoins particuliers; contrôler les accommodations sans assistance sémantique.
4. **Droits et déploiement :** textes originaux sans reprise substantielle de contenus tiers; aucune cession/licence externe spécifiée, aucune publication/activation entreprise. Une validation juridique si redistribution externe est envisagée reste distincte.
5. **Framework :** aucun `check`, `build-v9`, `check-ai`, LMS ou intégration au canon exécuté sur le workspace global; ce delta n'altère pas ses autorités et doit être revu avant usage qualifiant.
6. **Liens externes :** pages publiques de références consultées le 2026-10-08; l'accessibilité future des URL et les licences de ces pages ne sont pas garanties.

## Propositions de structure, non appliquées

- Ajouter **dans une future version centralisée**, si la gouvernance l'approuve, une définition structurée des quatre dimensions I/S/E/T et des conditions de double preuve, afin d'éviter des divergences entre Kristals.
- Définir un vocabulaire central des statuts `a_revoir`, revue humaine et essais apprenants; ne rien renommer ici.
- Clarifier lors d'une prochaine révision le champ d'origine `seed_reproductible: true` des familles lorsque leurs items sont strictement `fixe` avec `seed: null`, ainsi que la graphie existante `gouvernance/` dans `referentiel_technique` qui ne correspond pas au chemin réel `governance/`. Ces valeurs d'origine ont été **conservées**, pas corrigées silencieusement.

## Instructions de fusion

Ouvrir le dossier racine du workspace **existant** `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` et y décompresser `qc-pri-fr-007_livraison_v1.2.zip`. Ne pas extraire dans un dossier supplémentaire ni remplacer les registres. Les chemins internes sont préfixés par `kristals/qc-pri-fr-007/`.
