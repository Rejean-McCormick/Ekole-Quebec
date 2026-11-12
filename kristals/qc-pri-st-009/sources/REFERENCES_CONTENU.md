# Sources, provenance, exactitude et droits — qc-pri-st-009

**Vérification documentaire :** 8 octobre 2026. Ce document distingue **sources consultées**, **raisonnements dérivés et simplifications explicites**, **productions originales**, et **limites**. Aucune source citée n'est une homologation PFEQ. Aucune figure ou texte long externe n'a été recopié.

## 1. Sources consultées/vérifiées (faits)

| Identifiant | Source et adresse vérifiée | Propriété prise en charge | Portée et prudence |
|---|---|---|---|
| S1 | Science World, *Light and Shadows*, https://www.scienceworld.ca/resource/light-and-shadows/ | Trajet lumineux simplifié, obstacle opaque et ombre, comparaison d'états en ne changeant qu'un paramètre. | Une ombre dépend aussi des autres lumières; notre matériel **exclut** les rallonges/prises secteur proposées éventuellement dans la ressource. |
| S2 | NASA Science, *How does light travel?* (Big Idea 2.3), https://science.nasa.gov/big-idea-2-3-intermediate-level-guiding-question/ | Lumière = rayonnement électromagnétique, propagation possible sans milieu matériel, interactions selon les matériaux. | Modèle du rayon rectiligne utilisé uniquement dans un milieu transparent homogène; pas d'enseignement complet de l'optique. |
| S3 | Smithsonian, *Waves in the Air*, https://howthingsfly.si.edu/aerodynamics/waves-air | Le son est une perturbation mécanique transmise à travers l'air ou une matière; le vide n'est pas un milieu sonore. | Résultat de recherche consulté; l'ouverture du site a renvoyé une restriction d'accès au moment du contrôle : ne pas déclarer un contrôle visuel complet de la page. |
| S4 | Science Buddies, *Make a Rubber Band Guitar*, https://www.sciencebuddies.org/stem-activities/rubber-band-guitar | Un élastique en vibration peut générer un son, qui faiblit quand la vibration est freinée; lien à l'air. | Activité référentielle; nos montages, scripts et rubriques sont des productions nouvelles. Ne pas présumer que chaque montage sera audible. |
| S5 | Smithsonian Science Education Center, *How Can We Send a Message Using Sound?*, https://ssec.si.edu/sound | Lien entre source vibrante, interprétation du son et investigation scolaire. | Résultat de recherche consulté; l'ouverture de la page a renvoyé une restriction d'accès : pas de prétention de lecture exhaustive. |

**Lecture de gouvernance vérifiée directement dans le ZIP maître :**

- `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` — objectif, graphe, deux preuves, priorité à la science et à la sécurité.
- `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` — familles, variation encadrée, statut d'examen non certifié.
- `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` — appellation « Science et technologie » comme nomenclature; aucune validation PFEQ.
- `registry/GRAPHE_PEDAGOGIQUE_202.json` — pour `qc-pri-st-009` : `recommends_before` vers `qc-pri-st-001`, aucun `requires` ni `reinforces` déclaré.
- `kristals/qc-pri-st-009/authoring/ALIGNEMENT.md`, `BRIEF_REDACTION.md`, `PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json` — métadonnées et frontières v1.2.

## 2. Raisonnements scientifiques dérivés et simplifications

- Si une source lumineuse et un écran restent fixes et qu'un obstacle opaque s'interpose, une partie de la lumière n'atteint plus la même région : il peut apparaître une zone **moins éclairée**, non forcément noire (dérivé de S1 et S2).
- Si un objet est mis en vibration puis freiné, le son qu'il produit peut diminuer; la relation causale s'appuie sur une propagation mécanique dans l'air (dérivé de S3 à S5), **sans prétendre** que tous les montages sont audibles ou mesurables au décibel près.
- Une seule variable volontairement modifiée permet un contraste explicatif plus clair; contrôler le milieu ambiant ne supprime pas toutes les sources d'incertitude (démarche d'investigation, S1).
- La distinction « fait observé / modèle / inférence / conclusion » et les niveaux de la grille sont des **choix de conception pédagogique internes**, pas un résultat empirique démontré sur ce module.
- « Dans l'air homogène, rayon en ligne droite » est un modèle de géométrie simple, pas une description exhaustive des ondes lumineuses; « son → air → oreille » est une représentation schématique du transfert d'une perturbation mécanique, non un déplacement global de l'air de la source vers l'oreille.

## 3. Productions originales réalisées pour le Kristal

Tous les énoncés, discussions modèle, scénarios de maquette, protocoles A/B adaptés (lampe DEL à piles, théâtre, vibration douce), grilles P1–P5, rubriques, corrigés, tableaux et banques d'items ont été **rédigés pour ce Kristal**, en s'appuyant sur des principes scientifiques généraux. Aucune image, piste sonore, illustration ou transcription externe n'est distribuée dans le ZIP. Aucun droit de redistribution sur les sites liés n'est affirmé : les URLs sont des références, pas des licences accordées. Le nom des organismes est cité à titre d'attribution bibliographique.

## 4. Limites et revue humaine

- Les URLs ont été vérifiées par recherche; S1, S2, S4 ont pu être ouvertes et lues; S3 et S5 nécessiteraient une vérification de lecture manuelle hors restriction.
- Aucun montage matériel n'a été construit physiquement, aucune observation réelle recueillie, aucune sécurité locale auditée et aucun essai d'élève effectué dans cette livraison.
- Le montage de la bande peut être trop discret à l'oreille, et le contraste de l'ombre trop faible selon l'éclairage. Un adulte valide faisabilité, hygiène, allergies, attaches et accessibilité avant utilisation.
- Une revue scientifique/pédagogique humaine doit relire les faits, protocoles, items, variabilité B et critères, puis conduire des essais; **aucune certification, publication ou validation ministérielle** n'est revendiquée.
