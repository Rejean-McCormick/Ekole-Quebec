# Validation réellement effectuée — `qc-pri-mu-009` v1.2

**Statut :** contrôle documentaire et technique réussi, **revue humaine toujours requise** (`a_revoir`). **Archive :** `qc-pri-mu-009_livraison_v1.2.zip`. **Base de travail :** archive utilisateur `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip`, qui contient le dossier `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` et les fichiers gouvernance et auteur demandés. Ce constat a été établi par inspection du ZIP, pas par reconstitution hypothétique.

## Contrôles effectivement exécutés — avant emballage

**47 assertions réussies** par script local. Les contrôles portent sur :

- [x] En-tête YAML source strictement conservé.
- [x] 12 sections numérotées exactement une fois.
- [x] Objectif immuable conservé parcours et contrat.
- [x] Preuve immuable conservée.
- [x] Famille unique et identifiant conservés.
- [x] Préalable strict et ordre inchangés.
- [x] Concepts 4 conservés.
- [x] Tous champs préexistants famille conservés.
- [x] 13 champs gouvernance famille présents.
- [x] Relations conformes au graphe source.
- [x] Aucune dépendance inter-Kristal ajoutée.
- [x] Titre et discipline corrects.
- [x] Deux exemples commentés distincts.
- [x] Deux contre-exemples commentés.
- [x] Deux diagnostics complets.
- [x] Trois guidées à indices décroissants.
- [x] Quatre pratiques autonomes.
- [x] Deux tâches de transfert contextes distincts.
- [x] Feedback erreurs et remédiations.
- [x] Rappel différé 2 et 7 jours.
- [x] Plan lie tous items et critères.
- [x] Au moins huit items complets.
- [x] Item IDs uniques et séquentiels.
- [x] Schéma strict commun 11 items.
- [x] Tous items utilisables sans placeholder.
- [x] Statuts prudents fixés.
- [x] Tous items sont fixes sans seed variable.
- [x] Chaque item lié à famille objectif et critère.
- [x] Couverture complexité graduée.
- [x] Deux preuves contextes et sons différents.
- [x] Critères de maîtrise non compensatoires.
- [x] Préférence non notée.
- [x] Sécurité accessibilité auditives traitées.
- [x] Droits explicités.
- [x] Bibliothèque audio contient exactement 11 lecteurs.
- [x] Chaque item identifie une piste existante.
- [x] Contrôle technique WAV pour les 11 pistes.
- [x] Tous marqueurs WAV visibles et concordants.
- [x] Partition sonore explicite pour chaque piste.
- [x] Absence des termes de certification interdits au statut.
- [x] Manifeste 14 chemins exacts.
- [x] Vérification de contenu non vide avant archive.
- [x] 11 encodages base64 indépendamment décodables.
- [x] SHA-256 encodages et WAV synthétisés identiques.
- [x] Paramètres WAV sûrs du fichier décodé.
- [x] Protocole n’affirme pas avoir été testé par un humain.

- [x] Manifest et Validation présents, 14 contenus construits.

## Contrôles exécutés après emballage

Le script vérifie *à nouveau* après construction : (a) les 14 entrées exactes avec le premier chemin sous `kristals/qc-pri-mu-009/`; (b) l’absence d’entrée absolue, de `../`, de dossier parent englobant ou de chemin d’un autre Kristal; (c) le fait que chaque fichier n’est pas vide; (d) le manifeste et les trois JSON stricts (`CONTRAT_PEDAGOGIQUE.json`, `BANQUE_ITEMS.json`, `MANIFEST.json`) sont parsables; (e) la concordance byte-à-byte entre les fichiers ZIP et les contenus construits. **Résultat : réussite**, si et seulement si le script achève sa dernière ligne « POSTZIP PASS » (voir journal d'exécution). Une revue humaine de lecture et de lecture audio dans Moodle **n’a pas** été exécutée.

## Contrôle pédagogique des corrigés (limite)

Les repères de hauteur, de durée, d’ordre, de répétition, de dynamique relative et de timbre sont fondés sur la partition de synthèse déterminée et la concordance des 11 WAV (octets, paramètres, empreintes). Le script ne constitue pas une **écoute perceptive humaine** et ne démontre pas que chaque différence sonore soit aisée à discerner par tous les élèves. Les réponses-témoins sont donc des **exemples de productions recevables**, non des émotions exactes ni des « réponses officielles » à reproduire.

## Limites non résolues et revues humaines obligatoires

1. Vérifier **à l’oreille** les 11 mini-œuvres sur des haut-parleurs réels (volume, contrastes, fatigabilité et absence de sons agressifs), avec des éducateurs et, selon les procédures autorisées, des apprenants.
2. Contrôler la **compatibilité HTML5 et URI `data:`** dans Moodle/lecteurs d’écran; fournir au besoin une extraction des fichiers WAV originale et contrôlée avant diffusion, sans ajout de fichiers au ZIP de fusion.
3. Réviser la linguistique du français québécois, la lisibilité par cycle sans attribuer une année obligatoire, les temps de passation et les éventuels biais de contextes « sport » et « coin lecture ».
4. Valider la grille et son usage intercorrecteurs, la distinction de deux indices, les conditions d’autonomie et les adaptations sensorielles préservant le but « entendus ».
5. Contrôler les **droits de diffusion** et les ressemblances mélodiques fortuites des micro-créations; aucune licence de tiers ni droit commercial n’est inventé.
6. Effectuer un test réel des liens relatifs **après fusion** dans le LMS; seule la correspondance des chemins de cette livraison est vérifiée ici.

## Propositions d'évolution de structure (non appliquées)

- Ajouter à terme une bibliothèque média canonique dédiée aux extraits WAV avec empreintes et variantes accessibles; **aucun changement** apporté à `canon/`, `runtime/`, `docs/`, `registry/` ou `governance/`.
- Ajouter un champ standardisé « piste / segment / média alternatif » dans les banques, sous contrôle de version central plutôt que de forcer des URI de grande taille dans le Markdown.
- Journaliser le type d’aide et l’accommodation pour les deux preuves d’autonomie, en dehors de la connaissance canonique.

**Portée :** delta limité à ce Kristal; aucune modification d’un autre ID, aucun fichier maître livré.
