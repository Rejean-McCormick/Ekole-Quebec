# Validation technique — `qc-pri-us-013`, v1.2

**Statut de départ du delta :** rédaction complète, items `a_revoir`, revue humaine requise. Les contrôles documentaires décrits ci-dessous sont réalisés par le script de vérification indépendant avant et après empaquetage. Ce document n'atteste aucune homologation, certification ou observation d'élèves.

## Nature de la livraison

- **14 fichiers exacts** sous `kristals/qc-pri-us-013/`, dont 2 remplacements complets `authoring/` et 12 ajouts. Aucun autre Kristal ni fichier de registre ou gouvernance inclus.
- Source maître `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis.zip` (`initbundle(1).zip`) consultée; YAML et champs canoniques du contrat à conserver.
- Dossiers d'évaluation A1/A2 (logement) et B1/B2 (mobilité), tous fixes et attribués à des pages officielles réellement consultées; F1–F3 fictifs et marqués comme tels.

## Contrôles techniques exécutés

**587 assertions de préarchivage exécutées et réussies le 8 octobre 2026, zéro échec.** Elles couvrent les 14 chemins et leur contenu, le YAML parsable et les 12 sections, les identifiants et liens natifs, le JSON strict, les dix items complets en statut `a_revoir`, deux preuves de maîtrise distinctes (logement / mobilité), les dates/faits du corpus, les rubriques et références, la documentation d'accessibilité et des droits. Le calcul **33,7 − 25,2 = 8,5 points** a été recomputé indépendamment. Une simulation d'overlay sur l'inventaire original constate **2 remplacements, 12 ajouts**, et **34 fichiers protégés inchangés** (SHA-256). Les contrôles de contenu sont documentaires et ne prouvent ni exactitude exhaustive ni validité didactique terrain. **Après archivage**, un contrôle CRC et des chemins du ZIP a été réalisé (voir log de vérification).

## Limites et revue humaine obligatoire

- Un spécialiste doit relire les formulations sur revenus/logement, institutions et mobilité; vérifier que les sources sont encore pertinentes à la date d'administration, que le vocabulaire convient et que les faits attribués sont suffisamment représentatifs.
- Revoir les 10 items, le niveau de difficulté, les 2 épreuves et la stabilité de cotation M1–M5 entre correcteurs; essayer les supports avec des élèves, sans recueillir leur situation privée.
- Les quatre pages externes ont été consultées mais peuvent évoluer; la précision factuelle 2021 **ne vaut pas indicateur 2026**. Aucune recherche d'avis des groupes concernés ou d'effets de programmes n'est prétendue.
- Aménagements, neutralité, absence de stéréotypes et usage des données doivent faire l'objet de validation sur le terrain. Aucun alignement officiel PFEQ ni licence globale de matériel tiers revendiqués.

## Propositions d'évolution structurelle, sans modifier les bases centrales

- Ajouter au schéma central, dans une version future soumise à validation, un type de lien `source_card_id` daté permettant de figer URL, date de données et date de consultation.
- Prévoir un contrôle `source_claim_kind` parmi `statistique_observee`, `orientation_politique`, `programme_annonce`, `interpretation` pour limiter les erreurs causales dans des variantes approuvées.
- Un protocole de revue intercorrecteur pourrait préciser comment qualifier deux sources institutionnelles distinctes mais de même autorité, tout en distinguant preuves et perspectives absentes. **Aucun fichier `governance/` ou `registry/` n'est changé ici.**
