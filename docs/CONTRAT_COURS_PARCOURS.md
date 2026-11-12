# Contrat de composition Ekole — cours ≠ parcours

## Définitions

- **Cours (vue Ekole)** : fiche pédagogique individuelle, actuellement adossée à un Kristal du registre `qc-pri-*`; son contrat `obj-1`, ses préalables, ses activités et sa banque d’items restent sous l'autorité du Kristal source. Le mot « microparcours » peut exister dans l'Authoring Kit historique : l'interface Ekole distingue désormais le **cours** de ses assemblages.
- **Parcours d’étape** : ensemble explicite de cours pendant une étape d'une année, quatre étapes pédagogiques de durée variable. Il peut contenir zéro cours tant que la sélection n'est pas validée. Il n'est pas un cours Moodle.
- **Parcours d’année** : union des cours des quatre étapes pédagogiques de cette année, plus des cours affectés à l'année sans étape précisée. Les doublons sont dédupliqués pour l'affichage.
- **Parcours de cycle** : union des parcours de ses années. La configuration primaire initiale est 1–2, 3–4, 5–6; le modèle permet de remplacer ces groupes par des cycles de **deux ou trois années** selon une gouvernance pédagogique explicite. La similarité de contenus ne se présume pas : les regroupements sont éditoriaux jusqu’à revue.

## Arbre de navigation

```text
Ekole
├─ Parcours / cycles
│  ├─ 1er cycle : 1re année, 2e année
│  │  ├─ Étape 1 : ensemble de cours (automne)
│  │  ├─ Étape 2 : ensemble de cours (automne)
│  │  ├─ Étape 3 : ensemble de cours (hiver)
│  │  └─ Étape 4 : ensemble de cours (hiver)
│  ├─ 2e cycle : 3e, 4e année (idem)
│  └─ 3e cycle : 5e, 6e année (idem)
└─ Bibliothèque des 202 cours — accès indépendant, y compris cours non affectés
```

## Fichiers, autorité et compatibilité

- `site/data/organisation-parcours.json` : cycles, années, étapes et règles de composition. Changer les groupes de cycle seulement après revue; ne pas déduire un cycle à partir de la vague de production.
- `site/data/parcours-affectations.json` : table éditoriale locale des **affectations à une étape**. Chaque `cours_par_etape[annee-N-etape-M]` contient des IDs de cours exacts. Remplir `preuves_attribution[ID]` pour documenter qui et pourquoi; pour une publication, les revues restent obligatoires.
- `site/data/niveaux-manuel.json` : compatibilité avec l'overlay précédent, **jamais écrasé par cet overlay** (exemple sous `site/data/niveaux-manuel.exemple.json`). Une affectation de niveau 1–6 reste une **affectation à l'année sans étape** si aucune entrée `cours_par_etape` ne précise le placement.
- `site/data/index.json` / `site/data/cours/` : bibliothèque de cours existante; ce patch ne la remplace pas, ne modifie pas les 202 Kristals et n'expose aucune banque de réponses.

Aucune année, étape, groupe de cycle ne confère l'homologation PFEQ et aucune progression ne doit être copiée directement dans le mécanisme de verrouillage Moodle. Dans Moodle, les cours, sections et activités restent des objets distincts; l'assemblage de parcours est un produit de la couche Ekole.

## Exemple purement illustratif — ne pas publier comme vraie affectation

```json
{
  "cours_par_etape": { "annee-1-etape-1": ["qc-pri-ma-001"] },
  "preuves_attribution": { "qc-pri-ma-001": "EXEMPLE : attribution à confirmer" }
}
```

La liste réelle livrée reste vide : le mandat précédent ne contenait pas de classement scolaire validé des 202 cours.

## Compatibilité spécifique avec `moodle.zip` actualisé

Cette livraison `moodle.zip` apporte un pont **polymorphe** (`tools/kristal_moodle_bridge.py`, `moodle/contracts/`, lecteur PHP candidat sous `moodle/local_uckk_candidate/`) et une console `opsconsole/`. **Ne pas les remplacer**. Un Kristal peut avoir 0..n projections Moodle, et un cours Moodle peut assembler plusieurs Kristals. Le mot **cours** utilisé dans le site est une **fiche pédagogique de consultation**, pas un identifiant de cours Moodle. Les parcours scolaires Ekole sont une couche d'organisation supplémentaire, sans création ni modification de cours Moodle.

`py -3 tools\ekole.py moodle-plan` reste l'opération du pont polymorphe déjà présent dans la nouvelle version. `py -3 tools\valider_parcours.py` vérifie uniquement les parcours. Aucun champ `vague` du catalogue n'est écrasé : la vague peut rester une métadonnée d'auteur interne, jamais une offre scolaire.

Dans l'archive source fournie, les 202 **fiches publiques** existent sous `site/data/cours/`, mais l'archive ne contient pas nécessairement les 202 workspaces complets `kristals/`. Les commandes `verify`, `moodle-plan` ou certains tests antérieurs exigent ces workspaces et peuvent échouer tant qu'ils ne sont pas montés dans ton dépôt réel. Ne pas reconstituer des états Kristal à partir des fiches publiques.


## Calendrier québécois et terminologie officielle — vérifié le 9 octobre 2026

Les **quatre étapes pédagogiques Ekole** sont une organisation de consultation proposée : deux dans le bloc *automne*, deux dans le bloc *hiver*. Les dates ne sont pas inventées ni universelles. Le **bulletin unique au primaire** est, lui, remis en **trois étapes officielles** distinctes (référence : https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/epreuves-ministerielles-evaluation-apprentissages/ponderations-libelles-bulletin/prescolaire-primaire). Les profils de pondération et la provenance figurent aussi dans `A-Kristal-ScolQc/knowledge-base/sources/assessment_semantics.json`.

Aucun des quatre conteneurs Ekole n’est une *étape officielle de bulletin*, ne vaut quatre mois, ni n’impose une période de notation. Le calendrier local de chaque établissement doit qualifier les dates.

### Migration sans perte du fichier d’affectations

L’overlay **ne remplace jamais** `site/data/parcours-affectations.json`. Il fournit l’exemple `parcours-affectations.4-etapes.exemple.json` à 24 clés. Si tu as déjà une table v3 de 18 clés, le navigateur ajoute les six emplacements de l’étape 4 **en mémoire**, tout en préservant les affectations existantes. Pour inscrire réellement les six nouveaux emplacements :

```powershell
py -3 tools\migrer_4_etapes.py
py -3 tools\migrer_4_etapes.py --apply
py -3 tools\valider_parcours.py
```

La migration crée une sauvegarde du fichier original et ne touche ni aux cours, ni aux preuves d’attribution. Les étapes affichées doivent être publiées uniquement avec des affectations justifiées.
