# Plan d'évaluation — `qc-pri-ilss-007` | v1.2

**Objectif `obj-1` :** Écrire un message fonctionnel compréhensible pour un destinataire. **Critère `crit-1` :** Rédiger une demande ou une réponse scolaire utilisable. **Famille immuable :** `qc-pri-ilss-007-ev-01`. **Type v1.2 :** `observation_ou_production`. Aucun item ne constitue une évaluation certifiée : `validation_status=a_revoir`.

## Conception du dispositif

Écrire un message réellement utilisable au sein d'une école fictive : l'évaluateur remet une consigne avec faits et destinataire, puis observe **la production écrite**, la pertinence des informations, la formule de contact, la lisibilité et les décisions d'écriture de l'élève. Les fautes de surface qui n'empêchent pas la compréhension peuvent donner lieu à correction formative sans invalider une preuve déjà claire; une quantité erronée ou une intention absente en revanche peut rendre le message inutilisable. Évaluer la capacité de composer un écrit, **pas** les langues familiales, la situation personnelle, le niveau scolaire supposé ou l'aisance à prendre la parole.

Toutes les lignes ci-dessous sont **reliées à `obj-1`, `crit-1`, `qc-pri-ilss-007-ev-01`**; ces trois références figurent aussi dans chacun des dix objets JSON. Les scénarios, décisions, quantités et dates sont fixes et contrôlables par comparaison au stimulus. Le mode `fixe` (seed et paramètres nuls) est retenu délibérément : aucune variation algorithmique n'est nécessaire pour cette compétence.

## Matrice des dix items

| Item complet (`qc-pri-ilss-007-…`) | Difficulté | Représentation / contexte | Critères prioritaires | Finalité |
|---|---|---|---|---|
| `qc-pri-ilss-007-q-001` | initial | Demande écrite : crayons verts | intention + objet + quantité + date | formatif |
| `qc-pri-ilss-007-q-002` | initial | Réponse écrite : lecture collective | oui + activité + heure/local | formatif |
| `qc-pri-ilss-007-q-003` | initial | Révision écrite d'un brouillon vague | précisions utiles, pas seulement formule | formatif |
| `qc-pri-ilss-007-q-004` | intermédiaire | Question sur l'heure inconnue d'un atelier | ne pas inventer de fait; identifier la question | formatif |
| `qc-pri-ilss-007-q-005` | intermédiaire | Confirmation de réception d'enveloppes | distinguer réception et demande | formatif |
| `qc-pri-ilss-007-q-006` | intermédiaire | Réponse négative à invitation | refus factuel, sans justification privée | formatif |
| `qc-pri-ilss-007-q-007` | intermédiaire | Liste de renseignements → message | organisation, exactitude, lisibilité | formatif |
| `qc-pri-ilss-007-q-008` | transfert | Demande de lieu inconnu | question précise, absence de lieu inventé | préparation du transfert |
| `qc-pri-ilss-007-q-009` | transfert | **Épreuve A** : demande de réservation d'atlas | les cinq dimensions M1–M5, intention et faits exacts | maîtrise A |
| `qc-pri-ilss-007-q-010` | transfert | **Épreuve B** : réponse à madame Roy | les cinq dimensions M1–M5, deux engagements | maîtrise B |

**Couverture :** une demande concrète et une réponse concrète constituent deux manifestations réelles et différentes du critère « demande **ou** réponse »; pour soutenir une maîtrise transférable, les deux sont demandées **séparément**. Les items 001–008 entraînent ou diagnostiquent des composantes sans pouvoir remplacer les preuves A/B. Les cinq dimensions de la grille sont cotées pour chaque épreuve : M1 intention, M2 informations, M3 destinataire/formule, M4 lisibilité, M5 autonomie de production.

## Passation des épreuves de maîtrise

1. Présenter une fiche de tâche **fixe**, avec faits, destinataire et rôle fictif; vérifier la compréhension des mots par une lecture accessible sans écrire la réponse. Aucune formule modèle ou texte complet affiché au moment des épreuves; les faits du scénario restent visibles comme tout document de correspondance réel.
2. L'élève **compose et relit** un écrit en utilisant une modalité préalablement retenue (papier, clavier, outil adapté, reconnaissance vocale révisée, scribe strictement mécanique). La relecture et les décisions de contenus restent sous son contrôle. L'évaluateur n'offre ni mots d'intention ni rappel du détail oublié durant l'épreuve.
3. Évaluer l'écrit final et consigner **l'aide donnée**, les informations exactes, les différences significatives, et le motif d'une éventuelle hésitation. Le fait de disposer du stimulus n'est pas un indice : la lecture de la situation constitue une condition de base.
4. Faire l'épreuve B à un autre moment ou à la suite d'un intervalle suffisant pour éviter de copier le texte A. Elle demande une **confirmation** auprès d'une personne différente, non une seconde demande de matériel.
5. Appliquer `GRILLE_MAITRISE.md` à chaque preuve séparément. Les scores partiels ne sont jamais moyennés pour masquer un message incompréhensible ou des choix dictés.

## Variations et limites

**Variables figées par item :** objet/activité, quantité, date, heure, local, destinataire, décision attendue. **Variations non directives admises :** support papier ou numérique, taille des caractères, temps de traitement, vocabulaire d'accès ne contenant pas la phrase à écrire, lecture de consigne, clavier adapté ou dictée vocale **avec contrôle de l'élève**. **Interdits :** générateur de messages par IA en lieu et place de l'élève, script copié, aide humaine qui choisit la réponse, modification des faits, dépôt de données personnelles et envoi réel du texte.

Les technologies d'écriture assistive permettent d'ôter un obstacle moteur; elles n'autorisent pas à prêter une intention ou une sélection de détails non produite par l'élève. Si une modalité ne permet pas de recueillir la preuve d'écriture, documenter la situation et demander une décision humaine sur l'équivalence plutôt que d'accorder une maîtrise supposée.

## Sécurité sociale, linguistique et accessibilité

Tous les rôles, noms, locaux et activités sont fictifs; pas de révélation d'origine, de religion, de situation familiale ou de réel motif d'absence. Autoriser le français courant local et de simples formules respectueuses; ne pas évaluer l'accent, les compétences dans une autre langue ou une conformité orthographique totale. Documents à caractères lisibles, consignes courtes, supports de lecture et correction pédagogique ciblée. Aucun enregistrement vocal, compte de messagerie ni diffusion à des tiers. La clarté d'un écrit reste le critère, pas son apparence typographique.

**Statut :** document de conception vérifié sur le plan technique, pas d'étalonnage interévaluateurs ni d'observation réelle. Revue par une personne spécialisée en ILSS et accessibilité indispensable.
