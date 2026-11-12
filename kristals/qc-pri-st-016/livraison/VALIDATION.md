# VALIDATION — delta `qc-pri-st-016` (v1.2)

**État :** delta créé, contrôles techniques exécutés; `a_revoir` pour chaque item. **Non qualifié / non publié / non certifié**, pas d'homologation PFEQ.

## Contrôles réellement réalisés sur les sources et fichiers avant empaquetage

- **132 assertions techniques réussies**, avec script local `qa_st016.py` (script d'audit **non inclus** dans le ZIP). Contrôle indépendant par parsing Python JSON, YAML (`yaml.safe_load`) et inspection du graphe original.
- YAML d'origine **strictement identique** dans ses clés/valeurs (frontmatter conservé); **12 rubriques** dans l'ordre 1 à 12; objectif `obj-1`, preuve `crit-1`, famille v1.2 intactes.
- Contrat : tous champs originaux conservés; seuls les statuts de rédaction/revue ont évolué; famille originale enrichie de ses champs de génération, sans suppression. Mode de famille `generee_sous_contraintes` inchangé.
- Graphe source : **zéro `requires` sortant**, seul `qc-pri-st-001` conseillé non bloquant.
- **12 items** numérotés `q-001` à `q-012`, uniques, tous reliés à `obj-1`, `crit-1`, `qc-pri-st-016-ev-01`; chaque stimulus, consigne, réponse critériée, rétroaction et limite présents.
- **10 items fixes et 2 scénarios contrôlés**; calcul déterministe vérifié pour les deux, avec **2 variantes fermées et leurs corrigés respectifs** (4 variantes documentées). Aucune génération libre/validation automatique par IA.
- Deux preuves distinctes : `q-011` station météo (jour/nuit), `q-012` centre de découverte (phases); exigences non compensatoires explicitement liées à la grille et à l'autonomie.
- Six modules de cours : 2 exemples résolus, 2+ contre-exemples, 2 diagnostics, 3 guidés, 4 autonomes, 2 transferts, remédiations et rappel J+7/J+21 retrouvés.
- Liens des fichiers centraux cités retrouvés **dans le ZIP d'origine** (sans inclusion au delta). Droits, adaptations et sécurité explicités; sites NASA consultés séparément et attribués dans `sources/REFERENCES_CONTENU.md`.
- Les corrigés ont fait l'objet d'un **contrôle de cohérence explicite du mécanisme** par vérification des attentes textuelles structurées; **pas** d'essai d'élèves ou d'audit scientifique indépendant.
- Simulation par comparaison des noms des fichiers à ceux de l'archive maître : **2 remplacements (`authoring/`) et 12 ajouts**, aucun élément extérieur à ce Kristal.

## Contrôles du fichier ZIP final

- Génération puis réouverture par `zipfile.ZipFile` et `testzip()`, 14 fichiers réguliers, non vides, ordre/chemins stricts, aucun chemin absolu, `../`, doublon, préfixe supplémentaire ni dossier global.
- Vérification du manifeste contre les entrées réelles; JSON reparsés depuis les octets compressés; contenus ZIP bit à bit identiques aux 14 fichiers de travail. (Ces tests sont exécutés **après** la rédaction de ce rapport lors du contrôle final.)

## Limites ouvertes / revue humaine requise

1. Contrôle scientifique et didactique par un spécialiste : précision des représentations, inférences permises, ambiguïtés de points de vue sur les phases et limites des modèles.
2. Passation test auprès d'apprenants, temps, lisibilité, suffisance des consignes, adaptations et contrôle des risques matériels selon établissement.
3. Accord de correcteurs sur les niveaux de la grille, seuils M1–M5, preuves indépendantes et retests après remédiation.
4. Liens NASA vérifiés à la consultation; permanence future des URL et droits des **médias ultérieurs** non garantie. Aucun média tiers embarqué. Aucun contrôle automatisé de conformité PFEQ requis ou prétendu.
5. Le test YAML valide la syntaxe et la préservation des valeurs; aucun Framework canonique, build-v9, check-ai ou LMS testé car le mandat ne les modifie pas.

## Propositions **non appliquées** aux fichiers centraux

- Ajouter au registre d'épreuves une convention explicite pour `scenario_controle` avec banque fermée, graine, règle de sélection et statut de revue.
- Prévoir dans le LMS une trace séparée de l'aide donnée pendant les deux preuves et une revue humaine intercorrecteurs.
- En cas d'évolution future : documenter les conditions de projection 2D/3D des phases lunaires et une procédure locale de sécurité des lumières, sans toucher à `registry/`, `governance/`, `canon/` ni à tout autre ID dans cette livraison.
