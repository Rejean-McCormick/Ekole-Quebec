# Validation de la livraison — `qc-pri-ma-027`

**Nature de la livraison :** delta v1.2 pour un seul Kristal, 14 fichiers sous `kristals/qc-pri-ma-027/`, dont 2 remplacements `authoring/` et 12 ajouts. Ni PFEQ ni certification, homologation ou publication revendiqués.

## Contrôles réellement exécutés

**622 assertions préarchivage exécutées et réussies**, portant sur les 14 chemins, le frontmatter YAML (clés et invariants), les 12 sections, la préservation du contrat et des deux préalables, les liens de famille, la banque stricte de 10 items sans doublons, les deux preuves autonomes, les critères et les sources. **21 variantes paramétriques** recalculées par la somme des longueurs des côtés d’un polygone en coordonnées (calcul indépendant des formules génératrices) et confrontées aux solutions conservées dans le catalogue; aucun désaccord arithmétique. Toutes les sélections `seed % 3` reproduites et comparées aux énoncés et corrigés publiés dans les items. **Aucun essai avec élèves, revue humaine, certification ou validation de sécurité physique effectué.**

**Après création de l’archive :** test de 14 entrées, des chemins, du manifeste, du décodage JSON/YAML et contrôle CRC `testzip()`; comparaison des fichiers ZIP avec leurs sources de construction. Une simulation de fusion depuis l’archive maîtresse originale vérifie que seulement 2 fichiers existants sont remplacés et 12 ajoutés, et qu’aucun autre fichier n’est altéré.

## Points non résolus, requérant revue humaine

- Clarté et pertinence des figures en L et des supports selon l'âge et le contexte réel d'enseignement; tests pédagogiques non effectués.
- Recevabilité des aides de lecture, schémas en relief et moyens alternatifs lors d'une preuve autonome; vérifier l'équité de la procédure avant emploi.
- Validité de l'échelle de quatre dimensions, des seuils et de la distinction entre deux preuves; aucun étalonnage humain ni fiabilité intercorrecteurs.
- Relecture des formulations en français québécois, contrôle des droits du matériel supplémentaire qui pourrait être joint ultérieurement.
- Les références externes sont utilisées pour l'éclairage conceptuel et l'accessibilité, non comme preuve de conformité PFEQ.

## Propositions de structure sans modification centrale

1. Créer ultérieurement, par validation du propriétaire de la gouvernance, un schéma standard de `parametres.variantes` avec solveur indépendant et empreinte des catalogues.
2. Normaliser l'association explicite `obj-1`/`crit-1`/famille dans toutes les banques v1.2 et les décisions de maîtrise multi-contextes.
3. Ajouter, après décision centralisée, une convention de consignation des accommodements d'accès pour éviter leur confusion avec des indices directifs.

Aucun fichier `registry/`, `governance/`, `canon/`, `docs/`, `state/`, `runtime/` ou autre Kristal n'est présent dans le ZIP.
