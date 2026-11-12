# 07 — Plan d’évaluation : figures planes et propriétés

## **Contrat invariant**

`qc-pri-ma-023` · `obj-1` : Classer des figures planes à partir de propriétés observables. · `crit-1` : Trier de nouvelles figures et expliquer un cas de non-appartenance. · famille `qc-pri-ma-023-ev-01`. Mode privilégié `paramétrique_controle`, instanciations en `parametrique` au format de banque. **Tout item demeure `a_revoir`.**

## **Administration et validité**

Ordre recommandé : diagnostic → modelage → accompagnement → ancrages q001–q008 → variantes q009–q010 → preuves q011–q012. Le format fixe peut être présenté en matériel/tactile ou au quadrillage, sans déformer les coordonnées ou les relations. Aucune réponse n’est déterminée par impression visuelle, couleur, taille apparente ou noms d’objets. Les nombres et preuves exacts sont dans la banque.

## Matrice de couverture et traçabilité

Tous les items ci-dessous sont attachés explicitement à **`obj-1` / `crit-1` / `qc-pri-ma-023-ev-01`**. Les colonnes « figure » renvoient aux stimuli complets de la banque.

| Item | Niveau | Représentation / cible | Attendu vérifiable / justification | Variabilité |
|---|---|---|---|---|
| `qc-pri-ma-023-q-001` | initial | quadrillage : triangle et quadrilatère | T, non R; 3 contre 4 côtés | verrouillé |
| `qc-pri-ma-023-q-002` | initial | sommets + cercle | P polygone; cercle non polygonal | verrouillé |
| `qc-pri-ma-023-q-003` | initial | 3/4/5 côtés | T/R/P; exclusion 5 ≠ 4 | verrouillé |
| `qc-pri-ma-023-q-004` | intermédiaire | 3 quadrilatères sur quadrillage | I=0, Q=1, R=2 paires; Q exclu du 2 | verrouillé |
| `qc-pri-ma-023-q-005` | intermédiaire | quadrilatère incliné K | 2 paires conservées malgré la rotation | verrouillé |
| `qc-pri-ma-023-q-006` | intermédiaire | R et L (orientations différentes) | R et L : 4 côtés / 2 paires | verrouillé |
| `qc-pri-ma-023-q-007` | intermédiaire | polygones + cercle | R seul à 4 côtés; C contour courbe | verrouillé |
| `qc-pri-ma-023-q-008` | intermédiaire | Q / R / I, exactement une | Q seul; R=2, I=0 | verrouillé |
| `qc-pri-ma-023-q-009` | intermédiaire | J/K/L/M, grille instanciée | J : 2; K : 1; L : 0; M : 3 côtés | seed=245; corpus/similitude bornés |
| `qc-pri-ma-023-q-010` | intermédiaire | U/V/W/X, grille instanciée | U,V : 1; W : 2; X : 0 | seed=306; corpus/similitude bornés |
| `qc-pri-ma-023-q-011` | transfert | **Maîtrise contexte 1** : mosaïque | A,C : 2; B=1, D=0; rejet B | seed=415; corpus/similitude bornés |
| `qc-pri-ma-023-q-012` | transfert | **Maîtrise contexte 2** : jardin | E,F : 1; G=2, H=0; rejet G | seed=729; corpus/similitude bornés |

## Corrigé, barème et décision

- **Par item**, évaluer qualitativement trois dimensions : (C1) ensemble des inclus/exclus intégralement correct, (C2) nombre de côtés et/ou paires opposées qui fonde le tri correctement constaté (les paires sont nommées lorsque demandé), (C3) au moins une **non-appartenance correctement justifiée** par une propriété mesurable. Erreur de transcription isolée à vérifier oralement sans donner le critère; noter toute aide fournie. Le classement juste sans explication est une preuve partielle.
- **Preuves de maîtrise indépendantes** : `q-011` **mosaïque**, classement « exactement deux paires »; et `q-012` **jardin**, « exactement une paire ». Les stimuli sont nouveaux, instanciés par seeds distincts, administrés sans indice cognitif ni corrigé visible, idéalement à deux occasions. Le journal consigne seed, production, aide et contexte.
- **Acquis stable** : C1, C2 et C3 sont observés sur **les deux** tâches, avec justification autonome et transfert de règle. Un seul bon score, ou un seul contexte réussi, ne suffit pas. En cas de divergence, adapter/remédier au critère fautif puis demander deux nouvelles figures/contextes, sans réutiliser le même corrigé.
- **Contrôle de solution** : pour ABCD, vérifier les deux paires AB/CD et BC/DA par `ux*vy - uy*vx = 0`. Un validateur indépendant normalise les directions entières par PGCD. Les paramètres ne font que changer rotation par quarts de tour, échelle entière positive et translation; les invariants sont testables automatiquement. Aucun texte/question inventé à la volée par IA n'est autorisé.

## Variation, intégrité et cas limites

- q-001 à q-008 : stimuli fixes, réponses fixes. q-009 à q-012 : seuls les seeds **entiers 0 à 1023** peuvent varier. Le calcul `t=seed%4`, `k=1+(seed//4)%2`, `a=14+(seed//8)%5`, `b=14+(seed//40)%5`, suivi de `(a,b)+k*rotation90_t(sommet)`, est exhaustivement documenté dans `BANQUE_ITEMS.json` et le contrat enrichi. Les gabarits, leur ordre et les règles de tri sont figés.
- Les modèles sont des polygones convexes, non dégénérés, fermés; toutes les coordonnées restent entières. Les tests prévoient quart de tour, rotations 180/270°, facteurs 1/2, côtés verticaux, droites obliques, nombres exacts de paires 0/1/2, triangles sans couples opposés et figures non polygonales définies textuellement.
- Une même paire opposée est comptée **une fois**. Les critères disent *exactement* pour éviter l'ambiguïté de « une paire »; le nom de « trapèze » n'est pas exigé. On n'attribue jamais un score à la conformité graphique d'un dessin libre.

## Accessibilité, sécurité, confidentialité, revue

Présenter chaque figure avec **texte des coordonnées ET support quadrillé/manipulable**, non par une couleur seule; possibilité d'agrandir ou de tracer avec règle, d'utiliser tiges et diagramme tactile, lecture de la consigne, réponse orale transcrite ou écrite. Ces aménagements ne contiennent aucun indice de tri. Éviter obstacle moteur/visuel et taxer seulement le raisonnement géométrique. Aucune collecte d'identité ou de photo personnelle; « jardin » et « mosaïque » sont des situations fictives culturellement neutres. Durée flexible et matériel non dangereux.

**Avant tout usage sommatif** : revue humaine de la lisibilité, convenance développementale des coordonnées, diversité des représentations, définition de « parallèle », qualité des rubriques, charge de lecture, alternative accessible pour les paires obliques; essai avec élèves et vérification des contrôles de génération. Ces vérifications humaines ne sont **pas** déclarées réalisées.
