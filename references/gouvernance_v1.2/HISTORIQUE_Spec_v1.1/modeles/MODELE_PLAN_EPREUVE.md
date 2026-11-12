# Plan d'épreuve — `<blueprint_id>`

```yaml
format: qc.assessment-blueprint/1.0
id: qc-pri-eval-exemple-001
revision: 0.1.0
statut: brouillon
usage: entrainement
annee_primaire: null
annee_scolaire: null
variante_programme: null
programme_edition: null
assemblage_ref: null
source_state_commitments: null
random_seed_policy: fixed_per_instance
human_review_required: true
```

## But et conditions d'utilisation

Public, buts, durée indicative si justifiée, accessibilité, accommodations documentées sans données individuelles : …

## Matrice de couverture (définie avant les questions)

| objectif_ref | feuille_id + révision | compétence/critère sourcé | tâches/familles autorisées | poids prévu | raison |
|---|---|---|---|---|---|
| obj-1 | qc-pri-ma-012 @ à_vérifier | à_vérifier | family-1 | à_vérifier | … |

## Règles de génération / sélection

- Types : `fixe_valide`, `parametrique_controle`, `generee_sous_contraintes`, `observation_ou_production`.
- Familles admissibles : …
- Contraintes de tirage et équilibre : …
- Paramètres/difficulté/temps : …
- Interdiction de substituer une compétence sans modifier la matrice : **oui**.
- Stratégie de rejouabilité : seed/version exacts, journal des instances : …

## Corrigé et critères

Grille, tolérances, types d'erreur, correction humaine, contrôle intercorrecteurs le cas échéant : …

## Qualification et génération

| gate | état | preuve / réviseur |
|---|---|---|
| Alignement officiel | non_testé | … |
| Rubriques/corrigés | non_testé | … |
| Génération déterministe | non_testé | … |
| Relecture des variants | non_testé | … |
| Export LMS sans perte de sens | non_testé | … |

**Ne pas appeler cet outil « examen ministériel ».**
