# Références et provenance — qc-pri-ma-002

## Sources directement consultées et vérifiées (8 octobre 2026)

1. Archive maîtresse `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, fichiers `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md`. Vérifiés directement dans l'archive source. Portée : exigences internes de construction, contrat de génération, seule nomenclature disciplinaire québécoise; pas une homologation PFEQ.
2. Même archive, `registry/GRAPHE_PEDAGOGIQUE_202.json` : arête sortante `qc-pri-ma-002/requires/qc-pri-ma-001`, aucune autre relation sortante. Les autres arêtes mentionnant `qc-pri-ma-002` sont entrantes et ne donnent aucun droit de modifier ces Kristals.
3. Même archive, `kristals/qc-pri-ma-002/authoring/PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, lus directement : ID, titre, objectif observable, preuve, famille, concepts, préalables et structure YAML/JSON exacts. Aucun `ALIGNEMENT.md` n'est modifié ou redistribué.
4. **Alloprof**, *Les nombres* (Primaire), https://www.alloprof.qc.ca/fr/eleves/bv/mathematiques/les-nombres-1er-cycle-m1737p12 — page d'aide consultée sur le Web le 8 octobre 2026. Elle documente nombre, valeur de position, comparaison et droite numérique; ne prescrit ni les bornes spécifiques 0–9 999 ni la rubrique locale, et n'est pas une source de conformité PFEQ.
5. **Alloprof**, *La valeur de position — 1er cycle*, https://www.alloprof.qc.ca/fr/eleves/bv/mathematiques/la-valeur-de-position-1er-cycle-m1641p12 — consultée le 8 octobre 2026; rappelle unités, dizaines, centaines et conversion par groupements de dix. Aucune copie de fiche, image ou exercice Alloprof dans le livrable.

## Déductions et algorithmes mathématiques (vérifiés par raisonnement)

- Numération décimale : N=1 000M+100C+10D+U; comparer la longueur significative, puis le premier rang différent en partant de la gauche. Ce sont des conséquences arithmétiques du système de position.
- Encadrement entre centaines consécutives `100h < 100h+r < 100(h+1)` pour 1≤r≤99; classement de N, N+10, N+100; rapprochement sur une droite correctement graduée : résultats dérivés, non citations d'une source externe.
- Seeds 0…8 999, générateurs arithmétiques, permutations explicites, variantes et exemples ont été **créés pour ce dossier**. Leur exactitude est testée par calcul entier. Ni apprentissage automatique libre ni arbitrage de réponse par IA utilisé dans la validation.
- Les seuils de la grille (quatre dimensions à 2 dans chacune des deux preuves) sont une **décision éditoriale non étalonnée**, pas une norme publiée ou une mesure psychométrique.

## Production originale et droits

- Textes, scénarios fictifs (bibliothèque, inventaire, serre et bornes), exercices G1–G3, autonomes A1–A4, corrigés, banques paramétriques, algorithmes et rubriques produits pour le Kristal.
- Aucun texte d'éditeur, figure, marque graphique, jeu de données personnel, photographie, musique ou image externe intégrés. Les URL sont uniquement des références bibliographiques; aucun droit de reproduction des sources externes n'est supposé.
- Les métadonnées YAML et champs v1.2 copiés de l'archive appartiennent à la source de workspace du donneur d'ordre; la livraison est un delta destiné à sa fusion, **sans établir indépendamment les droits de redistribution du workspace**.

## Limites

Les vérifications de la génération et de la cohérence numérique ne prouvent pas l'adéquation pédagogique pour un âge ou une classe donnée, la lisibilité pour tous les handicaps ni l'accord de correcteurs; une revue humaine et des essais encadrés sont encore nécessaires avant tout statut qualifié.
