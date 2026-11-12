# Plan d'évaluation | qc-pri-ilss-003 — famille qc-pri-ilss-003-ev-01

**Objectif immuable `obj-1` :** Reconnaître et utiliser les mots clés des activités scolaires.  
**Critère immuable `crit-1` :** Associer lexique et consignes dans une tâche scolaire nouvelle.  
**Nature :** observation ou production observable. **Banque :** `BANQUE_ITEMS.json` (`qc.learning-item-bank/1.0`), 12 items fixes à revoir. **Jamais de notation de la compréhension d'une discipline scientifique ou de l'origine linguistique.**

## Couverture item par item

Tous les items sont liés à `obj-1`, `crit-1` et `qc-pri-ilss-003-ev-01` dans le JSON et par ce tableau. Les quatre notions sont outil (O), discipline (D), objet (B) et action (A).

| Item | Difficulté | Représentation / production | Notions | Critère observable et référence |
|---|---|---|---|---|
| q-001 | initial | cartes mots, parole/pointage | A, O, B, D | identifie action et outil, `obj-1` / `crit-1` |
| q-002 | initial | fiche formes et consigne, action | D, A, B, O | discipline + cercle autour de bonne forme, `obj-1` / `crit-1` |
| q-003 | intermédiaire | objets réels, placement | O, B, A | règle comme objet déplacé **dans ce contexte**, `obj-1` / `crit-1` |
| q-004 | intermédiaire | comparaison de deux traces, justification | A, B | trace conforme à *entoure*, `obj-1` / `crit-1` |
| q-005 | intermédiaire | étiquette écrite et colle, manipulation | A, B, O | *colle* verbe vs texte « COLLE » sur étiquette, `obj-1` / `crit-1` |
| q-006 | initial | bande A B C, action | A, B, O | ligne sous B uniquement, `obj-1` / `crit-1` |
| q-007 | intermédiaire | boîtes et cartes, tri | A, B | appariement selon même mot, `obj-1` / `crit-1` |
| q-008 | intermédiaire | quatre cartes, lien oral/gestuel | D, A, B, O | quatre rôles correctement associés, `obj-1` / `crit-1` |
| q-009 | intermédiaire | travail fictif erroné, correction | A, B, O, D | corrige deux erreurs séparées, `obj-1` / `crit-1` |
| q-010 | transfert | bande et carton, deux étapes | A, B, O | souligne puis colle, `obj-1` / `crit-1` |
| **q-011 — preuve A** | **transfert** | atelier de sciences, réalisation autonome | **D, A, B, O** | **deux actions, deux cibles et choix d'outils autonomes, `obj-1` / `crit-1`** |
| **q-012 — preuve B** | **transfert** | affiche d'arts plastiques, réalisation autonome | **D, A, B, O** | **deux autres actions, deux cibles et choix d'outils autonomes, `obj-1` / `crit-1`** |

## Rubrique, pondération et décision

- **Formative q-001 à q-010** : commentaires descriptifs itemisés, remédiation spécifique après toute erreur. Ne pas combiner ces réussites en « note de maîtrise ».
- **Épreuves q-011 et q-012, chacune séparément** : D1 (actions), D2 (outils et objets), D3 (contexte), D4 (autonomie/transfert), de 0 à 2 selon la `GRILLE_MAITRISE.md`. Pour chacune : D1=2, D2=2, D3≥1, D4≥1, avec un lien mot→geste/matériel visible, **sans indice lexical ciblé**. Les deux doivent satisfaire le seuil; une réussite ne compense pas l'autre.
- L'administration q-011/012 requiert une personne observatrice qui consigne *faits* et *modalités* sans faire le geste à la place de l'élève. Une lecture verbatim répétée, un grand caractère et un pointage/une manipulation équivalente ne sont pas des indices sémantiques.

## Variations permises et interdites

- **Modes** : exclusivement `fixe`; `seed=null`, `parametres=null`. Aucun tirage aléatoire. Les stimuli sont verrouillés; n'ajouter aucune question libre produite par IA à l'épreuve.
- **Permis** : agrandir la typographie, lire exactement l'énoncé, utiliser une carte magnétique/virtuelle pour simuler la colle, adapter la prise en main, réponses orales, par pointage, dessin ou cartes avec gestes identifiables. Conserver dans la trace le mode utilisé.
- **Interdit** : traduire ou définir *entoure*, *colle*, *colorie* pendant q-011/012, désigner la bonne cible, mimer l'action, remplacer librement *ÉRABLE* par un mot plus facile, changer l'ordre ou les étapes sans nouvelle validation.

## Biais, droits, sécurité, accessibilité

- Aucune question sur pays, langue de la maison, identité, religion, niveau scolaire antérieur ou immigration. Les étiquettes sont des supports arbitraires; aucun fait botanique ou artistique n'est vérifié.
- Documents rédigés ici, sans images protégées, pas de capture d'enfants ni de données sensibles. Cartes papier et colle en bâton usuelles, sous supervision appropriée; option carte aimantée/velcro, sans ciseaux.
- Corrigés définis sans dépendre d'une IA; la grille exige une revue humaine d'utilisabilité. Les adaptations ne doivent pas donner le sens des mots visés.

## Conditions de qualification

Revue d'une personne enseignante ILSS et d'une spécialiste de l'accessibilité, vérification des scripts en classe et essai avec élèves, harmonisation intercorrecteurs, audit de l'environnement de livraison. Rien de cela n'est déclaré exécuté.
