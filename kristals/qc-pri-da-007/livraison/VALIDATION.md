# Livraison et validation — `qc-pri-da-007` v1.2

**Nature :** delta fusionnable pour **un seul** Kristal, `qc-pri-da-007` (« Observer des œuvres chorégraphiques »), discipline **Danse**, vague **0**. Deux remplacements complets `authoring/`, douze fichiers nouveaux. **Statut :** contrôles documentaires et techniques, **revue humaine et essai pédagogique requis**; ni cours homologué ni banque d'items certifiée.

## 1. Source et périmètre exact

- L'archive autonome nommée `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis.zip` n'a pas été montée comme fichier indépendant. En revanche, **l'arborescence native v1.2** `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` est accessible à l'intérieur de l'archive conversationnelle `Spec_Kristals_Parcours_Primaire_Qc_v1.1(1).zip`, et c'est **cette source effectivement consultée** qui a servi de base.
- Documents lus avant production : `CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md` de la norme active, ainsi que `REFERENCES_EVIDENCE.md`, le graphe central, `authoring/PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md` et `BRIEF_REDACTION.md` du Kristal; lecture du `kristal.workspace.json` à titre de contrôle d'identité seulement.
- Seuls les chemins `kristals/qc-pri-da-007/authoring/`, `contenu/`, `evaluation/`, `sources/` et `livraison/` figurent dans le delta. **Aucun** fichier central, autre Kristal, `AGENTS.md`, `ALIGNEMENT.md`, `kristal.workspace.json`, `docs/`, `canon/`, `state/` ou `runtime/` n'est livré ou modifié.
- Fusion : décompresser l'archive maîtresse; entrer dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` puis extraire `qc-pri-da-007_livraison_v1.2.zip` à cet endroit. Aucun dossier englobant `Frames_202_...` ou au nom du ZIP n'est ajouté à la racine interne.

## 2. Livrables et décisions pédagogiques

- `PARCOURS.md` conserve le front matter original et ses **12 sections numérotées**, remplies avec notions, diagnostic, modelage, exercices, autonomie, remédiation, sécurité, maîtrise et rappel différé.
- Six fichiers `contenu/` : **2 exemples résolus**, **2 contre-exemples requis** (+ un supplémentaire), **2 diagnostics** D1/D2, **3 exercices** accompagnés G1–G3 à indices dégressifs, **4 pratiques** P1–P4, **2 contextes de maîtrise** M1/M2, **2 transferts** distincts T1/T2 et **rappel différé**. Tous les extraits sont des partitions textuelles originales fictives et horodatées; aucune œuvre externe ni captation n'est incluse.
- Onze items complets en mode **`fixe`**, famille **`qc-pri-da-007-ev-01`**, tous `obj-1`/`crit-1`, `seed=null`, `parametres=null`, `validation_status=a_revoir`. Deux preuves M1 `q-008` (duo « Passerelle d'ombres ») et M2 `q-009` (trio « Jardins d'angles »), dont la réussite indépendante est exigée. Des tâches de guidage ou de diagnostic ne deviennent pas automatiquement des preuves de maîtrise.
- `CONTRAT_PEDAGOGIQUE.json` conserve les champs natifs de la frame et les champs originaux de la famille, ajoute les paramètres de `GENERATEUR_ET_EXAMENS.md` et met à jour **seulement les statuts éditoriaux** au titre des changements de valeur. Aucun prérequis ni ordre conseillé créé; seule arête pertinente vers un autre ID : le registre comporte le lien **entrant** `qc-pri-da-008 requires qc-pri-da-007`.

## 3. Contrôles effectivement réalisés et limites des contrôles

**Contrôles automatisés exécutés localement** sur les fichiers générés, avec relecture du contrat original et du registre :

1. Arborescence **14 fichiers** exclusivement sous `kristals/qc-pri-da-007/`, non vides, noms manifestés et absence de traversée `../` ou chemin absolu.
2. Lecture/parsing des JSON stricts `CONTRAT_PEDAGOGIQUE.json`, `BANQUE_ITEMS.json` et `MANIFEST.json` et comparaison des champs d'identité/structure avec la frame native; parution des identifiants cohérents et 13 champs de famille requis.
3. Vérification du front matter YAML et de l'ordre des **12** sections, maintien du titre, objectif, preuve, discipline, famille et absence de prérequis sortant dans le graphe.
4. Contrôle des **11** IDs d'items séquentiels sans doublon; champs obligatoires, liens `obj-1`/`crit-1`/famille, modes `fixe` et statut `a_revoir`, critères et rétroactions non vides.
5. Vérification des étiquettes et sections des contenus : D1/D2, G1–G3, P1–P4, M1/M2, T1/T2, exemples commentés, contre-exemples et rappel différé; présence de déclarations de sécurité, accessibilité et provenance.
6. Contrôle de la structure et de l'intégrité du **ZIP final**, y compris la première entrée, 14 chemins strictement autorisés, correspondance exacte au manifeste, absence de dossiers englobants, absence d'entrées `../`, absence de fichiers supplémentaires et test de décompression CRC.

**Contrôle éditorial effectué à partir des supports écrits, et NON à partir de performances filmées :** les réponses proposées indiquent les trajectoires, arrêts, répétitions et relations correspondant aux *partitions inventées*. Un contrôle automatisé ne saurait établir la qualité expressive réelle, la clarté d'une danse jouée, ni une validation scientifique des seuils de jugement.

## 4. Limites non résolues et revue humaine obligatoire

- **Didactique :** un spécialiste de danse doit examiner les distinctions espace/temps/énergie/relation, les exemples, les erreurs typiques et les consignes pour la tranche d'âge choisie par le produit; un essai avec élèves doit vérifier compréhension, durée et intérêt réel.
- **Évaluation :** les rubriques et seuils (3 faits, 2 notions, 1 justification, 2 preuves A–D à niveau ≥2) sont des **décisions de design non étalonnées**. Procéder à une revue inter-évaluateurs, des exemples de réponses authentiques et un test d'équité avant un usage sommatif. Ne pas traiter `a_revoir` comme `certifié`.
- **Médias/droits :** aucun média tiers fourni, aucune recherche juridique d'antériorité menée. Toute future démonstration/captation exige autorisations, confidentialité, transcription, audiodescription et contrôle de l'équivalence avec les partitions fictives; une partition écrite ne prouve pas l'effet d'une vraie prestation.
- **Accessibilité/sécurité :** confirmer en contexte l'utilisabilité des supports et adaptations (lecture, cartes, audio, communication alternative, essais moteurs facultatifs). Pas de notation sur morphologie, virtuosité, goût, santé, âge ou divulgations privées; aucun diagnostic médical inféré.
- **Système :** aucun test d'import réel dans l'application ou LMS et aucune validation Framework/portabilité v9 ou publication n'a été exécutée; ces points restent hors du périmètre de ce delta. Aucun alignement détaillé ou homologation au PFEQ n'est visé.

## 5. Propositions sans changement du workspace central

1. Envisager une table de versions reliant les partitions textuelles approuvées et leurs éventuelles mises en scène enregistrées, avec attestation de droits et d'équivalence des repères.
2. Prévoir dans l'application un champ de trace d'aide **technique** versus **indice disciplinaire** pour ne pas surdéclarer l'autonomie.
3. Autoriser une validation humaine de versions accessibles (audiodescription/texte/diagrammes), distincte d'une simple copie de banque d'items.

**Aucune proposition ci-dessus ne modifie** `registry/`, `governance/`, `canon/`, le manifeste de workspace, le graphe ni d'autres Kristals. Les contrôles sur le ZIP, leurs résultats et l'absence de fichiers parasites ont été vérifiés au cours de la création de l'archive de livraison.
