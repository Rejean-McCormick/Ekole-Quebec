# Validation technique et réserves — livraison `qc-pri-fr-020` v1.2

**Statut :** vérifications automatiques réussies sur le contenu et les métadonnées; **revue pédagogique humaine requise**, banque `a_revoir`, aucune publication, qualification ou homologation.

## Tests effectivement exécutés

Script local de contrôle `validate_and_zip.py` (hors archive) exécuté sur les vrais fichiers de la livraison et sur l'archive v1.2 fournie. **29 contrôles préconditionnels passés / 29**. Chaque contrôle ci-dessous correspond à une vérification effectuée, non à une promesse.

- **OK — archive source présente**.
- **OK — manifest de 14 fichiers sans doublons**.
- **OK — racine exacte du manifeste**.
- **OK — 14 chemins exacts du payload**: 14 fichiers.
- **OK — 14 fichiers non vides**.
- **OK — anti-traversée de chemins**.
- **OK — première entrée correcte**.
- **OK — 2 remplacements existants et 12 ajouts inédits**.
- **OK — YAML parse et champs de base inchangés**: 17 champs conservés.
- **OK — 12 sections sans changement de structure**: Sections 1 à 12 ordonnées.
- **OK — identité et métadonnées canoniques conservées dans le contrat**.
- **OK — famille v1.2 conservée + 13 champs obligatoires**.
- **OK — graph de base respecté**.
- **OK — JSON strict 3 fichiers**.
- **OK — banque identité / famille**.
- **OK — 12 items numérotés sans doublons**.
- **OK — schéma item, réponse et feedback utilisables**.
- **OK — modes fixes et statuts sans certification**.
- **OK — traçabilité tous items vers obj-1/crit-1/famille**.
- **OK — deux preuves différentes avec autonomie**.
- **OK — grille 4 dimensions et seuil local**.
- **OK — 2 exemples et 2 contre-exemples rédigés**.
- **OK — 2 diagnostics / 3 guidés / 4 autonomes / 2 transferts**.
- **OK — rappel différé, rétroaction et accessibilité documentés**.
- **OK — provenance et droits explicités**.
- **OK — liens internes relatifs résolus**: 14 références testées; cassées : [].
- **OK — aucun placeholder de rédaction**.
- **OK — aucun dossier canon ou registre global inclus**.
- **OK — corrigés textuels distincts et alignés au but (structure)**.

## Tests de ZIP et fusion (exécutés lors de la fabrication)

- Test d'ouverture ZIP, liste exacte de 14 fichiers sans répertoire englobant, premier chemin `kristals/qc-pri-fr-020/`, absence de chemin absolu ou `../`, cohérence octet pour octet avec les fichiers produits.
- Vérification que le manifeste énumère les 14 entrées, dont lui-même et cette validation; extraction **simulée dans un dossier de test** du workspace maître et contrôle que seules deux entrées existantes sont écrasées et que douze entrées sont ajoutées.
- Test de parse de tous les JSON à partir des données ZIP et de YAML à partir du `PARCOURS.md` de l'archive.

## Limites non résolues

1. **Révision humaine des tâches ouvertes** non effectuée : exemples de corrigés et ancrages examinés pour la structure, **aucune validation psychométrique**, mesure de fidélité intercorrecteurs ni essai avec des élèves.
2. **Exactitude contextuelle locale** (modalités de prêt, compost, horaires, sécurité, règlement) volontairement laissée « à confirmer » : aucun fait local n'est certifié.
3. **Accessibilité** : modalités équivalentes spécifiées et contrôlées textuellement, mais **aucun essai utilisateur** avec lecteurs d'écran, dispositifs d'assistance ou élèves concernés.
4. **Droits** : rédaction nouvelle sans reproduction externe identifiée; licences des fichiers sources, droits de redistribution et revue juridique **non audités indépendamment**.
5. **Liens externes** : pages IES et CAST consultées lors de la rédaction, pas de supervision continue de leur disponibilité. **Liens internes** vérifiés par résolution de chemin, non par rendu LMS.
6. **Intégration produit** : aucune génération de canon v9, migration de schéma, vérification LMS, publication, activation ni contrôle de réussite en classe.

## Révision humaine recommandée avant utilisation sommative

Faire relire par une personne enseignante francophone du Québec le vocabulaire, la longueur des consignes, la pertinence des alternatives, la sécurité, les situations fictives et la grille. Faire deux corrections indépendantes de plusieurs plans réels, régler les désaccords, éprouver le temps et les adaptations. La validation automatique ne certifie **pas** la qualité sémantique de réponses ouvertes.

## Propositions structurelles (NON appliquées)

- Au registre central, envisager un identifiant normalisé pour les preuves A2/T1 et la traçabilité des deux contextes de maîtrise, sans le créer dans ce delta.
- Enrichir le futur schéma de famille par une version de grille et une règle de révision humaine signée. **Aucune modification** de `registry/`, `governance/`, `kristal.workspace.json` ou `AGENTS.md` dans ce ZIP.

**Fusion :** extraire l'archive dans la racine **interne** `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` du workspace maître, et non dans son dossier parent. Deux fichiers `authoring/` se superposent; douze autres sont ajoutés. Contrôler les conflits de modifications concurrentes avant fusion.
