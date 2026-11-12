# 06 — Erreurs, reprises ciblées, transfert et rappel différé

## Tableau des erreurs et rétroactions activables

| Erreur observable | Feedback descriptif | Reprise ciblée | Contre-vérification sur un nouveau cas |
|---|---|---|---|
| `2/8 + 3/8 = 5/16` | « Ta somme change la taille des parts alors que la bande reste divisée en huit. » | Marquer cinq cases d'une même bande de huit, recompter le tout. | `1/6 + 3/6 = 4/6` sur une bande neuve. |
| Une case plus grande traitée comme `1/4` | « Les quatre parts n'ont pas la même mesure. » | Rediviser une bande de longueur fixe en quatre parts égales. | Identifier `1/5` sur cinq segments de même taille. |
| `5/8 − 2/8 = 7/8` | « Le dessin doit montrer deux marques **en moins**. » | Enlever physiquement deux marques parmi cinq. | `6/10 − 3/10 = 3/10`, contrôle par somme. |
| `5/6 = 2/6 + 2/6` | « Les groupes totalisent quatre marques, alors que cinq doivent rester. » | Partager cinq jetons identiques en groupes de deux et trois. | `4/8 = 1/8 + 3/8`. |
| Addition de quarts de touts différents | « La valeur d'un quart dépend de la grandeur du tout. » | Aligner deux rubans inégaux, désigner l'unité de chaque fraction. | Justifier pourquoi deux tiers de deux surfaces différentes ne forment pas automatiquement `4/3` d'une même surface. |
| Calcul juste sans contrôle | « Que peux-tu retirer ou recomposer pour retrouver le départ? » | Écrire puis dessiner l'opération inverse. | `3/5 + 1/5 = 4/5`; vérifier `4/5 − 1/5 = 3/5`. |

## T1 — Transfert : un parterre quadrillé (preuve de maîtrise A)

**Situation illustrée :** une **seule** parcelle rectangulaire est divisée en huit cases de **même aire**. Trois cases accueillent des fines herbes; deux **autres cases**, sans chevauchement, accueillent des fleurs; les trois restantes ne sont pas plantées. **Question :** quelle fraction de la parcelle est plantée? Dessine les huit cases, écris la somme et **vérifie**.

**Réponse vérifiable :** `3/8 + 2/8 = 5/8`; dessin final `[■■■■■□□□]` (ou équivalent avec groupes distingués par des symboles). Contrôle `5/8 − 2/8 = 3/8` et `5 ≤ 8`. Ne pas considérer deux parcelles différentes comme le même tout. **Variante contrôlée :** items `q-011`, avec domaine fini et corrigés générés par formules exactes.

## T2 — Transfert : un parcours balisé (preuve de maîtrise B)

**Situation illustrée :** un parcours **unique** de dix tronçons de **même longueur** constitue le tout. Le relevé indique sept tronçons comptabilisés; une correction retire trois tronçons de ce relevé. **Question :** quelle fraction du parcours reste comptabilisée après correction? Représente, calcule et **vérifie**.

**Réponse vérifiable :** `7/10 − 3/10 = 4/10 = 2/5` du parcours; dessin final `[■■■■□□□□□□]`. Contrôle `4/10 + 3/10 = 7/10`, et le retrait diminue la quantité. Éviter d'interpréter une distance physique négative : on modifie un relevé, pas la longueur réelle du parcours. **Variante contrôlée :** items `q-012`, avec domaine fini et corrigés exacts.

**Règle de maîtrise :** T1 et T2 sont des contextes **réellement différents** (aire d'un parterre vs longueur d'un trajet), présentés lors d'occasions distinctes sans indices; voir `evaluation/GRILLE_MAITRISE.md`. Un score cumulé seul ne suffit pas. Chaque item exige la correspondance entre illustration, opération et contrôle.

## Rappel différé et enrichissement

- **Après 3–7 jours :** sans corrigé visible, montrer `2/6 + 3/6 = 5/6` dans une bande commune et contrôler `5/6 − 3/6 = 2/6`; puis `5/8 − 1/8 = 4/8 = 1/2` avec un nouveau dessin.
- **Après 2–3 semaines :** décomposer `4/10 = 1/10 + 3/10` puis utiliser une nouvelle situation de bandes; noter les erreurs sans transformer un seul rappel en décision de maîtrise.
- **Enrichissement (optionnel) :** expliquer comment `5/10 = 1/2` sans changer la quantité; envisager d'autres décompositions positives, puis distinguer formellement `1/3 + 1/4` des additions compatibles, sans exiger sa résolution pour `crit-1`.

**Accessibilité et sécurité :** matériels propres et non coupants ou représentations numériques; descriptions textuelles des schémas, contrastes suffisants, aucune dépendance à la couleur. Les contextes sont fictifs, sans données personnelles et sans achat réel.
