# Provenance, vérification et droits — `qc-pri-ma-021`

## Sources internes effectivement consultées (fichiers de l'archive source v1.2)

- `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` : décisions sur le cadre du primaire comme nomenclature, objectifs autonomes, diagnostic, absence de gate PFEQ, deux manifestations indépendantes de maîtrise.
- `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` : champs de famille, variation déterministe, seeds, solutions vérifiables, réviseur humain nécessaire.
- `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` : discipline « Mathématique », identité `qc-pri-*` interne, absence de correspondance officielle garantie.
- `registry/GRAPHE_PEDAGOGIQUE_202.json` : consultation du sous-ensemble des relations de `qc-pri-ma-021` : aucune relation **sortante** (`requires`, `recommends_before`, `reinforces`) pour cette feuille; entrées vers ce Kristal depuis d'autres feuilles non modifiées et non transformées en prérequis. Registre non livré ni altéré.
- `kristals/qc-pri-ma-021/authoring/PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md` et `AGENTS.md` : objectifs, limites, identifiants et contraintes de propriété; seul `PARCOURS.md` et `CONTRAT_PEDAGOGIQUE.json` sont remplacés dans le delta.

**Nature des sources :** documents internes fournis dans le ZIP de travail, consultés et nommés ici; pas de vérification sur un site externe ni de revendication de statut ministériel. La frame renvoie notamment à des sources génériques de pédagogie; **aucune lecture ou vérification directe de publications EEF, IES/WWC ou CAST n'est revendiquée** dans cette livraison. Ne pas transformer ces noms en citations bibliographiques contrôlées.

## Raisonnements et résultats dérivés (vérifiables, pas des citations externes)

- Sur un plan de points, les transformations unitaires sont les additions entières `E:(1,0)`, `O:(-1,0)`, `N:(0,1)`, `S:(0,-1)`; `E3` est trois applications successives. Convention éducative explicitée dans les leçons; cohérence vérifiable par calculs entiers.
- Borne de grille : chaque coordonnée intermédiaire doit être entre 1 et 6, et aucun point de l'ensemble d'obstacles ne peut être traversé. La seule égalité des coordonnées finales ne démontre ni le chemin parcouru ni sa validité.
- Pour un trajet sans obstacle avec directions orthogonales et escale, la somme des distances de Manhattan entre départ–escale et escale–arrivée borne le nombre de pas; si la route construite atteint cette borne, elle est minimale.
- Pour la route robot fictive, les six points interdits ferment le passage direct aux hauteurs y=4,5,6 entre x=2 et x=5. Tout chemin de longueur 7 évitant ces points doit traverser au plus y=3; la route `S2 E3 N2` y parvient exactement. Voir les vérifications arithmétiques consignées dans `livraison/VALIDATION.md`.

## Créations originales et droits

- Texte de cours, tables, exemples, contre-exemples, contextes fictifs bibliothèque et jardin, formulations des items, situations et grilles : **rédaction originale pour cette livraison**. Aucune image tierce, carte réelle, capture d'écran, marque ou donnée personnelle n'est incluse.
- Les énoncés d'exercice et coordonnées sont construits pour le Kristal; les faits mathématiques élémentaires n'impliquent pas de reproduction de pages tierces. Les éléments structurels et identifiants de la frame v1.2 proviennent de l'archive fournie par l'utilisateur.
- Aucune licence externe spécifique n'est déduite de la simple présence des fichiers source : le statut juridique du projet maître et l'autorisation de redistribution externe nécessitent une revue humaine. **Aucun droit supplémentaire ou citation de tiers n'est inventé.**
- Aucun alignement officiel, homologation, conformité PFEQ, qualification du canon, publication ou déploiement n'est affirmé.

## Limites de preuve

Les contrôles de calcul et de format attestent seulement la cohérence technique et arithmétique des exemples testés. Ils ne démontrent ni efficacité pédagogique avec des élèves ni validité universelle des seuils, des traductions en braille, de l'utilisabilité des supports, ni concordance avec une norme scolaire officielle.
