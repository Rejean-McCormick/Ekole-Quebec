# 13 — Gouvernance, révisions, arbitrages et compatibilité

## 13.1 Quatre versionnements différents

| Objet | Version | Effet |
|---|---|---|
| Norme du projet | SemVer `1.0.0` | Modifie contrats et protocole de contribution |
| Catalogue d'IDs | `registry_revision` | Crée/retire/réserve une identité; n'efface pas l'historique |
| Feuille pédagogique | `revision_contenu` | Change contenu, objectifs, activités, familles |
| État Kristal publié | State/Logical Commitment calculé | Pointeur vers **contenu logique exact** à la publication |

Les éditions officielles (`2026-2027`, `2027-2028`...) sont un **cinquième axe externe** distinct; un changement ministériel n'est pas une simple révision éditoriale de la norme.

## 13.2 Règles de compatibilité

- **PATCH** : orthographe, forme, correction sans changement de signification ni résultats.
- **MINOR** : ajout d'activité, variante, feedback, source mieux établie sans rompre les résultats ou contrats de sortie.
- **MAJOR** : changement de résultat principal, seuil, critères ou famille de tâche qui modifie les preuves; déclencher revue des assemblages/épreuves.
- Identifiant d'une feuille ne change jamais avec sa version. Si son objet pédagogique change au point de rendre les anciennes références trompeuses, créer un nouvel ID, marquer l'ancien `retiré` ou `remplacé`.
- Toute épreuve générée pointe vers les versions exactes utilisées; jamais seulement un titre de feuille.

## 13.3 Processus RFC

Obligatoire pour : nouvel ID, suppression/réaffectation, scission/fusion, nouveau type de relation, modification du contrat, ajout de branche, changement du protocole d'évaluation, changement d'interprétation curriculaire affectant plusieurs feuilles. Voir [MODELE_CHANGEMENT.md](../modeles/MODELE_CHANGEMENT.md).

1. Proposition sourcée + problème + options + impact.
2. Évaluation curriculaire (si pertinent), pédagogique, technique et de licences.
3. Décision par responsable d'intégration; journal de décision et date.
4. Si accepté : incrémenter versions concernées, migrer références, tester.
5. Publier nouvelle norme commune **avant** de démarrer de nouveaux lots.

## 13.4 Éditions officielles concurrentes

Une feuille peut garder sa signification pédagogique alors que ses mappings vers le français 2026–2027 et 2027–2028 divergent. On conserve **deux ensembles d'alignements** (et éventuellement deux recettes d'assemblage), sans rendre un seul enseignement intemporel « automatiquement conforme aux deux ».

## 13.5 Pas d'autorité implicite

L'intégrateur peut valider la cohérence du projet, **pas** certifier une homologation gouvernementale. Les états `qualifié` signifient « vérifié selon notre protocole ». Les changements du Framework/Kit nécessitent un audit de compatibilité spécifique avant migration.

## 13.6 Révisions du registre officiel (ajout v1.1)

Le registre `REFERENCES_OFFICIELLES_QC.md` est révisé par intégration centrale avec références contrôlées. Il ne crée aucune nouvelle autorité sur le PFEQ et ne renomme aucun des 202 Kristals. Les changements documentaires concernant une édition officielle peuvent nécessiter une relecture de tous les alignements concernés.
