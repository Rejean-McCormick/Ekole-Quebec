# PLAN_EVALUATION — `qc-pri-ale-003`

## 1. Contrat et jugement évaluatif

**Objectif observable, invariant (`obj-1`) :** Lire un passage anglais avec précision et rythme permettant la compréhension.  
**Preuve autonome, invariante (`crit-1`) :** Relire un texte nouveau avec meilleure exactitude et phrasé.  
**Famille invariante :** `qc-pri-ale-003-ev-01` ; **type natif :** `réponse_argumentée`. Dans cette discipline, l'argumentation est une brève explication des choix de lecture après la prestation; la preuve principale reste **la lecture orale observée deux fois**, et non une réponse écrite à un QCM.

Les textes de [BANQUE_ITEMS.json](BANQUE_ITEMS.json) sont fixes, originaux, en anglais correct. La [grille](GRILLE_MAITRISE.md) décrit la mesure lexicale et les niveaux d'exactitude (A), phrasé (P), continuité (C), révision autonome (R). Chaque item porte explicitement `obj-1`, `crit-1` et `qc-pri-ale-003-ev-01`. Les questions de compréhension littérales servent à détecter une lecture dépourvue de sens, sans permettre d'inférer la lecture fluide à partir d'une simple bonne réponse.

## 2. Matrice de couverture, difficulté, représentation

| Item | Usage | Difficulté | Représentation | Traçabilité | Observation / barème |
|---|---|---|---|---|---|
| q-001 | Diagnostic | initial | lecture_diagnostic | `obj-1` / `crit-1` / `qc-pri-ale-003-ev-01` | A,P,C,R + sens littéral |
| q-002 | Diagnostic | initial | lecture_diagnostic | `obj-1` / `crit-1` / `qc-pri-ale-003-ev-01` | A,P,C,R + sens littéral |
| q-003 | Guidé | initial | lecture_accompagnee | `obj-1` / `crit-1` / `qc-pri-ale-003-ev-01` | A,P,C,R + sens littéral |
| q-004 | Guidé | intermediaire | lecture_accompagnee | `obj-1` / `crit-1` / `qc-pri-ale-003-ev-01` | A,P,C,R + sens littéral |
| q-005 | Guidé | intermediaire | lecture_accompagnee | `obj-1` / `crit-1` / `qc-pri-ale-003-ev-01` | A,P,C,R + sens littéral |
| q-006 | Autonomie formative | intermediaire | message_instructif | `obj-1` / `crit-1` / `qc-pri-ale-003-ev-01` | A,P,C,R + sens littéral |
| q-007 | Autonomie formative | intermediaire | recit_meteo | `obj-1` / `crit-1` / `qc-pri-ale-003-ev-01` | A,P,C,R + sens littéral |
| q-008 | Autonomie formative | intermediaire | notice_informative | `obj-1` / `crit-1` / `qc-pri-ale-003-ev-01` | A,P,C,R + sens littéral |
| q-009 | Autonomie formative | intermediaire | recit_dialogue | `obj-1` / `crit-1` / `qc-pri-ale-003-ev-01` | A,P,C,R + sens littéral |
| q-010 | Transfert | transfert | dialogue_narratif | `obj-1` / `crit-1` / `qc-pri-ale-003-ev-01` | A,P,C,R + sens littéral |
| q-011 | Transfert | transfert | texte_de_consigne | `obj-1` / `crit-1` / `qc-pri-ale-003-ev-01` | A,P,C,R + sens littéral |
| q-012 | Preuve A | transfert | recit_exploration_parc | `obj-1` / `crit-1` / `qc-pri-ale-003-ev-01` | A,P,C,R + sens littéral |
| q-013 | Preuve B | transfert | information_projet_collectif | `obj-1` / `crit-1` / `qc-pri-ale-003-ev-01` | A,P,C,R + sens littéral |

**Couverture :** aux diagnostics, une première lecture suffit et R n’est pas coté; toutes les autres tâches font lire puis relire. 2 diagnostics de décodage et de groupes de sens; 3 guidages à étayage dégressif; 4 réinvestissements autonomes; 2 transferts de genre (dialogue et texte instructif); 2 manifestations formelles inédites dans des contextes **narratif de promenade** et **informatif scolaire**. Pour tous les items, la réponse attendue est **une lecture réelle documentée**, plus la réponse littérale explicitement écrite dans le JSON. La tâche de lecture ne peut être remplacée par une sélection de choix. Les passages des preuves sont exclus des leçons et pratiques.

## 3. Protocole uniforme de passation

1. Proposer un support lisible **sans slash de segmentation** ni enregistrement de l'adulte. Définir les aménagements non indicatifs avant l'essai. Passage inconnu à la première rencontre. Sauf aux diagnostics, ne pas avoir enseigné ce texte ni ses corrections.
2. Première lecture orale intégrale, sans interruption correctrice. L'observateur relève dans l'ordre les mots imprimés, omissions, substitutions, ajouts et autocorrections; il décrit une pause mal placée et une réussite de phrasé.
3. Entre les lectures : 45 à 60 secondes proposées (adaptables) de relecture visuelle et réflexion **silencieuse, personnelle et sans aide lexicale** pour pratique, transfert et maîtrise. Aucun mot prononcé par l'adulte; pas de barres de phrasé données. Répéter le protocole avec adaptations temporelles non normatives.
4. Deuxième lecture orale du **même** passage; relever à nouveau les mêmes indicateurs. Poser ensuite la question littérale de l'item. L'élève peut dire quelle ponctuation ou quelle séquence de mots l'a aidé; réponse orale, geste ou note, sans juger son vocabulaire métalinguistique.
5. Comparer les deux lectures et consigner l'aide effective. L'enseignant n'impose pas une réalisation unique du phrasé; accepter les limites de groupes qui préservent la syntaxe et le sens. Aucune décision automatique à partir d'une IA de reconnaissance vocale.

**Comptage reproductible** : chaque unité séparée par un espace du passage original compte pour un mot imprimé; guillemets et ponctuation attenants ne créent pas de mots. Une hésitation sans mot incorrect n'est pas une erreur; autocorrection spontanée aboutie = mot correct pour l'essai; substitution, omission, ajout non rectifié et inversion altérant l'ordre = erreurs décrites. Les mots ajoutés ne modifient pas le dénominateur, mais affectent le suivi qualitatif et la note de continuité/exactitude. Noter toute difficulté dialectale/intelligibilité séparément et vérifier humainement, jamais la punir mécaniquement. Ratio `corrects / mots imprimés * 100` pour chaque lecture; ne pas prétendre mesurer la vitesse.

## 4. Barème, acceptations et limites de variation

Sur chaque essai, noter **A, P, C** de 0 à 3 selon la grille et le pourcentage d'exactitude; après relecture, noter **R** de 0 à 3 sur une amélioration concrètement repérable ou un effet plafond documenté. Question de compréhension : correcte, partiellement correcte, non vérifiable; l'élève peut répondre par pointage ou écrit si la langue orale n'est pas l'objet de cette question auxiliaire. Le seuil de sortie éditoriale est **A ≥ 2, P ≥ 2, C ≥ 2, R ≥ 2** et sens littéral préservé dans **chacune** des preuves A et B; autonomie documentée. Les seuils (dont ≥95 % pour A2) sont des **hypothèses internes à éprouver**, non standards ministériels ni étalons psychométriques externes.

**Variation admissible** : taille de caractères, contraste, espacement, bande de lecture, lieu calme, temps de réflexion flexible, observation directe au lieu d'audio. Aucune variante de passage ou de ponctuation n'est générée pour ces 13 items; `mode=fixe`, `seed=null`, `parametres=null`. Une autre version requiert une **nouvelle validation humaine**. Réponse au sens peut être reformulée sans perdre les faits du passage. Un accent reconnaissable/dialecte d'anglais intelligible ne diminue pas A; timbre, intensité et vitesse brute ne sont pas notés. Synthèse vocale utilisée comme modèle = outil d'enseignement, incompatible avec une lecture autonome non assistée lors de la preuve.

## 5. Épreuves formelles distinctes

**Preuve A (`q-012`)** : récit d'une promenade dans un parc, 68 mots imprimés, information narrative et courte question dans un dialogue. Deux lectures du même passage inconnu, sans modèle ni mots soufflés. Cible: reconnaître les mots, séquencer les phrases, conserver les groupes de lieu, distinguer la question. Contrôle: « What did Nina draw later? » → dessin de la scène dans son cahier. Enregistrer L1 et L2, A/P/C/R, indices reçus et conditions d'accès.

**Preuve B (`q-013`)** : description informative d'un coin de lecture, 71 mots, instructions et échange bref. Recommencer avec un autre texte **inconnu et dans une autre séance/occasion**; aucune transmission des mots ou groupements corrects par le professeur. Contrôle: « Where did Amira point? » → vers le panier. Les deux épreuves évaluent la même compétence mais pas un apprentissage par cœur d'un unique passage; la décision dépend de leur cohérence et des observations d'autonomie.

**Désaccords ou plafond** : si une lecture initiale atteint déjà une précision ≥98 % et un phrasé clair, ne pas créer d'erreur artificielle pour exiger un gain; noter le haut niveau maintenu et un ajustement/choix de groupe s'il existe. Si un texte est insuffisant, proposer des interventions ciblées puis un **autre texte inédit de difficulté comparable, soumis à revue**; ne pas réutiliser l'échec comme « nouvelle preuve » par mémorisation. La décision reste humaine.

## 6. Qualité, sécurité, accessibilité, droits et limites

Textes anglais produits dans ce delta; aucune revendication de conformité au PFEQ, aucun manuel externe, aucune image ou audio copié. La lecture à voix haute peut provoquer de l'anxiété; privilégier passation privée, permission de pause, consignes positives et confidentialité. Ne pas juger accent, identité culturelle, trouble de l'élocution ni puissance vocale; toute adaptation qui transforme la lecture indépendante en écoute assistée nécessite une autre procédure de validité et une décision humaine. Ne stocker d'audio qu'avec autorisations locales; la feuille d'observation suffit par défaut.

**Avant usage sommatif :** revue d'anglais par personne compétente, essai réel auprès du public cible, calibration intercorrecteurs, enquête d'accessibilité, examen des seuils, contrôle des droits et autorisation de la collecte des traces. État de tous les items : `a_revoir`. Le contrôle de mots effectué par script porte sur les textes fixes et l'intégrité JSON; il ne valide **pas** la pertinence développementale, une lecture enregistrée, la validité psychométrique ou la stabilité de la grille en classe.
