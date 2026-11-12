# Validation du delta — qc-pri-da-009 (v1.2)

## Statut

**Contrôles statiques locaux : 35/35 réussis.** Résultats obtenus par le script local de vérification de fichiers, métadonnées, contenu minimal et banque avant empaquetage. Les contrôles ZIP et intégrité sont exécutés **après** création du ZIP et rapportés au résultat final si réussis. Cette validation **n'est pas** un audit de faisabilité en classe ou une certification pédagogique.

## Contrôles effectivement réalisés

- [x] 13 fichiers pré-validation sous le seul ID.
- [x] YAML frontmatter source préservé bit pour bit.
- [x] YAML du parcours parsable.
- [x] 12 sections numérotées une fois, de 1 à 12.
- [x] identité et état de la frame YAML préservés.
- [x] contrat format et identité préservés.
- [x] champs originaux du contrat sans perte ni modification.
- [x] objectif et preuve canoniques exacts.
- [x] préalable, ordre et famille inchangés.
- [x] relations alignées sur le graphe source.
- [x] famille de 13 champs minimum selon générateur.
- [x] type d’évaluation et family ID corrects.
- [x] banque JSON schéma de tête conforme.
- [x] banque 12 items.
- [x] numérotation séquentielle et unique.
- [x] 12 items avec tous les champs requis non vides.
- [x] 12 items reliés obj-1, crit-1 et famille.
- [x] types fixes, graines nulles, aucun paramétrage caché.
- [x] statuts des items tous a_revoir.
- [x] difficultés définies et couvertes.
- [x] stimuli et consignes uniques.
- [x] preuves A/B contextes distincts.
- [x] récits et traces personnelles pour deux preuves.
- [x] preuve sans vidéo obligatoire.
- [x] plan couvre tous les IDs.
- [x] grille signale les deux preuves et six axes.
- [x] diagnostic contient deux tâches distinctes.
- [x] 3 activités guidées présentes.
- [x] 4 pratiques autonomes présentes.
- [x] 2 transferts distincts.
- [x] 2 exemples commentés et 2 contre-exemples.
- [x] droit, accessibilité et sécurité documentés.
- [x] manifeste exact et fichiers valides.
- [x] références internes connues.
- [x] aucun autre ID workspace dans les chemins.

## Limites non résolues et revue humaine requise

- Revue pédagogique et linguistique des énoncés et rubriques; essai avec des enfants, étude de clarté et de fidélité entre correcteurs non effectués.
- Revue par personnel qualifié des conditions motrices, de l'accessibilité concrète, des besoins individuels et de la sécurité de l'espace avant activité.
- Vérifier le consentement des participants, les modalités d'échanges entre élèves et les règles locales d'enregistrement, de stockage, de conservation et de droits; **vidéo facultative**.
- Les deux preuves authentiques `q-011` et `q-012` exigent un projet réellement mené et des traces créées par l'élève; le présent paquet propose des rubriques, il ne prouve pas qu'un enfant a réussi.
- Pas de test d'intégration dans un LMS, pas de publication, pas de build de canon v9, pas d'homologation ou d'alignement PFEQ.
- Les `validation_status` de tous les items restent `a_revoir`; aucun état « certifié », « homologué », « publié ».

## Propositions facultatives de changement de structure — **NON APPLIQUÉES**

- Pour le registre central, proposer un champ de nature d'évidence (« notes », « storyboard », « vidéo volontaire ») et un indicateur de consentement géré côté LMS, hors connaissance canonique.
- Pour les familles d'évaluation, proposer une convention commune d'axes rubricaux et une liste de contextes distincts pour comparer les décisions sans centraliser les traces des enfants.
- Faire valider toute évolution du graphe ou de la gouvernance dans une modification versionnée **séparée**, jamais dans ce delta.

## Fusion attendue

Extraire `qc-pri-da-009_livraison_v1.2.zip` **dans** `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` pour superposer `kristals/qc-pri-da-009/`. **Deux remplacements** complets (`authoring/PARCOURS.md`, `authoring/CONTRAT_PEDAGOGIQUE.json`) et **douze ajouts**. Aucun autre chemin à écraser. Le YAML original du parcours est conservé tel quel; les champs originaux du contrat demeurent sans changement, des champs de famille ont été ajoutés.

## Contrôles du ZIP après empaquetage

**12/12 vérifications réussies.** Le contrôle CRC et les vérifications de chemins ont été effectués sur l’archive construite.

- [x] ZIP : exactement 14 fichiers.
- [x] ZIP : chemins et ordre conformes au manifeste.
- [x] ZIP : premier chemin sous le bon ID.
- [x] ZIP : absence de chemin absolu ou parent.
- [x] ZIP : aucun dossier enveloppant.
- [x] ZIP : chaque contenu non vide et UTF-8 lisible.
- [x] ZIP : archive CRC intégrale.
- [x] ZIP : JSON parsables.
- [x] ZIP : manifeste interne égale aux entrées.
- [x] ZIP : identités cohérentes.
- [x] ZIP : contenu correspond aux sources locales.
- [x] ZIP : aucun fichier gouvernance/registry/AGENTS/canon.
