# Plan d'évaluation v1.2 — `qc-pri-ilss-004`

**Objectif immuable :** `obj-1`, Comprendre des messages et documents fonctionnels du quotidien. **Preuve/critère immuable :** `crit-1`, Extraire l’information utile d’un document scolaire adapté. **Famille :** `qc-pri-ilss-004-ev-01`. **Type privilégié :** `observation_ou_production`, mesure par lecture de documents et réponse/pointage, sans QCM forcé.

## Cible, méthode et représentation

Une information **utile** est celle qui répond à une question fonctionnelle explicitement posée : jour, heure, local, matériel, date limite, action. Le correcteur exige sa correspondance à un segment du **document fictif fourni**, pas à une supposition scolaire ou culturelle. La réponse est recevable sous forme orale, pointée, textuelle ou en communication assistée. Une erreur d'accent ou d'orthographe ne compte pas si le champ ou le choix est sans ambiguïté. Une lecture à voix haute fidèle et un glossaire de consigne non directif peuvent être prévus; ils ne doivent pas localiser la réponse.

| Item complet | Niveau | Représentation | Critères ciblés | Usage |
|---|---|---|---|---|
| `qc-pri-ilss-004-q-001` | initial | horaire à une ligne | jour/heure/local explicitement extraits; champs pointés | formatif |
| `qc-pri-ilss-004-q-002` | initial | message bref | matériel précis et moment; segments | formatif |
| `qc-pri-ilss-004-q-003` | initial | symbole textuel légendé | activité établie par légende, heure non indiquée | formatif |
| `qc-pri-ilss-004-q-004` | intermédiaire | formulaire à cases | choix, date limite, donnée manquante | formatif |
| `qc-pri-ilss-004-q-005` | intermédiaire | message et coupon | distinguer moment de l'activité et échéance | formatif |
| `qc-pri-ilss-004-q-006` | intermédiaire | horaire + message | combiner supports sans mélanger leurs sources | formatif |
| `qc-pri-ilss-004-q-007` | intermédiaire | formulaire de club | destinataire, échéance, absence de date d'activité | formatif |
| `qc-pri-ilss-004-q-008` | transfert | deux documents complémentaires | lieu/moment/matériel, provenance correcte | entraînement de transfert |
| `qc-pri-ilss-004-q-009` | transfert | **bibliothèque : tableau + avis** | **preuve A**, 4 informations correctes, 2 segments montrés, autonomie | maîtrise A |
| `qc-pri-ilss-004-q-010` | transfert | **atelier de sciences : message + formulaire** | **preuve B**, 5 informations + cases, 2 segments montrés, autonomie | maîtrise B |

**Lien explicite pour CHAQUE item :** `objectif_id=obj-1`, `critere_id=crit-1`, `family_id=qc-pri-ilss-004-ev-01`. Ces clés figurent également dans les dix objets du JSON. Les huit premiers items vérifient des composantes progressives du critère; seuls 009 et 010 servent à attester la preuve complète dans deux contextes.

## Déroulement des deux évaluations indépendantes

1. **Avant** l'épreuve, l'adulte choisit le support de lecture accessible avec l'élève (agrandissement, lecture neutre, CAA, pointage) et vérifie la compréhension **de la consigne**, sans préciser les champs-réponses.
2. **A, bibliothèque** : le tableau donne mardi, 10 h 20, A12; l'avis donne le livre à apporter. L'élève répond aux quatre questions et montre **au moins deux** segments/cellules utilisés.
3. **B, atelier de sciences** : le message donne jeudi 13 h 15, salle 4 et un crayon; le formulaire donne **avant mardi**, cases non cochées. L'élève retrouve les informations et montre **au moins deux** sources. Les deux contextes comportent des structures documentaires et des actions différentes.
4. **Après** chaque tentative, enregistrer les réponses exactes, les repères pointés, les accommodements et tout indice directif intervenu. Une réponse soufflée n'est pas comptée autonome; l'adulte peut interrompre une passation si le support devient inaccessible.
5. Appliquer `GRILLE_MAITRISE.md` **séparément** à A et B; ne pas moyenner une note. Si une dimension essentielle est insuffisante, proposer remédiation ciblée et une autre épreuve fixée par un responsable humain.

## Corrigé contrôlé et variabilité permise

Les modes de banque sont **fixes**, avec `seed=null`, `parametres=null`; toutes les données sont reproduites dans `stimulus` et les solutions vérifiables dans `reponse_attendue`. **Aucune génération IA libre** ni remplacement automatique des lieux, heures, formulaires ou corrigés. La seule variabilité permise porte sur **la présentation et la réponse** (taille et contraste, lecture à voix haute neutre, version textuelle d'un pictogramme, support tactile accessible validé, dispositif de communication, temps et pauses). La réponse ne doit pas être indiquée à la place de l'élève. Les pictogrammes sont du **texte décrit et légendé**; aucune compréhension d'un logo non légendé n'est présumée.

## Sécurité, droits et équité

Aucun document réel, aucune collecte de nom, numéro, adresse, religion, allergie, nationalité ou statut migratoire. Les cases « participation » sont **fictives** et aucune décision d'inscription réelle n'est demandée. Ne pas noter la vitesse de lecture, le français d'origine, l'aisance d'accent, la réussite antérieure du système scolaire ni l'expression émotionnelle. Si l'accès auditif, visuel ou à l'écrit pose problème, établir une modalité équivalente avec l'équipe pédagogique et noter précisément ce qui a été adapté. Toutes les productions textuelles sont originales et ne nécessitent ni image ni licence audio.

## Limite de validité

Les corrigés ont une correspondance textuelle explicite mais la fiabilité interévaluateurs, la lisibilité des supports, l'équivalence linguistique des adaptations et la durée de passation n'ont **pas** été essayées avec des élèves. Les items sont `a_revoir`, non qualifiés d'examen homologué ni certifié.
