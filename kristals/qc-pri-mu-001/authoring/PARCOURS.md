---
format: qc.learning-path/1.0
id: qc-pri-mu-001
titre: Percevoir les sons, leurs qualités et les silences
discipline_code: MU
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Discriminer sons et silences selon des propriétés audibles.
objectifs_secondaires: []
criteres_reussite:
- Classer des extraits sonores selon deux critères expliqués.
prealables_declares: []
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-mu-001-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-mu-001`

**Discipline (appellation québécoise) :** Musique  
**Titre :** Percevoir les sons, leurs qualités et les silences  
**Norme active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**Statut de cette rédaction :** contenu préparé pour revue humaine; pas un cours publié ni un examen homologué. Les métadonnées YAML sont reprises sans changement de la frame.

## 1. Intention et frontières

- **`obj-1` (immuable) :** Discriminer sons et silences selon des propriétés audibles.
- **`crit-1` (preuve autonome immuable) :** Classer des extraits sonores selon deux critères expliqués.
- Notions : **durée, intensité, hauteur, timbre, silence**; utiliser un langage accessible (« court/long », « doux/plus marqué », « grave/aigu », « sonorité », « pause sans son intentionnel ») sans effacer les distinctions.
- Ce parcours vérifie l'attention portée à ce qui est entendu, non l'habileté vocale, le jugement esthétique, le diagnostic auditif, la notation sur portée ou la connaissance d'instruments.
- **Préalables stricts : aucun; ordre suggéré : aucun; liens de renforcement : aucun.** Le registre possède toutefois des liens entrants de Kristals ultérieurs vers celui-ci; ne modifier aucun autre ID.
- Tout classement est jugé d'après des **stimuli effectivement produits et contrôlés**. Les descriptions de production ne sont pas des enregistrements déjà vérifiés.

## 2. Notions et représentations

- **Son :** vibration produisant une sensation sonore, si perceptible dans les conditions d'écoute. Un événement sonore peut être bref ou long, plus ou moins intense, grave ou aigu, et avoir un timbre particulier.
- **Durée :** intervalle entre début et fin du son; ex. 0,40 s contre 1,40 s à hauteur et timbre identiques. Ne pas confondre durée et intensité.
- **Intensité perçue :** impression relative « plus doux/plus marqué » dans une comparaison contrôlée. L'amplitude du fichier ne garantit pas à elle seule un niveau sonore sûr ou une impression identique sur chaque appareil.
- **Hauteur :** grave/aigu; pour des sons périodiques simples, liée à la fréquence fondamentale (p. ex. 330 Hz contre 660 Hz), pas au volume.
- **Timbre :** qualité sonore qui aide à distinguer deux sources ou formes d'onde à hauteur et durée comparables; ne pas déduire le timbre de la seule intensité.
- **Silence :** intervalle prévu **sans signal sonore intentionnel**; il n'exige pas un monde totalement silencieux. Une fin de note n'est pas automatiquement une pause *au milieu* d'un motif.
- Représentations : écoute et verbalisation → cartes de critères et ligne du temps → imitation sûre de courtes suites → classement croisé (deux critères) → justification par indice audible.
- Support opérationnel : `contenu/01_NOTIONS_ET_EXEMPLES.md` contient le catalogue original D/E/G/P/Q/U/S/A/B/X/R, les recettes temporelles et un générateur WAV optionnel en Python standard; aucun enregistrement tiers n'est nécessaire.
- **Exemple commenté A :** E1 (0,50 s, doux) vs E4 (1,50 s, marqué) : ils diffèrent **sur deux axes**; les mettre seulement dans « longs » oublie l'intensité. E1 = court + doux, E4 = long + marqué.
- **Exemple commenté B :** S1 contient un silence de 0,60 s **entre** deux notes; S2 est continu pendant 1,60 s à la même hauteur. Réponses : S1 = pause interne; S2 = pas de pause interne. Les sons B de l’évaluation ne sont pas enseignés.
- **Contre-exemple 1 :** « Le son est aigu parce qu'il est fort » est faux : hauteur et intensité sont distinctes.
- **Contre-exemple 2 :** « Il y a silence quand la note est douce » est faux : une note faible mais audible reste un son.

## 3. Préparation / diagnostic

**Sans prérequis bloquant.** Fournir des écoutes à niveau modéré, offrir réécoute et vérifier l'accès à un mode d'écoute exploitable.

- `diag-1` : faire entendre D1 (1,20 s) et D2 (0,40 s), sons de même hauteur, timbre et niveau; demander « lequel dure davantage ? » et une justification (début/fin). Réponse attendue : D1.
- `diag-2` : faire entendre D3 (deux notes séparées par 0,60 s sans signal intentionnel) et D4 (note continue); demander de montrer la pause avec deux cartes « son / silence ». Réponse : D3 contient une pause interne, D4 non.
- `diag-3` (facultatif, découverte) : comparer Q1 grave et Q2 aigu, en indiquant sans vocabulaire spécialisé ce qui diffère; ne pas traiter une hésitation de lexique comme incapacité perceptive.
- **Décision :** si l'apprenant classe correctement deux séries de quatre extraits et explique deux critères sans aide, recueillir des preuves autonomes dans deux contextes nouveaux avant de constater la maîtrise; sinon choisir la microleçon appropriée. Une difficulté à entendre conduit à une adaptation/évaluation spécialisée, **pas** à un verdict scolaire d'incapacité.
- Voir `contenu/02_DIAGNOSTIC.md` pour protocole, barème descriptif et décisions.

## 4. Enseignement guidé

**`teach-1` :** annoncer l'objectif tel quel; donner le sens de *deux critères expliqués* : une même vignette reçoit **deux étiquettes**, accompagnées d'un indice d'écoute pour chaque axe.

1. Écouter **E1** et **E2**, même hauteur, timbre et niveau : « E1 se termine avant E2 → court/long ».
2. Écouter **E1** et **E3**, même durée, hauteur et timbre : « E3 paraît plus marqué au même réglage → doux/marqué ».
3. Établir une matrice 2 × 2 : E1 = court/doux; E2 = long/doux; E3 = court/marqué; E4 = long/marqué. L'enseignant place E1 en pensant à voix haute, puis demande une justification de E4.
4. Montrer S1 puis S2 : seule la piste S1 contient un silence **entre** deux sons. Suivre une ligne du temps « son – silence – son ».
5. Montrer U1 et U2 : même note, mêmes durée et amplitude numérique, forme d'onde différente; discuter le **timbre**, sans imposer un jugement affectif.
6. Contrôle immédiat : « Pourquoi E2 est-il long sans être forcément plus fort ? » / « Un son très doux est-il un silence ? » Réponses : la durée ne commande pas le niveau; non.

Le modelage est une démonstration **de méthode**, et non une preuve de maîtrise de l'élève. Voir `contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

- `guided-1` (indices forts) : G1–G4, trier d'abord par durée avec deux cartes « court/long », ensuite par intensité « doux/marqué ». Faire verbaliser « j'ai entendu que… ». Grille prévue : G1 court/doux, G2 long/marqué, G3 long/doux, G4 court/marqué.
- `guided-2` (indices réduits) : présenter P1, P2 et P3 dans un ordre annoncé uniquement au correcteur; l'élève place chaque son dans la matrice vide et explicite deux indices; au besoin autoriser un seul rappel « pense aux deux axes ».
- `guided-3` (sans indice sur l'axe) : jouer S1, S2, puis Q1/Q2; questionner sur présence d'une pause et sur grave/aigu avec un échange collaboratif où chacun peut répondre en parole, geste ou cartes.
- **Retrait progressif :** modèle complet → intitulé des axes → matrice vide → classement expliqué de mémoire. Après erreur, faire réécouter en ne faisant varier **qu'un paramètre à la fois**. Activités/solutions détaillées dans `contenu/04_PRATIQUE_ACCOMPAGNEE.md`.

## 6. Pratique autonome

- `independent-1` à `independent-4` : quatre tâches sans indice direct ni solution affichée, utilisant des extraits distincts des démonstrations (P, Q, U et S); exemples et rubriques dans `contenu/05_PRATIQUE_AUTONOME.md`.
- **Deux preuves formelles en contextes distincts :** `qc-pri-mu-001-q-009` — **atelier musical**, classer A1–A4 selon durée et intensité; `qc-pri-mu-001-q-010` — **jeu de signaux d'un jardin imaginaire**, classer B1–B4 selon hauteur et présence d'une pause interne. Les quatre combinaisons sont représentées dans chaque série.
- Pour chaque preuve, produire la matrice 2 × 2 complétée, les étiquettes de chacun des quatre extraits et **deux explications distinctes** appuyées sur les sons (une par critère). Sans aide de classement; consigne neutre et répétitions standardisées autorisées.
- Le correcteur vérifie la réalisation effective des fichiers WAV selon recette avant administration. Si stimuli non écoutés et validés, **ne pas compter la preuve**. Conserver traces uniquement dans le LMS ou dossier d'évaluation externe, jamais dans le canon.

## 7. Feedback et erreurs typiques

| Erreur repérée | Intervention descriptive | Nouvelle vérification |
|---|---|---|
| « long = fort » | Comparer E1/E2 à niveau identique, repérer fin du son | P1/P2 : distinguer uniquement la durée |
| « aigu = fort » | Comparer Q1/Q2 à niveau identique, ne parler que de hauteur | Autre paire de hauteur contrôlée, sans donner la clé |
| « doux = silence » | Faire entendre S2 continu à faible niveau et montrer qu'il y a signal | D3/D4 : localiser la pause interne |
| Confondre timbre et hauteur | U1/U2 : même fréquence, deux formes d'onde | Décrire différence de sonorité sans changer grave/aigu |
| Classer selon « j'aime » | Reformuler en indice audible et observation neutre | Nouvelle paire + justification par critère |
| Placer une seule étiquette | Donner une matrice à deux axes et verbaliser chaque choix | Quatre extraits inédits, sans rappel du professeur |

Des feedbacks complets et reprises figurent dans `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 8. Évaluation formative et preuves

- **Famille immuable :** `qc-pri-mu-001-ev-01`; **objectif :** `obj-1`; **critère :** `crit-1`; type : `observation_ou_production`.
- Banque contrôlée : 12 items (`evaluation/BANQUE_ITEMS.json`), tâches d'écoute ou productions documentées, jamais QCM de goûts; `evaluation/PLAN_EVALUATION.md` décrit les contraintes des stimuli, l'usage et les limites.
- Grille de sortie : sur **chacune** des séries A et B, au moins 3 extraits sur 4 correctement situés **sur les deux axes**, deux justifications distinctes correctes, démonstration d'autonomie et absence de difficulté auditive non résolue compromettant l'interprétation.
- Deux séries, deux contextes et deux couples de critères différents; ne pas remplacer le dispositif par une note unique, un hasard de réussite ou une seule exécution. Consigner les aménagements et la fiabilité des stimuli.
- Les réponses de référence décrivent la **recette attendue**; toute divergence sonore constatée à l'écoute impose le retrait de l'item, plutôt que de pénaliser l'élève.
- Statut : items `a_revoir`, revue humaine et essai nécessaires avant qualification.

## 9. Remédiation / enrichissement

- Remédiation minimale après diagnostic ou pratique : isoler un contraste (durée, puis intensité, puis hauteur, timbre, silence), poser une nouvelle paire et réévaluer **le même critère avec d'autres sons**. Pas de répétition aveugle du corrigé.
- Enrichissement sans nouveau préalable : décrire et composer un motif de quatre événements avec une pause intentionnelle; montrer quelles qualités restent stables et lesquelles changent. Une intention sonore (« signal doux, puis pause ») se vérifie par la trace, pas par « c'est beau ».
- **Transfert 1 :** panneau fictif de signaux X1–X4, deux critères hauteur/pause; autres fréquences que la preuve B et consignes nouvelles.
- **Transfert 2 :** brève « carte postale sonore » de classe, quatre événements joués avec la voix ou instrument adapté; classer les sons par durée/intensité, noter une pause et décrire l'organisation; aucune obligation de chanter juste.
- Rappel différé **après 3 à 7 jours** : R1–R4, changement d'ordre et de timbre, sans fiche visible; conserver séparément la trace et les corrections. Voir `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 10. Accessibilité

- Accepter réponses par parole, pictogrammes, pointage, classement de cartes, tableau tactile ou dictée à un tiers, tant que **l'apprenant** exprime réellement les critères.
- Utiliser des haut-parleurs calibrés à niveau confortable; éviter écouteurs imposés, sons soudains, niveaux élevés, longues expositions, stroboscopes, consignes mêlées au bruit. Offre de réécoute identique pour toutes et tous.
- Prévoir neutralisation du bruit de fond et contrôle du matériel avant l'évaluation; distinguer l'accès sensoriel (accès au son) de la compétence cognitive visée. Des descriptions textuelles, formes d'onde ou vibrations peuvent faciliter l'enseignement, mais **ne prouvent pas à elles seules** une discrimination *auditive*; déclarer honnêtement le type de preuve accessible et solliciter une adaptation compétente au besoin.
- Aucune note sur « belle voix », sensibilité auditive innée, volume maximal produit, goût, personnalité ou exposition à la musique familiale. L'évaluation porte sur classement, justification, organisation et écoute, et non sur la performance physique.
- Respecter le retrait volontaire en cas de douleur, acouphène, fatigue ou hyperacousie; ne jamais augmenter le volume pour forcer une réponse.

## 11. Critères de sortie

1. L'élève classe **autonomement** les quatre stimuli A selon **durée ET intensité** avec au moins 3/4 positions doubles correctes; deux raisons sonores correctes.
2. L'élève classe **autonomement** les quatre stimuli B selon **hauteur ET silence interne** avec au moins 3/4 positions doubles correctes; deux raisons sonores correctes.
3. Le matériel sonore et les pauses ont été préparés, validés localement et administrés dans des conditions accessibles et sûres; conserver les preuves de contexte, dates, consignes et adaptations.
4. Si l'une des deux preuves manque ou échoue, documenter le critère à renforcer, exercer un son nouveau puis refaire une **preuve renouvelée** sans réutiliser simplement le corrigé.
5. Prévoir un rappel différé non sommative; une erreur tardive déclenche consolidation, non annulation automatique de preuves antérieures.

## 12. Références pédagogiques et limites

- Autorité interne : `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md`; graphe : `registry/GRAPHE_PEDAGOGIQUE_202.json` (aucun « requires » entrant vers les ressources de ce Kristal).
- Présentation Québec : `authoring/ALIGNEMENT.md` déjà présent au workspace, **non compris dans la livraison**; pas de revendication de conformité, d'homologation ni de code de cours ministériel.
- Acoustique et santé : NIH/NIDCD, *How is Sound Measured?* (2025), *Noise-Induced Hearing Loss* (2025); voir les URL et la portée exacte dans `sources/REFERENCES_CONTENU.md`.
- Droits : les schémas de sons et le code de synthèse sont rédigés pour ce Kristal; aucun enregistrement externe, échantillon musical tiers ou autorisation implicite. Le vérificateur local doit encore examiner la diffusion de **tout** son éventuellement substitué.
- Limites non résolues : écoute et calibrage humain des WAV synthétisés, test d'accessibilité avec apprenants, révision des rubriques par spécialiste de musique, revue des droits pour toute future substitution, tests Framework/canon non exécutés. Qualification à poursuivre, **publication non autorisée par cette livraison**.
