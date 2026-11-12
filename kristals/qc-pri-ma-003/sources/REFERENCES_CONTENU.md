# Provenance du contenu, vérifications et droits — qc-pri-ma-003

## Sources **effectivement vérifiées dans l'archive source fournie**

L'archive disponible `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip` contient le dossier maître `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Les textes ci-dessous ont été **lus dans cette archive**, sans réécriture ni dépôt de ces sources dans le delta :

1. `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` — autorité du parcours, deux preuves, autonomie, frontières Québec.
2. `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` — treize champs de famille, seed stable, corrections contrôlées, statut de qualification.
3. `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` — discipline « Mathématique » et restriction de correspondance PFEQ.
4. `registry/GRAPHE_PEDAGOGIQUE_202.json` — relation sortante `qc-pri-ma-003/requires/qc-pri-ma-002`, aucune relation sortante `recommends_before` / `reinforces` du Kristal.
5. `kristals/qc-pri-ma-003/authoring/PARCOURS.md` — YAML/12 sections originales et intention centrale.
6. `kristals/qc-pri-ma-003/authoring/CONTRAT_PEDAGOGIQUE.json` — objectif `obj-1`, preuve cible, concepts, famille `qc-pri-ma-003-ev-01`, autres métadonnées natives.
7. `kristals/qc-pri-ma-003/authoring/ALIGNEMENT.md`, `authoring/BRIEF_REDACTION.md` — étiquette disciplinaire, mandat, limites.
8. `governance/Norme_Pedagogique_Autonome_v1.2/REFERENCES_EVIDENCE.md` — recense des pistes EEF/IES/CAST pour le design; leur existence dans le **fichier interne** est constatée, **sans prétendre avoir ouvert ni vérifié les pages externes**.
9. `kristals/qc-pri-ma-003/kristal.workspace.json`, `sources/source-catalog.json` — consultés pour confirmer l'identité du workspace et le catalogue de sources vide. Ces fichiers ne sont ni modifiés ni distribués ici.

## Raisonnements mathématiques dérivés et vérifiés localement

Les équivalences `1 D = 10 U`, `1 C = 10 D = 100 U`, `100H+10T+U = 100H+10(T−1)+(U+10)` (si T≥1), et `100H+10T+U = 100(H−1)+10(T+10)+U` (si H≥1) sont des conséquences arithmétiques de la définition du système décimal, pas des citations à un auteur externe. Les corrigés d'items et les exemples de seeds découlent de ces identités; les scripts de validation arithmétique sont décrits par les règles et résultats dans `livraison/VALIDATION.md`.

## Productions originales de cette livraison

Les démonstrations (274 et 308), erreurs illustratives, activités, contexte fictif de bibliothèque, mosaïque, grille descriptive, phrases de rétroaction et gabarits d'items sont **rédigés pour ce delta**; ce ne sont pas des extraits d'un manuel. Les textes de la gouvernance sont **référencés**, pas copiés comme fichiers livrés. Les symboles C/D/U sont des conventions mathématiques élémentaires.

## Droits et vérifications non réalisées

- Aucun visuel, photographie, dessin tiers, police, voix, texte protégé, marque ni contenu d'élève n'est embarqué. Le matériel est **décrit**, non reproduit de ressources commerciales.
- Les licences et droits des **documents maîtres fournis** ne sont pas déterminés par le présent travail. L'auteur du workspace devra vérifier ses droits de redistribution séparément; ce delta n'accorde aucune licence sur l'archive maîtresse.
- Les pages externes mentionnées dans `REFERENCES_EVIDENCE.md` n'ont pas été consultées directement pour cette livraison; ne pas leur attribuer de citations précises, de permissions ou une approbation du cours.
- La validation locale confirme l'arithmétique et la présence des fichiers; elle ne remplace pas revue humaine de l'enseignement, essai avec des élèves ni validation du cadre d'exécution.
