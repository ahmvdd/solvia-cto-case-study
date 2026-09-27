# 08 · Décisions, renoncements et registre

> *« Le conseil retiendra particulièrement ce que vous décidez de ne pas faire, et pourquoi. »* (P.10)

## Nos arbitrages

| Verbe | Quoi | Pourquoi |
|---|---|---|
| **MAINTENIR** | Facturation, production, sécurité, observabilité | Fonctions vitales, risque immédiat |
| **FINANCER** | Résilience, SRE, relève de la facturation, analyse d'impact RGPD (268 k€) | Dans le plafond annuel de 4 397 600 € |
| **REPORTER** | Migration du monolithe (phase 1), connecteur métier n° 3 | Pas de capacité démontrée. La migration traîne depuis 3 exercices sans spécification (P.9) |
| **REFUSER** | Une promesse de fonctionnalité automatisée et conforme sous 5 semaines | Ni la faisabilité ni la conformité ne sont établies |
| **SOUMETTRE** | La suspension conservatoire du Score | Décision du conseil après vérification sous 48 h |

## Ordre de priorité assumé

1. **Sécuriser la facturation** (933 k€/mois) et le prochain batch.
2. **Sécuriser la production** : astreinte, restauration testée, puis haute disponibilité.
3. **Mettre le Score sous contrôle** : garanties sous 48 h, audit, information des candidats.
4. **Tenir le budget** : −20 %, avec 323,7 k€ prouvés dès la semaine 1.
5. **Recruter** le SRE et le renfort facturation.
6. Seulement ensuite : de **nouveaux engagements produit**.

## Ce qu'on décide explicitement de NE PAS faire

- ❌ **Couper la masse salariale** pour tenir les −20 %.
- ❌ **Lancer la migration du monolithe** : c'est un chantier fantôme depuis 3 ans, et le lancer maintenant ajouterait du risque au moment le plus fragile.
- ❌ **Confirmer le Score v2 sous 5 semaines.**
- ❌ **Couper Datadog, la sécurité ou la conformité.**
- ❌ **Recruter le Data Engineer** avant la fin de l'audit du Score.
- ❌ **Désigner un coupable** pour l'incident de février.
- ❌ **Annoncer un montant de pénalités** sans les redevances.

## Registre des décisions (extrait)

> Tenu par le rôle conformité. Chaque décision a une date, une source, un responsable, et une preuve de clôture. Les décisions annulées restent visibles.

| ID | Décision | Source | Responsable | Échéance | Preuve de clôture | Statut |
|---|---|---|---|---|---|---|
| D-01 | Éteindre le cluster GPU solvia-ml-exp | P.3, P.6 | Direction tech | S1 | Facture du mois suivant sans la ligne | Proposée |
| D-02 | Nommer un binôme facturation | P.6 | Personnes | 24 h | Nom et agenda bloqué | Proposée |
| D-03 | Mettre en place une astreinte et un test d'alerte hors heures | P.6, P.7 | Direction tech | J7 | Acquittement en moins de 10 min | Proposée |
| D-04 | Test de restauration chronométré | P.2, P.6 | SRE et Lead Backend | J7 | RTO et RPO mesurés | Proposée |
| D-05 | Rechercher les garanties minimales du Score | P.6, P.8 | Conformité | 48 h | AIPD, contrat, base légale, ou constat d'absence | Proposée |
| D-06 | Suspendre le Score si aucune garantie n'est trouvée | P.8 | **Conseil** | après D-05 | Délibération du conseil | Soumise |
| D-07 | Refuser la livraison à 5 semaines, proposer un cadrage | P.6, P.9 | Direction tech | Immédiat | Réponse écrite envoyée | Proposée |
| D-08 | Plafond de 4 397 600 € et réinvestissement de 268 k€ | P.4, injection A | Finance | S1 | Budget signé | Soumise |
| D-09 | Reporter la migration du monolithe | P.9 | Direction tech | — | Retrait de la feuille de route | Proposée |
| D-10 | Geler le poste de Data Engineer | P.5 | Personnes | — | Bilan de capacité à J30 | Proposée |
| D-11 | ~~Couper 100 % de l'entrepôt de données (118 k€)~~ | P.4 | Finance | — | — | **Annulée** : le reporting de la DAF en dépend, on passe à une coupe partielle de 50 k€ |
| D-12 | ~~Classer la ligne cloud et prestations « à trouver »~~ | P.3, P.4 | Finance | — | — | **Annulée** : leviers identifiés un par un (voir [05](05-budget-revise.md)) |

> Les lignes D-11 et D-12 montrent une chose importante : **on a changé d'avis, et on l'a tracé.**
