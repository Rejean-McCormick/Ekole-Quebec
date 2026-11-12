---

format: qc.learning-path/1.0
id: qc-pri-ma-027
titre: Périmètre
discipline_code: MA
statut: contenu_redige_revue_humaine_requise
revision_contenu: 0.3.0
langue_contenu: fr-CA
resultat_principal: Calculer et interpréter le périmètre d’une figure comme longueur du contour.
objectifs_secondaires: []
criteres_reussite:
- Trouver le périmètre de deux figures et expliquer l’effet d’une modification.
prealables_declares:
- qc-pri-ma-023
- qc-pri-ma-025
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-027-ev-01
provenance_statut: references_documentees_exemples_originaux
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-027`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Périmètre  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**Statut :** rédaction complète; corrigés soumis à contrôle arithmétique; revue pédagogique humaine encore requise. Aucune conformité officielle au PFEQ ni certification revendiquée.

## 1. Intention et frontières

- `obj-1` — **Résultat vérifiable, inchangé :** Calculer et interpréter le périmètre d’une figure comme longueur du contour.
- `crit-1` — **Preuve inchangée :** Trouver le périmètre de deux figures et expliquer l’effet d’une modification.
- **Notions :** contour, longueur, addition, unité. L'unité du périmètre est une unité de longueur (cm, m), jamais de surface (cm²).
- **Frontière :** polygones droits dont les longueurs sont fournies, rectangles et figures en L décrites sans ambiguïté. Aucune inférence de mesures à partir d'un dessin non à l'échelle. Ni aire, ni mesure de courbes, ni formule généralisée pour toute figure concave.
- **Différence essentielle :** l'aire concerne l'intérieur; le périmètre additionne uniquement les bords extérieurs fermés. Deux formes d'aires différentes peuvent avoir le même périmètre.

## 2. Notions et représentations

| Notion | Définition opératoire | Exemple correct |
|---|---|---|
| **Contour** | Ligne fermée qui délimite la figure, parcourue en entier une seule fois, sans ajouter de segment intérieur. | Tracer l'extérieur d'une carte rectangulaire, pas sa diagonale. |
| **Longueur** | Mesure linéaire attribuée à chaque segment du contour. | Quatre côtés de 7, 4, 7 et 4 cm. |
| **Addition** | Somme de toutes les longueurs extérieures exprimées dans la même unité; le périmètre peut aussi être obtenu par regroupement correct. | 7 + 4 + 7 + 4 = 22. |
| **Unité** | Référence commune pour exprimer la mesure du contour. | 22 cm; non 22 cm². |

**Trois représentations :** ficelle non élastique suivant l'extérieur d'une maquette; schéma où chaque côté extérieur est étiqueté; notation `P = 7 + 4 + 7 + 4 = 22 cm`. Ne mesurer des figures réelles qu'avec un instrument approprié; les items n'exigent aucune mesure imprécise.

## 3. Préparation / diagnostic

- **Préalables `requires` stricts :** `qc-pri-ma-023` (figures planes et propriétés) et `qc-pri-ma-025` (longueurs, masses et capacités). **Ordre conseillé non bloquant : aucun. Renforcement/transfert liés : aucun.** Ces IDs restent de simples références, non copiées dans ce delta.
- `diag-1` (figure) : repérer les quatre côtés extérieurs d'un rectangle de 3 cm sur 2 cm, distinguer contour et intérieur, calculer `3 + 2 + 3 + 2 = 10 cm`.
- `diag-2` (longueurs et unités) : parcourir quatre côtés de 4, 3, 4 et 3 cm, additionner et répondre `14 cm`, puis expliquer pourquoi `cm²` serait inadéquat.
- **Passage sans blocage inutile :** si les deux aptitudes sont manifestées sans indices, attester une compétence diagnostique équivalente et commencer le parcours, même si les deux feuilles préalables ne sont pas marquées terminées. Sinon aider à nommer les figures, lire les côtés et convertir des unités seulement si nécessaire.

## 4. Enseignement guidé

- **Modelage concret → schéma → notation :** suivre un bord, identifier les longueurs, additionner, vérifier le résultat et l’unité.
- `teach-1` : expliciter le résultat attendu et présenter une carte rectangulaire fictive 7 cm × 4 cm. Suivre les quatre côtés avec le doigt, étiqueter `7, 4, 7, 4`, puis écrire `P = 22 cm`.
- **Modification :** augmenter la largeur de 7 à 9 cm sans changer la hauteur : les deux côtés horizontaux gagnent 2 cm; `P' = 9 + 4 + 9 + 4 = 26 cm`. Effet : **+4 cm**, non +2 cm.
- **Second modèle « coin découpé » :** figure en L de largeur totale 10 cm, hauteur 6 cm, coin supérieur droit retiré de 3 cm horizontalement et de 2 cm verticalement. Les six côtés extérieurs sont `10, 4, 3, 2, 7, 6 cm`, donc `P = 32 cm`. Un coin plus large de 4 cm donne `10, 4, 4, 2, 6, 6 cm = 32 cm` : le périmètre ne change pas. Le détour créé remplace exactement les bords supprimés.
- Interroger : « Quelle ligne mesures-tu? », « Chaque côté compté une fois? », « Quelle unité? », « Quels côtés changent après la modification? ».

## 5. Pratique accompagnée

- `guided-1` **indices forts** : rectangle de 5 cm × 3 cm. Tracer ensemble le contour, lire les côtés, calculer `5 + 3 + 5 + 3 = 16 cm`; retirer le geste de pointage au second calcul.
- `guided-2` **indices moyens** : rectangle 6 cm × 4 cm, agrandi en largeur de 2 cm. Élève remplit une table « largeur/hauteur/côtés modifiés » : `20 cm → 24 cm`, effet `+4 cm`. Adulte ne fournit que la question « Combien de côtés ont changé? » avant retrait.
- `guided-3` **indices faibles** : figure en L `W=9, H=6, w=2, h=3 cm`, côtés extérieurs `9,3,2,3,7,6`. Trouver `30 cm` et expliquer le tracé sans démonstration simultanée; gabarit vierge facultatif.
- Rétroaction toujours sur le premier maillon incorrect (contour, choix des côtés, addition, unité, comparaison), avec nouvel essai distinct.

## 6. Pratique autonome

- Quatre tâches originales sans exemple à copier en direct; voir `contenu/05_PRATIQUE_AUTONOME.md`.
- A1 : carré de 4 cm : `16 cm`, somme de 4 côtés.
- A2 : rectangle 7 × 5 cm, puis 8 × 5 cm : `24 cm`, `26 cm`, effet `+2 cm`.
- A3 : rectangle 9 × 3 cm, puis 9 × 4 cm : `24 cm`, `26 cm`, effet `+2 cm`.
- A4 : figure en L `W=8, H=5, w=3, h=2 cm`, coin changé en `w=2` : `26 cm` puis `26 cm`, variation `0 cm`.
- **Production attendue :** contour localisé, calcul annoté avec unités, modification des côtés concernés explicitée. Les calculs sont reconstruits individuellement sans aide sur les nombres.

## 7. Feedback et erreurs typiques

| Erreur observable | Rétroaction descriptive | Nouvelle tentative ciblée |
|---|---|---|
| Compter une diagonale, un segment intérieur ou un côté partagé | « Cette ligne fait-elle partie du bord extérieur? » | Suivre le bord d'un nouveau polygone avec le doigt avant de calculer. |
| Donner `7 × 4 = 28 cm²` au lieu du périmètre | « Le produit décrit une surface; quelle longueur additionnes-tu autour? » | Rectangle 6 × 2 cm → `16 cm`. |
| Augmenter un seul côté quand la largeur du rectangle augmente | « Combien de côtés opposés ont cette longueur? » | Rectangle 5 × 3 cm, largeur +1 cm → `16 → 18 cm`, effet `+2 cm`. |
| Écrire `cm²` ou oublier l'unité | « Quelle grandeur trouves-tu : contour ou surface? » | Écrire `P = 18 cm` et identifier l'instrument de longueur. |
| Ajouter les deux côtés intérieurs d'un coin « retiré » sans retirer les côtés extérieurs remplacés | « Repars de la liste des six côtés actuels, pas de la figure précédente. » | L `W=8,H=5,w=3,h=2` → 26 cm par six côtés. |

## 8. Évaluation formative et preuves

- Famille native inchangée `qc-pri-ma-027-ev-01` (`type = paramétrique_controle`), `obj-1`, `crit-1`. Banque de 10 items (`q-001` à `q-010`) : 3 fixes contrôlés et 7 paramétriques déterministes, chacune de ces sept familles d'items avec seed entière, **trois variantes exhaustivement contrôlées** et sélection `seed % 3`.
- Pour tous les paramétriques, **pas de tirage libre**. L'algorithme, les domaines, les contraintes, les exemples instanciés et les deux chemins de correction arithmétiques figurent dans `BANQUE_ITEMS.json` et `PLAN_EVALUATION.md`.
- **Preuve autonome A, `q-009` :** deux potagers rectangulaires, modification d'une largeur; trouver les deux périmètres, l'effet +2d et le justifier.
- **Preuve autonome B, `q-010` :** deux plateformes en L, élargissement du contour total à encoche conservée; trouver les deux périmètres, l'effet +2d et le justifier par les six côtés. Contextes et représentations distincts.
- Aucune note globale ne remplace la vérification **de chacune** des deux preuves en autonomie; conditions dans `evaluation/GRILLE_MAITRISE.md`.

## 9. Remédiation / enrichissement

- Contour non reconnu → ficelle le long de l'extérieur, repères de début/fin, sans intégrer l'intérieur.
- Addition faible → table de longueurs écrites dans une unité commune, addition par paires, puis retrait des couleurs et cases.
- Interprétation de variation erronée → surligner **seulement** les longueurs qui changent et comparer deux sommes.
- Figure concave → tracer les six côtés d'un L et calculer indépendamment par segments et par regroupement.
- **Rappel différé :** à la séance suivante, reconstruire un contour sans modèle; quelques séances plus tard, retrouver le changement `+2d` sur un nouveau rectangle (détails dans `contenu/06_REMEDIATION_ET_TRANSFERT.md`).
- Enrichissement : « un coin supérieur droit plus large modifie-t-il le périmètre? » Réponse conditionnelle **pour cette construction rectangulaire précise** : non si dimensions extérieures restent fixes; ne pas généraliser à toute découpe.

## 10. Accessibilité

- Schémas contrastés et descriptions textuelles équivalentes (rectangle = quatre côtés; L = six côtés listés dans l'ordre). Présenter par matériel manipulable, texte agrandi, lecture orale et écriture mathématique.
- Permettre réponse dictée, clavier, geste de contour, cartes-nombres ou technologie d'assistance. L'objectif évalué est le calcul/interprétation, **pas** la fluidité d'écriture, la dextérité ni le décodage oral.
- Aucun dessin à l'échelle exigé; toutes les mesures nécessaires sont fournies. Utiliser chiffres entiers en cm ou m et expliciter l'unité commune; éviter matériel tranchant, découpes réelles, manipulation imposée ou collecte d'informations personnelles.
- Adapter les modes sans fournir les réponses, déterminer les modalités en amont des deux observations autonomes.

## 11. Critères de sortie

1. Repérer le contour fermé des deux figures, sans segment intérieur ni côté oublié.
2. Établir et vérifier **chaque** périmètre numérique dans l'unité de longueur appropriée.
3. Expliquer précisément quels côtés changent, de combien et pourquoi la différence de périmètre vaut la variation annoncée.
4. Fournir deux preuves satisfaisantes séparées (`q-009` rectangulaire et `q-010` L) avec raisonnement indépendant, pas une seule note ni une récitation.
5. En cas de lacune, remédier à la dimension précise et faire une autre vérification autonome.

## 12. Références pédagogiques et limites

- Sources internes effectivement lues : `CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md`, `GRAPHE_PEDAGOGIQUE_202.json` et les quatre fichiers d'auteur du Kristal source. Aucune modification hors du delta.
- Références externes consultées : Alloprof, « Le périmètre et l'aire des figures planes » (définition du contour et distinction aire, https://www.alloprof.qc.ca/bv/mathematiques/le-perimetre-et-l-aire-des-figures-planes-m1478 ); CAST (2024), *UDL Guidelines 3.0* (variété des moyens de réponse, https://udlguidelines.cast.org/action-expression/expression-communication/ ). Les ressources ne garantissent pas la validité des seuils internes.
- Les exemples, figures à données numériques, interprétations et correcteurs ont été composés localement et testés comme indiqué dans `livraison/VALIDATION.md`. Aucune affirmation de propriété sur les documents externes.
- Revue humaine de pédagogie, difficulté et accessibilité encore requise; aucun essai terrain, certification ou homologation PFEQ.
