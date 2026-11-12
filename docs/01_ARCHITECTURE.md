# Chaîne Kristal → Ekole

```text
Kristal-Portail candidat (identité et organisation)
  ├── références exactes vers 202 workspaces d’auteur
  ├── graphe : requires / recommends_before / reinforces
  ├── pages institutionnelles et obligations de phrases
  └── politique des projections
       ├── SemantiK : phrases vérifiées et étiquetées (port non raccordé)
       ├── Konstellation / Light : navigation, perspectives (port candidat)
       ├── Ekole site : cartes, listes, fiches (fonctionnel hors ligne)
       ├── Médiathèque : liens et références (port candidat)
       └── Moodle local_uckk : cours / évaluations / accès (plan seulement)
```

## Différences de responsabilités

- `kristals/` : contenus pédagogiques complets et métadonnées de workspace, sans état sémantique v9 qualifié.
- `catalogue/` : index et graphe dérivés du registre, non autorité indépendante.
- `organisation/` : description éditoriale de l’établissement, pages, publics et vues croisées.
- `site/` : projection statique générique avec les six contenus pédagogiques par cours, **sans banque des réponses d'évaluation**.
- `vendor/reference-only/` : copies archivées des composants fournis à consulter; aucune exécution implicite, aucun déploiement automatique.
- `tools/ekole.py` : contrôles, génération, prévisualisation, plan Moodle, copie statique locale sécurisée.

## Invariants

- `vague de construction` ≠ `année scolaire`.
- Une recommandation d'ordre ne devient jamais un verrou Moodle.
- Les évaluations et leurs corrigés ne sont pas diffusés sur le site statique public.
- Aucun identifiant de Moodle n'est déduit d'un ID Kristal (mapping explicite obligatoire).
- Un nœud v10 peut héberger plusieurs États v9; le dépôt GitHub n'est pas l'État sémantique.
