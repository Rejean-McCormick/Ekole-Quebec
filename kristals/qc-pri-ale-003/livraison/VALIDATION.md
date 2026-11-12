# VALIDATION — delta `qc-pri-ale-003` v1.2

**État :** contenu rédigé, `a_revoir` pour qualification pédagogique. Aucun item « publié », « homologué » ou « certifié ». Les preuves de classe et les essais humains n'ont pas été réalisés. Cette page distingue strictement les contrôles techniques exécutés et les questions ouvertes.

## Périmètre de fusion

Archive cible : `qc-pri-ale-003_livraison_v1.2.zip`; racine interne `kristals/qc-pri-ale-003/`. **14 fichiers uniquement** : 2 remplacements intégraux dans `authoring/`, 6 nouveaux contenus, 3 évaluations, 1 référence de contenu, 2 fichiers de livraison. Aucun `kristal.workspace.json`, `AGENTS.md`, `ALIGNEMENT.md`, `docs/`, `canon/`, `runtime/`, `state/`, `registry/`, `governance/`, ni dossier d'autre Kristal n'est empaqueté. Fusion prévue à la racine du workspace `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` sans dossier englobant.

## Contrôles techniques et documentaires (à renseigner uniquement après exécution)

Le script local de validation `test_delivery.py`, **exécuté hors de l'archive et non livré**, vérifie :

1. Inventaire exact des 14 chemins, unicité, premier chemin, taille non nulle, aucune entrée absolue ni `..`, aucune racine englobante et CRC ZIP.
2. YAML `PARCOURS.md` analysable, contenu de frontmatter identique au fichier original, sections `## 1.` à `## 12.` présentes en ordre.
3. Trois JSON strictement parsables (contrat, banque, manifeste); conservation des champs natifs, des valeurs canoniques et de la famille existante; complétude des 13 champs familiaux.
4. Concordance des ID, titre, discipline, objectif observable, preuve, `requires qc-pri-ale-002` et aucune arête sortante supplémentaire, d'après le graphe original.
5. Banque de 13 items numérotés `q-001` à `q-013`, sans doublons, champs exigés et 13 stimuli anglais non identiques, usages 2 + 3 + 4 + 2 + 2, deux textes de maîtrise distincts et initialement nouveaux.
6. Correspondance textuelle entre chaque stimulus de banque et le passage de contenu (ou, pour les preuves, le plan/JSON), décompte de mots imprimés, question de sens et réponse déterminée, grille de lecture descriptive et absence de mécanisme génératif libre.
7. Cibles des liens Markdown locaux, mots-clés de droits/accessibilité, absence de fichiers étrangers, validation technique de la fusion sans modification des fichiers centraux.

**Résultats numériques et anomalies :** voir la section « Résultats exécutés » ci-dessous, renseignée à la fin de la génération technique; ne pas supposer qu'un test annoncé ici a déjà été lancé.

## Résultats exécutés

**Exécution locale documentaire — réussie :**

- Whitelist : exactement **14 fichiers non vides** et 14 chemins conformes dans le manifeste, tous sous `kristals/qc-pri-ale-003/`.
- `PARCOURS.md` : YAML analysé, frontmatter **identique** à la source v1.2, sections **1 à 12** dans l'ordre.
- **3 JSON stricts parsés**; champs et valeurs native du contrat conservés, famille originale et ses paramètres de gouvernance complétés.
- Identité, titre, discipline, `obj-1`, `crit-1`, preuve et relation `requires qc-pri-ale-002` cohérents avec le graphe consulté.
- **13 items fixes et uniques**, numéros consécutifs `q-001…q-013` ; ventilation 2 diagnostics / 3 guidages / 4 autonomies / 2 transferts / 2 maîtrises.
- Onze stimuli d'enseignement et leurs questions de sens comparés aux fichiers de contenu; les deux stimuli réservés font **68** et **71** mots et sont distincts; illustration du calcul d'exactitude vérifiée (`64/68≈94,1 %`, `66/68≈97,1 %`).
- **17 liens Markdown locaux** résolus; présence documentaire de droits, accessibilité et neutralité de l'accent vérifiée (contrôles statiques, **pas** validation de classe).
- **Contrôle final du ZIP** : 14 entrées dans l'ordre du manifeste, premier chemin conforme, aucun préfixe superflu ni chemin dangereux, CRC valide, octets identiques aux fichiers du delta, JSON internes relus.

Tous les contrôles ci-dessus sont documentaires ou techniques. **Aucune preuve d'apprentissage réelle, aucune fiabilité psychométrique, aucune revue linguistique externe ni essai d'accessibilité n'a été exécuté.**

## Limites non résolues et interventions humaines

- Reviseuse/reviseur compétent en anglais : syntaxe, fluidité des passages, phrasé alternatif valable, vocabulaire et adéquation au lectorat; contrôler aussi les réponses littérales.
- Essais de lecture réelle : équité dialectale, accès visuel et vocal, compréhension, besoins linguistiques divers; aucune mesure de terrain disponible.
- Calibration de 95 % / 98 %, niveaux A/P/C/R et stabilité entre observateurs : seuils proposés, non validés psychométriquement.
- Confidentialité : décider rétention, consentement et suppression des éventuels audios; aucun audio requis par ces fichiers.
- Droits : contrôle humain des textes originaux et des règles d'utilisation; aucun média tiers incorporé.
- Les contrôles automatiques lisent des fichiers, **ne jugent pas** de la qualité expressive réelle d'une voix ni de l'efficacité de l'enseignement.

## Propositions éventuelles au cadre central — **non appliquées**

1. Ajouter au schéma partagé un `evidence_protocol` optionnel indiquant `first_unseen_reading` / `same_text_rereading` / `second_distinct_context`, sans écraser les champs natifs des familles.
2. Autoriser une structure `accessibility_adaptation_log` et `observer_agreement_status` au niveau de la session LMS, pas dans les savoirs canoniques.
3. Documenter explicitement l'effet plafond quand objectif = amélioration entre deux lectures, après revue de l'autorité pédagogique.
4. Envisager un type de lecture orale observée pour un prochain schéma, tout en conservant ici **le type v1.2 d'origine `réponse_argumentée`**.

Toute modification du registre, des normes et de la structure centrale doit passer par la gouvernance appropriée, hors de ce ZIP.
