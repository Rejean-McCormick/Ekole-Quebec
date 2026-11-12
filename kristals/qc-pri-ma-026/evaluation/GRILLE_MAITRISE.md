# Grille critériée de maîtrise — `qc-pri-ma-026`

**Objectif observable `obj-1` :** Lire des horaires et déterminer des durées entre deux événements.  
**Preuve attendue `crit-1` :** Calculer une durée et vérifier le sens du résultat dans un horaire.  
**Famille :** `qc-pri-ma-026-ev-01` · Évaluation raisonnée, non QCM; les points peuvent guider la rétroaction mais **ne sont pas** une décision par note unique.

## Quatre dimensions observables (0 à 3)

| Dimension | 0 — non observé | 1 — émergent | 2 — satisfaisant | 3 — solide et transférable |
|---|---|---|---|---|
| **L. Lecture de l’horaire** | Instants non identifiés | Confond début/fin ou oublie une date essentielle | Début, fin et dates correctement repérés, ordre chronologique reconnu | Même exactitude avec plusieurs événements, justifie le passage de date sans hésitation |
| **C. Calcul et unités** | Aucun calcul exploitable | Résultat faux / minutes en base 100 / unité absente | Durée exacte, avec unité, écriture heures/minutes exacte lorsque demandée | Durée exacte par deux représentations cohérentes ou démontre aussi la recomposition |
| **V. Vérification et plausibilité** | Aucune vérification | Vérification invalide ou incohérence non détectée | Recompose `début + durée = fin` et vérifie correctement une contrainte explicite (marge, fermeture, chevauchement) | Détecte et explique aussi une affirmation fausse, ou vérifie le résultat par méthode alternative |
| **A. Autonomie et démarche observable** | Aucune démarche | Réponse obtenue après découpage fourni / correction suggestive | Solution personnelle lisible (écrit, oral, frise), sans indice de méthode ni confirmation | Démarche expliquée et adaptée spontanément au second contexte |

**Mesure sans biais :** lecture orale de l'énoncé, grand format, support tactile ou calculatrice de base accessibles sont des **aménagements** et non des aides méthodologiques; ils ne réduisent pas le niveau A. Donner la frise déjà segmentée, indiquer quelle opération effectuer ou confirmer une étape pendant l'essai **invalide l'autonomie de la preuve**; documenter et reprendre ultérieurement.

## Deux manifestations à conserver séparément

**Preuve A :** `qc-pri-ma-026-q-011`, **bibliothèque** (même date). Résultats attendus : **100 min = 1 h 40**, fin à **12 h 05**, réservation à **12 h 15**, **10 min de marge**. Vérifier le calcul et la conclusion de disponibilité, pas seulement le nombre 100.

**Preuve B :** `qc-pri-ma-026-q-012`, **station d'observation fictive** (date changeant à minuit). Corrigé de l'instance courante dans `BANQUE_ITEMS.json` : durée en minutes, nouvelle date correcte, addition de contrôle et marge positive jusqu'à la fermeture. Vérifier que la réponse suit bien la **graine livrée**; ne pas corriger une variation avec un ancien résultat.

L’évaluateur consigne pour **chaque** preuve : date de passation, contexte, représentation utilisée, réponse exacte, justification, contrôle de la contrainte, adaptation d'accès, indices éventuellement donnés et niveaux L/C/V/A. Il ne stocke pas d'observations individuelles dans ce package de contenu.

## Décision explicite

- **Maîtrise observée** seulement si **A et B** sont réalisées en situations distinctes **sans indice méthodologique**, avec `L ≥ 2`, `C ≥ 2`, `V ≥ 2`, `A ≥ 2` **dans chacune**, **durée et marge exactes**, et justification correcte du changement de date dans B. Une note moyenne élevée ou un succès à un seul item ne suffit jamais.
- **Preuve à compléter** si la durée est juste mais l'unité, la cohérence de l'horaire ou la justification de la date manque : donner un feedback ciblé puis recueillir une nouvelle preuve autonome; aucune validation par simple copie du corrigé.
- **Remédiation nécessaire** si lecture ou calcul faux : `R1` pour heures/minutes, `R2` pour base 60, `R3` pour minuit/calendrier, `R4` pour plausibilité (`contenu/06_REMEDIATION_ET_TRANSFERT.md`). Après entraînement, réévaluer dans deux contextes avec valeurs nouvelles recalculées et revues.
- **Données insuffisantes** si une preuve manque, si des indices de procédure ont été fournis, ou si le contexte n'est pas distinct : aucune décision de maîtrise.

## Exemple de rétroaction factuelle

- « Tu as trouvé 100 min, mais tu n'as pas vérifié si la bibliothèque est libre à 12 h 15. Place l'heure de fin et la prochaine réservation sur une frise, puis refais un autre horaire. »
- « Tu as traité 00 h 20 comme une heure antérieure à 23 h 40 sans regarder la date. Inscris les deux dates et repère minuit avant de recalculer. »

**Limites :** grille interne créée pour ce Kristal, pas étalonnée empiriquement; revue humaine et essais de passation requis avant qualification. Aucun score de croyance, de vitesse ou de vitesse de frappe.
