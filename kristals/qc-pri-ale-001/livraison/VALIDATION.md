# Validation de livraison — `qc-pri-ale-001`

**Date de préparation :** 2026-10-08. **Base native :** frame v1.2 de l’archive `initbundle(1).zip`, dossier `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` ; aucun nouveau dépôt ni fichier de gouvernance inclus.

## Contrôles effectivement exécutés
- Script `ale001package.py` (environnement de production) : **81 vérifications préalables réussies**, dont préservation intégrale des champs et valeurs YAML natifs, conservation des clés natives JSON, ID/titre/objectif/preuve, `requires=[]` et `ordre_conseille=[]`, les 12 sections, numérotation de 12 items, schéma des items, modes, deux contextes, A/B à graines 410 et 421.
- Vérification indépendante d’un dictionnaire **de 12 cibles** phonémiques / onset-rime / syllabiques dans 4 variantes (2 scénarios × 2 variantes × 3 mots), de la concordance entre segments énoncés et corrigés, et de l’absence de présentation préalable de ces mots dans l’enseignement ou la pratique autonome.
- Relecture statique des réponses fixes et de leurs critères par comparaison interne des consignes, pas par écoute enregistrée ni par phonéticien indépendant.
- Vérification de la mention des droits, de l’accessibilité, du consentement pour l’audio, du lien à la famille et des sources externes consultées.
- Contrôles techniques du ZIP, du manifeste, de la validité JSON, de l’intégrité CRC et de la liste complète de chemins exécutés au conditionnement final (voir résultat affiché par le script de validation); aucune preuve de certification en découle.

## Vérification spécifique du rendu
- L’archive doit contenir **14 fichiers** sous `kristals/qc-pri-ale-001/`, les deux `authoring/` remplacés et les 12 autres nouveaux, sans autre ID ni chemin parent.
- Aucun `AGENTS.md`, `ALIGNEMENT.md`, répertoire `governance`, `registry`, `canon`, `state`, `runtime` ou autre Kristal n’y figure.
- Les données `objet`, `famille` et `preuve` natives sont invariantes. Le champ natif de statut de l’en-tête YAML est conservé par choix de fusion; les lignes éditoriales documentent une rédaction complète mais non revue.

## Limites non levées / revue humaine
1. **Relecture phonétique anglophone** de tous les mots/IPA, comparaison aux variétés anglophones visées et essai réel de perception des pauses. Les segments ont été contrôlés par un lexique explicite de référence interne mais **pas** par enregistrement/sonogramme ni auprès d’enfants.
2. **Essais pédagogiques** : validité de la progression, familiarité des mots et durée; ajuster tout stimulus qui dépend trop d’un vocabulaire inconnu.
3. **Accessibilité** : contrôle d’une réponse équivalente pour des élèves avec difficultés de parole, audition ou motricité; aucune aide ne doit contaminer la preuve autonome.
4. **Éthique et confidentialité** : toute capture vocale exige des règles locales de consentement, de conservation et d’effacement.
5. **Droits/licences** : aucune image/audio/textes d’autrui incorporés; vérifier l’accord/licence de tout support extérieur ajouté plus tard. Les liens des références ne valent pas permission de reproduction.
6. **Statuts** : items `a_revoir`, livraison techniquement vérifiée, ni « publiée », ni « homologuée », ni « certifiée ».

## Propositions non appliquées au workspace central
- Ajouter ultérieurement au schéma central un indicateur `oral_prompt_hidden_from_learner`, des marqueurs `dialectal_variants_reviewed` et un champ de journal d’adaptations non nominatives. **Aucune modification du schéma, du registre ou du canon réalisée dans ce delta.**
