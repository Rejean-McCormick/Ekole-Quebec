# 06 — Feedback ciblé, remédiation et transferts

## Erreurs typiques → premier point à corriger → nouvel essai

| Trace d'élève | Diagnostic | Feedback descriptif | Micro-remédiation et contrôle nouveau |
|---|---|---|---|
| « 4 A sur 5, A est certain. » | Confusion beaucoup/tous | « Quel jeton peut encore sortir? » | Montrer `A,A,A,A,B`, pointer B; refaire avec `C,C,C,D` : C probable, non certain. |
| « 1 B sur 5, B est impossible. » | Confusion rare/zéro | « Où voit-on un B? » | Comparer `A,A,A,A,B` puis `A,A,A,A,A` : B passe de possible à impossible. |
| « Ça a donné X hier, donc X doit ressortir. » | Résultat passé utilisé pour classer | « Combien d'issues X y a-t-il maintenant? » | Mettre deux cartes X/Y, mélanger à nouveau *avec remise*, classifier sans regarder le résultat passé. |
| « 2 R et 2 B : R est plus probable. » | Égalité ignorée | « Combien pour chaque étiquette? » | Aligner quatre cases et comparer deux contre deux; refaire trois contre trois. |
| « 3 petits secteurs rouges et 2 très grands bleus : rouge a plus de chances. » | Hypothèse d'équiprobabilité absente | « Les secteurs ont-ils même taille? » | Revenir à roue à secteurs égaux; pour roue inégale, comparer la surface angulaire plutôt que le nombre de secteurs. |

La correction se valide sur une **nouvelle configuration**; ne jamais déclarer la maîtrise après répétition de la réponse donnée.

## Transfert 1 — Tirage fictif à la bibliothèque (contexte d'étiquettes)

Une bibliothécaire prépare six signets identiques : `H | H | H | H | P | P`. Un élève en tire un, bien mélangé. **Sans tirer**, classe (a) H; (b) P; (c) T; (d) H ou P; compare H et P, explique les conditions.  
**Réponses :** H probable, plus probable que P (4/6 > 2/6), mais non certain; P possible et moins probable; T impossible (0/6); H ou P certain (6/6). **Justification attendue :** les six signets sont équiprobables et leurs étiquettes sont entièrement connues. **Critères observables :** zéro/tout/partie corrects, comparaison fondée sur 4 vs 2, exception P citée.

## Transfert 2 — Choix d'une case dans une application fictive (contexte numérique)

Une application fictive et sans enjeu réel choisit uniformément une des huit cases `1 | 2 | 3 | 4 | 5 | 6 | 7 | 8`. Classer (a) nombre entre 1 et 8; (b) nombre 9; (c) nombre pair; (d) nombre supérieur à 6. Comparer c et d, expliquer les conditions.  
**Réponses :** (a) certain 8/8; (b) impossible 0/8; (c) possible, 4/8 (`2,4,6,8`), aussi probable que impair; (d) possible mais moins probable, 2/8 (`7,8`); pair plus probable que >6 (4/8 contre 2/8). **Justification :** huit cases de même chance, listes de cas favorables correctes. On ne peut pas prédire le nombre choisi.

## Enrichissement : comparer des modèles, pas des histoires

Présenter deux roues : dans la première, 3 secteurs rouges sur 4 **égaux**; dans la deuxième, 3 secteurs rouges de 10° et un secteur bleu de 330°. Dans la première, rouge = 3/4; dans la deuxième, rouge = 30°/360° = 1/12 si la roue est équitable en angle. **Conclusion :** « trois secteurs rouges » ne suffit pas sans préciser la taille des secteurs. Ce cas limite sert à comprendre l'hypothèse, pas à exiger le calcul d'angles pour la preuve principale.

## Rappel différé (vers J+7 puis J+21)

Nouveau jeu de 6 cartes identiques `A,A,A,B,B,B`. Sans support initial, demander : A certain? B impossible? A plus probable que B? Réponses : ni A ni B certain ou impossible; mêmes chances (3/6). Demander ensuite de transformer le jeu pour que A devienne certain (remplacer les trois B par A) puis impossible (remplacer les trois A par B). Noter la raison donnée et programmer une remédiation ciblée si elle manque.
