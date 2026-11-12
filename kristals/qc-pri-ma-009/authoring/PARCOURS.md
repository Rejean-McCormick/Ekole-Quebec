---
format: qc.learning-path/1.0
id: qc-pri-ma-009
titre: Sens et stratégies de la division
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Représenter le partage et le groupement pour résoudre des divisions.
objectifs_secondaires: []
criteres_reussite:
- Effectuer un partage justifié et vérifier quotient et reste.
prealables_declares:
- qc-pri-ma-008
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-009-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---
# Microparcours — `qc-pri-ma-009`

**Discipline (appellation québécoise) :** Mathématique  
**Titre :** Sens et stratégies de la division  
**Gouvernance pédagogique :** norme interne v1.2  
**Qualification :** contenu rédigé et arithmétique contrôlée; revue humaine non réalisée, aucune homologation PFEQ.

## 1. Intention et frontières

- `obj-1` — **Objectif immuable :** Représenter le partage et le groupement pour résoudre des divisions.
- `crit-1` — **Preuve immuable :** Effectuer un partage justifié et vérifier quotient et reste.
- **Notions :** quotient, reste, partage, groupement. Les problèmes portent sur des quantités entières non négatives et un diviseur entier positif. Aucune division par zéro, ni quotient décimal requis.
- Distinguer *répartir entre d destinataires* et *former des groupes de d objets*. Une quantité restante est expliquée avec son unité; on ne promet pas une distribution égale en donnant un objet supplémentaire seulement à quelques personnes.
- Conserver exactement les liens du registre; pas d'année prescrite ni de conformité ministérielle supposée.

## 2. Notions et représentations

**Partage (nombre de parts connu) :** 23 cartes pour 5 équipes : 4 par équipe, 3 cartes restantes. Schéma de 5 ensembles de 4 points et 3 isolés. Écriture `23 = 5 × 4 + 3` et `0 ≤ 3 < 5`.

**Groupement (taille des groupes connue) :** 23 cartes, pochettes de 5 : 4 pochettes complètes, 3 cartes restantes. Même écriture, mais les unités du quotient changent (cartes par équipe versus pochettes). Le quotient entier q donne des parts égales ou des groupes complets; le reste r est la quantité non répartie dans ce cadre.

Le trio invariant à expliquer et vérifier est `N = d × q + r`, `d ≥ 1`, `0 ≤ r < d`. Un reste au moins égal au diviseur permettrait une part ou un groupe de plus : la division n'est pas terminée. Voir `contenu/01_NOTIONS_ET_EXEMPLES.md` pour deux modèles détaillés et deux erreurs contre-modélisées.

## 3. Préparation / diagnostic

**Préalable strict `qc-pri-ma-008` :** sens et stratégies de la multiplication. Un diagnostic d'acquis équivalent peut satisfaire le préalable sans forcer le suivi du module. Aucun ordre conseillé ni transfert lié au graphe.

`diag-1` : 4 × 6 avec arrangement de points, puis expliquer 24 = 4 × 6. `diag-2` : répartir 17 cubes dans 4 assiettes, estimer le reste puis vérifier. Corrigés, observations et décisions dans `contenu/02_DIAGNOSTIC.md`. Une erreur de multiplication mène à une remise à niveau ciblée; une multiplication correcte mais division difficile mène à un modelage local.

## 4. Enseignement guidé

`teach-1` : matériel → groupes dessinés → égalité. Dire chaque décision : ce que N compte, ce que d compte, ce que q compte, ce que r compte. Exemple de partage : 29 jetons entre 6 personnes → 4 jetons par personne et 5 restants, car `29 = 6 × 4 + 5` et `5 < 6`. Exemple de groupement : 34 feuillets, lots de 8 → 4 lots et 2 feuillets, car `34 = 8 × 4 + 2` et `2 < 8`.

Avant d'effacer le schéma, demander : « Que représente le quotient dans **cette** situation? Peut-on former un groupe complet avec le reste? » Matériel et formulations disponibles dans `contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

`guided-1` : trois problèmes à indices dégressifs dans `contenu/04_PRATIQUE_ACCOMPAGNEE.md` : (1) 19 objets entre 4 destinataires, tableau à compléter; (2) 38 objets en groupes de 6, début de schéma donné; (3) 47 objets en équipes de 5, sans schéma fourni, avec une question de contrôle seulement après tentative. Faire formuler le quotient, le reste, les unités et le contrôle multiplicatif; retirer l'indice après réussite. Ne pas confondre aide au calcul et preuve autonome.

## 6. Pratique autonome

`independent-1` : quatre tâches différentes (partage exact, groupement avec reste, interprétation d'une solution, comparaison des deux sens de division) dans `contenu/05_PRATIQUE_AUTONOME.md`. Les réponses sont fixées, justifiées et utilisables en autoévaluation après production.

Les deux preuves de maîtrise distinctes sont les items `qc-pri-ma-009-q-011` (74 fiches entre 6 équipes : **partage**) et `qc-pri-ma-009-q-012` (91 gourdes en caisses de 8 : **groupement**). Faire passer sans indices procéduraux sur deux occasions, à des moments ou contextes distincts.

## 7. Feedback et erreurs typiques

- `r ≥ d` : « Peux-tu faire un groupe de plus? »; reprendre avec matériel et vérifier `0 ≤ r < d`.
- `d × q = N` imposé alors que le problème laisse des objets : ajouter le reste à l'égalité, puis vérifier la quantité d'origine.
- Quotient et reste inversés : nommer les unités et demander combien reçoit *chaque* équipe ou combien de groupes complets existent.
- Division correcte mais contexte mal interprété : réécrire une phrase entière avec l'unité (pas seulement « 4 reste 3 »).
- Un élève donne 5 objets à certaines équipes et 4 à d'autres : rappeler que « partage égal » exige la même quantité dans chaque part et que les objets supplémentaires sont mis de côté.

Après retour, demander **un nouveau cas**; détails et exercices correctifs dans `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 8. Évaluation formative et preuves

- `famille: qc-pri-ma-009-ev-01`; `objectif_ref: obj-1`; `critere_ref: crit-1`.
- Banques fixes et paramétriques déterministes, exactement décrites dans `evaluation/BANQUE_ITEMS.json`; aucune génération libre par IA. Toute version numérique autorisée suit les bornes, la formule et les tests documentés.
- Critères observables : représentation, calcul exact, contrôle `N=d×q+r` et `r<d`, interprétation de l'unité. Aucun résultat seul ne suffit.
- La maîtrise exige deux manifestations autonomes dans des situations distinctes; la grille `evaluation/GRILLE_MAITRISE.md` précise la décision. Tous les items demeurent `a_revoir` en attente de revue humaine et d'essai.

## 9. Remédiation / enrichissement

Revenir au sens de la multiplication `d × q`, afficher une distribution concrète, puis passer au dessin et à l'écriture. Si le reste dépasse la taille d'un groupe, redistribuer et recalculer; si le vocabulaire est fragile, annoter les unités. En enrichissement, comparer partage et groupement sur un même nombre en changeant le sens de d, et tester la limite `r = d−1`, ou `r = 0`. Transferts **nouveaux contextes** : logistique de bibliothèque et matériel de terrain (voir `06_REMEDIATION_ET_TRANSFERT.md`).

**Rappel différé :** à J+2, reprendre sans modèle `26 ÷ 4` dans une situation de partage; à J+7, résoudre `45 ÷ 7` en groupement et expliquer pourquoi le reste est valide. Réponses : `6 r 2`, car `26=4×6+2`; `6 r 3`, car `45=7×6+3`. Les rappels servent au suivi, pas à remplacer deux preuves autonomes.

## 10. Accessibilité

Proposer pions, points, boîtes tracées, tableau à colonnes, énoncé lu à voix haute, texte agrandi, écrit simple ou dictée vocale des explications. Autoriser une représentation tactile ou verbale équivalente; évaluer les mêmes liens quantitatifs. Les objets sont fictifs, non dangereux et ne supposent aucune réalité familiale. Éviter que fluidité de lecture, motricité fine ou lenteur d'écriture ne masquent la compréhension du partage et du groupement. Garder les nombres visibles et permettre une pause sans fournir le calcul lors des preuves autonomes.

## 11. Critères de sortie

`crit-1` : Effectuer un partage justifié et vérifier quotient et reste. Pour **chacune des deux preuves** : représentation compatible avec le sens de la tâche, `q` et `r` corrects, vérification `N=d×q+r` et `0≤r<d`, phrase qui restitue les unités. L'élève agit sans indice de procédure, mais peut choisir les adaptations non guidantes. Documenter les deux productions et dates; une seule réussite ou un score global n'autorise pas la maîtrise. Sur échec ciblé, remédier puis proposer un nouvel item de même type avec valeurs distinctes.

## 12. Références pédagogiques et limites

Sources internes effectivement consultées : gouvernance v1.2 (`CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md`), registre de dépendances, frame `PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md` et `BRIEF_REDACTION.md`. Les situations, exemples, rubriques et corrigés de cette livraison sont originaux; l'arithmétique est vérifiable par identité entière. Aucun contenu ministériel ni ouvrage protégé reproduit. Les méthodes pédagogiques sont une adaptation de la gouvernance interne, pas une évaluation externe des recherches citées par le cadre. Voir `sources/REFERENCES_CONTENU.md`.

**Limites :** pas d'approbation du PFEQ, pas d'essai auprès d'élèves, pas de revue humaine des biais ou de l'ergonomie LMS, pas de qualification Framework ni de publication canonique. Toute évolution structurelle sera proposée hors de ce ZIP.
