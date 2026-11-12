# VALIDATION — qc-pri-st-009 · delta de livraison v1.2

**Statut :** rédaction complète; validation technique locale exécutée; revue scientifique, didactique et sécurité réelle toujours requises. **Pas certifié, pas homologué, pas publié.**

## Provenance et frontière de modification

- Lecture effective, dans l'archive maîtresse `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, des trois fichiers de gouvernance demandés, du graphe, de `authoring/PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md` et `BRIEF_REDACTION.md`.
- Graphe : **un** lien sortant `recommends_before(qc-pri-st-009,qc-pri-st-001)`, **aucun** lien `requires` et aucun `reinforces` impliquant cet ID. L'ordre conseillé ne bloque rien.
- Deux fichiers `authoring/` remplacés en conservant YAML d'origine, identité, objectif et métadonnées; 12 fichiers ajoutés. Aucun chemin protégé n'est empaqueté.

## Tests automatiques réellement exécutés

La construction a exécuté **47 assertions nommées** sur l'archive source, la conservation des métadonnées, les 12 sections, les identifiants, l'unicité et la qualité structurelle des items, les références `obj-1` / `crit-1` / famille, le corpus fermé de variantes, l'absence de tirage libre, les deux preuves distinctes, les JSON, le manifeste, les consignes de sécurité/accessibilité et les chemins. Les contrôles ZIP et fusion sont exécutés ensuite dans le même script; ils sont consignés dans le bilan terminal d'exécution.

- **Contrôle de schéma :** le JSON a été chargé par un parseur standard; la structure minimale de chaque item est présente, les 10 ID sont consécutifs et sans doublon; les scénarios ont les deux variantes A/B et des règles de sélection reproductibles, avec B inactive jusqu'à revue.
- **Contrôle de provenance :** les quatre notions, les liens et les objectifs sont conformes aux fichiers source v1.2. Références factuelles et droits explicités dans `sources/REFERENCES_CONTENU.md`.
- **Contrôle scientifique de logique :** réponses et modèles confrontés aux propriétés documentées (obstacle opaque/ombre; vibration/air/son); aucun score numérique prétendument validé par mesure. Les résultats attendus sont conditionnels à un montage effectif; non-observation = reprise plutôt que résultat inventé.
- **Contrôle de sécurité/accessibilité :** instructions explicites, montage à piles, volume faible, interdiction de lasers/prises/flammes, adaptation audition/vision/motricité; **contrôle éditorial uniquement**, pas une inspection physique.

## Limites non résolues et revue humaine obligatoire

1. Faire tester le contraste de la silhouette dans un local suffisamment contrôlé, puis la sensibilité à l'éclairage ambiant.
2. Essayer le montage de vibration pour vérifier une vibration visible et, lorsque pertinent, audible, sans rupture d'élastique; contrôler le risque d'allergie et le volume.
3. Relire la justesse scientifique des descriptions, la distinction observation/modèle/inférence, l'accessibilité des deux tâches de manipulation et les attentes de niveaux P1–P5.
4. Essayer les items avec des élèves aux profils variés, contrôler durée, clarté, biais et éventuelles difficultés de passation; valider les variantes B avant activation.
5. Vérifier la licence et le droit de tout support complémentaire que l'établissement ajouterait ultérieurement; aucun média tiers n'est livré.
6. Aucune homologation PFEQ, aucun essai Framework/LMS ni validation humaine n'ont eu lieu dans cette production.

## Propositions de structure (NON appliquées)

- Ajouter au moteur un champ facultatif `assistance_motrice_neutre` distinguant gestes assistés et raisonnement guidé.
- Formaliser une catégorie `preuve_non_concluante_montage` distincte d'un échec de l'élève.
- Définir un contrat versionné d'activation des variantes fermées (`variante_id`, `revue_humaine`, `controle_de_faisabilite`) dans un processus central ultérieur.

**Fusion :** depuis la racine `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` du workspace maître décompressé, extraire le delta; ne pas créer de dossier englobant ni écraser d'autres Kristals.
