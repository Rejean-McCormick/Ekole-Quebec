# Journal de validation — `qc-pri-ilss-002` v1.2

**Date des contrôles :** 2026-10-09.  
**Base :** frame pédagogique v1.2 retrouvé dans l'archive de conversation `Spec_Kristals_Parcours_Primaire_Qc_v1.1(1).zip` sous le répertoire maître `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`.  
**Statut :** `controles_techniques_reussis_revue_pedagogique_humaine_requise`. Aucun item n'est publié, homologué ou certifié.

## Périmètre livré

- **Deux remplacements locaux :** `authoring/PARCOURS.md` (frontmatter YAML préservé à l'identique, douze sections complétées) et `authoring/CONTRAT_PEDAGOGIQUE.json` (tous les champs et valeurs v1.2 préservés, champs de famille ajoutés).
- **Douze nouveaux fichiers :** six documents `contenu/`, trois `evaluation/`, une bibliographie, ce journal et un manifeste. **Total : 14 fichiers**, tous sous `kristals/qc-pri-ilss-002/`.
- **Hors périmètre et non modifiés :** `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, `AGENTS.md`, `kristal.workspace.json`, `docs/`, `canon/`, `state/`, `runtime/`, `registry/`, `governance/`, les autres ID.

## Contrôles réellement exécutés par script local

1. **Intégrité des bases :** YAML comparé exactement au fichier source; douze en-têtes de sections consécutifs; tous les champs et valeurs du contrat d'origine comparés récursivement et conservés; id, titre, objectif, preuve, famille et discipline vérifiés.
2. **Graphe :** JSON du registre parsé; seules arêtes sortantes retrouvées pour cet ID : `requires(qc-pri-ilss-002,qc-pri-ilss-001)` et `recommends_before(qc-pri-ilss-002,qc-pri-ilss-003)`; la recommandation n'est pas transformée en verrou.
3. **Banque :** JSON strict parsé; **10 items** `q-001` à `q-010` numérotés sans trou ni doublon; champs obligatoires présents et renseignés, modes, difficultés, statuts `a_revoir`, corpus fixe et non-paramétrique vérifiés; deux scénarios de maîtrise distincts `q-009` et `q-010`.
4. **Réponses et critères :** confrontation automatisée des dix informations attendues avec les stimuli et les exemples de réponses; correspondance de chaque item dans le plan; rubriques I/D/R/T présentes, conclusion multi-tours explicite. **Limite :** ce contrôle teste la cohérence textuelle ciblée, pas l'adéquation complète des jugements humains.
5. **Couverture pédagogique :** présence de trois notions, deux exemples résolus et deux contre-exemples, deux diagnostics, trois exercices guidés, quatre pratiques autonomes et deux transferts. Adaptations et absence de captation obligatoire vérifiées par inspection de mentions explicites.
6. **Droits et sécurité :** fichiers exclusivement textuels et scénarios fictifs originaux; contrôle documentaire de l'absence de matériel tiers importé et présence des limites de licence, de confidentialité et d'accessibilité. Aucun audit juridique ou accessibilité avec des personnes n'a été mené.
7. **Empaquetage :** exactement 14 chemins du manifeste, chacun existant et non vide; archive commençant par `kristals/qc-pri-ilss-002/`; aucun fichier extérieur, traversée `../`, chemin absolu ou dossier maître imbriqué; JSON de sortie parsés; test CRC de l'archive effectué; ordre et fichier de validation concordants.

## Limites non résolues et revue humaine nécessaire

- Relecture par personnel ILSS (niveau de langue, authenticité des situations, cohérence pour divers âges du primaire, validité du seuil local de trois tours et de la grille 0–3).
- Essai en classe sur dyades et différentes modalités (pictogrammes, communication augmentée, plurilinguisme) : vérifier charge cognitive, compréhension des fiches, neutralité culturelle, temps et accord entre observateurs.
- Revue des droits de tout **futur** support tiers ajouté (aucun multimédia tiers n'est livré). Respect des pratiques de protection des données et consentements locaux en LMS.
- Aucune qualification psychométrique, homologation québécoise, preuve d'efficacité sur des élèves, tests Moodle ni validation par le framework Local Kristal v9 n'ont été effectués. Le caractère exploitable d'une grille n'implique pas un examen certifié.

## Propositions éventuelles (non appliquées au workspace central)

- Proposer au registre central un champ optionnel `aides_accessibilite_autorisees` et une trace des `indices_de_contenu` durant une passation, pour séparer accessibilité et guidage.
- Proposer une structure de `preuves_distinctes` identifiant contexte/partenaire et la règle de deux manifestations; n'ajouter le champ central qu'après gouvernance versionnée.
- Proposer une revue standardisée du statut `a_revoir` et d'un protocole d'archivage de traces minimisées dans le LMS.
