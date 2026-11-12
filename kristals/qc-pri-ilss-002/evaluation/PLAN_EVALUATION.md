# Plan d'évaluation — `qc-pri-ilss-002-ev-01`

**Objet immuable :** `obj-1` — Échanger des informations nécessaires à la vie de classe.  
**Critère de preuve immuable :** `crit-1` — Participer à un échange scolaire de plusieurs tours.  
**Famille :** `qc-pri-ilss-002-ev-01`; **type :** `observation_ou_production`; **statut :** banque créée, `a_revoir`, non certifiée.

## Déroulement, conditions et couverture

Les tâches sont des **dialogues fonctionnels observés** entre l'élève et un partenaire préparé, et non des QCM. Pour `q-001` à `q-004`, la production peut viser une composante de l'objectif; aucune de ces tâches isolées ne permet la maîtrise. Les tâches `q-005` à `q-010` vérifient de plus en plus l'échange multi-tours. Les deux dernières sont des **preuves distinctes** et se déroulent sans indice de contenu, avec partenaire différent si possible.

| Item | Objectif / critère / famille | Difficulté | Représentation contrôlée | Information fonctionnelle évaluée | Indices / variation admise |
|---|---|---|---|---|---|
| `q-001` | `obj-1` / `crit-1` / `qc-pri-ilss-002-ev-01` | initial | 2 images de bacs, dialogue bref | Demander quel bac | Montrer les deux bacs; changer seulement leur couleur sans changer la distinction. |
| `q-002` | idem | initial | 2 casiers étiquetés, rôle oral | Reformuler quel casier | Une relance de diagnostic notée; casiers A/B fixes. |
| `q-003` | idem | intermédiaire | cartes matériel, dialogue accompagné | Demander quantité et couleur | Amorces disponibles, puis retirées; valeurs figées « 5 / orange ». |
| `q-004` | idem | intermédiaire | horaire fictif, dialogue accompagné | Distinguer lecture et rangement | Icônes `? ↻`, pas de phrase modèle; deux heures figées. |
| `q-005` | idem | intermédiaire | atelier de papier, dyade sans carte | Demande précise, reformulation, 3 tours | Feedback seulement après; lieu fixé. |
| `q-006` | idem | intermédiaire | horaire de jeu, carte cachée au partenaire | Comprendre heure de début | Aucun indice; heure 13 h 20 distincte du rangement. |
| `q-007` | idem | intermédiaire | étiquette de colle, dyade | Quantité et couleur | Aucun indice; « une bleue » fixe. |
| `q-008` | idem | intermédiaire | deux casiers, dyade | Casier et tablette | Aucun indice; « 2 / haut » fixe. |
| `q-009` | idem — **preuve A** | transfert | affiche de groupe : rôles et matériel, partenaire préparé | Demander, vérifier et conclure l'organisation de l'affiche | **Zéro indice de contenu**; données « 2 feuilles vertes / équipe B découpe » fixées. |
| `q-010` | idem — **preuve B** | transfert | changement d'horaire ET local, nouveau partenaire | Vérifier une modification de routine de classe | **Zéro indice de contenu**; données « 10 h 30 / salle polyvalente » fixées. |

**Couverture des notions :** demande dans `q-001, 003, 005–010`; reformulation dans `q-002–010`; prise de parole alternée dans `q-003–010`. `q-009` et `q-010` exigent ensemble les trois notions et la totalité de `crit-1`. L'expression de la décision finale manifeste le fait que l'information obtenue est utile.

## Administration et règle de variation

1. Deux adultes ou un pair et un adulte peuvent jouer le partenaire après formation; le partenaire lit **uniquement** sa fiche fixe et répond à une demande, confirme une reformulation pertinente et ne donne pas de phrase à dire. Un pair ne juge pas l'autre élève.
2. Montrer à l'élève le but et l'objet de la tâche, mais **pas** la fiche-réponse. Laisser au moins cinq secondes de temps de traitement; un outil de communication habituel ou un pictogramme d'objet ne constitue pas un indice de contenu.
3. `q-001–004` : indices formateurs autorisés et consignés. `q-005–008` : aides d'accès, sans soufflage. `q-009–010` : aucune amorce de phrase, choix de mot-réponse, pointage de la réponse, correction en cours de dialogue ni encouragement directif; noter les aides effectivement utilisées.
4. Modes dans le JSON : `fixe` pour les items à fiche unique et `scenario_controle` quand le partenaire doit réagir à des demandes de clarification non identiques; `seed=null`, `parametres=null` partout car **aucun tirage ni algorithme paramétrique** n'est utilisé.
5. **Variation permise :** prénom fictif du partenaire, emplacement dans une classe simulée et équivalent accessible de la carte. **Variation interdite sans nouvelle révision :** nombre de faits à transmettre, informations cibles, complexité, nouveaux thèmes sensibles, temps, barème, existence d'une reformulation ou nombre de tours.
6. **Répétition :** pour une nouvelle tentative de maîtrise, ne pas réadministrer mot à mot `q-009` ou `q-010`; créer et valider une nouvelle fiche de même niveau, la consigner séparément. Une « nouvelle scène IA » non revue n'est pas valide.

## Grille, traces et décision

Quatre dimensions de 0 à 3 : **I** information juste et action; **D** demande pertinente; **R** reformulation/clarification; **T** alternance de tours et autonomie. Niveaux et exemples précis dans `GRILLE_MAITRISE.md`. Pour une **preuve complète** (`q-009` ou `q-010`), exiger `I,D,R,T ≥ 2`, au moins **trois interventions pertinentes** de l'élève alternées avec un partenaire, et une conclusion utile; en dessous de 2 dans une dimension, remédier et reprendre dans un nouveau cas. **Maîtrise** uniquement si deux preuves satisfaisantes en contextes distincts, dont une a minima sans indices (les deux sont planifiées sans indices). Pas de moyenne pondérée comme substitut et pas de décision sur un item isolé.

**Trace minimale :** `item_id`, date, contexte, partenaire pseudonymisé, aides d'accès/non indices, nombre de tours de l'élève, niveau I/D/R/T, exemple factuel bref, rétroaction et prochaine étape. Ne pas stocker d'informations migratoires, religieuses, médicales ou familiales; pas de voix captée obligatoirement. Les traces appartiennent au dispositif éducatif (LMS sécurisé), pas au dossier canonique.

## Accessibilité, biais et sécurité

Évaluer **la communication d'informations scolaires**, pas l'accent, l'origine, la vitesse, la forme grammaticale secondaire, la timidité ni les connaissances en mathématiques. Ajouter des images claires, consignes lues, temps supplémentaire, calme, adaptation auditive, communication augmentée, gestes ou support plurilingue lorsqu'ils soutiennent la participation fonctionnelle. Une aide de formulation pendant `q-009` ou `q-010` invalide seulement le **statut autonome de cette passation**, pas l'élève. Toutes les personnes et classes sont fictives. Ne pas forcer de divulgation personnelle.

**Qualité avant usage sommatif :** revue humaine des scénarios et rubriques, essai de passation, détection de biais/charge langagière, vérification de la stabilité entre partenaires, consentements et confidentialité selon le milieu. Les scripts constituent une banque éditoriale `a_revoir` et non une certification psychométrique.
