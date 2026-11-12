# 12 — Compatibilité avec Framework / Authoring Kit / UCKK / Moodle

## 12.1 Architecture de transport et d'exécution

```text
ScolQc + preuves officielles
          |
          v
sources Markdown de microparcours + registre + assemblages
          |
          v compilation/normalisation de domaine À IMPLÉMENTER
artefacts logiques Kristal v9 + states/commitments conformes
          |
          +-- qualification, publish, activation (séparés)
          +-- projection de contenu pour agents/tuteurs
          +-- plans d'épreuve / banques et grilles
                              |
                              v
                       adaptateur Moodle
```

Le fichier `PARCOURS.md` n'est **pas** directement un `Logical Artifact` conforme; son transformateur doit être versionné, audité et validé contre les schémas officiels `schemas/v9/` du Framework. Il conserve l'identité métier tout en produisant identité technique, provenance et engagements logiques exacts.

## 12.2 Responsabilités des outils existants

- **Kristal Framework v9** : contrat normatif des artefacts logiques, state snapshots, engagements, dérivations et matérialisations.
- **Authoring Kit** : authoring local, découverte de forme, validation, `check`, `build-v9`; multi-workspaces dans une collection commune.
- **UCKK-v9** : illustration de parents référant aux états enfants épinglés sans copie; **non** une ontologie scolaire.
- **V10 Hosted Network** : liens vers nœuds/hébergements et publication; indépendant de la sémantique v9.
- **Moodle** : activités, présentation, banques, suivi, soumissions; **pas de vérité canonique sur le contenu**.

## 12.3 Format des projections Moodle

Chaque export porte un manifest de liaison avec : `export_id`, `source_state_commitments`, `assembly_id`, `edition_curriculaire`, `adapter_version`, `generated_at`, `items_or_activities`, `evaluation_plan_ref`, `content_licences`, `known_losses`.

- Cours/sections : dérivés de l'ordre et des conditions de l'assemblage.
- Ressources : dérivées des sections d'enseignement et des médias autorisés.
- Exercices : activités ou banque de questions, selon support.
- Tests : compilés d'un plan d'épreuve validé; conserver traces et grilles.
- Observations/performance : activité de devoir, grille ou modalité pertinente, **pas nécessairement quiz**.
- Résultats des apprenants : conservés dans le LMS / le système autorisé, jamais réécrits dans les feuilles canoniques.

## 12.4 Limites

Ne pas promettre un export `Moodle XML` pour une activité qui n'est pas représentable sous forme de question. La correspondance des rubriques, questions calculées, banque aléatoire, H5P ou autres modules doit être testée sur une instance Moodle et selon la version/plugins disponibles. Une conversion avec perte DOIT documenter `known_losses` et être refusée pour une évaluation si elle modifie l'objet évalué.

## 12.5 Tests d'intégration minimaux

1. Un seul Kristal-feuille (contenu + pratique) → reconstruction fidèle dans l'activité cible.
2. Assemblage de deux feuilles avec `requires` → ordre et préalables conservés.
3. Deux variantes d'un item paramétrique → solutions, réponses, corrections reproductibles.
4. Une tâche ouverte/production → rubrique et correction humaine opérationnelles.
5. Changement de revision d'une feuille → export incrémental traçable; aucun écrasement silencieux des notes élèves.
