# Journal de livraison et validation — `qc-pri-ad-001` (delta v1.2)

**Périmètre :** une seule feuille existante `qc-pri-ad-001` en Art dramatique, depuis le workspace v1.2. **État :** production éditoriale intégrale avec **contrôles techniques**, mais sans essai terrain ni validation humaine. **Pas d’homologation PFEQ**, d’activation, de publication, de compilation canonique ou de certificat d’examen.

## Modifications et conservation

- **Remplacements intégrals :** `authoring/PARCOURS.md` (YAML préservé avec les mêmes clés; seuls statut éditorial et révision de contenu sont mis à jour, 12 rubriques développées) et `authoring/CONTRAT_PEDAGOGIQUE.json` (tous champs originaux conservés, famille native enrichie des champs contractuels d’instrumentation; statut éditorial actualisé).
- **Nouveaux :** six fichiers `contenu/`, trois fichiers `evaluation/`, `sources/REFERENCES_CONTENU.md`, `livraison/MANIFEST.json`, le présent journal. Le manifeste liste les **14** chemins complets et pas un fichier de plus.
- **Identités préservées :** `qc-pri-ad-001`, « Explorer corps, voix et espace scénique », `obj-1`, `crit-1`, objectif/proof exacts, `qc-pri-ad-001-ev-01`, `prerequis_bloquants=[]`, `ordre_conseille=[]`, conceptions et `observation_ou_production`.
- **Non modifiés ni livrés :** `kristal.workspace.json`, `AGENTS.md`, `authoring/ALIGNEMENT.md`, `BRIEF_REDACTION.md`, `docs/`, `canon/`, `state/`, `runtime/`, `registry/`, `governance/`, workspaces voisins. À la fusion, extraire **depuis** `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` sans dossier englobant.

## Contrôles exécutés sur le delta et le ZIP final

Contrôles **automatisés** réalisés avec script local sur les octets écrits et sur le ZIP après compression, avec résultat exigé « réussite » :

1. Ouverture CRC du ZIP; comparaison stricte du contenu des **14 fichiers** avec le manifeste; fichiers non vides, chemin initial `kristals/qc-pri-ad-001/`, aucune entrée extra, chemin absolu, `../`, dossier parent interdit ou autre Kristal.
2. Décodage UTF-8, JSON strict analysable (`authoring/CONTRAT_PEDAGOGIQUE.json`, `evaluation/BANQUE_ITEMS.json`, `livraison/MANIFEST.json`) et YAML analysable pour le frontmatter du parcours.
3. Préservation des champs canoniques du contrat et du frontmatter source; objectif, critère, famille, ID et type concordants; absence de préalables stricts et d’ordre conseillé.
4. Douze rubriques du parcours présentes dans le bon ordre; six documents de contenu; au moins deux exemples et deux contre-exemples, deux diagnostics, trois guidages, quatre activités autonomes, deux contextes distincts de transfert; références aux items correspondant à la banque.
5. Banque de **12 items** : identifiants `q-001` à `q-012` sans doublon, propriétés obligatoires présentes et renseignées, mode autorisé, complexité autorisée, seed/paramètres nuls pour scénarios fixes, `validation_status=a_revoir`, critères et feedback substantiels.
6. Scénarios de maîtrise indépendants : `q-010` musée (invitation à observer sans toucher) et `q-011` serre (avertissement + contournement); grille exige deux manifestations et quatre dimensions évaluées séparément. Sécurité, accessibilité, provenance et limites sont présentes dans les documents attendus.
7. Analyse manuelle des **corrigés de performance** : chaque réponse modèle est un **exemple possible** relié à l’intention et à deux familles de moyens; aucune sortie mathématique ou tirage libre à valider; aucune prétention de réponse artistique unique. Ce contrôle rédactionnel **n’est pas** un essai avec élèves.

**Statut :** les contrôles automatisés listés ci-dessus doivent être vérifiés sur l’archive finale et sont consignés ici seulement après leur exécution dans cette session. Aucun test d’environnement Moodle/Framework, de `build-v9` ou d’activation du canon n’est revendiqué.

## Limites, droits et décisions humaines requises

- **Revue pédagogique humaine** : validité des 12 tâches, clarté des consignes, quatre dimensions, seuil individuel I/M/C/A≥2, deux contextes de preuve, risques de biais, possibilités d’évaluation sans prestation publique.
- **Revue accessibilité/sécurité** avec situations réelles : vérifier l’équivalence de voix assistée, figurine, regard, partenaire ou adaptation de scène; le droit de pause, l’absence de contact et les contraintes de circulation; tenir compte des politiques locales de confidentialité et de consentement.
- **Droits** : seules des scènes et phrases rédigées pour cette livraison ont été utilisées; aucun élément audiovisuel externe n’est inclus. Aucun contrôle de droits sur d’éventuels médias futurs n’a été mené, ni avis juridique obtenu.
- **Essai terrain** : aucune collecte de performances d’élèves ni mesure d’efficacité; le contrôle humain peut conduire à changer les scénarios, les critères ou les seuils via une décision éditoriale versionnée.
- **Sources scientifiques externes** : aucune consultation ou vérification externe. Les seules références parcourues proviennent des documents de gouvernance et d’authoring inclus dans l’archive source.

## Propositions sans modification du registre ou du schéma central

1. **Proposer** un champ commun de suivi de revue des adaptations accessibles dans le système d’évaluation, sans l’ajouter au registre ni au canon dans cette livraison.
2. **Proposer** une liste contrôlée de statuts de livraison distincts pour « techniquement vérifié », « relu pédagogiquement », « essayé sur le terrain », « publiable », au lieu de déclarer automatiquement la qualification.
3. **Proposer** la séparation des traces d’observation d’élèves et des objets source dans l’export vers le LMS, sous réserve d’arbitrage technique.

**Décision finale proposée :** fusion du delta pour **revue humaine** seulement; aucune qualification pédagogique finale ni publication implicite.
