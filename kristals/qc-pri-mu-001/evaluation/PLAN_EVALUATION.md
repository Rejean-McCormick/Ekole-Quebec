# Plan d'évaluation — `qc-pri-mu-001-ev-01`

- **Kristal :** `qc-pri-mu-001` · **Discipline :** Musique · **Objectif unique :** `obj-1` — Discriminer sons et silences selon des propriétés audibles.
- **Critère unique :** `crit-1` — Classer des extraits sonores selon deux critères expliqués.
- **Famille :** `qc-pri-mu-001-ev-01` · **Type contractuel :** `observation_ou_production` · **Banque :** `qc.learning-item-bank/1.0` · **Statut :** items rédigés `a_revoir`, aucun examen certifié.
- **Nature :** écoute, classification, justification et création brève observée. Aucune épreuve de goût, de justesse vocale, de morphologie, d'acuité diagnostique ou d'intérêt musical.

## Planification et couverture de la banque (12 items fixes)

| ID | Objectif | Critère | Famille | Niveau | Représentation | Point vérifié / fonction |
|---|---|---|---|---|---|---|
| q-001 (suffixe) | obj-1 | crit-1 | qc-pri-mu-001-ev-01 | initial | écoute D1/D2 + ligne du temps | durée; diagnostic |
| q-002 | obj-1 | crit-1 | idem | initial | écoute D3/D4 + séquence son/silence | silence interne; diagnostic |
| q-003 | obj-1 | crit-1 | idem | initial | écoute E1/E3 + cartes | intensité (durée tenue stable); formation |
| q-004 | obj-1 | crit-1 | idem | initial | écoute Q1/Q2 + contraste | hauteur; formation |
| q-005 | obj-1 | crit-1 | idem | intermédiaire | écoute U1/U2 + description | timbre sans goût; formation |
| q-006 | obj-1 | crit-1 | idem | intermédiaire | écoute S1/S2 + chronologie | distinction signal et silence; formation |
| q-007 | obj-1 | crit-1 | idem | intermédiaire | matrice 2 × 2 P1–P4 | deux axes durée/intensité; pratique |
| q-008 | obj-1 | crit-1 | idem | transfert | production, ligne du temps et grille | intention, organisation, écoute, silence; transfert |
| **q-009** | **obj-1** | **crit-1** | **idem** | **transfert** | **matrice A1–A4, atelier musical** | **preuve de maîtrise A : durée × intensité** |
| **q-010** | **obj-1** | **crit-1** | **idem** | **transfert** | **matrice B1–B4, jeu de signaux fictifs** | **preuve de maîtrise B : hauteur × pause** |
| q-011 | obj-1 | crit-1 | idem | transfert | matrice X1–X4 | nouvelle situation; transfert |
| q-012 | obj-1 | crit-1 | idem | intermédiaire | matrice R1–R4 | rappel espacé des deux axes |

`q-001` signifie l'ID complet `qc-pri-mu-001-q-001` (et ainsi de suite). **Tous les items** ont explicitement `family_id`, `objectif_id=obj-1`, `critere_id=crit-1` dans la banque; « idem » ci-dessus n'est qu'une abréviation typographique.

## Matériel et procédure commune

1. Générer **localement** les 38 fichiers `.wav` à partir du script Python inclus dans `contenu/01_NOTIONS_ET_EXEMPLES.md`. Aucun WAV n'est fourni dans ce delta. Le correcteur doit **auditionner chaque série** et s'assurer que durée, silence, grave/aigu, douceur et timbre sont suffisamment distincts sans bruit, distorsion ni normalisation dynamique inattendue. Les valeurs d'amplitude numérique ne sont pas des décibels au niveau de l'oreille.
2. Pour chaque item, annoncer la consigne **sans lire les paramètres ni le corrigé**; jouer les identifiants dans l'ordre énoncé dans le fichier de banque; conserver le même réglage de lecture pour les comparaisons; laisser environ deux secondes entre fichiers. Autoriser, selon besoin, deux réécoutes **neutres** de la série entière ou de chaque paire, enregistrer leur nombre et les éventuelles adaptations.
3. Fournir une matrice à quatre cases ou l'équivalent tactile; réponse orale, pointage, cartes ou dictée de la décision à une personne neutre sont recevables. Les indices, telles les définitions des axes, figurent dans les consignes standard et ne révèlent pas les étiquettes de chaque son.
4. Journaliser hors du contenu/canon : identifiant item, date, contexte, ordre lu, identité des WAV utilisés (aucune donnée personnelle requise), contrôle audio, réponses, justifications, aide, réécoutes, adaptation, résultat critérié.
5. Si l'audio n'est pas disponible, non contrôlé, dangereux ou inaccessible, enregistrer `non_administre` / `preuve_non_interpretable` et **ne pas affecter un score**; aucune réponse fondée uniquement sur la description papier du stimulus ne prouve la discrimination *auditive*.

## Deux preuves formelles obligatoires et décision

- **A — `q-009` : atelier musical de répétition**. Quatre notes sinusoïdales A1–A4 de hauteur constante (523,25 Hz); croiser **court/long** et **doux/plus marqué**. Grille 2 × 2 complète + deux raisons indépendantes fondées sur la durée et le niveau perçu. Exigence : **au moins 3/4 des extraits correctement classés simultanément sur les deux critères**, puis **2/2 justifications** valides (une par axe); observation sans indice de placement.
- **B — `q-010` : jeu fictif de signaux dans un jardin**. Quatre motifs triangulaires B1–B4 à 330/660 Hz, avec ou sans pause *interne* 0,60 s; croiser **grave/aigu** et **pause / pas de pause**. Même seuil et deux raisons valides, une par axe; nouvelle règle, timbre, organisation et situation. Aucun signal réel d'urgence n'est imité.
- **Maîtrise :** A **ET** B atteignent chacun leur seuil, et l'observateur juge l'autonomie de l'élève dans les deux contextes. **Ne pas calculer** une moyenne compensatoire, ni accorder la maîtrise après une seule série. Ne pas noter la force physique, la précision du chant ou le goût.
- **Échec/partiel :** pointer critère fragilisé, courte remédiation, autre série de stimuli contrôlés et nouveau recueil autonome. Ne pas réévaluer simplement la même feuille après révélation des réponses. Le rappel différé q-012 complète le suivi mais ne remplace aucune des deux preuves.

## Variabilité, corrigés et seuils de contrôle

- **Mode déclaré pour les 12 items : `fixe`** (`seed: null`, `parametres: null`). L'identité, l'ordre, les fréquences, les durées, les amplitudes relatives, le timbre des signaux et les réponses sont verrouillés par le catalogue. Il n'y a **aucun mode paramétrique**; pas de graine ou calculateur de correction dissimulé.
- Variabilité permise **sans changer l'épreuve** : réécoute neutre, taille de la matrice, supports de réponse (verbal, tactile, pictogramme), aide à l'accès aux consignes, adaptation d'espacement entre fichiers; transcrire la réponse sans influencer le placement. L'égalisation/normalisation sonore ou la substitution de fichier ne sont **pas** des variantes admissibles sans nouveau contrôle humain et nouvelle version des recettes/rubriques.
- Corrigés : combinaisons déduites des recettes déterministes et vérifiables par code; **validité perceptive non certifiée** avant audition de chaque série. Pour l'item de production (`q-008`), la bonne réponse est **une trace observée** suivant la rubrique; jamais une phrase inventée qui prétend décrire ce qu'a fait l'élève.
- Utiliser exclusivement les sons synthétiques originaux locaux (ou une substitution autorisée après examen des droits et une nouvelle validation); pas d'enregistrements de musique commerciale, de données personnelles ou de fichiers téléchargés sans autorisation.

## Sécurité, équité et accessibilité

Démarrer volume bas puis ajuster à un **niveau conversationnel confortable**, sans écouteurs imposés ni impulsions brusques; proposer des pauses et l'arrêt en cas d'inconfort auditif, douleur ou bourdonnement. La différence numérique des gains (`0,08/0,24`) n'est pas un objectif de pression acoustique : toute écoute reste subordonnée au contrôle réel. Éviter environnements bruyants; ne pas transformer l'acuité sensorielle, l'hyperacousie ou un handicap en « erreur musicale ». Les aides visuelles/tactiles peuvent soutenir l'apprentissage, mais elles **ne démontrent pas à elles seules** une discrimination auditive : recueillir la preuve équivalente sans masquer la modalité et demander l'avis d'une personne compétente si nécessaire. Ne pas revendiquer de conformité PFEQ.

**Revue humaine obligatoire :** acoustique des fichiers et de l'appareil, formulations d'âge et d'accessibilité, structure des grilles, biais de contexte, droits de toute substitution, passation avec élèves, intégration framework/LMS. Statut `a_revoir` maintenu dans tous les items.
