# Provenance et références | qc-pri-ma-008

## 1. Sources effectivement consultées **dans l'archive source**

- `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` — autorité sur frontières de design, préalables, deux preuves distinctes, traces et statut non certifié.
- `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` — champs minimums des familles; modes fixes et paramétriques, contrôles des solutions, graines reproductibles.
- `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` — appellation « Mathématique » seulement; pas de garantie de conformité PFEQ.
- `governance/Norme_Pedagogique_Autonome_v1.2/REFERENCES_EVIDENCE.md` — répertoire *interne* de liens EEF, IES/WWC, CAST. Ces URLs sont présentes dans la source; **elles n'ont pas été ouvertes ni vérifiées en ligne pour cette livraison**.
- `registry/GRAPHE_PEDAGOGIQUE_202.json` — `requires: qc-pri-ma-006` et `recommends_before: qc-pri-ma-003`. Vérification dans le graphe, sans modification des relations.
- `kristals/qc-pri-ma-008/authoring/PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md` — frame et identités natives réutilisées et conservées. Les deux derniers documents sont lus et non modifiés.

**Portée du mot « vérifiées » :** présence, contenu et lecture des fichiers dans le ZIP source; ce terme ne signifie pas revue par une institution, revue externe de recherche ou essai sur des élèves.

## 2. Raisonnements dérivés et contrôles mathématiques

- `a × b` modélise `a` groupes contenant chacun `b` objets; le total équivaut à `b` répété `a` fois en addition. Les tableaux rectangulaires fournissent une autre représentation du même cardinal.
- Distributivité pour entiers naturels : `a × (b + c) = a × b + a × c`. Par exemple `4 × (5 + 2) = 20 + 8 = 28`.
- Le résultat seul ne permet pas de valider le **sens** du regroupement : `2 + 3 + 4` et `3 × 3` donnent tous deux 9, sans décrire les mêmes groupes. Ceci motive les critères de dessin et d'unité.
- Corrigés des instances seedées produits par les formules documentées dans `BANQUE_ITEMS.json`; contrôles locaux par itération et égalité distributive détaillés dans `livraison/VALIDATION.md`.

## 3. Productions nouvelles et droits

Sont rédigés pour cette livraison : les explications, scénarios, groupes ASCII, exemples, non-exemples, diagnostics, activités guidées et autonomes, transferts, douze tâches, feedback, rubriques et barèmes. Aucun passage d'un manuel ni image externe n'est incorporé. La réutilisation de règles et de métadonnées vient du workspace fourni; aucun droit de propriété sur les fichiers centraux ou sur d'éventuels textes tiers n'est revendiqué. Une vérification éditoriale finale des licences globales du produit reste une responsabilité distincte.

## 4. Limites et revue requise

Le contenu mathématique est contrôlé localement, mais son efficacité pédagogique, l'équité des tâches, la formulation précise adaptée aux élèves, les aménagements d'accessibilité en contexte réel et toute homologation ne sont **pas** établis par ces contrôles. Aucune référence ministérielle précise n'est revendiquée; les liens de recherche recensés dans l'archive ne sont pas présentés comme une preuve directe de chaque exercice.
