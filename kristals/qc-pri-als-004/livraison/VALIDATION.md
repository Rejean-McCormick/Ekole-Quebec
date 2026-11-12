# Validation technique et limites — `qc-pri-als-004` v1.2

## Provenance et périmètre
Source lue : archive maîtresse jointe, dossiers de gouvernance v1.2, graphe des relations et quatre fichiers de rédaction natifs. Delta strictement limité aux 14 chemins annoncés par `MANIFEST.json`, au seul identifiant `qc-pri-als-004`.

## Contrôles effectivement réalisés
Les résultats calculés après création des fichiers par le script de validation final sont consignés ci-dessous. Aucun test acoustique sur une voix réelle ni passation enfant n’est revendiqué.

<!-- CHECK_RESULTS_START -->
**41/41 contrôles statiques et de cohérence réussis**, exécutés sur les fichiers construits (parsing YAML via PyYAML, parsing JSON via `json` de Python); ce total **ne mesure pas** la justesse perceptive d’un enregistrement.

- **OK** — 14 fichiers et aucun autre dans le dossier de production.
- **OK** — 14 fichiers non vides.
- **OK** — JSON: banque, contrat et manifeste parsables en JSON strict.
- **OK** — Identité du contrat et de la banque.
- **OK** — Objectif et preuve immuables.
- **OK** — Concepts intacts.
- **OK** — Aucun prérequis ni ordre conseillé dans contrat.
- **OK** — Aucune arête dans le graphe source.
- **OK** — Tous les champs du contrat natif conservés sans altération.
- **OK** — Champs de gouvernance famille complets.
- **OK** — Famille v1.2 d’origine conservée.
- **OK** — Métadonnées YAML natives conservées sauf revision_contenu.
- **OK** — YAML de PARCOURS analysé et état non publié.
- **OK** — Exactement 12 rubriques numérotées.
- **OK** — Objectif et preuve dans parcours.
- **OK** — Famille et critère liés à la banque.
- **OK** — Au moins 8 items et douze ids uniques.
- **OK** — Numérotation q-001 à q-012 sans trou.
- **OK** — Chaque item contient les champs du contrat commun.
- **OK** — Modes et niveaux parmi valeurs autorisées.
- **OK** — Chaque énoncé, réponse, critère et rétroaction est utilisable.
- **OK** — Aucun item déclaré certifié.
- **OK** — 10 items fixes sans paramètres, 2 scénarios contrôlés.
- **OK** — Deux scénarios de maîtrise distincts.
- **OK** — Deux scénarios ont variantes A/B contrôlées.
- **OK** — Critères de grille en quatre dimensions par contexte.
- **OK** — Les tâches 11/12 portent des messages anglais et des réponses cohérentes.
- **OK** — Variantes classe correctes: objets attendus concordants.
- **OK** — Variantes parc correctes: objets attendus concordants.
- **OK** — Plan référence les 12 items et la double preuve.
- **OK** — Grille interdit note unique et exige deux contextes.
- **OK** — Diagnostic >= deux tâches.
- **OK** — Exercices guidés >=3.
- **OK** — Pratiques autonomes >=4.
- **OK** — Notions: 2 exemples et 2 contre-exemples.
- **OK** — Transferts >= 2 et rappel différé.
- **OK** — Liens internes utilisés portent le bon identifiant.
- **OK** — Aucun identifiant d’autre Kristal dans les 14 fichiers.
- **OK** — Sources et statut de droits documentés.
- **OK** — Accessibilité, consentement, voix non diffusée.
- **OK** — Manifeste 14 chemins complets et préfixe.

<!-- CHECK_RESULTS_END -->

## Revues humaines indispensables
1. **Prononciation/anglais oral :** écouter les exemples, distinguer variation régionale et obstacle réel à la compréhension; la banque ne remplace pas des modèles audio validés.
2. **Mesure et fidélité :** faire écouter `q-011` et `q-012` par au moins deux auditeurs à l’aveugle, comparer les deux informations reconstituées et stabiliser la rubrique 0/1/2. Il n’existe ici aucune mesure de fiabilité inter-juges.
3. **Accessibilité :** valider les solutions de captation vocale et les adaptations nécessaires pour élèves en situation de handicap sans déclarer un substitut automatiquement équivalent à un enregistrement oral.
4. **Vie privée :** approuver le dispositif de consentement, la durée de rétention, l’endroit du stockage des voix et les droits d’accès; le ZIP ne contient aucun enregistrement réel.
5. **Droits :** aucune pièce audio ou image externe reproduite; vérifier les éventuels supports ajoutés à l’école et leurs licences, avant diffusion.
6. **Contenu/apprentissage :** revoir les niveaux de difficulté, la compréhension réelle des mots *eraser* et *kite* selon le public et les besoins d’explicitation.

## Limites et décisions explicites
- Sources web publiques consultées comme repères phonétiques et didactiques, mais **aucune validation empirique locale** de la grille ni essai auprès d’élèves; les références sont consignées dans `sources/REFERENCES_CONTENU.md`.
- Barème et seuils = choix internes non homologués; aucun rapprochement détaillé avec le PFEQ, aucun statut « certifié », « validé pédagogiquement » ou « publié ».
- Aucun test d’évaluation automatique sur audio réel; la reconnaissance vocale IA n’est pas un contrôleur de correction.
- Scripts de modelage **textuels seulement** : aucun fichier son original ni commercial n’est distribué.
- Les valeurs d’exécution et le total de tests ci-dessus seront **insérés par le script** après leur exécution : ce texte n’anticipe pas un résultat.

## Propositions de structure (non appliquées)
- Étudier au niveau central un `media_manifest` facultatif pour indiquer source, droits et version du modèle sonore si un audio est ajouté plus tard.
- Étudier une structure de grille d’observation vocale commune avec informations-clés par scénario, contraintes de stockage et procédure d’équivalence accessible.
- Étudier un champ standard de `revue_humaine` (évaluateur, date, variété linguistique évaluée, tests d’écoute aveugle) sans modifier ici les schémas, le graphe ou les métadonnées globales.

**Livraison :** proposition pédagogique instrumentée en attente de revue humaine; aucun fichier central, canonique ou d’un autre Kristal inclus.

## Contrôle additionnel du ZIP réellement exécuté
- **OK** — ZIP exact: 14 entrées fichiers exclusivement.
- **OK** — Première entrée ZIP avec bonne racine.
- **OK** — Aucun chemin absolu, parent ../, dossier enveloppant.
- **OK** — Zéro erreur CRC du ZIP.
- **OK** — Toutes entrées ZIP non vides.
- **OK** — ZIP JSON strict et mêmes octets que les fichiers.
- **OK** — Manifest ZIP déclare toutes entrées exactement.

**Bilan : 48/48 contrôles techniques réussis** ; revue pédagogique humaine toujours requise.
