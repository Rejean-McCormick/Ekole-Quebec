# Sources, raisonnements dérivés et droits — `qc-pri-ma-011`

## Provenance et contrôles

### A. Sources réellement consultées, dans l'archive de travail (vérifiées comme disponibles)

1. `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` — autorité active sur méthode, diagnostic, deux preuves, mathématiques vérifiées et statut des items.
2. `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` — champs de famille, conditions de génération paramétrique déterministe, validation du corrigé, seed et revue.
3. `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` — « Mathématique », projection des années/cycles sans prétention d'homologation.
4. `registry/GRAPHE_PEDAGOGIQUE_202.json` — les deux relations de `qc-pri-ma-011` (`requires → qc-pri-ma-003`, `recommends_before → qc-pri-ma-010`).
5. `kristals/qc-pri-ma-011/authoring/PARCOURS.md` (**frame d'origine**) — YAML, objectif, preuve, 12 rubriques à enrichir sans altérer les IDs.
6. `kristals/qc-pri-ma-011/authoring/CONTRAT_PEDAGOGIQUE.json` (**frame d'origine**) — schéma natif, famille, limites, métadonnées canoniques.
7. `kristals/qc-pri-ma-011/authoring/ALIGNEMENT.md` et `BRIEF_REDACTION.md` — ancrage descriptif québécois et mandat de rédaction; ces fichiers ne sont pas modifiés.

Tous ces fichiers existent **dans** `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` de l'archive source fournie. Le fichier ZIP livré n'en réédite aucun autre que les deux fichiers authoring demandés. Pas de consultation externe nécessaire pour les propriétés arithmétiques élémentaires présentées; ne pas transformer les références méthodologiques EEF/CAST citées par la frame en « consultation et validation scientifique » nouvelle.

### B. Raisonnements arithmétiques dérivés et contrôlés

- **Échanges :** `10 U = 1 D`, `10 D = 1 C`; transformations distributives conservant la valeur (`602=5×100+9×10+12`).
- **Règles inverses :** si `s=a+b`, alors `s−b=a`; si `d=a−b` avec `a≥b`, alors `d+b=a`; si `p=a×b` alors `p` est la somme de `b` copies de `a` et éventuellement `p÷b=a` pour `b≠0`.
- **Contrôle du calcul :** toutes les paires des jeux de la banque ont été parcourues, avec solutions par nombres entiers, fausses copies obtenues par formules documentées et contre-vérifications exactes par opérations inverses. Le rapport `livraison/VALIDATION.md` précise ce qui a été réellement exécuté.
- Les critères de « premier faux pas » sont définis par le gabarit d'erreur du jeu fermé. La cohérence didactique de ces gabarits nécessite une revue humaine distincte.

### C. Productions originales et droits

Exemples 268+157, 602−175 et autres chiffres, copies fictives avec première erreur, tableaux, exercices, scénarios de livres et billets, rubriques, rétroactions et algorithmes de génération ont été **rédigés pour ce module**. Aucun texte d'exercice externe, visuel propriétaire, citation attribuée, marque, personnage ou jeu de données personnel n'est reproduit. Les scénarios et quantités de bibliothèque/centre sont fictifs, non des observations sur un établissement réel.

**À vérifier avant diffusion :** licence interne applicable au projet et règles locales d'attribution; revue humaine des termes, du niveau cognitif, de la lisibilité, et, le cas échéant, conformité des adaptations d'accessibilité. Aucun droit de tiers n'a été déclaré acquis sans vérification.
