# B2 → Ekole v3 : contrat d'intégration proposé (non appliqué)

La v3 décrite dans les échanges précédents utilisait `ekole-quebec/publications/eleve/<course_id>.json` avec les clés `format`, `id`, `titre`, `statut_publication`, `notice`, `modules`, et chaque module `{id,titre,texte}`. **Le générateur B2 produit exactement cette forme**, avec des instructions courtes à partir des blocs éditoriaux.

## Étapes de consolidation sur une COPIE

1. Décompresser la même v3 de référence pour B2, B3 et B4, puis vérifier les hachages des 202 fichiers `cours/*.json`.
2. Placer le module Python `b2_pipeline` dans l'outillage choisi (pas dans l'API publique) et connecter la lecture source `cours/<id>.json` + contrat Kristal.
3. Dans l'atelier B3, éditer `ekole.b2.student-draft/1` (ou écrire un adaptateur bijectif contrôlé). **Ne pas remplacer un document brut par un JSON éditorial au hasard**.
4. Après validation, exporter B2 vers une copie de `ekole-quebec/publications/eleve/qc-pri-ma-008.json`; conserver `brouillons`, `revues` et `audits` côté privé, non servi par HTTP.
5. Vérifier que le serveur Élève consulte **uniquement** `publications/eleve` pour un pack `politique_publication: vues_separees` et ne propose jamais `cours/<id>.json` comme fallback pour le Québec.
6. B4 doit rendre uniquement les `modules[].texte` publics et ne jamais lire les notes privées, ni afficher une réponse attendue anticipée.
7. Garder `integrations/spek.json` historique réservé à l'enseignant. Toute nouvelle publication Spek doit passer ses propres règles de sélection et d'autorisation.
8. Tests sécurité contre GET direct des corrigés et médias non approuvés, tests de modification tardive, captures Playwright Élève + Enseignant.

**Conflit connu avec la v3 :** son brouillon Enseignant semblait être un JSON à six modules Markdown. B2 introduit des blocs typés et des données de provenance privées. La migration du format **n'est pas encore faite**, et une écriture directe de B2 dans B3 casserait probablement son éditeur. La branche B3 et la consolidation doivent arbitrer.

**Aucun changement au dépôt `ecole-pastorale`** dans B2.
