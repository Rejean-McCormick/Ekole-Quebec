# Validation de livraison — qc-pri-fr-021

**Statut :** rédaction complète, contrôles techniques réalisés; `a_revoir` pour qualification par des humains. Aucune homologation PFEQ, certification, publication ou épreuve sommative approuvée.

## Tests réellement exécutés

- **181 assertions préarchivage réussies** à la génération, vérifiant notamment le YAML source intact et réanalysable, ses 12 sections, les champs et identifiants du contrat, le graphe (requires `qc-pri-fr-015`; recommends_before `qc-pri-fr-019`), les références internes du plan, la famille et les 10 items complets/uniques.
- Deux contextes de maîtrise réellement distincts (`q-009` journal de bibliothèque et `q-010` mini-projet scientifique fictif) avec deux rubriques et deux paragraphes chacun; rubriques explicites et statut `a_revoir`.
- Couverture vérifiée : deux exemples résolus, deux contre-exemples, deux diagnostics, trois tâches guidées avec retrait d'indices, quatre pratiques autonomes, deux transferts et rappel différé.
- Vérification des sources et droits **documentaires** : aucun média tiers repris, références bibliographiques identifiées. Aucune expertise juridique ni expérience terrain effectuée.
- Accessibilité : lecture neutre du plan, méthodes de saisie et consignes d'autonomie explicites. La pertinence réelle d'un aménagement doit être jugée humainement.
- **97 assertions de postvalidation supplémentaires exécutées** : 14 entrées uniques et non vides, JSON strict, chemins sécurisés, CRC, manifeste cohérent, **10 liens Markdown locaux résolus**, extraction effective du delta sur une copie temporaire du dossier source et contrôle SHA-256 de **34 fichiers source protégés restés inchangés**, avec exactement 2 remplacements et 12 ajouts.

## Limites à résoudre et revue humaine

1. Faire corriger à l'aveugle plusieurs productions réalistes pour examiner les divergences entre correcteurs, l'accessibilité et la clarté des rubriques.
2. Essayer les plans auprès d'élèves de différents niveaux et vérifier longueur, vocabulaire, durée et charge cognitive.
3. Vérifier l'équivalence des aides à la saisie : un scribe ne doit pas créer ni réorganiser les phrases à la place de l'élève.
4. Confirmer les droits de redistribution de l'archive maître avant partage hors du projet; aucune analyse juridique exhaustive n'a été exécutée.
5. Ne pas prétendre que les deux textes exemplaires sont les seules réponses admises; valider humainement la qualité des variantes.

## Propositions structurelles — non appliquées

- Créer un futur champ normalisé pour conserver les différentes modalités de saisie et l'autonomie réelle, sans modifier le schéma maître actuel.
- Définir une politique de comparaison intercorrecteurs pour les rubriques de rédaction et une distinction stable entre acquis du préalable et résultat du Kristal.
- Aucun fichier hors des 14 chemins du manifeste n'est modifié; `registry/`, `governance/`, `canon/`, `state/`, `runtime/`, `docs/`, `AGENTS.md`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md` et les autres Kristals restent inchangés.
