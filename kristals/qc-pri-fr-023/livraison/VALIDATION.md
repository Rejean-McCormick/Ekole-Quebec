# Validation de la livraison — qc-pri-fr-023

**Version source :** workspace v1.2 inclus dans le ZIP fourni de prompts. **Statut :** contenu et items à revoir humainement, **non qualifiés**; le delta n'est ni publié ni certifié.

## Périmètre du delta

Deux fichiers existants remplacés sans perte de leur forme native : `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`. Douze fichiers nouveaux couvrent six ressources de contenu, trois pièces d'évaluation, une référence et deux pièces de livraison. Aucun dossier `registry/`, `governance/`, `canon/`, `docs/`, `runtime/`, `state/` ni autre Kristal n'est modifié par cette archive.

## Contrôles exécutés

- **Inventaire ZIP et manifeste :** contrôle automatisé sur l'archive finale, liste exacte de quatorze fichiers, tous non vides, chemin préfixé par `kristals/qc-pri-fr-023/`, premier chemin conforme, aucune traversée `../`, aucun chemin absolu ou dossier englobant.
- **JSON :** lecture effective des trois JSON livrés (`CONTRAT_PEDAGOGIQUE.json`, `BANQUE_ITEMS.json`, `MANIFEST.json`) et vérification des champs et identifiants attendus.
- **Préservation v1.2 :** comparaison des clés initiales du contrat et des champs d'identité, objectifs, préalables, ordre et familles avec le JSON original; comparaison du YAML d'en-tête du parcours avec l'original et maintien des douze titres de section.
- **Graphe :** correspondance des trois arêtes de référence du graphe fourni (`requires` vers 021; `recommends_before` vers 012 et 019), sans dépendance inventée.
- **Banque :** huit IDs `q-001` à `q-008` sans doublon, chacun avec stimulus, consigne, correction commentée, cinq critères, feedback et `validation_status: a_revoir`.
- **Preuves :** `q-006` (collecte et note aux familles) et `q-008` (consignes de jardin) ont des genres et faits distincts; les deux tâches sont reliées à `obj-1`/`crit-1`/famille `ev-01`.
- **Cohérence des corrigés :** relecture éditoriale des huit fiches et solutions de référence; assertions automatiques explicites sur les repères factuels de `q-006` et `q-008`. Les paraphrases ouvertes ne peuvent pas être contrôlées automatiquement de manière fiable.
- **Droits et sécurité :** aucun extrait de tiers n'a été intentionnellement intégré aux tâches; situations inventées sans données personnelles. Vérification documentaire de la rubrique de provenance et des limitations de droits, sans audit juridique externe.
- **Accessibilité documentaire :** consignes présentes en texte, codes S/T/L utilisables sans couleur; lecture orale d'accès et saisie alternative prévues. Aucun test d'interface ni d'appareil d'assistance effectué.
- **Liens :** références aux nouveaux fichiers locaux présentes, chemins relatifs contrôlés; les références centrales désignent les fichiers réellement lus et n'ont pas été incorporées au ZIP.

Les contrôles ci-dessus décrivent des opérations faites lors de l'assemblage; voir également le résultat final synthétique ci-dessous.

## Résultat final des tests techniques

**Résultat : 39 contrôles automatisés réussis sur le delta et l’archive ZIP**. Détails principaux : 14/14 fichiers manifestés, non vides et au bon préfixe; 3/3 JSON parsables dans l’archive; YAML initial préservé; 12/12 sections; 8/8 items complets et uniques; 2/2 contextes de preuve identifiés; liens relatifs sans cible manquante; aucun chemin dangereux; test d’intégrité CRC sans erreur. Les vérifications sémantiques automatisées portent seulement sur des repères factuels explicitement codés pour les deux preuves terminales; elles ne valident pas l’ensemble des reformulations possibles ni les décisions de maîtrise d’un élève. Aucun essai avec un élève ni test de l’interface finale n’a été exécuté.

## Limites et revue humaine obligatoire

1. Révision par une personne compétente du français écrit québécois : niveau de formulation, acceptabilité des réponses équivalentes, ambiguïtés potentielles et feedback.
2. Essais sur des productions réelles : durée, stabilité de la grille, adéquation des items aux besoins des apprenants; aucune donnée d'essai collectée ici.
3. Accessibilité numérique en situation (lecteur d'écran, capture des annotations, contraste, dictée et autocorrection, navigation au clavier); aucun logiciel final fourni.
4. Vérification juridique de l'usage et de la redistribution des fichiers du workspace source; les textes originaux ici ne transfèrent pas automatiquement les droits du projet.
5. Les huit items et leurs reformulations possibles sont `a_revoir`; aucune validation psychométrique, publication ou conformité PFEQ n'est affirmée.

## Propositions de structure (non appliquées aux bases centrales)

- Ajouter, dans une version centrale future, un champ formel `preuves_maitrise` liant deux contextes distincts aux IDs d'items, et un journal d'aides par passation.
- Envisager un champ `variantes_acceptees` avec revue humaine datée et version de grille, plutôt qu'un correcteur IA ouvert.
- Ajouter au validateur central un contrôle automatisé des préfixes ZIP et de la non-régression des champs natifs.

**Aucun changement de `registry/`, `governance/`, `kristal.workspace.json`, `AGENTS.md`, `authoring/ALIGNEMENT.md` ou d'un autre Kristal n'a été empaqueté.**
