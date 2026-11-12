# Validation de livraison — qc-pri-ma-002 (v1.2)

**État :** contenu pédagogique rédigé et contrôles techniques réussis; famille et items **`a_revoir`** par revue humaine. Pas de statut certifié/homologué/publié ni de conformité PFEQ.

## Tests effectivement exécutés le 8 octobre 2026

- **189,299 assertions préarchivage réussies** dans `verify_ma002.py` en Python, dont **63,000 couples (algorithme, seed) testés exhaustivement** (sept familles × seeds 0 à 8 999). Un oracle indépendant a vérifié reconstruction décimale, rang de la première différence, symboles, bornes, encadrements, tris, permutations, écarts et retenues.
- Les quatre fichiers `authoring/` et de graphe ainsi que les trois normes internes exigés ont été lus dans le ZIP source; l'arête sortante `qc-pri-ma-002 requires qc-pri-ma-001` est conservée, sans relation sortante ajoutée.
- YAML du parcours conservé **identique champ par champ** à la source v1.2; 12 sections numérotées et complétées; contrat JSON natif enrichi sans suppression de champs ou rupture des invariants.
- Banque JSON composée de **10 items complets** : 3 fixes (`seed=null`, `parametres=null`) et 7 paramétriques (formules, contraintes, seeds, exemples reproductibles); identifiants séquentiels uniques, liens `obj-1`, `crit-1`, famille `qc-pri-ma-002-ev-01` et statut `a_revoir`.
- Les **deux preuves autonomes** ont des contextes différents (bibliothèque / inventaire) et des attendus déterministes. Les corrigés des exemples fixes, diagnostics, pratiques et transferts ont été recoupés arithmétiquement. Les deux modes d'accès visuel/tactile/oral sont décrits.
- Manifestes, références et droits : chemins attendus vérifiés, sources internes et pages Alloprof explicitement référencées, aucun visuel ou extrait tiers reproduit; absence de matériel privé.
- **Après création :** un second contrôle lit les 14 entrées dans le ZIP, vérifie son CRC, sa racine, la liste exacte du manifeste, le parsing de tous les JSON, l'absence de chemins absolus ou dangereux et simule la fusion sans inclure d'autres dossiers. Tout échec empêche la livraison.

## Points non vérifiés et revue humaine requise

1. Validité de la formulation des consignes pour des élèves de niveaux variés; adéquation des tâches à leurs connaissances et besoins.
2. Fidélité intercorrecteurs des justifications de rang, validité des seuils de maîtrise et essais supervisés auprès d'apprenants; **non réalisés**.
3. Lisibilité effective des nombres, formats braille, aides techniques et temps d'administration; adaptation locale à vérifier.
4. Autorisations du propriétaire pour toute redistribution ultérieure des métadonnées sources; liens externes cités sans reproduction de documents sous droits.
5. Aucun test de publication dans un LMS, de projection Framework canonique ni audit PFEQ réalisé. Mathématiques contrôlées **numériquement**, pas qualification pédagogique complète.

## Propositions de structure (non appliquées)

- À proposer centralement : un schéma de famille avec algorithmes paramétriques versionnés, oracle de comparaison indépendant et statut de contrôle des seeds.
- À proposer : une piste formalisée pour la validation d'un `requires` par diagnostic équivalent, sans changer le registre.
- Aucune modification de `registry/`, `governance/`, `docs/`, `canon/`, `state/`, `runtime/`, `kristal.workspace.json`, `AGENTS.md`, `ALIGNEMENT.md` ou d'un autre Kristal.
