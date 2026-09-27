# Architecture Decision Records (ADR)

> Les décisions structurantes du plan Solvia, au format ADR : **contexte → décision → alternatives écartées → conséquences**.
> Une ADR ne se modifie pas : si la décision change, on en écrit une nouvelle qui la remplace. C'est ce qui rend l'historique fiable.

| ADR | Décision | Statut | Horizon |
|---|---|---|---|
| [ADR-001](ADR-001-haute-disponibilite-base.md) | Haute disponibilité de la base principale et astreinte avant toute autre évolution d'infrastructure | Proposée | J7 → J60 |
| [ADR-002](ADR-002-suspension-conservatoire-score.md) | Suspension conservatoire des décisions automatisées du Score si aucune garantie RGPD n'est retrouvée sous 48 h | Soumise au conseil | 48 h |
| [ADR-003](ADR-003-report-migration-monolithe.md) | Report de la migration du monolithe, au profit d'une stabilisation du module de facturation | Proposée | J0 → J90 |
| [ADR-004](ADR-004-reinvestissement-fiabilite.md) | Réinvestir 268 000 € dans la fiabilité à l'intérieur de la coupe de 20 % (scénario C) | Soumise au conseil | Exercice en cours |

## Format utilisé

```
# ADR-XXX : titre à l'impératif
Statut · Date · Décideur · Pièces
## Contexte          ce qui force la décision, avec les faits sourcés
## Décision          ce qu'on fait, en une phrase, puis le détail
## Alternatives      ce qu'on a écarté, et pourquoi
## Conséquences      ce que ça coûte, ce que ça rend possible, ce qu'on accepte de perdre
## Critère de révision   ce qui nous ferait changer d'avis
```

Le dernier bloc est notre ajout au format classique : **une décision qui ne dit pas ce qui la rendrait fausse n'est pas vérifiable.**
