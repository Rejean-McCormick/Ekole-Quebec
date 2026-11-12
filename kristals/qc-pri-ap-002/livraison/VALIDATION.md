# Validation et journal de livraison — qc-pri-ap-002

**Dossier source :** archive `initbundle(1).zip`, racine `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, fournie dans la conversation. **Base :** v1.2. **Lot unique :** qc-pri-ap-002. **Statut :** `a_revoir` (non publié, non homologué, non certifié).

## Fichiers réellement produits

- **Remplacements natifs (2) :** `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json` en conservant l'identité, l'ensemble des champs YAML et des champs JSON originaux; seuls les statuts éditoriaux du JSON sont actualisés et les champs de famille sont complétés.
- **Ajouts (12) :** six modules complets `contenu/`, trois fichiers `evaluation/`, une traçabilité `sources/`, ce manifeste et ce rapport.
- **Banque :** 12 items à scénarios fixés, dont `q-011` et `q-012` épreuves autonomes à quatre cases et dans deux contextes distincts. Les matériaux, supports et contraintes sont explicités. Aucun examen certifié ni génération IA libre.

## Contrôles exécutés automatiquement avant compression

- **Banque et liens :** 378 assertions exécutées, sans échec.
- **Conservation contrat :** 47 assertions exécutées, sans échec.
- **Contenu et plan :** 52 assertions exécutées, sans échec.
- **Droits et accessibilité :** 3 assertions exécutées, sans échec.
- **Identité et graphe :** 7 assertions exécutées, sans échec.
- **Métadonnées natives YAML :** 19 assertions exécutées, sans échec.
- **Preuves et didactique :** 7 assertions exécutées, sans échec.
- **Structure initiale :** 14 assertions exécutées, sans échec.

- Méthode : assertions Python sur les fichiers UTF-8, `json.loads`, `yaml.safe_load`, comparaison des métadonnées au ZIP source, recherche de clés/chaînes nécessaires et vérification des identifiants. Le test des rubriques prouve la **présence** de critères détaillés, **pas** leur validité pédagogique auprès d'un enfant.
- Vérifications supplémentaires lors du conditionnement : manifeste exact, 14 fichiers non vides, chemins exclusivement dans `kristals/qc-pri-ap-002/`, absence de `../` et de chemin absolu, premier chemin conforme, parse des JSON réouverts, égalité octet pour octet, intégrité ZIP (CRC). Tous sont exécutés par le script de conditionnement avant l'affichage du résultat.

## Vérification des corrigés et limites de cette validation

- Les 12 réponses modèles ont été rédigées pour permettre une observation de processus (outil, geste, trace, support et comparaison); les tests automatiques confirment qu'elles sont présentes, non leur vérité pour tout matériel. Les propriétés réelles **doivent** être observées sur les planches. Les modèles explicitent les incertitudes (papier texturé, différence indiscernable, pression variable).
- **Non exécutés :** essais avec enfants, passation en classe, validation de la sécurité d'une marque précise, contrôle de toxicologie, mesure de motricité/accessibilité en conditions réelles, revue indépendante par spécialiste en arts, audit juridique de droits des travaux d'élèves, qualification Framework/canon v9, publication/activation.
- **Revue humaine nécessaire :** pertinence des quatre cases selon l'âge, lisibilité des légendes, ergonomie du matériel et adaptations, sécurité locale et inventaire des fournitures, équilibre des épreuves, cohérence observateur/élève, justesse des niveaux 0–3.
- **Droits :** textes et scénarios originaux; références externes indiquées sans copie d'œuvres ou images; aucune licence de contenu tiers inventée. Les captations de travaux ou de voix exigent une autorisation.

## Journal de modifications et propositions centrales (non appliquées)

1. YAML d'origine conservé intégralement, corps des douze sections remplacé par l'enseignement réel. JSON existant conservé avec statuts actualisés (`items_rediges_a_revoir` et `a_revoir`) et champs du contrat de génération ajoutés **dans l'unique famille native**.
2. Ajout des six modules, du plan et des deux preuves finales non compensatoires, de la grille, des sources et des fichiers de livraison.
3. **Proposition seulement :** définir au niveau du registre commun une politique documentée de substitutions de matériaux sûrs et de contrôle des adaptations motrices pour les évaluations de création. Aucun registre, norme, autre Kristal ni dossier canonique n'est modifié.

## Fusion

Se placer dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` du workspace maître **décompressé**, puis extraire `qc-pri-ap-002_livraison_v1.2.zip` à cet endroit. Le ZIP contient exclusivement des chemins commençant par `kristals/qc-pri-ap-002/`, aucun dossier parent de travail ni archive maîtresse.
