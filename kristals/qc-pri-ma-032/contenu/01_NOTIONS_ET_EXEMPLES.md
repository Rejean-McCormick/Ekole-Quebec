# 01 — Notions, exemples résolus et contre-exemples

**Cible :** `obj-1` — Décrire des événements en termes de possibilité et de chance relative. **Preuve :** `crit-1` — Classer des événements et expliquer les conditions du classement.

## Départ : ce que signifie « au hasard »

Une *expérience aléatoire* est une expérience dont on ne connaît pas d'avance le résultat particulier. Une *issue* est un résultat individuel possible; un *événement* regroupe une ou plusieurs issues (ex. : « obtenir une carte rouge »). Une boîte dont on connaît tout le contenu permet de comparer les chances **avant** le tirage, même si le résultat reste inconnu.

Dans nos expériences, un tirage se fait **à l'aveugle**, après mélange, parmi des objets identiques par leur forme et leur taille; chaque objet a la même chance d'être sélectionné. Une roue dite équitable a des secteurs **égaux** et un mécanisme non biaisé. Si cette condition est inconnue, on ne peut pas simplement compter les objets ou les secteurs pour quantifier les chances.

### Quatre notions exactes

- **Certain :** se produit dans toutes les issues prévues par les conditions. Ex. : un ticket tiré de `A,A,B` porte `A ou B` (3 cas favorables sur 3). Ce n'est pas « très fréquent » : c'est sans exception.
- **Impossible :** ne se produit dans aucune issue. Ex. : tirer un `C` d'un sac qui ne contient que `A,A,B` (0 cas sur 3).
- **Probable :** mot courant signifiant qu'un événement a de bonnes chances de se produire. **Convention précise de ce module** pour comparer à « peu probable » : plus de la moitié des issues *équiprobables* lui sont favorables. Par ex., `A` avec 2 tickets parmi 3 est probable, mais non certain. Si exactement la moitié, parler d'une chance égale à celle du contraire, pas de majorité.
- **Hasard :** imprévisibilité du résultat de l'essai individuel; il n'efface pas la connaissance de la composition. Lors d'un tirage parmi `A,A,B`, `B` peut très bien sortir, même si `A` est plus probable.

**Précisions :** *possible* veut dire qu'il existe au moins un cas favorable; *moins probable* est une comparaison entre événements, pas un synonyme d'impossible; *aussi probable* signifie mêmes chances. Sous les conditions fixées, comparer les fractions `favorables / total` est une aide facultative : la justification en mots et en dénombrement suffit.

## Exemple résolu 1 — Sac de jetons

Sac bien mélangé : **4 jetons marqués `L` et 1 marqué `M`**, indiscernables au toucher; on en tire un.

1. Inventaire total : `L | L | L | L | M` = 5 issues équiprobables.
2. `L` : 4 sur 5 ⇒ **probable et plus probable que M**, mais **pas certain**, car M existe.
3. `M` : 1 sur 5 ⇒ **possible et moins probable que L**, pas impossible.
4. `N` : 0 sur 5 ⇒ **impossible**.
5. `L ou M` : 5 sur 5 ⇒ **certain**.

Phrase-modèle : « L est plus probable que M parce qu'il y a quatre jetons L contre un M, et tous les jetons peuvent être tirés avec la même chance. »

## Exemple résolu 2 — Roue de six secteurs identiques

Une roue non biaisée a six secteurs égaux notés `A | A | B | B | B | B`.

- `A` : 2 secteurs sur 6; `B` : 4 sur 6 ⇒ B **plus probable** que A et probable selon notre convention de majorité.
- `A ou B` : 6 sur 6 ⇒ certain; `C` : 0 sur 6 ⇒ impossible.
- Même si un lancer donne A, la comparaison reste 4 secteurs B contre 2 A; un résultat particulier ne renverse pas les chances du modèle.

**Deux représentations équivalentes :** manipuler six cartes étiquetées; aligner six cases écrites; dire « 4 sur 6 vs 2 sur 6 » ou écrire `4/6 > 2/6` si cette notation est comprise.

## Contre-exemples commentés

1. **« Quatre L parmi cinq : L sortira obligatoirement. »** Faux : M existe et peut sortir; probable ≠ certain. Correction : « L est probable (4/5) et M reste possible (1/5) ».
2. **« Un seul M parmi cinq : M est impossible. »** Faux : impossible exigerait zéro M. Correction : « M est possible mais moins probable (1/5) ».
3. **« Trois secteurs X et deux secteurs Y : X a toujours plus de chances, même si X est minuscule. »** Non justifié : des secteurs inégaux n'ont pas nécessairement la même chance; compter les secteurs n'est valide qu'avec des secteurs égaux.
4. **« J'ai eu B deux fois de suite, alors A est sûr la prochaine fois. »** Faux dans les essais indépendants dont les conditions sont inchangées. Chaque essai garde ses propres possibilités. Sans remise, au contraire, la composition doit être recalculée — ce n'est pas la situation des exercices de base.

## Méthode à réutiliser

1. **Énoncer les conditions** (total et égalité des chances, expérience unique ou remise).
2. **Lister/compter les issues**; repérer celles favorables à l'événement.
3. **Classer** : 0 = impossible; total = certain; entre les deux = possible non certain. Pour comparer : davantage d'issues favorables sur le même total = plus probable; même nombre = aussi probable.
4. **Justifier** en citant le nombre de cas et la condition de chances égales. Ne jamais confondre résultat observé et chances annoncées.
