# Validation — delta `qc-pri-st-010` v1.2

## Portée et origine

Rédaction pour **un seul Kristal** à partir de `initbundle(1).zip` (dossier maître `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`). Gouvernance, graphe, `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, parcours et contrat de départ lus. Liens du graphe sortants : uniquement `requires(qc-pri-st-010,qc-pri-st-008)`; aucune autre relation sortante. Titre et objectif préservés, **aucune homologation PFEQ revendiquée**.

## Contrôles automatisés effectués avant empaquetage

- **74 assertions réussies** : existence des 13 premiers documents, absence de contenu vide, parsage des trois JSON, frontmatter YAML, 12 sections et leur numérotation.
- Conservation des champs de départ des fichiers `authoring/`; objectif, preuve, préalables, format, identifiants, famille et graphe sortant inchangés. Les champs de gouvernance manquants sont complétés **dans l'objet famille original**.
- 10 items `q-001` à `q-010`, sans doublons, reliés explicitement à `obj-1`, `crit-1` et à `qc-pri-st-010-ev-01`; modes valides, énoncés, réponses, rubriques et rétroactions renseignés.
- Deux épreuves de maîtrise réellement distinctes **E1 coin lecture / E2 atelier fictif** (interrupteur à bascule et poussoir), exigences de preuve décrites dans la grille.
- Pour les deux items à scénarios contrôlés : indices calculés `seed % 3`; exemples émis comparés à la même entrée de corrigé; **six variantes** contrôlées sur les états ouverts/fermés et prédictions de lampe, sans générateur libre.
- Relecture de la formulation des erreurs dangereuses et des règles d'accessibilité dans les textes. Vérification technique documentaire des liens et identifiants (pas test de navigateur/LMS).

## Contrôles de l'archive finale — exécutés et réussis

À la fermeture de l'archive, le constructeur vérifie **14 fichiers exactement**, non vides, tous sous `kristals/qc-pri-st-010/`, sans répertoire englobant ni traversée de chemin; vérifie la concordance du manifeste, le parsage des JSON et du YAML, l'intégrité CRC (`testzip()`), et simule la superposition avec l'archive maîtresse. **Résultat :** 2 fichiers `authoring/` remplacés, 12 nouveaux fichiers et aucun chemin protégé ni dossier d'un autre Kristal. Le script arrête la construction en cas d'échec. Une exécution du script terminée sans erreur atteste ces contrôles techniques, **pas** une qualification pédagogique.

## Limites non résolues / revue humaine nécessaire

1. Aucune expérience physique effectuée : l'allumage dans les corrigés est une **prédiction pour composants fonctionnels**, non un constat effectué.
2. Vérifier physiquement la compatibilité de la douille, ampoule incandescente **nominale 3 V**, support **2 AA alcalines**, connexions et commandes homologuées pour le kit choisi; la conformité d'un matériel commercial précis n'a pas été contrôlée.
3. Revue indépendante scientifique et pédagogique requise : clarté des schémas, vocabulaire des élèves, équité, accessibilité, charge cognitive et sécurisation du local.
4. Essais supervisés et vérification de la grille avec élèves requises; aucune maîtrise individuelle ni fiabilité psychométrique n'est démontrée. En cas de besoin d'un simulateur ou d'aide motrice, une décision humaine doit documenter l'équivalence.
5. Droits : seulement textes/croquis originaux et URL identifiantes; droits de tout futur contenu tiers à vérifier.

## Propositions structurelles **non appliquées**

- Définir éventuellement dans la gouvernance centrale un profil standardisé `materiel_3V_ampoule_incandescente` pour empêcher l'injection automatique de DEL ou piles boutons.
- Distinguer dans les registres de preuves l'état `observation_physique`, `simulation`, `non_teste` pour prévenir la confusion constat/prédiction.
- Harmoniser ultérieurement les champs `validation_status` et les journaux d'essai; demander modification centrale versionnée, pas de changement local de schéma maître.

**Statut :** contenu complet rédigé et contrôlé automatiquement; **revue humaine et démonstration pratique nécessaires**. Pas de mention « certifié », « homologué » ou « publié ».
