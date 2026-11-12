# Décisions d’architecture — Ekole

1. **Une seule racine locale** : `C:\mycode\Ekole`, sans perturber `C:\mycode\UCKK\uckk-moodle` ni `UCKK_ops_console`.
2. **202 Kristals auteurs indépendants** : garder les objectifs, préalables, contenus, évaluations et provenances v1.2; la fusion ne les rend pas v9 qualifiés.
3. **Kristal-Portail polymorphe** : `organisation/kristal-portail-ekole.candidat.json` décrit l’organisation et les obligations de communication, pas une fausse fédération v9.
4. **SemantiK Architect produit des phrases** : chaque `utterance` avec identifiant et source; jamais de paragraphes IA implicites.
5. **Konstellation navigue** : les vues par matières / cycles / profils sont des projections renouvelables; les années restent non qualifiées.
6. **Moodle exécute** : catégories, cours, sections, activités, ressources, quiz, droits, notes et inscriptions. La copie statique n’est pas Moodle.
7. **Médiathèque référence** les médias via identifiants ou URL autorisés, sans dupliquer une bibliothèque cachée.
8. **Hôtes GitHub / Kristal v10** : node, binding, publication, directory et activation séparés; pas de manifeste v10 fabriqué sans identifiants et engagements validés.
9. **Aucune publication automatique** : les commandes livrées font uniquement des tests, exports, prévisualisations et copies locales explicitement approuvées.
10. **Confidentialité** : aucun compte d’élève, note, mot de passe ni secret d’infrastructure dans l’interface statique.

## Source d’autorité

L’Authoring Kit v1.2 décrit l’apprentissage; UCKK porte le plan institutionnel; SemantiK réalise les phrases; Konstellation compose les perspectives; Moodle possède les données opérationnelles. Aucun composant aval ne réécrit l’autorité amont.
