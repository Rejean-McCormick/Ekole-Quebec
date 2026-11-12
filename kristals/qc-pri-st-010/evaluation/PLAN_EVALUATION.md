# Plan d'évaluation — `qc-pri-st-010-ev-01`

**Objet immuable :** `obj-1` — Construire un circuit très simple et distinguer circuit fermé et ouvert. **Critère immuable :** `crit-1` — Dessiner puis vérifier le fonctionnement d’un montage à basse tension. **Couverture :** 10 items (8 d'entraînement/formative + 2 preuves de maîtrise) tous explicitement liés à `obj-1`, `crit-1`, `qc-pri-st-010-ev-01` dans `BANQUE_ITEMS.json`.

| Item | Lien objectif/critère/famille | Difficulté | Représentation | Dimension dominante | Variabilité |
|---|---|---|---|---|---|
| q-001 | obj-1 / crit-1 / qc-pri-st-010-ev-01 | initial | deux schémas écrits | ouvert/fermé, prévision | fixe |
| q-002 | obj-1 / crit-1 / qc-pri-st-010-ev-01 | initial | section de fil décrite | conducteur/isolant | fixe |
| q-003 | obj-1 / crit-1 / qc-pri-st-010-ev-01 | initial | phrases à classifier | observation/prédiction/inférence | fixe |
| q-004 | obj-1 / crit-1 / qc-pri-st-010-ev-01 | intermédiaire | fiche de scénario | correction sûre d'état | catalogue fixe à trois états, seed 20261008 |
| q-005 | obj-1 / crit-1 / qc-pri-st-010-ev-01 | intermédiaire | dessin de boucle | qualité du schéma | fixe |
| q-006 | obj-1 / crit-1 / qc-pri-st-010-ev-01 | intermédiaire | critique de plan | sécurité et court-circuit | fixe |
| q-007 | obj-1 / crit-1 / qc-pri-st-010-ev-01 | intermédiaire | compte-rendu de panne | prudence inférentielle | fixe |
| q-008 | obj-1 / crit-1 / qc-pri-st-010-ev-01 | transfert | commande décrite | fonctionnement des commandes | catalogue fixe à trois états, seed 20261010 |
| q-009 (E1) | obj-1 / crit-1 / qc-pri-st-010-ev-01 | transfert | dessin + kit à interrupteur | 1re preuve autonome, coin lecture | fixe, aucune aide de fond |
| q-010 (E2) | obj-1 / crit-1 / qc-pri-st-010-ev-01 | transfert | dessin + kit à poussoir | 2e preuve autonome, atelier | fixe, aucune aide de fond |

## Rubrique, décision et couverture

Rubrique des E1/E2 : (1) boucle schématisée avec source/récepteur/commande et absence de court-circuit, (2) prédiction ouverte/fermée, (3) **vérification réelle des deux états**, (4) constat séparé de l'inférence, (5) comportement sûr. Chaque critère est **non compensatoire** pour les deux preuves; la maîtrise ne provient pas d'un score total. L'adulte vérifie la sécurité avant chaque séance, note les performances et arbitre la possibilité d'une adaptation équivalente lorsque la manipulation directe est inaccessible. Une preuve sur simulateur est documentée comme simulation; ne pas prétendre qu'un test physique a été fait.

Les items q-001 à q-008 permettent le diagnostic ciblé, mais leur réussite seule ne qualifie pas l'acquis. Les deux manifestations exigent deux scénarios autonomes distincts avec commandes différentes. En cas de non-réussite d'un maillon : remédiation ciblée, puis preuve renouvelée sur nouveau scénario documenté, sans réutiliser les mêmes items tels quels.

## Contraintes de variation et contrôle

- q-004 : `seed=20261008`, catalogue ordonné [ouvert, fermé, faux_contact], index `seed % 3`; corrigé correspondant à l'entrée sélectionnée. q-008 : `seed=20261010`, catalogue [poussoir_releve, poussoir_appuye, interrupteur_bascule], même règle.
- **Aucun calcul aléatoire ni génération IA ouverte.** Toutes les variantes sont des textes avec états explicitement vérifiés par logique booléenne (continuité, fonctionnement présumé intact), jamais des expériences de court-circuit ou de panne provoquée.
- Une variation ultérieure de contexte ou de commande requiert un nouveau catalogue revu, pas un mot substitué à l'aveugle. Énoncés, rubriques, matériels compatibles, niveaux et difficultés sont gelés dans la banque à revoir par un humain.

## Sécurité et accessibilité

Kit pédagogique 3 V nominal avec 2 AA, ampoule 3 V incandescente, douille, fils isolés et fiches protégées; piles installées par adulte uniquement, supervision et vérification avant activation. Aucun secteur, transformateur improvisé, pile bouton, DEL sans résistances adaptées, batterie lithium, aimant détachable, expérimentation de court-circuit ou défaut volontaire. Pour impossibilité d'accès au geste : commande adaptée, scribe neutre pour la trace et/ou simulateur étiqueté; décision d'équivalence prudente et explicitée par le réviseur sans abaisser le critère cognitif. L'accent, l'écriture manuscrite et l'expérience préalable ne sont pas notés.

**Statut :** banque rédigée, exemples de sélection contrôlés, mais non certifiée; validation de schéma, essais pratiques, durées et accessibilité individuelle à confirmer humainement.
