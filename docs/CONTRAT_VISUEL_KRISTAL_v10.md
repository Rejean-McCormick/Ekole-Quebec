# Contrat fonctionnel de la couche visuelle conceptuelle

Le Kristal possède la **sémantique pédagogique**. MiniLab possède la **manipulation et la validation**. La couche visuelle possède le **sens de l'image**, pas son style. Ekole possède le rendu et le texte de remplacement. SemantiK peut ultérieurement réaliser les phrases; Konstellation peut naviguer entre les Kristals publiés. Aucun de ces services n'est requis pour afficher un prompt.

## Slot d'exemple : qc-pri-ma-012

Source inchangée : `authoring/CONTRAT_PEDAGOGIQUE.json`, objectif `obj-1` « Représenter une fraction comme partie d'un tout ou d'une collection »; concepts `tout`, `parts égales`, `numérateur`, `dénominateur`.

Le slot `concept` décrit une situation visuelle expliquant le tout et les parts. Le slot `situation` décrit un autre contexte. Le slot `support-outil` donne le contexte du MiniLab de fractions **sans figer** le nombre de parties, les quantités exactes ou la réponse.

## Statuts explicites

- `source`: les notions viennent du contrat Kristal lorsque disponible.
- `statut: proposition_a_valider`: la description du visuel exige une revue humaine.
- `outils_associes`: les associations historiques du MiniLab ne sont pas déclarées approuvées; les autres suggestions ne sont pas des parcours actifs.
- `image_disponible`: seulement quand une image saine est physiquement présente et compilée.
- `prompt_visible`: comportement par défaut.
- `source_absente_a_completer`: source manquante (2 cours), description provisoire issue seulement du catalogue.

## Fichiers de sortie

- Source autoritative : `kristals/<id>/experience/RESSOURCES_VISUELLES.json`.
- Registre public calculé : `site/eleve/data/kristals-visuels.json`.
- Emplacements des médias produits manuellement : `kristals/<id>/experience/images/<slot>.<ext>`.
- Copie destinée au seul affichage : `site/eleve/assets/kristals/<id>/<slot>.<ext>`.

Ne jamais placer les corrigés dans les manifestes publics ou dans les prompts d'image.
