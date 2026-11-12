# VALIDATION — livraison qc-pri-ma-025 v1.2

**Date de contrôle :** 8 octobre 2026. **Périmètre strict :** seul `kristals/qc-pri-ma-025/`. **Statut :** contrôles techniques automatisés réussis; contenu pédagogique et mesures réelles **à revoir** par une personne qualifiée avant mise en usage.

## Contrôles effectivement réalisés

- [x] Contrat JSON parsable et toutes clés v1.2 conservées.
- [x] Frontmatter YAML parsable, clé et valeur v1.2 intactes.
- [x] Douze sections du PARCOURS présentes dans l’ordre.
- [x] Identités, objectif et preuve inchangés.
- [x] Préalables et ordre de construction : aucune arête sortante.
- [x] Contrat famille : 13 champs obligatoires renseignés.
- [x] Banque JSON strict : format et IDs exacts.
- [x] 12 items uniques et numérotés de 001 à 012.
- [x] Champs et contenus obligatoires présents dans chaque item.
- [x] Cinq items paramétriques et deux preuves réelles distinctes.
- [x] Semences stables, algorithmes, domaines et exemples détaillés.
- [x] 50 000 essais paramétriques de contraintes, résultats et conversions (10 000 graines × 5).
- [x] Cinq corrigés instanciés contrôlés contre jeux manuels fixes.
- [x] Contrôles arithmétiques fixes et transferts vérifiés.
- [x] Pédagogie : diagnostics≥2, guidés≥3, autonomes≥4, transferts≥2.
- [x] Accessibilité, sécurité, droits et limites renseignés.
- [x] Liens et références locales principales résolus.
- [x] Contrôle final du ZIP : 14 entrées fichiers, noms exactement conformes au manifeste, première entrée `kristals/qc-pri-ma-025/authoring/PARCOURS.md`, aucune entrée parent ni traversée de chemin, fichiers non vides, CRC ZIP lisible, JSON en archive parsable; effectué lors de l'empaquetage final.
- [x] Comparaison avec les fichiers source : 2 remplacements (PARCOURS.md, CONTRAT_PEDAGOGIQUE.json), 12 nouveaux fichiers; simulation de superposition des chemins du delta sur la base extraite, sans modification de la base centrale.

**Détail du contrôle arithmétique :** 10 000 seeds entiers de `0` à `9999` pour chacun des 5 algorithmes paramétriques (50 000 évaluations), plus les seeds de livraison et 3 seeds d'exemples par item. Vérification de toutes les bornes, des différences de repères, des soustractions de tare, des conversions cm/mm et mL/L au moyen de `fractions.Fraction` pour les égalités exactes. Les cinq cas livrés ont aussi été comparés à des résultats attendus fixes : q-003 `20−4=16 cm`, q-004 `230−80=150 g`, q-005 `700−400=300 mL`, q-006 `180−160=20 mm`, q-007 `5×100=500 mL=0,5 L`. Les énoncés fixes q-002, q-009 et les deux transferts ont été confrontés à des résultats connus.

## Limites non résolues et revue humaine impérative

- **Aucune mesure physique faite avec un enfant ni avec les objets réels des épreuves.** Les réponses aux q-010, q-011, q-012 reposent à dessein sur une mesure locale et une grille, pas sur un corrigé numérique inventé.
- **Aucun essai utilisateur, audit formel d'accessibilité ni validation d'appareil** : la tolérance de ±1 graduation est une proposition à régler selon la résolution, le matériel et les pertes de transvasement; l'étalonnage effectif des instruments n'a pas été vérifié.
- **Revue éditoriale et psychométrique nécessaire :** adéquation des consignes à l'âge réel des élèves, clarté du vocabulaire (capacité utile/volume), biais, qualité des adaptations, faisabilité et fiabilité intercorrecteurs. Aucun item n'est « certifié », homologué ou publié.
- **Droits :** textes et cas originaux; BIPM cité par URL sans reprise de figures/photographies. Vérification juridique externe non réalisée; provenance des sources du workspace non auditée au-delà des fichiers consultés.
- **Aucune conformité PFEQ revendiquée** : appellation québécoise conservée seulement.

## Changements proposés à la gouvernance — NON appliqués

1. Documenter formellement dans le schéma commun les sous-champs `critere_id`, `family_id`, `representation`, `role`, `variation_permises` des items : conservés comme extensions JSON compatibles avec le contrat commun, sans modifier la norme.
2. Standardiser un enregistrement de la résolution, de la tolérance et de la mesure de référence locale pour les tâches manipulatoires dans le système d'apprentissage, hors `canon/` et `state/`.
3. Définir un test de validation intercorrecteurs de la grille avant publication, distinct du contrôle JSON/arithmétique.

## Journal du delta

- `authoring/PARCOURS.md` : remplacement complet avec YAML v1.2 inchangé et 12 sections remplies.
- `authoring/CONTRAT_PEDAGOGIQUE.json` : remplacement complet, conservation des champs natifs et ajout des 13 paramètres de famille exigés.
- Six nouveaux modules `contenu/`, trois nouveaux documents `evaluation/`, un fichier `sources/` et deux fichiers `livraison/`.
- Aucun autre ID, registre, norme, contenu canonique, profil LMS, `AGENTS.md` ou `kristal.workspace.json` modifié ou empaqueté.
