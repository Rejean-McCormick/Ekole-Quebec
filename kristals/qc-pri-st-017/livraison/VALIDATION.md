# Validation et journal des changements — `qc-pri-st-017`

**Livraison :** `qc-pri-st-017_livraison_v1.2.zip` ; **base :** v1.2 ; **statut :** `a_revoir` (contenu pédagogique produit, ni publié, ni certifié, ni homologué). **Date :** 2026-10-08.

## 1. Fichiers réellement produits (périmètre exclusif)

- **Remplacements complets** : `authoring/PARCOURS.md` (YAML d'origine inchangé, 12 rubriques entièrement rédigées) et `authoring/CONTRAT_PEDAGOGIQUE.json` (identité, objectif, lien conseillé, unique famille et champs initiaux conservés; paramètres de famille enrichis).
- **Six nouveaux contenus** : définitions, deux exemples résolus, trois contre-exemples, deux tâches diagnostiques, enseignement, trois exercices guidés à indices dégressifs, quatre pratiques autonomes, remédiations, deux transferts et rappels différés.
- **Trois fichiers d'évaluation** : plan, banque JSON (12 situations contrôlées, 2 preuves de maîtrise sans indice) et grille descriptive A–D exigeant deux contextes de réussite.
- **Autres ajouts** : provenance des sources et droits, ce manifeste et ce rapport. Exactement 14 entrées listées dans `livraison/MANIFEST.json`.

## 2. Contrôles réellement exécutés

Un script de validation **extérieur au ZIP livré** a analysé l'archive source v1.2 et les fichiers produits :

- **244/244 contrôles avant archivage réussis** : 14 chemins attendus, taille des fichiers de travail hors présent rapport, JSON parsables, métadonnées et champs natifs préservés, YAML lu et identique au YAML d'origine, titres des 12 rubriques conservés, `obj-1`/`crit-1`/famille/absence de `requires`, ordre conseillé `qc-pri-st-001`.
- **Vérification de chacun des 12 items** : identifiant unique et continu, champs obligatoires, modes reconnus, consigne/stimulus/réponse/feedback, critères de grille, absence de paramètre aléatoire déguisé, présence de trois organismes au minimum, cartes dans les stimuli, caractère unique par groupe et appartenance de tous les organismes. Le script **recalcule chaque groupe** à partir des valeurs normalisées et contrôle que toutes les réponses modèles contiennent les groupes et les membres attendus.
- **Couverture textuelle contrôlée** : deux diagnostics, trois guidés, quatre autonomes, deux transferts, deux exemples et au moins deux contre-exemples; vérification de mentions sur les droits, l'accessibilité, la sécurité, les références et les liens internes. Épreuves q-011 et q-012 sur des domaines distincts, cinq cartes chacune, choix du critère **non donné dans la consigne**.
- **Contrôle final de l'archive** : 252/252 après compression, comprenant 8 contrôles ZIP supplémentaires (intégrité, ordre et racine, nombre et identité des chemins, absence de chemins dangereux, concordance octet à octet, absence de dossiers supplémentaires, toutes les 14 entrées non vides). Vérifications effectuées par lecture de l'archive créée.

## 3. Qualité scientifique des corrigés — étendue du contrôle

- Vérification logique **réellement exécutée** pour les 12 partitions de fiches : une même valeur de caractère est utilisée à l'intérieur de chaque groupe; pas de carte oubliée ou présente dans deux groupes; noms de groupes et organismes présents dans les corrigés.
- Vérification documentaire **effectuée** via Natural History Museum (six pattes des insectes, huit des araignées adultes, gastéropodes distincts des annélides), American Museum of Natural History (caractères, classement et parenté), University of Minnesota Extension (feuilles larges vs aiguilles) et Arnold Arboretum (mélèze caduc à aiguilles). Détails et URL dans `sources/REFERENCES_CONTENU.md`.
- **Ne sont pas garantis par ces tests** : la complétude du tableau biologique réel, la qualité de toutes les formulations adaptées à chaque âge, la stabilité des jugements humains de rubrique, le fonctionnement avec les technologies d'assistance en situation réelle, ou l'effet pédagogique sur une classe. Un tri fondé sur une seule propriété est présenté comme un modèle descriptif, **pas** comme phylogénie prouvée.

## 4. Limites non résolues, revue humaine requise

1. **Revue scientifique** : relire chaque proposition zoologique et botanique, notamment les stades adultes, escargot/limace/annélide, caractères des oiseaux et le mélèze caduc; refuser une épreuve basée sur une espèce ou un stade non spécifié.
2. **Revue pédagogique** : évaluer l'âge, le niveau de langue, les critères A/B/C/D, les alternatives de groupement acceptables et les deux seuils de maîtrise par une équipe humaine.
3. **Essais de passation** : tester q-011 et q-012 sans indice et avec accessibilité (oral, lecteur d'écran, tableaux linéarisables, temps adapté) avant emploi certificatif ou publiable.
4. **Exemples de reprise** : la banque contient 12 items, dont deux preuves maîtresses; constituer de nouveaux scénarios **revus** si l'élève a déjà vu les corrigés de q-011 ou q-012. Aucun mécanisme d'IA libre ne contrôle automatiquement une nouvelle question.
5. **Droits et production** : seules les fiches textuelles originales sont fournies; aucune image tierce reproduite. Aucune autorisation de réemploi d'illustrations externes n'est présumée. Les scénarios fictifs ne sont pas des rapports d'expérience réelle.
6. **Institutionnel** : discipline québécoise conservée pour présentation; aucun alignement détaillé ni aucune conformité au PFEQ revendiquée.

## 5. Propositions de changements de structure (non appliqués)

- À soumettre en gouvernance **future**, et **non modifié ici** : un champ de statut de validation par fait biologique, référencé à un lien par fiche, afin de distinguer vérification documentaire et décision pédagogique.
- À envisager au niveau système : une table de scénarios de remplacement revue humainement et versionnée, distincte du générateur libre, pour les reprises après divulgation des deux épreuves.
- À envisager dans le LMS : protocole de conservation des deux traces de maîtrise et du niveau d'indice réellement fourni, sans altérer le savoir canonique.

**Périmètre intact :** aucune modification ou inclusion de `kristal.workspace.json`, `AGENTS.md`, `authoring/ALIGNEMENT.md`, `docs/`, `canon/`, `state/`, `runtime/`, `registry/`, `governance/` ni d'un autre identifiant Kristal. L'archive se superpose à la racine du workspace maître v1.2.
