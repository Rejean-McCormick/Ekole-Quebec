# Plan d'évaluation — qc-pri-fr-005

**Objet unique :** `obj-1` — Repérer des informations explicites et les restituer fidèlement après lecture ou écoute.  
**Critère de preuve :** `crit-1` — Répondre à des questions littérales en citant un indice présent dans le texte.  
**Famille inchangée :** `qc-pri-fr-005-ev-01` ; **type :** `réponse_argumentée` (réponse courte justifiée, pas débat d'opinion).  
**Banque :** `BANQUE_ITEMS.json` ; **grille :** `GRILLE_MAITRISE.md` ; **statut :** `a_revoir` (aucune certification).

## Architecture : planifier les preuves avant de donner les questions

Chaque item a `objectif_id=obj-1`, `critere_id=crit-1` et `family_id=qc-pri-fr-005-ev-01`. Les réponses et citations doivent être fidèles à **un stimulus entièrement visible ou entièrement lu**, jamais à une connaissance externe. Les 12 items sont **fixes**; pas de génération libre, pas de paramètres variables ni de seed applicable. Le contenu et les clés de correction restent verrouillés jusqu'à une révision humaine.

| Items | Contexte / manifestation | Notions couvertes et question | Difficulté | Représentation | Fonction |
|---|---|---|---|---|---|
| 001 | Récit de jardin, preuve **A** | personnage qui accompagne | initial | récit écrit ou lecture neutre | preuve d'exactitude + citation |
| 002 | Même récit, preuve A | lieu | initial | récit | preuve |
| 003 | Même récit, preuve A | temps précis écrit | intermédiaire | récit | preuve |
| 004 | Même récit, preuve A | fait explicite / objet | intermédiaire | récit | preuve |
| 005 | Avis à une classe, preuve **B** | responsable nommé | initial | avis fonctionnel | preuve en nouveau contexte |
| 006 | Même avis, preuve B | heure explicitée | intermédiaire | avis | preuve |
| 007 | Même avis, preuve B | lieu | intermédiaire | avis | preuve |
| 008 | Même avis, preuve B | matériel demandé | transfert | avis | preuve |
| 009 | Consigne de classe, contrôle **C** | acteur | initial | consigne descriptive | rappel différé ou stabilité |
| 010 | Même consigne, contrôle C | temps | intermédiaire | consigne | rappel |
| 011 | Même consigne, contrôle C | lieu | intermédiaire | consigne | rappel |
| 012 | Même consigne, contrôle C | action d'un deuxième acteur | transfert | consigne | rappel |

**Couverture vérifiable :** personnage/personne (001, 005, 009), lieu (002, 007, 011), temps (003, 006, 010), faits explicites (004, 008, 012). Preuve A et preuve B sont des **stimuli inédits** de genres différents, administrés sans correction intermédiaire; elles attestent deux manifestations de l'objectif et non deux scores d'un même texte. C propose une troisième forme pour rappel/confirmation, sans remplacer les deux preuves distinctes requises.

## Protocole d'administration

1. Confirmer que l'élève ne connaît pas les textes A et B. Présenter chaque stimulus en entier une fois, puis le laisser consultable ou le relire intégralement et neutralement à la demande. Pour une personne qui ne lit pas encore le texte couramment, lecture par l'adulte possible si le but reste la compréhension; noter « écoute » plutôt que conclure sur le décodage.
2. Donner la consigne standard : **« Réponds à chaque question. Cite les mots du texte qui prouvent ta réponse. »** L'élève peut citer à voix haute ou souligner des mots qu'il lit; si le stimulus est oral, il répète l'expression entendue. Un scribe neutre note les propos sans apporter de précision.
3. Dans chaque contexte, recueillir les quatre réponses et les quatre citations **avant tout feedback**. Faire A et B en séances indépendantes si souhaité, toujours sans modelage ni indice de localisation sur ces stimuli. La répétition entière et neutre du texte est permise et consignable; une reformulation qui révèle la réponse ne l'est pas.
4. Noter exactitude (E), indice pertinent (I) et autonomie (A) par item, puis appliquer la grille à **chaque contexte séparément**. Ne pas établir la maîtrise par la somme des points A+B.
5. Conserver la réponse originale hors du canon pour audit local; ne pas intégrer les données personnelles au workspace livré. Ne jamais exposer le corrigé de B avant le recueil de B.

## Rubrique et décision

Par item : **E=1** si la réponse restitue la donnée littérale demandée sans contresens; **I=1** si les mots cités sont présents et étayent directement cette réponse; sinon 0. **Autonomie de contexte** requise : aucune indication ciblée vers la réponse ou la citation. Pour un contexte à 4 items, il est **satisfaisant** si les quatre réponses sont fidèles, les quatre indices probants et si l'ensemble a été produit sans aide de localisation. Ce seuil strict est une **règle de conception interne révisable**, non une norme scolaire externe. Un contexte échoué ne peut pas être compensé par le succès dans un autre.

**Décision de maîtrise :** A satisfaisant **et** B satisfaisant, avec autonomie documentée. Si A ou B est partiel, diagnostiquer la notion en défaut, remédier, puis administrer après validation humaine un **nouveau** stimulus d'un genre comparable; ne jamais réutiliser un texte dont la solution a été donnée pour une preuve indépendante. La série C, si encore inconnue, peut éclairer la stabilité; elle ne garantit pas à elle seule deux nouveaux contextes indépendants après diffusion de A/B.

## Variabilité contrôlée, corrigés, biais et sécurité

- Variantes permises **sans changer le stimulus** : orthographe non gênante, reformulation fidèle (« son grand-père »/« le grand-père d'Inès »), citation minimale ou phrase complète tant que le lien est explicite; réponse orale/écrite. Ne jamais remplacer « dans » par « devant », « trois » par « plusieurs », « heure » par « jour ».
- Un **nouveau texte** ne constitue pas une variation automatique autorisée; une version alternative requiert une nouvelle entrée documentée, une réponse verrouillée, des tests et une revue humaine.
- Enjeu culturel : histoires fictives ordinaires, pas de connaissance du jardin, de la bibliothèque ou du matériel scolaire requise pour répondre; lecture entière possible, sans décoration ni code couleur exclusif.
- Enjeu de confidentialité : pas de données réelles d'enfant ni demande de parler de sa famille. Aucune mesure de la voix, vitesse de décodage, écriture manuscrite ou orthographe.
- **Limites de contrôle :** les valeurs textuelles et la concordance questions/indices sont vérifiables, mais une interprétation humaine doit valider lisibilité, équité des formulations, expérience d'administration et pertinence des seuils. Pas de générateur IA libre comme contrôleur fiable.
