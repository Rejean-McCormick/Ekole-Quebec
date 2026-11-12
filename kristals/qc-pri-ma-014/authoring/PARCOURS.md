---
format: qc.learning-path/1.0
id: qc-pri-ma-014
titre: 'Fractions : opérations selon la progression'
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Effectuer des opérations élémentaires sur les fractions en conservant leur sens.
objectifs_secondaires: []
criteres_reussite:
- Résoudre une situation illustrée sur des fractions et vérifier le résultat.
prealables_declares:
- qc-pri-ma-013
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-014-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-014`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Fractions : opérations selon la progression  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**Statut :** matériel didactique rédigé pour validation humaine; aucune publication ni qualification acquise.

## 1. Intention et frontières

- **`obj-1` — objectif observable immuable :** Effectuer des opérations élémentaires sur les fractions en conservant leur sens.
- **`crit-1` — preuve autonome immuable :** Résoudre une situation illustrée sur des fractions et vérifier le résultat.
- Les notions enseignées sont **fraction unitaire**, **addition compatible** et **décomposition**. Pour donner sens à « opérations élémentaires », on traite aussi le **retrait** de parts de même unité, l'addition et la recomposition; la soustraction n'introduit pas une nouvelle famille.
- Domaine de base : un tout identifié, partagé en `d` parties *égales*, `d ∈ {2,3,4,5,6,8,10}`, numérateurs entiers non négatifs et quantités comprises entre 0 et 1. Les fractions d'un tout distinct ne s'additionnent pas comme si le tout était commun.
- La notation impropre et l'addition de dénominateurs différents ne font **pas** partie des exigences de sortie. L'équivalence est utilisée pour vérifier (`4/8 = 1/2`), sans en faire une opération nouvelle; son acquis relève du préalable `qc-pri-ma-013` ou d'une attestation diagnostique équivalente.
- Un résultat numérique sans unité, partition, démarche et vérification n'est pas une preuve suffisante de maîtrise.

## 2. Notions et représentations

1. **Fraction unitaire** `1/d` : une des `d` parts égales d'un même tout; pour `d=4`, `[■□□□]` représente `1/4`. Quatre carrés de surfaces inégales ne représentent pas des quarts.
2. **Addition compatible** `a/d + b/d = (a+b)/d` si les deux collections de parts réfèrent à la **même unité entière**, à des parts de même taille et si `a+b ≤ d` dans le domaine travaillé. On réunit des parts, on ne réadditionne pas leur taille. Exemple : `2/8 + 3/8 = 5/8`.
3. **Décomposition** : `a/d = b/d + (a−b)/d` pour `0 ≤ b ≤ a`; aussi `a/d` équivaut à `a` fois `1/d`. Exemple : `5/6 = 2/6 + 3/6`.
4. **Retrait compatible** : `a/d − b/d = (a−b)/d` pour `0 ≤ b ≤ a`; le modèle reste une même unité et partition.

Représentations coordonnées : bande de parts égales, description textuelle complète (pas uniquement les couleurs), manipulation de jetons/segments égaux, écriture fractionnaire et phrase de vérification. Les illustrations textuelles `[■■■□□□]` désignent **six cellules de largeur égale du même tout**, dont trois occupées. L'élève doit pouvoir nommer à quoi correspond le tout.

**Exemple résolu E1 :** un carré quadrillé en 8 cases de même aire; 2 cases + 3 cases occupées = 5 cases : `2/8 + 3/8 = 5/8` (schéma `[■■■■■□□□]`). Contrôle par l'opération inverse : `5/8 − 3/8 = 2/8`.

**Exemple résolu E2 :** une piste divisée en 10 segments égaux; 7 segments parcourus, puis on revient de 2 segments : `7/10 − 2/10 = 5/10 = 1/2`. Contrôle : `5/10 + 2/10 = 7/10`; le résultat est inférieur au point de départ.

**Contre-exemple C1 :** `1/3 + 1/4 = 2/7` est faux : les parts n'ont pas la même taille; une conversion préalable donnerait `4/12 + 3/12 = 7/12`, abordée seulement comme distinction, pas comme exigence opératoire de ce microparcours.

**Contre-exemple C2 :** additionner `1/4` d'une petite tarte et `1/4` d'une grande tarte comme `1/2` de *la même* tarte est invalide : le tout est différent; on peut parler de deux portions, pas les réunir en fraction d'une unité commune sans la définir.

## 3. Préparation / diagnostic

- **Lien strict :** `requires(qc-pri-ma-014, qc-pri-ma-013)` pour l'équivalence/comparaison; aucun `recommends_before` ni `reinforces` sortant. Le diagnostic peut attester un acquis équivalent et ouvrir l'accès sans imposer la consultation du Kristal précédent.
- **`diag-1` :** présenter `[■■□□]` (4 quarts égaux) et `[■□]` (2 moitiés égales) représentant des touts de même grandeur; demander si `2/4 = 1/2` et pourquoi. Attendu : même aire / même longueur occupée; ne pas retenir la réponse « oui » seule.
- **`diag-2` :** dans une bande de six parts égales, comparer `3/6` et `4/6`, puis marquer les deux quantités. Attendu : `3/6 < 4/6`, une part de différence.
- **Sonde d'entrée non éliminatoire :** représenter `1/6 + 2/6` par six cases et justifier `3/6`. Ceci situe l'accompagnement à prévoir, sans transformer les futures réponses d'examen en diagnostic de préalable.
- **Décision :** si `diag-1` et `diag-2` sont correctement justifiés, noter une attestation équivalente du préalable (trace dans LMS, pas dans le registre); sinon proposer une reprise ciblée de `qc-pri-ma-013` ou un soutien d'équivalence, puis refaire deux situations distinctes. Aucun blocage fondé sur la seule absence de suivi administratif.

## 4. Enseignement guidé

**`teach-1` — modelage « je fais, j'explique, je vérifie » :** montrer une bande *entière* divisée en 8 parts égales. Placer 2 parts, ajouter 3 parts nouvelles de cette **même bande**, compter les cinq parts sans redessiner le tout. Dire : « Le huit indique la taille fixe des parts; le numérateur compte les parts. Donc `2/8 + 3/8 = 5/8`. » Effacer/retirer ensuite 3 parts pour vérifier `5/8 − 3/8 = 2/8`.

**Deuxième modelage :** `5/6 = 1/6 + 4/6 = 2/6 + 3/6`; les deux découpages couvrent exactement cinq sixièmes du même rectangle. Montrer en quoi les décompositions sont différentes mais de même valeur.

**Contrôles oraux/écrits :** « Quelle est notre unité? », « Pourquoi conserve-t-on le 8? », « Comment prouver que cinq parts sur huit ne dépassent pas le tout? », « Que devient l'addition si une bande est deux fois plus longue? » Expliquer la dernière comme cas non compatible sans imposer de conversion.

## 5. Pratique accompagnée

**`guided-1` (indices forts) :** une bande de 6 cases; `1/6 + 2/6`. Indices : identifier la bande entière; placer 1 puis 2 marques; recompter; compléter `__/6`. Réponse `3/6 = 1/2`; vérifier avec `3/6 − 2/6 = 1/6`.

**`guided-2` (un indice à la demande) :** sur 8 cases, `5/8 − 2/8`; l'unique indice initial est « Qu'arrive-t-il au nombre de cases occupées? ». Réponse `3/8`; vérifier `3/8 + 2/8 = 5/8`.

**`guided-3` (sans indice préalable, aide seulement après essai) :** marquer `4/6` puis le décomposer en `1/6 + ___`; répondre `3/6`; vérification par recomposition `1/6 + 3/6 = 4/6`. Demander aussi une autre décomposition valide : `2/6 + 2/6`.

**Consigne de feedback commune :** signaler le premier choix de tout, de partition ou d'opération qui diverge, puis demander une correction dessinée et une deuxième tentative sur une bande nouvelle; ne pas offrir d'emblée l'égalité finale.

## 6. Pratique autonome

Quatre tâches inédites sans indices et sans modèle affiché; l'apprenant doit, pour chacune, identifier le tout, représenter la partition, écrire l'opération, puis contrôler le résultat. Voir `contenu/05_PRATIQUE_AUTONOME.md` pour consignes et corrigés.

- **A1 :** une bande de 5 sections égales : `2/5 + 1/5 = 3/5`; contrôle `3/5 − 1/5 = 2/5`.
- **A2 :** un ruban de 8 sections égales : `6/8 − 3/8 = 3/8`; contrôle `3/8 + 3/8 = 6/8`.
- **A3 :** `5/6` d'un rectangle : trouver deux décompositions `2/6 + 3/6` et `1/6 + 4/6`; vérifier les parts réunies.
- **A4 :** une planche de 4 sections égales : `1/4 + 2/4 = 3/4`; contrôle `3/4 − 2/4 = 1/4`.

Retenir la trace du dessin ou de sa description structurée, de l'égalité et de la vérification; un corrigé calculé n'est pas une preuve que la procédure a été autonome.

## 7. Feedback et erreurs typiques

- **Dénominateurs additionnés :** `2/8 + 3/8 = 5/16`. Demander « Combien de parts possède *toujours* la bande? »; revenir aux huit cases, corriger en `5/8`, puis refaire `1/6 + 3/6`.
- **Touts différents :** des « quarts » de grandeurs distinctes sont combinés. Exiger une unité commune, ou déclarer l'opération non justifiée.
- **Parts inégales :** une image à tailles inégales est traitée comme fraction ordinaire. Repartager en segments congruents avant de calculer.
- **Sens de soustraction inversé :** `5/8 − 2/8 = 7/8`. Retirer matériellement deux parts, voir que l'occupation diminue, puis contrôler `3/8 + 2/8 = 5/8`.
- **Équivalence confondue avec changement de quantité :** `4/8 = 1/2` représente la même longueur si les touts sont égaux; justifier par appariement deux à deux, pas par simple récitation.

Après rétroaction, présenter une **nouvelle** partition/nouveaux nombres et observer une justification reformulée.

## 8. Évaluation formative et preuves

- **Famille immuable :** `qc-pri-ma-014-ev-01`; `objectif_ref: obj-1`; `critere_ref: crit-1`; `type: paramétrique_controle` dans le contrat natif; les modes d'items sont `fixe` et `parametrique` selon le contrat de banque.
- **Banque :** 12 items explicites, 8 paramétriques à candidats finis et corrigés exacts; **aucune sortie IA libre**. Seeds reproduisibles et formules/contraintes écrites dans `evaluation/BANQUE_ITEMS.json`.
- **Manifestations essentielles :** `qc-pri-ma-014-q-011` (jardin / partie d'un terrain commun) et `qc-pri-ma-014-q-012` (trajet / part d'une longueur commune), toutes deux illustrées et avec contrôle de l'égalité. Elles sont faites sans indices, à deux occasions distinctes.
- **Grille :** sens du tout et des parts, opération exacte, représentation cohérente, vérification interprétée; niveaux 0, 1, 2 par dimension. Une décision ne découle pas d'une somme unique : les quatre dimensions doivent atteindre 2 sur **chacune** des deux situations, dont au moins une sans matériel aidant au calcul, avec observation authentifiée d'autonomie. Adaptations d'accès permises, non les indices procéduraux.
- **État :** questions `validation_status: a_revoir` jusqu'à revue humaine et essai local; ce matériel n'est pas un examen certifié.

## 9. Remédiation / enrichissement

Si la taille de l'unité est confuse, construire deux bandes de longueur identique puis vérifier des parts égales avant l'écriture fractionnaire. Si l'addition est erronée, revenir à une seule ligne de `d` cases et au compte des parts; si la soustraction échoue, enlever matériellement `b` marques; si la décomposition échoue, partitionner une collection occupée en deux groupes en conservant le total. Pour un apprenant qui réussit, varier `d`, proposer `a/d = (a−1)/d + 1/d` ou comparer deux stratégies de vérification, sans prescrire des opérations à dénominateurs différents.

Deux transferts documentés : **parterre** (`3/8 + 2/8`) et **trajet balisé** (`7/10 − 3/10`); changer les nombres ne remplace pas le changement de contexte. Aucun nouveau `requires`, `reinforces` ou `recommends_before` n'est créé.

## 10. Accessibilité

- Proposer objets identiques, bande contrastée non codée seulement par couleur, grands caractères, descriptions orales ou textuelles des cases et lecture de la consigne; garder visibles le tout et le nombre de parts égales.
- Accepter dessin, tracé tactile, jetons identiques, schéma numérique accessible, dictée à un scripteur neutre ou explication orale transcrite. Le scripteur ne choisit ni l'opération ni la vérification.
- Demander une explication mathématique équivalente quel que soit le mode; éviter minutage inutile, effets d'animation, dépendance exclusive à la couleur, données personnelles et achats réels.
- Si l'outil devient un indice procédural (suggestion automatique du numérateur/résultat), la tentative doit être marquée **assistée** et ne compte pas comme preuve autonome.

## 11. Critères de sortie

1. Sur une illustration de parts égales, nommer le tout, vérifier la compatibilité des parts et poser une addition ou un retrait cohérent.
2. Calculer exactement avec dénominateur conservé, représenter le résultat et pouvoir montrer une décomposition adéquate.
3. **Prouver `crit-1` au moins deux fois dans des contextes distincts** (jardin et trajet), sans feedback en cours de tâche; démontrer une vérification arithmétique **et** sa cohérence avec la représentation.
4. Enregistrer pour chacune des preuves les quatre critères au niveau 2 et les modalités d'autonomie; si un point manque, prescrire une remédiation ciblée et une nouvelle paire de contextes équivalents, pas un crédit automatique au score.
5. **Rappel différé :** 3 à 7 jours après, faire `2/6 + 3/6 = 5/6` et `5/8 − 1/8 = 4/8 = 1/2`, en exigeant une vérification; puis à 2 à 3 semaines, réactiver par `4/10 = 1/10 + 3/10` et le dessin d'un nouveau tout. Ces intervalles sont des choix internes adaptables, non une prescription ministérielle.

## 12. Références pédagogiques et limites

- **Sources du workspace consultées :** `governance/Norme_Pedagogique_Autonome_v1.2/{CONTRAT_PEDAGOGIQUE_V1.2,GENERATEUR_ET_EXAMENS,CHARTE_CONVERSION_QC,REFERENCES_EVIDENCE}.md`, `registry/GRAPHE_PEDAGOGIQUE_202.json`, et `authoring/{PARCOURS,CONTRAT_PEDAGOGIQUE,ALIGNEMENT,BRIEF_REDACTION}` de ce Kristal. Inventaire et qualification dans `sources/REFERENCES_CONTENU.md`.
- **Conception originale :** bandes dessinées en caractères, scénarios de parterre/route, solutions, rubriques, variantes finies et leur algorithme; aucun recours à une illustration tierce ou à un contenu protégé recopié.
- **Québec :** « Mathématique » n'est qu'une appellation conservée; aucune conformité PFEQ, approbation ou code officiel n'est revendiqué.
- **Limites :** revue humaine pédagogique, lisibilité et accessibilité en situation réelle, vérification d'intégration LMS, pilote auprès d'apprenants et qualification du framework restent à réaliser. Aucune écriture dans `canon/`, `state/`, `runtime/`, `registry/` ou `governance/`.
