# Tests B1 — résultats observés

Date : 2026-10-16.

## Exécuté

```text
python auditer_b1.py znapshot_Ekole_10151241.zip znapshot_Kontexte_10152150.zip
python -m unittest discover -s tests -v
```

**4/4 tests** de cohérence passés. Vérifications : exactement 202 Kristals, 36 cours candidats 3e année, 83 objectifs uniques, 32 scénarios principaux, 36 semaines, 34 micro-situations, 49/34 objectifs avec/sans scénario, 12/71 liens internes classés en/hors 3e, intégrité du calendrier (semaines 9, 18, 27 et 36) et statut non attesté.

Vérification du fichier `.xlsx` : 6 onglets (tableau de bord, 83 objectifs, 36 cours, 11 disciplines, 36 semaines, guide), cellules de synthèse calculées par formules. Inspection ciblée du tableau de bord et recherche d'erreurs de formules : **aucune erreur relevée**.

Tests des correspondances de la matrice avec les pièces sources : contrôles structurels et d'identifiants effectués. Le script enregistre les empreintes SHA-256 des deux ZIP et de neuf fichiers JSON analysés.

## Non exécuté / hors champ

- Validation officielle PFEQ **ligne à ligne et par année** à partir des PDF de progression et cadres d'évaluation.
- Revue par un enseignant ou des spécialistes de CCQ / univers social.
- Validation pédagogique des activités, tests avec des élèves, ou observation d'acquis.
- Inventaire des publications Élève **du paquet v3 actuel**, non inclus dans les snapshots historiques utilisés ici.
- Playwright : aucun frontend ni backend n'a été modifié dans B1, et aucun test d'interface n'est nécessaire pour ce paquet d'audit.

**Le résultat B1 est un audit documentaire interne, pas une certification de couverture pédagogique.**
