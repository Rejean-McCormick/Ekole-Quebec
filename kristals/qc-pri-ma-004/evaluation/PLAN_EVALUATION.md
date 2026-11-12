# Plan d'évaluation — qc-pri-ma-004 (v1.2)

**Contrat gelé :** `obj-1` — « Identifier, poursuivre et décrire une régularité numérique. »; `crit-1` — « Compléter une suite et expliciter une règle qui permet d’en prévoir la suite. »; **famille** `qc-pri-ma-004-ev-01`. **Type privilégié de la famille :** `paramétrique_controle`; modes d'items `parametrique` et `fixe` tels que spécifiés par `BANQUE_ITEMS.json`. Aucune homologation scolaire, certification ou déclaration de publication.

## Couverture item par item

**Chaque ligne** lie le même `obj-1`, `crit-1` et `qc-pri-ma-004-ev-01`. « Prévu pour preuve » ne signifie pas validé par une revue humaine.

| Item | Diffic. | Mode | Représentation | Cible et correction vérifiable | Preuve autonome? |
|---|---|---|---|---|---|
| `q-001` | initial | parametrique | nombres écrits | Deux termes suivants, pas positif; formule et différences | non |
| `q-002` | initial | parametrique | étapes de cubes | Deux termes et règle d'ajout à partir des quantités | non |
| `q-003` | initial | parametrique | nombres et flèches | Deux termes, direction décroissante, `d < 0` | non |
| `q-004` | intermédiaire | parametrique | rangs/cases | Case intérieure et terme au rang 6 | non |
| `q-005` | intermédiaire | fixe | motif alterné écrit | Récurrence de deux valeurs, pas non constant | non |
| `q-006` | intermédiaire | parametrique | tableau de rangs | Deux valeurs aux bons rangs; écart commun | non |
| `q-007` | intermédiaire | fixe | critique d'une règle | Rejeter faux pas, rectifier et poursuivre | non |
| `q-008` | intermédiaire | parametrique | deux cases intérieures | Pas inféré d'un écart sur deux rangs | non |
| `q-009` | transfert | parametrique | chaises, effectifs | Modéliser le nombre par rangée, donner la règle | non |
| `q-010` | transfert | fixe | longueurs de rubans, cm | **Preuve 1** : compléter et justifier sans indice | **oui (contexte mesure)** |
| `q-011` | transfert | parametrique | chaises par rangée | **Preuve 2** : compléter et justifier sans indice | **oui (contexte dénombrement)** |
| `q-012` | transfert | fixe | justification d'une règle | Règle compatible, limites d'unicité | non |

## Contrôle et variabilité

- **Items paramétriques `q-001`, `q-002`, `q-003`, `q-004`, `q-006`, `q-008`, `q-009`, `q-011` :** le champ `seed` contient une graine entière; les domaines inclusifs, la loi modulo, les termes calculés `t(n)`, les contraintes de signe et de non-négativité, les positions masquées et **deux instances calculées par item** sont intégrés dans `parametres`. Paramètres modifiables : uniquement `a` et `|d|`, sans changer le contexte. Le corrigé peut être recalculé indépendamment par récurrence.
- **Items fixes `q-005`, `q-007`, `q-010`, `q-012` :** conserver exactement les nombres, les contextes, les indices et le corrigé. Toute nouvelle situation constitue un **nouvel item à réviser**. `q-012` accepte une autre continuation seulement si la règle est entièrement définie, compatible avec les quatre termes affichés et non présentée comme unique.
- **Validation algorithmique :** la concordance de deux méthodes de calcul ne valide pas automatiquement la clarté, le niveau ou le biais. `validation_status: a_revoir` pour les douze items.

## Passation, critères et niveau de preuve

1. **Avant :** D1 et D2 diagnostiques (hors banque), puis enseignement et exercices si nécessaire. Aucun verrou inter-Kristals; `qc-pri-ma-002` recommandé mais non bloquant.
2. **Formative :** choisir `q-001` à `q-009` en variant croissant/décroissant, début/case intérieure, motif répétitif, données tabulaires et situations concrètes. Ne pas inférer la maîtrise d'un nombre brut de bonnes réponses.
3. **Preuves de maîtrise :** administrer `q-010` (longueurs) et `q-011` (quantités) dans des conditions **sans aide de méthode**, avec matériel neutre si besoin et sans exposition préalable au corrigé. Sur `q-011`, employer la seed affichée ou une seed calculée et archivée; les deux épreuves ont des contextes différents. Ne pas offrir les mêmes réponses sous deux déguisements.
4. **Critères sur chaque preuve :** (A) termes aux bons rangs, (B) règle complète avec départ, direction et variation, (C) deux transitions vérifiées, (D) exécution autonome transférable. Documenter traces et aides éventuelles. Rubrique détaillée dans `GRILLE_MAITRISE.md`.
5. **Décision :** deux preuves satisfaisantes dans deux contextes et autonomie observée. Une erreur réparée **avec indice** implique réenseignement/retest indépendant sur des valeurs et contexte renouvelés, et non approbation automatique.

## Sécurité, droits et accessibilité

- Calculs sur entiers dans des plages bornées; cas décroissants non négatifs aux rangs affichés; les objets sont fictifs et ne demandent aucun achat ni divulgation de données personnelles.
- Gros caractères, énoncés audibles, tableaux étiquetés, jetons ou transcription d'une réponse orale permis **sans indice sur le pas**; ne pas juger l'orthographe ou la vitesse.
- Aucun résultat ne dépend d'une couleur ou d'un dessin inaccessible; chaque schéma a sa transcription numérique. Faire surveiller les petits objets lorsque nécessaire.
- Textes, motifs et corrigés créés ici; pas d'illustration copiée ou de prétention à des droits sur des œuvres tierces. Provenance : `sources/REFERENCES_CONTENU.md`.

## Limites devant être revues par un humain

Qualité des énoncés pour le public visé, acceptabilité des corrections orales, accessibilité avec aides réelles, niveau de difficulté et adéquation des seuils de la grille; **les seuls tests automatisés ne concluent pas à l'enseignement efficace**.
