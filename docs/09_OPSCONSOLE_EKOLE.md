# 09 — OpsConsole Ekole et frontières UCKK

## Rôle

OpsConsole est une **surface de contrôle opérationnelle** locale du repo `Ekole`. Elle lit le registre des 202 Kristals, le graphe de 252 relations, le Kristal-Portail candidat et le site statique. Elle ne possède pas les connaissances pédagogiques et ne crée pas d'engagement Kristal v9/v10.

## Architecture

```text
scripts/START_EKOLE_OPSCONSOLE.bat
                ↓
opsconsole/ekole_ops.py (HTTP local 127.0.0.1:8766)
   ├─ lecture catalogue / graphe / inspection Kristals
   ├─ exécution autorisée tools/ekole.py verify | build | moodle-plan | pages-zip
   ├─ prévisualisation site/ (127.0.0.1:8765)
   ├─ Git local (lecture seule)
   └─ copie statique locale : simulation → contrôle → confirmation → sauvegardes

Moodle, GitHub, SemantiK, Konstellation et Médiathèque
   └─ états affichés seulement (pas d'écriture ni d'appel réseau)
```

## Règles du snapshot UCKK Ops Console

- « Le rapport explique. Le log diagnostique. L'interface résume. »
- Source locale → inspection/validation → prévisualisation → simulation → copie locale contrôlée.
- Des actions irréversibles, serveur ou base de données ne sont **pas disponibles** dans cette version.
- Pas de SQL direct, wipe, anciens scripts recovery/legacy, dump, tokens distants.
- Ne pas reprendre le runtime OpsConsole UCKK ni l'installer dans `uckk-moodle` : Ekole possède son périmètre.

## Répertoires

Le dépôt reste responsable des sources : `kristals/`, `catalogue/`, `organisation/`, `site/`, `tools/`. OpsConsole ajoute seulement `opsconsole/`, `docs/09_OPSCONSOLE_EKOLE.md` et les scripts de lancement. Les opérations créent leurs sorties dans les répertoires déjà prévus `site/data/`, `plans/` ou `dist/` et les journaux sous `opsconsole/logs/` (ignorés par Git).

## Politique de livraison

Cet overlay ne modifie pas le Kristal-Portail, les 202 cours, les contrats du Framework, les ports v10 ni les scripts `tools/ekole.py`. Tous les ponts d'écosystème non intégrés demeurent explicitement marqués non opérationnels.
