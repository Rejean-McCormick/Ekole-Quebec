---
format: qc.learning-path/1.0
id: qc-pri-ma-033
titre: Justifier et communiquer une démarche mathématique
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Communiquer un raisonnement mathématique vérifiable, au-delà du résultat.
objectifs_secondaires: []
criteres_reussite:
- Présenter une solution cohérente et repérer l’erreur d’un autre raisonnement.
prealables_declares: []
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-033-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-033`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Justifier et communiquer une démarche mathématique  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**Statut :** contenu pédagogique proposé, contrôlé sur le plan arithmétique; revue humaine requise, ni canon v9 ni cours publié.

## 1. Intention et frontières

- `obj-1` — **Résultat vérifiable IMMUTABLE :** Communiquer un raisonnement mathématique vérifiable, au-delà du résultat.
- `crit-1` — **Preuve autonome IMMUTABLE :** Présenter une solution cohérente et repérer l’erreur d’un autre raisonnement.
- Notions : **justification, représentation, contrôle, conclusion**. On travaille le *pourquoi* de l'opération et la vérifiabilité des étapes, pas la simple mémorisation d'un résultat.
- Une solution communicable donne la question, les unités, un modèle pertinent, une ou plusieurs étapes explicitées, un contrôle indépendant, une conclusion et une analyse de l'erreur présentée.
- **Frontières :** calculs de nombres entiers accessibles par le diagnostic (additions, soustractions, multiplications, divisions exactes, périmètres de rectangles). Aucun enseignement avancé ni relation cachée à d'autres Kristals. La difficulté des nombres se module sans changer l'objectif argumentatif.
- Produits de la leçon : `../contenu/01_NOTIONS_ET_EXEMPLES.md` à `06_REMEDIATION_ET_TRANSFERT.md`; évaluation : `../evaluation/PLAN_EVALUATION.md`.

## 2. Notions et représentations

1. **Justification :** une affirmation étayée par une relation mathématique vérifiable. « 4 sacs de 6 billes donnent 4 × 6 = 24 billes parce que chaque sac contient 6 billes » est une justification; « j'ai deviné 24 » ne l'est pas.
2. **Représentation :** correspondance explicite entre quantités de la situation et objets, croquis étiqueté, tableau, expression ou phrase; elle rend les quantités et leurs unités contrôlables. Un dessin sans légende peut être insuffisant.
3. **Contrôle :** vérification distincte du calcul initial : recomptage groupé, opération inverse, estimation ou comparaison d'unités. Répéter exactement l'affirmation initiale ne constitue pas un contrôle indépendant.
4. **Conclusion :** réponse contextualisée à la question, avec nombre et unité cohérents. « 22 » seul n'indique ni ce qui a été calculé ni à quoi il correspond.
5. **Repérage d'erreur :** nommer la *première* étape injustifiée, montrer pourquoi elle ne correspond pas aux quantités et reconstruire une démarche correcte sans ridiculiser l'auteur.

**Représentations graduées :** matériel (jetons en rangées) → schéma annoté (rangées et retraits) → égalités avec unités → phrases justificatives. Pour un rectangle, distinguer longueurs du contour (périmètre) et carreaux intérieurs (aire). Plusieurs méthodes exactes sont recevables si la correspondance est explicite. 

**Modèle intégral A :** 4 boîtes de 6 crayons, plus 3 crayons isolés → quatre groupes de six et trois jetons → 4 × 6 + 3 = 27 crayons → vérification 6 + 6 + 6 + 6 + 3 = 27 → « Il y a 27 crayons ». Le calcul 4 + 6 + 3 = 13 confond nombres de groupes et éléments par groupe. Voir les deux autres exemples et contre-exemples dans `../contenu/01_NOTIONS_ET_EXEMPLES.md`.

## 3. Préparation / diagnostic

- **Préalables stricts `requires` :** aucun. **Ordre conseillé :** aucun. **Renforcement/transfert inter-Kristals :** aucun. Le graphe v1.2 ne crée pas de verrou.
- Présenter sans indice les deux tâches de `../contenu/02_DIAGNOSTIC.md`, dont une solution à justifier et une erreur à analyser. Observer séparément le calcul, la représentation, l'explication, le contrôle et l'analyse d'erreur.
- `diag-1` : 3 rangées de 4 chaises, 2 retirées : expliquer pourquoi 3 × 4 − 2 = 10, montrer par rangées, invalider « 3 + 4 − 2 = 5 ».
- `diag-2` : 18 cartes réparties également dans 3 enveloppes : montrer 18 ÷ 3 = 6 cartes/enveloppe, critiquer « 18 − 3 = 15 cartes/enveloppe » au moyen du contrôle 3 × 6 = 18.
- Décision formative : si l'élève réussit les deux avec étapes, erreur localisée et contrôle, raccourcir le guidage et proposer immédiatement deux cas neufs. Sinon remédier *la dimension manquante* (sens de l'opération, mise en image, vérification, justification, formulation). Ne jamais bloquer par niveau scolaire ou par un autre ID.

## 4. Enseignement guidé

- `teach-1` : expliciter l'objectif, puis afficher la grille des cinq questions : **Que cherche-t-on? Que représente chaque nombre? Pourquoi cette opération? Comment vérifier autrement? Quelle conclusion?**
- Démonstration orale + écrite : le gymnase prépare 4 paniers de 5 ballons et en prête 3 : matériel 4 groupes de 5, puis enlever 3; schéma « (5+5+5+5)−3 »; symboles « 4 × 5 − 3 = 17 »; contrôle « 17 + 3 = 20 »; conclusion « Il reste 17 ballons de ces paniers ».
- Contre-démonstration : « 4 + 5 − 3 = 6 » ne représente pas quatre groupes de cinq. Faire entourer le premier saut illégitime (« 4 + 5 ») et proposer la correction; 6 n'est pas défendable avec les unités décrites.
- Élargir au contrôle d'un résultat exact obtenu par hasard : pour 6 m × 2 m, le contour est 6+2+6+2=16 m; « 6×2+4=16 » n'est pas une formule générale. Pour 5×3, elle donnerait 19 m alors que le contour vaut 16 m.
- **Pause explicite de compréhension :** inviter l'élève à expliquer la différence entre une *justification* et une *affirmation*, puis entre une *vérification indépendante* et le même calcul répété.
- Version complète dans `../contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

- `guided-1` : réaliser les trois activités graduées de `../contenu/04_PRATIQUE_ACCOMPAGNEE.md`.
  1. Six paquets de quatre autocollants moins cinq distribués. Indices forts : dessin des paquets, phrase à trous, vérification inverse. Résultat 19 autocollants; erreur « 6+4−5 » explicitée.
  2. 28 cartes partagées entre quatre équipes. Indice intermédiaire limité à « combien par équipe? ». Résultat 7; invalider « 28−4=24 par équipe » par 7×4=28.
  3. Un rectangle de 8 cm par 3 cm : sans schéma fourni, retrouver le périmètre 22 cm, le justifier, corriger « 8×3=24 cm ». Après effort, un unique indice « suis le contour » peut être donné, mais la réussite finale nécessite un autre essai sans indice.
- Diminuer les indices **entre** les activités; après une erreur, donner une question qui cible le maillon défaillant, non la réponse entière. Séparer réussite accompagnée et preuve autonome.

## 6. Pratique autonome

- `independent-1` : quatre tâches originales de `../contenu/05_PRATIQUE_AUTONOME.md`, sans indice ni correction visible au premier essai : réserves de ballons, livraisons de boîtes, partage de cartes, contour d'un terrain.
- Pour chaque tâche : modèle / représentation étiquetée, égalité exacte, une phrase « parce que », contrôle *distinct*, conclusion et correction localisée du raisonnement fictif erroné. Accepter écriture, enregistrement oral avec croquis, manipulation enregistrée ou saisie structurée, si les mêmes exigences sont observables.
- Les corrigés du fichier sont destinés à l'enseignant ou à l'autoévaluation **après la production**. Les deux preuves de sortie `q-009` et `q-010` emploient d'autres données et un autre habillage; pas de réutilisation mot pour mot des réponses.

## 7. Feedback et erreurs typiques

- `error-1` — Confondre nombre de groupes et effectif de chaque groupe (« 4 + 6 » au lieu de 4 × 6) : demander une rangée par groupe, entourer l'unité des nombres et justifier chaque opération.
- `error-2` — Bon résultat sans raison valide : utiliser un **autre cas** (6×2 puis 5×3 pour le périmètre) afin de tester la généralité; ne pas valider une formule parce qu'elle coïncide une fois.
- `error-3` — Contrôle circulaire : remplacer « je recalcule pareil » par opération inverse, dénombrement ou autre représentation; nommer ce qui a été vérifié.
- `error-4` — Confondre périmètre et aire : suivre physiquement les quatre côtés du rectangle plutôt que compter les carreaux intérieurs.
- `error-5` — Dire seulement « c'est faux » : localiser l'étape précise, expliquer l'unité erronée et fournir une réparation respectueuse.
- `error-6` — Omettre unité / conclusion : retourner à « combien de quoi? ». Feedback formatif descriptif et mini-essai de remplacement, voir `../contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 8. Évaluation formative et preuves

- **Famille inchangée :** `qc-pri-ma-033-ev-01`, **objectif :** `obj-1`, **critère :** `crit-1`, **type favorisé :** `paramétrique_controle`.
- Banque : 10 items `q-001` à `q-010`; 6 paramétriques à trois variantes finies calculées, 2 fixes et 2 épreuves de sortie avec scénario figé. Aucun générateur IA libre n'est admis comme contrôleur.
- `q-009` : **bibliothèque** (quantités de livres regroupées et prêtées); `q-010` : **aménagement d'un jardin** (périmètre et confusion avec l'aire). Les deux sont requises comme preuves distinctes sans aide; chaque élève doit présenter une solution vérifiable ET expliquer précisément une erreur d'autrui dans les deux contextes.
- Appliquer `../evaluation/PLAN_EVALUATION.md` et `../evaluation/GRILLE_MAITRISE.md`. Le score descriptif soutient la décision mais **aucune note isolée** ne la détermine. Conserver les traces dans un dispositif d'apprentissage externe, sans ajout au canon.
- Contrôles des variantes : catalogues bornés, graine fixe et algorithme explicite; tests techniques arithmétiques réalisés, essai élève et validation humaine non réalisés.

## 9. Remédiation / enrichissement

- Remédiations A–E dans `../contenu/06_REMEDIATION_ET_TRANSFERT.md` : groupes/unités, explication d'opération, contrôle indépendant, périmètre/aire, diagnostic de la première erreur.
- Après erreur, l'élève reformule la réparation puis tente une tâche de même structure sur **d'autres nombres**. Une simple répétition du corrigé ne valide pas la remédiation.
- Transfert 1 (organisation d'un atelier scientifique) : compter 5 bacs de 4 fioles et 3 utilisées, soit 17 restantes, justifier et rectifier « 5+4−3 »; contrôle 17+3=20.
- Transfert 2 (planification d'une affiche rectangulaire) : panneau de 9 dm × 2 dm, contour 22 dm et non aire 18 dm², expliquer choix d'opération et erreur d'une autre démarche.
- **Rappel différé :** à J+2, donner 3 sachets de 7 perles et 4 utilisées (17 restantes) à justifier sans modèle. À J+7, rectangle de 4 cm × 7 cm, évaluer « 4×7=28 cm de ruban » et montrer 22 cm. Si hésitation, micro-remédiation ciblée; ne pas compter le rappel comme deuxième preuve tant que l'autonomie n'est pas visible.
- **Enrichissement :** analyser deux raisonnements produisant le même nombre dans un seul cas et construire un contre-exemple où ils divergent.

## 10. Accessibilité

- Proposer énoncé lu, police lisible, texte segmenté, schémas textuels alternatifs, matériel manipulable non dangereux, papier quadrillé ou tableau et temps adaptable. Décrire oralement rangées et côtés pour accès non visuel.
- Un élève peut répondre oralement avec enregistrement/transcription et gestes sur matériel; la preuve doit toujours montrer les quantités, opérations, contrôle, conclusion et erreur repérée. La maîtrise de la calligraphie n'est pas évaluée.
- Les diagrammes doivent porter les unités en toutes lettres et ne jamais dépendre seulement de couleurs. Les versions paramétriques restent dans de petits entiers et avec partage exact. Ne pas injecter de contexte personnel, financier sensible ou culturellement opaque.
- Prévenir la divulgation de données privées; personnages fictifs, aucune mesure réelle de personnes. Corrigés et aides cachés au moment de la preuve autonome.

## 11. Critères de sortie

1. Dans **deux contextes distincts**, présenter une solution numérique correcte avec représentation reliée aux données et justification des opérations.
2. Montrer un contrôle non circulaire; formuler une conclusion exacte incluant l'unité.
3. Dans **chacun des deux contextes**, localiser l'erreur du raisonnement fictif, expliquer pourquoi elle est invalide et proposer une réparation mathématiquement valable.
4. Être autonome : aucun indice, suggestion d'opération, modèle à compléter ou confirmation pendant la prestation; seules les adaptations d'accès non cognitives sont admises.
5. Appliquer la grille analytique; niveau 2 requis sur chacun des axes essentiels dans les deux manifestations. Une performance partielle entraîne une reprise ciblée suivie d'une nouvelle tâche, jamais l'attribution automatique de maîtrise à partir d'un total.

## 12. Références pédagogiques et limites

- **Sources effectivement consultées :** contrat et générateur v1.2, charte de conversion, graphe central, frame source, alignement et brief `qc-pri-ma-033`. Traçabilité : `../sources/REFERENCES_CONTENU.md`.
- **Appellations :** « Mathématique » est une étiquette de discipline; pas de certification ni de conformité PFEQ revendiquée. `ALIGNEMENT.md` n'est pas modifié; code de cours officiel : `null`.
- **Statut scientifique :** contenu de conception et calculs contrôlés localement; ces documents ne constituent ni un état canonique construit, ni un examen validé sur un échantillon d'élèves. Revue humaine de la progression, équité, clarté des consignes et de la cotation obligatoire avant qualification.
- **Livraison :** remplacement du présent fichier et de `CONTRAT_PEDAGOGIQUE.json`, ajout de 12 fichiers seulement. Les propositions de changement éventuel sont enregistrées dans `../livraison/VALIDATION.md`, sans modification des bases centrales.
