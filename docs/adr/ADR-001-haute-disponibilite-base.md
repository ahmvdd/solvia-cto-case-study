# ADR-001 : Rendre la base principale hautement disponible, astreinte d'abord

**Statut** : Proposée · **Décideur** : direction technique intérimaire · **Pièces** : P.2, P.5, P.6, P.7

## Contexte

- Le 14 février, la base PostgreSQL principale est tombée : **6 h 08 d'indisponibilité totale** (P.7).
- L'alerte est partie à 03 h 12. Personne ne l'a vue avant 07 h 40, faute d'astreinte (P.6).
- La remise en service a été **manuelle** : il existe un réplica de lecture, mais aucune bascule automatique (P.2, P.6).
- La préproduction ne ressemble pas à la production (P.6), et un seul SRE sait déployer (P.5).
- **3 quasi-incidents** similaires depuis février (P.6).
- Le SRE avait chiffré la remise à niveau en mars : **40 000 €/an d'infrastructure et un poste** (P.6).
- 11 contrats prévoient un SLA de 99,9 % avec pénalités (P.7).

## Décision

**On traite d'abord la réponse humaine, puis la reprise, puis la bascule automatique, dans cet ordre.**

1. **J7 : astreinte** avec rotation, escalade et test d'alerte hors heures acquitté en moins de 10 minutes.
2. **J7 : test de restauration chronométré**, pour mesurer le RTO et le RPO réels au lieu de les supposer.
3. **J15 : conception** d'une base hautement disponible, avec promotion automatique du réplica en cas de panne.
4. **J60 : exercice de bascule** en conditions contrôlées, avec la preuve du RTO obtenu.

L'ordre compte : le 14 février, la panne a duré 1 h 40, mais **l'absence de réponse en a duré 4 h 28**. L'astreinte seule aurait divisé l'arrêt par trois, pour un coût bien plus faible que la haute disponibilité.

## Alternatives écartées

| Alternative | Pourquoi on l'écarte |
|---|---|
| **Statu quo et « renforcement des procédures »** (la réponse officielle) | C'est ce qui a été fait après février, et 3 quasi-incidents ont suivi (P.7). Une procédure ne remplace ni une astreinte ni une bascule. |
| **Haute disponibilité d'abord, astreinte ensuite** | Plus spectaculaire, mais elle traite la cause qui a coûté 1 h 40 et laisse ouverte celle qui a coûté 4 h 28. Elle dépend aussi du seul SRE disponible. |
| **Migrer vers une autre base ou un service managé différent** | Un chantier de plusieurs mois, porté par une équipe sans capacité (P.5), au moment le plus fragile. Il ajoute du risque avant d'en retirer. |
| **Tout externaliser à un infogérant** | Déplace le bus factor sans le supprimer, et aucune pièce ne chiffre ce coût. À réévaluer après J90. |

## Conséquences

- **Coût** : 40 000 €/an d'infrastructure et 80 000 € (estimés) pour un second SRE, financés dans la coupe de 20 % ([ADR-004](ADR-004-reinvestissement-fiabilite.md)).
- **Charge humaine** : une astreinte pèse sur l'équipe. Elle doit être compensée et tournante, sinon elle crée le prochain épuisement.
- **Ce qu'on accepte** : pas de chantier d'infrastructure « de fond » pendant 90 jours.
- **Ce que ça rend possible** : tenir le SLA, et pouvoir le **prouver** aux 11 bailleurs.

## Critère de révision

On revoit cette décision si le test de restauration de J7 montre une **perte de données** (RPO supérieur à zéro sur les transactions de facturation) : la priorité passerait alors à la sauvegarde, avant la bascule.
