# Plan d'évaluation — `qc-pri-fr-010` (proposition v1.2 non qualifiée)

**Références invariantes de TOUS les items :** objectif `obj-1` — « Exprimer une réaction argumentée à une lecture en distinguant goûts et indices textuels. »; critère `crit-1` — « Défendre une appréciation personnelle fondée sur deux éléments du texte. »; famille `qc-pri-fr-010-ev-01`; type de famille `réponse_argumentée`. Tous les stimuli sont des textes originaux **fixés**. Il n'existe pas de moteur de génération libre de questions ou de correction par IA fiable implicite.

## Table de traçabilité, difficulté et représentation

| Item de `BANQUE_ITEMS.json` | Réfs obligatoires | Difficulté | Représentation / contexte | Usage et couverture |
|---|---|---|---|---|
| `qc-pri-fr-010-q-001` | `obj-1` · `crit-1` · `qc-pri-fr-010-ev-01` | initial | Court récit : plan de la cour | Diagnostic argumenté : opinion, critère et deux actions. |
| `qc-pri-fr-010-q-002` | `obj-1` · `crit-1` · `qc-pri-fr-010-ev-01` | initial | Information pratique : coin lecture | Apprécier la clarté d'une explication avec deux règles. |
| `qc-pri-fr-010-q-003` | `obj-1` · `crit-1` · `qc-pri-fr-010-ev-01` | intermédiaire | Récit : cerf-volant | Appréciation nuancée, distinction de deux épisodes. |
| `qc-pri-fr-010-q-004` | `obj-1` · `crit-1` · `qc-pri-fr-010-ev-01` | intermédiaire | Texte descriptif : sentier | Critère d'utilité et deux informations distinctes. |
| `qc-pri-fr-010-q-005` | `obj-1` · `crit-1` · `qc-pri-fr-010-ev-01` | transfert | Invitation : échange de graines | Transférer une réaction argumentée à une annonce. |
| `qc-pri-fr-010-q-006` | `obj-1` · `crit-1` · `qc-pri-fr-010-ev-01` | transfert | Note d'observation : ombre | Transférer la compétence à un compte rendu. |
| `qc-pri-fr-010-q-007` | `obj-1` · `crit-1` · `qc-pri-fr-010-ev-01` | transfert | Récit inédit : spectacle déplacé | **Preuve de maîtrise A** : intérêt des actions/personnages; réservé. |
| `qc-pri-fr-010-q-008` | `obj-1` · `crit-1` · `qc-pri-fr-010-ev-01` | transfert | Texte informatif inédit : suivi des pluies | **Preuve de maîtrise B** : clarté d'une démarche; réservé, contexte distinct. |

Les **huit** items évaluent explicitement la réaction personnelle, un aspect pertinent, **deux preuves textuelles non redondantes** et le lien explicité de chacune. `q-007` et `q-008` sont à faire sur deux textes **jamais montrés lors des exercices**; ils constituent deux manifestations en **genres différents** (récit vs information). Si la banque est exposée avant l'épreuve, créer d'abord deux nouveaux stimuli **revus par un humain** aux mêmes exigences; une substitution non contrôlée n'est pas une validation.

## Consigne et conduite d'évaluation

1. Présenter intégralement le texte et : « Donne ton appréciation du texte. Nomme un aspect sur lequel tu portes ton jugement. Appuie ton avis sur **deux détails différents du texte** et explique pourquoi chacun soutient ton avis. » Ne donner aucun indice sur les détails à choisir.
2. Noter la modalité (lecture autonome, audio fidèle, lecture humaine; réponse écrite, orale ou dictée), la présence d'aide d'accès et toute **aide au raisonnement**. Une aide de raisonnement rend l'essai formatif et non autonome.
3. Repérer précisément les deux ancrages textuels dans le stimulus. Accepter citation exacte ou paraphrase **fidèle**. Vérifier l'absence d'invention, de doublon et de lien causal non étayé.
4. Appliquer la grille analytique `GRILLE_MAITRISE.md` : A (avis/critère), B (deux éléments distincts fidèles), C (deux liens argumentatifs), D (indépendance, preuve de procédure). Deux correcteurs humains peuvent comparer leurs décisions; si désaccord, documenter le passage en cause.
5. Après correction, donner un feedback descriptif : réussite, détail non retrouvé, doublon ou lien à expliquer; proposer un texte neuf pour la remédiation, sans donner la réponse de l'épreuve pendant qu'elle se déroule.

**Barème descriptif :** A/B/C chacun 0, 1 ou 2 (6 possibles); D consigné séparément comme 0, 1 ou 2. La maîtrise n'est **pas** un score de 5/6 ni une moyenne : il faut, dans **deux contextes différents**, A=B=C=2, avec au moins une prestation D=2 (aucune aide de raisonnement), et une absence de contradiction majeure avec le texte. Si une réponse est obtenue avec une suggestion d'indice, répéter la mesure sur un texte jamais utilisé. Le jugement personnel n'est pas noté comme « bon » ou « mauvais ».

## Variations et contrôles

- **Mode réel :** tous les items de cette livraison sont `fixe`; `seed: null` et `parametres: null` sont volontaires. Il n'existe **aucune** transformation paramétrique ou calcul de solution à tester pour les items actuels.
- **Variabilité admise :** formulation personnelle des opinions et du critère, sélection de deux autres faits effectivement attestés dans le même stimulus, paraphrase fidèle, longueur raisonnable, réponse orale ou écrite. La grille **reste identique**.
- **Variabilité interdite sans nouvelle revue :** réécriture automatique du stimulus, remplacement d'une action par une autre, modification de nombres/heures, ajout d'un fait culturel implicite, notation de l'orientation de l'avis ou génération d'un corrigé par IA sans vérification. Chaque stimulus substitué devient un **nouvel item à revoir**, même si le scénario semble similaire.
- **Couverture :** q001–002 initiaux, q003–004 intermédiaires, q005–006 transferts de genres, q007–008 preuves autonomes en deux contextes. Deux exemples résolus, deux diagnostics, trois guidés et quatre autonomes figurent hors banque dans `contenu/`.
- **Sécurité :** personnages et cadres fictifs; aucune divulgation personnelle; aucune action réelle dangereuse demandée; aucun jugement sur identité, convictions, accent ou goût esthétique. Éviter de supposer une expérience culturelle partagée.
- **Accessibilité :** textes lisibles et disponibles en version audio fidèle, segmentation/agrandissement, pauses et temps flexible, scripteur neutre, modalités orales si souhaitées. La lecture à voix haute est notée comme modalité; elle ne donne pas d'indices argumentatifs. Aucun renseignement indispensable porté uniquement par une image ou couleur.

**Qualification suspendue :** tous les items ont `validation_status: a_revoir`. Une revue humaine (langue fr-CA, pertinence des textes, équité, justesse des rubriques, temps et essai réel) est exigée avant un usage sommatif ou une déclaration de qualification.
