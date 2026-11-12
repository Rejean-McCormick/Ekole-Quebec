# Note de migration — norme 1.0.0 vers 1.1.0

## Décision

**Ajout du registre `REFERENCES_OFFICIELLES_QC.md` et du contrat de non-invention des codes administratifs.** Les 202 IDs, le découpage en 14 disciplines, le contrat de microparcours et les états existants restent inchangés.

## Compatibilité des contributions en cours

- Les fichiers `PARCOURS.md` existants restent lisibles.
- Les `ALIGNEMENT.md` existants doivent être **contrôlés** : vérifier que les prétendus codes officiels ne sont pas nos codes internes et que chaque lien a document, édition et localisateur.
- Si aucun code ministériel de cours ou matière n'est établi : laisser `code_officiel: null` / `non_etabli`. Il n'est **pas** nécessaire d'inventer un code pour valider la pédagogie.
- Les briefs de toutes les nouvelles conversations doivent mentionner la norme `1.1.0` et joindre le registre.

## Statut de vérification

Les portails disciplinaires sont vérifiés; l'alignement individuel des **202 Kristals** reste `à_vérifier`, tout comme leur granularité et les dépendances pédagogiques proposées. Cette mise à jour n'est **pas** une certification ministérielle.
