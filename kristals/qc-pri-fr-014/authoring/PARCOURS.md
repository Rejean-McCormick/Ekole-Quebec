---
format: qc.learning-path/1.0
id: qc-pri-fr-014
titre: Groupes de mots et fonctions syntaxiques
discipline_code: FR
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Repérer des groupes de mots et expliquer leurs principales fonctions dans une phrase.
objectifs_secondaires: []
criteres_reussite:
- Segmenter plusieurs phrases et expliciter le rôle de leurs groupes.
prealables_declares:
- qc-pri-fr-013
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-fr-014-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-fr-014`

**Discipline :** Français, langue d’enseignement (appellation québécoise). **Titre :** Groupes de mots et fonctions syntaxiques. **Vague :** 1. **État :** leçon rédigée, revue humaine requise; les métadonnées YAML natives v1.2 ont été préservées, notamment leur statut d’origine.

## 1. Intention et frontières

- **Objectif immuable (`obj-1`) :** Repérer des groupes de mots et expliquer leurs principales fonctions dans une phrase.
- **Preuve immuable (`crit-1`) :** Segmenter plusieurs phrases et expliciter le rôle de leurs groupes.
- **Notions :** groupe nominal (GN), groupe verbal (GV), fonctions syntaxiques. En extension guidée : GN complément direct du verbe au sein du GV et complément de phrase clairement amovible.
- **Limite :** analyser d’abord des phrases déclaratives simples à sujet GN et GV prédicat; ne pas confondre classe de groupe et fonction, ni limiter le GV à son seul verbe. Aucun accord grammatical avancé, cas d'inversion ou subordonnée n'est requis pour la preuve.
- Les exemples et évaluations privilégient les constructions naturelles en français québécois standard et évitent la variation orale qui modifierait les frontières analysées.

## 2. Notions et représentations

- **GN** : groupe dont le noyau est un nom; peut comprendre déterminant et adjectif (`les petits chats`). GN est une **nature de groupe**, non automatiquement sa fonction. En phrase, un GN peut être sujet ou complément direct.
- **GV** : groupe dont le noyau est un verbe conjugué (`rangent les cahiers`). Dans la phrase déclarative simple travaillée, le GV constitue le **prédicat**, incluant ses compléments éventuels; il ne se réduit pas à `rangent`.
- **Fonctions** : rôle syntaxique exercé par une unité dans une construction : **sujet** pour le GN sujet, **prédicat** pour le GV et **complément direct (CD)** pour un GN situé *dans* le GV lorsque le verbe l'admet. Les fonctions sont relatives à la phrase ou au groupe étudié; ne pas mélanger les deux niveaux.
- **Tests contrôlés :** repérer le nom noyau, remplacer le GN sujet par `il/elle/ils/elles`, vérifier l'accord avec le verbe; repérer le verbe conjugué et tout son GV; remplacer un GN CD par `le/la/les` si la structure le permet. Ces manipulations sont des indices et non des règles universelles applicables hors de ce corpus.
- **Représentation :** `GN sujet {Les élèves} | GV prédicat {préparent GN CD {une affiche}}`. Le CD est **imbriqué dans** le GV; on n'en fait pas un troisième constituant immédiat de la phrase. Deux exemples entièrement résolus et deux contre-exemples : `contenu/01_NOTIONS_ET_EXEMPLES.md`.

## 3. Préparation / diagnostic

- **`requires` strict :** `qc-pri-fr-013` (Classes de mots), seul lien sortant du graphe. **`recommends_before` :** aucun; **`reinforces` :** aucun. Les liens entrants d'autres Kristals n'ajoutent aucune obligation.
- Le diagnostic peut **attester un acquis équivalent** : reconnaissance d'un nom, d'un déterminant, d'un verbe conjugué et de la différence nature/fonction; si démontrée, le parcours se poursuit même sans consommation du module préalable.
- `diag-1` : « Les petits chats observent les oiseaux. » — repérer noms/verbe et délimiter GN sujet, GV, GN CD.
- `diag-2` : « La voisine transporte une boîte. » — expliquer GN et GV, puis justifier les fonctions avec deux manipulations simples.
- Corrigés et embranchements : `contenu/02_DIAGNOSTIC.md`. Une difficulté de décodage n'est pas assimilée à une méconnaissance syntaxique; lecture des consignes autorisée.

## 4. Enseignement guidé

- Modèle A : « Les jeunes élèves rangent les cahiers. » L'enseignant identifie noms (`élèves`, `cahiers`), verbe (`rangent`), les deux constituants immédiats et le GN CD interne au GV.
- Modèle B : « La bibliothécaire prépare une affiche. » Tests : « Elle prépare une affiche » (GN sujet remplacé), « La bibliothécaire la prépare » (GN CD remplacé); montrer que `prépare une affiche` demeure le GV.
- Exploiter la méthode **repérer le noyau → délimiter les groupes → attribuer la fonction → justifier la fonction**, sans enseigner le seul truc trompeur « qui fait l'action ? ».
- Séquence complète, diagrammes et corrigés : `contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

- `guided-1` : « Les grands chiens poursuivent les balles. » Tableau amorcé des groupes, **indices forts** (verbe et déterminants repérés).
- `guided-2` : « Le facteur apporte un colis. » **Indice intermédiaire** : rappeler le test de remplacement du GN sujet sans présenter la segmentation.
- `guided-3` : « Après le repas, les élèves lavent les tables. » **Indice minimal**, donné après une tentative : tester déplacement/suppression de `Après le repas` et identifier la hiérarchie sujet / prédicat / complément de phrase.
- Trois résolutions, erreurs probables et feedback : `contenu/04_PRATIQUE_ACCOMPAGNEE.md`. Retirer progressivement les soutiens.

## 6. Pratique autonome

- Quatre tâches inédites (`independent-1` à `independent-4`) avec réponses et indices linguistiques justifiés dans `contenu/05_PRATIQUE_AUTONOME.md`.
- Production : segmenter les groupes demandés, nommer leur nature, préciser sujet / prédicat / CD quand ce dernier est un GN, et étayer au moins une fonction par remplacement ou accord. Ne pas fournir de modèle durant l'essai autonome.
- Les **preuves de maîtrise indépendantes** ne sont pas ces quatre tâches : elles sont réservées aux items `q-009` (projets d'école) et `q-010` (jardin collectif), avec trois phrases par contexte et justification sans indice de fond.

## 7. Feedback et erreurs typiques

- **Nature confondue avec fonction** : « GN = toujours sujet » → comparer GN sujet et GN CD dans la même phrase, pronominaliser les deux séparément.
- **GV tronqué** : « GV = seulement le verbe » → inclure le GN CD qui dépend du verbe; représenter son inclusion par accolades imbriquées.
- **Frontière du GN trop courte** : omettre `jeunes` dans « Les jeunes élèves » → essayer de remplacer **tout** le GN par `ils`.
- **Complément de phrase confondu avec complément du verbe** : mettre `Après le repas` dans le GV → vérifier suppression/déplacement de ce groupe dans la phrase travaillée.
- **Question sémantique insuffisante** : chercher seulement « qui agit ? » → utiliser pronominalisation et accord; rappeler qu'un sujet peut ne pas être un agent.
- Feedback et tâches de remédiation : `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 8. Évaluation formative et preuves

- **Famille :** `qc-pri-fr-014-ev-01`; `objectif_ref: obj-1`; `critere_ref: crit-1`; type `réponse_argumentée`, items fixes contrôlés. Pas de génération IA libre, pas de statut certifié.
- 10 items originaux et complets, du repérage initial au transfert. Les épreuves `q-009` et `q-010` comportent chacune **trois phrases** dont les GN sujet, GV prédicat et GN CD sont documentés dans le corrigé.
- Sur les deux épreuves, appliquer la **même grille** (segmentation, nature/fonction, justification, autonomie, transfert), mais avec des noms, verbes et contextes différents.
- Sources de vérité : `evaluation/BANQUE_ITEMS.json`, `evaluation/PLAN_EVALUATION.md`, `evaluation/GRILLE_MAITRISE.md`.

## 9. Remédiation / enrichissement

- Échec sur le nom noyau → revenir brièvement à la distinction nom/verbe/déterminant; diagnostic d'équivalence du préalable sans copier le contenu de `qc-pri-fr-013`.
- Échec sur le GV → dessiner une grande accolade autour du verbe **et** du CD; faire contraster avec le seul verbe conjugué.
- Échec sur les fonctions → proposer deux GN dans une phrase et vérifier par `il/elle` puis `le/la/les`.
- Réussite stable → ajouter un complément de phrase clairement déplaçable, non de cas ambigus.
- Transferts avec corrigés : article de babillard et inventaire de jardin, `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 10. Accessibilité

- Consignes offertes en texte lisible et oral; phrases agrandies, espaces typographiques et couleurs **non exclusives**; utiliser accolades, mots et listes structurées plutôt qu'une couleur seule.
- L'élève peut répondre par dictée, oral transcrit ou étiquettes de mots; l'adulte ne nomme pas les fonctions pendant la passation. Séparer l'évaluation du **décodage** de celle de **l'analyse grammaticale**.
- Test oral de substitution possible; lecture par synthèse vocale sans révéler les limites des groupes. Aucun jugement sur accent ou variation du français parlé québécois. Exemples de phrases écrites normalisées pour une analyse sans équivoque.
- Les données du devoir ne demandent aucune donnée personnelle; aucun matériel dangereux ni déplacement requis.

## 11. Critères de sortie

- `crit-1` : **Segmenter plusieurs phrases et expliciter le rôle de leurs groupes.** Deux manifestations contextuellement distinctes (q-009 et q-010) réalisées de façon autonome avec **les frontières de GN sujet et de GV prédicat correctes pour chacune des trois phrases**; **GN CD correctement imbriqués** et justifiés; une distinction claire entre nature et fonction.
- Grille dimensionnelle à niveaux 0, 1, 2. La maîtrise exige des indices de compréhension sur **les deux** contextes, non un total de points unique ou une seule phrase réussie.
- Si une manifestation est insuffisante, cibler le point manquant, proposer de nouveaux exemples et une épreuve indépendante non apprise à l'avance; ne pas répéter mot pour mot un item de test.

## 12. Références pédagogiques et limites

- **Sources internes lues et préservées :** gouvernance v1.2, charte de conversion, graphe des relations, parcours, contrat, alignement et brief du workspace maître.
- **Sources linguistiques vérifiées :** Office québécois de la langue française, Vitrine linguistique : « groupe nominal », « groupe verbal », « complément direct », « les fonctions syntaxiques », « le prédicat ». URLs et portée dans `sources/REFERENCES_CONTENU.md`.
- **Raisonnement original :** ordre des activités, phrases d'entraînement, seuils de la grille, diagnostic et items; ils ne sont pas des prescriptions officielles.
- **Rappel différé :** après quelques jours, segmenter une phrase nouvelle et expliquer la portée du GV; après 1 à 2 semaines, réaliser une comparaison de deux phrases inédites avec CD au sein du GV.
- Le présent microparcours n'est ni homologué au PFEQ, ni validé auprès d'élèves, ni certifié; revue pédagogique et intercorrecteurs nécessaire avant usage institutionnel.
