# Références, provenance et droits — `qc-pri-da-001`

## 1. Sources vérifiées et périmètre d'utilisation

**Archive source effectivement consultée :** `initbundle(1).zip` contenant le dossier `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Consultée pour ses chemins et son contenu original v1.2 le 8 octobre 2026. Les documents **cités en provenance** sont consultés, mais **non copiés dans le delta** :

| Source du workspace source | Ce qui est repris / vérifié | Statut |
|---|---|---|
| `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` | Une feuille, deux manifestations autonomes, méthode diagnostic→enseignement→pratique, grilles arts/EPS, absence d'homologation PFEQ | lu directement |
| `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` | Champs obligatoires de famille, modes fixes et variations contraintes, items non certifiés avant revue | lu directement |
| `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` | « Danse », discipline conservée; aucune conformité PFEQ revendiquée | lu directement |
| `registry/GRAPHE_PEDAGOGIQUE_202.json` | `qc-pri-da-001` sans arête sortante `requires` ni `recommends_before` ni `reinforces`; arêtes **entrantes** depuis `qc-pri-da-002` et `qc-pri-da-005`, non éditables ici | lu et extrait directement |
| `kristals/qc-pri-da-001/authoring/PARCOURS.md` | YAML, 12 intitulés et métadonnées, objectif et preuve de maîtrise v1.2 | lu, conservé et développé |
| `kristals/qc-pri-da-001/authoring/CONTRAT_PEDAGOGIQUE.json` | JSON natif, `format`, `kristal_id`, `objectif_id`, `concepts`, `preuve_attendue`, `prerequis_bloquants`, `ordre_conseille`, famille existante et métadonnées | lu, enrichi sans changer les invariants |
| `kristals/qc-pri-da-001/authoring/ALIGNEMENT.md` et `BRIEF_REDACTION.md` | Titre, discipline, frontières, exigences et absence d'alignement curriculaire détaillé | lus, protégés, non livrés |

**Source externe vérifiée :** CAST, *Universal Design for Learning Guidelines*, version 3.0 (2024), section **Action & Expression**, https://udlguidelines.cast.org/action-expression/ (consultée le 8 octobre 2026). Les options de réponse, de mouvement et de communication soutiennent le choix éditorial d'adaptations. **Limite :** la ressource ne valide ni les seuils ni l'efficacité du présent module; ses formulations, images et graphiques ne sont pas reproduits.

**N'ont pas été vérifiés ici** : normes médicales/biomécaniques individuelles, instruments psychométriques, âge scolaire précis, homologation par un ministère, validité clinique d'un geste et licences de pistes musicales.

## 2. Raisonnements dérivés, explicitement non attribués

- Choisir **quatre étapes**, **deux types de mouvements** et **deux passages** concrétise la preuve générale de maîtrise du workspace; ce sont des **opérationnalisations éditoriales** et non des prescriptions ministérielles.
- Permettre les gestes de faible amplitude, la posture assise et les repères de communication reflète la priorité au choix, à l'accessibilité et à l'observation d'une compétence plutôt qu'à la mesure brute d'amplitude. Ce n'est pas un avis médical.
- Dissocier **intention de l'élève** et **interprétation du spectateur** évite de sanctionner le style ou une expérience intime.
- Les seuils et critères 0–2 de la grille sont proposés par le rédacteur; ils n'ont pas été étalonnés ni évalués par une recherche expérimentale.

## 3. Productions originales dans le delta

- Définitions opérationnelles, descriptions, exemples « fenêtre et nuage » et « petit phare », contre-exemples, diagnostics, modelage et exercices G1–G3.
- Pratiques A1–A4; transferts « bibliothécaire du futur » et « constellation »; thèmes d'évaluation « feuille dans le vent » et « atelier de mécanismes ».
- Tous les 10 énoncés fixes, rétroactions, conditions observables, rubriques, seuils et fiches de consignation.

Ces textes sont **rédigés pour cette livraison** : aucun matériel musical, vidéo, image, photo d'enfant, chorégraphie tierce, extrait d'œuvre ou code source externe n'est intégré. Le fait d'avoir écrit des contenus originaux ne constitue pas une garantie juridique exhaustive d'absence de similarité; la réutilisation externe relève des conditions du projet et d'une éventuelle revue des droits. Le consentement à toute captation doit être demandé séparément; aucune captation n'est requise.

## 4. Validation et précautions

- Vérification documentaire des champs de gouvernance et des identifiants; qualité et cohérence textuelles contrôlées par des assertions techniques décrites dans `livraison/VALIDATION.md`.
- **Non testé avec des enfants** : lisibilité réelle, effet des consignes, équité des adaptations, seuils de maîtrise et sécurité en classe nécessitent revue de spécialistes et essais supervisés.
- Aucune image ni musique à licencier dans les 14 fichiers. Toute future illustration ou bande sonore ajoutée devra faire l'objet d'une provenance et d'un droit d'utilisation documentés.
