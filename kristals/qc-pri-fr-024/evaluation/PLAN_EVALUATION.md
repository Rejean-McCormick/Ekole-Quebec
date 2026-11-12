# Plan d'évaluation interne — qc-pri-fr-024 (v1.2)

**Titre :** Comprendre des communications orales. **Discipline :** Français, langue d’enseignement.  
**Objectif immuable (`obj-1`) :** Reformuler les points essentiels d’une communication orale suivie.  
**Preuve immuable (`crit-1`) :** Restituer un message oral et répondre à des questions de vérification.  
**Famille immuable :** `qc-pri-fr-024-ev-01`; **type natif :** `réponse_argumentée` (reformulation fidèle et réponse étayée), **mode des dix items :** `fixe`. **Statut :** `a_revoir` pour les dix items.

## Conditions d'administration et de correction

1. Un évaluateur fait entendre **le texte exact** de chaque `stimulus` à débit naturel, deux fois, sans découper l'information ni fournir d'indices de fond; pause silencieuse entre deux écoutes. Les directives de prosodie entre crochets ne sont pas prononcées. L'élève n'a accès ni au script ni aux réponses avant l'essai; les questions sont posées après la restitution, non entre deux passages.
2. L'élève reformule dans ses mots, puis répond aux trois questions factuelles. Une réponse non verbatim, exprimée en français québécois naturel, est valable si elle conserve le sens. Si une question est ambiguë à l'oral, l'enseignant la clarifie **sans donner la réponse** et documente l'intervention; soumettre l'item à révision.
3. Le correcteur utilise `reponse_attendue`, `faits_essentiels_a_conserver`, `relations_a_conserver` et `reponses_questions` de `BANQUE_ITEMS.json`, puis la grille qualitative à cinq dimensions. Corriger sur la preuve dans le script, **pas** sur une supposition plausible. Une intonation n'établit pas seule un fait; les mots restent l'ancrage.
4. Les tâches q-001 à q-006 servent au calibrage formatif, q-009/q-010 à la généralisation/révision; **q-007 et q-008**, sur deux séances distinctes et des contextes indépendants, fournissent deux preuves de maîtrise. Les deux ne doivent pas être modelées ni données en exercice avant la décision.
5. À consigner par épreuve : date, version du script, lieu, qualité d'audition, nombre de passages, dispositif d'accès/expression, aide de contenu (oui/non), cinq niveaux 0–3, faits modifiés ou oubliés, questions exactes/erronées, décision ciblée. Pas de diffusion des voix enregistrées.

## Table d'alignement : chaque item → même objectif, critère et famille

| Item | Objectif | Critère | Famille | Difficulté | Représentation et compétence dominante | Rôle |
|---|---|---|---|---|---|---|
| `qc-pri-fr-024-q-001` | `obj-1` | `crit-1` | `qc-pri-fr-024-ev-01` | initial | annonce orale; distinguer deux catégories de livres | calibrage |
| `qc-pri-fr-024-q-002` | `obj-1` | `crit-1` | `qc-pri-fr-024-ev-01` | initial | consigne orale; conserver l'ordre et la nouvelle date | calibrage |
| `qc-pri-fr-024-q-003` | `obj-1` | `crit-1` | `qc-pri-fr-024-ev-01` | intermédiaire | annonce d'activité; condition météorologique fictive | calibrage |
| `qc-pri-fr-024-q-004` | `obj-1` | `crit-1` | `qc-pri-fr-024-ev-01` | intermédiaire | programmation d'ateliers; inscription différentielle | calibrage |
| `qc-pri-fr-024-q-005` | `obj-1` | `crit-1` | `qc-pri-fr-024-ev-01` | intermédiaire | réunion; condition de proposition commune | calibrage |
| `qc-pri-fr-024-q-006` | `obj-1` | `crit-1` | `qc-pri-fr-024-ev-01` | intermédiaire | annonce vocale; changement d'horaire localisé | calibrage |
| `qc-pri-fr-024-q-007` | `obj-1` | `crit-1` | `qc-pri-fr-024-ev-01` | transfert | service collectif; dépôt/classement/échange et condition | **preuve 1** |
| `qc-pri-fr-024-q-008` | `obj-1` | `crit-1` | `qc-pri-fr-024-ev-01` | transfert | fabrication; étapes/partage des tâches et interdiction | **preuve 2** |
| `qc-pri-fr-024-q-009` | `obj-1` | `crit-1` | `qc-pri-fr-024-ev-01` | transfert | rectification orale; temps recalculé | généralisation |
| `qc-pri-fr-024-q-010` | `obj-1` | `crit-1` | `qc-pri-fr-024-ev-01` | transfert | collecte; opposition et cause | généralisation |

**Couverture :** 10/10 demandent une restitution **et** trois réponses de vérification; 10/10 testent sujet + faits; 9/10 explicitent ordre, opposition ou condition, et le reste une distinction de catégories/temps; les deux preuves utilisent des domaines sémantiques différents (service collectif / réalisation d'objet). La progression initial → intermédiaire → transfert est une décision de design interne, pas un étalonnage normatif externe.

## Rubrique, poids et décision

- **Poids logique :** cinq dimensions de même importance de décision (*sujet*, *faits*, *relations*, *questions*, *reformulation fidèle/autonome*). Les niveaux 0–3 servent à identifier les besoins, non à calculer une note unique. La conformité sémantique prime sur l'élégance de la parole.
- **Seuil opérationnel proposé :** pour q-007 **et** q-008, minimum niveau 2 **à chaque dimension**, aucune contradiction critique non rectifiée (négation, acteur, horaire, condition) et aucune aide sémantique. Deux performances stables à des moments distincts; en cas d'incohérence, statut « preuve insuffisante » et nouvelle collecte après remédiation.
- **Feedback :** signaler l'élément juste, nommer un point erroné, citer la partie du script après la collecte de preuve, proposer une activité R1–R6. Ne pas transformer une note globale en « maîtrise ».

## Variabilité autorisée et interdite

**Autorisée :** voix et genre du lecteur, prosodie sobre, volume adapté, débit naturel comparable, formulation personnelle des réponses, dispositif expressif qui ne fournit pas les mots de la réponse. Tous les stimuli sont **figés**; `seed=null`, `parametres=null`, `variables=[]`, pas d'algorithme génératif.

**Interdite :** IA générant librement des messages/solutions avec ce même item_id; reformulation du stimulus avant l'essai; ordre, acteur, date, négation ou condition changés; explication ciblée pendant une des deux preuves; texte écrit fourni à la place de l'oral sans évaluation distincte et revue d'équivalence. Une substitution de scénario demanderait une **nouvelle version revue**, pas une variante implicitement approuvée.

## Accessibilité, sécurité et revue humaine

Les scripts originaux ne demandent aucune divulgation personnelle et n'incluent pas de noms réels; aucun enregistrement obligatoire. Adapter l'accès sonore (acoustique, volume, écouteurs, nombre de passages fixé) et la sortie expressive (scribe neutre, outil non génératif). Pour surdité/malentendance, un message signé peut constituer une **épreuve adaptée** de compréhension d'une communication suivie, mais pas une preuve strictement identique de traitement auditif : faire valider la décision par une équipe qualifiée. Les variantes régionales et accents ne sont pas des erreurs. Tester la durée, la compréhension des mots, l'équivalence des deux épreuves, la neutralité culturelle, le caractère naturel des pauses et les conditions matérielles avec une revue humaine/pilote avant toute qualification. Aucune homologation ou conformité détaillée au PFEQ revendiquée.

## Sources internes

`../authoring/CONTRAT_PEDAGOGIQUE.json`, `../authoring/PARCOURS.md`, `../contenu/01_NOTIONS_ET_EXEMPLES.md`, `../contenu/06_REMEDIATION_ET_TRANSFERT.md`, `../sources/REFERENCES_CONTENU.md`, `BANQUE_ITEMS.json`, `GRILLE_MAITRISE.md`.
