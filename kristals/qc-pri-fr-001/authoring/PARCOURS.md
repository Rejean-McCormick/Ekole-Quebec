---
format: qc.learning-path/1.0
id: qc-pri-fr-001
titre: Conscience phonologique et syllabes
discipline_code: FR
statut: en_rédaction
revision_contenu: 0.3.0
langue_contenu: fr-CA
resultat_principal: Segmenter, fusionner et transformer des syllabes et sons de mots entendus.
objectifs_secondaires: []
criteres_reussite:
- Segmenter puis recomposer oralement cinq mots nouveaux.
prealables_declares: []
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-fr-001-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---


# Microparcours — `qc-pri-fr-001`

**Discipline (appellation québécoise) :** Français, langue d’enseignement  
**Intitulé éditorial :** Conscience phonologique et syllabes  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**État :** contenu rédigé et contrôlé localement; validation humaine et qualification du système non faites.  
**Liens de production :** `contenu/01_NOTIONS_ET_EXEMPLES.md` à `contenu/06_REMEDIATION_ET_TRANSFERT.md` ; `evaluation/PLAN_EVALUATION.md`, `evaluation/BANQUE_ITEMS.json`, `evaluation/GRILLE_MAITRISE.md`.

## 1. Intention et frontières

- `obj-1` (texte IMMUTABLE) — **Segmenter, fusionner et transformer des syllabes et sons de mots entendus.**
- `crit-1` (preuve IMMUTABLE) — **Segmenter puis recomposer oralement cinq mots nouveaux.**
- Concepts : syllabe, phonème, rime, attaque et finale; manipulations orales de découpage, fusion, substitution et suppression.
- Le stimulus est **entendu**; la trace peut être constituée d'une observation ou d'un enregistrement autorisé, non d'une production orthographique. Aucune reconnaissance des lettres, lecture ou écriture requise, ni évaluée.
- Cette unité ne constitue ni certification ministérielle ni prérequis universel pour tous les élèves.

## 2. Notions et représentations

- **Syllabe orale** : unité sonore organisée autour d'un noyau vocalique; elle n'est pas la syllabe graphique. `moto` entendu « mo | to » = deux émissions structurées, `sac` = une seule syllabe malgré trois lettres.
- **Phonème** : unité sonore distinctive, différente de la lettre; `/ʃ/` dans *chat* est un phonème bien que **ch** s'écrive avec deux lettres; `/k/` final de *sac* est audible.
- **Attaque** d'une syllabe : consonne(s) précédant sa voyelle; *sac* = `/s/` + rime `/ak/`. **Rime phonologique** : noyau vocalique et sons suivants; *sac* et *lac* ont la rime `/ak/`. Ne pas confondre avec la dernière syllabe.
- **Finale** : dans ce module, mot pédagogique pour *dernier son* ou *dernière syllabe*, à expliciter dans chaque consigne, sans l'ériger en synonyme technique de rime. Dans *sac*, dernier phonème `/k/`; dans *tapis*, dernière syllabe `/pi/` et dernier phonème `/i/` (le **s** final est muet).
- Montrer par voix réelle, jetons **sans lettres** et gestes de séparation; les transcriptions `/.../` et segments avec `|` sont une **clé de correction destinée à l'adulte**, jamais un test de lecture de l'API.
- Exemples commentés : *moto* → « mo | to » → *moto*; *sac* → `/s/ + /ak/`, puis `/s/` remplacé par `/l/` → *lac*. Contre-exemples : trois lettres ≠ trois syllabes dans *sac*; **ch** ≠ deux phonèmes dans *chat*.
- Référence interne : `contenu/01_NOTIONS_ET_EXEMPLES.md` (schéma et limites de prononciation).

## 3. Préparation / diagnostic

- **`requires` :** `[]` ; **`recommends_before` :** `[]` ; **`reinforces` sortants :** `[]` selon le graphe du workspace. Aucun blocage inter-Kristals.
- Avant tout écrit, demander : D1 « Écoute *maman*, sépare les morceaux entendus; puis *lac*. » Attendu `ma | man` (2), `lac` (1). D2 « J'émets `/ve/` puis `/lo/` : quel mot ? Et `/ka/` + `/fe/` ? » Attendu *vélo*, *café*.
- Consigner séparément segmentation, fusion, intelligibilité et éventuel besoin de répétition; garder les réponses indépendantes. Ne pas qualifier un accent, une vitesse de parole ou l'accès à l'écrit d'incapacité phonologique.
- Si démonstration spontanée complète, offrir une tâche de vérification non entraînée et passage sans blocage; sinon choisir la remédiation précisément correspondant au maillon manquant. Détails dans `contenu/02_DIAGNOSTIC.md`.

## 4. Enseignement guidé

- `teach-1` — Annoncer : « Nous allons écouter un mot, découper ce qu'on entend, réunir les morceaux, puis parfois en changer un. »
- Étape 1, modeler lentement *moto* : dire normalement, puis `/mɔ/ | /to/` (deux jetons), puis fusionner immédiatement *moto*. En français québécois, un `/o/` plus fermé en première syllabe reste recevable; on juge les **frontières**.
- Étape 2, modeler *sac* : une syllabe; trois phonèmes `/s/ /a/ /k/`; isoler attaque `/s/`, rime `/ak/`, dernier phonème `/k/`. Reconstituer *sac* sans ajouter de son « euh » aux consonnes.
- Étape 3, remplacer l'attaque `/s/` de *sac* par `/l/` : *lac*. Demander « Qu'est-ce qui a changé ? Qu'est-ce qui est resté ? » Attendu « le premier son; `/ak/` reste ».
- Étape 4, expliciter que la dernière lettre d'un mot n'est pas forcément son dernier son (*tapis* /i/); introduire geste « doigts pour les syllabes », puis retirer les jetons.
- Contrôle oral : « *sac* a combien de syllabes ? Quelles différences entre `/s/` et la lettre s ? »; corriger avant les entraînements. Script exact : `contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

- `guided-1` comprend trois exercices à **indices dégressifs**, distincts des ensembles de maîtrise.
- G1, indice fort : l'adulte dit *papa*, montre deux jetons, effectue avec l'élève « pa | pa », puis recomposition; réessaie avec *tapis* sans afficher ses lettres. Vérifie que *tapis* = `ta | pi`, et que le **s** écrit n'est pas audible.
- G2, indice moyen : l'adulte dit *bateau*, amorce seulement le premier battement; l'élève donne `ba | to`, puis *bateau*. Pour *chat*, l'animateur rappelle qu'un « ch » prononcé forme un seul son `/ʃ/`, puis fait isoler `/ʃ/ + /a/`.
- G3, sans indice initial : *boule* → remplacer `/b/` par `/p/` → *poule*; demander d'expliquer que `/ul/` reste inchangé. Indice uniquement en cas d'échec, puis essai avec un mot différent.
- Ne pas prononcer la réponse en même temps que l'élève lors de l'essai final. `contenu/04_PRATIQUE_ACCOMPAGNEE.md` fournit scripts, corrections et retrait des aides.

## 6. Pratique autonome

- `independent-1` : quatre activités sans indices : (A1) *bateau/dodo* segmenter-recomposer; (A2) comparer *sac/lac* et situer attaque/rime; (A3) transformer *papa* → *papi* en changeant la dernière syllabe; (A4) fusionner `/ʃɔ/ /kɔ/ /la/` en *chocolat* puis restituer trois syllabes.
- Après entraînement et **sans avoir donné leurs décompositions**, preuve `crit-1` dans deux contextes différents, mots disjoints (voir banque `q-011`, `q-012`) : A « message à une marionnette », B « radio des mots mystères ». Chaque contexte contient **cinq mots nouveaux**, présentés oralement dans un ordre fixé.
- Consigne unique pour chaque mot : « Répète le mot, dis ses syllabes une par une, puis redis le mot d'un seul souffle. » Aucune démonstration ni carte syllabique pendant la preuve; autoriser une répétition naturelle du stimulus **entier**, tracée. Pas de changement spontané de mots.
- Traces d'observation locales, avec consentement si audio; aucune information personnelle incluse dans les fichiers du module. Voir `contenu/05_PRATIQUE_AUTONOME.md` et `evaluation/GRILLE_MAITRISE.md`.

## 7. Feedback et erreurs typiques

- Confondre lettres/syllabes : « Tu as compté les lettres de *sac*. Écoute plutôt les groupes prononcés : *sac* = un. Essaie maintenant *lac*. »
- Ajouter une voyelle d'appui (« seuh » pour `/s/`) : « Garde le souffle `/s/` sans ajouter `/ə/`. Réunissons `/s/ + /ak/` : *sac*. »
- Conserver un découpage mais ne pas recomposer : « Tu as trouvé les parties; maintenant redis-les **sans pause** pour retrouver le mot. »
- Supprimer un son prononcé ou inventer un son écrit : vérifier *tapis* (dernière syllabe `/pi/`, dernier phonème `/i/`), sans lire les lettres à l'élève.
- Confondre attaque, rime et dernière syllabe : reprendre *sac/lac* avec deux jetons sonores (début `/s/`, reste `/ak/`), puis retirer les jetons.
- Toute remédiation exige un **nouvel essai distinct** et l'annotation de l'aide donnée; ne jamais valider comme autonome une réponse obtenue en imitation.

## 8. Évaluation formative et preuves

- **Famille** `qc-pri-fr-001-ev-01`, `objectif_ref: obj-1`, `critere_ref: crit-1`; **type** `réponse_argumentée` interprété comme production **orale observable** et brève verbalisation du procédé, sans exigence de justification écrite.
- Diagnostics `q-001/q-002`; formateurs `q-003` à `q-008`; transferts `q-009/q-010`; deux épreuves de maîtrise `q-011/q-012` : même compétence, listes fixées, contextes distincts, aucune restitution de mots enseignés.
- Par contexte : 5/5 mots **segmentés puis recomposés correctement** sans aide de contenu (autocorrection spontanée acceptée avant rétroaction), frontières orales pertinentes, ordre des syllabes maintenu; 2 contextes réussis et processus observable pour attester. Si échec, décision « à consolider », puis nouvelle preuve indépendante non créée automatiquement.
- Aucune inférence d'une moyenne globale, d'un âge, d'un score d'orthographe ou d'une reconnaissance vocale automatique. Plan, banque fixe et grille disponibles dans `evaluation/` ; **statut `a_revoir`**, essai terrain et revue humaine obligatoires.

## 9. Remédiation / enrichissement

- **R1 :** syllabes non repérées → d'abord mots à deux syllabes ouvertes avec rythme et jetons, puis supprimer les jetons; valider sur un nouveau mot.
- **R2 :** segmentation réussie/fusion échouée → accélérer progressivement deux unités entendues, puis dire le mot en un seul flux; un deuxième mot vérifie l'acquis.
- **R3 :** confusion phonème-lettre → demander uniquement des sons, jamais épeler; contraster *chat* `/ʃa/` et *sac* `/sak/`.
- **R4 :** confusion attaque/rime → *sac/lac* et *boule/poule*; isoler ce qui change et ce qui reste, puis retirer les repères.
- **Enrichissement** : suppression/substitution d'une syllabe d'un mot entendu, en annonçant si le résultat est un pseudo-mot; ne pas juger son existence lexicale. Aucun lien `reinforces` sortant n'a été déclaré pour ce Kristal.

## 10. Accessibilité

- L'adulte parle clairement en français québécois à débit habituel puis peut répéter **le mot entier** une fois sans en découper les syllabes; utiliser écoute de proximité, réduction du bruit, casque adapté ou modalité audio accessible selon besoins.
- L'élève peut montrer les frontières de syllabes par gestes, jetons ou battements **en complément de** sa restitution orale; l'objectif exige qu'une recomposition orale soit observable. Prendre en compte une difficulté d'articulation documentée par preuve gestuelle/explicative et prévoir une revue humaine plutôt que sanctionner un accent.
- Images facultatives non indispensables; ne pas demander lecture, épellation, vitesse, dévoilement de santé, enregistrement sans consentement, déplacement corporel obligatoire ni accès à une technologie.
- Les variantes régionales qui **ne changent pas** la segmentation ou les unités pertinentes ne sont pas des erreurs. En cas d'ambiguïté dialectale sur un item, suspendre son usage et soumettre à la révision humaine; ne pas improviser un nouveau corrigé.

## 11. Critères de sortie

1. `crit-1` — **Segmenter puis recomposer oralement cinq mots nouveaux.** Répéter dans **deux contextes distincts**, avec cinq autres mots la seconde fois; trace par mot des deux actions (segmentation + recomposition).
2. Aucune aide de contenu dans l'une ou l'autre preuve, ordre des syllabes préservé, auto-correction spontanée autorisée; comprendre le procédé, sans récitation d'exemples antérieurs.
3. Vérifier en parallèle `obj-1` par des tâches d'attaque/rime, de phonèmes et de transformation, sans réduire la décision à une note unique.
4. Si une preuve est insuffisante : documenter le maillon en défaut, remédier, puis réévaluer avec du matériel neuf **approuvé**, sans valider artificiellement par répétition immédiate de la même liste.

## 12. Références pédagogiques et limites

- Autorité de conception : `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md` et `REFERENCES_EVIDENCE.md`; la référence au système scolaire québécois est une **étiquette de discipline** et non un alignement PFEQ.
- Références de terminologie vérifiées : Office québécois de la langue française, pages « La syllabe phonétique » et « Phones et phonèmes : les distinguer » (adresses et périmètre dans `sources/REFERENCES_CONTENU.md`).
- Conceptions propres au module : choix des mots, ordre de difficulté, séparation de deux contextes et seuil interne 5/5; **choix pédagogiques locaux non démontrés comme universellement optimaux**.
- Limites : usages québécois variés, écoute humaine requise, absence de captation et d'essai terrain, statut des items `a_revoir`, aucune publication/qualification/certification technique ou institutionnelle.
