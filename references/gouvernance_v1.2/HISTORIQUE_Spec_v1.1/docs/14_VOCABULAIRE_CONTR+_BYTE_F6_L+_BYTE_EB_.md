# 14 — Dictionnaire de champs et valeurs contrôlées

Ce vocabulaire s'applique aux **sources de domaine du projet**; il ne remplace pas les schémas natifs Framework v9.

## 14.1 Champs de l'identité

- `id` : motif `^qc-pri-(fr|ale|als|fls|ilss|ma|st|us|ap|ad|da|mu|eps|ccq)-[0-9]{3}$` pour les 202 IDs initiaux. Si une discipline dépasse 999 unités, RFC pour étendre le motif.
- `discipline_code` : `FR`, `ALE`, `ALS`, `FLS`, `ILSS`, `MA`, `ST`, `US`, `AP`, `AD`, `DA`, `MU`, `EPS`, `CCQ`.
- `langue_contenu` : BCP 47; `fr-CA` ou `en-CA` par défaut selon rédaction effective.
- `revision_contenu` : SemVer numérique `MAJOR.MINOR.PATCH`.
- `auteur`, `reviseur` : identifiant organisationnel stable ou rôle avec journal de contribution, pas donnée d'élève.

## 14.2 Statuts

**Feuilles :** `réservé`, `en_rédaction`, `prêt_validation`, `qualifié`, `publié`, `activé`, `bloqué`, `retiré`.

**Alignement :** `à_vérifier`, `partiel`, `verifie`, `conflit`.

**Provenance :** `non_documentée`, `références_identifiées`, `vérifiée`, `conflit`.

**Preuve de relation / famille :** `proposition`, `en_revue`, `valide`, `rejeté`.

**Assemblage :** `brouillon_assemblage`, `prêt_validation`, `qualifié`, `publié`, `retiré`.

**Usage d'épreuve :** `entrainement`, `sommative_locale`. Une épreuve produite ici n'est jamais qualifiée d'épreuve ministérielle.

**Plan d'épreuve :** `brouillon`, `entrainement_non_certifie`, `prêt_validation`, `qualifié`, `retiré`.

Lettres, accents et casse sont **significatifs** dans les valeurs d'auteur ci-dessus; aucun synonyme n'est accepté par les validateurs du projet.

## 14.3 Cycles et années

- `annee_primaire` : entier `1` à `6`, ou `null` tant que non établi.
- `cycle_primaire` : `1`, `2`, `3`, ou `null` si non établi.
- `annee_scolaire` : `AAAA-AAAA` avec seconde année = première + 1.
- `maturite_pda` : `learn_with_teacher`, `expected_end_of_year`, `reuse` **seulement si sourcée**, sinon `null`.
- `programme_variante` : libellé référencé depuis ScolQc; `base`/`immersion` pour FLS lorsque pertinents; une valeur non trouvée n'est pas inventée.

## 14.4 Relations du graphe

`requires`, `recommends_before`, `reinforces`, `supports`, `alternative_to`, `composed_of`. Sens et règles définis par doc 06. La notation d'implémentation doit explicitement spécifier `from` et `to` selon ce même sens.

## 14.5 Noms de champs requis d'une activité

`activity_id`, `objectif_ref`, `consigne`, `materiel_ou_contexte`, `production_attendue`, `feedback`, `differenciation` optionnel, `barreme_ou_rubrique` optionnel, `seuil_de_decision` optionnel.

## 14.6 Noms de champs d'une famille d'évaluation

`family_id`, `objectif_ref`, `critere_ref`, `format`, `difficulte_cible`, `variables`, `contraintes`, `solution_ou_rubrique`, `strategie_feedback`, `generabilite`, `verification`, `accessibilite`, `risques`, `licence_support`. `competence_ref` si correspondance curriculaire prouvée.

**`null` = inconnu/non vérifié. `[]` = ensemble vide établi.** Cette distinction est obligatoire partout dans le projet; « aucune source » ne doit pas cacher « source non encore cherchée ».
