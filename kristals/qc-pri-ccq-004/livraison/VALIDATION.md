# Validation de livraison — qc-pri-ccq-004 (v1.2)

**Statut :** contenu rédigé et contrôles techniques automatisés exécutés; `a_revoir` pour la révision humaine. Aucune qualification « certifié », « homologué », « publié » ou conformité PFEQ.

## Contrôles réellement exécutés par le script de construction
- Lecture des huit fichiers obligatoires dans l'archive source fournie; présence vérifiée.
- Identifiants source (`qc-pri-ccq-004`, `obj-1`, `crit-1`, `qc-pri-ccq-004-ev-01`), objectif, preuve, concepts, absence de préalables et d'ordres conseillés confirmés; aucune relation du graphe n'implique cet ID.
- En-tête YAML du parcours conservé à l'identique et analysé avec PyYAML; 12 sections numérotées présentes.
- Contrat JSON natif enrichi **sans supprimer ni remplacer ses clés existantes**, avec champs du contrat de génération sur la famille existante.
- Dix items ordonnés 001–010, uniques, `obj-1`, `crit-1`, famille constante, statuts `a_revoir`, consignes, stimuli, corrigés, critères et feedback non vides; tests des seeds et des couples variantes/corrigés.
- Deux preuves autonomes distinctes q-009 et q-010 avec consignes, données, rubriques et contextes indépendants; modes d'accès équivalents.
- Vérification éditoriale automatisable des mentions d'accès, confidentialité, droits, sections et liens internes; relecture des corrigés des 10 items à partir des faits inventés (contrôle manuel de cohérence, **pas** étude empirique).
- Exactement 14 fichiers non vides, en-têtes de ZIP autorisés, aucun dossier enveloppant, aucun chemin relatif dangereux, JSON analysables, CRC ZIP valide et manifeste exact.
- Simulation de superposition sur les chemins de l'archive maîtresse : **2 remplacements existants (authoring) et 12 ajouts**, aucun fichier protégé n'est inclus ou écrasé.

## Limites / revue humaine indispensable
1. Tester les formulations auprès d'apprenants et vérifier l'adéquation de leur longueur, l'âge, les particularités culturelles et l'accessibilité réelle.
2. Faire lire les rubriques à au moins deux correcteurs et comparer leur cohérence; essayer les deux preuves dans leurs modalités orales et écrites.
3. Confirmer les licences et droits de redistribution si ce delta doit quitter le cadre de son propriétaire; les sources extérieures sont des liens, non des fichiers copiés.
4. Vérifier la neutralité des compromis et le caractère non intrusif des scénarios en fonction du milieu d'enseignement.
5. Les conséquences des situations fictives sont limitées aux faits de leur énoncé; aucune enquête de terrain ou analyse quantitative d'impact environnemental n'a été réalisée.
6. Aucune qualification du Framework v9, des `canon/`, `runtime/` ni de publication n'a été tentée.

## Propositions de structure — non appliquées
- Ajouter centralement, lors d'une évolution versionnée, un schéma commun formel des items qualitatifs avec rubriques multicritères, métadonnées de biais/accessibilité et versions explicites de corpus de scénarios.
- Ajouter ultérieurement une procédure commune de revue entre correcteurs et d'archivage des deux preuves, hors fichiers canoniques.

**Périmètre de ce delta :** uniquement les 14 fichiers listés dans `livraison/MANIFEST.json`, sous `kristals/qc-pri-ccq-004/`. Aucun registre, aucune gouvernance ni autre Kristal inclus.
