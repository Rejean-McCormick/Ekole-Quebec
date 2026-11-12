# Validation locale — livraison `qc-pri-ma-016` v1.2

**Archive :** `qc-pri-ma-016_livraison_v1.2.zip`. **Racine de fusion :** `kristals/qc-pri-ma-016/`. **Statut :** contrôles techniques et arithmétiques locaux réalisés; items `a_revoir` et relecture humaine obligatoire. **Ni publié, ni certifié, ni homologué.**

## Composition du delta

- **14 fichiers, seulement pour cet ID :** remplacement complet de `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`; 12 nouveaux fichiers (6 modules de contenu, 3 d'évaluation, 1 de sources, manifeste et ce rapport).
- YAML du parcours original conservé sans changement et 12 sections explicitement développées; champs natifs JSON conservés, famille existante enrichie des champs prévus par `GENERATEUR_ET_EXAMENS.md`.
- Banque de **12 items** dont **6 paramétriques** à seed fixe, 3 variantes documentées chacun, soit **18 variantes**, tous au statut `a_revoir`.
- Deux preuves de sortie non interchangeables : `q-009` **marché fictif** (prix total et monnaie rendue), `q-010` **marche fictive** (distance parcourue et restante). **Deux calculs et deux vérifications de plausibilité par preuve** sans indice conceptuel.
- Aucune pièce `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, `AGENTS.md`, `kristal.workspace.json`, ni `governance/`, `registry/`, `docs/`, `canon/`, `runtime/`, `state/` ni autre Kristal incluse.

## Tests effectivement exécutés dans le script de production

- Présence/lecture des **8 pièces sources** prévues (trois gouvernances, graphe, quatre fichiers `authoring/`), seul lien sortant `requires` vers `qc-pri-ma-015`, concordance ID/titre/objectif/preuve, aucun ordre conseillé.
- Vérification **exacte de l'en-tête YAML original** avant/après remplacement, lecture YAML si module présent et présence des 12 sections; contrat JSON reparsé, clés et valeurs antérieures maintenues, 13 champs obligatoires de famille présents.
- JSON de la banque et du manifeste parsables, douze IDs `q-001`…`q-012` sans trous ni doublons, clés communes de chaque item, et liens `obj-1`, `crit-1`, `qc-pri-ma-016-ev-01`.
- **30 066 instances testées** (5 011 seeds par chacun des six générateurs) : formules et bornes contrôlées; chaque réponse calculée en centièmes entiers puis contrôlée indépendamment par `decimal.Decimal`, sans flottants ni génération IA comme correcteur. **18 variantes** réexécutées; **22 opérations numériques d'exemple** recalculées. Les contrôles testent les calculs et domaines, pas la pertinence des choix didactiques.
- Couverture textuelle : 2 diagnostics, 3 exercices guidés à indices dégressifs, 4 pratiques autonomes, 2 transferts, deux preuves contextuelles, références aux fichiers locaux, accessibilité et droits documentés.
- Simulation des chemins du workspace source : exactement **2 remplacements et 12 ajouts**. Inspection sur le ZIP réellement écrit : première entrée dans `kristals/qc-pri-ma-016/`, exactement 14 fichiers non vides, manifeste en correspondance, aucun chemin absolu/traversée `../` ou dossier englobant, JSON parsables et CRC ZIP `testzip()` réussi.

## Contrôles de fond, limites et revues humaines

1. **Mathématiques :** les formules, bornes et résultats explicitement testés sont exacts selon les contrôles exécutés. Les contextes, hypothèses de compréhension, progressivité et critères n'ont **pas** été validés par une enseignante ou un enseignant ni par des élèves.
2. **Droits :** aucune ressource externe tierce (image, fichier audio, police, texte cité) n'a été insérée dans le delta; aucune expertise juridique ou revue de licences du workspace entier n'a été réalisée.
3. **Accessibilité :** modalités écrites, orales, tactiles et scribe neutre prévues; contrôles uniquement statiques, aucun audit WCAG d'application, aucun essai utilisateurs, aucun jugement de biais validé sur le terrain.
4. **Liens :** chemins relatifs et IDs contrôlés statiquement; aucune navigation interactive LMS ni vérification de liens distants. La fusion est simulée **par comparaison de chemins**; pas d'extraction en production, pas de `build-v9`, `check-ai` ou qualification Framework.
5. **Décision de maîtrise :** P1 et P2 requièrent chacune R1–R4 « Atteint », deux opérations et deux justifications. L'observateur doit encore vérifier fiabilité, durée, consignes et absence d'indices. Une note unique ne peut pas homologuer l'élève.

## Propositions structurelles, **non appliquées**

- Versionner au niveau central un schéma importeur qui valide `critere_id`, `family_id`, `preuve_maitrise`, les objets `parametres`, les graines et les contrôles indépendants.
- Prévoir dans le LMS une trace d'autonomie (sans données sensibles), deux preuves séparées, leurs rubriques R1–R4, ainsi qu'un statut explicite de revue humaine.
- Examiner avec les responsables pédagogiques l'usage éventuel de décimaux au millième dans une version ultérieure, sans modifier ce Kristal ni le graphe dans cette livraison.

**Fusion :** décompresser le maître puis se placer **dans** `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` avant d'extraire ce ZIP. Tous les chemins débutent par `kristals/qc-pri-ma-016/`. Aucun dossier `Frames_202_.../` supplémentaire n'est livré.
