# Validation de livraison — `qc-pri-ap-006` v1.2

## 1. Portée et source
**Livré :** delta de 14 fichiers au seul emplacement `kristals/qc-pri-ap-006/`. **Source contrôlée :** le dossier v1.2 original, accessible sous `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` à l'intérieur de l'archive transmise `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip`; **le fichier ZIP indépendant nommé `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis.zip` ne se trouvait pas comme fichier séparé.** Aucune archive source substitutive inventée. Les deux fichiers `authoring/` sont remplacés intégralement, les douze autres ajoutés. Les originaux de l'archive source n'ont pas été édités.

## 2. Contrôles automatisés locaux effectivement réalisés par le script de construction
- Lecture/parsing JSON du graphe et du contrat de base; cohérence des liens sortants `requires/qc-pri-ap-003`, `recommends_before/qc-pri-ap-004`, `reinforces/qc-pri-fr-020`.
- Validation du YAML frontal du parcours (mêmes clés/valeurs que la base pour les métadonnées héritées) et des **12 rubriques numérotées**; objectifs textuels `obj-1`, preuve `crit-1` et titre identiques à la base.
- Comparaison des champs d'origine dans le contrat JSON et dans son unique famille : aucun champ natif supprimé, aucune identité ou lien changé; ajout des 13 champs de famille requis par `GENERATEUR_ET_EXAMENS.md`.
- Parsing JSON des trois fichiers `authoring/CONTRAT_PEDAGOGIQUE.json`, `evaluation/BANQUE_ITEMS.json` et `livraison/MANIFEST.json`; format banque strict `qc.learning-item-bank/1.0`.
- Banque de **10 items** `q-001` à `q-010` sans doublon, tous liés à `obj-1`, `crit-1` et `qc-pri-ap-006-ev-01` avec tâches, réponses observables/rubriques, critères, rétroaction, difficulté, limites de variation et statut `a_revoir`. Deux preuves distinctes `q-009/q-010` avec public, action et vérification par un pair non informé.
- Contrôles rédactionnels par présence de deux exemples, deux contre-exemples, deux diagnostics, trois essais guidés, quatre autonomies, deux transferts, grille 0–3, protocoles de pairs, sécurité, accessibilité et droits. Il s'agit de **vérifications structurelles et textuelles**, pas d'une expérience pédagogique avec élèves.
- Vérification des 14 chemins autorisés à la racine interne du ZIP, premier chemin sous `kristals/qc-pri-ap-006/`, fichiers non vides, manifeste exhaustif, absence de chemins absolus ou de `../`, absence de tout autre workspace et absence de modification des répertoires centraux. Test d'intégrité CRC du ZIP.

## 3. Contrôles humains non réalisés — limites explicites
- **Non réalisé :** essai de compréhension sur pairs réels; aucune réponse présentée dans les exemples n'est une observation collectée. On ne peut pas conclure que ces dix items ont des résultats fiables en classe.
- **Non réalisé :** double cotation indépendante de productions artistiques, étude de fiabilité inter-évaluateurs ou calibrage des quatre dimensions et du seuil 2.
- **Non réalisé :** test d'usage des moyens tactiles, du zoom, de lecteurs d'écran et des limitations motrices auprès de personnes concernées; niveau d'accessibilité reste à apprécier en situation.
- **Non réalisé :** contrôle juridique d'affichage public, de consentement local ni essai d'intégration du moteur v1.2 / LMS. Des matériels graphiques finaux devront être relus avant diffusion.
- **Non réalisé :** audit externe des études ou citations EEF, IES/WWC, CAST; aucune revendication d'homologation PFEQ. **Statut final :** contenu rédigé et vérifié techniquement, `a_revoir` / revue humaine obligatoire, non « publié », « certifié » ou « homologué ».

## 4. Points proposés à une revue humaine
1. Faire produire les deux affiches A/B par quelques apprenants et soumettre les versions à des pairs inconnus du brief; noter les confusions et le temps requis.
2. Calibrer par plusieurs évaluateurs l'interprétation de D2 (message compris après révision) et D4 (preuve fidèle du test), sans jugement de préférence esthétique.
3. Réviser les briefs pour jeunes lecteurs, personnes dyslexiques, déficiences visuelles et besoins moteurs; confirmer la conservation du pouvoir décisionnel de l'apprenant.
4. Confirmer matériel sécurisé et droits relatifs aux images/affichages dans chaque implantation; ne pas collecter de données personnelles des pairs.

## 5. Propositions de structure (NON appliquées)
- Ajouter dans un prochain schéma central un champ `preuves_distinctes_requises` liant explicitement q-009 et q-010 ainsi qu'un protocole anonymisé de test pair.
- Documenter un type normé `rubrique_observation_plastique` et les accommodations permises par item; laisser ces propositions à la gouvernance, sans toucher au registre ni aux bases centrales dans ce delta.
