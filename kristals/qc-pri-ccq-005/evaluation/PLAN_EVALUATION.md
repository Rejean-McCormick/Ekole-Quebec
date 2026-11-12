# Plan d'évaluation — `qc-pri-ccq-005`

**`obj-1` (intact) :** Distinguer informations, opinions et influences dans des contenus médiatiques.  
**`crit-1` (intact) :** Analyser un message fictif et expliciter deux mécanismes d’influence.  
**Famille unique :** `qc-pri-ccq-005-ev-01` ; type de famille `observation_ou_production`. Tous les items sont **des productions analysables**, pas des QCM de croyances. Les réponses attendues sont des modèles justifiés, jamais des opinions imposées.

## Plan de couverture et traçabilité

Chaque ligne relie explicitement l'item à `obj-1`, `crit-1` et `qc-pri-ccq-005-ev-01`. Les tâches initiales permettent de localiser les erreurs; les deux dernières constituent les preuves autonomes de maîtrise.

| Item | Niveau | Représentation | Rôle | Cible particulière | Lien figé |
|---|---|---|---|---|---|
| 001 | initial | cartouche de journal fictif | formatif_D1 | classement | `obj-1` / `crit-1` / `qc-pri-ccq-005-ev-01` |
| 002 | initial | mini-publicité fictive sur une carte | formatif_D3 | mécanismes | `obj-1` / `crit-1` / `qc-pri-ccq-005-ev-01` |
| 003 | initial | transcription de capsule audio fictive | formatif_D2 | source | `obj-1` / `crit-1` / `qc-pri-ccq-005-ev-01` |
| 004 | intermediaire | publication numérique fictive | formatif_D1_D3 | classer/expliquer | `obj-1` / `crit-1` / `qc-pri-ccq-005-ev-01` |
| 005 | intermediaire | deux commentaires fictifs sur une affiche | formatif_D2_D4 | réputation/sources | `obj-1` / `crit-1` / `qc-pri-ccq-005-ev-01` |
| 006 | intermediaire | billet commandité fictif | formatif_D1_D2_D3 | commandite | `obj-1` / `crit-1` / `qc-pri-ccq-005-ev-01` |
| 007 | intermediaire | affiche illustrée transcrite | formatif_D3 | mécanismes | `obj-1` / `crit-1` / `qc-pri-ccq-005-ev-01` |
| 008 | intermediaire | notice de blogue fictive | formatif_D4 | respect | `obj-1` / `crit-1` / `qc-pri-ccq-005-ev-01` |
| 009 | transfert | affiche papier — jardin collectif fictif | preuve_A | preuve A, sans indice | `obj-1` / `crit-1` / `qc-pri-ccq-005-ev-01` |
| 010 | transfert | transcription audio — bibliothèque imaginaire | preuve_B | preuve B, sans indice | `obj-1` / `crit-1` / `qc-pri-ccq-005-ev-01` |


## Mode, situations et critères

- Tous les items sont en mode **`fixe`**, sans paramètre calculé, sans algorithme ni seed requis (`seed: null`, `parametres: null`). Aucune génération autonome d'énoncés n'est permise; les scénarios et corrigés sont fermés, leur lecture verbatim vérifiable. Le champ hérité `seed_reproductible: true` du contrat de base reste inchangé, sans prétendre qu'un générateur a été exécuté.
- q-001 à q-008 : **formatifs**, utilisables comme productions observées. Certaines tâches isolent une sous-compétence plutôt que d'exiger toute la preuve `crit-1`. Elles ne peuvent pas certifier seules la maîtrise.
- q-009 **preuve A** : **affiche papier** d'une équipe de jardin fictive, deux procédés « popularité alléguée + urgence ». q-010 **preuve B** : **capsule audio transcrite** d'une bibliothèque imaginaire, deux procédés « autorité alléguée + émotion ». Les médias, contextes et leviers dominants diffèrent; ni le lexique ni les réponses ne sont recyclés mot à mot.
- Dans chaque preuve : D1 classification des propositions, D2 source / réputation / limites, D3 deux mécanismes différents, citation et effet possible pour chacun, D4 justification prudente et respectueuse. Chaque dimension 0–3 et seuil **D1, D2, D4 ≥ 2 et D3 ≥ 2** aux DEUX preuves (voir `GRILLE_MAITRISE.md`). Le total /12 est **informatif et non décisif**.
- Au niveau 2 en D3, l'analyse nomme **deux familles différentes**, cite un indice lisible pour chacune et décrit le rôle persuasif plausible de chacune. Un seul mécanisme nommé deux fois vaut au plus niveau 1. Une source ne devient pas fiable parce qu'elle a un nom.
- Corrigés : les informations exactes sont contrôlées **à l'intérieur de chaque dossier fictif**; des paraphrases raisonnables sont acceptées. Un jugement « la publicité est bonne/mauvaise » sans indice n'est pas une réponse de maîtrise; une opinion personnelle sur la cause n'est jamais exigée.

## Variabilité et contrôles

Aucune substitution automatique d'auteurs, dates, lieux, dates, arguments ou mécanismes dans les dix items. Seules sont admises : segmentation visuelle, police adaptée, lecture humaine **verbatim**, transcription orale fidèle, ordre de présentation des phrases de réponse, et synonymes justifiés sans changement des assertions. Toute nouvelle variante de contenu exige nouveau document, correction explicite, contrôle de biais et révision humaine; ne jamais déclarer une variation IA libre validée.

## Passation, équité et sécurité

1. Avant q-009 et q-010, retirer cartes d'indices, modèles, glossaires révélant les procédés et feedback directif; autoriser les adaptations d'**accès** (temps, lecture neutre, grand caractère, transcription fidèle), mais noter si un soutien **cognitif** est intervenu, car une preuve ainsi assistée ne satisfait pas le critère d'autonomie.
2. Administre les preuves dans deux séances ou avec séparation permettant un nouveau traitement, sans donner le corrigé de A avant B. Conserver deux traces datées séparément dans l'environnement autorisé; ne pas enregistrer de voix ou de personnes identifiables par défaut.
3. Aucun compte réel, capture de réseau social, personnalité réelle, enfant identifiable, donnée privée, discours haineux ni croyance intime. On décrit le mécanisme de **messages inventés**, sans évaluer l'identité du lecteur ni une adhésion à un enjeu.
4. Évaluer la **qualité de la justification**, pas l'aisance en lecture lorsqu'un format d'accès équivalent est offert. Une faute orthographique n'annule pas une explication comprise; examiner les biais linguistiques/culturels avant utilisation sommative.
5. En cas d'une seule preuve réussie ou d'une dimension insuffisante, décision **« maîtrise non encore attestée »**, remédiation ciblée puis nouveau contexte rédigé et corrigé; ne pas « repasser » la même preuve avec le corrigé mémorisé.

## Rappel et limitations

Un rappel sur texte inédit après une période espacée (suggestion de design : 7–14 jours) apporte une observation de stabilité; la réussite des deux preuves est nécessaire mais la publication dépend toujours d'une **revue humaine** : lisibilité, durée, conséquences d'une adaptation orale, équivalence des exigences A/B, descriptions exactes, absence de biais et convenance des seuils. **Aucun item n'est certifié** et aucune homologation PFEQ n'est revendiquée.
