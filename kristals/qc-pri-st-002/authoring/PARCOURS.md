---
format: qc.learning-path/1.0
id: qc-pri-st-002
titre: Formuler des hypothèses et planifier une investigation
discipline_code: ST
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Formuler une prédiction motivée et concevoir un test simple et sûr.
objectifs_secondaires: []
criteres_reussite:
- Proposer un protocole avec paramètres observables et mesures prévues.
prealables_declares:
- qc-pri-st-001
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-st-002-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-st-002`

**Discipline (appellation québécoise) :** Science et technologie  
**Intitulé éditorial :** Formuler des hypothèses et planifier une investigation  
**Objectif :** `obj-1` — Formuler une prédiction motivée et concevoir un test simple et sûr.  
**Preuve de maîtrise :** `crit-1` — Proposer un protocole avec paramètres observables et mesures prévues.  
**Statut :** contenu rédigé; revue scientifique, pédagogique et accessibilité humaine requise avant qualification. Le frontmatter d'origine v1.2 est conservé sans aucune altération, y compris son statut de départ.

## 1. Intention et frontières

- **Cible observable :** une personne formule une réponse provisoire argumentée (« Si X varie, je prévois Y, parce que… »), distingue ce qu'elle modifie/mesure/maintient, propose un protocole réalisable, consigne à l'avance comment observer et mesurer, et anticipe la sécurité.
- **À apprendre :** hypothèse, variable, comparaison, sécurité; distinction **question → hypothèse → prédiction → plan → données futures → conclusion éventuelle**.
- **À ne pas supposer :** un protocole correct ne signifie pas que l'hypothèse est vraie; une variation observée ne prouve pas automatiquement une relation de cause à effet. Les résultats ne sont pas inventés; aucune expérience réelle ni résultat scientifique ne sont simulés comme faits.
- **Frontière :** investigation **planifiée**, non obligation d'exécuter un essai ou de rédiger une conclusion fondée sur de fausses données. Matériel scolaire usuel, basse énergie, sans substances dangereuses, sans chaleur, sans prise secteur, sans tests sur des personnes ou animaux.
- **Graphe :** seul préalable strict sortant `requires` : `qc-pri-st-001` (observer et formuler une question scientifique); aucun ordre conseillé sortant ni renforcement/transfert sortant. Le graphe contient un *lien entrant* non bloquant depuis `qc-pri-st-012` vers cet ID; il ne devient pas un préalable de ce Kristal.

## 2. Notions et représentations

| Notion | Définition opérationnelle | Exemple précis et critère |
|---|---|---|
| **Hypothèse** | Proposition provisoire, justifiée par une raison plausible, formulée de manière réfutable par des observations possibles. La **prédiction** annonce un résultat attendu si une condition change. | « Si l'on augmente la largeur d'une bande de papier, je prévois que sa flexion changera, car la forme modifie sa rigidité » : prédiction testable, sans certitude sur le résultat. |
| **Variable** | Caractéristique pouvant avoir différentes valeurs : **indépendante** (ce qu'on change), **dépendante** (ce qu'on mesure) et **contrôlée** (ce qu'on garde identique). | Une seule largeur varie; la flèche de flexion en millimètres est mesurée; papier, longueur libre, charge, supports restent identiques. |
| **Comparaison** | Confrontation de deux conditions sur une unité et une méthode de mesure communes, en changeant une variable ciblée. | Deux essais par condition, même instrument, tableau `condition / essai 1 / essai 2 / unité`. Deux mesures sont des répétitions, pas nécessairement une preuve statistique. |
| **Sécurité** | Choix préalable d'équipements, gestes, supervision et critères d'arrêt proportionnés au contexte. | Aucun objet lourd ou tranchant; installer des bandes de papier à plat; interrompre si chute, eau sur le sol ou inconfort. |

**Représentations :** texte court, tableau de variables, pictogrammes « je change / je mesure / je garde », schéma annoté, explication dictée à un scribe ou vocale. Une opinion (« ça marchera mieux ») n'est pas un indicateur mesurable. Une **observation** se rapporte à ce qui est vu/mesuré; un **modèle** est une représentation simplifiée (dessin); une **inférence** propose une explication; une **conclusion** dépend de données obtenues et n'appartient pas à la simple planification.

## 3. Préparation / diagnostic

- Préalable strict `qc-pri-st-001` : observer un phénomène et produire une question testable. **Équivalence diagnostique possible :** réussir les deux tâches suivantes atteste la capacité utile sans imposer la lecture de l'autre Kristal; consigner cette équivalence localement, sans éditer l'autre feuille.
- `diag-1` : partir de « une bande de papier se courbe quand on la pose entre deux supports »; identifier **observation** (« elle est courbée ») et **question** (« la largeur change-t-elle l'ampleur de la courbure ? »); refuser « le papier est triste » comme observation physique.
- `diag-2` : avec deux bandes **de papier identiques**, proposer quoi mesurer si l'on change seulement leur **largeur** (écart vertical au centre en mm, méthode fixe) et nommer une chose à conserver (longueur entre supports, type de papier, charge). On évalue le plan, pas un résultat attendu.
- **Décision :** acquis équivalent → commencer la conception; observation/question déficitaires → revoir observer et poser une question puis reprendre le diagnostic; mesure instable → préenseigner le tableau des variables. Ne pas bloquer arbitrairement une personne déjà compétente.

## 4. Enseignement guidé

- `teach-1` — **Modelage original :** « L'épaisseur d'une cale de carton sous un côté d'une feuille modifie-t-elle la pente mesurée ? » Choisir deux cales cartonnées prédécoupées de **5 mm et 10 mm** (fournies par un adulte); même feuille, même point de mesure, même table. Hypothèse provisoire : « Une cale plus haute pourrait augmenter la pente, car elle relève davantage le bord. »
- **Plan explicité :** X = hauteur de cale (mm); Y = écart vertical d'un point marqué de la feuille à la table (mm), mesuré à la règle; constantes = feuille, point, table, position de cale; conditions = 5/10 mm; deux répétitions prévues; tableau prêt **sans données inventées**.
- **Nuance de validité :** cette manipulation dépend aussi de la géométrie de l'installation; l'enseignant ne prétend pas connaître les valeurs finales. Le plan, pas la confirmation de la prédiction, est la réussite. Risque minime, pas de découpage par l'élève ni objet pointu.
- **Contre-modelage :** varier en même temps hauteur de cale et longueur de feuille interdit d'attribuer une différence à la hauteur seule. Corriger en stabilisant la longueur.
- **Vérification :** à quoi sert la colonne Y et pourquoi deux répétitions ? → mesurer pareil et vérifier la stabilité, non garantir la vérité.

## 5. Pratique accompagnée

- **`guided-1` — indices forts :** l'enseignant fournit le phénomène « deux bandes de papier, une étroite et une large » et la grille complète (question, prédiction, X, Y, constantes, outil, tableau, sécurité). L'élève remplit une ligne à la fois avec aide verbale; correction formative du mélange X/Y.
- **`guided-2` — indices moyens :** scénario « distance parcourue par une gomme qu'on laisse glisser d'une rampe basse »; cartes « inclinaison / distance parcourue / même gomme / même départ » à répartir en X, Y, constantes. Pas de valeur d'effet annoncée comme vraie. L'élève choisit l'unité centimètre, les répétitions et le risque de chute.
- **`guided-3` — indice faible :** scénario « temps nécessaire à une goutte d'eau pour traverser une marque sur une feuille de papier » : fournir **seulement** question et rappel « que changeras-tu et comment sauras-tu ? ». L'élève peut *refuser* un protocole peu mesurable et le remplacer par une observation plus accessible; l'autonomie et la prudence priment sur une fausse précision.
- Progression : tableau renseigné → cartes de catégories → consigne sans cases préremplies. Tous les exercices détaillés dans `contenu/04_PRATIQUE_ACCOMPAGNEE.md`.

## 6. Pratique autonome

- `independent-1` : quatre plans complets, nouveaux par rapport au modelage : distance d'une gomme selon inclinaison; flèche d'une bande selon sa largeur; longueur d'un trait selon une règle de mesure; comparaison de traces de crayon selon le papier. Consignes, éléments acceptables et limites dans `contenu/05_PRATIQUE_AUTONOME.md`.
- **Trame obligatoire :** question testable → hypothèse + raison → X avec **deux valeurs explicites** → Y avec mesure/unité/moment → au moins deux constantes → deux essais par condition ou justification du nombre → tableau vierge de résultats → sécurité et critère d'arrêt.
- **État d'autonomie :** aucun adulte ne choisit les variables ou la mesure; supports de communication/accessibilité non directifs autorisés. On n'exige pas d'exécuter l'expérience : la preuve est le protocole proposé.

## 7. Feedback et erreurs typiques

| Indice | Rétroaction ciblée | Reprise observable |
|---|---|---|
| « L'hypothèse est vraie parce que je l'ai écrite » | « C'est une proposition à vérifier, pas une observation. Quelles données pourraient la contredire ? » | Reformuler une prédiction conditionnelle réfutable. |
| Deux paramètres changés ensemble | « Quelle variable veux-tu comparer ? Que peux-tu maintenir identique ? » | Retirer un changement et nommer deux constantes. |
| « Le papier est meilleur » comme mesure | « Quelle grandeur précise, avec quelle unité et quel instrument ? » | Choisir longueur en mm, temps en s ou compte d'objets suivant le cas. |
| Un seul essai non comparé | « Comment comparerais-tu les mêmes conditions ? » | Prévoir deux valeurs de X et deux répétitions pour chaque condition. |
| Conclusions annoncées sans données | « Tu as une prédiction; laisse les cases de résultats vides avant l'expérience. » | Écrire tableau vierge et condition de décision après observation. |
| Matériel risqué ou inaccessible | « Nous changeons la méthode, pas la question : passons à un plan papier/simulation. » | Indiquer risque, prévention, arrêt et superviser si exécution. |

## 8. Évaluation formative et preuves

- Famille native `qc-pri-st-002-ev-01`, objectif `obj-1`, critère `crit-1`, type natif **`generee_sous_contraintes`**; banque réelle = corpus de **10 tâches approuvables** en modes `fixe` et `scenario_controle`. Aucune génération libre par IA, aucun tirage paramétrique non contrôlé. Sélection reproductible par IDs fixes et deux scénarios de maîtrise verrouillés.
- Les items `q-001` à `q-008` diagnostiquent question, hypothèse, variables, mesure, tableau, contrôle, risques et correction de plan. Le plan d'évaluation lie **chaque** item aux trois identifiants.
- **Maîtrise A `q-009` (« Comparateur de papiers »)** : planifier une comparaison de diffusion visible d'une goutte d'eau entre deux types de papier, avec deux conditions, mesure de diamètre maximal de tache (mm) **20 s** après dépôt, constantes et répétitions; aucune exécution obligatoire.
- **Maîtrise B `q-010` (« Atelier d'ombres »)** : planifier la comparaison de deux distances lampe LED/objet pour mesurer la **largeur d'une ombre (cm)** sur écran fixé, mêmes repères et contrôles. Autre phénomène, autre grandeur et nouveau plan; aucune lumière dans les yeux, aucune source secteur ni laser.
- Chaque épreuve exige un protocole autonome complet; grille M1–M6 appliquée à A **et** B sans compensation par moyenne globale. **Deux preuves** distinctes et justification de causalité prudente.

## 9. Remédiation / enrichissement

- Si hypothèse infalsifiable → écrire une condition et une mesure qui pourraient contredire la prévision.
- Si variable dépendante confondue → entourer la colonne des mesures, puis nommer ce qui varie volontairement.
- Si comparaison injuste → entourer les changements simultanés, fixer deux constantes et refaire sur un objet différent.
- Si mesure imprécise → fournir unités et point/moment de mesure; faire préparer le tableau **avant** les résultats.
- Si risque non identifié → remplacer le geste par modèle sur papier; mettre une condition d'arrêt vérifiable.
- **Enrichissement :** prévoir une anomalie, un échec d'instrument et un nouveau test plus robuste sans prétendre établir un résultat causal.
- **Rappel différé :** séance ultérieure avec phénomène inédit : redonner X, Y et deux constantes; quelques séances plus tard concevoir de mémoire un mini-plan et vérifier via grille sans indice.

## 10. Accessibilité

- Formats d'entrée : lecture facilitée, texte agrandi, audio, pictogrammes et tableaux; formats de sortie : texte, dictée à scribe neutre, schéma, dispositif de communication assistée. Évaluer **la pensée expérimentale**, pas la vitesse d'écriture ni la dextérité.
- Alternatives sans manipulation, simulation sur papier et tableau de données **vierge** sont recevables car la cible est la conception. Une donnée fictive fournie pour un exercice doit être identifiée comme telle et ne prouve pas un résultat scientifique.
- Privilégier petits objets non pointus, lampe LED à piles à faible intensité si démonstration approuvée, eau en très faible quantité sur plateau non glissant et lingette de nettoyage. Stop si eau renversée, lampe qui chauffe ou gêne visuelle; jamais de circuit secteur, laser, substances corrosives, cuisson, feu, hauteurs, épreuve sur personnes/animaux.
- Temps flexible, lecture répétée, aucune pénalisation de l'orthographe sans perte de sens. Aides à l'accès convenues à l'avance, **sans fournir X, Y ni hypothèse** durant l'épreuve finale.

## 11. Critères de sortie

1. `obj-1` : une prédiction conditionnelle, motivée, réfutable et distincte d'une observation est exprimée.
2. `crit-1` : protocole ordonné comportant deux valeurs d'une variable changée, mesure Y définie **avec unité et moment**, au moins deux constantes, répétitions et tableau vierge.
3. Sécurité anticipée : matériel autorisé, précaution concrète et règle d'arrêt appropriées; aucune conclusion inventée.
4. Ces conditions sont observables **de manière autonome dans deux contextes distincts**, `q-009` et `q-010`; les critères essentiels M1–M6 atteignent le niveau 2 **dans les deux**. Si une composante manque, remédiation ciblée et nouvelle preuve, pas de promotion sur score total.

## 12. Références pédagogiques et limites

- **Sources internes lues :** `CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md`, graphe 202, `PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md` et `BRIEF_REDACTION.md` du présent Kristal.
- **Source externe consultée :** Science Buddies, « What Are Variables? » (définitions variable indépendante, dépendante, contrôlée), https://www.sciencebuddies.org/science-fair-projects/science-fair/variables-beginner. National Academies (2012), *A Framework for K-12 Science Education*, chapitre des pratiques d'investigation, https://www.nationalacademies.org/read/13165/chapter/7 . Les textes/illustrations de ces sources ne sont pas reproduits.
- **Créations éditoriales originales :** scénarios, tableaux, consignes, barèmes et seuils; ils n'ont pas été testés auprès d'élèves, ni validés scientifiquement en situation. Détail des droits dans `sources/REFERENCES_CONTENU.md`.
- **Limite institutionnelle :** aucun alignement détaillé au PFEQ, aucune certification ou homologation; qualification exige revue humaine et validation technique distincte.
