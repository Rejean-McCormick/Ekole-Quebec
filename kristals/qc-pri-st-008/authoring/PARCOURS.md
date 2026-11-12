---
format: qc.learning-path/1.0
id: qc-pri-st-008
titre: Énergie et transformations énergétiques
discipline_code: ST
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Repérer des sources d’énergie et décrire les transformations observées.
objectifs_secondaires: []
criteres_reussite:
- Construire un schéma simple d’une chaîne énergétique observable.
prealables_declares: []
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-st-008-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-st-008`

**Discipline :** Science et technologie · **Titre :** Énergie et transformations énergétiques · **Autorité :** gouvernance pédagogique autonome v1.2.  
**État :** contenu rédigé pour revue humaine; ni cours homologué ni items certifiés. Les champs YAML d'identité et de provenance v1.2 demeurent inchangés.

## 1. Intention et frontières

- `obj-1` — **Résultat IMMUTABLE :** Repérer des sources d’énergie et décrire les transformations observées.
- `crit-1` — **Preuve IMMUTABLE :** Construire un schéma simple d’une chaîne énergétique observable.
- L'élève nomme la source qui fournit l'énergie au système considéré; suit une ou plusieurs transmissions; décrit les formes avant et après conversion; relie la chaîne à une trace observable et à un usage. **La source n'est pas une « création d'énergie ».**
- Distinction épistémique : observation (ce qu'on voit/entend), inférence (ce qu'on pense se produire), modèle (schéma explicatif simplifié), conclusion limitée aux indices. Un composant caché (courant, réaction de pile) ne devient pas observable parce qu'on le dessine.
- **Limites :** pas de calcul de rendement, de bilan quantitatif, ni d'expérience avec secteur, chaleur, combustion ou démontage de pile; différencier transfert d'une forme conservée et transformation entre formes. Contenus dans `../contenu/` et évaluations dans `../evaluation/`.

## 2. Notions et représentations

1. **Source :** système ou réserve d'où provient, à l'échelle étudiée, l'énergie utilisée (Soleil, pile, roue déjà mise en mouvement). Expliquer la frontière choisie : le panneau reçoit du rayonnement, il ne crée pas l'énergie.
2. **Transfert :** énergie passant d'un système à un autre; exemple : une énergie électrique transmise par des conducteurs à une lampe, ou le vent entraînant des pales. On indique qui donne et qui reçoit.
3. **Transformation :** passage d'une forme à une autre; exemple : énergie électrique reçue par la lampe → lumière et échauffement. Le passage entre deux objets n'est pas automatiquement un changement de forme.
4. **Usage :** fonction recherchée par l'humain (éclairer, avertir, faire tourner); à distinguer de l'ensemble des sorties d'énergie (chaleur, son).
5. **Schéma standard :** `[source et forme initiale] —transfert→ [convertisseur : entrée → sortie(s)] → [effet observable/usage]`. La flèche décrit un **trajet d'énergie**, pas un trajet d'objets. Pour une pile, le stockage chimique est modélisé; le courant ne se voit pas directement.
6. **Cas de référence :** lampe à piles allumée : pile (réserve chimique) → transfert électrique → lampe (électrique vers lumière + thermique) → éclairer; visible : lumière; inférés : transformations internes. Panneau photovoltaïque + petit ventilateur sans batterie : Soleil (rayonnement) → panneau (électrique) → moteur (mouvement + thermique) → déplacer l'air; visible : pales tournent.

Voir les exemples/contre-exemples et les nuances sur les limites du modèle dans `../contenu/01_NOTIONS_ET_EXEMPLES.md`.

## 3. Préparation / diagnostic

- **Préalables stricts `requires` :** aucun. **Ordre conseillé non bloquant :** `qc-pri-st-007`. **Renforcement externe :** aucun pour le présent Kristal; une relation entrante depuis un autre parcours n'est pas une condition d'accès ici.
- `diag-1` : image décrite « une lampe de poche s'allume quand on actionne l'interrupteur »; distinguer vue de la lumière (observation) et courant de la pile (inférence), puis proposer source et usage.
- `diag-2` : « vent qui fait tourner un moulinet » versus « lampe électrique qui éclaire »; identifier un transfert de mouvement pour le premier et une transformation de forme pour le second.
- Deux réponses indépendantes et entretien oral bref si nécessaire; le diagnostic ne sert **pas** de gate d'accès. Si l'élève fournit déjà une chaîne claire et distingue les niveaux de preuve, accélérer vers les deux contextes autonomes. Sinon, revenir précisément à l'obstacle constaté.

## 4. Enseignement guidé

- `teach-1` — Montrer une courte description (non manipulation) : « une lampe de poche avec pile s'allume quand on appuie sur le bouton ». Nommer **constat** : lumière visible; **modèle** : pile chimique → énergie électrique transmise à la lampe → énergie lumineuse + thermique; **usage** : voir dans l'obscurité. Le chemin est un modèle, pas une photographie de l'électricité.
- Modeler verbalement « Où est la source? Qui reçoit l'énergie? La forme change-t-elle? Quel effet puis-je constater? ». Annoter chaque flèche par transfert et chaque appareil par conversion; expliciter l'échauffement possible sans toucher la lampe.
- Faire réparer « la pile fabrique de l'énergie » par « la pile contient de l'énergie chimique qui peut être transformée ». Contre-test : une pile déchargée ne peut plus fournir de façon utile l'énergie prévue.
- Contrôle immédiat : demander « Qu'a-t-on *vu*? Qu'a-t-on seulement *déduit*? Pourquoi la lumière n'est-elle pas la source? ». Ensuite comparer une simple transmission de mouvement par vent et un convertisseur photovoltaïque. Trame détaillée dans `../contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

- `guided-1` — Trois activités graduées dans `../contenu/04_PRATIQUE_ACCOMPAGNEE.md` : (G1) sonnette à pile, avec étiquettes offertes et phrase à trous; (G2) moulinet poussé par le vent, seules questions-clés; (G3) calculatrice solaire éclairée et en fonctionnement, sans liste de formes : produire un schéma autonome tenté, puis un seul indice si indispensable.
- À chaque activité : **observation ↔ inférence**, source, forme transmise, conversion ou absence de conversion, usage, une sortie non recherchée plausible si pertinente. Réduire les indices; aucune réussite accompagnée n'est comptée comme preuve autonome.

## 6. Pratique autonome

- `independent-1` — Les quatre situations de `../contenu/05_PRATIQUE_AUTONOME.md` : lampe solaire de jardin (sans batterie dans cette version didactique), jouet à ressort, lampe à manivelle, sonnette à pile. Pour chaque situation, produire **un schéma étiqueté** et une phrase qui relie indice et modèle; distinguer transformations et simples passages d'énergie.
- Fournir les descriptions ou lectures orales sans donner les catégories à insérer. Les corrigés n'apparaissent qu'après le travail. La production peut être écrite, dictée ou construite avec étiquettes vierges : le choix des termes reste celui de l'élève.
- Les preuves de maîtrise ne reprennent pas ces scénarios : `q-009` dynamo de vélo, `q-010` ventilateur photovoltaïque d'extérieur.

## 7. Feedback et erreurs typiques

- `error-1` — « énergie apparaît de rien » : revenir au fournisseur d'énergie et ajouter la réserve ou l'apport.
- `error-2` — « transfert = transformation » : faire dire si la forme change effectivement (vent → rotation : mouvement vers mouvement; électricité → lumière : changement).
- `error-3` — « l'usage est la source » : souligner la différence entre fonction (éclairer) et provenance (pile/Soleil).
- `error-4` — « j'ai vu le courant » : demander les indices visibles, reclasser le courant comme inférence du modèle.
- `error-5` — « toute énergie devient utile » : ajouter sortie thermique/sonore lorsque justifiée; le schéma simplifié ne prétend pas quantifier cette sortie.
- L'élève répare son propre schéma puis applique la correction à **un autre** cas. Guide complet de remédiation dans `../contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 8. Évaluation formative et preuves

- **Famille IMMUTABLE :** `qc-pri-st-008-ev-01` · `obj-1` · `crit-1` · type natif `generee_sous_contraintes`.
- Banque `../evaluation/BANQUE_ITEMS.json` : 10 items, 6 `scenario_controle` avec **catalogues fermés et seed stable**, 2 fixes et 2 preuves intégratrices fixes. Le validateur ne génère aucun nouveau texte scientifique libre; les variantes possèdent chacune leur corrigé connu.
- Lien item → objectif/critère/famille décrit dans `../evaluation/PLAN_EVALUATION.md`. Les deux preuves **distinctes** `q-009` (vélo) et `q-010` (ventilateur solaire sans batterie) sont requises, après enseignement, sans aide cognitive.
- Observer quatre axes : source, ordre du schéma et distinction transfert/transformation, preuve observation/modèle, lien au résultat/usage. Cotation séparée sur deux contextes; pas de seuil global déduit d'une seule note. Grille détaillée `../evaluation/GRILLE_MAITRISE.md`.

## 9. Remédiation / enrichissement

- Si source oubliée : tableau « système donneur / récepteur » avant tout schéma. Si transfert confondu avec transformation : contraste moulinet/lampe. Si flèches inversées : partir de l'indice d'utilisation et remonter vers l'alimentation. Si hypothèse présentée comme constat : deux colonnes « visible / modèle ».
- **Transfert T1 :** école — éclairage automatique avec panneau solaire et lampe, données fictives contrôlées, interpréter un schéma à partir de la situation décrite.
- **Transfert T2 :** milieu naturel — petite roue entraînée par une eau qui coule, distinguer transfert de mouvement et éventuelle conversion électrique *seulement si un générateur est explicitement présent*.
- **Rappel différé :** J+2 (annoncer une chaîne pour une sonnette différente), J+7 (corriger « le ventilateur fabrique du vent à partir de rien » sur un dessin solaire), J+21 (nouvel objet à manivelle). Les rappels nourrissent le suivi, pas une preuve de sortie automatique.
- Enrichissement : discuter de plusieurs sorties (lumière + chaleur) et des limites d'un schéma qui ne fournit ni mesure ni rendement.

## 10. Accessibilité et sécurité

- Narrations en français québécois clair, description textuelle des schémas, flèches nommées, pictogrammes avec libellés, agrandissement, lecture orale, temps modulable, appareils fictifs ou vidéos/schémas verbaux décrits. Éviter de coder les formes uniquement par couleurs.
- Accepter une chaîne énoncée oralement ou assemblée à partir de cartes non orientées (source / appareil / formes), photographiée ou transcrite, si les **mêmes relations** sont vérifiables. Le lecteur ne remplace pas le choix scientifique de l'élève.
- **Aucune construction ni manipulation de circuit électrique, pile ouverte, prise murale, outil coupant, élément chauffant, solaire concentré, mécanique rotative à proximité du corps, plan d'eau ou équipement en mouvement**; les tâches reposent sur des scènes écrites, photos libres appropriées si disponibles, ou observations réalisées par adulte sous protocole sûr. Ne pas inspecter une machine réelle en marche.
- Respecter vie privée : noms et situations fictifs; pas de données personnelles d'élèves. Rubriques non fondées sur aisance en lecture/graphisme. La sécurité fait partie du protocole, pas du jugement sur la maîtrise conceptuelle.

## 11. Critères de sortie

1. Sur **deux contextes différents**, dessiner ou dicter seul un schéma avec origine énergétique, récepteur/convertisseur, chemin dans le bon sens, entrée et sorties appropriées, effet observable et usage.
2. Nommer correctement au moins un transfert et une transformation lorsqu'ils existent, sans inventer une transformation pour une transmission simple; préciser ce qui est observé et ce qui relève du modèle.
3. Chaque preuve atteint le niveau « autonome et exact » de **chaque axe essentiel**, sans indice, amorce de chaîne ou confirmation pendant la prestation. Des mesures d'accès sont admises; la connaissance ne doit pas être soufflée.
4. Si l'un des deux contextes est incomplet, documenter l'axe à reprendre et exiger un autre contexte nouveau après remédiation, sans compter automatiquement une réussite d'entraînement.

## 12. Références pédagogiques et limites

- Gouvernance et documents originaux consultés (sans les modifier), graphe et catalogage : `../sources/REFERENCES_CONTENU.md`. Sources scientifiques vérifiées : U.S. Energy Information Administration et U.S. Department of Energy, citations et limites précisées au même endroit.
- Contenus, exemples, tests et scénarios originaux rédigés comme **propositions de travail**. Ne pas prétendre observer directement l'électricité d'un circuit opaque, ni prétendre que toute l'énergie est convertie en effet utile.
- L'appellation Science et technologie est conservée; **aucune conformité PFEQ, certification d'items, publication ou conversion canonique v9** n'est revendiquée. Relecture pédagogique et essai des rubriques nécessaires. L'archive contient deux remplacements autorisés et douze nouveaux fichiers.
