# Plan d'évaluation — qc-pri-ma-010 / `qc-pri-ma-010-ev-01`

## Cibles invariantes
- **`obj-1` :** Choisir une stratégie de calcul mental et mobiliser une propriété opératoire.
- **`crit-1` :** Comparer deux stratégies mentales et expliquer laquelle convient le mieux.
- **Type principal v1.2 :** `paramétrique_controle` — famille globale mixte : ancrages fixes, quatre variantes à paramètres déterministes, deux scénarios de maîtrise verrouillés. **Statut de tous les items : `a_revoir`.**

## Couverture et administration
Chaque item renvoie au même objectif et au même critère; aucune performance de vitesse n'est notée. `q-001` à `q-006` diagnostiquent et étayent; `q-007` à `q-010` vérifient des variantes bornées; **q-011 et q-012 sont les deux preuves sommatives locales distinctes**, idéalement sur deux séances après retrait des appuis.

| Item | Niveau | Mode | Représentation | Concept / comparaison attendue | Utilisation |
|---|---|---|---|---|---|
| q-001 | initial | fixe | notation | commutativité, décomposition | formative |
| q-002 | initial | fixe | cartes/nombres | échange puis regroupement | formative |
| q-003 | intermédiaire | fixe | dizaines/unités | compensation d'une somme | formative |
| q-004 | intermédiaire | fixe | droite numérique | compensation d'une différence | formative |
| q-005 | intermédiaire | fixe | critique d'erreur | soustraction non commutative | formative |
| q-006 | intermédiaire | fixe | parenthèses | soustraction non associative | formative |
| q-007 | intermédiaire | paramétrique | trois termes | associativité, paire à 100 | formative |
| q-008 | intermédiaire | paramétrique | deux collections | transfert de k unités | formative |
| q-009 | intermédiaire | paramétrique | deux repères | augmentation égale de l'écart | formative |
| q-010 | transfert | paramétrique | quatre termes | groupements à 100 | formative/enrichissement |
| q-011 | transfert | scénario contrôlé | kiosque / quantité | comparer décomposition et compensation additive | **preuve 1** |
| q-012 | transfert | scénario contrôlé | sentier / distance | comparer correction et compensation soustractive | **preuve 2** |

## Variabilité permise et contrôle
- **Ancrages q-001 à q-006 :** nombres, énoncés, corrigés et critères fixes; seule la modalité de réponse et l'ordre de présentation sont adaptables.
- **Paramétriques q-007 à q-010 :** `seed` entier non négatif; générateurs `p-assoc`, `p-comp-somme`, `p-comp-diff`, `p-quatre-termes` documentés dans le JSON banque et le contrat auteur. Divisions entières `//` et reste `%`; les instances livrées utilisent les seeds **137, 428, 515, 772** et possèdent un corrigé calculé. Pas d'IA libre et pas de variation des opérations, critères ou résultats hors formule. Un changement de seed implique **recalcul et validation indépendante de la nouvelle instance** avant administration.
- **Preuves q-011 et q-012 :** deux situations originales fixes, aucune substitution de scénario non approuvée. Vérifier le sens de l'unité (fruits, mètres) et les deux méthodes proposées.
- **Limites mathématiques :** nombres naturels; pas de changement de signe illicite, de soustraction à ordre inversé ni d'associativité inventée. Les préférences stratégiques peuvent varier quand le calcul et l'argument sont cohérents.

## Critères et barème
Quatre axes 0–2 chacun (8 au maximum par item) : (1) exactitude du résultat et unité; (2) validité des deux démarches/propriété utilisée, y compris détection d'une démarche fausse; (3) comparaison réelle des démarches; (4) choix et raison mathématique contextualisée. Les niveaux détaillés et la décision multi-preuves sont dans `GRILLE_MAITRISE.md`.

## Sécurité, biais, accessibilité et indépendance
- Aucune performance physique, vitesse, achat réel ou opinion personnelle exigés; vocabulaire contextualisé expliqué. Les scénarios sont fictifs et ne révèlent aucune donnée de l'élève.
- Lire à haute voix les consignes ou offrir notation large, schéma textuel, matériel adapté *pendant l'apprentissage*, réponse orale/écrite/dictée. Pour les preuves autonomes, aide à l'accès seulement : aucune suggestion sur le `+k/−k`, le regroupement, le résultat ou la préférence.
- Enregistrer la trace de raisonnement dans l'outil pédagogique éventuel, pas dans les champs du canon du Kristal.
- Après indice/erreur : feedback descriptif, entraînement sur **autre item** et preuve inédite; ne pas transformer un essai assisté en preuve autonome.

## Décision
**Ne jamais déduire la maîtrise d'une note unique.** Les deux preuves indépendantes (addition d'inventaire et soustraction spatiale) doivent satisfaire chacune les critères de la grille, sans procédure soufflée; sinon remédiation ciblée puis deux nouveaux contextes revus. Validation humaine et essais nécessaires avant publication.
