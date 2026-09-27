# ADR-002 : Suspendre les décisions automatisées du Score faute de garanties

**Statut** : Soumise au conseil · **Décideur** : conseil d'administration, sur proposition de la direction technique et de la conformité · **Pièces** : P.1, P.6, P.8, P.9

## Contexte

- Solvia Score rend **28 000 recommandations par mois** sur des candidatures de logement (P.1).
- Les agences suivent la recommandation **sans modification dans 61 % des cas**, et le candidat **n'est pas informé** du traitement automatisé (P.8).
- Taux de recommandation défavorable : **33,9 % en quartiers prioritaires, contre 12,1 % à Paris** (P.8). Le code postal n'est pas une variable, mais d'autres peuvent agir comme proxys.
- Une partie de la chaîne passe depuis 8 mois par une **API américaine non documentée** (P.6).
- Aucune analyse d'impact (AIPD) retrouvée, **pas de service juridique** (P.6).
- La data scientist a alerté le CTO il y a 4 mois, **sans réponse** (P.8).
- La plaquette annonce « 2 millions de dossiers ». La réalité est d'environ 190 000 (P.1, P.6).

## Décision

**Sous 48 h, on cherche les garanties minimales. Si elles n'existent pas, on propose au conseil de suspendre les nouvelles décisions automatisées jusqu'à la fin de l'audit.**

Garanties minimales recherchées :

1. une AIPD, même incomplète ;
2. une base légale identifiée pour le traitement ;
3. un contrat de sous-traitance avec le fournisseur américain, et la localisation des données ;
4. une logique d'intervention humaine documentée.

Pendant la suspension, les agences continuent de recevoir les dossiers **sans recommandation automatique**, et l'audit mesure les écarts par groupe comparable.

## Alternatives écartées

| Alternative | Pourquoi on l'écarte |
|---|---|
| **Continuer en l'état pendant l'audit** | 28 000 décisions par mois sans base légale connue. Chaque mois d'attente accroît l'exposition, et l'entreprise sait depuis 4 mois. |
| **Arrêter définitivement le Score** | Le constat justifie un audit, **il ne prouve pas une discrimination**. Arrêter sans mesurer, c'est décider sans preuve, dans l'autre sens. |
| **Retirer les variables « suspectes » et relancer** | Retirer une variable ne retire pas son effet : d'autres font proxy. Sans mesure par groupe, on ne sait pas si on a corrigé quoi que ce soit. |
| **Décision de la direction technique seule** | La décision touche le CA, les contrats et la responsabilité juridique : elle revient au conseil. La direction technique propose, elle ne tranche pas seule. |

## Conséquences

- **Coût commercial** : le CA du Score n'est pas isolé dans le dossier. Solvia Gestion fait 90 % du CA (P.1), donc le Score pèse **au plus ~1,12 M€ d'ARR**. C'est le plafond de l'exposition en cas de suspension totale.
- **Coût direct** : ~40 000 € d'analyse d'impact (estimé), financés dans le budget révisé.
- **Effet sur le deal à ~400 k€** : aucune promesse sur le Score v2 tant que l'audit n'est pas conclu ([réponse commerciale](../07-reponse-commerciale.md)).
- **Ce que ça rend possible** : repositionner le Score en **aide à la décision explicable**, un argument de vente auprès de bailleurs institutionnels ([vision CTO](../11-vision-cto.md)).

## Critère de révision

On lève la suspension dès que les 4 garanties existent **et** que l'audit mesure des écarts par groupe expliqués par des variables légitimes, avec une information du candidat et un canal de recours en place.
