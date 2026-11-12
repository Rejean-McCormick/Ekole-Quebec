---
format: qc.learning-path/1.0
id: qc-pri-us-002
titre: Lire des cartes et se repérer dans l’espace
discipline_code: US
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Lire une carte à l’aide de son titre, sa légende et ses repères.
objectifs_secondaires: []
criteres_reussite:
- Localiser des lieux et justifier le parcours entre eux sur une carte.
prealables_declares: []
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-us-002-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-us-002`

**Discipline :** Géographie, histoire et éducation à la citoyenneté. **Titre :** Lire des cartes et se repérer dans l’espace. **État :** textes et items livrés pour revue humaine; aucune homologation au PFEQ. **Invariants :** `obj-1` — « Lire une carte à l’aide de son titre, sa légende et ses repères. »; `crit-1` — « Localiser des lieux et justifier le parcours entre eux sur une carte. »; famille `qc-pri-us-002-ev-01`.

## 1. Intention et frontières

La cible unique est **Lire une carte à l’aide de son titre, sa légende et ses repères.** La preuve exigée reste **Localiser des lieux et justifier le parcours entre eux sur une carte.** Les élèves doivent montrer **où** et **pourquoi** un trajet convient, non choisir au hasard une flèche. Plans schématiques fictifs, pas de déduction historique, de déplacement réel ou de comparaison de sociétés à évaluer. Pas de conformité PFEQ revendiquée.

## 2. Notions et représentations

**Carte** : représentation construite et partielle d’un espace, désignée par un **titre**. **Orientation** : flèche ou rose qui précise les directions, toujours vérifier `N ↑`; **symbole** : marque définie par la légende du plan; **échelle simple** : correspondance du modèle entre un déplacement horizontal/vertical et un nombre de mètres, jamais estimation du temps réel. **Repères** : coordonnées colonne-lettre / ligne-chiffre (`C2`). **Parcours** : cases voisines par un côté, jamais en diagonale, sans franchir une case `X/#`. **Justification** : référence aux signes, directions et mesures effectivement indiqués. Les cartes originales A et B sont définies dans `contenu/01_NOTIONS_ET_EXEMPLES.md`; les cartes C, D et E dans les exercices, et les cartes inédites F et G seulement dans la banque d’évaluation.

**Exemple 1** (carte A) : école A2 → B2 → B1 → bibliothèque C1 = 3 passages × 100 m = **300 m**, sans X en C2. **Exemple 2** (carte B) : station A3 → B3 → C3 → bibliothèque D3 = 3 × 150 m = **450 m** vers l’est. **Contre-exemple 1** : passer par C2 sur carte A franchit un bassin `X`, non permis. **Contre-exemple 2** : multiplier 4 cases par 100 m au lieu de compter 3 déplacements donne 400 m, incorrect. **Contre-exemple 3** : croire « nord toujours en haut » sans consulter la flèche. Corrigés et explications dans `contenu/01_NOTIONS_ET_EXEMPLES.md`.

## 3. Préparation / diagnostic

**Aucun `requires` entrant**; aucun ordre préalable conseillé pour cet ID. **Diagnostic D1** : carte A, retrouver titre, E en A2, B en C1, X = bassin. **Diagnostic D2** : carte B, station A3 vers bibliothèque D3 par B3–C3; est et **450 m**. Observer symbole, coordonnées, orientation, compte de déplacements. Acquis suffisant → raccourcir le modelage et tenter une tâche nouvelle, **sans** donner automatiquement la maîtrise. Erreur ciblée → micro-remédiation, pas blocage inter-Kristals. Détails et décisions dans `contenu/02_DIAGNOSTIC.md`.

## 4. Enseignement guidé

**teach-1** : expliciter Lire une carte à l’aide de son titre, sa légende et ses repères. Démontrer lentement Titre → Légende → Nord → Repères → Parcours → Échelle → Justification, carte A. Verbaliser la correction d’un passage interdit `C2` et dénombrer **3 déplacements, pas 4 cases**. Faire produire à l’élève une raison vérifiable, pas seulement « parce que c’est le chemin ». Contrôles : que signifie X ? pourquoi B2 est-il à l’est de A2 ? peut-on inférer une durée réelle ? Voir `contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

**guided-1** — G1 carte B station→hôpital : trois indices complets, corrigé `A3–A2–A1–B1`, **450 m**. G2 carte C départ→belvédère : seul indice facultatif sur les cases voisines, corrigé `A3–B3–C3–D3–E3`, **800 m**. G3 carte D parc→bibliothèque : aucun indice initial, comparer **200 m** à **300 m**, argumenter. Diminuer les indications; enregistrer les aides. Voir `contenu/04_PRATIQUE_ACCOMPAGNEE.md`.

## 6. Pratique autonome

**independent-1** — Quatre tâches résolubles sans aide de fond, cartes A, B, C, D : (A1) titre, symboles et parcours **300 m**; (A2) est, parcours **450 m**, limite du plan; (A3) repérer deux cases X d’une proposition et corriger vers l’accueil **800 m**; (A4) comparer deux trajets **200 m** et **300 m**. Corrigés et critères à `contenu/05_PRATIQUE_AUTONOME.md`. Ne pas présenter les mêmes tâches corrigées comme preuve indépendante.

## 7. Feedback et erreurs typiques

**error-1** : attribuer à un signe un sens sans légende; corriger avec la légende locale. Orientation déduite du haut de page plutôt que de la flèche → pointer N. Cases inversées → lire lettre puis numéro. Passage diagonal/obstacle → retracer case par case. Compter les cases au lieu des déplacements → segmenter. Distance confondue avec durée → décrire la limite du document. Contrôler une nouvelle production après feedback (`contenu/06_REMEDIATION_ET_TRANSFERT.md`).

## 8. Évaluation formative et preuves

**Famille** `qc-pri-us-002-ev-01`, **objectif** `obj-1`, **critère** `crit-1`, mode source `generee_sous_contraintes` opérationnalisé par **six items à scénarios contrôlés** et **quatre items fixes**. Banque : `evaluation/BANQUE_ITEMS.json` (10 items, 12 variantes explicites pour 6 items). Montrer où sont les lieux, quel trajet est valide, et justifier avec la légende, les directions, l’échelle et les limites. **Deux preuves distinctes** q-009 centre scientifique et q-010 centre sportif, **sans indices** et non déjà enseignées/corrigées au même élève. Maîtrise critériée, jamais sur un score unique; voir `evaluation/GRILLE_MAITRISE.md`. État : `a_revoir`.

## 9. Remédiation / enrichissement

Symbole → décodage légende; orientation → rose/N; quadrillage → voisins; échelle → nombre de segments; justification → affirmation + indices; limite → information présente/absente. Offrir ensuite une carte nouvelle. Enrichissement : comparer deux itinéraires valides et expliciter pourquoi une carte fictive ne renseigne pas l’état d’un sentier réel. **Lien `reinforces` sortant vers `qc-pri-ma-021`**, jamais exigence d’accès; liens des Kristals tiers pointant vers celui-ci ne sont pas des préalables de `qc-pri-us-002`.

## 10. Accessibilité

Une représentation du quadrillage **en texte linéaire** accompagne chaque plan; les coordonnées, la flèche nord et les symboles sont annoncés explicitement. Permettre zoom, relief/tactile, lecteur d’écran, lecture orale, cases sur carton; autoriser une réponse orale transcrite, chemin dicté ou dessiné. Ne pas évaluer acuité visuelle, motricité fine ou vitesse. Éviter émojis et contrastes de couleur comme seuls indices. Aucune sortie extérieure ni localisation personnelle requise. Garder exigence cognitive de lecture, localisation et justification.

## 11. Critères de sortie

1. Démontrer exactement **Localiser des lieux et justifier le parcours entre eux sur une carte.** sur deux cartes de contextes distincts.
2. Lire titre, légende et coordonnées; tracer un chemin continu évitant les cases interdites et calculer avec l’échelle annoncée.
3. Justifier avec indices de la carte, expliciter au moins une limite du document; agir **sans indice de fond** lors de chaque preuve.
4. Si une preuve manque ou si une correction a été montrée avant l’épreuve, statuer **non encore démontré**, enseigner le geste manquant et proposer un autre contexte contrôlé; ne pas inférer la maîtrise d’une note ni d’un âge.

## 12. Références pédagogiques et limites

**Convention cartographique vérifiée :** Ressources naturelles Canada (légende et échelle de cartes topographiques) et USGS (composantes d’une carte); liens, périmètres et dates de consultation dans `sources/REFERENCES_CONTENU.md`. **Dérivation** : règles du quadrillage, dénombrements exacts et parcours calculés sur des cartes **originales inventées**. **Fichiers de travail** : `contenu/` (six modules), `evaluation/` (plan, banque et grille), `livraison/` (manifeste et validation). La charte québécoise conserve une appellation de discipline, sans homologation PFEQ. Tous les exercices et preuves exigent revue humaine avant qualification; aucune donnée réelle ou trajet sûr n’est garanti.
