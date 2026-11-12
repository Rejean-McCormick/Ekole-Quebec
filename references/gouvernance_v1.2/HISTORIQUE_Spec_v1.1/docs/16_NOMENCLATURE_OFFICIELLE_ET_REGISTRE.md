# 16 — Nomenclature officielle, registre central et non-invention des codes

## 16.1 Référence normative

Le fichier racine [REFERENCES_OFFICIELLES_QC.md](../REFERENCES_OFFICIELLES_QC.md) est l'unique **index central** des pages officielles du primaire, des `discipline_id` ScolQc et des éventuels codes administratifs **qualifiés**. Il **ne remplace pas** `A-Kristal-ScolQc`, propriétaire du curriculum et des sources.

## 16.2 Types à ne jamais confondre

- `discipline_officielle` : nom affiché dans le PFEQ; **pas un code**.
- `code_interne_kristal` : identifiant gelé `qc-pri-...`; **pas officiel**.
- `source_id_scolqc` : identifiant de provenance interne à ScolQc; **pas un numéro de programme ministériel**.
- `code_matiere` / `code_cours` / `code_programme` : code administratif **s'il est attesté** (autorité, format et portée).
- `code_epreuve` : identifie une épreuve ou une composante d'épreuve; **pas un code de cours**.
- `numero_publication` : identifie un document; **pas une compétence**.

Aucun code administratif « de cours » du primaire n'est ajouté sans source primaire précise. `non_etabli` = absence de preuve au registre, pas affirmation universelle d'inexistence.

## 16.3 Contraintes des conversations

- **DOIT** charger le registre officiel gelé de la même version que le brief.
- **NE DOIT PAS** créer/modifier une entrée de code, un `source_id` ou une édition officielle à partir d'une intuition.
- **DOIT** proposer un nouvel enregistrement via `modeles/MODELE_PROPOSITION_CODE_OFFICIEL.md`.
- **DOIT** aligner par objectif, édition, localisateur et cycle/année applicable lorsque démontré.
- **DOIT** inscrire `code_officiel: null`, `statut_code: non_etabli` quand aucun code qualifié n'est connu; ne pas remplacer ce vide par le code interne de Kristal.

## 16.4 Contrôle de qualité G2-R

Tout `officiel_verifie` sans localisateur, édition et autorité contrôlée échoue G2. Un code administratif associé à une feuille sans entrée qualifiée du registre échoue **G2-R** (résolution de codes). G2-R **ne bloque pas la rédaction pédagogique** si `code_officiel: null`; il bloque la déclaration non vérifiée de conformité.

## 16.5 Changements et migrations

L'ajout d'un code vérifié à un programme ne doit **pas** renommer les 202 IDs. Les mises à jour d'éditions peuvent générer de nouveaux alignements et révisions de parcours, sans dupliquer leurs contenus canoniques.

Voir [docs/05_ALIGNEMENT_CURRICULAIRE.md](05_ALIGNEMENT_CURRICULAIRE.md) et [docs/13_GOUVERNANCE_ET_VERSIONS.md](13_GOUVERNANCE_ET_VERSIONS.md).
