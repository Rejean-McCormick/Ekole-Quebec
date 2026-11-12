---
format: qc.learning-path/1.0
id: qc-pri-ma-023
titre: Figures planes et propriétés
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Classer des figures planes à partir de propriétés observables.
objectifs_secondaires: []
criteres_reussite:
- Trier de nouvelles figures et expliquer un cas de non-appartenance.
prealables_declares: []
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-023-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-023`

**Discipline :** Mathématique · **Titre :** Figures planes et propriétés · **Gouvernance :** v1.2.  
**Statut réel :** contenu et banque préparés pour revue pédagogique humaine; ni cours homologué ni banque certifiée. Le statut YAML natif et les identifiants sont conservés.

## 1. Intention et frontières
- `obj-1` (immuable) : **Classer des figures planes à partir de propriétés observables.**
- `crit-1` (immuable) : **Trier de nouvelles figures et expliquer un cas de non-appartenance.**
- Notions : **côtés, sommets, parallélisme, figure**. On limite le classement initial à des figures planes closes, dont des polygones simples non dégénérés et un cercle comme cas contrastif. Une figure plane n'est pas nécessairement un polygone.
- Conventions explicites : côté = segment entre deux sommets consécutifs d'un polygone; sommet = rencontre de deux côtés consécutifs; une paire de côtés parallèles est constituée de deux côtés distincts portés par des droites parallèles (pas seulement « deux côtés qui ne se touchent pas »). Les dessins sont schématiques; les coordonnées fixent la géométrie exacte.
- Aucun classement selon la couleur, l'orientation, la longueur apparente ou le nom d'un objet réel. L'élève doit citer le critère qui fait entrer ou exclure chaque figure.

## 2. Notions et représentations
- **Figure plane** : ensemble géométrique dessiné ou défini dans un plan; un cercle et un polygone sont des figures planes. Un disque, un cercle et la bordure d'un polygone ne doivent pas être confondus; ici, les contours suffisent au tri.
- **Polygone simple** : ligne fermée composée d'au moins trois segments dont les côtés ne se croisent qu'à des sommets consécutifs. Exemples : triangle et quadrilatère. **Contre-exemple** : un cercle, car son contour est courbe.
- **Côté/sommet** : un triangle non dégénéré a 3 côtés et 3 sommets; un quadrilatère simple non dégénéré en a 4 de chaque. Changer le sens de parcours ne change pas les nombres.
- **Parallélisme** : les droites supports de deux côtés distincts ne se rencontrent pas, même si elles sont prolongées. Dans un quadrilatère, seuls les côtés opposés peuvent former une paire parallèle; 0, 1 ou 2 paires sont possibles. Deux segments séparés ne sont pas nécessairement parallèles.
- **Concret → schéma → notation** : bandelettes droites et tiges articulées; contours contrastés et sommets marqués; coordonnées de sommets reliés dans l'ordre et justification « côté AB // CD ». Rappeler qu'une translation, un quart de tour ou un agrandissement uniforme préserve le nombre de côtés et le parallélisme.
- Voir `contenu/01_NOTIONS_ET_EXEMPLES.md` : deux exemples résolus, trois contre-exemples et calculs exacts.

## 3. Préparation / diagnostic
- **`requires` : aucun.** Lien de séquence non contraignant : `qc-pri-ma-021`; les autres identifiants ne sont pas du contenu à recopier.
- `diag-1` : trier T (triangle), R (quadrilatère) et C (cercle) selon « polygone / non-polygone », puis compter les côtés; un schéma ou des tiges sont autorisés.
- `diag-2` : trier deux quadrilatères ayant respectivement une et deux paires de côtés opposés parallèles; demander *pourquoi l'autre n'appartient pas au groupe*. Réponses et décision dans `contenu/02_DIAGNOSTIC.md`.
- Résultat : maîtrise déjà observable → épreuves autonomes inédites; confusion côté/segment courbe → mini-leçon ciblée; confusion parallélisme → travail avec droites prolongées. Le diagnostic ne bloque pas l'accès.

## 4. Enseignement guidé
- `teach-1` : expliciter « Je ne trie ni par l'inclinaison ni par le nom, mais par un test visible et stable »; fabriquer un quadrilatère avec quatre bandes, souligner les côtés opposés et prolonger leur support en pointillé.
- Modéliser R : A(0,0), B(4,0), C(4,2), D(0,2), reliés dans cet ordre. Quatre côtés et sommets; AB // CD et BC // DA : **2 paires**. Comparer à Q : A(0,0), B(5,0), C(4,2), D(1,2) : AB // CD, mais BC non // DA : **1 paire**.
- Mettre en mots la non-appartenance : « Q ne fait pas partie des quadrilatères ayant deux paires de côtés opposés parallèles, car il n'en a qu'une ».
- Contrôle : « Un quadrilatère tourné devient-il un triangle ? Pourquoi ? » Réponse : non, toujours 4 côtés. Voir `contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée
- `guided-1` : **G1** compter côtés/sommets de T, R et C avec repères visuels et verbalisation; **G2** repérer dans trois quadrilatères les 0, 1 et 2 paires avec aide partielle; **G3** classer sans modèle visible et expliquer un contre-exemple.
- Indices dégressifs : entourer un sommet et tracer un côté → seulement rappeler de comparer les côtés opposés → aucun indice avant tentative; correction après justification.
- Enseignant·e : relever les preuves et utiliser une rétroaction de procédure, pas simplement « bon/mauvais ». Résolutions détaillées `contenu/04_PRATIQUE_ACCOMPAGNEE.md`.

## 6. Pratique autonome
- `independent-1` : quatre tâches indépendantes inédites (classement par nombre de côtés, appartenance polygonale, paires parallèles, tri multicritère) dans `contenu/05_PRATIQUE_AUTONOME.md`. Documents et tiges possibles pour matérialiser, sans aide sur le critère.
- Exiger le tri **et** une exclusion justifiée; consigner l'énoncé exact, la production et les aménagements dans le LMS local, pas dans le canon.
- Les figures sur quadrillage sont spécifiées par coordonnées pour éliminer l'incertitude d'une impression ou d'un dessin à main levée.

## 7. Feedback et erreurs typiques
- **E1** « un carré incliné n'a plus ses côtés opposés parallèles » → faire tourner un modèle en carton et vérifier les deux paires inchangées.
- **E2** « côtés qui ne se touchent pas = parallèles » → prolonger deux droites supports sécantes et montrer le point de rencontre.
- **E3** « un cercle a un côté courbe » → distinguer contour courbe et segments de polygone; le cercle a **0 côté polygonal et 0 sommet**.
- **E4** « 4 sommets, donc 2 paires parallèles » → comparer Q (1 paire) et I (0 paire); compter ne suffit pas.
- **E5** « une paire » veut dire « au moins une paire » → travailler la distinction **exactement une** vs **au moins une** avec exemples.
- Pour toute erreur : question ciblée → représentation de remplacement → contre-exemple → nouvel essai isomorphe, sans dicter la réponse initiale.

## 8. Évaluation formative et preuves
- `qc-pri-ma-023-ev-01` → `obj-1` et `crit-1`; mode privilégié **paramétrique contrôlé** (transformations déterministes des coordonnées sur un corpus borné). Aucun tirage IA libre.
- Les items `q-001` à `q-008` sont des ancrages ciblés, `q-009` et `q-010` des variantes déterministes; `q-011` (mosaïque) et `q-012` (jardin) constituent deux manifestations de maîtrise à contextes distincts. Voir `evaluation/PLAN_EVALUATION.md`.
- Examiner les classements exacts, les propriétés expliquées et une non-appartenance démontrée dans **chacun** des contextes, sans indices; conserver le raisonnement oral transcrit ou écrit.
- Les items portent `validation_status: a_revoir` jusqu'à revue humaine et essai auprès des apprenants; pas de certification automatique.

## 9. Remédiation / enrichissement
- Soutien court et adaptatif par erreur (`contenu/06_REMEDIATION_ET_TRANSFERT.md`). Si erreur sur côtés/sommets, manipuler T et C; si sur parallèles, prolonger les supports; si sur le nombre exact de paires, comparer R/Q/I et cocher une grille.
- Enrichissement : analyser une figure tournée; déduire que toutes les figures à 4 côtés ne possèdent pas des côtés opposés parallèles; expliquer pourquoi la couleur ou l'orientation ne sont pas des critères géométriques.
- Transfert 1 : mosaïque de classe. Transfert 2 : plan du jardin. Aucun verrou ni changement d'un autre workspace.

## 10. Accessibilité
- Fournir ensemble texte structuré, liste de coordonnées, quadrillage grand format et tiges mobiles; ne pas transmettre le seul dessin en couleur; contraste et lignes distinctes.
- Chaque figure est désignée par une lettre et ses sommets dans l'ordre; consigne lisible à voix haute ou par lecteur d'écran; éviter de noter l'habileté graphique ou la dextérité.
- Réponses écrites, dictées à un scribe, orales enregistrées ou par étiquettes tactiles, avec justification explicitée. Le scribe **ne donne pas d'indice de classement**.
- En cas de difficulté de lecture, lire la consigne; conserver l'exigence logique de tri et d'exclusion. Pas de minutage obligatoire. Carton/tiges utilisables sans indices de correction.

## 11. Critères de sortie
- `crit-1` : produire **deux tris indépendants corrects**, l'un pour une mosaïque de classe et l'autre pour un plan de jardin, sur des figures nouvelles et avec règles explicites.
- Dans chaque tâche : (1) toutes les figures incluses/exclues sont classées selon la règle, (2) l'élève relève pour chacune les paires parallèles utiles, (3) il/elle justifie au moins un **cas de non-appartenance** par une propriété vérifiable; pas de soutien cognitif ni révélation de la réponse.
- Distinguer : *acquis stable* après les deux contextes; *à consolider* si une justification/forme échoue; *non démontré* si le tri est généralement incorrect; *preuve insuffisante* si accessibilité ou énoncé a empêché d'observer la compétence. Aucun pourcentage unique comme décision.
- Rappel différé : 2 à 7 jours plus tard, refaire un tri inédit avec un quadrilatère incliné et un quadrilatère sans paire parallèle; expliquer une exclusion, puis ajuster si oublié. Ne pas confondre rappel et deuxième preuve si mêmes figures.

## 12. Références pédagogiques et limites
- Gouvernance consultée dans le ZIP source : `CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md`; origine des liens : `registry/GRAPHE_PEDAGOGIQUE_202.json`.
- `sources/REFERENCES_CONTENU.md` distingue documents effectivement consultés, déductions mathématiques testées et créations originales. Les références EEF/IES/CAST sont **mentionnées par le workspace**, non vérifiées individuellement sur le Web dans cette livraison.
- La charte Québec fournit l'appellation **Mathématique**, pas une homologation PFEQ ni une affectation à une année. Revue humaine toujours requise pour accessibilité, formulation, pertinence et utilisabilité des tâches. Le canon, les registres et le contrat de formation central ne sont pas modifiés.
