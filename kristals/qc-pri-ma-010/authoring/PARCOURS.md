---
format: qc.learning-path/1.0
id: qc-pri-ma-010
titre: Calcul mental et propriétés des opérations
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Choisir une stratégie de calcul mental et mobiliser une propriété opératoire.
objectifs_secondaires: []
criteres_reussite:
- Comparer deux stratégies mentales et expliquer laquelle convient le mieux.
prealables_declares:
- qc-pri-ma-006
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-010-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---
# Microparcours — `qc-pri-ma-010`

**Discipline :** Mathématique — **Titre :** Calcul mental et propriétés des opérations  
**Statut :** contenu rédigé, calculs contrôlés automatiquement; révision humaine requise avant toute qualification.  
**Gouvernance :** norme pédagogique autonome v1.2; le PFEQ n'est pas une norme de validation ici.

## 1. Intention et frontières
- **`obj-1` (immuable) :** Choisir une stratégie de calcul mental et mobiliser une propriété opératoire.
- **`crit-1` (immuable) :** Comparer deux stratégies mentales et expliquer laquelle convient le mieux.
- L'élève choisit une stratégie **adaptée aux nombres**, calcule justement, reconnaît la propriété ou la transformation utilisée et explique *pourquoi* ce choix est efficace pour lui. Une autre stratégie exacte et justifiée demeure acceptable.
- Dans ce Kristal, les opérations travaillées sont l'addition de nombres naturels et la soustraction lorsque le résultat est un naturel; on utilise commutativité/associativité **de l'addition** et compensation **de l'addition ou soustraction**. On ne prétend pas que la soustraction est commutative/associative; la multiplication peut être évoquée comme prolongement facultatif, non requise.
- Ni vitesse chronométrée, ni calcul mental sans trace obligée, ni niveau scolaire arbitraire ne déterminent la maîtrise. Les indices s'effacent progressivement.

## 2. Notions et représentations
- **Commutativité (addition) :** `a + b = b + a` ; on échange les termes, sans en changer la valeur. Exemple : `26 + 14 = 14 + 26 = 40`. Ne pas inverser une soustraction (`26 - 14` n'est pas `14 - 26`).
- **Associativité (addition) :** `(a + b) + c = a + (b + c)` ; on modifie le regroupement, pas les termes. Exemple : `(25 + 37) + 75 = 25 + (37 + 75) = 137`; pour former une centaine, on peut **d'abord** permuter et regrouper : `25 + 75 + 37 = 100 + 37 = 137`. La réorganisation d'une liste de termes invoque généralement les deux propriétés.
- **Compensation :** transformation équilibrée qui conserve le résultat. Addition : `a+b=(a+k)+(b-k)` si `b≥k`. Soustraction : `a-b=(a+k)-(b+k)`; augmenter **les deux** termes d'une même quantité conserve l'écart. Exemple : `48+37=50+35=85`; `154-98=156-100=56`. Vérifier qu'on a effectué les deux ajustements, à bon signe.
- **Représentations :** jetons/dizaines-unités pour former un paquet de dix; segments de droite numérique pour les déplacements; égalités symboliques annotées `+2` et `−2`; courts commentaires oraux, écrits ou pictogrammes. Des schémas textuels sont fournis dans `contenu/01_NOTIONS_ET_EXEMPLES.md`.
- **Choix raisonné :** chercher nombres complémentaires à 10/100, une soustraction près de 100, peu d'étapes sûres; l'efficacité dépend aussi de ce que l'élève sait faire de façon fiable. Deux stratégies peuvent être valides sans qu'une seule soit « meilleure » universellement.

## 3. Préparation / diagnostic
- **Préalable strict :** `qc-pri-ma-006` — Sens et stratégies de l’addition. **Diagnostic d'équivalence permis** : résoudre `36+27` en décomposant (`30+20+6+7=63`) et expliquer pourquoi la somme conserve 63; si correct de manière autonome, la compétence préalable est attestée sans devoir suivre le module antérieur.
- **Ordre conseillé non bloquant :** `qc-pri-ma-007` (voir graphe). Aucune référence `reinforces` sortante.
- **`diag-1` :** `24+16` avec deux représentations (40 par dizaines/unités et saut de 16 sur droite). Vérifier sens de l'addition, regroupement des dizaines, conservation de la somme.
- **`diag-2` :** demander si `42−18` et `18−42` sont interchangeables; puis comparer `42−18=24` à `44−20=24` en montrant un déplacement égal de chaque terme. Ne pas inférer la maîtrise de la compensation d'une seule erreur.
- **Décision :** si les acquis élémentaires manquent, remédier au préalable; sinon choisir les appuis de ce cours. Critère d'entrée et barème détaillés dans `contenu/02_DIAGNOSTIC.md`.

## 4. Enseignement guidé
1. **Rendre visible** une somme avec jetons : `58+27`. Déplacer deux unités de 27 vers 58 : `60+25=85`. Décrire que l'on *transfère*, sans créer ni perdre d'unités.
2. **Modeler** `25+16+75`: regrouper d'abord les deux termes qui font 100, après permutation des termes : `25+75+16=116`. Nommer commutativité et associativité distinctement.
3. **Contraster** `152−98=154−100=54` avec la fausse transformation `152−98=152−100` (deux unités perdues); représenter avec deux flèches `+2` sur les deux termes.
4. **Comparer** méthodes, pas seulement réponses : une suite de calculs sûrs et peu coûteux est souvent préférable; respecter un autre choix justifié.
5. Vérifier : « Quelle propriété autorise à intervertir *des termes d'addition*? » et « Pourquoi ajoute-t-on 2 aux deux termes de la soustraction? » Modèles pas à pas dans `contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée
- **`guided-1`**, indices complets : `36+14+64`. Trier les nombres, pointer les paires 36+64, expliquer commutativité puis associativité; réponse `114`.
- **`guided-2`**, indice partiel : `47+28`. Chercher le prochain multiple de 10 à partir de 47; utiliser `47+3 + (28−3)=50+25=75`; comparer avec `47+20+8=75`.
- **`guided-3`**, sans indice initial : `263−99`; comparer `263−100+1=164` et `(263+1)−(99+1)=264−100=164`; justifier son choix et nommer compensation pour la deuxième.
- Indices **dégressifs** et critères de réponse dans `contenu/04_PRATIQUE_ACCOMPAGNEE.md`; retrait des supports avant preuve autonome.

## 6. Pratique autonome
- **`independent-1` :** quatre travaux différents : (A) `45+55+18` et deux regroupements; (B) `68+27` et deux stratégies; (C) `231−98` et compensation; (D) critique d'une mauvaise associativité en soustraction. Réponses, solutions de rechange et critères dans `contenu/05_PRATIQUE_AUTONOME.md`.
- Formuler pour chaque travail : résultats de **deux** méthodes, propriété/transformation mobilisée, justification de la méthode la plus convenable pour ces nombres et vérification inverse ou estimation. Une méthode plus longue peut être retenue si son choix est mathématiquement étayé.
- Sans indice de procédure; support de lecture ou réponse orale consignable; aucune application à un autre Kristal comme condition cachée.

## 7. Feedback et erreurs typiques
- **Inversion abusive :** `75−18=18−75` ; contre-exemple accessible : `75−18=57`, tandis que `18−75` n'est pas la même soustraction dans les naturels. Revenir à la droite numérique.
- **Associativité abusive :** `90−(30−10)=70`, mais `(90−30)−10=50`. Enlever les parenthèses change le sens.
- **Compensation à sens unique :** `48+37=50+37` est faux (85 contre 87). Ajuster 37 de `−2`.
- **Soustraction :** `154−98` n'est pas `156−98` ; ajouter 2 aux deux termes, pas seulement au premier.
- **Explication insuffisante :** « parce que c'est facile » ; exiger un fait calculatoire observable : « 58 est à 2 de 60; je transfère 2 depuis 27 pour obtenir 60+25 ».
- `contenu/06_REMEDIATION_ET_TRANSFERT.md` contient micro-remédiations, essais neufs et rétroaction graduée.

## 8. Évaluation formative et preuves
- **Famille canonique :** `qc-pri-ma-010-ev-01`, `objectif_id: obj-1`, `critere: crit-1`; 12 items `qc-pri-ma-010-q-001` à `q-012` : six fixes, quatre paramétriques déterministes et deux scénarios contrôlés d'attestation.
- Chaque item demande un calcul exact, une comparaison de stratégies et la justification d'un choix (ou l'identification d'une méthode invalide). Banque, seeds et vérifications sous `evaluation/BANQUE_ITEMS.json`; plan sous `evaluation/PLAN_EVALUATION.md`.
- **Deux preuves indépendantes obligatoires** : `q-011` (kiosque de fruits, addition) et `q-012` (distance de randonnée, soustraction); supports neutres autorisés, sans indices procéduraux, avec administration distincte si possible.
- Grille sur quatre axes : réponse, équivalence ou propriété, comparaison des démarches, justification explicite; maîtrise exige résultats justes et justification valide dans **les deux** contextes, sans effet d'un score isolé.
- Toutes les variantes et rubriques sont au statut `a_revoir` avant examen humain; ce n'est pas une certification.

## 9. Remédiation / enrichissement
- **Erreur de valeur :** regroupement par dizaines/unités puis vérification par un second calcul.
- **Confusion de propriétés :** classer « échanger / regrouper / compenser » sur trois petites cartes avec cas et contre-cas.
- **Choix non justifié :** faire entourer le nombre proche de dix ou de cent et expliquer les ajustements; reformuler sans terme technique avant de l'introduire.
- **Enrichissement :** comparer une méthode par regroupement et une méthode par compensation sur `199+76+1=276`; reconnaître plusieurs solutions valides et leurs limites.
- **Transferts** dans `contenu/06_REMEDIATION_ET_TRANSFERT.md` : inventaire alimentaire et déplacements mesurés; nouveaux nombres, pas une récitation des exemples.

## 10. Accessibilité
- Lire les problèmes ou les présenter en gros caractères, en texte structuré, en code de couleurs facultatif mais toujours accompagné de signes `+`/`−`; privilégier schémas accessibles en texte.
- Permettre jetons, dizaines/unités, droite numérique ou prise de notes de décomposition à l'apprentissage; à l'évaluation de la **stratégie mentale**, la représentation externe peut documenter le raisonnement après le choix, sans fournir l'opération ni la procédure.
- Permettre réponse orale, dictée à un adulte non aidant, clavardage ou écrit; mêmes quatre critères de raisonnement. Pas de pénalité pour lenteur, écriture, aisance orale, trouble moteur ou besoin d'outil d'accès.
- Annoncer unités et vocabulaire concret; éviter contexte culturel présupposé ou achat réel. Des nombres compatibles sont fournis aux deux modalités.

## 11. Critères de sortie
1. Dans **deux contextes** jamais simplement mémorisés, donner le bon résultat ou se corriger de façon autonome avant remise.
2. Comparer deux méthodes pertinentes (ou reconnaître qu'une est fausse), nommer ou décrire une propriété autorisant le passage, sans invoquer une propriété interdite.
3. Choisir celle qui convient le mieux **pour les nombres et pour sa propre maîtrise**, en citant une facilité calculatoire précise; accepter deux préférences différentes si argumentées.
4. Obtenir « acquis autonome » sur **chacune** des deux preuves `q-011` et `q-012` selon la grille; sinon remédiation ciblée et nouvelle preuve inédite.
5. Effectuer un **rappel différé** après 2–7 jours : `69+31+17=117` par regroupement et `245−99=146` par compensation; comparer les choix et expliquer le maintien de l'égalité. Les délais sont des propositions pédagogiques, pas des garanties de mémoire.

## 12. Références pédagogiques et limites
- Source interne consultée : norme v1.2 (`CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md`), registre du graphe, `ALIGNEMENT.md`, `BRIEF_REDACTION.md` et contrat d'auteur; voir `sources/REFERENCES_CONTENU.md`.
- Égalités, corrigés et exemples numériques sont des déductions mathématiques vérifiables. Énoncés, explications et représentations sont des productions originales; aucune licence externe présumée.
- **Limites :** pas d'alignement détaillé ni de validation PFEQ; pas de certification d'item ni revue pédagogique, accessibilité ou essai utilisateur indépendants; pas de publication automatique; pas de modification du registre central.
- **Livrables :** `contenu/01…06`, `evaluation/PLAN_EVALUATION.md`, `BANQUE_ITEMS.json`, `GRILLE_MAITRISE.md`, `sources/REFERENCES_CONTENU.md`, `livraison/MANIFEST.json`, `livraison/VALIDATION.md`.
