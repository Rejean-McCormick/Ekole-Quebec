# Références, provenance et droits — `qc-pri-ma-001`

## A. Sources internes du workspace effectivement consultées

Ces sources existent dans l'archive maîtresse `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, **non** dans le delta livré; les liens ci-dessous sont relatifs à la racine du workspace maître.

- `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` : cycle diagnostic–modelage–pratique–maîtrise; deux manifestations autonomes; variantes déterministes en mathématiques.
- `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` : champs obligatoires d'une famille d'évaluation; trois modes; statut non certifié sans revue.
- `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` : appellation « Mathématique » et refus d'homologation PFEQ implicite.
- `registry/GRAPHE_PEDAGOGIQUE_202.json` : `qc-pri-ma-001` ne possède pas de lien sortant; un lien **entrant** de type `requires` vers ce Kristal existe, sans impact sur la présente livraison et sans modification d'un autre Kristal.
- `kristals/qc-pri-ma-001/authoring/PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md` et `AGENTS.md` : identité, limites, contraintes de rédaction et séparation canon/projection.
- `governance/Norme_Pedagogique_Autonome_v1.2/REFERENCES_EVIDENCE.md` : **liste de ressources recommandées**; sa présence dans l'archive ne constitue pas, en elle-même, une vérification indépendante de chaque ressource.

## B. Sources externes effectivement consultées (en ligne, 8 octobre 2026)

1. **Institute of Education Sciences (IES), What Works Clearinghouse**, *Teaching Math to Young Children* (guide de pratiques), https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/early_math_pg_111313.pdf — recommandation de compter un objet par mot-nombre et de lier dernier mot et total; appui conceptuel uniquement. Une autre adresse accessible dans la recherche : https://ies.ed.gov/ncee/wwc/Docs/practiceguide/early_math_pg_111313.pdf.
2. **IES / Regional Educational Laboratory**, *Teaching Math to Young Children Toolkit*, https://ies.ed.gov/ncee/rel/math-young-children — lexique de « one-to-one tagging », cardinality, keeping-track errors et représentations; renseignements factuels sur le comptage, sans rattachement officiel au PFEQ.
3. **IES**, *Teaching Math to Young Children for Families and Caregivers*, https://ies.ed.gov/use-work/resource-library/resource/other-resource/teaching-math-young-children-families-and-caregivers — comptage objet par objet, quantité totale et activités concrètes.

Ces ressources n'autorisent **pas** à déclarer les items locaux validés empiriquement, « certifiés » ou conformes au ministère de l'Éducation du Québec. Ni figures ni extraits significatifs n'ont été copiés; seuls les concepts généraux ont orienté la rédaction.

## C. Raisonnements dérivés et vérifications mathématiques

- Le cardinal d'une collection finie est indépendant de l'ordre de désignation si chaque élément est compté exactement une fois.
- Pour deux groupes disjoints couvrant la collection, total = taille du groupe A + taille du groupe B; extension à trois groupes ou davantage.
- Pour `n` objets, une partition en groupes de cinq donne `n = 5*q + r` avec `q = n // 5`, `r = n % 5`, `0 <= r < 5`; le reste, s'il existe, est conservé.
- Les instances paramétriques de `evaluation/BANQUE_ITEMS.json` résultent d'un calcul déterministe; la validation technique indépendante et les bornes sont documentées dans `livraison/VALIDATION.md`.
- Le choix éditorial de 0–20 objets, les deux contextes de preuve et les seuils de maîtrise sont des **décisions pédagogiques locales**, non des prescriptions empiriques universelles.

## D. Productions originales et droits

- Textes de leçon, exemples, contre-exemples, stimuli à symboles élémentaires Unicode, algorithme de seed, consignes, rubriques et feedback ont été élaborés pour cette livraison; aucun texte/figure de tiers n'est reproduit comme un actif de cours.
- Les simples caractères typographiques ne constituent pas une image de banque d'illustrations; vérifier le rendu des polices dans l'environnement de destination.
- Aucune permission nouvelle ni cession de droits sur des contenus tiers n'est affirmée. Aucun matériel sous licence externe n'est intégré au ZIP.
- Avant redistribution publique ou publication LMS, le responsable doit vérifier le contexte légal, les attributions éventuelles à ajouter si d'autres ressources sont intégrées, la qualité et l'accessibilité des rendus.
