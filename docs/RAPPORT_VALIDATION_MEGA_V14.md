# Contrôles — Ekole v14 (snapshot fourni le 10 octobre 2026)

## Réalisé et vérifié

- Snapshot source : 14 303 entrées ZIP, 202 cours, Core et historique Moodle conservés.
- Reconstruction `tools/ekole.py build` : 202 cours et 20 pages.
- Synchronisation `tools/synchroniser_ekole_apps.py` : 202 références, visuels conceptuels et cinq scénarios v11/7 micro-mondes v12 conservés.
- Compilation v14 : 51 défis sur 14 moteurs, 35 références, 25 cours possédant des outils, 177 cours sans association ; 8/8 cours de mathématique proposés en 3e année pourvus.
- 12 tests v14 Python réussis ; tests JavaScript v14 exécutés sur les 51 défis (réponse juste, état initial, transition pure, erreurs incomplètes).
- Validation des associations du cours, des suggestions d'année et refus des références modifiées.
- Export Élève v14 testable et limité : sans `kristals/`, `enseignant-app/`, `data/cours/`, banques de correction originales.
- API Enseignant : `401` hors session, `200` avec session locale.
- Tests des versions v9, v12 et v13 mis à jour lorsqu'ils imposaient un nombre historique devenu obsolète.

## Limites et anomalies antérieures

- Test Chromium essayé : `net::ERR_BLOCKED_BY_ADMINISTRATOR` sur `127.0.0.1`. Pas de preuve de rendu visuel sur cet environnement.
- Suite héritée : cinq incidents (quatre échecs + une erreur) restent dans les tests `test_architecture_societes_v3`, `test_encyclopedie_autochtones_v4` et `test_propositions_affectations`. Les cinq étaient déjà présents dans le snapshot d'origine; ils ne sont pas réglés par la v14. Réparer le canon historique ou effacer l'affectation manuelle simplement pour faire passer ces contrôles serait incorrect.
- Le contrôle de compilation n'est qu'un contrôle **structurel**. Exactitude des exercices, difficulté par âge, perspectives culturelles, accessibilité réelle et compréhension des élèves exigent des observations humaines.
- Aucune publication Kristal v10 ni homologation Moodle n'est revendiquée.

## Invariants de livraison

Le correctif ne contient aucune version modifiée de : `tools/kristal_moodle_bridge.py`, `opsconsole/`, `site/app.js`, `kristals/*/canon/`, `site/data/index.json`, `site/data/parcours-affectations.json`, ou des modules de contenu/corrigés. Le Kristal encyclopédique reste indépendant.
