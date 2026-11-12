# Validation de livraison — `qc-pri-als-006`, delta v1.2

**Périmètre exclusif :** `kristals/qc-pri-als-006/` · **Archive livrée :** `qc-pri-als-006_livraison_v1.2.zip` · **Statut :** contrôles techniques exécutés; revue humaine nécessaire (`a_revoir`). La présente livraison **n'est pas** un cours publié, homologué ou certifié.

## 1. Base de travail et conservation d'identité

La source effectivement ouverte est le ZIP déjà joint à la conversation **`Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip`**, qui contient intégralement le sous-répertoire de workspace **`Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`**. Les **neuf fichiers sources** de gouvernance, graphe et authoring du Kristal ont été lus depuis ce sous-répertoire et conservés séparément comme base de contrôle, sans être livrés ni modifiés. Le ZIP demandé sous le nom propre `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis.zip` n'était pas nécessaire puisqu'il s'agit d'un workspace embarqué authentique avec ses chemins canoniques, non d'une reconstitution.

**Préservé mot à mot au titre des valeurs :** toutes les clés/valeurs du frontmatter YAML natif; toutes les clés/valeurs natives du contrat JSON (racine et éléments de famille), dont `kristal_id`, `objectif_id`, objectif, notions, preuve, `prerequis_bloquants`, `ordre_conseille`, `type`, `rubric_dimensions`, `generation` et `review_status`. Seuls le **corps rédactionnel** de `authoring/PARCOURS.md` et les **champs additionnels** requis à l'intérieur de la famille du contrat ont évolué. Les 12 sections numérotées sont maintenues. Les deux remplacements sont complets; les douze autres fichiers sont nouveaux.

## 2. Tests réellement exécutés

Tests locaux par Python 3 (`json`, `zipfile`, `re` et analyseur `yaml`) sur les fichiers source/delta; vérification du ZIP final **après sa création** :

- Lecture des neuf références sources indiquées; parsing du graphe; arêtes sortantes : `requires(qc-pri-als-006, qc-pri-als-005)` uniquement. Absence de conseil de progression sortant, conformément au contrat. Une arête **entrante** d'un autre Kristal ne constitue pas un préalable sortant de celui-ci.
- Extraction et parsing du frontmatter YAML; égalité des champs et valeurs d'origine; sections Markdown exactement `1` à `12` dans l'ordre.
- Parsing JSON strict du contrat, de la banque et du manifeste; conservation de tous les champs natifs et des identifiants; présence des 13 paramètres minimum de la famille; statut `a_revoir`.
- Cohérence de l'objectif exact, de la preuve exacte, des quatre notions, du préalable et de l'absence d'ordre conseillé; références internes `obj-1`, `crit-1` et `qc-pri-als-006-ev-01`.
- Banque : 8 identifiants distincts et séquentiels `q-001` à `q-008`, 8 stimuli distincts, mode **fixe**, champs et tâches non vides, au moins 3 faits de scène distincts par item, critères/rétroaction, variation permise/interdite documentée, aucune seed/paramètre artificiel. `q-007` et `q-008` seulement sont des preuves de maîtrise réservées (bibliothèque / terrain de jeu).
- Comptes pédagogiques : au moins 2 exemples résolus, 2 contre-exemples, 2 diagnostics, 3 exercices accompagnés, 4 pratiques autonomes, 2 transferts. Documents de plan/grille : références de tous les items et critères de décision.
- Vérification **statique** de mentions d'accessibilité et d'aide, scénarios fictifs, confidentialité et source/droits; résolution des références locales identifiées par chemins Markdown et présence des fichiers de référence dans le workspace source.
- Conformité du manifeste au delta; **exactement 14 fichiers**, non vides, tous sous la racine `kristals/qc-pri-als-006/`, ni chemins absolus, ni remontée `..`, ni fichiers interdits. Contrôle de la **première entrée** du ZIP, égalité de ses chemins au manifeste, test d'intégrité CRC par `zipfile.testzip()` et relecture de ses trois JSON.

**Nature de ces tests :** vérifications de structure, cohérence déterministe des métadonnées et présence de grilles/énoncés. Ce ne sont **pas** des mesures d'apprentissage, de validité de grille, de compréhension réelle d'élèves, d'accessibilité vécue ou de droits. Les exemples de performances anglaises ont été relus lors de la rédaction, **sans** validation externe indépendante ni test automatique de correction grammaticale fiable.

## 3. Limites non résolues et revue humaine

1. **Revue linguistique ALS requise :** naturel et niveau des expressions orales anglaises; diversité des réponses acceptables; décision en cas d'énoncé intelligible malgré erreur grammaticale; variabilité dialectale et accents.
2. **Fiabilité de la grille non établie :** faire corriger de vraies prestations anonymisées par au moins deux évaluateurs, réviser les descripteurs et vérifier la constance de l'identification des trois informations.
3. **Accessibilité non testée avec usagers :** vérifier vraies cartes/illustrations et descriptions audio, réglages d'aide technique, besoins auditifs/visuels, et procédure d'adaptation si la parole orale est impossible. Aucune image/audio tiers n'est livré.
4. **Confidentialité :** essais d'enregistrement/stockage/consentement LMS non exécutés; ne pas enregistrer la voix sans autorisation et règles de conservation.
5. **Droits :** pas d'emprunt déclaré à une œuvre tierce dans le delta, mais **aucun audit juridique externe de droits**; la banque est originale et reste `a_revoir`.
6. **Référence technique héritée non résolue :** le champ JSON natif `referentiel_technique` indique **`gouvernance/Norme_Pedagogique_Autonome_v1.2`**, tandis que le vrai dossier source commence par **`governance/`**. Ce champ a été **préservé exactement** pour ne pas casser le contrat existant. Il ne peut donc pas être considéré comme un lien résolu.
7. **Alignement source :** le statut YAML `alignement_statut: à_vérifier` et la référence `ALIGNEMENT.md` demeurent tels quels. Aucune approbation PFEQ ou équivalence ministérielle revendiquée.

## 4. Propositions de changement STRUCTUREL (non appliquées)

- Corriger dans une **migration centrale versionnée**, après consultation des propriétaires du schéma, la graphie du champ natif `referentiel_technique` (`gouvernance/` → `governance/`) si d'autres workspaces sont touchés. **Aucun champ natif n'a été corrigé localement** en violation du contrat de fusion.
- Définir un stockage externe de preuves orales chiffré et un format interopérable de fiche d'observation, **hors du canon du Kristal**, avec consentement, rétention et support d'accessibilité.
- Ajouter ultérieurement un protocole humain de validation d'intelligibilité et d'équité interévaluateurs, sans modifier `registry/`, `governance/`, `docs/`, `canon/`, `state/`, `runtime/` ni aucun autre ID.

## 5. Mode de fusion

Décompresser l'archive maîtresse v1.2, entrer **dans** `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, puis extraire `qc-pri-als-006_livraison_v1.2.zip` à cet emplacement. Ses chemins commencent immédiatement par `kristals/qc-pri-als-006/`. Ne pas déplacer son contenu dans un dossier supplémentaire, ne pas importer d'autres fichiers de cet échange.
