# Validation de livraison — qc-pri-us-016 (v1.2)

**Statut : `a_revoir`**, non certifié, non homologué, non publié. Delta d'un seul Kristal.

## Contrôles réellement exécutés

- **196 contrôles programmatiques pré-emballage réussis sur 196** (`verify_pack.py` local). Les contrôles portent sur : conservation littérale du YAML et de ses 12 sections, invariants v1.2 du contrat (champs du blueprint inclus), famille et préalables, alignement avec le graphe natif, 12 numéros sans doublons, champs obligatoires et états de la banque, scénarios verrouillés, deux preuves différentes, années-clés dans les stimuli et les corrigés, renvois du plan, présence des diagnostics/pratiques/transferts, manifeste et sécurité des chemins.
- **Contrôles manuels du contenu rédactionnel :** 12 corrigés parcourus et confrontés aux notices attribuées; différences entre langue, pratique, héritage et diversité; dates 1755–1763 (Grand-Pré), 1832–1937 (Grosse-Île), 1864 (Monument-Lefebvre); distinction entre sources, interprétations et lacunes; aucune fausse citation ou photographie reprise.
- **Vérification web des sources lors de la rédaction (2026-10-08) :** S1 UNESCO, S2 Musée canadien de l'histoire, S3/S4/S5 Parcs Canada; liens, portées et limites documentés dans `sources/REFERENCES_CONTENU.md`. La vérification des URLs dans les fichiers est une validation de forme; les pages web peuvent être modifiées.
- **Contrôles post-emballage exécutés séparément avant la livraison :** premier chemin, 14 entrées exactement et non vides, racine `kristals/qc-pri-us-016/`, aucun parent englobant, aucune entrée `../` ou absolue, manifeste identique au ZIP, lecture et parsing JSON dans le ZIP, correspondance SHA-256 du contenu ZIP/fichiers locaux. Voir le script de packaging et sa sortie de test. Les valeurs définitives sont testées à nouveau sur l'archive livrée.

## Livrables et changements
- **Remplacements conservateurs (2) :** `authoring/PARCOURS.md` (frontmatter natif inchangé, douze sections remplies), `authoring/CONTRAT_PEDAGOGIQUE.json` (champs v1.2 préservés, paramètres complémentaires de la famille).
- **Ajouts (12) :** 6 modules de contenu, 3 fichiers d'évaluation, 1 provenance, 1 manifeste, présent rapport.
- **Dispositif pédagogique :** 2 diagnostics, 3 accompagnements à indices dégressifs, 4 autonomies, 2 transferts et 12 scénarios d'évaluation dont 2 preuves finales (`q-011` langues / `q-012` lieux de mémoire). Rubrique analytique à 4 dimensions; deux manifestations nécessaires.
- **Droits :** paraphrases et textes originaux; aucun visuel, témoignage ou document protégé copié. **Aucune licence réutilisable de tiers n'est affirmée**. Les licences des pages externes n'ont pas été auditées individuellement : réutilisation de ressources tierces à autoriser séparément.

## Limites non résolues et revue humaine nécessaire
1. **Revue disciplinaire** : confirmer la nuance des usages linguistiques, le contexte des mémoires acadienne et irlandaise, les choix de présentation institutionnelle et l'absence de stéréotypes, idéalement avec expertise des communautés concernées.
2. **Revue pédagogique** : essayer durée, compréhension du lexique, équivalence oral/écrit et fiabilité interévaluateurs de la rubrique sur des réponses réelles.
3. **Sources évolutives** : revalider les pages S1–S5 au moment de l'emploi; les notices sont factuellement bornées à ces pages, non à toutes les interprétations historiques possibles.
4. **Essais LMS et lecteurs d'écran** : adaptations décrites, non vérifiées dans un LMS concret ni avec élèves.
5. **Épreuves** : données et rubriques contrôlées, mais aucun test psychométrique et aucune certification d'items.

## Propositions de structure, NON appliquées
- Éventuellement enregistrer `scenario_id`, `source_id` et date de revue directement dans un registre central *par version de corpus*, après décision de gouvernance.
- Prévoir un mécanisme de remplacement de stimulus sourcé et révisé pour éviter qu'une deuxième passation ne répète un texte mémorisé.
- Ajouter un journal de revue communautaire et d'accessibilité séparé à la chaîne de qualification; **aucune base centrale n'est modifiée ici**.

**Fusion :** extraire le ZIP depuis la racine `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` du workspace maître. Aucun fichier hors `kristals/qc-pri-us-016/` n'est livré.
