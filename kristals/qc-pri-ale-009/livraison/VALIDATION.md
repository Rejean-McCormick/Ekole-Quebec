# Journal de validation — qc-pri-ale-009 (v1.2)

## Origine et portée

Source : `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip`, contenant le dossier maître `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Les trois textes de gouvernance requis, le graphe et les quatre fichiers authoring du Kristal ont été lus. Livraison **delta** de 14 fichiers exclusivement sous `kristals/qc-pri-ale-009/` ; aucune base centrale n'est remplacée.

## Contrôles effectivement exécutés

1. **Réussi** — Source trouvée : ZIP maître interne, gouvernance, graphe, PARCOURS, CONTRAT, ALIGNEMENT et BRIEF lus.
2. **Réussi** — Identité/titre/objectif/critère/famille/préalable/ordre identiques au contrat v1.2.
3. **Réussi** — Conservation des champs du contrat JSON v1.2 y compris champs imbriqués.
4. **Réussi** — YAML d’origine conservé à l’identique et 12 sections numérotées.
5. **Réussi** — 13 champs réglementaires de la famille d’évaluation présents.
6. **Réussi** — Banque : 10 IDs uniques séquentiels, champs communs complets et JSON sérialisable.
7. **Réussi** — Deux preuves contextualisées indépendantes et trois catégories S/C/P sur chaque preuve.
8. **Réussi** — Calculs des 8 et 10 modifications ciblées des preuves autonomes.
9. **Réussi** — 10 corrections : différences tokenisées conformes aux décomptes documentés.
10. **Réussi** — Corrigés ancrés : graphies et ponctuation de preuve attendues, point conservé dans la déclaration.
11. **Réussi** — Couverture 2 modèles, 2 contre-exemples, 2 diagnostics, G1-G3, A1-A4, 2 transferts et rappel.
12. **Réussi** — Liens internes de fichiers livrés et références au bon Kristal.
13. **Réussi** — Droits, confidentialité et adaptations : références et consignes présentes.
14. **Réussi** — Liens Markdown relatifs aux fichiers livrés résolus.

**Contrôles finaux d'empaquetage :** ZIP ouvert après écriture et testé via `ZipFile.testzip`; 14 fichiers non vides, première entrée `kristals/qc-pri-ale-009/authoring/PARCOURS.md`, aucun chemin absolu ni `../`, tous les noms du manifeste correspondants sans entrées supplémentaires, JSON parsables et 12 sections encore présentes. Ces contrôles finaux sont exécutés après génération de ce journal dans le script de construction.

**Précision sur la validation des corrigés :** contrôle mécanique des différences entre les 10 stimuli et les 10 réponses attendues, y compris les comptages 8 et 10. Les tests informatiques ne prouvent **pas** l'adéquation à tous les usages linguistiques ou toutes les variantes de l'anglais. Les textes et justifications ont été relus dans ce lot, sans protocole de validation externe.

## Limites et revue humaine encore nécessaires

- Relecture éditoriale et linguistique anglaise (notamment exemples, clarté des consignes, justifications et fréquence des mots au niveau visé).
- Essai pédagogique avec élèves d'âges/années variés, durée, charge cognitive et capacité à donner une justification, sans attribuer d'année-cible canonique.
- Étude d'accessibilité avec lecteurs d'écran, modalités de dictée qui ne corrigent pas automatiquement la casse/ponctuation, et besoins individuels.
- Vérification des droits et autorisations si des **ressources externes** devaient être reproduites ultérieurement; aucune reprise textuelle externe dans le présent delta.
- Validation humaine des rubriques, seuils internes (≥80 % et trois catégories), compréhension des deux contextes et absence de biais. Pas de test avec un LMS, ni revue indépendante, ni qualification/sommative effectués.

## Propositions à transmettre à la gouvernance (aucune modification centrale)

1. Proposer une règle de représentation JSON commune des `corrections_ciblees` avec catégorie S/C/P, pointage et preuves, et une décision LMS distincte de la somme de points.
2. Proposer une convention explicite de dictée fidèle et d'aides d'accès excluant l'autocorrection quand orthographe et ponctuation sont l'objet de l'évaluation.
3. Proposer un mécanisme de versionnement des scénarios contrôlés et d'essais alternatifs pour réévaluation sans mémorisation des corrigés.

**Statut final :** contrôle technique local réussi; revue humaine requise. Ni publié, ni homologué, ni certifié.
