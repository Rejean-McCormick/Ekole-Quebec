# Références de contenu, raisonnement, créations et droits — `qc-pri-mu-009`

**Objet :** `obj-1`, `crit-1`, famille `qc-pri-mu-009-ev-01`. **Date de consultation externe :** 8 octobre 2026. **Statut documentaire :** `a_revoir`. Cette fiche distingue rigoureusement **sources effectivement vérifiées**, **inférences pédagogiques** et **créations musicales/documents originaux**.

## 1. Sources du workspace maître consultées et contrôlées

Archives et chemins lus (contenus conservés **à l’extérieur** du ZIP de livraison) :

- `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` — invariant : objectif vérifiable, préalable franchissable sur diagnostic équivalent, deux preuves d’autonomie distinctes, pas de PFEQ comme critère.
- `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` — contrat des familles, trois modes, cadre éthique des évaluations en arts; critères/processus plutôt que goûts.
- `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` — appellation « Musique » exclusivement; aucun statut de conformité attribué.
- `registry/GRAPHE_PEDAGOGIQUE_202.json` — seule relation de ce Kristal : `qc-pri-mu-009/requires/qc-pri-mu-008`; aucune recommandation d’ordre ni renforcement dans le graphe.
- `kristals/qc-pri-mu-009/authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json` (versions source) — préservation des identifiants, YAML, critère, notion et famille.
- `kristals/qc-pri-mu-009/authoring/ALIGNEMENT.md` et `authoring/BRIEF_REDACTION.md` — consignes disciplinaires, frontières, preuve attendue.

Il s’agit de **décisions internes de gouvernance**, non d’autorités scientifiques externes ni d’homologations québécoises. Le présent ZIP ne copie pas les fichiers de gouvernance.

## 2. Sources externes effectivement vérifiées pour les définitions musicales

1. **The Open University**, OpenLearn, « *Discovering music through listening* », première publication **22 juillet 2020**. URL : https://www.open.edu/openlearn/history-the-arts/discovering-music-through-listening/ . Consultée pour la notion d’écoute rapprochée et le répertoire descriptif des éléments (pulsation, tempo, rythme, timbre, dynamique, texture), **sans reprendre ni audio ni partition**. Cette ressource publique ne transfère pas automatiquement un droit de reproduction de ses œuvres sonores.
2. **OpenStax**, *College Physics 2e*, section 17.6, « *Hearing* ». URL : https://openstax.org/books/college-physics-2e/pages/17-6-hearing . Consultée pour distinguer hauteur/fréquence, intensité perçue et timbre; ne présuppose pas qu’une valeur physique produit une impression émotionnelle identique chez tous.
3. **The Art of Music: Music Appreciation with an Equity Lens**, chapitre 2, « *Elements of Music* », Pressbooks. URL : https://rotel.pressbooks.pub/artofmusic/chapter/chapter-2/ . Consultée pour cadrer le timbre comme description de qualité de son, non jugement de goût.

**Périmètre de vérification :** présence des pages publiques et concordance de leurs descriptions avec les notions élémentaires; aucune citation textuelle longue, reproduction de partition ou extraction d’enregistrement. Les choix de pédagogie primaire, les seuils et les tâches sont des **décisions internes**, non des conclusions issues d’une étude d’efficacité réalisée ici.

## 3. Raisonnements dérivés (ne pas présenter comme citations)

- « Un avis esthétique a autant de valeur indépendamment de son sens positif/négatif » : principe d’évaluation éthique choisi pour ce parcours; on note les *justifications* plutôt que le goût.
- « Une caractéristique de durée et une caractéristique de hauteur forment deux indices distincts » : distinction opérationnelle fondée sur catégories musicales reconnues; on demande de situer les phénomènes à la réécoute.
- « Un élève peut demander plusieurs écoutes sans recevoir des indices » : accommodation de procédure, non preuve scientifique d’efficacité universelle.
- « Une aide de contenu empêche de qualifier l’essai d’indépendant » : règle locale de maîtrise, non mesure standardisée externe.
- « Même propriété sonore, effets ressentis différents » : séparation conceptuelle entre description et interprétation; ne pas diagnostiquer émotions ou aptitudes.

## 4. Productions créées ici (origine et mode de génération)

**Mini-œuvres S01 à S11, originales au niveau des choix de séquences et de leur réalisation numérique :** synthèse additive de sinusoïdes de fréquences spécifiées, sans échantillons téléchargés, sans paroles ni musique citée. Pour chaque note : début, durée, fréquence fondamentale en Hz, amplitude relative et type de timbre sont inscrits **dans `contenu/01_NOTIONS_ET_EXEMPLES.md`**. Échantillonnage 8 000 Hz, mono, PCM 8 bits non signé; enveloppe d’entrée de 18 ms et de sortie de 47 ms; coefficients de mélange sinusoïdal :

- `doux` : sinus fondamental pur.
- `rond` : 0,85 sin(f) + 0,15 sin(2f).
- `clair` : 0,72 sin(f) + 0,25 sin(2f) + 0,12 sin(3f).
- `sec` : 0,65 sin(f) + 0,25 sin(3f) + 0,10 sin(5f).

L’échantillon est borné à ±0,9 en valeur normalisée et codé par `arrondi(128 + 119 × valeur)`. Un facteur commun de sortie 0,68 multiplie amplitude, enveloppe et timbre. La durée finale inclut 240 ms de silence après l’événement le plus tardif. Ces paramètres permettent de **recréer** et de contrôler les pistes sur un autre système; chaque page fournit l’empreinte SHA-256 du WAV correspondant. Le son réellement rendu doit être réécouté avant usage avec enfants; ce test perceptif n’a pas été effectué par un auditeur humain indépendant.

**Autres créations originales :** les 12 sections pédagogiques rédigées, les exemples et contre-exemples, les deux diagnostics, trois exercices guidés, quatre situations autonomes, deux transferts, les onze items fixes, leurs réponses-témoins et leurs rubriques. Aucune question ou musique d’un manuel externe n’a été copiée. L’expression « original » décrit le procédé de création, pas une **certification juridique de non-contrefaçon**, qui exige une revue.

## 5. Déclaration de limites et droits

- **Éléments externes cités** : références bibliographiques et concepts généraux; aucune reproduction de contenu protégé dans le livrable.
- **Éléments sonores livrés** : encodages WAV synthétisés localement dans les 14 fichiers autorisés uniquement (lecteurs `data:audio/wav` dans le Markdown); aucune pièce commerciale, voix, prestation de tiers, boucle échantillonnée ou captation d’élève.
- **Droits futurs de réutilisation** : la licence commerciale / la cession des créations n’est **pas déterminée par ce dossier**. Réviser cette question et les éventuelles ressemblances fortuites avant diffusion publique; ne pas inventer une licence CC pour un tiers.
- **Accessibilité et sécurité** : les réglages audio et rendus réels ne sont pas certifiés; validation en situation et modalité d’accommodation nécessaires. L’usage d’une partition seule ne permet pas d’affirmer avoir directement mesuré l’écoute.
- **Sources musicales supplémentaires** : inexistantes à ce stade; toute insertion ultérieure de matériau tiers exigera provenance, licence, consentement si applicable et révision des items et empreintes.
