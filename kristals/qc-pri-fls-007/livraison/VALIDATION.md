# Validation du delta — `qc-pri-fls-007`

**Statut :** rédaction complète soumise à revue pédagogique humaine; aucun examen homologué ni certifié. Les résultats ci-dessous proviennent de l’exécution effective du script local de prévalidation et du test du ZIP.

## Contrôles de livraison

- **550 assertions préarchivage réussies**, zéro échec : filetree 14, source v1.2, conservation exacte des caractères YAML de tête, identifiants et champs d’origine JSON, douze sections, graphe, dix items et deux preuves de maîtrise indépendantes.
- **Faits et corrigés :** vérification de plus de 40 ancrages textuels explicitement présents dans les scripts sources, de la distinction 10 h / 10 h 30 et des faits essentiels au jardin. Le rapprochement sémantique de toutes les variantes rédigées par des apprenants **n’a pas été exécuté** : revue humaine requise.
- **Liens et accessibilité :** objectif, critère, famille, parcours, plan et grille recoupés; conditions d’accès sensoriel et statut des droits contrôlés par présence de mentions explicites.
- **Simulation de fusion :** exactement 2 fichiers authoring remplacés, 12 fichiers nouveaux; tous les autres fichiers originaux du dossier ont gardé leur SHA-256.
- **Contrôle ZIP :** après archivage, lecture de tous les fichiers, CRC, manifeste et absence de chemin dangereux vérifiés (résultat rapporté à la génération).

## Risques et limites ouverts

- Scripts oraux conçus éditorialement; débit, intelligibilité et équilibre des deux sources à revoir en situation réelle avec des élèves de français langue seconde.
- Les rubriques reposent sur des choix internes non étalonnés; vérifier fiabilité de jugement entre correcteurs et recevabilité des reformulations alternatives.
- Les accommodements sensoriels et linguistiques nécessitent une décision humaine, notamment si le script oral B est présenté sous forme transcrite.
- Aucun essai terrain, aucune observation d'élève, aucune revue juridique complète ni qualification PFEQ effectués.

## Revue humaine à planifier

- **Linguistique :** adéquation du vocabulaire FLS, équité face aux accents légitimes, absence d'ambiguïtés dans les réponses et scripts oraux.
- **Pédagogique :** progression des aides, pertinence des 10 items, capacité de transferts réellement distincts, grille S/F/R/T/A non compensatoire.
- **Accessibilité :** modalités écrites/orales ou communication assistée, accommodations non directives, protection de la vie privée et consignes inclusives.
- **Provenance :** vérifier les droits de tout futur extrait réel; le lot n'intègre aucun média ni texte tiers.

## Propositions structurantes — non appliquées aux fichiers centraux

- Prévoir dans une future révision centrale un champ standard `message_mode` (`ecrit` / `oral_script`) et un champ de décision d'accommodation garantissant la traçabilité des deux sources dans une passation adaptée.
- Prévoir un schéma de correction distinguant faits invariants, paraphrases équivalentes, provenance et inventions plutôt qu'une correction par chaînes identiques.
- Maintenir ces propositions dans le présent rapport; **ne pas modifier** `registry/`, `governance/`, `canon/`, `runtime/`, `state/` ou d'autres Kristals.
