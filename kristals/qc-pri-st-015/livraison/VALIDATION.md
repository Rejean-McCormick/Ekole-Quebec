# Rapport de validation — `qc-pri-st-015` (v1.2)

**Livraison :** delta `kristals/qc-pri-st-015/`, 14 fichiers exactement, dont 2 remplacements natifs et 12 nouveaux. **Statut :** contrôlé techniquement, **à revoir humainement** (ni publié, ni homologué, ni certifié).

## Source et respect de la structure

- Source vérifiée : archive jointe `initbundle(1).zip`, racine `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Fichiers lus : norme v1.2, générateur, charte, graphe, les 4 fichiers `authoring/` du Kristal, AGENTS et workspace.
- Front matter YAML du `PARCOURS.md` **strictement préservé** ; objectif, titre, discipline, absence de `requires`, `qc-pri-st-014` recommandé, `qc-pri-ma-031` renforcement confirmés. Tous les champs natifs de `CONTRAT_PEDAGOGIQUE.json` et de sa famille initiale sont préservés, avec compléments de générateur.
- Aucun fichier de gouvernance, de registre, `kristal.workspace.json`, `AGENTS.md`, `ALIGNEMENT.md`, des dossiers `docs/`, `canon/`, `runtime/`, `state/` ou d'un autre ID n'est livré.

## Contrôles réellement exécutés

- **50 assertions préalables concluantes** : lecture des sources, YAML conservé/parsable, 12 sections, notions, 2 diagnostics, 3 guidés à indices dégressifs, 4 activités autonomes, 2 transferts, contenus/corrigés, rubriques, accessibilité, droits, liens, JSON source/cible, identifiants et 12 IDs uniques.
- **12 288 séries générées et contrôlées** par énumération de toutes les graines `0..4095` pour les **3 items paramétriques**. Assertions exécutées sur bornes, unités, sens des évolutions, extrema, pluie non négative, contre-exemples nuages/pluie, calculs visibles et réponses attendues. Deux exemples explicitement recalculés par item. Ces tests n'établissent pas une preuve formelle indépendante de tout défaut de code ou de consigne.
- Contrôle manuel des corrigés fixes : comparaison thermique `10−7=3 °C`, cumul disjoint `1+0+3=4 mm`, preuve de nuages sans pluie, distinction `—` / `0 mm` et impossibilité de sommer des fenêtres chevauchantes.
- **Archivage :** un ZIP de prévalidation a été **réellement assemblé et vérifié** : 14 fichiers non vides, chemins ordonnés conformes, aucune traversée ni chemin absolu, manifeste exact, CRC valide et JSON/YAML parsables. Le contrôle de l’archive finale est ensuite exécuté par le même programme; sa sortie est conservée dans le journal de construction externe.

## Limites non résolues / revue nécessaire

1. Relecture scientifique des formulations sur les phénomènes météorologiques, unités et précautions d'inférence ; l'algorithme décrit des **relevés fictifs**, non des mesures de station officielle.
2. Revue pédagogique et essai avec élèves : pertinence langagière, lisibilité des fenêtres horaires, durée, biais et fonctionnement de la grille; aucune épreuve psychométrique menée.
3. Accessibilité réelle (lecteurs d'écran, braille, supports audio) non testée avec utilisateurs. Les adaptations sont documentées mais non auditées.
4. Les pages ECCC/OMM ont été consultées et leurs faits clés recoupés, mais aucun audit complet de licences n'a été réalisé; **aucune image/extrait tiers** n'est fourni.
5. Aucune conformité détaillée au PFEQ revendiquée, aucun contrôle canon/build-v9 ni publication réseau réalisé. Les 12 items sont **`a_revoir`**.

## Propositions de structure (NON appliquées)

- Ajouter au schéma général des familles des types de fenêtres temporelles (`intervalle_disjoint`, `intervalle_chevauchant`, `donnee_absente`) et un champ de provenance des relevés simulés.
- Ajouter un champ de preuve d'autonomie (aides utilisées, date et contexte) dans le stockage **LMS/évaluation**, hors canon et hors `kristal.workspace.json`.
- Pour une version prochaine, prévoir tests d'accessibilité automatisés sur une projection publiée sans changer les identifiants du graphe.

## Fusion

Décompresser d'abord l'archive maîtresse, entrer dans son dossier racine `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, puis y extraire `qc-pri-st-015_livraison_v1.2.zip`. Ne pas extraire le delta au-dessus de cette racine, sinon le chemin attendu ne se superpose pas.
