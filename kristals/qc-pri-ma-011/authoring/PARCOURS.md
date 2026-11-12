---
format: qc.learning-path/1.0
id: qc-pri-ma-011
titre: Algorithmes et vérification des calculs
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Exécuter, vérifier et expliquer une procédure de calcul écrit.
objectifs_secondaires: []
criteres_reussite:
- Calculer puis détecter une erreur dans une procédure proposée.
prealables_declares:
- qc-pri-ma-003
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-011-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---
# Microparcours — `qc-pri-ma-011`

**Discipline :** Mathématique (appellation québécoise conservée).  
**Titre :** Algorithmes et vérification des calculs.  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`.  
**Statut :** contenu rédigé, contrôles arithmétiques automatisés réalisés; revue humaine et qualification locale requises.  
**Frontmatter YAML :** recopié sans modification de la frame v1.2; le champ historique `statut: en_rédaction` reste conservé intentionnellement.

## 1. Intention et frontières

- **`obj-1`, invariant :** Exécuter, vérifier et expliquer une procédure de calcul écrit.
- **`crit-1`, invariant :** Calculer puis détecter une erreur dans une procédure proposée.
- Les trois notions enseignées sont **algorithme**, **valeur de position** et **contrôle inverse**. L'élève pose et calcule une addition ou une soustraction de nombres naturels (jusqu'à quatre chiffres pour la consolidation, surtout trois chiffres pour les évaluations), avec retenue ou emprunt; en prolongement, une multiplication à deux chiffres par un chiffre illustre la même logique de colonnes. Il repère le **premier pas faux**, corrige et prouve par opération inverse.
- Hors portée : division posée longue, calcul décimal, test de rapidité, mémorisation d'une unique présentation graphique. Une disposition différente est admise si la correspondance des unités est explicite et le résultat contrôlable.
- **Frontière du préalable :** le sens des unités/dizaines/centaines et des échanges relève de `qc-pri-ma-003`; on ne réécrit pas sa feuille.

## 2. Notions et représentations

1. **Algorithme de calcul écrit :** suite finie et justifiable d'étapes opérant sur des chiffres **avec leur valeur de position**. L'alignement en colonnes, le sens des retenues et les échanges sont des propriétés et non de simples gestes appris.
2. **Valeur de position :** dans 704, le 7 vaut 700, le 0 vaut 0 dizaine et le 4 vaut 4 unités. Échange permis : 1 centaine = 10 dizaines et 1 dizaine = 10 unités, sans changer la quantité.
3. **Contrôle inverse :** vérifier une addition `a+b=c` par `c-a=b` (ou `c-b=a`), une soustraction `a-b=c` par `c+b=a`, une multiplication `a×b=c` par `c÷b=a` pour `b ≠ 0` si la division est maîtrisée; sinon par addition répétée/distributivité. La vérification doit être recalculée, pas recopiée.
4. **Trois représentations :** matériel regroupable (jetons/barres/blocs), tableau C-D-U pour visualiser les échanges, écriture alignée; passage progressif au symbole seul. Voir `contenu/01_NOTIONS_ET_EXEMPLES.md`.
5. **Contre-exemples :** 268+157 annoncé 325 (retenue des dizaines oubliée) et 602−175 annoncé 527 (centaine non diminuée après l'échange). Une réponse fausse peut cacher une bonne étape initiale : nommer précisément la première erreur.

## 3. Préparation / diagnostic

- **`requires` strict :** `qc-pri-ma-003` (valeur de position et regroupements), avec équivalence constatée par diagnostic; **`recommends_before` :** `qc-pri-ma-010`, non bloquant; aucun renforcement/transfert imposé par le graphe.
- **`diag-1`** : représenter 314 comme 3 C, 1 D, 4 U puis échanger 1 C contre 10 D; expliquer pourquoi la valeur ne change pas. **Attendu :** 2 C, 11 D, 4 U = 314.
- **`diag-2`** : calculer 243+125 et vérifier par la soustraction; **attendu :** 368; `368−125=243`, avec chiffres alignés et démarche racontée. Alternative orale/manipulatoire acceptée.
- Si le sens des échanges est démontré malgré l'absence de feuille préalable suivie, on peut reconnaître `qc-pri-ma-003` comme acquis équivalent. Sinon enseigner le micro-palier correspondant avant de poursuivre. Le diagnostic n'est ni un contrôle de vitesse ni une note de maîtrise.

## 4. Enseignement guidé

- **`teach-1`** : annoncer et illustrer « Je calcule, je détecte l'erreur d'une autre solution, je vérifie indépendamment ».
- **Démonstration A (addition)** : 268+157 → 425. Unités 8+7=15, écrire 5, reporter 1 D; dizaines 6+5+1=12, écrire 2, reporter 1 C; centaines 2+1+1=4. Contrôle `425−157=268`. Une copie donne 325 : le premier faux pas est l'oubli de la retenue au rang des centaines.
- **Démonstration B (soustraction)** : 602−175 → 427. Échanger 1 C en 10 D, puis 1 D en 10 U : 5 C, 9 D, 12 U; `12−5=7`, `9−7=2`, `5−1=4`. Contrôle `427+175=602`. La copie donne 527, ayant gardé 6 C après l'échange : premier pas faux aux centaines.
- Enseigner la distinction **résultat**, **procédure**, **vérification**. Demander : « Pourquoi l'échange n'a-t-il pas modifié 602? » Voir `contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

- **`guided-1`** : 346+287, contrôle inverse et correction de 533; indices complets (tableau et retenues). Résultat 633.
- **`guided-2`** : 703−268, contrôle inverse et correction de 535; indice partiel « il y a zéro dizaine : où prendre une dizaine? ». Résultat 435.
- **`guided-3`** : 58×3, correction du calcul 164 et vérification; aucun indice d'avance, question seulement après essai. Résultat 174.
- Pour chaque tâche, expliquer **le premier pas erroné**, le rang, la correction, puis une vérification. Accorder une rétroaction ciblée et retirer l'aide. Voir `contenu/04_PRATIQUE_ACCOMPAGNEE.md`.

## 6. Pratique autonome

- **`independent-1`** : quatre productions nouvelles, sans solution visible pendant l'essai : addition avec retenues, soustraction à travers zéro, alignement de nombres de longueurs différentes, multiplication courte. Activités et corrigés dans `contenu/05_PRATIQUE_AUTONOME.md`.
- **Tâches de transfert obligatoires en deux contextes distincts :** `qc-pri-ma-011-q-011` (inventaire de bibliothèque, addition) et `qc-pri-ma-011-q-012` (billets d'un centre communautaire, soustraction). Ces deux preuves sont autonomes, sans indice, à des moments distincts si possible.
- L'apprenant doit **produire le calcul**, **repérer la première erreur d'une copie**, **expliquer le rang concerné**, **vérifier par inverse**. Consigner seulement dans le système d'apprentissage la production de l'élève, pas dans les fichiers source.

## 7. Feedback et erreurs typiques

- **`error-1`**, oublier une retenue : « Quel nombre as-tu échangé? Où la nouvelle dizaine ou centaine apparaît-elle? » Représenter 10 U comme 1 D, recommencer sur 159+276.
- **`error-2`**, emprunter à 0 D directement : « D'où vient la dizaine? Que reste-t-il en centaines après l'échange? » Revenir à 501−176 avec un tableau C-D-U.
- **`error-3`**, mauvaise colonne : « Compare les unités sous les unités et non sous les dizaines. » Refaire 507+68 à l'aide d'un quadrillage.
- **`error-4`**, vérification recopiée ou circulaire : imposer l'opération inverse par un chemin distinct, puis contrôler la somme/deuxième calcul sans voir l'original.
- **`error-5`**, résultat sans unité ou ordre de grandeur absurde : demander une estimation préalable et contextualiser (objets, billets).
- Voir `contenu/06_REMEDIATION_ET_TRANSFERT.md` pour les micro-remédiations, nouvelle tentative et rappel espacé.

## 8. Évaluation formative et preuves

- **Famille `qc-pri-ma-011-ev-01` / `obj-1` / `crit-1`** et préférence `paramétrique_controle` préservées; banque `evaluation/BANQUE_ITEMS.json` : 12 items, dont 8 à générateur déterministe borné et 4 ancrages fixes.
- Les jeux de couples admissibles sont **énumérés**, l'indice est déterminé par `seed % longueur_du_jeu` et le corrigé découle d'une arithmétique entière exacte; les modèles de copies erronées décrivent une erreur définie, non un tirage de texte IA.
- **Maîtrise :** deux manifestations satisfaisantes dans des contextes distincts (`q-011`, `q-012`), les deux sans assistance et avec calcul, détection, justification et contrôle indépendant. Même score numérique isolé ≠ décision de maîtrise.
- Les critères et conditions sont dans `evaluation/PLAN_EVALUATION.md` et `evaluation/GRILLE_MAITRISE.md`; tous les items restent `a_revoir`, non certifiés.

## 9. Remédiation / enrichissement

- Intervention diagnostic selon le premier écart constaté, puis exercice différent : retenue mal transportée → échanges; emprunt à zéro → C-D-U; alignement → tableau quadrillé; inverse peu fiable → recomposition `c+b=a` et comparaison par estimation.
- **Enrichissement :** demander deux procédures valides (colonne, décomposition), expliquer pourquoi elles concordent et identifier l'erreur possible d'une copie nouvelle; la division longue ne devient pas un prérequis.
- Aucun lien supplémentaire au graphe et aucun verrou nouveau. La variation du contexte ne modifie pas la preuve attendue.

## 10. Accessibilité

- Grands chiffres alignés, repères C-D-U, en-têtes de colonnes énoncés à l'oral, matériel regroupable ou schémas textuels; supports compatibles lecteur d'écran, sans code couleur obligatoire.
- Permettre de dicter les opérations et la justification, d'écrire sur quadrillage, de pointer une colonne ou de déplacer des jetons; la **justesse mathématique**, le **repérage de l'erreur** et la **vérification** restent obligatoires.
- Aucun chronomètre, aucun contexte supposant des expériences privées ou des moyens financiers. L'aide est permise à l'enseignement; les deux preuves finales doivent être indépendantes, avec les adaptations d'accès maintenues.

## 11. Critères de sortie

1. En situation nouvelle, calcul écrit exact avec échanges correctement explicités, sans aide de contenu.
2. Identifier le **premier pas incorrect** d'une procédure proposée et le corriger en nommant la valeur de position.
3. Effectuer et interpréter un **contrôle inverse exact** plutôt que recopier la solution.
4. **Deux preuves distinctes `q-011` et `q-012`, satisfaisantes séparément**, sans moyenne compensatoire; si une échoue, remédiation ciblée et nouvelle épreuve isomorphe après délai.
5. Vérification différée dans quelques jours (par exemple J+3 ou J+7, selon le rythme local), sans figer une fréquence obligatoire au niveau du graphe.

## 12. Références pédagogiques et limites

- Sources vérifiées **dans l'archive** : norme v1.2, générateur/examens, charte, graphe et frame de `qc-pri-ma-011`; inventaire dans `sources/REFERENCES_CONTENU.md`. Opérations et corrigés : calculs arithmétiques originaux, testés sur les jeux de valeurs fermés; la validation technique ne vaut pas essai auprès d'élèves.
- `authoring/ALIGNEMENT.md` reste intact dans le workspace et rappelle que la discipline est une appellation; aucune homologation PFEQ.
- Références à `qc-pri-ma-003` et `qc-pri-ma-010` : des liens du registre, pas des copies ni des modifications.
- Revue humaine nécessaire : progression, durée, lisibilité des rubriques, accessibilité en classe, essai de passation, intégration LMS / Framework; aucun statut « publié » ou « certifié ».
