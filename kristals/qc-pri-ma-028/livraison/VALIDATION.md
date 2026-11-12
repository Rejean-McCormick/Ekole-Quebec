# Validation de livraison — `qc-pri-ma-028`

## Statut et périmètre

Livraison d'un **seul** Kristal en version 1.2, composée de **14 fichiers**; remplacements `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`, plus 12 ajouts. Tous les autres objets du workspace, y compris les deux Kristals préalables, sont laissés inchangés. **Les items sont `a_revoir`; aucune conformité ministérielle ni certification scientifique/pédagogique n'est alléguée.**

## Contrôles techniques effectivement exécutés

**651 assertions de préarchivage exécutées avec succès**, aucune erreur : 14 chemins exacts, contenu non vide, YAML et 12 sections, comparaison des identifiants de l’ancien contrat, préalables et famille, dix items distincts et référencés, deux manifestations, droits et accessibilité documentés.

- **Contrôle mathématique indépendant :** les **12 instances** des quatre items paramétriques ont été recalculées via lecture des `#`, puis via `W×H - nombre_de_points`; les 6 items fixes ont été confrontés à des figures de référence et à des résultats attendus indépendants. Les seeds et les quatre indices modulo 3 ont été recalculés.
- **Qualité des corrigés (contrôle documentaire) :** nombres, unités, calculs, contraintes et solutions exposées relus par assertions; les justifications pédagogiques restent à revoir humainement.
- **Fusion simulée :** exactement 2 fichiers existants remplacés et 12 ajoutés; **34 fichiers originaux protégés** du seul Kristal sont restés identiques après superposition, par SHA-256. Aucune autre entrée n’est livrée.
- **Droits :** fichiers sources effectivement lus identifiés, créations pédagogiques originales signalées, aucune musique ou image tiers intégrée. Pas d'audit juridique exhaustif.
- **Accessibilité :** modalités de réponse et supports équivalents sont documentés; aucun essai sur appareil d’assistance ou en classe effectué.
- **ZIP :** inspection des 14 entrées, chemins sûrs, validation CRC et cohérence avec le manifeste après génération; détails vérifiés par le script d’archivage exécuté.

## Limites non résolues

- Revue experte des niveaux de difficulté, des formulations, de la charge cognitive, des critères et des adaptations d'accès avant tout usage sommative.
- Aucun test avec de véritables élèves, aucune mesure du temps de passation, de fidélité intercorrecteurs ou de transfert réel en classe.
- Les banques de paramètres sont des tables finies validables et non un générateur universel; aucun énoncé IA libre n'est contrôlé ou approuvé automatiquement.
- Les exemples constituent du contenu original sans images ni licences externes utilisées; une revue des droits et politiques de diffusion du workspace demeure un devoir de l'éditeur.

## Propositions de structure (non appliquées à la base centrale)

1. Un schéma commun pour les générateurs finis (`mode_generation`, `index`, `seed`, `instances`, `verify_method`) faciliterait le contrôle machine entre disciplines.
2. Une trace de double vérification arithmétique en amont de la publication éviterait le transfert d'un corrigé jamais recompté.
3. Une procédure de validation intercorrecteurs et d'aménagement de quadrillage accessible pourrait être officialisée par la gouvernance, sans modifier celle-ci dans le présent delta.
