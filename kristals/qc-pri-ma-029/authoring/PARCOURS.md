---
format: qc.learning-path/1.0
id: qc-pri-ma-029
titre: Volume et unités de volume
discipline_code: MA
statut: contenu_redige_revue_requise
revision_contenu: 0.3.0
langue_contenu: fr-CA
resultat_principal: Déterminer un volume par comptage ou structuration d’unités cubiques.
objectifs_secondaires: []
criteres_reussite:
- Évaluer le volume d’un assemblage de cubes en montrant le comptage.
prealables_declares:
- qc-pri-ma-022
- qc-pri-ma-025
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-029-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-029`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Volume et unités de volume  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**Statut :** contenu rédigé, items contrôlés par calcul, revue humaine requise; non certifié, non homologué.

## 1. Intention et frontières

- `obj-1` — **Objectif immuable :** Déterminer un volume par comptage ou structuration d’unités cubiques.
- `crit-1` — **Preuve immuable :** Évaluer le volume d’un assemblage de cubes en montrant le comptage.
- **Notions :** espace occupé, cube unité, couche. Compter des cubes de même taille, utiliser rangées × colonnes × couches ou additionner des couches inégales. Justifier tout cube masqué.
- **Frontière :** des cubes unitaires entiers, sans trou implicite dans une couche annoncée pleine; distinguer cm³, cube unité, aire en carrés, capacités en litres. Les solides non cubiques, le déplacement d’eau et les formules de cylindres sont hors cible.
- **Graphe :** `requires` stricts `qc-pri-ma-022` et `qc-pri-ma-025` ; aucun `recommends_before`, aucun `reinforces`. Une preuve diagnostique d’équivalence évite de forcer un cours préalable.

## 2. Notions et représentations

- **Espace occupé / volume** : mesure tridimensionnelle de la place prise par un solide, exprimée par le nombre de cubes unitaires sans chevauchement et sans vide à l’intérieur du modèle annoncé.
- **Cube unité** : petit cube de référence de même taille que les autres de l’assemblage. Si son arête mesure 1 cm, son volume est 1 cm³. Si elle mesure 2 cm, son volume est 8 cm³ : trois tels cubes représentent 24 cm³, bien que le **comptage** soit 3 cubes.
- **Couche** : ensemble des cubes occupant un même niveau vertical. Une couche complète de L colonnes par P rangées compte L × P cubes; des couches incomplètes peuvent différer.
- **Schéma contrôlé** : chaque niveau est fourni par un tableau de P rangées, chaque rangée de L cases, `■` = 1 cube et `·` = absence. La position est déclarée pour que les cubes cachés soient déterminables.
- **Trois représentations** : matériau manipulable → plans couche par couche → somme ou produit avec unité. Une vue en perspective sans information sur les faces cachées ne permet pas toujours un résultat unique.
- **Exemples/contre-exemples** détaillés dans `contenu/01_NOTIONS_ET_EXEMPLES.md`.

## 3. Préparation / diagnostic

- Matériel : cubes emboîtables identiques ou reliefs tactiles sécuritaires; cartons en grille, images lisibles et cubes dessinés; pas de pièce assez petite pour être avalée par un enfant vulnérable; ne pas imposer de manipulation fine.
- `diag-1` : une rangée de quatre cubes visibles identiques, puis deux rangées de trois; montrer 4 puis 6 cubes avec organisation, sans simple réponse devinée.
- `diag-2` : reconnaître le cube unité et distinguer la surface de 6 carrés sur une face de 2 couches de 6 cubes; obtenir 12 cubes au total.
- Vérifier séparément les deux liens `requires` (solide et ses représentations; grandeur/unité) : l’élève qui démontre la compétence équivalente peut poursuivre directement. Si difficulté, soutien ciblé, pas de blocage automatique d’âge ou de classe.

## 4. Enseignement guidé

- `teach-1` : annoncer l’objectif et préparer une base de 3 colonnes × 2 rangées de cubes identiques : 3 × 2 = 6 cubes. Ajouter une deuxième couche **complète** : 6 + 6 = 12 cubes.
- Montrer les 2 plans de niveau `[■■■ / ■■■]` et `[■■■ / ■■■]` (deux rangées par couche), puis noter `2 × (3 × 2) = 12 cubes unités`. Chaque `■` est une place occupée; aucun cube compté deux fois.
- **Vérification :** « Qu’est-ce qui prouve qu’il y a 6 cubes cachés au premier niveau quand on regarde d’en haut ? » — le plan annonce explicitement une couche complète. L’apparence seule ne suffit pas.
- **Contre-modèle :** faire `3 + 2 + 2 = 7` additionne des longueurs de disposition, pas les cubes; revenir à un plan de niveau puis grouper.

## 5. Pratique accompagnée

1. `guided-1` : forte aide, 2 × 2 carrés sur une seule couche → 4 cubes, puis une deuxième couche → 8; indices de comptage un à un, puis `4 + 4`.
2. `guided-2` : aide moyenne, 3 rangées de 2 cases pleines × 2 niveaux → 6 + 6 = 12; élève choisit addition ou multiplication, l’adulte retire les flèches de repérage.
3. `guided-3` : aide minimale, couche inférieure `[■■■ / ■■■]`, couche supérieure `[■■■ / ···]` → 6 + 3 = 9, sans produit `3 × 2 × 2` car le niveau supérieur est incomplet.

Retrait effectif des indices, fiches et rétroactions explicites dans `contenu/04_PRATIQUE_ACCOMPAGNEE.md`.

## 6. Pratique autonome

- `independent-1` à `-4` : dénombrer couches pleines, couches inégales, comparer deux formes de même volume et conserver les unités avec cubes de 2 cm d’arête (`contenu/05_PRATIQUE_AUTONOME.md`).
- Pour chacune : montrer **les unités comptées** et la somme ou le produit vérifiable, et nommer le cube unité; la réponse numérique seule n’est pas suffisante.
- Deux contextes d’évaluation inédits : `q-009` entrepôt de blocs (pavé complet) et `q-010` maquette de gradins (2 couches non uniformes). Ils ne répètent pas les exercices d’entraînement.

## 7. Feedback et erreurs typiques

| Observation | Question ou rétroaction descriptive | Remédiation |
|---|---|---|
| Compte les carrés visibles | « Comptons-nous des faces ou des cubes entiers ? » | Dessiner la coupe des niveaux pour montrer les cubes cachés. |
| Compte un cube deux fois | « À quel niveau appartient-il ? » | Marquer chaque cube une fois sur son plan de couche. |
| Multiplie par un nombre de couches malgré des trous | « Les niveaux sont-ils complets et identiques ? » | Additionner le nombre de `■` niveau par niveau. |
| Écrit `12 cm²` | « Une face carrée est-elle un espace en trois dimensions ? » | Expliciter cube unité versus carré unité; `12 cm³` si arête 1 cm. |
| Écrit `3 cm³` pour trois cubes de 2 cm d’arête | « Combien de petits cm³ forme chaque cube de référence ? » | Décomposer chaque cube en `2 × 2 × 2 = 8 cm³`; calculer `3 × 8`. |
| Une perspective ambiguë | « Peut-on déterminer les cubes cachés sans plan ? » | Exiger une vue de dessus par couche ou ajouter « niveaux complets ». |

## 8. Évaluation formative et preuves

- Famille native `qc-pri-ma-029-ev-01`, `obj-1`, `crit-1`, type `paramétrique_controle`. Banque : 10 items, dont deux **paramétriques déterministes** (009, 010), sans générateur IA libre.
- `q-009` : `L=2+seed%3`, `P=2+(seed//3)%2`, `H=2+(seed//6)%2` ; chaque couche L×P est pleine, `V=L×P×H`. Le matériel précise l’invisibilité des couches inférieures.
- `q-010` : `L=3+seed%2`, `P=2+(seed//2)%2`; couche basse pleine L×P, couche haute une seule rangée complète de L; `V=L×P+L`. Matrice explicitement fournie.
- Seed entier stable et valeurs calculées enregistrées dans chaque item; validation indépendante par énumération de positions `(x,y,z)`. Aucun changement de formule ou d’unité autorisé sans nouvelle vérification.
- Maîtrise établie **sur les deux épreuves indépendantes**, avec volume juste et procédé de comptage retracé, sans indice directif; le score global n’efface pas l’absence d’un critère. Voir grille.

## 9. Remédiation / enrichissement

- Si oublis de cubes masqués : manipuler le modèle transparent ou représenter une couche par grille; refaire avec une deuxième disposition nouvelle.
- Si produit inadapté à une couche trouée : `6 + 3`, pas `6 × 2`; nouvel assemblage de 2 couches inégales.
- Si confusion unités : choisir clairement « 1 cube unité » versus « cm³ », illustrer 2 cm → 8 cm³, ne pas multiplier 3 cubes par 2.
- Enrichissement : trouver deux assemblages différents de même volume, prouver par listes de niveaux; ne pas introduire de nouveau préalable.
- Deux transferts : gestion de matériel en entrepôt fictif et préparation d’une maquette de musée, décrits dans `contenu/06_REMEDIATION_ET_TRANSFERT.md`.
- **Rappel différé :** à une séance ultérieure, sans modèle, deux niveaux de cubes comptés; plus tard, une couche trouée à reconstruire, puis feedback sur le premier calcul erroné.

## 10. Accessibilité

- Produire les niveaux en gros caractères (`■`/`·` avec légende), en relief, par lecture orale linéaire ou par tableau accessible; demander toujours le même raisonnement.
- Réponse écrite, dictée, pointage ou communication assistée recevable; les difficultés de motricité fine, de perception visuelle ou d’écriture ne constituent pas la grandeur mathématique évaluée.
- Un adulte peut manipuler sur instruction précise de l’élève (sans choisir les cubes ni le regroupement à sa place). Le matériel doit être stable, sans petit objet dangereux; pas d’obligation de photographie, vidéo ou collecte personnelle.

## 11. Critères de sortie

1. Dire ou montrer quelle unité cubique est comptée et pourquoi l’unité est cubique.
2. Compter toutes les positions occupées, y compris celles cachées; documenter la séparation en couches ou la structure d’un pavé complet.
3. Indiquer un calcul vérifiable et le bon total, avec unité exacte.
4. Réussir **deux contextes différents** `q-009` et `q-010`, sans aides sur la méthode durant l’épreuve; considérer séparément les deux preuves.
5. Si un obstacle d’accessibilité empêche de conclure, consigner la preuve « non concluante » et adapter sans inférer une non-maîtrise.

## 12. Références pédagogiques et limites

- Sources internes lues : norme et générateur/examens v1.2, charte Québec, graphe v1.2, et fichiers source `PARCOURS`, `CONTRAT_PEDAGOGIQUE`, `ALIGNEMENT`, `BRIEF_REDACTION` du seul Kristal.
- Source externe vérifiée : NIST, *SI Units – Volume*, https://www.nist.gov/pml/owm/si-units-volume ; définition du volume comme espace en trois dimensions et unités cubiques.
- Source externe vérifiée : CAST (2024), *UDL Guidelines 3.0 – Action & Expression*, https://udlguidelines.cast.org/action-expression/ ; options de réponses sans changer la cible mathématique.
- Les nombres, contextes, grilles, corrections et seuils de maîtrise sont des créations originales, vérifiables par calcul; ils ne sont pas présentés comme textes ministériels.
- Limitations : revue scientifique et pédagogique humaine, essais de lisibilité et d’accessibilité, aucune homologation PFEQ, aucune certification d’item. Voir `sources/REFERENCES_CONTENU.md` et `livraison/VALIDATION.md`.
