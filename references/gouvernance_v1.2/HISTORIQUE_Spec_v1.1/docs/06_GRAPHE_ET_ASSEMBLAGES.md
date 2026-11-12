# 06 — Graphe typé et contrats d'assemblage

## 6.1 Relations typées — aucune arête anonyme

| Relation | Sens | Cycle autorisé ? | Validation |
|---|---|---|---|
| `requires(A,B)` | A **exige** B comme préalable maîtrisé | **Non**, DAG obligatoire | justification + preuves de dépendance pédagogique |
| `recommends_before(A,B)` | B conseillé avant A, mais non bloquant | Oui | avis pédagogique explicite |
| `reinforces(A,B)` | A réinvestit B | Oui | exemples concrets |
| `supports(A,B)` | A contribue à une compétence B / objectif référencé | Oui | mapping sourcé |
| `alternative_to(A,B)` | variantes de parcours selon contexte | Oui | conditions de choix |
| `composed_of(P,A)` | assemblage P référence la feuille A | **Non** entre assemblages | identifiant + version épinglée |

**Notation :** `requires(A,B)` = « pour faire **A**, posséder **B** ». Le sens ne doit jamais être inversé. `requires` NE DOIT PAS être attribué à partir de l'ordre des lignes du catalogue. Un lien hypothétique demeure `proposition` et n'est pas utilisé comme blocage avant validation.

## 6.2 Invariants du registre

- IDs source et cible existants, types compatibles.
- Un seul propriétaire du registre; tous les autres fichiers ne contiennent qu'un miroir dérivé.
- Aucun `requires(A,A)` ni cycle `requires`; aucun cycle `composed_of`.
- Les liens pédagogiques optionnels peuvent être réciproques et ne constituent pas un ordre scolaire.
- Chaque relation a `id`, `type`, `from`, `to`, `justification`, `statut_validation`, `provenance`, `version`.
- Les liens `supports` vers ScolQc utilisent des identifiants *réels* et une version de source.
- Toute modification de dépendance fait réévaluer les assemblages affectés.

## 6.3 Contrat d'assemblage

Un assemblage porte : `id`, `type`, `revision`, `annee/cycle` si applicable, `variante_linguistique`, `programme_edition`, `offre_artistique`, `conditions`, `members`, `ordre`, `regles_de_selection`, `couverture`, `refs_epinglees`, `statut`.

- **Discipline :** regroupe des feuilles de même discipline; n'impose pas à elle seule les années.
- **Cycle :** organise apprentissages et reprises selon attentes vérifiées pour les deux années concernées.
- **Année :** ordonne des feuilles (ou phases des feuilles) conformément aux progressions et préalables prouvés.
- **Variante :** modifie une sélection ou un contexte *sans recopier* les feuilles.
- **Remédiation/enrichissement :** sous-parcours selon diagnostic, explicitement référencés au parent.

## 6.4 Procédure de composition

1. Fixer `annee_scolaire`, `annee_primaire`, `cycle`, `variante`, `offre_locale`, `profil_curriculaire`.
2. Sélectionner les feuilles dont l'alignement est applicable **et qualifié**; bloquer les correspondances de portée incertaine.
3. Déterminer pour chacune la phase requise : introduire / attendre autonomie / réutiliser, **selon la source**.
4. Ajouter et vérifier les vrais préalables; si un préalable est hors parcours, créer une entrée de diagnostic/remédiation explicitée.
5. Trier selon `requires` et les contraintes officielles; l'ordre pédagogique local peut raffiner sans renverser une exigence.
6. Contrôler couverture par compétence et année, exclusions mutuelles, variantes, duplications et manque de preuves.
7. Épingler pour la release les révisions d'enfants exactes (références v9); produire le rapport de couverture.

Un parcours annuel **vide ou incomplet** demeure `brouillon_assemblage`, jamais « programme complet ».

## 6.5 Paramètres particuliers

- Les 6 gabarits `qc-pri-parcours-{1..6}` ne sont pas six clones de contenus : ils sélectionnent des feuilles avec `annee` + `variante` + `édition`.
- Pour les arts, la configuration définit la sélection réelle de disciplines proposées; ne pas prétendre que les quatre sont suivies partout.
- La science et l'univers social ne doivent pas être artificiellement déclarés matières obligatoires au 1er cycle au seul motif que nos connaissances transversales y contribuent.
- ILSS peut être assemblé autour de **paliers documentés** sans correspondance stricte 1..6.

Voir [MODELE_ASSEMBLAGE.md](../modeles/MODELE_ASSEMBLAGE.md).
