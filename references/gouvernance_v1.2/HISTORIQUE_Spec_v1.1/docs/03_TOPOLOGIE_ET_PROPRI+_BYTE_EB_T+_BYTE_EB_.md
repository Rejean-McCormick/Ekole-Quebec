# 03 — Topologie logique, répertoire et propriété du savoir

## 3.1 Quatre catégories; une seule source de vérité par classe

| Classe | Propriétaire | Canonique ? |
|---|---|---|
| Structure scolaire, édictions, programmes, compétences, maturités PDA, édition applicable | `A-Kristal-ScolQc` | Oui, pour ses assertions sourcées et dans ses limites de couverture |
| Microparcours pédagogiques : objectifs internes, enseignement, activités, feedback, évaluations | Collection `Kristal-Parcours-Primaire-Qc` | Oui, pour le contenu créé par le projet |
| Graphe de préalables pédagogiques validés et règles d'assemblage | Registre partagé de la collection | Oui, dans la couche projet |
| Cours Moodle, banques importables, examens générés, index IA, runtime | Adaptateurs / compilateur | **Non : dérivés** |

Une compétence officielle n'est pas recopiée comme connaissance originale; un résultat individuel d'élève n'est pas encodé comme savoir. Les conflits de provenance ne sont pas effacés.

## 3.2 Topologie

```text
A-Kristal-ScolQc (source curriculum et références)
           |
           v [refs précises + éditions]
Kristal-Parcours-Primaire-Qc (collection / nœud potentiel)
    +-- kristals/qc-pri-ma-001/          -> état logique indépendant
    +-- kristals/qc-pri-ma-002/          -> état logique indépendant
    +-- ...                             -> 202 réservations initiales
    +-- registre relations typées        -> sans duplication
    +-- assemblages discipline/cycle/année/variante
           |
           v (projections dérivées)
    Moodle / entraînement / évaluations / tuteur
```

Modèle UCKK réutilisé **seulement** pour le principe de parent référant à des enfants épinglés; ne pas recopier ses « 10 voies × 10 cours » ni transformer nos feuilles en réservations vides publiables.

## 3.3 Convention de dossiers de la collection

```text
Kristal-Parcours-Primaire-Qc/
  README.md
  governance/                    # norme et versions communes
  registry/                      # IDs et propriétaires, relations, assemblages
  kristals/
    qc-pri-ma-001/
      kristal.workspace.json     # généré/conforme à l'Authoring Kit
      docs/                      # intention, frontière, forme native, validation
      sources/                   # catalogue de sources lié
      canon/                     # payload de domaine compilé (après implémentation)
      state/                     # état Kristal v9 / export explicite
      authoring/
        PARCOURS.md              # source éditoriale selon modèle 04
        ALIGNEMENT.md            # preuves curriculaires 05
    qc-pri-fr-001/
      ...
  assemblages/                   # topology de parcours, versionnée
  evaluations/                   # plans d'épreuves, banques propriétaires
  projections/                   # recettes, non vérité canonique
  builds/                        # dérivés jetables, ignorés en source
```

**Important :** la structure `authoring/` et les modèles Markdown sont une convention du projet, **pas des fichiers v9 reconnus nativement**. Les workspaces doivent être générés avec l'Authoring Kit, leurs schémas réels validés; aucune conversation ne doit bricoler un `state-snapshot.json` en le déclarant conforme.

## 3.4 Ownership par type de relation

- La feuille **possède** son enseignement, ses activités et ses critères de maîtrise internes.
- Le registre **possède** les relations inter-feuilles `requires`, `supports`, `reinforces`, `alternative_to` et les métadonnées de revue de ces liens. Une feuille peut en afficher une vue, qui reste dérivée.
- L'assemblage **possède** l'ordre de présentation, ses conditions, filtres et références exactes aux états de feuilles; il ne possède pas leurs contenus.
- Le générateur d'examens **ne possède pas** le sens des compétences : il consomme les sources de vérité et crée des épreuves identifiables.

## 3.5 Formes natives, versionnage et fédération

Les activités pédagogiques sont des séquences ordonnées; les préalables sont un DAG; les liens de réinvestissement peuvent former des cycles sémantiques; les évaluations forment des plans de couverture et des familles de tâches. Il est **interdit** de tout aplatir en un seul graphe non typé. Une publication d'assemblage **DOIT pinner** chaque état référencé à une révision / Logical Commitment conforme au modèle v9; la publication v10 sur GitHub reste une étape opérationnelle distincte et optionnelle.
