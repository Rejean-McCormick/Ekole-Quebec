# Journal de livraison et validation — `qc-pri-st-002`

**Statut :** contenu rédigé et tests techniques documentaires exécutés, revue humaine requise; revue humaine requise avant usage décisionnel. Aucune publication, certification, homologation ou validation réelle d'expérimentation n'est revendiquée.

## Delta et identité

- **14 fichiers exclusivement** dans `kristals/qc-pri-st-002/` : 2 fichiers `authoring/` remplacés intégralement, 12 fichiers ajoutés.
- Champs YAML v1.2 du parcours préservés textuellement; identité, titre, objectif, `qc-pri-st-001`, famille native et graphe non modifiés.
- La famille native `generee_sous_contraintes` reçoit les champs manquants, mais la banque de 10 items utilise uniquement un **corpus fixe/scénarisé contrôlé**, sans génération par IA libre ou chiffres aléatoires.
- Deux preuves autonomes indépendantes : étalement sur deux papiers et largeur d'ombre selon une distance, plans seulement; aucune valeur expérimentale inventée.

## Contrôles réellement réalisés

- **574 assertions préarchivage réussies** par un script Python effectivement exécuté; aucune anomalie préarchivage. Contrôle du YAML source préservé octet pour octet, des 12 rubriques, des champs canoniques JSON, de la famille native, des liens, 10 énoncés et rubriques, des deux épreuves, des sources/droits et mentions d'accessibilité/sécurité.
- **Trois fichiers JSON** (`authoring/CONTRAT_PEDAGOGIQUE.json`, `evaluation/BANQUE_ITEMS.json`, `livraison/MANIFEST.json`) ont été décodés sans erreur; **10 items** uniques numérotés `q-001..010`, dont **deux preuves** `q-009` et `q-010` à six critères observables.
- **Sélection contrôlée :** corpus de scénarios fixe, aucune génération libre, aucune génération numérique paramétrique prétendue. Corrigés de protocoles vérifiés structurellement : variables, unités, moments, tableaux vides et limites; leur validité pédagogique réelle demeure à revoir.
- **Simulation de fusion :** 2 remplacements authoring autorisés, 12 nouveaux fichiers, aucun autre fichier source du Kristal modifié (hash SHA-256 comparé).
- **Sources et droits :** deux références externes et sources internes consignées, aucune œuvre musicale, image, vidéo ou donnée d'élève incluse; audit juridique exhaustif non réalisé.
- **Vérification ZIP en sortie :** archive écrite et testée, 14 chemins complets sans parent, intégrité CRC et contenu comparé aux fichiers de sortie (contrôle détaillé lors de la construction).


## Revue humaine nécessaire

1. **Science :** vérifier les limites de comparabilité et l'instrumentation des scénarios, la pertinence des deux hypothèses et l'absence de prétention causale excessive.
2. **Pédagogie et psychométrie :** tester en situation la clarté, l'autonomie des plans et la fidélité de la grille M1–M6 entre correcteurs.
3. **Sécurité :** approuver localement les manipulations facultatives avant toute exécution, la lampe LED et la prévention des glissades avec eau.
4. **Inclusion et droits :** examiner l'accès pour modes de communication divers; vérifier l'absence de médias externes ajoutés ultérieurement.

## Limites non résolues

Pas de données mesurées, d'essai de laboratoire, de simulation empirique fiable, de validation psychométrique, de certification externe ou de conformité PFEQ. Une correction sémantique humaine demeure indispensable, même si les JSON, champs et fichiers sont exacts.

## Propositions sans modifier la structure centrale

- Ajouter plus tard au générateur interne un champ de **validité de mesure** (`unite`, `moment`, `instrument`, `regle_bord_de_mesure`) pour contrôler les scénarios scientifiques.
- Prévoir un **journal des adaptations d'accès** séparé des notes de maîtrise, ainsi qu'une procédure de revue de sécurité avant manipulation.
- Maintenir la distinction dans les évaluations entre **planification testable** et **observations recueillies**; ce delta n'impose aucune modification au registre ou aux bases centrales.
