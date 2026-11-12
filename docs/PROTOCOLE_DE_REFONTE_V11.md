# Ekole · protocole de refonte des Kristals — v11

## Principe

**Un Kristal est un ensemble de connaissances, de situations d'apprentissage et de preuves**, pas un écran ni un cours Moodle. Son objectif, ses exigences de maîtrise, ses préalables et ses sources restent identifiables. L'expérience interactive est un contrat *attaché au Kristal*, susceptible d'être révisé.

La v10 a posé 406 concepts visuels, mais leur lien aux activités était souvent trop général. La v11 repart des dossiers pédagogiques existants et approfondit **cinq pilotes représentatifs**, pas 202 évaluations.

## Structure d'un Kristal enrichi

```text
kristals/qc-pri-ma-012/
  authoring/CONTRAT_PEDAGOGIQUE.json       ← source, inchangé
  authoring/PARCOURS.md                  ← source, inchangé
  authoring/REVISION_EKOLE_v11.md        ← motifs de conception, statut
  contenu/01_... / 02_... / ...          ← corpus pédagogique de référence
  evaluation/BANQUE_ITEMS.json          ← preuves/réponses, enseignant seulement
  evaluation/PLAN_EVALUATION.md         ← conservé
  experience/
    SCENARIO_APPRENTISSAGE.json         ← 4 moments + liens outils + limites
    RESSOURCES_VISUELLES.json           ← concepts et prompts, sans style
    ANNEXE_GUIDE_v11.md                ← approfondissement du modelage
    ANNEXE_PRATIQUE_v11.md              ← erreurs et rétroactions
    images/                             ← à compléter plus tard, pas d'image livrée
```

Les deux annexes peuvent être apposées à `contenu/03_ENSEIGNEMENT_GUIDE.md` et `contenu/04_PRATIQUE_ACCOMPAGNEE.md` par l'outil de révision avec vérification d'empreinte; **seulement sur demande explicite**.

## Cinq portes de qualité, par Kristal

1. **Fidélité de contenu** : consignes, scénarios et représentations directement justifiés par l'objectif et les modules. Toute variante inventée est indiquée comme création d'entraînement, non comme source.
2. **Cohérence cognitive** : manipuler la propriété visée, et non seulement cliquer sur des éléments visuellement agréables. Contraster les erreurs qui révèlent une incompréhension.
3. **Validation limitée et traçable** : énumérer les propriétés effectivement testées par le code. Jamais de maîtrise conclue à partir d'une activité ludique partielle.
4. **Accessibilité** : clavier, contrôles assez grands, consignes courtes et alternatives au geste/écrit/audio en fonction de l'objectif. La voie choisie ne doit pas changer arbitrairement la compétence évaluée.
5. **Revue humaine et publication** : vérifier exactitude, programme scolaire local, sécurité des activités, données personnelles, licences, prompts, variantes et expérience auprès d'enfants.

Aucun passage au statut *approuvé* n'est automatique. Les mentions « prototype » ne sont jamais des étiquettes officielles.

## Séparer les trois couches d'interface

| Couche | Peut afficher | Doit masquer |
|---|---|---|
| Élève | Consigne, matériel, prompt si image absente, entraînement et retour non noté | Banque d'items, réponses source, diagnostic enseignant |
| Enseignant | Ensemble du dossier, erreurs typiques, plan de séance, limites et sources | Rien de scolaire ne doit être rendu public sans contrôle |
| Core | Navigation institutionnelle, cours, parcours, états de revue | Ne pas publier le Core brut avec les données sensibles |

## Trois catégories de validation

- `exactitude_mathematique` : les propriétés dénombrables ou calculées se valident par des règles déterministes; la justification reste à observer.
- `interpretation_textuelle`, `enquete_scientifique` : quelques tris/ordres sont validables; l'argumentation et l'explication nécessitent un regard humain.
- `performance_observee` : aucune captation ou analyse d'émotions de l'enfant; critères descriptifs et observation humaine.

## La couche image (concept, pas style)

Une intention visuelle précise les **objets, relations, notion, rôle dans la séance, ancrage de source et contraintes d'exactitude**. Elle ne demande ni palette, ni rendu, ni mascotte, ni filtre esthétique. Un visuel manque ? Le prompt intégral apparaît à l'emplacement prévu. Un fichier `.webp`, `.png`, `.jpg` ou `.jpeg` valide est placé dans le dossier Kristal, puis compilé et affiché. Les objets exacts et mesurables sont rendus par le MiniLab déterministe, non par une image IA.

## Sortie pour les 197 autres références

`docs/CARNET_DE_REFONTE_202_v11.json` contient un dossier préparatoire pour **200 sources** et **2 sources manquantes**; seuls les cinq pilotes ont une séquence révisée. Les 195 autres n'ont qu'un **archétype candidat** fondé sur leur domaine et leur objectif source. C'est une file de travail, pas une réalisation ni une évaluation.

## Précautions de publication

Le port local Enseignant n'est pas une gestion des rôles institutionnels. Un export statique Élève est filtré et séparé. Aucun corrigé source, droit d'auteur non vérifié ou donnée personnelle d'apprenant ne doit entrer dans l'export public. Konstellation Light est un navigateur indépendant; aucun état v10 non publié n'est présenté comme vérifié. Moodle reste facultatif.
