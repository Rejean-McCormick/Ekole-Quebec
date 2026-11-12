# Validation effective — qc-pri-als-001 — livraison v1.2

**Archive attendue :** `qc-pri-als-001_livraison_v1.2.zip`.  
**Source lue :** `initbundle(1).zip`, racine `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`.  
**Identité :** `qc-pri-als-001` — Anglais, langue seconde — Comprendre des consignes et des messages oraux.  
**Statut :** rédaction terminée **pour revue**; **aucune certification, homologation ni publication**.

## Contrôles automatiquement exécutés avant empaquetage

**44 assertions réussies**, notamment : YAML strictement identique pour les métadonnées v1.2; maintien des 12 sections et des champs initiaux de contrat; IDs, objectif, critère, famille, concepts, préalables et liens du graphe; JSON strict parsable; numérotation de 10 items sans doublon; 2 contextes de maîtrise comprenant **3 consignes** chacun; 10 contrôles textuels ciblés des corrigés; banque fixée sans génération libre; présence de 2 diagnostics, 3 tâches guidées, 4 autonomes et 2 transferts; provenance/droits déclarés et protocoles d'accessibilité/sécurité spécifiés. **Ces assertions textuelles ne remplacent pas une revue linguistique ni un essai avec élèves.**

## Contrôles de paquet et de fusion

- La validation finale de l'archive est exécutée par le script **après** production de ce rapport : racine de tous les chemins `kristals/qc-pri-als-001/`, premier fichier sous cette racine, exactement 14 fichiers non vides, absence d'entrées superflues et de chemins absolus ou `../`, CRC ZIP, manifeste fidèle à la liste et fichiers JSON parsables.
- Simulation de fusion **sur les noms d'entrées du ZIP maître en mémoire** (sans extraction ni écriture dans le workspace) : seuls `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json` se superposent aux entrées existantes; les **12 autres** sont de nouveaux chemins. Les fichiers protégés et les autres Kristals ne figurent pas dans le delta. Ce n'est pas une intégration réelle dans un déploiement Moodle/LMS.
- Le rapport de vérification automatique et les résultats du contrôle de ZIP sont imprimés dans le journal de construction du présent travail; si l'une de ces assertions échoue, le script ne livre pas l'archive.

## Relecture des solutions, limites de validation

Les solutions sont explicites et **vérifiées sémantiquement par comparaison de mots cibles et par logique d'action** : *on/sur, under/sous, inside/dans, next to/à côté, open/ouvrir, close/fermer*. Aucune simulation audio, aucun test de compréhension en classe, aucun test intercorrecteurs, aucune validation de prosodie ou d'accent d'un lecteur. Les scripts sont **anglais d'usage courant original**, à réviser par une personne enseignante qualifiée (niveau de langue, diversité d'accents, débit, ambiguïtés possibles). Le contrôle de corrigés est **textuel ciblé**, pas un solveur, pas une certification.

## Droits, sécurité, accessibilité

- Sources internes réellement lues et créations originales inventoriées dans `sources/REFERENCES_CONTENU.md`; absence d'images, d'audio, de citations longues ou de matériel externe joint. **Audit légal complet des droits non réalisé**.
- Contrôle textuel de la présence de gestes accessibles, objets grands, réponse en français/anglais simple/CAA, non-évaluation de l'accent; **aucun essai d'accessibilité utilisateur** exécuté. Dépendance au son audible à traiter avec spécialiste si audition non accessible. Proscrire petits objets ingérables et déplacements non sécuritaires.
- Questions de revue humaine : phrases naturelles dans une variété d'anglais intelligible? distinction aide motrice/aide sémantique réaliste? faisabilité 3/3 dans chaque contexte et nombre de répétitions? sécurisation des objets selon l'âge? contrôle préalable du vocabulaire suffisant sans divulgation des phrases? adéquation des accommodations pour chaque élève?

## Modifications locales et demandes centrales éventuelles

- **Deux remplacements complets préservant l'identité** : `authoring/PARCOURS.md` (front matter v1.2 inchangé) et `authoring/CONTRAT_PEDAGOGIQUE.json` (champs natifs préservés, famille enrichie; seuls `review_status` et `statut` mis à jour vers `à revoir`).
- **12 nouveaux fichiers** : six contenus, trois évaluations, une provenance et deux fichiers de livraison.
- **Proposition non appliquée** à discuter au niveau central : format de trace d'observation orale (script entendu, nombre d'écoutes, modalité de réponse et niveau d'aide), et mécanisme de gestion de familles variantes contrôlées après révision. Aucun registre, graphe, norme, schéma, fichier protégé ou autre Kristal n'a été modifié.
