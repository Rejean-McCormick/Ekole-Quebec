# Rapport de validation — livraison `qc-pri-ma-014` v1.2

**Nature :** delta fusionnable à extraire depuis la racine du workspace `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, sans répertoire englobant. **Statut :** validation technique effectuée; **revue pédagogique humaine obligatoire**; ni publication ni certification.

## 1. Provenance et contenu

- **Source effectivement consultée :** archive existante `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip`, contenant la racine `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` et les originaux nécessaires. L'archive `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis.zip` n'était pas jointe séparément; aucun fichier de gouvernance, registre ou autre Kristal n'a été reconstitué.
- **Normes consultées :** `CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md` et inventaire `REFERENCES_EVIDENCE.md` dans la gouvernance v1.2.
- **Graphe effectivement lu :** une unique relation sortante `qc-pri-ma-014/requires/qc-pri-ma-013`; aucun `recommends_before` ni `reinforces` pour cet ID.
- **Authoring effectivement lu :** `PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md` dans `kristals/qc-pri-ma-014/authoring/`.
- **Delta :** 2 remplacements complets d'authoring avec identité/valeurs d'origine préservées, 6 modules de contenu, 3 fichiers d'évaluation, 1 document de références et 2 fichiers de livraison : **14 fichiers exactement**. Aucun autre chemin dans le ZIP.

## 2. Tests techniques réellement exécutés

**Méthode :** assertions Python de structure et d'identifiants; parsing strict des JSON avec détection des clés dupliquées; parsing YAML avec PyYAML; calculs indépendants avec `fractions.Fraction`; ouverture et contrôle CRC du ZIP via `zipfile`.

1. **Compatibilité et identité :** champs, valeurs et listes originaux du contrat JSON préservés récursivement; famille `qc-pri-ma-014-ev-01`, `obj-1`, `crit-1`, objectif, preuve, notion et lien `requires` contrôlés. Les champs supplémentaires imposés par `GENERATEUR_ET_EXAMENS.md` sont présents. Le statut natif reste `architecture_complete_items_a_produire`, non promu.
2. **PARCOURS.md :** en-tête YAML parseable et **identique en valeurs et structure à l'original**; sections numérotées **1 à 12**, chacune une fois et dans l'ordre; références vérifiées.
3. **JSON :** `authoring/CONTRAT_PEDAGOGIQUE.json`, `evaluation/BANQUE_ITEMS.json` et `livraison/MANIFEST.json` parsables, sans clés dupliquées; format de banque `qc.learning-item-bank/1.0` présent; manifeste à 14 chemins.
4. **Banque :** 12 items `001` à `012`, distincts et sans trou; chaque item contient consigne, stimulus, réponse/grille, critères, rétroaction, difficulté, mode et statut; chacun lie exactement `obj-1`, `crit-1`, `qc-pri-ma-014-ev-01`.
5. **Génération :** huit items paramétriques, chacun avec **3 variantes finies** (24 triplets vérifiés); contraintes entières, bornes de fractions, indice reproductible `seed modulo 3`, correspondance du stimulus et du corrigé avec l'instance choisie, résultat réduit et recomposition/contrôle inverse validés exactement en arithmétique rationnelle. Quatre items fixes vérifiés comme non paramétriques.
6. **Contrôles complémentaires :** 13 assertions numériques d'exemples, équivalences et cas de touts différents (10 égalités de leçon, un groupe d'équivalences et 2 calculs de contexte); présence de dispositions d'accessibilité dans les fichiers de parcours, diagnostic, évaluation et remédiation; provenance et absence d'images importées déclarées; références relatives identifiées et résolues.
7. **Maîtrise :** deux preuves explicites dans des **contextes différents**, `q-011` sur l'aire d'un parterre et `q-012` sur la longueur d'un parcours, à occasions séparées, sans indices de résolution et sans inférence d'une note unique.
8. **Fusion et sécurité du ZIP :** vérification finale de la liste exacte des **14 chemins**, de la première entrée commençant par `kristals/qc-pri-ma-014/`, de l'absence de `../`, de chemins absolus, de répertoire englobant, de fichiers globaux ou étrangers; 14 fichiers non vides; conformité octet par octet aux fichiers préparés et CRC valide.

Un contrôle intermédiaire a réussi **314 assertions** sur les 13 fichiers disponibles avant l'ajout de ce rapport, dont le contrôle exact des 24 variantes. Le contrôle final est exécuté **après** génération de l'archive et doit confirmer les 14 entrées; les résultats terminaux du script `validate_build.py --final` constituent le relevé d'exécution et non une certification d'examen.

## 3. Limites et points de revue humaine

- **Expert de mathématique et didactique :** vérifier la progression choisie, l'expression « addition compatible », la clarté de la soustraction du relevé de trajet, la difficulté des partitions 5, 6, 8 et 10, la correction conceptuelle des exemples d'unités distinctes et la pertinence d'exiger deux prestations intégralement réussies.
- **Évaluation :** faire tester les consignes sans montrer les réponses, contrôler le temps de réalisation, la compréhension de la grille et l'indépendance réelle des deux contextes; compléter une observation pilote. Les 12 items sont `a_revoir` et ne peuvent pas être dits certifiés.
- **Accessibilité :** tester lecteurs d'écran/voix, objets manipulables et formulations orales auprès d'usagers réels; les cases Unicode ne garantissent pas à elles seules l'accessibilité dans tous les LMS.
- **Droits :** aucune ressource d'image ou de texte externe importée, mais les droits de publication du workspace et les licences de diffusion doivent être confirmés par le propriétaire avant publication; la seule vérification documentaire n'est pas un avis juridique.
- **Références :** seules les sources du ZIP ont été ouvertes; les pages externes EEF, WWC, CAST et UNESCO listées par la gouvernance n'ont pas fait l'objet d'un contrôle indépendant. Aucune homologation, conformité PFEQ, équivalence scolaire ou efficacité pédagogique observée n'est revendiquée.
- **Intégration :** non testée dans un LMS, l'architecture state/canon/framework ni la fusion effective sur une copie complète du workspace; seul l'emplacement relatif et le contenu ZIP sont contrôlés.

## 4. Propositions de structure, non appliquées

1. Ajouter à un schéma central **dans une évolution versionnée future** un champ optionnel `critere_id` de banque et un référentiel commun de la grille (utilisés ici en extension compatible, **sans toucher** aux bases centrales).
2. Définir un format de gabarits paramétriques approuvés (`gabarit_stimulus`, candidats finement bornés, calculateur rationnel, vérifications de seed), avec passage explicite par une revue humaine; éviter tout moteur de correction IA libre.
3. Introduire au niveau LMS un enregistrement de la preuve par **contexte, occasion et autonomie** afin de ne pas convertir la grille en note unique.
4. Après revue humaine, proposer une mise à jour centrale cohérente du `statut` initial de la frame, sans modifier ici le statut v1.2.

**Aucun changement n'est apporté à** `kristal.workspace.json`, `AGENTS.md`, `authoring/ALIGNEMENT.md`, `docs/`, `canon/`, `state/`, `runtime/`, `registry/`, `governance/` ou aux autres IDs.
