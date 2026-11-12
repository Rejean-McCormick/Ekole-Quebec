# Validation — `qc-pri-st-019` v1.2

**Exécution technique :** 8 octobre 2026, script de validation local. **Statut :** contrôles techniques réussis, révision scientifique et pédagogique humaine requise; aucun item homologué/certifié.

## Contrôles réellement effectués

- **501 assertions préarchivage réussies** : arbres, contenu présent, frontmatter YAML, contrats JSON, identifiants, préalables du graphe, conservation des clés et valeurs canoniques, 12 sections, 10 items séquentiels, rubriques et sécurité/accessibilité en texte, deux contextes autonomes, liens de manifeste et plan.
- YAML du parcours parsé; champs invariants égaux à ceux du maître, sans suppression de clé; modifications limitées au statut éditorial, à la révision et à la provenance.
- **Trois JSON stricts** décodés : `authoring/CONTRAT_PEDAGOGIQUE.json`, `evaluation/BANQUE_ITEMS.json`, `livraison/MANIFEST.json`; tous les 10 items en statut `a_revoir`.
- Graphique v1.2 lu : **seul** préalable sortant `requires` = `qc-pri-st-017`; lien entrant `qc-pri-st-020` non transformé en dépendance.
- Les solutions factuelles des cycles papillon et pissenlit ont été confrontées manuellement à des sources externes identifiées; tests automatisés ont vérifié la présence des étapes et liens mais **ne sont pas une validation scientifique exhaustive**.
- Les textes citent les pages Smithsonian et Kew effectivement consultées; aucun média, photo ou musique externe n'est inclus. Pas d'avis juridique exhaustif.
- **Fusion virtuelle testée** : chevauchement avec archive maîtresse = deux fichiers authoring d'origine; douze fichiers sont strictement nouveaux. Les **7320 autres fichiers sources** du maître sont hors des chemins de remplacement (empreintes SHA-256 recensées en mémoire), donc inchangés par l'application du delta. Le ZIP n'emporte aucun fichier de gouvernance, de registre ou d'un autre Kristal.
- **ZIP construit dans la même exécution et contrôlé après écriture** : compte exact, ordre de première entrée, chemins sûrs, tailles, CRC, manifeste et JSON (11 vérifications après création).

## Limites et revue humaine obligatoires

1. **Scientifique :** confirmer validité des modèles simplifiés, fonctions d'adaptation selon les organismes nommés et précision terminologique fruit/graine; éviter anthropomorphisme, téléologie et généralisations hâtives.
2. **Pédagogique :** tester intelligibilité des stimuli, deux épreuves autonomes et capacité de la grille à discriminer la maîtrise; vérifier que les réponses alternatives correctes sont acceptées.
3. **Accessibilité/sécurité :** constater en situation l'efficacité de la lecture orale, des cartes, du pointage et des outils d'assistance; ne pas exiger de capture, élevage ou contact avec organisme/allergènes.
4. **Droits :** les seules ressources externes sont des citations bibliographiques/URLs, sans leurs textes longs ou médias; revoir tout futur ajout audiovisuel.
5. **Validité de banque :** items fixes du corpus, aucune IA générative libre, aucune graine ni mode paramétrique; toute nouvelle variante scientifique exige source, corrigé et révision.

## Propositions de changement de structure, non appliquées

- Proposer un registre central **futur** de corpus de scénarios scientifiques revus avec leurs sources et dates; aucune modification de `registry/` ou `governance/` réalisée.
- Proposer un champ commun traçant l'accommodement de modalité et le niveau de preuve de « caractère décrit » versus « directement observé »; ne pas modifier les schémas du maître durant ce mandat.
- Enregistrer les résultats de pilotage pédagogique dans le système de suivi prévu, jamais dans les fichiers canoniques du Kristal.
