---
format: qc.learning-path/1.0
id: qc-pri-ale-001
titre: Conscience phonologique en anglais
discipline_code: ALE
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Segmenter et manipuler syllabes et phonèmes de mots anglais oraux.
objectifs_secondaires: []
criteres_reussite:
- Recomposer oralement des mots nouveaux après segmentation.
prealables_declares: []
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ale-001-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ale-001`

**Discipline (appellation québécoise) :** Anglais, langue d’enseignement. **Titre :** Conscience phonologique en anglais.  
**Gouvernance :** `governance/Norme_Pedagogique_Autonome_v1.2/`. **État :** cours et banque rédigés; revue humaine et essai en situation requis.

## 1. Intention et frontières
- `obj-1` : **Segmenter et manipuler syllabes et phonèmes de mots anglais oraux.** (formulation canonique inchangée)
- `crit-1` : **Recomposer oralement des mots nouveaux après segmentation.** (preuve canonique inchangée)
- À la fin, l'enfant sépare des mots entendus en syllabes ou phonèmes, identifie onset et rime dans un mot monosyllabique, puis réassemble à voix haute de nouvelles séquences. Une explication orale de la stratégie montre le processus.
- Pas de lecture, d'orthographe, de reconnaissance de lettres ni de notation de la qualité d'un accent natif. Les chaînes IPA et l'orthographe sont des **corrigés réservés à l'adulte**, jamais des indices affichés à l'élève lors des tâches orales.
- Évaluer la perception et la combinaison des sons, non la vitesse ou la mémorisation d'une liste. Les cibles sont des mots anglais authentiques et non des pseudo-mots.

## 2. Notions et représentations
- **syllable :** unité rythmique orale organisée autour d'un noyau vocalique; `rocket` /ˈrɑ.kɪt/ (illustration de réalisation nord-américaine) comporte deux syllabes, non six sons simplement parce qu'il y a six lettres.
- **phoneme :** unité distinctive de sons de la parole; `fish` /f ɪ ʃ/ comporte trois phonèmes, bien que quatre lettres soient imprimées.
- **onset :** consonne(s) avant la voyelle d'une syllabe : dans `cap`, /k/; certains mots comme `in` n'ont pas d'onset.
- **rime :** noyau vocalique et consonnes qui le suivent, à l'intérieur de la syllabe; dans `cap`, /æp/. À distinguer de la « rhyme » (relation entre mots dont les rimes sonores concordent).
- Représentations successives : écouter → redire en parties → frapper une fois par syllabe ou déplacer un jeton par phonème → joindre les parties → prononcer le mot entier. Les jetons n'ont **aucune lettre**.
- Choisir des mots suffisamment connus oralement; présenter le vocabulaire par image avant le test, mais sans dire le mot entier au moment de l'évaluation de synthèse.

## 3. Préparation / diagnostic
- `requires = []`, aucun prérequis strict; `recommends_before = []`, aucun ordre conseillé; `reinforces = []`. Aucun autre Kristal n'est imposé.
- `diag-1` (« umbrella » oral) : dire *rainbow* [prononcé naturellement par l'adulte], demander : « How many beats? Say the parts. » Attendu : 2, `rain | bow` (on accepte la réalisation syllabique de la variété de l'élève). L'adulte ne présente pas le mot écrit.
- `diag-2` : dire distinctement /m/ – /ɪ/ – /t/ sans dévoiler le mot; « What word? Say the sounds, then blend. » Attendu *mitt*. En cas d'incompréhension, répéter les unités, sans fournir la réponse.
- Décision : si les deux sont réussis sans indices, proposer immédiatement les tâches autonomes et la vérification sur deux contextes; sinon enseigner le niveau déficitaire, sans bloquer sur un parcours externe.

## 4. Enseignement guidé
- `teach-1` : « Listen to my voice, not to letters. » Modeler *picnic* comme deux battements `pic | nic`, puis réunir. Expliquer qu'un battement n'est pas une lettre.
- Modeler *fish* : /f/ /ɪ/ /ʃ/ → *fish*. Faire trois déplacements de jetons, puis les rapprocher. « I heard three sounds. The last one is /ʃ/, not separate /s/ and /h/. »
- Modeler l'onset-rime de *cap* : /k/ + /æp/ → *cap*; /k/ est l'onset et /æp/ la rime. Démontrer le cas limite `in` (pas d'onset consonantique).
- Contrôle : faire écouter /s/ – /ɪ/ – /t/ → *sit*, et demander « Which part did you put first? »; noter l'efficacité de la fusion, sans exiger la terminologie IPA.

## 5. Pratique accompagnée
- `guided-1` : *rainbow*, modèle à deux battements rappelé au besoin, puis *basket* : `bas | ket`, sans montrer le mot. Indice complet d'abord (gestes + pause), puis gestes seulement.
- `guided-2` : /m/ + /æn/ → *man*; découper l'onset et la rime avec deux jetons; second essai /f/ + /æn/ → *fan* avec seul temps de pause.
- `guided-3` : /l/ /ɛ/ /ɡ/ → *leg*, puis /k/ /ʌ/ /p/ → *cup*, sans indice; feedback descriptif avant un nouvel essai. Les indices sont explicitement décroissants d'une tâche à la suivante.
- Pour chaque essai : écouter, reprendre les segments, fusionner, vérifier à l'écoute; ne pas demander à l'élève de lire le corrigé.

## 6. Pratique autonome
- `independent-1` : 4 tâches nouvelles à faire à l'oral, décrites dans `contenu/05_PRATIQUE_AUTONOME.md` : synthèse de phonèmes, synthèse onset-rime, segmentation de syllabes puis synthèse, et substitution du premier son. Aucun indice de réponse avant la production.
- Consigner, pour chaque tâche, les segments présentés, la production audible et les autocorrections; une aide lexicale donnée au milieu de la tâche rend cette tâche accompagnée, pas autonome.
- Une performance déjà suffisante au diagnostic autorise un accès direct à `evaluation/BANQUE_ITEMS.json`; deux contextes restent obligatoires.

## 7. Feedback et erreurs typiques
- `error-1` : « three letters = three sounds » : *fish* produit quatre frappes → redonner les trois sons parlés /f ɪ ʃ/ avec trois jetons, sans montrer `sh`.
- Segmentation trop fine de *picnic* en phonèmes pendant une consigne de syllabes : réécouter le mot entier et frapper deux fois.
- Confusion onset/rime : `cap` devient /kæ/ + /p/ → demander où commence la voyelle, puis proposer /k/ + /æp/.
- Fusion avec voyelle ajoutée (`/m/` devient « muh ») : prolonger les consonnes qui s'y prêtent, joindre immédiatement aux voyelles; accepter la variation articulatoire naturelle lors de la fusion.
- Après chaque correction, vérifier avec **un autre** stimulus non identique.

## 8. Évaluation formative et preuves
- Famille `qc-pri-ale-001-ev-01`, `objectif_ref = obj-1`, `critere_ref = crit-1` ; mode de famille natif **`réponse_argumentée`** conservé : réponse **orale** + justification ou démonstration du découpage/fusion.
- Banque de 12 items contrôlés : dix fixes, deux scénarios contrôlés avec variantes A/B. Toutes les consignes destinées à l'élève sont en anglais oral; l'adulte lit le script distinctement et garde le corrigé caché.
- Deux preuves autonomes dans des contextes distincts : objets de classe et préparation d'un pique-nique. Chacune exige reconstitution de phonèmes, onset/rime et syllabes à partir de mots non employés au modelage ni à la pratique.
- Maîtrise : deux contextes réussis séparément, sans indice décisif, avec recomposition correcte d'au moins deux cibles sur trois **et** exactitude de la cible phonémique et d'une deuxième forme (onset-rime ou syllabes) dans **chaque** contexte; autocorrection permise; compréhension et justification orale observables. Aucune note unique suffisante.

## 9. Remédiation / enrichissement
- Si échec syllabes : deux jetons pour `sunset` [exemple après évaluation, non utilisé comme preuve] et réécoute lente, puis mot inédit à deux syllabes.
- Si échec phonèmes : reconstruire une chaîne CV-C simple /s ɪ p/ (sip), trois jetons, puis /n ɛ t/ (*net*).
- Si échec onset-rime : contraste /m/ + /æt/ (*mat*) contre /s/ + /æt/ (*sat*), puis nouvel exemple; ne pas confondre syllabes et segments de mots écrits.
- Enrichissement : inverser un phonème de *cat* /k æt/ en *hat* /h æt/; comparer *cat* et *cap* à l'oral. Ces mots d'enrichissement ne sont pas des preuves de maîtrise.
- Reprise formative 48 h puis 7–10 jours plus tard avec cibles orales non identiques; deux preuves finales demeurent nécessaires.

## 10. Accessibilité
- Pas de lecture ni d'écriture exigée; si utile, supports tactiles anonymes (trois jetons) et gestes silencieux n'exposant pas la réponse. Lecture labiale visible, son clair, volume confortable, répétition de la consigne **sans segmenter davantage**.
- Pour difficultés motrices : pointer des jetons au lieu de frapper; pour difficultés de parole : réponse par sélection séquentielle d'unités audibles + sortie vocale contrôlée, avec observation authentique de la fusion; consigner l'adaptation et demander une appréciation humaine de l'équivalence avec la preuve **orale** canonique.
- Ne pas confondre accent dialectal, allophonie, trouble de l'articulation ou audition avec manque de conscience phonologique; demander l'appui d'un spécialiste au besoin, sans diagnostic improvisé. Aucune capture vocale nominative nécessaire dans le ZIP.

## 11. Critères de sortie
1. Deux performances distinctes de `crit-1`, une au moins sans aucune relance, dans deux situations inédites, avec les seuils de `evaluation/GRILLE_MAITRISE.md`.
2. Segmentation audible ou gestuelle cohérente au niveau demandé (syllable, onset-rime, phoneme), suivie d'une fusion produisant le mot cible.
3. Réponse explicative courte : « I put /p/ /ɛ/ /n/ together » ou démonstration équivalente (pas de justification orthographique).
4. Décision : maîtrise attestée **seulement** après deux manifestations; sinon réenseigner l'opération insuffisante et recueillir de nouvelles preuves.

## 12. Références pédagogiques et limites
- Définitions conceptuelles vérifiées : Reading Rockets « Basics: Phonological and Phonemic Awareness » et « In Depth »; IES/WWC (2016, révisé 2019); CAST UDL 3.0. Détails et URLs : `sources/REFERENCES_CONTENU.md`.
- Exemples, activités et scripts sont des **productions originales**, conçues à partir des notions vérifiées. Les notations IPA sont des **prononciations de référence illustratives** nord-américaines; l'enseignant doit vérifier la réalisation orale locale de chaque stimulus.
- Aucune prétention d'homologation au PFEQ; statut **à revoir humainement**, notamment essais d'écoute et accessibilité de la réponse orale.
- Rappel différé proposé à J+2 et J+8 : /v/ /ɛ/ /t/ (*vet*), puis /m/ + /ʌɡ/ (*mug*); nouveaux mots distincts des deux preuves et du modelage. Noter résultats et besoin d'aide.
