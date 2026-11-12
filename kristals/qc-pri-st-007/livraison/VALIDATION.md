# Validation de livraison — `qc-pri-st-007` (v1.2)

**Statut :** vérifications techniques effectuées; **revue humaine pédagogique/scientifique et essai en classe nécessaires**. Aucun statut publié, homologué ou certifié.

## Source, périmètre et préservation

- Archive source réellement lue : `initbundle(1).zip`, racine `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` ; gouvernance v1.2, graphe, les quatre fichiers `authoring` demandés, `AGENTS.md` et identité du workspace examinés.
- Delta prévu : **exactement 14 fichiers** sous `kristals/qc-pri-st-007/` : **2 remplacements** (`authoring/PARCOURS.md`, `authoring/CONTRAT_PEDAGOGIQUE.json`) et **12 ajouts**. Aucun autre Kristal, aucun registre, canon, gouvernance, `AGENTS.md`, `kristal.workspace.json`, `ALIGNEMENT.md`, `docs/`, `state/` ou `runtime/` livré.
- Métadonnées immuables conservées dans YAML et contrat JSON. Les champs natifs, dimensions de rubrique et `generation` initiale restent présents. Deux champs éditoriaux de statut/révision évoluent dans le YAML; le statut de complétude du contrat évolue de façon non canonique.

## Contrôles réellement exécutés par les scripts locaux

1. **Source et graphe :** lecture effective des JSON et Markdown de l'archive; `requires` sortants inexistants; seul ordre sortant conseillé `qc-pri-st-001` et non bloquant.
2. **YAML :** front matter analysé par `yaml.safe_load`, conservation des valeurs de base hors statut/révision éditoriaux, **12 sections** présentes et ordonnées de 1 à 12.
3. **Contrat :** JSON strict parsé; objectif, preuve, concepts, famille, identifiant et prérequis identiques au source; champs et clés natifs conservés; 13 attributs minimaux du générateur présents.
4. **Banque :** JSON strict parsé, IDs `001`–`012` uniques, **8 scénarios contrôlés et 4 fixes**; objet, famille, critère, feedback et corrigé ou grille présents dans chaque item; `validation_status=a_revoir` partout.
5. **Variation :** pour les huit scénarios, vérification mécanique de l'index `seed modulo 2`, de la paire inséparable stimulus/corrigé, des seeds alternatives et des exemples du corpus (32 tirages de reproductibilité, plus 16 exemples explicités) ; aucune génération textuelle libre.
6. **Qualité éditoriale vérifiable :** contrôle de présence de deux diagnostics, deux exemples résolus, deux contre-exemples, trois pratiques guidées, quatre autonomes, deux transferts et notions cibles; vérification des douze références du plan, deux preuves autonomes distinctes avec modalités de correction non numériques. Le test de présence **ne constitue pas** une expertise pédagogique.
7. **Sources et droits :** provenance explicitement distinguée (fichiers internes lus, sources OpenStax consultées, raisonnements dérivés, textes originaux); aucune image, citation longue ou texte externe reproduit dans les supports. Vérification documentaire, non audit juridique indépendant.
8. **Accessibilité et sécurité :** consignes et modalités d'alternative explicites; vérification documentaire uniquement. Aucune manipulation réelle n'a été exécutée par l'assistant.
9. **Liens internes :** chemins cités vers les fichiers livrés vérifiés sur disque; lien de référence conseillé seulement, sans écrasement du workspace lié.
10. **Archive et fusion :** contrôle automatique des 14 entrées, de la première entrée, des contenus non vides, JSON parsables, de l'absence de chemin absolu/`../` ou dossier englobant; simulation d'extraction dans une copie temporaire de l'archive maîtresse, comparant collisions et fichiers hors périmètre. Les résultats ont été confirmés lors de l'exécution de ce validateur.

## Limites non résolues et revues à faire

- **Physique / pédagogie :** un spécialiste doit relire la justesse conceptuelle des 16 variantes de stimuli, le langage de causalité, les déductions possibles, les contre-exemples et l'étalonnage des niveaux. Vérifier en situation si la distinction friction/traction/poussée est accessible au public visé.
- **Observations expérimentales :** les items `q-011` et `q-012` évaluent une production réellement observée. **Aucun résultat de classe ni mesure de force n'a été produit, testé ou certifié ici.** Un protocole pilote avec des objets locaux doit être observé, et la grille adaptée à la réalité du matériel.
- **Accessibilité :** la médiation adulte et l'usage de traces rapportées demandent validation d'équivalence avec `crit-1`; la qualité de la lecture audio et du matériel tactile n'a pas été éprouvée.
- **Droits :** audit de publication/licences à faire avant toute réutilisation publique; références factuelles et productions originales identifiées, sans déclaration de droits sur le bundle initial.
- **Framework :** pas de test LMS, de publication, de génération IA libre ni de test automatisé d'une vraie manipulation; les scripts ne jugent pas la validité de performances d'élèves.

## Propositions de structure — non appliquées

- Introduire dans une future version centrale un champ standard `nature_de_preuve` (`trace_fournie` / `observation_reelle`) pour empêcher de confondre question sur récit et épreuve expérimentale.
- Définir centralement un schéma `scenario_controle` avec vérification des paires corpus/seed et une référence stable aux critères de rubrique.
- Définir une fiche de sécurité et d'équivalence d'accessibilité pour expérimentations scolaires; aucune modification centrale effectuée ici.

## Instructions d'intégration

Décompresser l'archive maîtresse, entrer dans son dossier `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, puis extraire **`qc-pri-st-007_livraison_v1.2.zip`** à cet endroit. Les chemins internes sont directement `kristals/qc-pri-st-007/...`. En fusion, seuls les deux fichiers `authoring` prévus doivent être écrasés.
