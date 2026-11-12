# B1 — proposition pour les branches et la consolidation

1. Définir un identifiant canonique d'exigence ministérielle (programme, progression, cycle/année, page, libellé exact, date de version) et **ne pas confondre** l'ID interne `qc3.*` avec cet identifiant.
2. Ajouter un **tableau d'alignement révisé par enseignant** : objectif interne → exigence officielle → source → Kristal(s) → classe/année pertinente → éventuels prérequis. Les 71 écarts sont une file de revue, pas des corrections automatiques.
3. Pour chaque objectif, publier séparément : situation planifiée, activité vérifiée, preuve élève attendue, preuve recueillie (non personnelle par défaut), critères d'évaluation, statut et date de validation. Ne pas compter une activité proposée comme réalisée.
4. Organiser un calendrier par compétence plutôt que par seul scénario et préciser la fonction des semaines 9, 18, 27 et 36.
5. En CCQ et en univers social, exiger une revue de contenu et de sources avant scénario interactif; les activités obligatoires ne doivent pas dépendre uniquement de jeux de rôle.
6. Dans le portail Enseignant, ajouter un tableau de couverture et d'alertes lisible; dans le portail Élève, ne jamais montrer les contrôles réglementaires.
7. Préparer un pilote vérifié avec la multiplication (`qc3.ma.multiplication` → `qc-pri-ma-008` → scénario `commande-de-pains`), mais ne pas le généraliser aux autres matières sans vérification.

## Contrat proposé, NON intégré

```json
{
  "requirement_id": "a_confirmer_depuis_pdf_officiel",
  "internal_objective_id": "qc3.ma.multiplication",
  "course_ids": ["qc-pri-ma-008"],
  "grade_proposed": 3,
  "official_reference": {"url": "", "page": null, "revision": ""},
  "alignment_status": "a_revoir_par_enseignant",
  "learning_activity_status": "planifiee",
  "evidence_status": "non_observee",
  "publication_status": "non_verifiee",
  "updated_by": null
}
```

Ce schéma doit être discuté avec B2 et B5, **pas imposé au moteur**.
