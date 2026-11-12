# 01 — Notions et exemples : Temps et durées

**Kristal :** `qc-pri-ma-026` · Mathématique · `obj-1` / `crit-1` · Les horaires sont fictifs.

## Savoir distinguer un instant et une durée

Une **heure affichée** (`09 h 25`) situe un instant de la journée. Une **heure comme unité** représente **60 minutes** de temps écoulé; `1 h 25 min = 60 + 25 = 85 min`. La **minute** est une unité de durée égale à 60 secondes; sur une horloge à notation `HH h MM`, la partie `MM` appartient à `00...59` et ne représente jamais des centièmes de l'heure. Ainsi `09 h 50` ne correspond pas à « 9,50 heures ».

Un **calendrier** situe les dates selon leur succession : un jour suivant peut aussi commencer un nouveau mois ou une nouvelle année. Avril, juin, septembre et novembre ont 30 jours; janvier, mars, mai, juillet, août, octobre et décembre 31; février a 28 jours, ou 29 si l'année est bissextile. Dans le calendrier grégorien, une année divisible par 4 est bissextile, sauf les siècles non divisibles par 400. Donc **2024** est bissextile, **2025** ne l'est pas, **2100** ne l'est pas.

La **durée** est la quantité de temps entre deux instants, indiquée en minutes ou heures et minutes. La notation **1 h 15** de durée désigne 75 min; `01 h 15` dans un horaire désigne l'instant 1 h 15. Le **début** doit précéder ou coïncider avec la **fin** : une durée écoulée n'est pas négative. Un horaire qui traverse minuit doit donner les **dates**, sinon plusieurs durées sont possibles. Pour tous nos exercices : journée civile uniforme de 24 h, sans heures d'été/d'hiver ni changement de fuseau.

## Trois représentations d'un même calcul

- **Matériel** : sur une horloge mobile, déplacer les aiguilles en avançant le temps, jamais en reculant; un tour de 60 minutes équivaut à une heure.
- **Schéma** : tracer une frise `début → heure ronde → ... → fin`, écrire le nombre de minutes sur chaque bond.
- **Symbolique** : convertir les instants en minutes depuis minuit : `T(H,M) = 60H+M`; même date, `durée = T(fin)-T(début)`. Si les dates sont différentes, ajouter `1440 × nombre de jours écoulés` (comptés sur le calendrier) au décalage des heures et minutes. **Vérifier** : `début + durée = fin`, puis contrôler la place de la fin dans l'horaire.

## Exemple résolu 1 — Franchir une heure

**Horaire fictif :** répétition, début **09 h 35**, fin **11 h 10**. Quelle durée?

1. Encadrer les instants : début `09 h 35`; fin `11 h 10` le même jour.
2. Frise : `09 h 35 → 10 h 00` = 25 min; `10 h 00 → 11 h 00` = 60 min; `11 h 00 → 11 h 10` = 10 min.
3. Addition : `25 + 60 + 10 = 95 min = 1 h 35`.
4. Vérification arithmétique indépendante : `(11×60+10) − (9×60+35) = 670 − 575 = 95 min`. Vérification de sens : 95 min est entre une heure et deux heures; la fin suit le début.

## Exemple résolu 2 — Changer de jour en février bissextile

**Horaire fictif :** observation du **28 février 2024 à 23 h 40** au **29 février 2024 à 00 h 25**. Quelle durée?

1. Lire les **deux dates**; 2024 est bissextile : le jour suivant est bien le 29 février.
2. Frise : `28 fév., 23 h 40 → 29 fév., 00 h 00` = 20 min; `00 h 00 → 00 h 25` = 25 min.
3. Résultat : **45 min**.
4. Vérification : départ + 45 min = lendemain 00 h 25. Le nombre affiché sur l'horloge a diminué, mais la date a avancé : la durée reste positive.

## Contre-exemple 1 — La fausse soustraction en base 100

**Erreur :** « De 09 h 50 à 10 h 20, j'obtiens 70 minutes, car 10 h 20 − 09 h 50 = 0 h 70. » **Pourquoi c'est faux :** les minutes de l'horloge se comptent par 60; les chiffres ne se soustraient pas comme des centièmes. **Correction :** `09 h 50→10 h 00` = 10 min; `10 h 00→10 h 20` = 20 min; total **30 min**. Vérification : `09 h 50 + 30 min = 10 h 20`.

## Contre-exemple 2 — Oublier le calendrier

**Erreur :** « 31 décembre 2025 à 23 h 50 jusqu'au 1er janvier 2026 à 00 h 05 : la durée est négative, donc l'horaire est impossible. » **Pourquoi c'est faux :** la date suivante est le premier jour de la nouvelle année; `00 h 05` est **après** `23 h 50`. **Correction :** `10 min` jusqu'à minuit + `5 min` après = **15 min**. Vérification : `23 h 50 + 15 min = 00 h 05` le lendemain.

## Contre-exemple 3 — Résultat hors de l'horaire

**Erreur :** « L'atelier est de 13 h 15 à 14 h 00, donc il dure 45 minutes; je peux participer à un rendez-vous à 13 h 50 *après* cet atelier. » **Erreur de sens :** 13 h 50 est **avant 14 h 00**. La durée de l'atelier (45 min) est exacte, mais l'affirmation sur l'ordre des événements est fausse. Réparation : le rendez-vous à 13 h 50 **chevauche** l'atelier pendant ses 10 dernières minutes.

**Repère à mémoriser :** J'identifie les dates et les instants → je calcule une durée positive en minutes → je recompose l'instant final → je vérifie que l'horaire est cohérent.
