# VALIDATION ET JOURNAL DE LIVRAISON — qc-pri-ma-015

**Livraison :** delta seul `qc-pri-ma-015_livraison_v1.2.zip` à extraire à la racine du workspace `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. **Base :** frame `1.2.0` trouvée dans l'archive source fournie. **Statut :** contrôles automatiques structurels et arithmétiques réussis; **revue humaine requise**, pas de publication ou de certification revendiquée.

## Périmètre et changements réellement produits

- **Deux fichiers de frame remplacés** : `authoring/PARCOURS.md` (frontmatter YAML conservé à l'identique, 12 sections intégralement rédigées) et `authoring/CONTRAT_PEDAGOGIQUE.json` (toutes clés identitaires et familles v1.2 maintenues, champs du générateur complétés et statuts rédactionnels actualisés).
- **Douze nouveaux fichiers** : six contenus, trois évaluations, un document de références, un manifeste et ce rapport de validation.
- **Aucun** `kristal.workspace.json`, `AGENTS.md`, `ALIGNEMENT.md`, fichier de registre, gouvernance, canon, docs, state, runtime ni autre Kristal inclus ou modifié. Aucun doublon de la racine `Frames_202_...` dans le ZIP.

## Contrôles effectivement exécutés

1. Extraction et lecture des neuf ressources internes demandées dans le workspace v1.2 de l'archive fournie, vérification des deux `requires` de `qc-pri-ma-015` dans le graphe; ressources répertoriées avec SHA-256.
2. **235 assertions avant emballage** dans `validate_package.py` : préservation de l'en-tête YAML, de ses 12 sections et de l'identité; contrôle de conservation des champs initiaux et de la famille JSON; présence des champs d'évaluation, unicité et numérotation des 12 items; traçabilité des deux contextes de maîtrise.
3. **27 variantes numériques** couvrant les sept items paramétriques contrôlées indépendamment par `fractions.Fraction` et par recomptage des cases; algorithme reproductible `seed % longueur_du_domaine`, valeurs bornées et seed enregistrées. Deux corrigés finaux vérifiés : `1,26=1+2/10+6/100` et `0,84=8/10+4/100=84/100` (84 cm si l'unité est le mètre). Pas de calcul par tirage IA libre.
4. Couverture structurelle vérifiée : définitions et contre-exemples, D1/D2, G1/G2/G3, A1–A4, T1/T2, deux preuves distinctes et grille à quatre axes. La présence de ces marqueurs ne remplace pas une validation didactique humaine.
5. Contrôle de provenance/droits **documentaire** : schémas textuels et scénarios créés ici; fichiers tiers et images externes non inclus; URL externes de la gouvernance citées comme non reconsultées. Ceci n'est **pas** un audit juridique de droits externes.
6. **Contrôle final du ZIP :** prévu et exécuté dans le même script après rédaction de ce rapport : exactitude de 14 chemins relatifs sous `kristals/qc-pri-ma-015/`, taille non nulle, première entrée sous cette racine, aucune remontée `../` ni chemin absolu, trois JSON stricts analysables et contrôle CRC de l'archive. Le résultat concret est imprimé par le script et vérifié avant restitution.

## Points à revoir humainement AVANT qualification

- Enseignant ou spécialiste de didactique : adéquation du niveau d'explication, âge cible selon parcours local, clarté des quantités et du langage français québécois; tester les erreurs probables auprès d'apprenants.
- Responsable des évaluations : distinction réelle de M1 et M2 dans l'administration, absence d'exposition préalable aux corrigés, critères de notation et seuils sur cas représentatifs.
- Accessibilité : rendu tactile/numérique fiable des grilles 10 × 10 et de la droite en centièmes, compatibilité lecteur d'écran, scripteur sans indices et justice des adaptations.
- Examen des droits/diffusion : vérifier les licences des supports que l'intégrateur pourrait ajouter après fusion; aucun emprunt d'images/licences externes revendiqué ici.
- Intégration technique : vérifier la résolution des liens au LMS et les règles d'état du workspace; aucune exécution sur un Framework de production, aucun test avec des élèves ou plateforme LMS réelle.

## Propositions hors périmètre (non appliquées)

1. Ajouter ultérieurement au schéma central une fonction de vérification rationnelle des valeurs et des représentations en cases pour familles paramétriques, avec corpus fini et revue humaine.
2. Ajouter un champ de collecte LMS pour l'aide conceptuelle vs la simple transcription technique, afin d'appliquer rigoureusement la décision d'autonomie.
3. Prévoir une représentation accessible canonique des grilles et droites, associée au même nombre de centièmes et non à une image non décrite.

Ces propositions ne changent ni le registre, ni la gouvernance, ni aucun autre dossier.
