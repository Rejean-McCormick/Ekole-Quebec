# Références, dérivations et droits — qc-pri-ma-022

## 1. Sources internes réellement consultées

- `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` : frontière avec le curriculum québécois, démarche diagnostic → modelage → pratique → deux preuves de maîtrise, interdiction de déclarer des items certifiés sans revue.
- `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` : champs de familles, trois modes de génération et règle de correction contrôlée des paramètres.
- `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` : discipline « Mathématique » et absence de correspondance ministérielle automatique.
- `registry/GRAPHE_PEDAGOGIQUE_202.json` : arête sortante `qc-pri-ma-022/recommends_before/qc-pri-ma-021`; aucun `requires` ni `reinforces` pour la feuille.
- `kristals/qc-pri-ma-022/authoring/PARCOURS.md` (état avant remplacement), `CONTRAT_PEDAGOGIQUE.json` (état avant remplacement), `ALIGNEMENT.md` et `BRIEF_REDACTION.md` : identité, objectif, quatre notions, critère, famille et format de production.

Ces sources appartiennent au workspace de départ et ont été lues localement; **aucune d'elles n'est incluse dans le ZIP**, sauf les deux remplacements autorisés du dossier `authoring/`.

## 2. Connaissances géométriques et raisonnement dérivé

Les définitions adaptées aux **polyèdres** et les nombres F/A/S sont établis par comptage des faces, sommets et arêtes (en tenant compte qu'une arête borde deux faces). Les vérifications sont reproductibles sur des modèles combinatoires :

| Polyèdre | Faces et types | Incidences de côtés I | A=I/2 | S | Contrôle F+S=A+2 |
|---|---|---:|---:|---:|---|
| Cube | 6 carrés | 6×4=24 | 12 | 8 | 6+8=12+2 |
| Pavé droit non cubique | 6 rectangles | 6×4=24 | 12 | 8 | 6+8=12+2 |
| Prisme droit triangulaire | 2 triangles + 3 rectangles | 2×3+3×4=18 | 9 | 6 | 5+6=9+2 |
| Pyramide carrée | 1 carré + 4 triangles | 4+4×3=16 | 8 | 5 | 5+5=8+2 |
| Tétraèdre | 4 triangles | 4×3=12 | 6 | 4 | 4+4=6+2 |

La relation d'Euler citée ici sert de **contrôle secondaire pour ces polyèdres convexes uniquement**. Elle ne suffit pas à identifier un solide. Les caractères pliables et non pliables des patrons de cube sont vérifiables par propagation des orientations des faces et par montage d'un modèle en carton; le test informatique est précisé dans `livraison/VALIDATION.md`. Un « patron » doit toujours respecter le placement des faces et la fermeture du volume, pas seulement leur nombre.

## 3. Productions originales et droits

Textes, descriptions de maquettes, exercices, rubriques, scénarios de musée et de lanterne, dispositions de patrons en mots, calculs et algorithmes des items ont été rédigés pour ce Kristal. Aucun schéma, photographie, extrait de manuel ni illustration externe n'a été recopié ou embarqué. Les documents internes cités sont des **références de travail**, pas des déclarations d'autorisation de republication de leur contenu. Aucune licence de tiers, citation littérale externe, URL factice ou permission de droit inventée.

## 4. Ce qui n'a pas été vérifié et doit l'être

Aucune revue externe de manuels et aucun essai d'utilisation auprès d'élèves n'ont été effectués pour cette livraison. Les tableaux mathématiques et exemples de génération peuvent être contrôlés automatiquement, mais un spécialiste doit relire : ambiguïtés linguistiques de consignes, faisabilité des maquettes au matériel réel, adaptation tactile, temps de passation, biais culturels et fidélité de correction de réponses argumentées. Aucune qualification PFEQ, homologation, licence institutionnelle ou certification d'item n'est revendiquée.
