# Déploiement — local, GitHub et Moodle

## Prévisualisation locale

`py -3 tools\ekole.py verify`, puis `build`, puis `preview`. Le site statique est servi à `127.0.0.1:8765`; il ne publie aucune donnée vers le réseau.

## Déploiement statique local (copie contrôlée)

`py -3 tools\ekole.py deploy --target C:\chemin\vers\site` produit un plan de différences sans modifier la cible. Utiliser `--apply` après validation; seul `site/` est copié, sans suppression des fichiers déjà présents. Refus d’une cible interne à `Ekole/` et d’un emplacement sans consentement. Contrôler la cible et les sauvegardes avant tout déploiement réel.

## GitHub — intégration Kristal v10

Ne pas créer de `Publication Record` sans `state_ref`, engagement d’État v9 et octets exacts qualifiés. Les exemples des schémas/framework v10 sont sous `vendor/reference-only/kristal-framework-v10-source.zip`. La projection `site/` peut être publiée comme **site de démonstration**, indépendamment de la publication sémantique. GitHub Pages et le catalogue réseau v10 exigent leur propre configuration et revue. Aucun dépôt, token, URL de publication, branche ou workflow auto-activé n'est inclus.

## Moodle UCKK

Le dépôt original attend son propre workflow : source locale → Moodle local → Git → source serveur → Moodle serveur. Ekole ne le remplace pas. `python tools/ekole.py moodle-plan` écrit un plan JSON de catégories/cours/sections et les états de revue des évaluations, mais **n'écrit pas** en base et ne lance pas `local_uckk`. Établir des mappings explicites `Ekole ID → Moodle courseid/categoryid` dans une configuration séparée avant un adaptateur réel.

## Ops Console

Le snapshot original comporte des paramètres orientés vers une autre machine; ne pas importer sa configuration dans Ekole ni lancer ses scripts à distance. Garder ses actions sensibles derrière leurs confirmations et simulations natives. Consultez le snapshot en lecture seule, puis adaptez **une configuration locale** sous le contrôle de l’opérateur.

## Export GitHub Pages (uniquement projection du site)

La page est désormais compatible avec une base de chemin dans un sous-dossier (`./?page=...`, `./?cours=...`). Le dossier `site/` est l’unique artefact statique à publier. Éviter toute copie de `kristals/`, `vendor/`, `plans/` et `references/` dans un site public.

Pour fabriquer une archive de site statique (sans publication distante) :

```powershell
py -3 tools\ekole.py pages-zip
```

Ce ZIP de sortie `dist/ekole-site-preview.zip` contient uniquement la projection statique. Il ne constitue pas une publication Kristal v10 et ne révoque pas les revues pédagogiques nécessaires.
