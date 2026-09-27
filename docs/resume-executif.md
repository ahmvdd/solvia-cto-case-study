# Résumé exécutif : Solvia en une page

> **Mission** : reprendre la direction technique d'une scale-up SaaS (fictive) de 180 personnes après le départ brutal de son CTO, et remettre l'entreprise sous contrôle en 90 jours.
> **Contrainte** : 5 jours, aucune ligne de code, un dossier incomplet et contradictoire, un conseil d'administration qui ne veut plus être rassuré.

## Ce qu'on a trouvé

| | Constat | Enjeu |
|---|---|---|
| 🔥 **Production** | Panne totale de 6 h 08, dont 4 h 28 d'alerte sans réponse. Pas d'astreinte, pas de bascule de base, un seul SRE. 3 quasi-incidents depuis | SLA à 99,9 % non tenu sur 11 contrats institutionnels |
| 💶 **Facturation** | ~933 k€/mois encaissés par un module que **une seule personne** sait relancer. Elle démissionne en cours d'exercice | Le robinet du chiffre d'affaires |
| ⚖️ **Solvia Score** | 28 000 décisions de logement par mois, 61 % suivies sans modification, candidats non informés. Refus ×2,8 en quartiers prioritaires. Vendu « 2 M de dossiers », entraîné sur ~190 000 | Juridique (RGPD), réputationnel, commercial |
| 📉 **Coûts** | Cloud +140 % en 12 mois pour +22 % de clients. Un cluster GPU oublié à 3 % d'usage (288 k€/an). 12 lignes budgétaires sur 23 sans propriétaire | Discipline financière absente |

**Notre lecture** : ce ne sont pas quatre problèmes, c'en est un seul. **Solvia laisse tourner des systèmes critiques sans maîtrise collective.** Chaque risque avait été signalé par quelqu'un, et personne n'a décidé.

## Ce qu'on a décidé

1. **Facturation** : un binôme nommé sous 24 h, un batch exécuté sans le titulaire avant J30.
2. **Production** : astreinte testée (acquittement en moins de 10 min) et restauration chronométrée à J7, haute disponibilité à J60.
3. **Score** : garanties RGPD recherchées sous 48 h, **suspension conservatoire soumise au conseil** si elles n'existent pas, audit d'équité par groupe.
4. **Budget** : coupe imposée de −20 % (**1 099 400 €**) tenue **sans toucher à la masse salariale**. 323 700 € prouvés et immédiats, **268 000 € réinvestis** dans la fiabilité.
5. **Commercial** : refus d'une livraison à 5 semaines sur un deal à ~400 k€, contre un cadrage et une date engageante sous 30 jours.

## Ce qu'on a refusé de faire

Couper les salaires · lancer la migration du monolithe · promettre une date intenable · désigner un coupable · annoncer un montant de pénalités sans les données.

## Ce qui nous différencie

- **Établi / probable / inconnu** : chaque affirmation cite sa pièce, chaque inconnu reçoit une action datée.
- **Des chiffres reproductibles** : [un script recalcule tout](../outils/verif_calculs.py), et un [dashboard](https://ahmvdd.github.io/solvia-cto-case-study/dashboard/) permet de rejouer les arbitrages budgétaires.
- **Des décisions tracées**, y compris celles qu'on a annulées ([registre](08-decisions-registre.md), [ADR](adr/README.md)).

> **Critère de succès à J90** : Solvia peut démontrer qui décide, sur quelle preuve, avec quel coût et quel résultat.
