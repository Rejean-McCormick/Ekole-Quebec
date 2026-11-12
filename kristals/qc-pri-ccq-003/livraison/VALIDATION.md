# Validation de livraison — qc-pri-ccq-003

**Date du contrôle : 2026-10-08.** **Archive :** `qc-pri-ccq-003_livraison_v1.2.zip`. **Base :** `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` (archive disponible, lue à l'origine). **Statut :** vérification technique réalisée, revue humaine requise; aucune certification, homologation ni publication accordée.

## Contenu livré

- **14 chemins exacts :** 2 remplacements complets (`authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`) et 12 nouveaux fichiers. Aucune modification de `ALIGNEMENT.md`, `AGENTS.md`, des registres, de la gouvernance ni d'un autre Kristal.
- Douze sections de parcours avec front matter YAML conservé; concepts, exemples, diagnostics, trois guidages à indices dégressifs, quatre pratiques autonomes, cinq remédiations, deux transferts, rappel différé et accessibilité.
- **10 items** : 6 fixes (`q-001`–`q-004`, `q-009`, `q-010`) et 4 à scénarios fermés (`q-005`–`q-008`), soit **8 variantes rédigées pour ces quatre items**. Deux preuves autonomes inédites dans des contextes distincts (musée fictif; station fictive de questions).

## Contrôles effectivement exécutés

**Vérifications avant emballage : 46 / 46 réussies.** Liste détaillée :

- OK — filetree 14 chemins exacts dans le manifeste.
- OK — chaque fichier existe et est non vide.
- OK — aucun fichier imprévu dans le dossier de livraison.
- OK — tous les chemins du manifeste sous la bonne racine.
- OK — chemins sans traversée ni forme absolue.
- OK — manifeste identité et version.
- OK — identité historique du contrat inchangée.
- OK — objectif et preuve littéralement conservés.
- OK — aucun préalable ni ordre ajouté.
- OK — famille originale préservée sans perte de champs.
- OK — treize champs de gouvernance dans la famille.
- OK — famille et mode de production invariants.
- OK — YAML original conserve toutes ses clés.
- OK — YAML identité discipline et objectifs inchangés.
- OK — YAML sans préalable ajouté.
- OK — douze sections pédagogiques numérotées 1 à 12.
- OK — aucune relation entrante ou sortante au graphe.
- OK — banque de dix items et famille fixée.
- OK — IDs d’items sans doublon, numéros séquentiels.
- OK — chaque item a tous les champs exigés et réponses non vides.
- OK — tous les items liés à la famille, objectif et critère.
- OK — statuts non certifiés.
- OK — modes autorisés et difficultés définies.
- OK — six items fixes et quatre scénarios.
- OK — seed et paramètres nuls sur six items fixes.
- OK — scénarios avec deux variantes et réponse individuelle.
- OK — sélection par seed reproductible.
- OK — 8 variantes sélectionnées correctement aux deux seeds.
- OK — variantes distinctes sans corrigé inversé.
- OK — preuves A et B sur contextes distincts.
- OK — deux preuves entièrement autonomes.
- OK — cinq critères pour chacune des deux preuves.
- OK — deux tâches diagnostiques présentes.
- OK — trois guidages à indices dégressifs présents.
- OK — quatre pratiques autonomes documentées.
- OK — deux transferts distincts documentés.
- OK — au moins 2 exemples résolus et 2 contre exemples.
- OK — cinq remédiations ciblées présentes.
- OK — cinq dimensions C1-C5 de maîtrise détaillées.
- OK — plan évaluation liste 10 numéros.
- OK — conditions de confidentialité et accessibilité présentes.
- OK — sources externes identifiables et absence de licences inventées.
- OK — nomenclature CCQ conservée dans les fichiers.
- OK — aucune inclusion de dossier voisin ou registre par le manifeste.
- OK — les trois JSON produits sont strictement décodables.
- OK — références internes principales pointent aux fichiers produits.

**Contrôles du ZIP après emballage initial : 8 / 8 réussis.**

- OK — 14 entrées exactes à la racine interne.
- OK — premier chemin sous le bon Kristal.
- OK — aucun répertoire englobant, entrée interdite ou traversée.
- OK — 14 membres non vides.
- OK — intégrité ZIP CRC.
- OK — 3 JSON parsables depuis archive.
- OK — manifest du ZIP correspond à ses entrées.
- OK — aucun autre Kristal ni fichiers centraux.

**Mode de vérification :** lecture structurée des fichiers de l'archive source, comparaison des métadonnées originales, chargement YAML (`PyYAML`) et des trois JSON (`json` de Python), contrôle des champs et 10 identifiants, vérification des huit sélections de variantes aux graines préétablies et à leur graine suivante, contrôle des 14 chemins et test CRC de l'archive (`zipfile.testzip`). Après insertion du présent rapport, le ZIP est reconstruit puis recontrôlé avec les mêmes huit conditions d'empaquetage. **Cette suite est une validation structurale :** elle ne remplace pas une évaluation pédagogique ni une mesure intercorrecteurs.

## Points nécessitant une revue humaine

1. **Justesse interprétative :** faire relire les scénarios à une personne formée à la discussion pluraliste; plusieurs reformulations sont légitimes et les modèles ne sont pas exhaustifs.
2. **Âge et charge de lecture :** vérifier avec le public visé la lisibilité des vignettes et, le cas échéant, fournir des cartes simplifiées sans changer la question ni les arguments.
3. **Équité et sécurité :** s'assurer que l'animation en classe ne force ni témoignage, ni expression de croyance, ni exposition publique d'un enfant; vérifier les règles locales de conservation de traces.
4. **Calibrage de la grille :** faire coter quelques copies anonymes par deux personnes, analyser les divergences C1–C5; aucun essai ou étalonnage de terrain n'a été effectué.
5. **Droits d'auteur :** les cas sont des productions originales; les liens UNICEF/UNESCO sont mentionnés sans copier leur contenu; vérifier les conditions de toute éventuelle publication ou ajout ultérieur d'images externes.
6. **Faits externes :** les scénarios ne se présentent pas comme des situations historiques réelles. Vérifier l'actualité des liens et toute modification du cadre documentaire avant usage prolongé.

## Limites non résolues

- **Aucun test auprès d'apprenants**, aucune observation réelle des deux preuves, aucune validation psychométrique ou scientifique indépendante; pas d'homologation PFEQ revendiquée.
- Les **corrigés ouverts** sont des ancrages vérifiables par rapport aux vignettes; les réponses naturelles alternatives doivent être jugées par une personne et la grille, non par égalité de chaînes.
- Les scénarios contrôlés n'utilisent **aucune génération IA libre**; le test de reproductibilité vérifie la correspondance texte/réponse pour deux graines par item, **pas** la validité éthique de toute future modification.
- L'audit juridique, les licences de diffusion et les adaptations pratiques d'accessibilité restent à examiner dans le contexte du déploiement.

## Suggestions de changement de structure — NON appliquées

- Prévoir au niveau d'une future spécification centrale un champ `preuve_contextes` pour distinguer mécaniquement les deux preuves indépendantes et un champ `protection_donnees` pour rappeler l'interdiction de collecter des croyances.
- Prévoir dans un éventuel schéma de catalogue un champ `rubrique_ouverte_ref` et une version de calibrage humain intercorrecteurs. Aucune base centrale, aucun `AGENTS.md`, `kristal.workspace.json`, `ALIGNEMENT.md` ni dossier canonique modifié.

## Procédure de fusion

Décompresser l'archive maîtresse, entrer dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, puis y extraire `qc-pri-ccq-003_livraison_v1.2.zip`. **Ne pas** extraire depuis le répertoire parent et **ne pas** ajouter un dossier englobant. La racine interne commence immédiatement par `kristals/qc-pri-ccq-003/`.
