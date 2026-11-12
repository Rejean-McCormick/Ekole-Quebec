---
format: qc.learning-path/1.0
id: qc-pri-st-010
titre: Électricité et magnétisme
discipline_code: ST
statut: redaction_complete_revue_requise
revision_contenu: 1.0.0
langue_contenu: fr-CA
resultat_principal: Construire un circuit très simple et distinguer circuit fermé
  et ouvert.
objectifs_secondaires: []
criteres_reussite:
- Dessiner puis vérifier le fonctionnement d’un montage à basse tension.
prealables_declares:
- qc-pri-st-008
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-st-010-ev-01
provenance_statut: sources_repertoriees_et_verifiees_partiellement
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-st-010`

**Discipline :** Science et technologie. **Titre immuable :** Électricité et magnétisme. **Autorité :** contrat pédagogique v1.2 interne; la nomenclature québécoise ne constitue pas une homologation. **Statut :** contenu rédigé, revue humaine et essai pratique requis.

## 1. Intention et frontières

- `obj-1` (IMMUTABLE) : **Construire un circuit très simple et distinguer circuit fermé et ouvert.**
- `crit-1` (IMMUTABLE) : **Dessiner puis vérifier le fonctionnement d’un montage à basse tension.**
- Famille `qc-pri-st-010-ev-01`; concepts : **composant, conducteur, circuit, sécurité**.
- On étudie un seul récepteur (ampoule miniature incandescente adaptée à 3 V), une source de **deux piles AA dans un support fermé (3 V nominal)** et un interrupteur ou raccord prévu pour cet usage. L'électricité domestique, les circuits à haute énergie, le calcul d'intensité et la mesure de tension ne font PAS partie du parcours.
- « Magnétisme » est une fenêtre culturelle du titre : un aimant n'est pas une pile et n'est pas nécessaire au circuit démontré. Ne pas transformer cette fenêtre en objectif ou preuve notée.

## 2. Notions et représentations

**Composant :** élément avec une fonction dans le montage : support de piles/source, ampoule/récepteur, interrupteur/commande, fil/liaison. **Conducteur :** matériau par lequel le courant peut circuler dans les conditions du montage; âme métallique d'un fil isolé. La gaine plastique est isolante. **Circuit :** trajet d'ensemble partant d'une borne de la source, passant par l'ampoule, puis revenant à l'autre borne. **Circuit fermé :** chemin continu qui permet le courant; **ouvert :** coupure empêchant le courant. **Sécurité :** ensemble de décisions préventives contre court-circuit, chaleur, fuite de pile, ingestion, risque électrique.

Représentations concordantes : objets réels (support 3 V, ampoule 3 V, interrupteur), carte schématique simplifiée de boucle, tableau prédiction/constat/inférence, texte descriptif. Un schéma montre les connexions, pas l'emplacement géométrique exact. La lumière de l'ampoule seule n'est pas un test suffisant de l'ouverture : une pile usée ou une ampoule défectueuse peut produire « éteint » même si les connexions forment une boucle.

**Exemple A :** borne positive → interrupteur fermé → ampoule → borne négative; lampe allumée avec composants fonctionnels. **Exemple B :** même circuit, interrupteur ouvert; lampe éteinte. **Contre-exemples :** fil seulement entre les bornes d'un support de piles = court-circuit à INTERDIRE; lampe éteinte donc « forcément ouvert » = conclusion non justifiée.

## 3. Préparation / diagnostic

- `requires(qc-pri-st-010,qc-pri-st-008)` est le seul préalable strict selon le registre; un diagnostic des acquis équivalents permet le passage, sans imposer une visite formelle de l'autre Kristal.
- `diag-1` : trier trois phrases entre *observation*, *prédiction* et *explication*. Corrigé et décision : `contenu/02_DIAGNOSTIC.md`.
- `diag-2` : repérer sur un dessin un trajet continu et un trajet interrompu et signaler une liaison directe dangereuse entre bornes; aucun branchement réel au diagnostic. Toute confusion sécurité déclenche une démonstration encadrée, jamais une manipulation autonome.
- Les références `qc-pri-st-008` sont des liens, non une autorisation d'éditer son contenu.

## 4. Enseignement guidé

`teach-1` : montrer un montage **hors tension** (support de piles installé exclusivement par l'adulte), tracer la boucle en nommant les composants; fermer l'interrupteur seulement après inspection par l'adulte. Dire : « Je prévois que l'ampoule s'allume si le trajet est complet et les composants en état »; observer; ouvrir; distinguer la cause supposée de l'observation. Deux exemples résolus et deux contre-exemples dans `contenu/01_NOTIONS_ET_EXEMPLES.md`; procédure dans `contenu/03_ENSEIGNEMENT_GUIDE.md`.

**Contrôle :** « Quelle partie conduit ? Pourquoi faut-il une boucle et non un seul fil ? Quelle observation a-t-on faite ? » Réponse : âme métallique, retour à l'autre borne, constat de lumière/absence de lumière; expliquer l'état du circuit en contrôlant le matériel.

## 5. Pratique accompagnée

`guided-1` : (G1) tracer un chemin sur un schéma fléché avec indice complet; (G2) prévoir la lampe avec coupure indiquée, indice réduit; (G3) résoudre un défaut en justifiant, sans indice. Tous comportent consigne, résultat et rétroaction dans `contenu/04_PRATIQUE_ACCOMPAGNEE.md`. Matériel réel seulement sous supervision adulte, jamais de liaison directe des deux bornes.

## 6. Pratique autonome

`independent-1` : quatre exercices nouveaux (lecture de schéma, choix du conducteur, diagnostic contrôlé, plan de montage) dans `contenu/05_PRATIQUE_AUTONOME.md`, avec corrigés distincts. Les deux preuves de maîtrise **E1 « coin lecture »** et **E2 « balise de maquette d'atelier »** dans `evaluation/BANQUE_ITEMS.json` q-009 et q-010; chacune requiert un schéma légendé, une prédiction, l'observation des deux états, la justification du trajet et un protocole sûr. Aucune aide de contenu pendant la preuve, adaptation de modalité autorisée.

## 7. Feedback et erreurs typiques

- `error-1` : « une ampoule éteinte prouve circuit ouvert » → demander si la pile, l'ampoule et le raccord ont été contrôlés.
- « un fil sur une seule borne suffit » → suivre au doigt la boucle jusqu'à la seconde borne.
- « les deux bornes peuvent être reliées directement » → **interrompre avant toute exécution**, réexpliquer le court-circuit et passer à la maquette papier.
- « un aimant peut remplacer une pile » → distinguer action magnétique et source électrique, sans autre phénomène noté.
- Refaire un essai différent après feedback, enregistrer la correction et la preuve d'autonomie.

## 8. Évaluation formative et preuves

- `obj-1` ↔ `crit-1` ↔ `qc-pri-st-010-ev-01` pour tous les items. Modes fixes et scénarios **à catalogue fermé** avec corrigé par variante; aucun correcteur libre génératif.
- 10 items q-001 à q-010, dont deux manifestations indépendantes (q-009 et q-010); énoncés et rubriques dans `evaluation/BANQUE_ITEMS.json`, couverture dans `evaluation/PLAN_EVALUATION.md`.
- Maîtrise = présence des critères essentiels dans **deux contextes** différents, sans indication technique de fond, avec conditions de sécurité satisfaites; jamais simple seuil de note. Grille : `evaluation/GRILLE_MAITRISE.md`.

## 9. Remédiation / enrichissement

- Liaison manquante : reconstituer physiquement une boucle fictive avec cartes « source, fil, ampoule, fil » puis la dessiner.
- Confusion conducteur/isolant : comparer « métal au centre » et « gaine plastique » sur un fil non branché.
- Prédiction prise pour un fait : colonnes « avant : je prévois / pendant : j'observe / après : j'explique ».
- Erreur de sécurité : activité de manipulation suspendue; enseignant·e modélise uniquement sur planche non alimentée.
- Enrichissement (hors critère) : discussion supervisée d'un aimant massif encapsulé, sans petits aimants libres ni objets avalables; distinguer magnétisme et électricité.

## 10. Accessibilité

Gros symboles textuels, connexions représentées par traits contrastés et mots, lecture orale des consignes, schéma tactile hors tension, montage préassemblé ou simulation accessible quand besoin. L'élève peut dicter/indiquer le schéma à un scribe neutre, pointer un chemin continu et activer un gros interrupteur adapté; les décisions et explications doivent venir de l'élève. Pour impossibilité ou risque physique, version simulateur **avec observations simulées explicitement signalées** et vérification sous supervision de l'adulte; distinguer la preuve simulée de la vérification physique et demander une équivalence humaine selon `crit-1`.

**Sécurité impérative :** exclusivement support de deux AA alcalines installé par l'adulte (aucune pile bouton), ampoule incandescente 3 V compatible, fils isolés/connexions protégées et interrupteur de kit approuvé par l'enseignant. Pas de prise murale, secteur, adaptateur USB ou bloc d'alimentation improvisé, piles lithium, recharge, démontage, chauffage, liquide ou court-circuit. Débrancher dès anomalie; adulte responsable du matériel et de la supervision.

## 11. Critères de sortie

1. Deux productions q-009 et q-010 distinctes : schéma légendé et boucle correcte.
2. Pour chacune : prédire **avant** le test, montrer circuit fermé puis ouvert, consigner ce qui est observé, interpréter sans affirmer plus que les données.
3. Les deux preuves démontrent une méthode sûre, autonome sur le plan intellectuel, y compris signalement de tout problème au responsable.
4. Si un critère manque dans l'une des preuves, remédier au point précis puis renouveler dans un **nouveau contexte**, plutôt que sommer des points.

## 12. Références pédagogiques et limites

Références vérifiées et droits : `sources/REFERENCES_CONTENU.md`; références du workspace dans `governance/Norme_Pedagogique_Autonome_v1.2/`; conversion québécoise dans `authoring/ALIGNEMENT.md` (non modifié). Rappel différé : après 2–3 jours et après une semaine, redessiner de mémoire une boucle fermée et une coupure, puis expliquer ce qui est observé si une lampe reste éteinte; corriger avec démonstration contrôlée. **Limites :** revue pédagogique/scientifique, test physique et vérification des besoins individuels demeurent requis; ni certification, ni conformité officielle au PFEQ alléguée.
