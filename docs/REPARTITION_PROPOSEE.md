# Affectation provisoire des 202 cours — note d'autorité

**Statut : proposition de navigation, non validation pédagogique ni conformité ministérielle.**

Les 202 Kristals existants n'affectent pas les cours aux années scolaires. Les 134 liens `requires` du graphe pédagogique gouvernent les préalables, mais **ne définissent pas le niveau d'étude**. L'overlay applique une approximation explicite pour rendre les pages année, étape et cycle explorables. Le personnel enseignant doit vérifier et ajuster ces hypothèses avant usage scolaire.

## Règles effectives (reproductibles)

1. Lire `catalogue/202_kristals.json` et `catalogue/graphe_pedagogique.json` (ou index public équivalent).
2. Utiliser le rang interne des ID dans chaque discipline comme **hypothèse de progression**, jamais une vague de production.
3. Appliquer des ancrages éditoriaux explicites pour certaines notions de mathématique et de français, sans revendiquer un niveau prescrit.
4. Vérifier le graphe `requires` par tri topologique : un préalable strict ne peut être proposé à une date après l'apprentissage qui l'exige.
5. Répartir les propositions de chaque année en quatre périodes (deux sous « Automne », deux sous « Hiver »), classées par profondeur dans les préalables puis par identifiant. **Ce choix est un regroupement de navigation**, pas un calendrier ou une échéance pédagogique obligatoire.
6. Conserver le statut `proposition_non_validee`, les preuves et la méthode pour chaque ID.

## Résolution des conflits

`site/data/parcours-affectations.json` et `site/data/niveaux-manuel.json` sont **autorités de saisie locale**. Le patch ne les écrase pas, même si leurs entrées sont vides ou n'ont pas les mêmes niveaux que nos suggestions. Un cours déjà attribué manuellement n'est pas repositionné par le générateur.

**Important** : une proposition de l'overlay n'est pas une décision de classe, une programmation annuelle validée, un lien de prérequis Moodle, un résultat d'évaluation ni une conformité PFEQ. Ces propositions sont affichées avec un avertissement. Toute promotion au statut validé exige une décision tracée, avec personne responsable et source.

## Contrôles d'acceptation

- Le catalogue couvre les 202 IDs exactement.
- Les 24 ensembles année-étape existent.
- Aucune affectation ne fait référence à un cours inconnu.
- Les préalables stricts sont antérieurs ou simultanés à leurs descendants dans les hypothèses.
- Toute proposition conserve une source et un statut « à valider ».
- Aucune table manuelle ni aucune fiche source du Kristal n'est modifiée.
