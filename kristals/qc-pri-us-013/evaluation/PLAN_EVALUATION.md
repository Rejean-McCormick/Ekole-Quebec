# Plan d'évaluation — `qc-pri-us-013` / v1.2

**Alignement identique pour les dix items :** `obj-1` — Décrire un enjeu du Québec contemporain à partir d’informations croisées. **`crit-1` :** Synthétiser un enjeu avec faits, acteurs et limites des sources. **Famille :** `qc-pri-us-013-ev-01` (type natif `generee_sous_contraintes`, réalisation en **dossiers fixes contrôlés**, sans génération AI libre et sans seed applicable aux items fixes). Les items sont tous `a_revoir`.

## Couverture documentée de chaque item

| Item (ID complet) | Difficulté | Documents / représentation | Preuve ciblée, critères de correction | Rôle |
|---|---|---|---|---|
| `qc-pri-us-013-q-001` | initial | A1/A2, frise et tableau | Auteur/date, type, chronologie; 2016, 2021, 2022, 2026 distingués | formatif |
| `qc-pri-us-013-q-002` | initial | A1, données 33,7 % / 25,2 % | Population correcte, baisse de 8,5 **points**; aucune prétention 2026 | formatif |
| `qc-pri-us-013-q-003` | initial | B1/B2, propositions classées et justifiées | Portée politique, soutien, inférence locale impossible | formatif |
| `qc-pri-us-013-q-004` | intermédiaire | A1/A2, acteurs-fonctions | Statistique Canada / SHQ, échelles et causalité | formatif |
| `qc-pri-us-013-q-005` | intermédiaire | B1/B2, territoires | Province, municipalité, milieu rural et limite de desserte | formatif |
| `qc-pri-us-013-q-006` | intermédiaire | A1/A2, révision d'énoncé | Chiffres, unité, dates, population et non-causalité | formatif |
| `qc-pri-us-013-q-007` | intermédiaire | B1/B2, trois phrases | Politique 2018, aides 2026, acteurs, limite | formatif |
| `qc-pri-us-013-q-008` | transfert | A1/A2 + B1/B2, indicateurs manquants | Rechercher données concrètes datées, pas inventer des résultats | formatif |
| `qc-pri-us-013-q-009` | transfert | A1/A2, synthèse logement | **Preuve complète A**, M1–M5; deux sources / deux acteurs / deux limites | maîtrise A |
| `qc-pri-us-013-q-010` | transfert | B1/B2, synthèse mobilité | **Preuve complète B**, M1–M5; autre enjeu, autre corpus | maîtrise B |

**Traçabilité :** chaque ligne est liée à `obj-1`, `crit-1`, `qc-pri-us-013-ev-01` par la déclaration de tête, et chaque enregistrement JSON possède les trois champs.

## Corpus fermé, variation et contrôle

- Quatre documents **A1** Statistique Canada (2016/2021, tableau modifié 2022), **A2** SHQ (2026), **B1** Politique de mobilité durable (2018), **B2** aides transport collectif (2026), tous attribués et paraphrasés avec URLs dans les références.
- `mode=fixe` pour les dix items : **seed=null**, `parametres=null`, même consigne, même source, même ensemble d'informations prouvables. La *famille* reste du type natif `generee_sous_contraintes`; l'implémentation en corpus fermé est sa variante minimale fiable; aucune génération automatique ne certifie les réponses.
- Variations **d'accès seulement** : taille de police, texte lu, dictée fidèle, oral/écrit, temps de préparation, table linéarisée; aucun remplacement non approuvé de dates, valeurs, acteurs, territoire ou cible.
- **Faits vérifiables et limites** : différence 33,7−25,2=8,5 points, pas causalité; couverture B1 toutes régions ≠ fréquentation; B2 décrit du soutien, pas résultats. Le correcteur accepte paraphrases factuellement équivalentes avec citations et limites.

## Administration et deux preuves

1. Présenter q-009 seul à partir de A1/A2, sous forme lisible, **sans modèle de synthèse visible**; noter sources citées, date, chiffres, acteurs et limites.
2. Administrer q-010 sur un autre enjeu B1/B2, idéalement à un autre moment; éviter transfert direct d'un paragraphe appris mot à mot.
3. Coter **chaque preuve séparément** selon M1–M5 de `GRILLE_MAITRISE.md` : suffisant (2) sur **toutes** les dimensions de chaque épreuve, sans compensation par note totale.
4. Un échec isolé entraîne rétroaction ciblée, réentraînement et **nouvelle** preuve équivalente validée par un humain; jamais une moyenne 009+010.

## Équité, sécurité et neutralité

Aucune divulgation de situation résidentielle, sociale, migratoire, économique, religieuse ou de transport vécue; aucune opinion politique notée. Reconnaître qu'une source gouvernementale expose une intention institutionnelle, et qu'une statistique ne représente pas mécaniquement la voix de tous les groupes. Aucun portrait inventé des Premiers Peuples, aucun stéréotype. Alternative orale ou dictée fidèle : **seules la preuve d'analyse et les justifications sont cotées**. Aucun entretien avec tiers ni collecte de données personnelles.

## Limitations et revue

Relecture nécessaire pour les biais, la difficulté, l'évolution éventuelle des programmes et les réponses admissibles. Les quatre cartes sont des **paraphrases datées vérifiées le 8 octobre 2026**, non une garantie d'actualité future. Ni item certifié ni examen homologué.
