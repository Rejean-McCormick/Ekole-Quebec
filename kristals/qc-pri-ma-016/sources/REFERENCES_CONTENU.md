# Provenance et droits — qc-pri-ma-016

## Sources internes effectivement consultées dans l'archive fournie

Les chemins ci-dessous correspondent au dossier maître `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, **pas** à des pièces incluses dans le présent delta.

1. `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` : frontières de gouvernance, méthode diagnostic → enseignement → autonomie, preuve dans deux contextes et absence d'homologation présumée.
2. `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` : champs de famille, trois modes, seed reproductible et revue humaine des items.
3. `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` : discipline Mathématique comme appellation québécoise, non comme revendication de conformité PFEQ.
4. `registry/GRAPHE_PEDAGOGIQUE_202.json` : seule relation sortante `qc-pri-ma-016 requires qc-pri-ma-015`; aucune relation conseillée ou de renforcement sortante.
5. `kristals/qc-pri-ma-016/authoring/PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md` : titre, identité, objectif/proof immuables, notions et structure originale v1.2.

**Précision :** « vérifiées » signifie que ces pièces étaient physiquement lisibles et que leurs mentions ont été contrôlées contre l'archive. Cela ne constitue pas un audit indépendant de leurs fondements scientifiques ni une consultation des liens externes.

## Raisonnements mathématiques dérivés (sans source externe revendiquée)

- Par la valeur de position en base dix : `u,d c = 100u + 10d + c` centièmes; `2,5 = 2,50` car `250 = 250` centièmes; comparer deux entiers de centièmes avec une unité identique préserve l'ordre.
- Addition et soustraction des centièmes représentent des calculs exacts; emprunt et retenue modifient l'écriture du nombre sans sa valeur. Pour des opérandes positifs `a,b`, l'addition donne un résultat supérieur à chaque terme; pour `a≥b`, la différence est non négative et `a-b+b=a`.
- Bornes et inverses sont des justifications de plausibilité; elles ne sont pas un « score » autonome sans observation du sens de l'opération. Les cas paramétriques ont été testés par entiers de centièmes et vérification croisée `decimal.Decimal`.

## Productions originales et licences

- Toutes les leçons, tableaux textuels, situations fictives (marché, marche, rubans, contenants), corrections et rubriques du présent delta ont été rédigés spécifiquement pour ce Kristal; pas de textes tiers copiés, photographie, image, audio, police ou document externe inclus.
- La présence de noms d'unités (dollars fictifs, kilomètres, litres) n'implique pas de marques, jeux propriétaires ou médias sous licence.
- **Droits :** absence de ressources tierces embarquées vérifiée sur le contenu de cette livraison; aucun avis juridique sur le dépôt maître, la propriété globale du projet ou les politiques des établissements n'a été rendu.
- **Non vérifié :** sources en ligne, citations littérales externes, licences de l'infrastructure hôte; ne pas inventer de validation de droits, de source scientifique externe ou de conformité gouvernementale.
