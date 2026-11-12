# Provenance et références de contenu — `qc-pri-ma-033`

## 1. Sources internes effectivement consultées et vérifiées dans l'archive source

Les documents suivants ont été lus dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` à partir de `initbundle(1).zip` fourni dans la conversation. Leur présence et leurs champs ont été vérifiés directement; leur statut est celui du **workspace interne**, non d'une référence gouvernementale ou d'une validation scientifique externe.

| Document source (chemin dans la racine du workspace) | Apport vérifié |
|---|---|
| `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` | Méthode diagnostic → modèle → guidage → autonomie → rappel/transfert; deux manifestations autonomes; pas de conformité PFEQ revendiquée. |
| `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` | Champs de famille, trois modes de génération, paramètres bornés, seed stable, revue humaine des épreuves. |
| `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` | Appellation « Mathématique », identité `qc-pri-*` interne et absence d'assignation automatique à une année. |
| `registry/GRAPHE_PEDAGOGIQUE_202.json` | Aucune arête `requires`, `recommends_before` ni `reinforces` pour `qc-pri-ma-033` dans ce graphe. |
| `kristals/qc-pri-ma-033/authoring/PARCOURS.md` (original) | Frontmatter v1.2, 12 sections, objectif `obj-1`, preuve `crit-1`, notions et statut de frame. |
| `kristals/qc-pri-ma-033/authoring/CONTRAT_PEDAGOGIQUE.json` (original) | Famille `qc-pri-ma-033-ev-01`, type `paramétrique_controle`, champs natifs à préserver. |
| `kristals/qc-pri-ma-033/authoring/ALIGNEMENT.md` | Charte de présentation uniquement, aucun alignement ministériel détaillé demandé. |
| `kristals/qc-pri-ma-033/authoring/BRIEF_REDACTION.md` | Notions, critères, autonomie et interdiction d'inventer les liens du graphe. |

## 2. Raisonnements dérivés, avec contrôles arithmétiques

Les règles élémentaires utilisées sont : multiplication pour groupes identiques, division exacte pour partage en parts égales, addition/soustraction pour entrée/sortie, périmètre du rectangle `2×(L+ℓ)` (une longueur), aire `L×ℓ` (une surface). Les exemples utilisent uniquement des valeurs entières (aucun arrondi). Les paramètres et cas bornés des six items paramétriques sont calculés/testés avec un script local avant empaquetage; les équations et résultats de chaque variante figurent dans `BANQUE_ITEMS.json`. Ce contrôle de cohérence **ne prouve pas** à lui seul l'efficacité de l'enseignement ou l'absence d'ambiguïté pour les élèves.

Les règles de cotation, la sélection de deux contextes et les seuils analytiques sont des **décisions éditoriales internes** dérivées de l'objectif, de la preuve et du contrat v1.2; elles n'ont pas été validées empiriquement auprès d'élèves.

## 3. Productions originales créées pour cette livraison

Définitions didactisées, exemples de paniers / cartes / rectangle, contre-exemples, diagnostics, dialogue de modelage, quatre exercices autonomes, remédiations, transferts, dix items, calculs paramétriques et rubriques sont rédigés ici pour `qc-pri-ma-033`. Les schémas sont textuels et construits sur place, sans images de tiers ni extraits littéraires sous licence. Aucune autorisation de diffusion d'éléments externes n'est supposée.

## 4. Ce qui n'est pas vérifié / revendiqué

La source initiale du frame mentionne EEF, IES/WWC et CAST (voir sa section 12), mais **cette livraison ne prétend pas avoir audité indépendamment** leurs études, leurs éditions ou leurs droits; elle n'en reproduit ni tableaux ni passages. Aucune page de la Progression des apprentissages québécoise, aucun contenu externe protégé et aucune norme scolaire officielle détaillée n'ont été importés. Aucune homologation PFEQ, certification d'items, validation auprès d'élèves, propriété canonique v9 ou publication n'est revendiquée. Une relecture pédagogique et une validation d'accessibilité en situation sont nécessaires.
