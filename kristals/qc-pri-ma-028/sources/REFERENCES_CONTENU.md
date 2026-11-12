# Références, provenance et droits — `qc-pri-ma-028`

## Documents de base v1.2 effectivement lus (autorité interne)

Les fichiers suivants ont été lus directement dans l'archive maîtresse `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis.zip` :

- `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` : méthode commune, deux preuves de maîtrise, contrôle mathématique des paramètres et absence de certification IA.
- `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` : champs des familles, modes fixe/paramétrique, reproductibilité, contrôles de solution, validation humaine.
- `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` : appellation **Mathématique**, aucune conformité détaillée au PFEQ induite.
- `registry/GRAPHE_PEDAGOGIQUE_202.json` : deux arêtes de préalables `requires` sortantes, vers `qc-pri-ma-023` et `qc-pri-ma-025`; aucun ordre conseillé sortant ni renforcement sortant.
- `kristals/qc-pri-ma-028/authoring/PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md` : titre, objectif, preuve, famille, frontières de rédaction; identités et liens préservés dans la livraison.

**Sources externes :** aucune source externe n'a été indispensable ni consultée pour établir les calculs élémentaires de ce lot; les mentions générales EEF, IES/WWC ou CAST dans le parcours d'origine sont reprises **comme références du workspace source**, non comme publications recherchées, relues ou dont des extraits seraient ici utilisés. Ne pas les qualifier de « vérifiées » dans ce lot.

## Justifications mathématiques dérivées (règles élémentaires contrôlables)

1. Une union de cases carrées entières et disjointes a pour aire la somme de leurs aires. En unités non métrées, c'est le nombre de cases `#` (une unité carrée chacune).
2. Pour un rectangle plein de `h` rangées et `w` colonnes : `h×w` cases, vérifiable par `w+w+...` (`h` termes).
3. Les cases d'une figure composée peuvent être groupées **sans recouvrement**, ou comptées par complément dans un rectangle englobant. Contrôles indépendants : `S = somme(largeurs_rangees)` et `S = W×H − nombre_de_points`.
4. Si chaque case carrée a un côté de `c cm`, son aire est `c² cm²`; aire totale `S×c² cm²`. Avec `c=2`, `c²=4`, et non 2. Sans donnée de côté, aucune unité métrique ne peut être déduite d'un dessin arbitraire.
5. Pour un L, le coin commun de deux bandes est compté deux fois si les deux bandes entières sont additionnées. Il faut retirer la case commune ou former des morceaux disjoints.

Les règles ne sont pas des citations littérales d'une publication extérieure; elles sont appliquées et testées dans les instances de cette livraison. Les cas 001–010 et les tableaux d'instances sont créations pédagogiques.

## Productions originales et régime des droits

Les grilles textuelles en `#`/`.`, scènes de panneau, mosaïque, étagère, tapis et jardinière, exercices, exemples et contre-exemples, grilles critériées, algorithmes d'indexation par graine et textes de rétroaction ont été rédigés pour le présent Kristal. Aucun fichier d'image, de musique, de vidéo, de photo, de matériel commercial, ni extrait protégé d'une œuvre extérieure n'a été reproduit dans le ZIP. Les sources de gouvernance et des autres Kristals ne sont **pas** livrées ni recopiées dans leur intégralité.

Les modalités de distribution ultérieure et les licences applicables à des ajouts futurs doivent être vérifiées par le titulaire du workspace. Originalité éditoriale ne signifie ni homologation ni garantie légale exhaustive.

## Limites

Une vérification automatisée des égalités arithmétiques et des chemins ne mesure pas la clarté en classe, l'équité culturelle et langagière, l'accessibilité effective ni la validité pédagogique réelle. Une revue humaine des consignes et des corrigés est nécessaire avant usage décisionnel.
