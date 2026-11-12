# Références et provenance — `qc-pri-ma-014`

**Périmètre :** « Fractions : opérations selon la progression » · Mathématique · version de base v1.2. Cet inventaire distingue **consultation réelle du workspace**, **conséquences mathématiques contrôlables** et **rédaction originale**. Les sources pédagogiques citées en interne ne sont pas des preuves d'homologation ou de conformité au PFEQ.

## A. Sources primaires du workspace effectivement consultées

Ces fichiers se trouvent **dans l'archive existante**, sous la racine `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` imbriquée dans `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip`. Ils ont été lus; aucun n'est reproduit ou modifié dans la livraison, hormis les **deux** documents `authoring/` autorisés :

1. `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` — frontière institutionnelle/interne, diagnostic permettant un acquis équivalent, deux manifestations de maîtrise, règle des variantes mathématiques contrôlées.
2. `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` — champs obligatoires d'une famille, trois modes, seed, contraintes, solution contrôlée, revue humaine nécessaire.
3. `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` — appellation « Mathématique », sans équivalence officielle ni exigence d'année fixée.
4. `governance/Norme_Pedagogique_Autonome_v1.2/REFERENCES_EVIDENCE.md` — liste de guides externes de principes généraux (IES/WWC, EEF, CAST, UNESCO) **identifiés dans la gouvernance**. Les textes originaux externes n'ont pas été consultés indépendamment dans cette production; aucune efficacité spécifique de ce cours n'est donc affirmée.
5. `registry/GRAPHE_PEDAGOGIQUE_202.json` — une relation sortante vérifiée : `requires(qc-pri-ma-014, qc-pri-ma-013)`; aucun lien conseillé ou de renforcement propre au Kristal.
6. `kristals/qc-pri-ma-014/authoring/PARCOURS.md` — en-tête YAML, objectif, critère et 12 rubriques de départ (remplacement enrichi livré).
7. `kristals/qc-pri-ma-014/authoring/CONTRAT_PEDAGOGIQUE.json` — blueprint v1.2, champ `familles`, identifiants et métadonnées de base (remplacement enrichi livré).
8. `kristals/qc-pri-ma-014/authoring/ALIGNEMENT.md` — correspondance de présentation non normative, conservée sans modification.
9. `kristals/qc-pri-ma-014/authoring/BRIEF_REDACTION.md` — mandat rédactionnel v1.2, conservé sans modification.

## B. Raisonnements et faits mathématiques dérivés (reproductibles)

- Pour `d` entier strictement positif et un **même tout en d parts égales** : `a/d + b/d = (a+b)/d`; pour `0 ≤ b ≤ a ≤ d`, `a/d − b/d = (a−b)/d`. Ce sont des égalités rationnelles exactes; le contexte impose qu'on combine bien des parts de même taille.
- Décomposition : `a/d = b/d + (a−b)/d` si `0 ≤ b ≤ a`. Une fraction unitaire vaut `1/d` et une fraction `a/d` décrit `a` de ces parts.
- Simplification : `n/d = (n/g)/(d/g)` avec `g = pgcd(n,d)`, d'où `3/6 = 1/2`, `4/8 = 1/2`, `4/10 = 2/5`; toutes les déductions numériques soumises au calcul rationnel exact.
- Le contre-exemple `1/3 + 1/4 ≠ 2/7` résulte de `1/3 + 1/4 = 7/12`; ce calcul illustre la non-compatibilité, sans étendre les compétences exigées au changement de dénominateur.
- `1/4` de 20 cm = 5 cm et `1/4` de 40 cm = 10 cm : ces quantités ne prouvent pas une demi-longueur de l'un ou l'autre ruban. L'unité choisie est toujours déterminante.
- Les 24 variantes de huit items sont fournies dans la banque avec formules, paramètres finis, seeds et rétroactions; les contrôles réalisés sont décrits dans `livraison/VALIDATION.md`.

## C. Productions originales et droit d'usage

Sont des **créations rédigées pour ce Kristal** : titres de sous-parties, modèles et contre-modèles, bandes de cases ASCII/Unicode, cas fictifs de rubans, parterre de plantation et parcours balisé, diagnostic, pratiques accompagnées et autonomes, huit familles d'items à variations finies et quatre items fixes, grilles et commentaires. Aucune image, photographie, texte long, dessin externe, extrait protégé ni ressource commerciale n'a été repris ou intégré. Les symboles de cases sont une convention graphique simple; une description textuelle équivalente est incluse pour l'accessibilité.

**Droits :** l'absence de contenu externe intégré n'autorise pas à affirmer un statut juridique de licence que le workspace ne définit pas. Avant diffusion publique, confirmer les droits de diffusion internes et revoir la formulation des références institutionnelles. Les URL référencées dans la gouvernance ne sont pas des licences de réemploi.

## D. Limites de validation documentaire

- La lecture des documents v1.2 locaux **ne valide pas** les études externes ni l'efficacité en classe de ces séquences.
- L'alignement précis au PFEQ n'a été ni demandé ni entrepris; seule la nomenclature de discipline est maintenue.
- Les choix de difficulté, d'indices, de seuil et de rappel différé sont des décisions de conception interne, à étudier lors d'une revue pédagogique et d'un pilote de classe.
