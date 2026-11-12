# Validation — `qc-pri-ale-013`, livraison v1.2

**Statut :** `a_revoir` — livraison technique et pédagogique candidate, **non certifiée**. Les scripts anglais et rubriques restent soumis à revue humaine et essais réels.

## Matériel source effectivement ouvert

- Archive utilisateur : `initbundle(1).zip`, racine `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`.
- Gouvernement interne : `CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md`, ainsi que `REFERENCES_EVIDENCE.md`.
- Registre : `registry/GRAPHE_PEDAGOGIQUE_202.json` (filtrage des relations concernant cet ID).
- Fichiers natifs du seul Kristal : `authoring/PARCOURS.md`, `authoring/CONTRAT_PEDAGOGIQUE.json`, `authoring/ALIGNEMENT.md`, `authoring/BRIEF_REDACTION.md`.

## Contrôles effectivement exécutés et réussis

L'outil de vérification local a exécuté des assertions sur les fichiers de travail, puis sur le ZIP produit; **530 assertions réussies** au dernier passage, réparties ainsi :

| Groupe | Assertions réussies | Ce qui a été vérifié |
|---|---:|---|
| YAML natif, identité et 12 sections | 20 | Frontmatter YAML identique à celui du workspace, parse YAML, identité, titre, objectif, concepts indirectement via contrat, douze titres de section |
| Schéma et champs natifs du contrat | 34 | Toutes les clés/valeurs préexistantes du JSON et de sa famille conservées; présence des champs exigés par le générateur |
| 12 items, tâches et conditions | 325 | Banque JSON, format, séquence et unicité q-001 à q-012, références obj-1/crit-1/famille, tous champs communs, dialogues à deux voix, critères et modèles de réponses, deux preuves indépendantes |
| Scripts originaux et graphe | 38 | Présence de données contrôlées et manques d'information dans les douze scripts; absence d'arêtes sortantes, lien entrant non modifié |
| Couverture et contenu pédagogique | 31 | Deux diagnostics, trois guidés, quatre pratiques autonomes, deux contre-exemples, deux résolus, deux transferts, rappel différé, critères et accessibilité déclarée |
| Exactitude des chemins et du manifeste | 36 | Exactement 14 fichiers non vides, chemins relatifs, format du manifeste, 3 JSON stricts lisibles |
| Archive ZIP finale, CRC et identité | 46 | 14 entrées dans l'ordre exact du manifeste, première entrée au bon chemin, chemins sans traversée ni dossier englobant, CRC et octets identiques aux fichiers vérifiés |

**Sur les corrigés :** contrôle comparatif de faits explicitement présents dans les douze scripts, revue de leur cohérence avec les réponses modèles et vérification des situations où un renseignement manque. Cela ne remplace pas une double correction indépendante des réponses libres.

## Droits et accessibilité : contrôle de conception, non essai terrain

- Tous les dialogues et contextes sont des fictions pédagogiques rédigées pour cette livraison; aucune piste audio/image/voix tierce fournie, aucun texte de dialogue tiers reproduit.
- Consignes pour deux écoutes, débit compréhensible, canal de réponse oral/dicté/écrit, gestion des transcriptions et adaptations de l'accès documentées. **Aucun test utilisateur réel d'accessibilité n'a été effectué**.
- Scripts et corrigés réservés à l'enseignant avant la réponse; droits/consentement des voix à considérer seulement si un enregistrement est produit ultérieurement.

## Limites, revues humaines restantes et essais recommandés

1. Relecture linguistique indépendante (grammaire, richesse, naturalité des dialogues et acceptabilité de plusieurs questions de clarification).
2. Passation par de vraies voix ou audio produit avec consentement, analyse de l'intelligibilité, du rythme et de la durée.
3. Revue des ambiguïtés de scripts et calibration intercorrecteurs sur réponses libres; les modèles de réponses **ne sont pas des oracles automatiques**.
4. Tests avec les accommodations pertinentes; sous-titres ou transcription pendant l'épreuve changent la modalité mesurée et doivent être consignés.
5. Aucun score d'élèves collecté, aucune enquête d'équité ni homologation PFEQ ou autre certification.

## Propositions de changement structurel, non appliquées

- Prévoir dans le futur un champ central facultatif de journal de passation orale (deux voix, répétitions, modalités d'accès, transcription), après décision versionnée.
- Prévoir une validation humaine indépendante des items ouverts et un statut distinct de la réussite des contrôles techniques avant éventuelle publication.

**Périmètre :** deux remplacements `authoring/`, douze fichiers ajoutés; aucune inclusion ou modification de `governance/`, `registry/`, `state/`, `runtime/`, `canon/`, `docs/`, `AGENTS.md`, `kristal.workspace.json` ou d'un autre Kristal.
