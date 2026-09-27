# ADR-004 : Financer la fiabilité à l'intérieur de la coupe de 20 %

**Statut** : Soumise au conseil · **Décideur** : conseil d'administration, sur proposition de la Finance · **Pièces** : P.3, P.4, P.5, P.6, P.7, injection A

## Contexte

- Le conseil impose **−20 % sur le budget technique** de 5 497 000 €, soit **1 099 400 €**, avec effet immédiat (injection A). Le principe n'est pas négociable, la répartition l'est.
- Des économies sans risque existent : un cluster GPU à 3 % d'usage (**288 000 €/an**, P.3), des sièges SaaS jamais utilisés (**35 700 €**, P.4).
- En face, des trous de fiabilité documentés : pas d'astreinte, un seul SRE, une facturation portée par une personne, un Score sans AIPD (P.5, P.6, P.7).
- La consigne du rôle Finance : *« Économiser aujourd'hui en payant plus cher dans six mois n'est pas une économie. »*

## Décision

**Réinvestir 268 000 € dans la fiabilité, et atteindre malgré tout −20 % net, en portant la coupe brute à 1 367 400 € (scénario C).**

| Réinvestissement | Montant |
|---|---|
| Infrastructure et astreinte | 40 000 € |
| Poste SRE (estimé) | 80 000 € |
| Renfort facturation : recrutement | 18 000 € |
| Renfort facturation : salaire (estimé) | 90 000 € |
| Analyse d'impact RGPD (estimée) | 40 000 € |
| **Total** | **268 000 €** |

Et une règle de présentation : **seuls les 323 700 € prouvés sont comptés comme acquis.** Le reste est « à auditer » ou « à contractualiser », et il est présenté comme tel.

## Alternatives écartées

| Scénario | Réduction nette | Pourquoi on l'écarte |
|---|---|---|
| **A. −20 % brut, fiabilité reportée** | 1 099 400 € (20,0 %) | Le chiffre plaît au conseil, mais il laisse ouverts les trois risques qui peuvent coûter bien plus que la coupe. C'est exactement « couper le futur ». |
| **B. −20 % brut, fiabilité financée** | 831 400 € (15,1 %) | Honnête et défendable, mais il ne respecte pas la demande du conseil. On le présente comme repli si le scénario C n'est pas atteignable. |
| **Couper la masse salariale** | — | Turnover de 29 %, 18 k€ par recrutement, des personnes irremplaçables par une embauche (P.5). Une coupe qui provoque un départ clé coûte plus qu'elle ne rapporte. |

## Conséquences

- **Il faut trouver 268 000 € de coupes brutes en plus**, sur les prestations externes (680 k€, non détaillées dans le dossier) et les engagements cloud. Ce n'est **pas prouvé aujourd'hui** : c'est la condition de réussite du scénario C, et on le dit.
- **Runway** : de 14,0 à ~15,0 mois dans le scénario C, contre ~14,75 dans le B. Quelques semaines, pas un sauvetage : le budget tech seul ne sauve pas Solvia.
- **Ce que ça rend possible** : couvrir les risques mortels sans demander un euro de plus au conseil.
- Les chiffres se rejouent dans le [simulateur budgétaire](https://ahmvdd.github.io/solvia-cto-case-study/dashboard/).

## Critère de révision

Si l'audit des prestations à J30 montre que les 268 000 € supplémentaires ne sont pas trouvables sans toucher à des prestations critiques, **on revient au scénario B** et on l'assume devant le conseil, plutôt que de couper la fiabilité en silence.
