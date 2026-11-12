# Journal de validation — `qc-pri-ilss-010`, delta v1.2

## Périmètre et résultats techniques

Document de validation automatisée et de limites : contrôles préarchivage effectués le 8 octobre 2026. Deux fichiers `authoring` sont des remplacements de leurs originaux v1.2; douze autres sont des ajouts. Aucun registre, fichier de gouvernance, autre Kristal ni objet canonique n'est inclus.

## Tests effectués

**498 assertions préarchivage ont réussi, sans échec**, sur :
- les métadonnées YAML, les 12 sections, la conservation du contrat JSON natif et les liens du graphe;
- les 10 items numérotés, les objectifs/critères/famille, le format fixe et les deux contextes de preuve, les critères et rétroactions;
- les consignes de participation concrète, les conditions de sécurité et d'accessibilité inscrites;
- la provenance, les droits, le manifeste, les 14 chemins et l'intégrité de l'archive;
- la simulation de superposition sur la frame d'origine sans effet sur les fichiers non autorisés.

## Résultat d’intégrité de l’archive

Un contrôle CRC, le nombre exact de 14 fichiers, les chemins autorisés, les trois JSON et la concordance avec le manifeste sont vérifiés après création du ZIP.

## Points non validés par code

- Sécurité effective et consentement dans une classe : **non testés**.
- Pertinence interculturelle et absence de stigmatisation en contexte réel : **revue humaine à faire**.
- Fidélité interévaluateurs, compréhension des consignes, faisabilité de deux événements participatifs : **non étalonnées**.
- Droits de ressources éventuelles ajoutées par un enseignant : **à vérifier localement**.
- Statut des dix items : **`a_revoir`**, aucun examen homologué, aucune qualification au PFEQ.

## Revue humaine prioritaire

1. Faire vérifier par une personne qualifiée en ILSS que la participation n'exige pas de fluence française, de dévoilement identitaire ou d'adhésion culturelle.
2. Examiner conditions d'accès et alternatives pour les apprenants utilisant des outils de communication ou ne pouvant rejoindre un grand groupe.
3. Tester les rubriques sur deux activités réelles avec volontaires et recueillir des évaluations indépendantes.
4. Contrôler ressources, consentement, confidentialité et droits avant toute réutilisation d'images, musique ou production d'élève.

## Propositions d'évolution de structure (non exécutées)

- Ajouter ultérieurement à un schéma central un champ d'accessibilité de la **participation réelle** et un journal de « partenaire volontaire / environnement accessible » sans données sensibles.
- Prévoir au niveau d'un moteur de déploiement une option d'épreuve non concluante lorsque le milieu n'offre pas de partenaire ou de ressource accessible; aucune base centrale modifiée ici.
