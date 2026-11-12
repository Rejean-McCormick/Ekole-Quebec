# Sources, justifications dérivées, créations et droits — `qc-pri-ma-024`

## Sources internes réellement consultées (fichiers source v1.2)

Les fichiers suivants ont été lus dans l'archive originale `initbundle(1).zip`, dont la racine interne est `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` :

- `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` : protocole diagnostic–modèle–pratique–preuves doubles; mathématiques à corrigés contrôlés; statut non certifié.
- `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` : champs de famille d'évaluation; fixation des seeds, contraintes et solutions, contrôle indépendant.
- `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` : discipline **Mathématique** comme étiquette; ne pas revendiquer la conformité PFEQ.
- `registry/GRAPHE_PEDAGOGIQUE_202.json` : arête sortante unique `qc-pri-ma-024/requires/qc-pri-ma-023`; aucune arête sortante `recommends_before` ni `reinforces`.
- `kristals/qc-pri-ma-024/authoring/PARCOURS.md` et `CONTRAT_PEDAGOGIQUE.json` : métadonnées locales, objectif, concepts, critère, famille et préalable préservés.
- `kristals/qc-pri-ma-024/authoring/ALIGNEMENT.md` et `BRIEF_REDACTION.md` : frontières, titre, discipline, méthodes et modalités de revue; fichiers **non** modifiés dans le delta.

## Références externes vérifiées (consultation documentaire au moment de rédaction)

- **Math Is Fun**, *Reflection*, https://www.mathsisfun.com/geometry/reflection.html : une réflexion construit les sommets à des distances égales **mesurées à angle droit** de l'axe; on relie ensuite les points réfléchis. L'article soutient le principe géométrique mais ne valide pas notre banque d'items. Aucune illustration ni phrase longue copiée.
- **Math Is Fun**, *Line in Geometry*, https://www.mathsisfun.com/geometry/line.html : droite sans extrémités, distinction avec segment et demi-droite. N'autorise aucune redistribution de ses images; non réutilisées.
- **CAST**, *UDL Guidelines v3.0*, « Expression & Communication », https://udlguidelines.cast.org/action-expression/expression-communication/ : supports d'expression variés et technologies accessibles; **ne** certifie **pas** la grille ni les accommodements individuels proposés.

## Mathématiques dérivées et vérifiables sans autorité externe

- Si l'axe est `x=6`, le segment `PP′` doit être horizontal, son milieu d'abscisse 6; pour `P(x;y)`, la seule image répondant à ces deux contraintes est `(12−x;y)`.
- Si l'axe est `y=6`, `PP′` doit être vertical et son milieu d'ordonnée 6; la seule image est `(x;12−y)`.
- Pour les six familles paramétriques, `seed mod n` et `seed // n` fixent les décalages autorisés; les domaines `0..12` empêchent toute position hors quadrillage. La validation indépendante compare milieux, distances et perpendicularité, et teste des cas limites. Les algorithmes et seeds sont documentés dans chaque item JSON.
- Le choix des deux contextes (« panneau » et « frise »), le nombre de sommets, les points retenus et les niveaux M1–M5 sont des **décisions éditoriales internes**, et non une norme ministérielle, une conclusion de recherche expérimentale ni une échelle étalonnée.

## Créations originales et propriété intellectuelle

Tous les énoncés, tableaux, exercices, corrigeries, scénarios, suites de points, scripts de génération/contrôle et rubriques de ce delta ont été rédigés pour ce dossier. Le ZIP ne contient aucune image, musique, vidéo, photographie, extrait substantiel de publication, carte ou matériel tiers à redistribuer. Les droits d'adaptation du dossier dépendent des conditions du projet; **aucune opinion juridique ni garantie exhaustive de non-similarité** n'est affirmée. Il appartient au projet de documenter la licence des futures images ou fichiers externes, si ajoutés.

## Limites et revue

L'exactitude mathématique des coordonnées et paramètres est vérifiée dans `livraison/VALIDATION.md`. La lisibilité réelle de la grille, la différenciation motrice/visuelle, la compréhension des justifications, les seuils de maîtrise et l'accord entre correcteurs doivent être examinés par un humain avant usage décisionnel. Aucun protocole d'homologation PFEQ, aucune certification ni essai en classe n'ont été effectués.
