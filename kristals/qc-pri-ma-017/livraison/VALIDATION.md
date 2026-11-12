# Rapport de validation — qc-pri-ma-017 | v1.2

**Statut :** `a_revoir` / contrôles techniques et arithmétiques exécutés; **revue pédagogique humaine encore requise**. Il s'agit d'un delta pour un workspace existant, **pas** d'un cours publié, d'une validation PFEQ ou d'un examen certifié.

## Source et modifications

- Source lue : archive `Spec_Kristals_Parcours_Primaire_Qc_v1.1(1).zip`, sous-dossier exact `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`; huit documents lus : trois normes de gouvernance, graphe, PARCOURS initial, contrat initial, ALIGNEMENT, BRIEF_REDACTION.
- **Remplacement intégral** de `authoring/PARCOURS.md` avec en-tête YAML d'origine préservé et 12 sections développées.
- **Remplacement intégral** de `authoring/CONTRAT_PEDAGOGIQUE.json` avec ses champs/valeurs v1.2 conservés sauf statuts rédactionnels avancés; champs de famille exigés ajoutés sans supprimer les champs existants.
- **12 ajouts** : six documents de contenu, trois documents d'évaluation, une provenance, un manifeste, ce rapport.
- Aucun changement à `kristal.workspace.json`, `AGENTS.md`, `ALIGNEMENT.md`, `registry/`, `governance/`, `docs/`, `canon/`, `state/`, `runtime/` ni à un autre Kristal.

## Contrôles réellement exécutés

1. **YAML** : front matter identique à l'original (comparaison textuelle), `id`, titre, résultat principal, deux préalables et famille identiques; séquence des **12 sections** (1 à 12) vérifiée.
2. **Contrat JSON** : décodé; vérification récursive de la préservation des clés et valeurs d'origine (exceptions documentées : les seuls champs de statut rédactionnel); `obj-1`, `crit-1`, famille et tous les champs minimums de famille vérifiés.
3. **Graphe** : les deux arêtes sortantes `requires` lues dans le registre pointent vers `qc-pri-ma-013` et `qc-pri-ma-015`; aucun autre lien sortant inventé, aucun lien conseillé.
4. **Couverture** : 3 tâches diagnostiques (D1–D3), 3 guidées avec indices décroissants (G1–G3), 4 autonomes (A1–A4), 2 transferts T1–T2; exemples résolus A–C et contre-exemples accessibles.
5. **Banque** : 10 items numérotés Q001–Q010 uniques, tous reliés à `obj-1`, `crit-1`, `qc-pri-ma-017-ev-01` avec consigne, stimulus, réponse, grille, feedback, statut `a_revoir`. Trois items fixes et sept paramétriques.
6. **Vérification paramétrique exhaustive** : 28 couples `(p,N)` provenant des **7 corpus fermés de 4 couples**; chaque résultat évalué par fraction exacte, puis contrôlé par égalité indépendante `100*q=p*N`, bornes et complément. Les 7 seeds et valeurs sélectionnées ont été comparées à leurs corrigés affichés. Pas de valeurs libres ni de contrôle par une IA génératrice.
7. **Calculs rédactionnels** : 17 identités sélectionnées de la leçon, des pratiques et du rappel contrôlées avec fraction exacte et multiplication croisée. Cela n'est pas une lecture humaine de chaque phrase pédagogique.
8. **Maîtrise** : M1 (`Q009` maquettes, 25 % de 180 = 45) et M2 (`Q010` pots, 75 % de 160 = 120) ont des bases, unités et contextes distincts; rubrique exige deux preuves sans indice, avec calcul et vérification, sans moyenne compensatoire.
9. **Accessibilité et droits** : présence des consignes orales/tactiles, tableaux textuels, des indications sur unités et de situations fictives contrôlée à la lecture du matériel; provenance déclarée comme production originale. **Aucun audit externe de droits ni essai d'accessibilité avec élèves n'a été réalisé.**
10. **ZIP** : test programmé séparément après rédaction de ce rapport : 14 fichiers attendus, racine, absence de traversées de chemin, non-vacuité, JSON stricts, manifeste exact, CRC et identité des octets avec les fichiers de sortie. Voir les résultats d'exécution ci-après.

## Variantes par défaut vérifiées

- Q004: 20% × 60 crayons = 12 crayons
- Q005: 25% × 200 places = 50 places
- Q006: 50% × 180 billets = 90 billets
- Q007: 20% × 200 minutes = 40 minutes
- Q008: 10% × 230 pages = 23 pages
- Q009: 25% × 180 maquettes = 45 maquettes
- Q010: 75% × 160 pots = 120 pots

## Résultat de l'empaquetage et tests de ZIP

- Le script de validation final doit contrôler le contenu binaire et le CRC du ZIP; **les résultats publiés dans cette livraison ont été produits après exécution de ce script**.
- **Résultat observé** : 14 entrées et 14 fichiers non vides, toutes les entrées sous `kristals/qc-pri-ma-017/`, aucun dossier englobant, aucun chemin absolu ou traversal, JSON stricts analysables, CRC sans erreur, manifeste contenant exactement les 14 chemins, fichiers embarqués identiques aux fichiers vérifiés.

## Limites et décisions humaines encore nécessaires

- Relecture par enseignante ou enseignant des stratégies, de la difficulté et de l'âge/cycle retenu lors de la projection.
- Essais terrain des consignes, de la durée et des adaptations orales/visuelles avec élèves; contrôle qu'une aide motrice ou de lecture ne soit pas comptabilisée comme indice mathématique.
- Qualification humaine des distracteurs et variations s'il s'agit d'un examen sommatif local. Les items **ne sont ni certifiés, ni publiés, ni psychométriquement étalonnés**.
- Revue des droits en cas de publication externe; les seuls éléments utilisés sont des documents de gouvernance internes et des exercices nouveaux rédigés ici.
- Recommandation de structure **non appliquée** : disposer d'un validateur central de familles, d'un assembleur seed→stimulus→corrigé exact, et d'une piste d'audit des deux preuves distinctes dans le LMS. Aucune modification de `registry/` ou `governance/` n'est faite.
