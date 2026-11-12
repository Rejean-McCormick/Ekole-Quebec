# PLAN D’ÉVALUATION — `qc-pri-als-004-ev-01`

**Alignement invariant pour tous les items :** `qc-pri-als-004`, `obj-1` = « Produire de manière intelligible des sons, accents et rythmes élémentaires. »; `crit-1` = « Enregistrer un court message compréhensible après modelage. ». Les items préparent ou documentent le même critère sans prétendre qu’un seul exercice le certifie. Type gouvernance : `observation_ou_production`; la banque utilise `fixe` ou `scenario_controle` à variables fermées, **aucune génération IA aléatoire**.

## Plan de couverture et contrôles
| Item | Complexité | Représentation | Phonèmes | Accentuation | Rythme | Contexte, variabilité permise | Rôle |
|---|---|---|---|---|---|---|---|
| `q-001` | initial | salut oral | /h/ | — | groupe bref | accueil, texte fixé | formatif |
| `q-002` | initial | image décrite + oral | /s/–/ʃ/ | — | deux groupes | see/she fixés | formatif |
| `q-003` | initial | syllabes entendues | — | HEL-lo | salut | Sam fictif | formatif |
| `q-004` | intermédiaire | manque de matériel | — | NEED / PENcil | groupe demande | crayon, texte fixé | formatif |
| `q-005` | intermédiaire | chapeau + oral | /h/ | HAT informative | deux groupes | chapeau, texte fixé | formatif |
| `q-006` | intermédiaire | boîte imaginaire | /h/ (help) | HELP informatif | demande polie | paraphrase approuvée | formatif |
| `q-007` | intermédiaire | sac bleu | /h/ (hi/have) | BLUE BAG | présentation | formule courte permise | formatif |
| `q-008` | intermédiaire | pastilles + oral | — | ba-NA-na, HEL-lo | groupes de mots | texte fixé | formatif |
| `q-009` | transfert | couleur à corriger | — | BLUE contraste | unité blue pen | texte fixé ou please | formatif |
| `q-010` | transfert | invitation après école | /h/ (hi) | PLAY / SCHOOL | message | texte fixé | formatif |
| `q-011` | transfert | **audio classe** + description | /h/ | hello / NEED / objet | plusieurs groupes | A pencil ou B eraser | **preuve A** |
| `q-012` | transfert | **audio parc** + description | /h/ | PLAY / PARK / objet | plusieurs groupes | A ball ou B kite | **preuve B** |

Tous les items : **`objectif_id: obj-1`, `critere_id: crit-1`, `family_id: qc-pri-als-004-ev-01`**. Les tâches formatives évaluent seulement les dimensions annoncées; seuls `q-011` et `q-012` servent ensemble à la décision de maîtrise.

## Protocole de correction humain, reproductible
1. L’enseignant présente une courte situation en français, fait entendre des **modèles génériques pendant l’enseignement**, et ne les répète **pas pendant les preuves**. Une variante `A` ou `B` est choisie et notée avant la passation; il n’y a ni seed aléatoire ni invention de nouveau corpus.
2. L’élève enregistre 10–30 s environ (durée indicative, **non notée**). Une prise intégrale autonome supplémentaire est autorisée pour incident technique ou débit empêchant l’enregistrement; ni indices ni souffle sur le contenu entre les prises finales. En présence de reprise pédagogique, la nouvelle épreuve est datée séparément.
3. À l’écoute, l’auditeur note **sans regarder le corrigé textuel** les deux informations-clés; il consulte ensuite la fiche de la variante pour les comparer. Si un seul évaluateur est disponible, masquer le script au premier passage et conserver sa transcription spontanée; consigner le risque de biais.
4. Cotation analytique indépendante **0 / 1 / 2** pour chacun : **(I)** intelligibilité effective des deux informations (0 aucune; 1 une seule ou reconstruction avec indices; 2 les deux), **(P)** phonèmes utiles (0 altérations gênant régulièrement; 1 quelques altérations sans perte majeure; 2 contrastes suffisamment nets), **(A)** accentuation (0 aucun relief utilisable; 1 relief partiel; 2 relief utile), **(R)** rythme et groupements (0 blocs coupés gênants; 1 quelques interruptions; 2 groupes soutenant le sens). Pour les phrases très courtes, un trait non observable doit être **non évalué**, et non 0 automatique.
5. **Maîtrise** : les **deux** preuves indépendantes `q-011` et `q-012`, réalisées sans assistance, doivent chacune recevoir I=2 et P≥1, A≥1, R≥1. Aucun calcul de moyenne ne remplace le seuil par dimension. Si une dimension non observable subsiste sur un item, recueillir une **nouvelle preuve** dans ce contexte avant décision.
6. **Feedback** : rapporter d’abord ce qui a été compris (« J’ai entendu que tu veux un crayon »), puis un seul conseil (« rends /h/ de hello plus perceptible »), puis micro-remédiation et essai sur une situation **non identique**. Ne pas utiliser un classificateur vocal automatique non validé pour décider de la maîtrise.

## Protection, accessibilité, variabilité
- Protéger les audios d’enfants : consentement ou autorisation selon l’établissement et les responsables, LMS restreint ou dispositif sécurisé, conservation limitée selon politique locale, jamais de publication publique ni de données personnelles dans ce delta.
- Fournir consignes en français, objets réels/dessins + descriptions textuelles, modèle oral et texte optionnel **pendant l’apprentissage**. Éviter de laisser le script intégral à lire pendant les prises autonomes de maîtrise si cela masquerait la compétence prosodique; offrir un accès équitable adapté documenté.
- Micro adapté, pièce calme, temps supplémentaire et préparation indépendants admis; dysfluence, variation dialectale, accent francophone, timbre/hauteur individuels non évalués en eux-mêmes. Si une accommodation change la nature de `crit-1` (enregistrement vocal), demander et documenter une décision d’adaptation avant de le déclarer satisfait.
- Limiter la variabilité : `q-001` à `q-010` modèles fixes avec paraphrases **explicitement** admises; `q-011`/`q-012` variantes `A/B` dans les `parametres`, sans générateur libre et sans seed. Tout élargissement du vocabulaire requiert une revue humaine, une mise à jour du corrigé et une nouvelle version.

## Sécurité scientifique de la décision
Pas d’égalisation phonétique exhaustive des variétés d’anglais; `HEL-lo`, `ba-NA-na` et les messages ont été vérifiés au niveau linguistique des références listées, mais **aucune revue d’un phonéticien, aucun essai avec des élèves ni étude inter-juges** n’a été effectuée. Aucun item n’est certifié. Un correcteur humain connaissant l’anglais oral doit vérifier la compréhensibilité dans chaque situation avant emploi à enjeu.
