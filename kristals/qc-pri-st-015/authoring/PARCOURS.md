---
format: qc.learning-path/1.0
id: qc-pri-st-015
titre: Atmosphère et phénomènes météorologiques
discipline_code: ST
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Décrire des phénomènes météorologiques à partir de mesures et observations.
objectifs_secondaires: []
criteres_reussite:
- Interpréter une courte série de relevés météorologiques.
prealables_declares: []
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-st-015-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---


# Microparcours — `qc-pri-st-015`

**Discipline (appellation québécoise) :** Science et technologie.  
**Titre :** Atmosphère et phénomènes météorologiques.  
**Gouvernance :** `governance/Norme_Pedagogique_Autonome_v1.2/`.  
**État :** matériel rédigé, **à réviser par une personne compétente avant qualification**; le front matter v1.2 et son statut restent inchangés. Le présent contenu n'est pas une prescription PFEQ.

## 1. Intention et frontières

- `obj-1` — **Objectif observable IMMUTABLE :** Décrire des phénomènes météorologiques à partir de mesures et observations.
- `crit-1` — **Preuve autonome IMMUTABLE :** Interpréter une courte série de relevés météorologiques.
- Quatre notions centrales : **température** (de l'air, °C), **vent** (vitesse en km/h et direction facultative), **pluie** (hauteur recueillie, mm, pour une durée indiquée), **nuages** (présence ou fraction approximative du ciel couverte).
- L'atmosphère est l'enveloppe gazeuse de la Terre. Les relevés décrivent la **météo à un lieu, un instant ou pendant une période** : ils ne suffisent ni à établir le climat d'une région ni à expliquer avec certitude la cause d'une variation.
- Distinguer **observation** (ciel couvert), **mesure** (12 °C, 5 mm sur une période), **inférence prudente** (« les données montrent une augmentation »), **modèle** (schéma simplifié) et **prévision** (énoncé sur l'avenir, non démontré par ces données).
- Aucun risque d'exposition aux intempéries ne doit être nécessaire; les séries chiffrées de cette livraison sont **fictives et construites pour l'enseignement**.

## 2. Notions et représentations

- **Température de l'air** : grandeur indiquant l'état thermique, exprimée ici en °C et lue sur un thermomètre adéquatement placé; on compare des valeurs, pas une sensation personnelle (« j'ai chaud »).
- **Vent** : mouvement de l'air. La vitesse (km/h) se mesure avec un anémomètre; si une direction est mentionnée, le vent « du nord » **vient du nord**. Le mouvement d'un drapeau peut suggérer un vent, sans chiffrer sa vitesse.
- **Pluie** : précipitation d'eau liquide tombant des nuages. La quantité cumulée au sol se mesure avec un pluviomètre en **mm sur une période définie**. `0 mm` signifie aucune pluie mesurée pendant cet intervalle, pas absence absolue d'humidité; `—` signifie donnée absente, pas zéro.
- **Nuages** : ensembles visibles de très petites gouttelettes et/ou de cristaux de glace suspendus dans l'atmosphère. On peut décrire un ciel dégagé, partiellement nuageux, couvert ou donner une estimation simple de la couverture (`0/10` à `10/10`). Nuages ≠ pluie garantie.
- Trois représentations : carnet d'observation, tableau légendé avec unités/périodes et mini-frise chronologique en texte. L'absence de pictogrammes n'empêche jamais l'accès à l'information.
- Références factuelles : `sources/REFERENCES_CONTENU.md`; exemples `contenu/01_NOTIONS_ET_EXEMPLES.md`.

## 3. Préparation / diagnostic

- **Préalables bloquants :** `requires = []`, aucun verrou inter-Kristals; le diagnostic peut attester une compétence équivalente, sans imposer la consultation d'autres feuilles.
- **Ordre conseillé non bloquant :** `qc-pri-st-014`; **renforcement/transfert non bloquant :** `qc-pri-ma-031`, sans importation ni modification de contenus voisins.
- `diag-1` : devant « 11 °C, ciel couvert », différencier **valeur mesurée** et **observation visuelle**; distinguer « il pleuvra » (prévision).
- `diag-2` : sur trois relevés `8 °C → 12 °C → 10 °C`, repérer maximum et variation entre deux heures, citer les nombres et préciser ce que les données ne permettent pas d'affirmer.
- Diagnostic : deux petites tâches individuelles, réponse orale, écrite ou pointée; rétroaction sans note éliminatoire. Acquis déjà solide → nouvelles données autonomes; hésitation → micro-remédiation sur mesure/observation et lecture de tableaux. Corrigés dans `contenu/02_DIAGNOSTIC.md`.

## 4. Enseignement guidé

- `teach-1` : afficher **objectif**, légende et tableau fictif : `9 h : 8 °C, vent 6 km/h, pluie 0 mm (8–9 h), ciel couvert 2/10; 12 h : 12 °C, vent 11 km/h, pluie 2 mm (11–12 h), ciel couvert 8/10`.
- Modeler à voix haute : **(1)** lire lieu/heures/unités et intervalles, **(2)** pointer deux valeurs, **(3)** calculer uniquement si approprié (`12 - 8 = +4 °C`), **(4)** formuler « entre 9 h et 12 h la température a augmenté de 4 °C », **(5)** distinguer « il a plu 2 mm entre 11 h et 12 h » de « il pleuvra demain », non justifié.
- Vérifier : « Quelle est la preuve de +4 °C ? » / « Peut-on dire que les nuages **ont causé** la pluie ? » (non, pas avec ces seules lignes).
- Introduire un contre-exemple (`8/10` nuages, `0 mm`) montrant qu'un ciel très nuageux n'implique pas nécessairement une pluie mesurée. Leçons prêtes à l'emploi dans `contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

- `guided-1` : tableau de trois heures, identification d'une mesure et d'une observation avec indices explicites (g-1).
- `guided-2` : comparer vitesse du vent et pluie dans un relevé différent; seul un rappel d'unité reste visible (g-2).
- `guided-3` : interpréter seul une petite série de ciel nuageux et de précipitations; indice uniquement si l'élève le demande, puis on retire toute aide (g-3).
- Indices **dégressifs** : questions pas à pas → simple légende → aucune aide. Chaque tâche comporte un corrigé et une nouvelle question de vérification; voir `contenu/04_PRATIQUE_ACCOMPAGNEE.md` [corrigé : `04_PRATIQUE_ACCOMPAGNEE.md`].

## 6. Pratique autonome

- `independent-1` : quatre petites séries inédites, sans hints, couvrant hausse/baisse, nuages sans pluie, cumul de pluies à périodes distinctes et incertitude liée à une donnée manquante.
- Traces : deux nombres corrects avec unités, un constat appuyé sur des valeurs et un refus justifié d'une affirmation non étayée; formats réponse écrite, dictée, oral transcrit ou tableau tactile.
- Corrigés intégralement documentés dans `contenu/05_PRATIQUE_AUTONOME.md`; données créées pour cette feuille, **pas d'observations réelles**.

## 7. Feedback et erreurs typiques

- `error-1` : confusion constat / inférence / prévision. Demander « quelle ligne du tableau le prouve ? » et faire surligner la valeur justificative.
- `error-2` : confondre °C, km/h et mm; associer l'instrument et l'unité à chaque colonne avant un nouvel essai.
- `error-3` : déduire la pluie de la seule présence de nuages; fournir deux lignes aux couvertures nuageuses semblables mais pluies différentes.
- `error-4` : additionner deux cumuls qui se chevauchent ou traiter `—` comme `0`; travailler uniquement avec intervalles **disjoints** et reclasser les données manquantes.
- `error-5` : parler de « climat » avec trois journées; rappeler que l'échantillon décrit uniquement **cette courte période**. Remédiations pas à pas dans `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 8. Évaluation formative et preuves

- Identité fixe : `family_id: qc-pri-st-015-ev-01`; `objectif_ref: obj-1`; `critere_ref: crit-1`; mode natif : `generee_sous_contraintes` (banque mixte d'items fixes et de paramètres déterministes explicites).
- `evaluation/BANQUE_ITEMS.json` : **12 tâches** (9 fixes, 3 paramétriques déterministes); stimuli et corrigés affichés pour chaque graine fixée, niveaux et critères liés au plan.
- Deux **manifestations de maîtrise** séparées : `q-011` (relevés horaires de la cour d'école) et `q-012` (relevés quotidiens du jardin communautaire). Elles requièrent une interprétation sans indices, justifiée et prudente; les séries sont différentes.
- La grille `evaluation/GRILLE_MAITRISE.md` examine la lecture des données, exactitude/units, justification, distinction constat/prévision et autonomie. **Aucune note isolée ne certifie la maîtrise.**
- Les items ne sont ni certifiés ni publiés; contrôle technique ≠ validation humaine des tâches.

## 9. Remédiation / enrichissement

- Difficulté pour identifier l'unité → cartes « °C / km/h / mm / dixièmes de ciel », puis lecture d'un relevé réduit.
- Difficulté à comparer → deux valeurs puis trois, calcul verbal/écrit de différence; zéro et valeurs négatives admis en °C.
- Difficulté à raisonner → tableau de preuves à deux colonnes « ce qui est écrit » / « ce que j'en conclus »; refuser les explications causales non démontrées.
- Maîtrise démontrée → transfert comparatif vers nouveau lieu, graphique à axes accessibles, réflexion sur conditions de mesure. Lien non bloquant `qc-pri-ma-031` pour organiser les données, sans importer les contenus de l'autre feuille.

## 10. Accessibilité

- Tableaux lisibles sans couleurs; unités explicites et heures écrites; jamais des icônes seules ou des flèches ambiguës; chiffres annoncés à l'oral, possibilité de gros caractères/braille/lecteur d'écran.
- Autoriser réponse dictée, audio, pointage structuré, clavier ou script d'assistance; évaluer **l'interprétation scientifique**, non l'orthographe ni la motricité.
- Ne jamais exiger photos d'élèves, localisation personnelle, accès Internet, déplacement, enregistrement météo extérieur ni exposition à la pluie/foudre/vent fort. Toutes les observations peuvent être fictives; si observation réelle facultative, elle est faite depuis un endroit sûr, sous supervision.
- Ne pas modifier les valeurs ni les exigences cognitives sans documenter une adaptation équivalente.

## 11. Critères de sortie

1. Dans chaque contexte, identifier correctement au moins **trois éléments** mesurés/observés, avec unité ou légende pertinente.
2. Comparer exactement au moins **deux** valeurs temporelles et rapporter le bon sens de variation ou un cumul d'intervalles distincts, avec unité.
3. Produire une conclusion **appuyée sur deux données explicites** et nommer une affirmation non déductible (prévision/causalité excessive).
4. Manifester ces critères **dans les deux contextes** (`q-011` et `q-012`) sans indice de contenu, avec au plus une répétition neutre de la consigne; en cas d'écart, remédier puis réévaluer dans une nouvelle série contrôlée.
5. Rappel différé : reprendre après ~7 jours un tableau inédit et expliquer une limite d'inférence; ce rappel informe la stabilité, ne remplace pas les deux preuves initiales.

## 12. Références pédagogiques et limites

- Les définitions scientifiques reposent sur les glossaires d'Environnement et Changement climatique Canada et l'Atlas international des nuages de l'OMM; sources vérifiées et limites dans `sources/REFERENCES_CONTENU.md`.
- Les tableaux, questions et corrigés sont des **productions originales fictives**; ne pas les présenter comme mesures d'un organisme ou d'un élève.
- Les recommandations pédagogiques générales figurent dans la gouvernance; efficacité propre au dispositif non testée. Pas d'alignement détaillé ni d'homologation PFEQ.
- Vérifications machine et limites consignées dans `livraison/VALIDATION.md`; revue scientifique de détail, revue pédagogique et tests avec élèves restent nécessaires.
