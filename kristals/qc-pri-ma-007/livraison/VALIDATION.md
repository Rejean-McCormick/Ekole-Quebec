# Rapport de livraison et de validation — qc-pri-ma-007

**Périmètre :** delta de 14 fichiers sous `kristals/qc-pri-ma-007/` destiné à être extrait **dans** `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Archive : `qc-pri-ma-007_livraison_v1.2.zip`. Aucune source centrale ni aucun autre Kristal n'est livré.

## Contrôles effectivement exécutés

La génération locale a exécuté un script Python utilisant la bibliothèque standard pour :

1. **Ouvrir la source v1.2** imbriquée dans l'archive des prompts et lire les quatre fichiers d'authoring, la norme, la charte, le générateur et le graphe; confirmer les relations sortantes `requires` et `recommends_before`.
2. **Comparer le contrat natif** avant/après : tous les champs de premier niveau conservés; tous les champs existants de la famille et de `generation` conservés à l'exception du libellé descriptif de validité du contenu, actualisé sans altérer le schéma; ajout des champs minimaux requis.
3. **Vérifier le YAML de `PARCOURS.md`** : en-tête conservé textuellement, douze sections `## 1.` à `## 12.` présentes dans l'ordre; contenu lié au bon objectif/critère.
4. **Parser les trois JSON** `authoring/CONTRAT_PEDAGOGIQUE.json`, `evaluation/BANQUE_ITEMS.json` et `livraison/MANIFEST.json` et, si le module PyYAML est présent, parser aussi le front matter.
5. **Vérifier la banque** : dix ID séquentiels et uniques, mêmes `obj-1`, `crit-1`, famille, dix énoncés/réponses/rétroactions/critères, statuts tous `a_revoir`, modes autorisés; deux preuves en contextes distincts.
6. **Vérifier les corrigés** : pour dix configurations numériques et les deux scénarios figés, calculer de façon indépendante `a−b=d` puis `b+d=a`; pour les deux items paramétriques, recalculer la seed et les deux sorties LCG; tester en plus **256 seeds d'essai par règle** (512 instanciations) pour domaines et égalités.
7. **Contrôler les renvois relatifs** entre documents livrés et les références à l'ID du Kristal.
8. **Ouvrir le ZIP final** pour contrôler première entrée, chemins autorisés et non absolus, absence de `../`, absence de dossier enveloppant, **exactement 14 fichiers non vides**, manifeste bijectif avec les fichiers et aucune entrée hors périmètre; recalculer les tailles et les parsings à partir du ZIP lui-même.

**Bilan du script :** contrôles automatiques exécutés et réussis. Détails des limites ci-dessous. Les contrôles textuels ne valent pas relecture pédagogique humaine ni homologation de la famille d'items.

## Limites non résolues et revues humaines obligatoires

- **Aucune observation d'élève**, étude d'accessibilité menée avec utilisateurs, essai en classe, étalonnage psychométrique ou validation des traductions LMS réalisés.
- **Aucune revue humaine** des consignes, biais des contextes, pertinence des niveaux de difficulté, rubrique de maîtrise ou sécurité de la génération à l'exécution.
- **Aucune vérification en ligne** des documents EEF, IES/WWC ou CAST : leur référencement est attesté uniquement dans la gouvernance source locale.
- **Droits de redistribution du workspace complet à confirmer** par son titulaire; le delta ne réutilise ni médias externes ni items éditoriaux protégés repérés.
- La validation technique locale ne remplace pas les tests du framework/Kristal, la qualification officielle interne, ni une décision de publication. Aucun item n'est « certifié », « homologué » ou « publié ».

## Propositions de structure à faire approuver (sans modifier les bases centrales)

- Ajouter à l'avenir un champ optionnel `critere_id` au gabarit officiel des items, déjà livré ici comme extension additive, pour des liaisons non ambiguës.
- Standardiser un registre de variantes calculées (`seed`, version de l'algorithme, valeurs, contrôle) et sa validation en CI avant usage LMS.
- Séparer systématiquement **aide de contenu** et **adaptation d'accès** dans la collecte des traces d'autonomie.
- Prévoir une procédure de revue humaine versionnée (contenu mathématique, équité, accessibilité, droits) distincte de la vérification automatique, sans modifier `registry/`, `governance/`, `canon/`, `state/` ou `runtime/` dans cette livraison.

**Statut final :** delta préparé et contrôlé localement; **revue humaine et qualification nécessaires** avant publication.
