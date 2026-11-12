# PLAN D'ÉVALUATION — qc-pri-us-007

## Table d'alignement
**Objectif invariant `obj-1` :** Décrire des aspects des sociétés inuites et leurs relations aux milieux nordiques. **Critère invariant `crit-1` :** Expliquer deux relations entre environnement et activités, avec sources. **Famille :** `qc-pri-us-007-ev-01`, mode privilégié *generee_sous_contraintes* rendu ici sous formes fixes et deux scénarios à variantes fermées. Tous les items relèvent du même objectif/critère/famille; aucune question sur une opinion ou identité d'élève.

| Item | Diffic. | Représentation | Notion et preuve attendue | Source(s) | Variation |
|---|---|---|---|---|---|
| q-001 | initial | fiche/carte verbale | quatre régions, territoire incluant eaux/glaces | S1 | fixe |
| q-002 | initial | texte court | deux activités côtières et portée | S2 | fixe |
| q-003 | initial | notice datée | autorité, date, limite | S2 | fixe |
| q-004 | initial | phrase à corriger | contre-stéréotype sourcé | S1 | fixe |
| q-005 | intermédiaire | fiche locale | météo/glace ↔ récoltes | S4 | fixe |
| q-006 | intermédiaire | projet communautaire | transmission contemporaine | S4 | fixe |
| q-007 | intermédiaire | parc géré conjointement | savoir du milieu ↔ conservation | S3 | fixe |
| q-008 | intermédiaire | comparaison | côtes vs gestion du parc | S2, S3 | fixe |
| q-009 | intermédiaire | vérification de faits | rapport vs inférence | S4 | fixe |
| q-010 | transfert | deux fiches | deux relations avec sources distinctes | S2, S4 | fixe |
| q-011 | transfert | carte verbale + deux fiches | **preuve A** : littoral, déplacements, ressources | S1, S2 | scénario A/B, seed 20010 |
| q-012 | transfert | dossier communautaire | **preuve B** : Hopedale, récolte et réponse communautaire | S4 | scénario A/B, seed 20021 |

## Barème commun et décision
Quatre dimensions évaluées **séparément** de 0 à 3 : (1) deux relations vérifiables; (2) sources et appui explicites; (3) contexte spatial/temporel et limites; (4) nuance, absence de raccourci dégradant. Voir descriptions et exemples dans `GRILLE_MAITRISE.md`. Chaque production de maîtrise doit obtenir au moins 2 dans chaque dimension et doit être réalisée sans indices de contenu. Si une des deux preuves échoue, aucune maîtrise actée; remédiation ciblée puis **nouvelle** preuve autonome. Les items q-001 à q-010 servent à diagnostiquer et entraîner, ne suffisent pas à déclarer la maîtrise. Ne pas remplacer une tâche argumentée par QCM.

## Variabilité et reproductibilité
- q-001 à q-010 : items **fixes** sans tirage.
- q-011 et q-012 : `mode=scenario_controle`; corpus de deux variantes **A/B** chacune, intégralement documentées dans `parametres.dossiers_et_corriges`; `index = seed % 2`; `0→A`, `1→B`. Stimuli, sources, corrigés **verrouillés** et sélection reproductible. Exemple q-011 seed 20010→A, seed 20011→B; q-012 seed 20020→A, seed 20021→B. Pas de nouvelles affirmations générées par IA; changement de corpus exige validation humaine. Les limites de variation sont inscrites pour chaque item.
- Il ne s'agit pas d'un moteur qui certifie automatiquement les interprétations : seule la sélection des variantes est déterministe. Rubrique évaluée par personne formée, preuve conservée hors du canon.

## Conditions de passation, sécurité et accessibilité
Prévoir deux moments, deux **contextes substantiellement différents** (régions côtières vs Hopedale); ne pas utiliser de fiche préparée pendant les preuves; fiches sources fournies lors des épreuves, mais **pas** de correction ni d'indices. Autoriser lecteur, texte agrandi, audio, dictée et temps supplémentaire sans changer les critères. Aucune sortie sur glace ou récolte; aucune recherche de récits sacrés/privés; aucune photographie ou carte tierce incluse. On évalue la capacité d'argumenter à partir de documents, pas la fluidité en lecture, l'accent, les croyances ou l'identité. Veiller à ne pas faire parler un élève inuit au nom de ses pairs. Sources S1–S5 et contraintes de droits dans `sources/REFERENCES_CONTENU.md`.

**Contrôle humain requis** : vérifier enjeux de représentativité, dates des sites mis à jour, précision des paraphrases et biais potentiels avant diffusion; statut `a_revoir` de chaque item.
