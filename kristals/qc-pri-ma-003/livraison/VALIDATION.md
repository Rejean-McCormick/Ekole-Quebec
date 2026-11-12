# Validation de livraison — qc-pri-ma-003

**Portée :** delta de 14 fichiers fusionnables, archive maître v1.2 imbriquée dans le ZIP de prompts; ni workspace complet ni publication. **Statut :** contrôles locaux exécutés, revue humaine et test Framework non effectués.

## Contrôles réellement exécutés

La fabrication effectue une vérification indépendante des valeurs de départ, seconde décomposition et regroupement inverse de chaque corrigé modèle; elle énumère également les 3 seeds d'exemples par item paramétrique. Un script distinct de validation est exécuté après création du ZIP pour vérifier format, chemins, JSON/YAML, liens, compatibilité et mathématique. Les résultats détaillés sont inscrits ci-dessous **uniquement après exécution**.

| Contrôle réalisé | Résultat observé |
|---|---|
| Identité et sources v1.2 | Archive mère retrouvée au chemin interne `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`; contrats et fichiers originaux ouverts; graphe relu : seule relation sortante `requires` vers `qc-pri-ma-002`. |
| Fichiers livrés | 14/14 chemins prescrits, tous non vides; aucun fichier des bases communes. |
| YAML de `PARCOURS.md` | Frontmatter comparé **à l'identique** avec la source; analysé avec PyYAML; 12 sections numérotées présentes. |
| Contrat de famille | Champs natifs conservés, sauf statuts éditoriaux révisés sans changer le schéma; 13 champs de la gouvernance présents et renseignés. |
| Banque et JSON strict | 10 items distincts, IDs consécutifs `q-001` à `q-010`; 5 fixes, 3 paramétriques, 2 scénarios contrôlés; toutes les ressources `.json` analysées et contrôlées contre les clés JSON dupliquées. |
| Corrigés arithmétiques | 10/10 réponses modèles recalculées : même valeur de deux décompositions, échange valide, inverse exact et retour aux trois groupes de départ. |
| Génération reproductible | **30 000** cas d'essai (`seed` 0 à 9 999 pour chacun des trois générateurs) contrôlés par évaluation numérique indépendante; **9** exemples de seeds dans la banque recomputés et comparés. |
| Deux contextes de maîtrise | Présence contrôlée de `q-007` bibliothèque (C↔D) et `q-008` mosaïque (D↔U), avec réponses, critères, absence d'indice mathématique demandé dans la passation. |
| Seuils et contenus minimaux | 2 diagnostics, 3 pratiques guidées, 4 autonomes, 2 transferts et 2 contre-exemples repérés; 12 liens Markdown locaux résolus. |
| Accessibilité et droits | **Contrôle documentaire seulement** : modalités accessibles, sécurité du matériel, absence de médias tiers et réserves de droits explicités; **aucun test utilisateur ni audit juridique** effectué. |

La vérification de la **structure ZIP finale** est effectuée séparément après empaquetage : noms des 14 entrées, premier chemin, chemins relatifs, contenu non vide, JSON et concordance avec le manifeste. La production finale est contrôlée à nouveau après insertion de cette validation.


## Limites non résolues, revue humaine requise

- **Pédagogie :** âge de vocabulaire et charge cognitive des situations; pilotage sur élèves réels et observations d'accès; juger la pertinence du seuil de quatre critères à 2/2 sur les deux occasions.
- **Psychométrie :** M1/M2 ne sont pas étalonnés; compléter par essais indépendants et vérification de l'équité. Les contextes fictifs ne garantissent pas le transfert observé.
- **Technologie :** aucune intégration Moodle/Framework, aucune qualification du solveur dans un runtime de production, aucune publication ou activation.
- **Sources/droits :** calculs originaux contrôlés localement; aucune validation externe des sites EEF/IES/CAST et aucune licence de l'archive source attestée.
- **Accès :** modalités textuelles prévues, mais aucune vérification réelle avec lecteurs d'écran ou matériel tactile n'a été conduite.
- **Statuts natifs :** en-tête YAML (`revision_contenu: 0.2.0`, `statut: en_rédaction`) préservés; les champs JSON natifs de statut ont été mis à jour en `contenu_en_revision_items_a_revoir` et `banque_items_a_revoir` pour ne pas annoncer des items encore manquants. Chaque item demeure `a_revoir`; aucune publication ou certification ne découle de ce changement.

## Propositions de structure **non appliquées**

1. Exposer dans le registre, lors d'une future révision approuvée, un champ facultatif « diagnostic_equivalence_prerequis » attaché à l'arête `requires`, sans modifier le graphe actuel.
2. Définir un validateur central des champs de famille et des paramètres de seed (schéma JSON) et une politique de version de `revision_contenu`, plutôt que changer de façon isolée le format natif.
3. Ajouter au moteur LMS un journal séparé par apprenant documentant aides d'accessibilité versus indices de mathématique et les deux occasions de maîtrise, sans rien pousser dans `canon/`, `state/` ou `registry/`.

## Instructions de fusion

Ouvrir l'archive maîtresse `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` à sa racine puis y extraire `qc-pri-ma-003_livraison_v1.2.zip` **sans** créer de dossier enveloppant. Les entrées commencent exactement par `kristals/qc-pri-ma-003/`; seules les deux ressources `authoring/` présentes sont écrasées; les 12 autres ressources sont ajoutées.
