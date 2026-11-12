# Validation de livraison — `qc-pri-fr-011` (delta v1.2)

**État :** tests techniques locaux réussis, **relecture humaine et essai pédagogique non effectués**. Ce delta n'est ni certifié, ni homologué, ni publié, ni un artefact canonique v9.

## Source et périmètre

Source inspectée : archive `initbundle(1).zip`, sous la racine originale `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Contrat v1.2, générateur/examens, charte de conversion, graphe et fichiers locaux d'origine consultés. Aucune dépendance inter-Kristals n'est déclarée ou créée pour `qc-pri-fr-011`. Révisions limitées aux deux fichiers existants `authoring/` et aux douze fichiers nouveaux du filetree autorisé.

## Contrôles réellement exécutés

- **Contrôles de préarchivage exécutés :** 31 assertions Python réussies : inventaire, chemins, manifeste, identifiants, conservation des champs v1.2, analyse du front-matter YAML, douze sections substantielles, JSON parseables, dix ID d'items sans doublon, couverture des trois niveaux, 4 observables par item, deux preuves A/B, indices présents textuellement dans les stimuli et leurs corrigés, mode fixe et absence de seed/paramètres, absence de préalables, validité des liens Markdown, absence de placeholders.
- **Vérification des corrigés automatisable :** les indices cités dans le corrigé existent dans **le bon** stimulus A ou B; chaque item possède deux définitions différentes, une réponse rédigée, un exemple de réemploi, un retour spécifique et des limites de variation. **Cela ne prouve pas** l'exhaustivité lexicographique de chaque réponse ni l'équité des formulations.
- **Revue éditoriale lors de la rédaction :** examen raisonné des paires mot/sens, contre-exemples, formulation de réemploi et correspondances entre le cours, les pratiques, les transferts et le plan d'évaluation. Il ne s'agit pas d'une revue indépendante.
- **Postarchivage :** vérification ZIP des 14 fichiers exacts non vides, aucun chemin absolu/traversal, premier chemin au bon préfixe, aucun fichier étranger, manifeste congruent, intégrité CRC, et simulation locale de fusion par superposition sur la version source : résultat ajouté en fin de journal à partir des assertions réellement réussies.

## Limites et points de revue humaine

1. **Linguistique :** vérifier tous les sens et paraphrases acceptables en français québécois, les indices non équivoques, l'intensité des mots et la classe grammaticale pour les synonymes. Les alternatives d'élèves ne peuvent pas être toutes anticipées par un corrigé fixe.
2. **Évaluation :** essais avec apprenants, durées, difficulté réelle, concordance entre correcteurs, absence d'exposition préalable des preuves A/B, validité de deux observations séparées et pertinence du seuil de maîtrise.
3. **Accessibilité/équité :** vérifier en contexte réel le fonctionnement des présentations audio, la neutralité du scripteur, la lisibilité et la diversité des usages linguistiques. Les options proposées n'ont pas été testées avec des participants.
4. **Sources/droits :** documents et pages web identifiés dans `sources/REFERENCES_CONTENU.md`; matériel rédigé original; examen juridique des droits et de la licence de diffusion restant à faire.
5. **Technique aval :** ni `python tools/kristal.py check`, ni `build-v9`, ni `check-ai`, ni qualification de publication réseau exécutés : ce ZIP ne modifie pas le canon et aucune simulation ne prouve la conformité d'un environnement de publication.
6. **Contrôle des variations :** seul le mode fixe est utilisé. Aucune génération IA libre ni variation paramétrique n'a été testée ou annoncée comme fiable.

## Propositions non appliquées (nécessitent gouvernance centrale)

- Éventuellement ajouter un champ stable `critere_id` au contrat d'évaluation natif si un schéma commun l'autorise; le présent delta utilise le champ `critere` requis par la norme et ne modifie pas les registres.
- Prévoir un emplacement contrôlé pour consigner les deux dates, aides et productions des preuves dans la **couche LMS/suivi**, sans injection dans `canon/` ou `state/`.
- Après validation humaine, considérer un corpus fermé de variantes révisées pour les preuves, sans modification implicite de l'objectif, du graphe ou de la famille.

## Résultats postarchivage exécutés (2026-10-08)

- **ZIP :** exactement 14 entrées et 14 fichiers non vides, chemin initial `kristals/qc-pri-fr-011/authoring/PARCOURS.md`, aucun dossier englobant, aucune entrée hors `kristals/qc-pri-fr-011/`, aucun chemin absolu ni remontée `../`. Contrôle CRC (`ZipFile.testzip`) : réussi.
- **JSON embarqués :** `authoring/CONTRAT_PEDAGOGIQUE.json`, `evaluation/BANQUE_ITEMS.json` et `livraison/MANIFEST.json` parseables; manifeste égal à la liste réelle ordonnée.
- **Fusion simulée :** extraction sur le sous-arbre existant tiré de l’archive source; les 14 fichiers du delta se superposent, tandis que `AGENTS.md`, `kristal.workspace.json`, `authoring/ALIGNEMENT.md` et `authoring/BRIEF_REDACTION.md` demeurent identiques à la source (comparaison des octets). Pas de test d'intégration du workspace complet ni d'activation.

**Verdict local :** 31 contrôles préarchivage + contrôles d’intégrité ZIP, contenu JSON et fusion simulée réussis; **revue humaine toujours requise**.
