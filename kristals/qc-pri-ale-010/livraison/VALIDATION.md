# Validation de livraison — qc-pri-ale-010 · version 1.2

**Livraison :** delta du workspace v1.2 pour `qc-pri-ale-010` uniquement, `statut_validation: a_revoir`. Cours rédigé **pour revue**, non certifié, non homologué, non publié.

## Contrôles réellement effectués sur les contenus (tous réussis)

- **OK —** YAML lisible / 17 champs natifs conservés.
- **OK —** Métadonnées YAML gelées hors révision éditoriale.
- **OK —** 12 sections numérotées exactement et dans le bon ordre.
- **OK —** Identité/titre, discipline, objectif, preuve et famille dans le parcours.
- **OK —** Préalable strict et conseil non bloquant.
- **OK —** Graphe maître: requires et recommends_before concordants.
- **OK —** Contrat JSON: champs/familles v1.2 existants conservés.
- **OK —** Objectif, critère, identifiants, préalables et famille invariants.
- **OK —** Famille: 13 champs du générateur/examens.
- **OK —** Génération fixe sans paramètres libres.
- **OK —** BANQUE_ITEMS: JSON strict et format/ID/famille exacts.
- **OK —** 10 items numérotés consécutivement sans doublons.
- **OK —** Tous les items: champs obligatoires et liens constants.
- **OK —** Mode fixe, valeurs null, statut à revoir.
- **OK —** Chaque item possède tâche, corrigé/rubrique et feedback non vides.
- **OK —** Deux preuves et thèmes distincts: jardin/bibliothèque.
- **OK —** Chaque preuve inclut 5 phrases, question, négation, impératif.
- **OK —** Deux preuves: seuils identiques et autonomie requise.
- **OK —** Épreuve A: 5 phrases contrôlées sur Mira/helpers.
- **OK —** Épreuve B: 5 phrases contrôlées sur Owen/volunteers.
- **OK —** Corrigé indépendant - Mira: affirmation/question/négation.
- **OK —** Corrigé indépendant - Owen: affirmation/question/négation.
- **OK —** Corrigés formatifs fixés dans un échantillon de réponses clés.
- **OK —** Au moins 2 exemples, 2 contre-exemples, 2 diagnostics, 3 guidés, 4 autonomes, 2 transferts.
- **OK —** Rapports citent accès, droits et limites de validité.
- **OK —** Matrice de plan couvre chacun des dix items.
- **OK —** Grille exige A et B sans compensation.
- **OK —** Aucun ID d’autre Kristal ajouté dans un chemin de livraison.
- **OK —** Manifeste JSON, ID, version, archive_root, statut cohérents.
- **OK —** Manifeste: exactement 14 chemins attendus sans doublon.
- **OK —** 13 fichiers prévalidation non vides.

## Couverture et conformité de forme

- Sources initiales lues : 3 documents de gouvernance, registre du graphe, 4 sources du Kristal (PARCOURS, contrat, ALIGNEMENT, BRIEF), plus références internes; deux ressources grammaticales externes consultées, signalées dans les références.
- YAML d'origine conservé en entier; seul `revision_contenu` passe de `0.2.0` à `0.3.0` (statut auteur `en_rédaction` préservé). Contrat JSON d'origine conservé pour toutes les valeurs canoniques; `statut` éditorial et `review_status` de la famille mis à jour pour la revue, autres champs exigés ajoutés sans suppression.
- 12 sections développées; 2 exemples modelés, 4 contre-exemples, 2 diagnostics, 3 guidages dégressifs, 4 activités autonomes, 2 transferts contrôlés; rétroactions ciblées, accessibilité et rappel différé.
- 10 items fixes numérotés `q-001`–`q-010`. Deux preuves distinctes de cinq phrases liées à un thème, `q-009` jardin et `q-010` bibliothèque. Réponses fixes et rubriques avec variantes limitées; aucune génération de paramètres, aucune seed ni solveur externe.
- Contrôles de réponses **partiellement déterministes** : comparaison de réponses figées à un générateur grammatical minimal, sur les verbes réguliers *water* et *sort* des deux preuves; revue de quelques réponses clés de la banque. **Ce n'est pas un correcteur grammatical universel ni une validation de toutes les variantes**.

## Conditionnement ZIP : contrôles réellement exécutés

- Les 14 chemins du ZIP et du manifeste sont rigoureusement identiques; première entrée `kristals/qc-pri-ale-010/authoring/PARCOURS.md`, aucun conteneur intermédiaire, aucun autre dossier de Kristal.
- Chaque chemin est relatif et commence par `kristals/qc-pri-ale-010/`, sans `../` ni entrée absolue; aucune entrée vide, doublonnée ou globale; aucune entrée interdite (`registry/`, `governance/`, `AGENTS.md`, `kristal.workspace.json` etc.).
- Tous les fichiers du ZIP sont octet pour octet identiques à la construction; 3 JSON parsables; contrôle CRC du ZIP effectué.
- L'archive source et les registres communs **n'ont pas été modifiés**. Aucune fusion sur un workspace exploité, build-v9, check-ai, LMS, essai réel ni publication effectués.

## Limites explicites et revue humaine obligatoire

1. **Révision linguistique** : exactitude et idiomaticité de toutes les phrases et des variantes de réponse, justesse des distinctions *subject*, *verb*, *complement*, ponctuation, niveau du vocabulaire. Les contrôles ponctuels de corrigés et les sources grammaticales ne constituent pas une certification.
2. **Étalonnage des seuils** : grille G/V/T et seuils (3/4, 3/3, 2/3), durée, facilité comparée des deux contextes, fiabilité intercorrecteurs et adaptation à l'âge non testés sur des élèves.
3. **Accessibilité / biais** : ergonomie, compatibilité des aides à la saisie, passation avec scribe et perception des exemples nécessitent des essais utilisateurs.
4. **Droits / diffusion** : textes déclarés originaux, pas de tiers reproduits volontairement; revue juridique et licence de diffusion non exécutées.
5. **Préservation des deux preuves** : ne pas exposer le corrigé ou les scénarios A/B au cours de l'enseignement. Toute variante ou remplacement ultérieur requiert une revue humaine avant décision.
6. **Schémas / moteur** : les champs d'enrichissement du contrat et de la banque ont été contrôlés comme JSON et selon ce mandat, pas testés avec un validateur Framework officiel.

## Évolutions centrales proposées, non appliquées

- Normaliser ultérieurement le champ `critere_id` des familles, le protocole de masquage du corrigé et la traçabilité des adaptations d'accès dans un schéma central.
- Versionner une banque de scénarios A/B de remplacement validés humainement; cela éviterait de réemployer une preuve dont la correction a déjà été dévoilée.

**Fusion prescrite :** décompresser la source maîtresse; se placer dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` puis extraire **ce ZIP** directement à cet endroit, sans dossier englobant. Ne pas considérer cette opération comme une qualification ou une publication.
