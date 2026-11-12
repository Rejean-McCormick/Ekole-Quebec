# 10 — Gates de validation, tests et critères de publication

## 10.1 États du cycle de vie

`réservé` → `en_rédaction` → `prêt_validation` → `qualifié` → `publié` → éventuellement `activé`; `bloqué`, `retiré` possibles. **Une transition doit avoir une preuve**, pas seulement une nouvelle étiquette. `publié` et `activé` sont des événements distincts gérés par la toolchain adéquate.

## 10.2 Gates

| Gate | À vérifier | Si échec |
|---|---|---|
| G0 identité | ID attribué et unique; discipline exacte; propriétaire/branche déclarés | Refus d'intégration |
| G1 structure | Modèle complet, champs, sections, références internes | Retour rédaction |
| G2 curriculum | Source, édition, localisateur, année et compétence vérifiés; inconnus non dissimulés | Pas de qualification PFEQ |
| G3 pédagogie | Résultat observable, activités guidées/autonomes, feedback, remédiation, preuve de maîtrise | Pas de qualification |
| G4 graphes | Références résolues, zéro cycle `requires`/`composed_of`, aucune duplication propriétaire | Blocage assemblage |
| G5 évaluation | familles vérifiables, critères, corrigé/rubrique, contraintes de génération, traces | Pas d'export d'épreuve |
| G6 sécurité | droits, âge, accessibilité, données personnelles, CCQ | Blocage publication |
| G7 technique | schémas réels du Framework/Authoring Kit, build, integrity, provenance | Pas de publication Kristal |
| G8 assemblage | couverture documentée, variantes compatibles, états enfants pinnés, absence de trous dissimulés | Publication limitée ou interdite |

## 10.3 Contrôles automatiques à implémenter

1. Parser frontmatter des feuilles; vérifier `format`, champs, types, énumérations, sections et IDs.
2. Vérifier 202 IDs de référence sans doublon ni réaffectation; détecter IDs nouveaux non attribués.
3. Graphe `requires` acyclique et liens existants; pas de parent contenant son descendant.
4. Alignements : localisateurs non vides pour `officiel_verifie`, édition applicable, interdiction d'une année sans preuve, variant différencié.
5. Activités et familles d'évaluation : références de résultats et critères résolues.
6. Questions paramétriques : rejouer mêmes seeds, tester bornes et calculs (validation déterministe); séparer les statistiques psychométriques à acquérir plus tard.
7. Contrôle de non-régression : comparaison des versions de contenus, changements des liens et des exigences affectées.
8. Build des workspaces avec `python tools/kristal.py check <workspace>` puis `build-v9 <workspace>` **selon la version réelle du kit**; jamais simuler une réussite.

Ces tests sont **la cible de validation**, et non une affirmation qu'un validateur pédagogique complet est déjà implémenté.

## 10.4 Définition de « fait »

- **Rédigé** : contenu complet mais non certifié.
- **Prêt validation** : G0–G1 réussis, G2–G6 accompagnés de preuves ou de problèmes documentés.
- **Qualifié pédagogiquement** : G0–G6 réussis, relecteur humain identifié, sources/édition et limites transparentes.
- **Qualifié techniquement** : G7 réussi sur l'artefact v9 exact.
- **Publier dans un parcours assemblé** : G8 réussi et toute dépendance finale pinnée, versionnée et auditée.

Un examen ne passe `qualifié` que si son plan, chacune de ses familles, ses critères et ses instances admissibles sont revus; la qualification d'une feuille **ne qualifie pas automatiquement ses examens générés**.

## 10.5 Gate supplémentaire G2-R (ajout v1.1)

Vérifier qu'aucun code administratif déclaré officiel n'est absent du registre central qualifié. Refuser la mention `officiel_verifie` d'un code qui n'a ni source, ni type, ni édition, ni applicabilité précise. `code_officiel: null` est valide si la donnée n'est pas attestée. **G2-R ne remplace pas G2** sur l'alignement curriculaire.
