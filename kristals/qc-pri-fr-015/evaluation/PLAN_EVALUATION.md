# Plan d'évaluation — qc-pri-fr-015 / v1.2

**Kristal :** `qc-pri-fr-015` — Construction des phrases. **Discipline :** Français, langue d’enseignement.  
**Objectif unique :** `obj-1` — Construire des phrases compréhensibles en organisant correctement leurs constituants.  
**Critère-source :** `crit-1` — Transformer des mots désordonnés en phrases correctes et varier leur structure.  
**Famille unique :** `qc-pri-fr-015-ev-01` ; `type : réponse_argumentée`.  
**Banque :** `BANQUE_ITEMS.json`, mode **fixe** pour les 12 items; `seed: null`, `parametres: null`, aucun générateur d'items ouvert. **Statut :** `a_revoir`, non certifié.

## Matrice de couverture complète

Toutes les lignes ci-dessous sont liées à `obj-1`, `crit-1` et `qc-pri-fr-015-ev-01` (aucun autre objectif, critère ou famille n'est implicite).

| Item | Difficulté | Contexte | Représentation | Attendu vérifiable / focalisation |
|---|---|---|---|---|
| `qc-pri-fr-015-q-001` | initial | ciel | cartes écrites, 1 phrase + justification | Sujet « Les nuages », prédicat « cachent le soleil »; pas de CP fourni. |
| `qc-pri-fr-015-q-002` | initial | courrier | cartes, 2 phrases + justification | CP de temps « ce matin » avant/après; P « distribue le courrier ». |
| `qc-pri-fr-015-q-003` | initial | entraide | cartes, 2 phrases + justification | Respect des rôles : enfants aident voisins, non l'inverse. |
| `qc-pri-fr-015-q-004` | intermédiaire | école | cartes, 2 phrases + justification | P « préparent des affiches » non fragmenté; variation « demain ». |
| `qc-pri-fr-015-q-005` | intermédiaire | patinage | cartes, 2 phrases + justification | CP de lieu « sur la patinoire »; objet « un gant » dans P. |
| `qc-pri-fr-015-q-006` | intermédiaire | arbres | cartes, 2 phrases + justification | Accord pluriel « Les érables perdent »; CP temporel « en automne ». |
| `qc-pri-fr-015-q-007` | intermédiaire | solidarité | cartes, 2 phrases + justification | CP « le jeudi » et prédicat « trient des dons ». |
| `qc-pri-fr-015-q-008` | intermédiaire | port | cartes, 2 phrases + justification | CP de lieu « près du quai » / prédicat « vérifie son filet ». |
| `qc-pri-fr-015-q-009` | transfert | atelier scientifique | cartes, 2 phrases + justification | **Preuve autonome A** : « Jade classe des roches » + CP « pendant l’atelier ». |
| `qc-pri-fr-015-q-010` | transfert | sport collectif | cartes, 2 phrases + justification | **Preuve autonome B** : « Les équipes rangent les cônes » + CP « après le match ». |
| `qc-pri-fr-015-q-011` | transfert | transports | cartes, 2 phrases + justification | Transfert supplémentaire : gare, voyageurs, horaires, CP de lieu. |
| `qc-pri-fr-015-q-012` | transfert | spectacle | cartes, 2 phrases + justification | Transfert supplémentaire : lumières, technicien, CP de temps. |

**Couverture :** 1 item d'identification/production simple sans CP, 7 situations de construction/variation à difficulté initiale ou intermédiaire, 4 situations de transfert; 8 CP de temps et 3 CP de lieu (dans les 11 items à CP). Les compléments du verbe restent dans le prédicat et sont mis en contraste avec les CP mobiles. Tous les énoncés sont originaux et fixés.

## Passation, rubriques et décision

1. **Avant la maîtrise :** prendre les items 001–008 pour diagnostic formatif au besoin; ne pas enseigner les réponses des items 009–010 avant leur utilisation comme preuves nouvelles.
2. **Manifestation A, séance distincte :** item 009 en contexte d'atelier scientifique; réponse indépendante, deux structures de même sens et justification.
3. **Manifestation B, autre séance ou contexte :** item 010 dans un contexte de rangement sportif, consigne de même exigence, toujours sans aide. Une autre paire de transferts de complexité équivalente ne peut remplacer celle-ci qu'après revue documentée.
4. **Observation par item :** lire les critères et variantes admises dans `BANQUE_ITEMS.json`, puis appliquer la grille descriptive de `GRILLE_MAITRISE.md`. Une correspondance exacte de caractères ne suffit pas à juger les justifications; inversement, une justification convaincante ne répare pas une phrase mal ordonnée.
5. **Règle de maîtrise :** satisfaction de tous les critères essentiels **dans chacune** des deux manifestations, sans indices syntaxiques; tolérance documentée pour graphies accessoires isolées si l'ordre et le sens restent observables. Si l'une échoue, remédier à la dimension ciblée et administrer plus tard une **nouvelle tâche** de transfert non mémorisée. Ne pas agréger deux notes pour compenser une erreur de sens.

## Barème et variabilité permise

- **Rubrique descriptive par dimensions**, non note sommative : (1) sujet + prédicat bien construits et accord pertinent; (2) mots et sens conservés; (3) CP déplacé pour obtenir deux structures correctes; (4) justification et autonomie. Niveaux dans `GRILLE_MAITRISE.md`.
- **Variantes admissibles :** ordre première/deuxième phrase inversé; explication en français courant plutôt qu'en étiquettes techniques; réponse tapée, dictée verbatim ou manuscrite. Le correcteur humain tient compte des variantes syntaxiques valides qui préservent l'objectif **sans déroger** à la tâche contrôlée.
- **Limites :** ne pas changer sujet, verbe, objet, temps, lieu, nombre ou voix; ne pas omettre ni dupliquer des cartes; pas de seule variation lexicale; pas de déplacement du complément du verbe à la place du CP. Dans le modèle enseigné, la phrase complète en tête avec CP est séparée par une virgule. Une ponctuation mineure isolée est une piste de feedback, pas un substitut aux critères syntaxiques.
- **Paramétrique :** aucun item de ce mode; donc aucun domaine numérique, seed active ni solveur à revendiquer. Tout ajout de variantes automatiques exigerait un corpus fermé, une validation indépendante des solutions et une nouvelle version.

## Sécurité, accessibilité et biais

- Scénarios fictifs, aucune demande d'information intime, de photo, d'accent particulier ou de déplacement physique. Lexique simple; expliciter oralement « cône » et « horaire » sans offrir la solution syntaxique si une barrière lexicale apparaît, puis consigner cette adaptation.
- Consignes disponibles sous forme écrite lisible, lecture neutre ou matériel de cartes; transcription mot à mot possible; laisser des pauses, sans chronométrage. Ne pas évaluer la prononciation, la vitesse de décodage ou la motricité fine.
- Pour la décision autonome, **ne pas** présenter catégories [S]/[P]/[CP] ni rétroaction en direct; noter les soutiens accordés et refaire une preuve si l'aide touche précisément le critère mesuré.
- Revue humaine à faire : ambiguïtés syntaxiques alternatives, variété linguistique québécoise, lexique, équité, durée, qualité de la justification et validité de deux contextes.

**Références :** `../authoring/CONTRAT_PEDAGOGIQUE.json`, `../sources/REFERENCES_CONTENU.md`, `GRILLE_MAITRISE.md`. Cette banque n'est ni un examen homologué ni un test certifié.
