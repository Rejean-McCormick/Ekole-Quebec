# Sources, originalités, dérivations, droits et limites — `qc-pri-mu-001`

**Périmètre :** toutes les notions, recettes, situations et grilles livrées pour ce Kristal. Date de consultation des références publiques : **9 octobre 2026**. Les références externes ont été ouvertes/repérées au moment de la rédaction; elles n'accréditent **ni** les sons particuliers **ni** leur validation sur appareil. Pas de citation textuelle longue ni de musique enregistrée réutilisée.

## A. Sources internes effectivement lues dans l'archive reçue

- `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` — autorité de contenu, deux preuves indépendantes, pas de dépendance scolaire officielle.
- `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` — clés minimales de famille, modes fixe/paramétrique/scénario et items non certifiés.
- `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` — appellation « Musique » et absence de déclaration de conformité PFEQ.
- `registry/GRAPHE_PEDAGOGIQUE_202.json` — relations internes : **aucun préalable strict** pour `qc-pri-mu-001`; autres Kristals ont des liens `requires` vers lui, sans droit de les modifier.
- `kristals/qc-pri-mu-001/authoring/PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md` — identité, intitulé, objectif, critère, notions et famille; les deux premiers sont remplacés en conservant l'identité et la structure, les deux derniers ne sont pas inclus dans la livraison.

La gouvernance est **interne au produit Kristal**, et non une validation scientifique empirique de chacune des activités. Références institutionnelles du curriculum québécois employées seulement pour la nomenclature.

## B. Sources publiques vérifiées : portée réelle

1. **National Institute on Deafness and Other Communication Disorders (NIDCD), NIH**, *How is Sound Measured?* (mise à jour du 28 avril 2025), <https://www.nidcd.nih.gov/health/how-sound-measured>. Énonce que l'intensité ressentie varie selon l'environnement, la fréquence et le niveau, explique dB/dBA et le lien entre fréquence et hauteur. Appuie les précautions « volume du lecteur ≠ garantie de niveau perçu »; ne valide pas les contrastes proposés comme facilement perceptibles par tous.
2. **NIDCD, NIH**, *How Do We Hear?* (mise à jour du 16 mars 2022), <https://www.nidcd.nih.gov/health/how-do-we-hear>. Décrit la perception des hauteurs par le système auditif. Ne démontre aucune compétence individuelle d'écoute chez les enfants.
3. **NIDCD, NIH**, *Noise-Induced Hearing Loss* (mise à jour du 28 avril 2025), <https://www.nidcd.nih.gov/health/noise-induced-hearing-loss>. Appuie la prévention des expositions sonores excessives; notamment, une exposition longue ou intense peut abîmer l'audition. Les présents fichiers ne sont **pas calibrés en dBA**.
4. **Organisation Mondiale de la Propriété Intellectuelle (OMPI/WIPO)**, *Frequently Asked Questions: Copyright*, <https://www.wipo.int/en/web/copyright/faq-copyright>. Expose qu'une reproduction/enregistrement d'œuvre d'autrui peut nécessiter une autorisation, avec exceptions selon les lois et licences. Cette source n'attribue **aucune licence précise** à un enregistrement tiers. Les sons locaux sont produits par synthèse originale et n'utilisent aucune œuvre téléchargée.

## C. Raisonnements dérivés, contrôlables sans autorité externe

- À fréquence, timbre et appareil constants, la différence **de temps** entre une onde synthétique de 0,40 et de 1,40 seconde relève de la durée programmée. Cela n'atteste pas automatiquement une perception correcte à l'écoute.
- À fréquence et durée identiques, des gains numériques `0,08` vs `0,24` induisent une différence d'amplitude numérique (rapport ×3). **Il n'est pas licite d'en conclure un niveau précis en dBA**, car haut-parleurs, distance et traitement audio interviennent; la compréhension « doux/plus marqué » doit être vérifiée à la diffusion.
- À amplitude, enveloppe et timbre identiques, 330 Hz vs 660 Hz correspond à une fréquence fondamentale doublée; le second son est destiné à constituer l'élément aigu de cette paire.
- Une onde sinusoïdale et une onde triangulaire de fondamentale 440 Hz n'ont pas la même forme et le même spectre, ce qui sert à illustrer une différence de timbre; sa perception est à vérifier par l'adulte.
- Une séquence de 0,50 s de note / 0,60 s de signal numérique nul / 0,50 s de note comprend une pause **intentionnelle**. Le bruit de fond réel peut subsister; cette absence de signal n'est pas une preuve de silence physique absolu.
- Les tables de vérité de A1–A4 et B1–B4 découlent directement des recettes ci-dessus; un contrôle automatisé vérifie les paramètres numériques, **pas** la validité pédagogique d'un jugement artistique.

## D. Productions originales composées pour cette livraison

- Situations fictives « atelier musical », « jardin imaginaire », « carte postale sonore », matrices et consignes; aucune œuvre reconnaissable, marque sonore, mélodie commerciale ni citation musicale transcrite.
- Trente-huit **recettes de signaux** numériques simples et leur programme Python standard de génération locale WAV; les paramètres permettent un contrôle par reproduction. Les sorties WAV ne sont pas incluses dans le ZIP demandé de 14 fichiers et n'ont pas été revendiquées comme droits cédés par un tiers.
- Explications, contre-exemples, pratiques, rétroactions, rubriques et règles de décision de maîtrise : rédaction originale pédagogique **soumise à revue humaine**.

## E. Droits, accessibilité et travaux qui restent à confirmer

**Aucun extrait audio externe** n'est copié, embarqué ou distribué. Pour remplacer les sons originaux par des œuvres ou échantillons tiers, recueillir la licence ou l'autorisation applicable et conserver les preuves de provenance/droit avant toute diffusion (une mise en ligne publique peut demander un traitement distinct d'un usage en classe). **Ne pas présumer** qu'un usage éducatif donne automatiquement droit à redistribuer tout enregistrement.

Avant utilisation : produire les WAV, écouter les 38 fichiers pertinents, évaluer les contrastes sur le matériel réel et auprès du public concerné, contrôler niveau et sécurité, faire relire par une personne compétente en pédagogie musicale et en accessibilité. Aucun audiogramme, niveau d'exposition réel, homologation, test auprès d'élèves ni avis juridique n'a été réalisé dans cette rédaction. Une personne ne pouvant accéder à une modalité auditive doit recevoir des aménagements appropriés sans fiction de preuve auditive.
