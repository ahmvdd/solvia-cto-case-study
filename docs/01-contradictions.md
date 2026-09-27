# 01 · Relevé des contradictions

> Rendu le soir du jour 1. Il n'est pas noté pour lui-même, mais **tout le reste en dépend** : on ne décide pas sur une pièce que contredit une autre.

## Les six contradictions certaines (présentées au conseil)

| # | Sujet | Version A | Version B | Pièces | Ce qu'on retient |
|---|---|---|---|---|---|
| 1 | **Feuille de route** | « Validée », présentée comme tenue | Livrée en retard ou non démarrée sur 5 lignes sur 7 | P.6 (VP Product), P.9 | Le statut « validé » ne prouve pas une capacité |
| 2 | **Facturation** | « On est trois dessus, c'est maîtrisé » (EM) | « C'est moi, tout seul, depuis deux ans et demi » (Lead Backend) | P.6 | **Bus factor = 1** sur ~933 k€/mois |
| 3 | **Cause de l'incident** | « Erreur humaine lors d'un déploiement » | Base unique sans bascule, pas d'astreinte, préprod non représentative | P.7, P.6 (SRE) | Un déclencheur n'est pas une cause racine |
| 4 | **Clôture de l'incident** | Statut « clos » | 3 quasi-incidents depuis, aucune action tracée | P.7, P.6 | Le risque est toujours ouvert |
| 5 | **Demande budgétaire du SRE** | « Jamais de demande écrite » (EM) | Chiffrage de 40 k€ et d'un poste envoyé sur Slack, acquitté d'un 👍 | P.6 | Une demande a bien existé ; il n'y a juste pas de circuit formel |
| 6 | **Données d'entraînement du Score** | « IA propriétaire entraînée sur plus de 2 millions de dossiers » | Gradient boosting sur ~190 000 dossiers, plus une API externe américaine non documentée | P.1, P.6 | Un écart d'un facteur 10 entre ce qu'on vend et ce qu'on a construit, donc un **risque commercial et juridique** |

**Celle qu'on a gardée « à vérifier »** : le cluster GPU. La data scientist le croyait éteint (P.6), la facture montre qu'il tourne depuis 14 mois (P.3). Ce n'est pas une contradiction entre deux affirmations, plutôt une **croyance démentie par un fait**.

> **Parti pris** : on donne un nombre exact et on ne confond pas *contradiction* (deux pièces qui s'opposent) et *anomalie* (une pièce qui révèle un problème).

## Ce qu'on a trouvé en plus à la relecture (après la soutenance)

Avec du recul, et en recalculant tout (voir [`outils/verif_calculs.py`](../outils/verif_calculs.py)), d'autres tensions apparaissent. Elles n'étaient pas dans notre rendu. On les ajoute ici parce que **c'est exactement le travail qu'un CTO entrant devrait faire.**

| # | Tension | Calcul | Pourquoi c'est important |
|---|---|---|---|
| 7 | **Volume du Score** : 28 000 dossiers/mois (P.1), mais 214 000 dossiers analysés sur 6 mois (P.8) | 214 000 ÷ 6 = **~35 700/mois**, soit +27 % | Soit le volume facturé est sous-déclaré, soit l'analyse inclut autre chose (des tests, des doublons ?). Il faut rapprocher la facturation à l'usage des logs du service de scoring |
| 8 | **Disponibilité de février** : 99,15 % annoncés (P.7) | 6 h 08 sur 28 jours (février) = **99,09 %**. On retrouve 99,15 % seulement sur 30 jours | La base de calcul du SLA n'est pas claire, et la pénalité en dépend (7 ou 8 tranches de 0,1 %) |
| 9 | **Dérive du cloud** « liée à la croissance » (P.3) | Cloud +140 % pour +22 % de clients (et +34 % d'ARR) | La croissance n'explique pas la dérive. Le cluster GPU seul pèse 288 k€/an |
| 10 | **Effectif technique** : « 42 déclarés » (P.1) | Registre : 36 CDI + 4 prestataires + 2 alternants = 42 | Le total tombe juste, mais il **compte les prestataires et les alternants** comme de la capacité. La capacité CDI réelle est de 36, moins 3 démissions en cours |
| 11 | **Certification sécurité** : « devis signé » (P.9) | Montant absent du budget (P.4) | Un engagement non provisionné |
| 12 | **Encadrement** : un EM Data et Intégrations « assuré de fait par personne » (P.5) | Les équipes Data et Intégrations comptent 14 personnes | 14 personnes sans manager, et c'est là qu'est le Score |
