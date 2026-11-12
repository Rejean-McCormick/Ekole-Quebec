---
format: qc.learning-path/1.0
id: qc-pri-ma-005
titre: Estimation et arrondissement
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Produire une estimation défendable et arrondir selon un rang annoncé.
objectifs_secondaires: []
criteres_reussite:
- Estimer puis vérifier une quantité en signalant l’écart observé.
prealables_declares:
- qc-pri-ma-003
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-005-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-005`

**Discipline :** Mathématique · **vague :** 3 · **cadre :** contrat pédagogique interne v1.2, sans homologation PFEQ.

**Objectif `obj-1` immuable :** Produire une estimation défendable et arrondir selon un rang annoncé. **Preuve `crit-1` immuable :** Estimer puis vérifier une quantité en signalant l’écart observé.

**Convention locale explicite :** quantités entières non négatives; pour un arrondi à l'unité de rang `r` (`r=10,100,1000`), chiffre suivant ≥5 → choisir le multiple supérieur. Le symbole ≈ signale une approximation et ≠ une égalité exacte. Différence signée = estimation − valeur exacte; écart absolu = |différence|.

## 1. Intention et frontières

Enseigner à annoncer le **rang d'arrondi** et la **quantité estimée**, expliquer une stratégie compatible avec les unités, calculer ensuite la valeur exacte et annoncer l'écart. Une estimation défendable n'est pas toujours l'arrondi unique « le plus proche » : pour estimer une somme on peut arrondir les termes; il faut en préciser la méthode.

**Frontières :** ne pas confondre approximation avec calcul exact; ne pas faire d'estimations au cent près si le rang choisi est la dizaine; pas d'obligation d'une vitesse de calcul. `qc-pri-ma-003` (valeur de position) est le seul prérequis bloquant, diagnostic équivalent permis.

## 2. Notions et représentations

**Ordre de grandeur :** valeur approchée située à l'échelle plausible du résultat (des dizaines, des centaines…). Exemple : 487 objets ≈ 500 à la centaine.
**Arrondi :** valeur choisie selon le rang annoncé et la règle retenue : à la dizaine, 374 → 370; 375 → 380 (convention 5 vers le haut pour entiers positifs).
**Approximation :** nombre volontairement voisin de l'exact, noté ≈. Elle ne remplace pas la quantité vérifiée.
**Écart absolu :** |estimation − exact|, jamais négatif; différence signée : estimation − exact, utile pour dire surestimation ou sous-estimation.

Représentations : droite graduée entre deux multiples, paquets de 10 ou 100, tableau valeur exacte / estimation / différence, notation ≈. Exemples et pièges en module 01.

## 3. Préparation / diagnostic

**Pré requis :** `qc-pri-ma-003` (valeur de position et regroupements), avec passage autorisé par diagnostic attestant l'équivalence. Aucun autre verrou ni ordre conseillé.
**D1 :** placer 346 entre 300 et 400, repérer le rang des centaines; **D2 :** arrondir 65 à la dizaine, comparer 60 et 70 et justifier le choix (cas de milieu). Voir `02_DIAGNOSTIC.md` avec réponses et décision.

## 4. Enseignement guidé

**Modelage E1 :** 374 ≈ 370 à la dizaine, écart |370−374|=4 et direction sous-estimée.
**Modelage E2 :** 187+213 = 400 exactement; en arrondissant chaque terme à la dizaine, 190+210=400, écart 0; un écart nul est possible sans rendre l'arrondi illégitime.
**Modelage E3 :** 248+163 ≈ 250+160=410, calcul exact 411, écart 1, approximation légèrement inférieure. Toujours annoncer la stratégie, le rang et les unités. Démonstrations et contre-exemples module 03.

## 5. Pratique accompagnée

Trois exercices avec indices dégressifs : **G1 :** 462 à la centaine (repères 400/500, chiffre des dizaines); **G2 :** 275 à la dizaine (question-guide « quand le chiffre suivant vaut 5? »); **G3 :** 246 + 138, estimation par arrondi des termes à la dizaine sans indices au calcul final. Chaque exercice doit nommer l'estimation, l'exact, l'écart signé ou absolu et une phrase de plausibilité (module 04).

## 6. Pratique autonome

A1–A4 sans indices : comparer 748 à la centaine; estimer 328+146 à la dizaine; estimer 692−257 à la dizaine; estimer 44+58 à la dizaine. Corrigés et écarts en module 05.

**Maîtrise M-A :** inventaire de boîtes (addition) estimé et vérifié; **M-B :** billets disponibles après distribution (soustraction) estimés et vérifiés. Deux contextes distincts, pas de moyenne. Un choix de stratégie cohérent peut varier; la méthode adoptée doit être contrôlable et l'écart correctement calculé.

## 7. Feedback et erreurs typiques

Confusions ciblées : (1) arrondir à la dizaine mais regarder le chiffre des centaines → encadrer la position; (2) prendre 5 « vers le bas » → rappeler la convention et tracer la droite; (3) écrire « = » entre valeur approchée et exacte → utiliser ≈ et indiquer le rang; (4) rapporter un « écart de −6 » quand on demande l'écart absolu → calculer |estimation − exact|; (5) ignorer les unités ou sens soustraction → estimer puis vérifier par calcul.

Feedback = montrer **la première étape incorrecte**, faire corriger avec droite graduée, puis nouvel exemple, pas simple réponse modèle.

## 8. Évaluation formative et preuves

Famille `qc-pri-ma-005-ev-01`, `obj-1`, `crit-1`; type `paramétrique_controle` inchangé. Banque de 12 items, dont 6 paramétriques via **listes finies de cas**, paramètres et seed numérique reproductible. Algorithme d'arrondi défini et vérification indépendante des variantes; 2 preuves autonomes M-A (`q-011`) et M-B (`q-012`) dans des contextes distincts.

Grille : rang et stratégie annoncés, ordre de grandeur plausible, calcul exact, différence signée et écart absolu, justification; la maîtrise nécessite deux contextes avec autonomie, jamais un unique pourcentage.

## 9. Remédiation / enrichissement

Arrondi faux → droite entre multiples consécutifs; valeur de position fragile → revenir à `qc-pri-ma-003` via référence, sans copier. Écart faux → aligner estimation et valeur exacte sur une ligne puis soustraire. Sous-estimation/surestimation inversée → confronter les deux valeurs numériquement.

Transferts T1 (budget de livres) et T2 (approvisionnement de matériel) dans module 06; rappel différé à J+2 puis J+7; nouvelle quantité et rang déterminé.

## 10. Accessibilité

Présenter manipulations de paquets de 10/100, droites graduées graduées lisibles et textes courts. Autoriser lecture orale des consignes, calcul posé, calculatrice **pour vérifier le calcul exact après l'estimation** seulement si le but évalué reste le raisonnement sur les nombres; documenter l'adaptation. Ne pas imposer de contexte de consommation réelle ou d'informations privées. Les nombres et unités sont fournis; stratégies écrites, orales ou visuelles acceptées avec mêmes exigences de justification. Aucun calcul aléatoire non contrôlé.

## 11. Critères de sortie

**Sortie `crit-1` :** sur M-A et M-B, l'élève choisit un rang annoncé, fournit une estimation cohérente (et la stratégie), calcule précisément la quantité réelle et l'écart, explique le sens de cet écart, sans indices. La réussite sur un seul scénario ou la seule application d'une recette n'établit pas la maîtrise. Si différence entre estimé et exact est importante, elle peut être recevable si la stratégie/rang était défendable et l'écart justifié; les rubriques l'explicitent.

## 12. Références pédagogiques et limites

Fondations lues : gouvernance v1.2 (contrat, générateur, charte) et frame v1.2 de `qc-pri-ma-005`; exemples, variantes, données et contextualisations originaux. Les lois d'arithmétique et les algorithmes déterministes sont vérifiés localement; aucune source externe ni conformité détaillée PFEQ n'est revendiquée. Liste des contrôles réellement exécutés : `livraison/VALIDATION.md`. Revue humaine requise pour l'adéquation au niveau, les consignes et l'équité.
