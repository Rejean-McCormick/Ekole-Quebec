# Validation du delta `qc-pri-ma-023` — v1.2

**Portée :** uniquement `kristals/qc-pri-ma-023/` ; **statut :** préparation techniquement vérifiée, revue pédagogique humaine requise. Aucune certification, homologation, publication ou activation.

## Exécution locale, vérifiable

Contrôles exécutés sur le dossier temporaire avant l'archivage :

1. **Réussi :** Manifest JSON strict, 14 chemins uniques, racine de fusion.
2. **Réussi :** 13 fichiers de rédaction présents avant génération du rapport.
3. **Réussi :** Aucun chemin dangereux, dossier parent ou autre Kristal.
4. **Réussi :** Banque et manifeste : format / IDs exacts.
5. **Réussi :** 12 items distincts, séquence consécutive, tous liés à obj-1 / crit-1 / famille.
6. **Réussi :** Consigne/stimulus/réponse/critères/feedback non vides, types et statuts valides.
7. **Réussi :** Quatre items paramétriques, seeds entiers et deux preuves en contextes distincts.
8. **Réussi :** Frontmatter natif YAML conservé exactement (texte et ordre).
9. **Réussi :** Structure des 12 sections numérotées du microparcours conservée.
10. **Réussi :** Tous les champs, familles et valeurs originaux JSON v1.2 conservés.
11. **Réussi :** Contrat famille complet selon GENERATEUR_ET_EXAMENS.
12. **Réussi :** Identité, objectif, preuve, préalables, séquence immuables.
13. **Réussi :** Graphe original : 0 requires sortants et lien conseillé qc-pri-ma-021.
14. **Réussi :** 8 items fixes ont un mode fixe, seed null et des corrigés documentés.
15. **Réussi :** Gabarits fixes simples convexes et nombres de paires exacts par 2 méthodes.
16. **Réussi :** Règles de 8 corrigés fixes contrôlées par corpus attendu.
17. **Réussi :** Item paramétrique documents variables / domaines / contraintes / résolution / trace : qc-pri-ma-023-q-009.
18. **Réussi :** Item paramétrique documents variables / domaines / contraintes / résolution / trace : qc-pri-ma-023-q-010.
19. **Réussi :** Item paramétrique documents variables / domaines / contraintes / résolution / trace : qc-pri-ma-023-q-011.
20. **Réussi :** Item paramétrique documents variables / domaines / contraintes / résolution / trace : qc-pri-ma-023-q-012.
21. **Réussi :** 4×1024 seeds ×4 polygones: 16384 cas intègres (2 solveurs, convexité, invariance).
22. **Réussi :** Corrigés des 4 seeds publiés concordent avec le solveur indépendant et le texte.
23. **Réussi :** Contenu des six leçons présent et non-placeholder.
24. **Réussi :** 2 tâches diagnostics, 3 guidages, 4 autonomes, 2 transferts explicitement présents.
25. **Réussi :** Deux exemples résolus et ≥2 contre-exemples présents.
26. **Réussi :** Traçabilité de 12 items au plan, grille et deux contextes.
27. **Réussi :** Accès multimodal, droits, limites humains non revendiqués.
28. **Réussi :** Textes référencent uniquement ce Kristal et son lien conseillé.
29. **Réussi :** Liens locaux cités vérifiés vers les chemins internes livrés.


**Synthèse :** 35 assertions nommées réussies; 4 modèles paramétriques × 1 024 graines admissibles × 4 figures = **16,384 figures instanciées vérifiées** par comparaison de deux détecteurs de parallélisme exacts (déterminant et directions normalisées), convexité et conservation des propriétés. Les deux preuves de maîtrise sont des items séparés (`q-011` et `q-012`). Les contrôles automatiques sont des vérifications techniques, pas une validation scientifique en classe.

## Limites non résolues

- Aucun essai auprès d'élèves ni validation par un spécialiste de didactique mathématique, orthopédagogue ou de l'accessibilité tactile n'a été réalisé. Les rubriques et les situations fictives requièrent une revue de compréhension, de neutralité et de faisabilité.
- Les schémas quadrillés ne sont pas fournis comme images : les coordonnées et descriptions sont exploitables, mais un support visuel/tactile équivalent devra être matérialisé avant usage si nécessaire.
- Aucun site externe cité dans `REFERENCES_EVIDENCE.md` n'a été inspecté ici. Les références sont attribuées à la gouvernance locale; pas de validation PFEQ, d'homologation ni de garantie de droits sur le workspace maître.
- Le générateur est **spécifié et testé** dans cet ensemble fermé de gabarits, mais aucun composant d'exécution LMS n'est livré ou testé; la conformité d'intégration nécessite un essai ultérieur.

## Revue humaine à planifier (non effectuée)

Vérifier les formulations « exactement une/deux paires », les distinctions côté/contour et la lisibilité des coordonnées; tester une représentation tactile de côtés parallèles obliques; faire résoudre les 12 items par une personne indépendante et vérifier les réponses/l'erreur typique; évaluer la charge de calcul et la charge de lecture selon le profil réel des apprenants; vérifier la licence de diffusion du corpus parent; tester l'intégration dans l'outil de déploiement et l'archivage sécurisé des productions.

## Propositions de changement de structure (non appliquées)

1. Ajouter dans une version future du **schéma central** un champ formel `critere_id` obligatoire dans les familles (le delta le déclare sans remplacer les champs natifs).
2. Définir un adaptateur standard **coordonnées → quadrillage tactile / SVG accessible**, avec contrôle automatique de non-chevauchement et description alternative, hors de ce delta.
3. Prévoir un journal LMS privé des deux manifestations (seeds, contextes, aides et dimensions C1–C4), indépendant du contenu canonique; versionner une procédure de qualification humaine des items.

**Fichiers protégés :** aucun `kristal.workspace.json`, `AGENTS.md`, `authoring/ALIGNEMENT.md`, dossier `docs/`, `canon/`, `state/`, `runtime/`, `registry/`, `governance/` ou autre Kristal inclus ou modifié dans l'archive.

## Contrôles après archivage (effectivement exécutés)

- **Réussi :** ZIP 14 entrées, premier chemin et tous les chemins à la racine demandée.
- **Réussi :** ZIP sans archive englobante, sans arborescence globale ni traversée de chemin.
- **Réussi :** ZIP entries non vides et identiques en SHA256 aux fichiers de travail.
- **Réussi :** ZIP JSON parsable et manifest reflet exact des entrées.
- **Réussi :** ZIP CRC testzip et taille non nulle.
