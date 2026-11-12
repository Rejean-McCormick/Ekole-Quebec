# Validation de livraison — `qc-pri-ap-003`

**Statut :** contenus rédigés, structurés et items `a_revoir`; les vérifications techniques listées ont été exécutées le 8 octobre 2026 et ont réussi. Aucune revue pédagogique humaine, publication ou certification n'a été accomplie.

## Périmètre du delta

Deux remplacements complets seulement : `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`. Douze fichiers nouveaux dans `contenu/`, `evaluation/`, `sources/`, `livraison/`. Aucun changement à `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, `AGENTS.md`, `kristal.workspace.json`, `canon/`, `docs/`, `state/`, `runtime/`, `registry/`, `governance/` ni aux autres IDs.

## Contrôles réellement exécutés

- **532 assertions pré-archivage réussies** dans le script de vérification exécuté, aucune erreur : 14 fichiers non vides, frontmatter YAML strictement inchangé, 12 sections, contrat et famille natifs conservés, liens au bon ID, 10 items complets, statut `a_revoir`, rubriques critériées et deux preuves distinctes A/B.
- Les 3 JSON de contrat, banque et manifeste sont analysés en objets; tous les 10 items ont des consignes distinctes, identifiants uniques et champs de réponse, feedback, variation et accessibilité. Aucune génération libre n'est utilisée.
- **Fusion simulée** à partir du dossier Kristal source : 2 fichiers autorisés remplacés, 12 fichiers nouveaux ajoutés, **34 autres fichiers initiaux protégés conservés octet pour octet (SHA-256)**.
- Les références Getty et CAST ont été consultées; contenu original, aucune œuvre tierce reproduite. Les critères d'accessibilité/sécurité ont été **contrôlés textuellement**, pas testés avec du matériel réel.
- Contrôle CRC ZIP, arborescence et JSON après empaquetage exécuté (résultat extérieur de ce script).

## Limites non résolues

- Aucune épreuve en classe, aucun contrôle d'accord entre évaluateurs ni de fidélité de la grille C1–C5.
- La qualité d'une production artistique ne peut pas être certifiée par des assertions automatiques. La sécurité matérielle, les allergies et les adaptations individuelles requièrent un jugement humain.
- Aucune conformité détaillée ni homologation PFEQ revendiquée. Le contenu n'a pas été fusionné au dépôt canonique ou projeté en état v9.
- Les références externes ont été consultées pour leur terminologie générale seulement; les seuils de la grille restent des créations éditoriales.

## Revue humaine avant utilisation sommative

1. **Enseignant en arts plastiques :** vérifier les occasions de création réelle et les critères sans jugement de style ou d'identité.
2. **Spécialiste accessibilité :** vérifier contrastes, alternatives tactiles, scribe non directif, taille des pièces, fatigue et temps.
3. **Responsable sécurité et vie privée :** vérifier disponibilité de matériaux sûrs, risques de petites pièces et politiques de captation.
4. **Évaluateurs indépendants :** essayer C1–C5 avec des œuvres variées, négocier les cas limites de la distinction des deux compositions.

## Propositions de changement structurel (non exécutées)

- Envisager des champs optionnels de preuves artistiques (`composition_diff_count`, `aide_non_directive`, `dimensions_observees`) dans une future norme, après consultation de l'équipe de gouvernance.
- Prévoir une annexe projet d'accessibilité et de droits des images pour l'ajout ultérieur de documents visuels; ne pas changer les bases centrales dans ce delta.
