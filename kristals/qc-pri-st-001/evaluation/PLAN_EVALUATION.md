# Plan d'évaluation — qc-pri-st-001

**Objet strict :** `obj-1` — Observer un phénomène et poser une question investigable et précise. **Critère d'exit :** `crit-1` — Décrire un phénomène puis transformer une curiosité en question testable. **Famille inchangée :** `qc-pri-st-001-ev-01` (`generee_sous_contraintes` en blueprint natif). **Banque :** `qc.learning-item-bank/1.0` — 12 items originaux, verrouillés, tous `validation_status=a_revoir`.

## Matrice item / difficulté / représentation / rattachements

| Item | Niveau | Représentation contrôlée | Attente observable / couverture | Liens |
|---|---|---|---|---|
| `qc-pri-st-001-q-001` | initial | texte avec deux nombres | Tri observation/inférence; tache humide, durée absente | `obj-1` / `crit-1` / `qc-pri-st-001-ev-01` |
| `qc-pri-st-001-q-002` | initial | image décrite et règle | Description mesurée; feuilles et âge inconnu | `obj-1` / `crit-1` / `qc-pri-st-001-ev-01` |
| `qc-pri-st-001-q-003` | initial | comparaison de deux descriptions | Question de goût → comptage observable | `obj-1` / `crit-1` / `qc-pri-st-001-ev-01` |
| `qc-pri-st-001-q-004` | intermediaire | fiche de longueurs fictives | Jeunes plants; cause inconnue, hauteur à mesurer | `obj-1` / `crit-1` / `qc-pri-st-001-ev-01` |
| `qc-pri-st-001-q-005` | intermediaire | schéma à échelle en cases | Tissu humide; quantité d’eau à contrôler | `obj-1` / `crit-1` / `qc-pri-st-001-ev-01` |
| `qc-pri-st-001-q-006` | intermediaire | horaires et longueur | Ombres; heure, longueur et sécurité | `obj-1` / `crit-1` / `qc-pri-st-001-ev-01` |
| `qc-pri-st-001-q-007` | intermediaire | dénombrement descriptif | Piles de blocs; prédiction et sécurité | `obj-1` / `crit-1` / `qc-pri-st-001-ev-01` |
| `qc-pri-st-001-q-008` | intermediaire | états successifs décrits | Glaçon; description qualitative vs mesure à prévoir | `obj-1` / `crit-1` / `qc-pri-st-001-ev-01` |
| `qc-pri-st-001-q-009` | transfert | deux plans quadrillés | Transfert cour/flaque; temps et surface | `obj-1` / `crit-1` / `qc-pri-st-001-ev-01` |
| `qc-pri-st-001-q-010` | transfert | deux schémas de déflexion | Transfert technologie/pont; pliage, fléchissement | `obj-1` / `crit-1` / `qc-pri-st-001-ev-01` |
| `qc-pri-st-001-q-011` | transfert | deux fiches de papier chiffrées | Maîtrise M-A : type de papier, marque à 25 s, protocole sûr | `obj-1` / `crit-1` / `qc-pri-st-001-ev-01` |
| `qc-pri-st-001-q-012` | transfert | deux trajets chiffrés | Maîtrise M-B : texture de surface, distance, départ contrôlé | `obj-1` / `crit-1` / `qc-pri-st-001-ev-01` |

## Objectif d'épreuve et poids

Les 12 items ne forment pas une note totalisante : q-001 à q-008 instruisent/diagnostiquent les quatre dimensions, q-009 à q-010 testent le transfert (cour / technologie) et q-011/q-012 sont les **deux preuves autonomes obligatoires** (matière absorbante / mouvement d'un objet). Tous évaluent le même objectif et le même critère. Dimensions dans chaque contexte : observation fidèle de la fiche, distinction observation–inférence, question testable précise, facteur/trace/conditions/sécurité. En particulier, le résultat numérique d'une fiche fictive ne valide pas une explication causale.

## Conditions et administration

- **Avant :** annoncer que toutes les mesures et scènes illustrées sont des **données fictives à analyser**, non des résultats observés en classe. L'enseignant ou le lecteur peut lire mot à mot le stimulus, sans en suggérer l'interprétation. Le cours a expliqué la méthode, mais le contexte spécifique des preuves doit rester nouveau pour l'élève.
- **Pendant q-011 et q-012 :** distribuer les fiches séparément, ne proposer aucun indice de contenu ni rétroaction entre consigne et remise; autoriser seulement une clarification du vocabulaire d'accès ou une lecture fidèle neutre. Documenter toute aide reçue, sans la transformer en preuve d'autonomie.
- **Après :** appliquer la grille analytique à la trace observée (orale consignée/dictée/texte/schéma annoté); noter une citation ou un élément concret par dimension, expliquer les manques, éviter notation par simple mots-clés. Une prestation satisfaisante sur les **deux** contextes distincts, sans indices substantiels, est requise pour décider la maîtrise. En cas de discordance, une troisième tâche nouvelle est requise après remédiation.

## Difficulté et représentations

- **Initial :** reconnaître une observation et remplacer une préférence par un critère mesurable.
- **Intermédiaire :** rendre explicites une variable de comparaison et une trace, signaler une limite de la fiche.
- **Transfert :** proposer une enquête faisable sur un phénomène inédit, distinguer ce que la carte affirme de ce qu'une mesure réelle permettrait de vérifier. Ne pas confondre difficulté du vocabulaire et niveau scientifique.
- Représentations admissibles : texte accessible, description équivalente d'image, chiffres avec unités, tableau sur demande, oral transcrit, schéma annoté; ne pas ajouter de données nouvelles lors de l'adaptation.

## Variabilité et génération contrôlée

- Famille de génération issue du blueprint : `generee_sous_contraintes`. Implémentation : **corpus fermé** de 12 stimuli/consignes/corrigés/grilles. Un appel facultatif `seed s` sélectionne l'item d'indice `(s mod 12)` dans l'ordre de la banque : s=24001 → index 1 → q-002; s=24002 → index 2 → q-003. Une variation de présentation (texte, dictée, lecture neutre) est permise; une variation libre des chiffres, variables, causes, contraintes, droits et réponses **est interdite**.
- Les preuves q-011 et q-012 ne sont jamais remplacées par le tirage; elles sont obligatoires. Les différentes rédactions de questions de l'élève sont évaluées **par critères**, non au moyen d'une réponse textuelle unique. Tout scénario neuf ou modifié exige auteur identifié et revue humaine avant usage.

## Sécurité / accessibilité / données

- Situations de faible risque sur cartes fictives; pas de produits nocifs, feu, courant secteur, petits objets pour jeunes enfants, observation directe du Soleil, manipulation sur sol glissant ou charge dangereuse. L'enquête réelle est **facultative** et supervisée; la fiche suffit.
- Formats accessibles (lecture neutre, police agrandie, contraste, réponse en français oral/dictée/saisie, temps additionnel) sans abaisser les quatre dimensions. Ne noter ni l'orthographe, ni la dextérité, ni un déficit sensoriel hors compétence visée. Préserver la description exacte des chiffres et conditions.
- Traces individualisées enregistrées uniquement dans le système d'évaluation autorisé, **pas** dans le contenu canonique ou le manifeste. Aucun identifiant personnel nécessaire aux cartes.

## Contrôles et limites

Corrigés critériés avec exemples alternatifs acceptables et rétroactions par item; aucune réponse produite librement par IA n'est un contrôle fiable. Les scènes sont des **modèles fictifs**, non des mesures valides scientifiquement. Épreuves non testées avec des élèves; durée, lisibilité, biais de contexte et fidélité intercorrecteurs requièrent revue humaine. La publication, la conformité PFEQ et la certification ne sont pas revendiquées.
