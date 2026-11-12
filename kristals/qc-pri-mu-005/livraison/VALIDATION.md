# Validation de livraison — `qc-pri-mu-005`

**Statut :** rédaction complétée et tests documentaires/techniques réussis; jugement humain encore nécessaire. Ce delta ne prétend ni publier le Kristal ni certifier une prestation vocale.

## Périmètre fixe

- Exactement 14 fichiers, exclusivement sous `kristals/qc-pri-mu-005/` : 2 remplacements des fichiers `authoring/` et 12 nouvelles pièces pédagogiques.
- Aucun changement du graphe, de la gouvernance, des autres Kristals, de la documentation canonique, du runtime ni des métadonnées centrales.
- Objectif, préalables, discipline, intitulé, preuve, famille et identifiants sont conservés du workspace maître v1.2.

## Contrôles exécutés

- **7912 assertions préarchivage réussies** avec vérification Python (fichiers, YAML, JSON, invariants source, famille, banque de 10 items, deux preuves, contenu, sécurité, accessibilité, droits et liens); 0 échec.
- **YAML** : champs originaux conservés et champs immuables identiques, 12 rubriques numérotées et non vides.
- **Contrat JSON** : famille v1.2 conservée, champs requis enrichis; objectif, preuve et préalable `qc-pri-mu-001` inchangés.
- **Banque** : dix items `q-001` à `q-010` distincts, consignes/stimuli/réponses/rétroactions présents, chacun fixe et `a_revoir`. Les deux preuves utilisent des chants et contours originaux différents.
- **Contrôle des supports** : cinq unités et deux hauteurs relatives pour chacune des quatre phrases originales, selon le script de vérification. La qualité vocale en situation réelle n’est pas testée.
- **Fusion simulée sur l’index du ZIP source** : sur 7322 fichiers originaux du workspace, exactement 2 remplacés, 12 ajoutés et 7320 fichiers préexistants protégés conservés avec SHA-256 identique; 0 suppression. Aucun workspace central modifié.
- **Provenance et droits** : références internes et externes contrôlées; pas d’audio ni de partition tierce incluse. Aucune garantie juridique exhaustive.
- **Archive ZIP** : contrôle final du nombre, des chemins, CRC, absence de répertoires englobants et cohérence du manifeste après la création (résultat annoncé par le script).

## Limites et contrôles non exécutables dans ce lot

- Aucun essai avec enfant, aucune vérification physique d’une tessiture ou d’une respiration personnelle, aucune validation orthophonique ni mesure de fidélité des évaluateurs.
- La bonne interprétation de « diction reconnaissable » varie avec l’accent et les besoins; la grille doit être testée pour éviter des biais d’accessibilité.
- Les deux chants originaux ont été écrits pour le projet; une revue juridique d’originalité exhaustive n’a pas été faite. Aucun audio tiers ni enregistrement d’élève n’est inclus.
- Aucun alignement détaillé au Programme de formation de l’école québécoise ni processus de reconnaissance ministérielle n’a été demandé ou accompli.

## Revue humaine nécessaire

1. Pédagogie musicale : motifs originaux, diction, contours 1/2, critères d’indépendance et nuances non esthétiques.
2. Santé et accessibilité : instructions vocales sûres pour les élèves concernés, accommodations de hauteur, souffle, audition, expression, droit d’arrêt; décision clinique réservée aux professionnels.
3. Évaluation : cotation M1–M5, biais de timbre et d’accent, validité des deux contextes et essai interévaluateurs.
4. Droit et vie privée : chansons réellement originales pour l’usage prévu, absence de droits tiers à mobiliser, consentement si une captation est envisagée.

## Propositions de structure centrale (aucune modification effectuée)

- Prévoir à terme un champ standard d’accessibilité vocale par famille (`modalites_adaptables` et `conditions_arret`), distinct du critère de compétence, à soumettre au propriétaire du schéma.
- Prévoir un registre local des preuves de performance audio facultatives avec consentement, hors canon et hors fichier des savoirs.
- Conserver deux épreuves de transfert et une procédure de revue humaine avec versionnage des rubriques avant toute qualification sommative.
