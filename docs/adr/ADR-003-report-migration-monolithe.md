# ADR-003 : Reporter la migration du monolithe, stabiliser la facturation

**Statut** : Proposée · **Décideur** : direction technique intérimaire · **Pièces** : P.2, P.5, P.6, P.9

## Contexte

- La « migration du monolithe, phase 1 » figure sur les feuilles de route de **trois exercices consécutifs**, sans aucune spécification retrouvée (P.9).
- Le monolithe Rails porte l'API, le back-office et le **module de facturation** qui encaisse ~933 k€/mois (P.2, P.1).
- Ce module est du Rails de 2019 avec « sept ans de dérogations métier empilées », compris par **une seule personne**, qui démissionne (P.6).
- Capacité de l'équipe : 36 CDI, 3 démissions en cours, 29 % de turnover, 3 postes ouverts depuis 7 mois (P.5).
- Personne ne relit vraiment le code, et l'onboarding prend 3 mois faute de documentation (P.6).

## Décision

**On sort la migration de la feuille de route pour 90 jours. On investit à la place dans la connaissance et la sécurité du module de facturation, sans changer son architecture.**

Concrètement :

1. **Runbook** du batch de prélèvement, exécuté par une autre personne que le titulaire.
2. **Tests de caractérisation** sur les chemins critiques de facturation : on fige le comportement actuel avant d'y toucher.
3. **Cartographie** des dérogations métier : lesquelles sont encore utilisées, et par quels clients.
4. **Revue de code obligatoire** à deux personnes sur ce module.

La migration pourra revenir **après J90**, avec une spécification, un périmètre et une équipe qui comprend le code.

## Alternatives écartées

| Alternative | Pourquoi on l'écarte |
|---|---|
| **Lancer la migration maintenant** (« profitons-en pour tout refaire ») | Réécrire un module que personne ne comprend, pendant que son seul expert s'en va, c'est le scénario classique de la réécriture qui échoue. Aucune spécification n'existe après 3 ans. |
| **Extraire progressivement la facturation** (approche « strangler ») | C'est la bonne approche *à terme*. Mais elle suppose de savoir ce que fait le module. Les tests de caractérisation de cette ADR en sont le prérequis. |
| **Garder la ligne sur la feuille de route « pour plus tard »** | C'est ce qui se passe depuis 3 ans. Une ligne jamais démarrée dégrade la crédibilité de toute la feuille de route auprès du produit (P.6). |

## Conséquences

- **Économie** : l'arrêt des prestations liées à ce chantier contribue aux 250 à 340 k€ de leviers sur les prestations externes ([budget révisé](../05-budget-revise.md)).
- **Dette assumée** : le monolithe reste en l'état. On l'écrit, on ne le cache pas.
- **Ce que ça rend possible** : une future migration **fondée sur des tests et une documentation**, au lieu d'un savoir détenu par une seule personne.
- **Message au produit** : une feuille de route qui retire une ligne irréaliste est plus crédible qu'une feuille de route qui la reporte chaque année.

## Critère de révision

On rouvre la migration quand **deux personnes** savent exécuter et modifier la facturation, et que les tests de caractérisation couvrent le batch de prélèvement.
