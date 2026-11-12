# Validation de livraison — `qc-pri-us-003`

**Workspace maître source :** `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` extrait de l'archive conversationnelle `initbundle(1).zip` ; seule cette archive a fourni les métadonnées. **Cible :** delta de 14 fichiers sous `kristals/qc-pri-us-003/`.

## Contrôles effectivement exécutés (préarchivage)

- Script Python `build.py` : **130 assertions préarchivage réussies**, dont contrôle caractère pour caractère du front matter YAML, chargement YAML, JSON strict, préservation des clés d'origine, objectif/preuve/famille, graphe (`requires=[]`, ordre recommandé), séquence des 12 sections, numéros uniques 001–010, champs/rubriques complets, 2 situations distinctes de maîtrise et limite de variation.
- Inspection textuelle des corrigés et des fiches fictives incluses, avec contrôle automatisé des coordonnées/chaînes-clés pour les deux preuves. **Ce contrôle n'est pas une validation exhaustive par un expert** de tous les corrigés.
- Intégrité ZIP, racine et ordre des entrées, 14 fichiers non vides, absence de traversée de chemin, lecture des JSON depuis le ZIP, CRC, manifeste et comparaison des octets : contrôles exécutés à la fin du script.
- Simulation d'une extraction dans le dossier maître : 2 fichiers `authoring/` remplacés et 12 fichiers nouveaux; aucun fichier protégé présent dans le delta. Ces assertions sont vérifiées après la construction de l'archive et le script échoue si elles échouent.

## Provenance et limites

- Les fiches et cartes sont des créations originales fictives, datées *éditorialement* du 8 octobre 2026; nulle observation réelle ou donnée climatologique locale n'est revendiquée. Sources réelles vérifiées sur le Web pour le climat, le relief et les pratiques de carte, détaillées dans `sources/REFERENCES_CONTENU.md`. Aucun support cartographique tiers copié, aucune licence externe revendiquée.
- Non effectués : essai en classe, validation scientifique/pédagogique humaine, vérification de lisibilité sur tous appareils/assistances techniques, homologation institutionnelle, tests de plateforme LMS ou du Framework canonique.
- Tous les items sont `validation_status=a_revoir`; ce livrable constitue un **contenu rédigé à qualifier**, pas un Kristal publié ou canonique.
- Vérifier humainement notamment la signification de « ressource » et « occupation » en contexte, les éventuels biais de territorialité, la compréhension des grilles, les seuils des rubriques et l'adéquation au public visé.

## Propositions de structure (NON exécutées)

1. Prévoir en central, dans une future version validée, des champs explicites `preuves_independantes` et `modalite_accessibilite` dans le schéma d'évaluation, plutôt que les transporter comme extensions locales.
2. Prévoir un catalogue signé/versionné des fiches fictives (coordonnées, autorité, contexte temporel) et un outil de contrôle par tableau de correspondances pour la localisation.
3. Clarifier centralement le statut de validation humaine des cartes tactiles et des rendus transcrits. **Aucune modification centrale n'est livrée dans ce delta.**
