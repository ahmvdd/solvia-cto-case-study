# 00 · Le cas et les règles du jeu

> Ceci est **notre synthèse** du dossier remis par l'école, pas une reproduction. Les pièces sont référencées **P.0 à P.10** dans tous les autres documents.

## La situation

On prend la **direction technique intérimaire** de Solvia SAS. Le CTO et cofondateur est parti il y a trois semaines, sans passation, dans des circonstances que le conseil « ne souhaite pas commenter ».

Le conseil attend trois choses sous 90 jours (P.0) :

1. un **état des lieux honnête**, parce qu'il soupçonne que ce qu'on lui a dit et ce qui est vrai divergent ;
2. un **plan de remise sous contrôle chiffré**, avec des arbitrages assumés ;
3. une **position claire sur le produit de scoring**, sujet signalé comme sensible.

Et un avertissement : *on ne nous demande pas de rassurer.*

## Les 11 pièces du dossier

| Pièce | Contenu | Fiabilité annoncée |
|---|---|---|
| P.0 | Lettre de mission du conseil | Remise en main propre |
| P.1 | Fiche entreprise : 180 personnes, 11,2 M€ d'ARR (+34 %), trésorerie de 18,6 M€, burn de 1,33 M€/mois, runway de 14 mois. Deux produits : **Solvia Gestion** (90 % du CA) et **Solvia Score** (scoring des candidatures de locataires, 28 000 dossiers/mois) | Reporting investisseurs |
| P.2 | Cartographie du SI : monolithe Rails, facturation, service de scoring en Python, Kubernetes, **PostgreSQL avec une instance principale unique** | Non revue depuis 9 mois, annotée « à jour ? » |
| P.3 | Facture cloud : **113 k€/mois (+140 % en 12 mois)**, dont un cluster GPU à 24 k€/mois **utilisé à 3 %** | Facture d'origine |
| P.4 | Budget technique : **5 497 000 €/an**. Aucun propriétaire pour 12 des 23 lignes, des sièges SaaS payés mais inutilisés | Consolidation manuelle |
| P.5 | Organisation : 36 CDI, 4 prestataires, 2 alternants. **1 seul SRE**, 29 % de turnover, 3 postes ouverts depuis 7 mois, pas d'astreinte | Registre du personnel |
| P.6 | Verbatims de six entretiens (EM, lead backend, data scientist, SRE, VP Product, dev front) | Retranscription partielle |
| P.7 | Rapport de l'incident du 14 février : panne de 6 h 08, « erreur humaine », statut « clos ». Un SLA de 99,9 % avec pénalités | Version publiée aux clients |
| P.8 | Note interne de la data scientist sur les **écarts géographiques des refus** du Score, restée sans réponse pendant 4 mois | Aucune réponse enregistrée |
| P.9 | Feuille de route « validée » : presque rien n'est livré, la migration du monolithe traîne depuis 3 exercices | Statut non confirmé |
| P.10 | Ce que le conseil attend comme livrables | — |

## Les personnages clés (fictifs)

| Personne | Rôle | Ce qu'elle apporte au cas |
|---|---|---|
| Claire Lemoine | Engineering Manager | La version « officielle », rassurante |
| Thomas Roussel | Lead Backend | « La facturation, c'est moi. Tout seul. » Épuisé |
| Camille Berger | Data Scientist | Le Score vendu ≠ le Score construit. A monté le cluster GPU |
| Marc Fontaine | SRE, seul à ce poste | La vraie chronologie de la panne, un budget de 40 k€ demandé et ignoré |
| Élodie Prat | VP Product | Un deal à 400 k€ vendu sur une fonctionnalité non démarrée |
| Antoine Mercier | Dev Front | « Personne ne relit le code de personne » |

## Le format

- **5 jours, 4 personnes, 4 rôles** (direction technique, personnes, finance, conformité et risque). Chaque rôle **signe** une section.
- Le rôle conformité a un **droit de veto** : une recommandation qui ne cite aucune pièce n'entre pas dans le dossier.
- **Aucune production de code**, de maquette ou de schéma d'architecture.
- **Des imprévus sont injectés en cours de route**, sans prévenir.

### Les imprévus qu'on a reçus

| Injection | Contenu | Impact |
|---|---|---|
| **A** | Le conseil impose **−20 % sur le budget tech**, avec effet immédiat | Refonte complète du budget ([05](05-budget-revise.md)) |
| **Démission** | Thomas Roussel démissionne, en épuisement, et veut partir avant la fin de son préavis de 3 mois | Plan de continuité de la facturation ([06](06-personnes-continuite.md)) |
| **Commercial** | Le deal est réévalué à 3,5 % de l'ARR (**392 k€**), et le client veut une livraison **sous 5 semaines** | Réponse écrite au directeur commercial ([07](07-reponse-commerciale.md)) |
| **Cas réel** | Annexe sur l'algorithme de contrôle de la CNAF | Éclaire la position sur le Score ([04](04-position-score.md)) |

## La grille d'évaluation

| Critère | Poids |
|---|---|
| Traçabilité : chaque affirmation renvoie à une pièce | **25 %** |
| Détection des contradictions | 20 % |
| Arbitrage : décisions chiffrées, datées, avec leur contrepartie | 20 % |
| Tenue sous pression face aux imprévus | 15 % |
| Honnêteté : savoir dire « je ne sais pas » | 10 % |
| Oral | 10 % |

> *« Une recommandation qui ne s'appuie sur aucune pièce du dossier vaut zéro, quelle que soit sa qualité de rédaction. »*
