# 02 · Diagnostic : établi, probable, inconnu

## La méthode

Chaque affirmation reçoit un statut, et chaque statut entraîne une conduite différente.

| Statut | Définition | Conduite |
|---|---|---|
| **ÉTABLI** | Une pièce, un calcul reproductible ou un événement explicite | On l'affirme et on le chiffre |
| **PROBABLE** | Une inférence motivée | Elle justifie une **mesure conservatoire**, pas une conclusion |
| **INCONNU** | Une donnée absente, non testée ou ambiguë | On ouvre une **action datée** pour l'établir |

> **La règle d'or à l'oral** : *« Ce qui est établi, c'est X. Ce qui ne l'est pas, c'est Y. Voici l'action qu'on ouvre pour l'établir. »*

## Trois risques qui exigent une décision immédiate

| Risque | Constat | Décision | Sources |
|---|---|---|---|
| **Facturation** | 90 % du CA passe par le produit historique. Une seule personne sait relancer le batch de prélèvement | Un **binôme nommé sous 24 h**, un exercice avant J15 | P.1, P.5, P.6 |
| **Production** | Un seul SRE, pas d'astreinte, 6 h 08 d'arrêt, 3 quasi-incidents depuis | Un relais, des **sauvegardes et une restauration vérifiées à J7** | P.5, P.6, P.7 |
| **Solvia Score** | 28 000 décisions/mois, candidats non informés, écart géographique inexpliqué, sous-traitant américain non documenté | **Suspension conservatoire soumise au conseil** | P.1, P.6, P.8 |

> **Priorité commune** : protéger les fonctions vitales **avant** toute nouvelle promesse commerciale.

## Le tableau complet

### ÉTABLI

- Panne totale de **6 h 08** (de 03 h 12 à 09 h 20), une alerte non traitée pendant **4 h 28**, une remise en service manuelle en 1 h 40 (P.6, P.7).
- Pas de bascule automatique sur la base principale, pas d'astreinte formelle (P.2, P.5, P.6).
- **3 quasi-incidents** depuis février, aucun suivi retrouvé (P.6, P.7).
- Cluster GPU à **3 % d'usage**, actif depuis 14 mois, **288 k€/an** (P.3).
- 12 lignes budgétaires sur 23 sans propriétaire ; sièges SaaS : 210 payés pour 96 actifs, 60 pour 41, 40 pour 6 (P.4).
- Score : **61 %** des recommandations suivies sans modification, candidat **non informé** du traitement automatisé (P.8).
- Taux de refus de **33,9 %** dans les quartiers prioritaires, contre **12,1 %** à Paris intra-muros (P.8).
- Données d'entraînement réelles : ~190 000 dossiers, pas 2 millions (P.6).
- Alerte de la data scientist au CTO il y a 4 mois, sans réponse (P.8).

### PROBABLE (justifie une mesure conservatoire)

- L'écart géographique du Score traduit un **effet de variables proxy** (type de contrat, garant, ancienneté), même si le code postal n'est pas une variable d'entrée. Ça justifie un audit, **pas une conclusion de discrimination**.
- Le départ de Thomas avant la fin de son préavis rendrait la facturation **inopérable** lors d'une fin de mois.
- Une part de l'ARR repose sur des promesses non tenues (deal Score v2), donc **un ARR potentiellement surévalué**.

### INCONNU (une action datée pour chaque point)

| Inconnu | Action | Échéance |
|---|---|---|
| Montant exact des pénalités SLA (redevances et règle d'arrondi absentes) | Note contractuelle DAF et conseil juridique | J+7 |
| Ce que la direction a fait entre l'alerte de Camille et aujourd'hui | Revue des échanges, entretien avec le conseil | J+7 |
| AIPD, base légale, contrat de sous-traitance, localisation des données du Score | Audit de conformité | **48 h** (garanties minimales) puis J+30 |
| État réel des sauvegardes, RTO et RPO | Test de restauration chronométré | J+7 |
| Perte ou corruption de données le 14 février | Contrôle d'intégrité formel | J+7 |
| Détail des 680 k€ de prestations externes | Revue contrat par contrat | J+30 |

## La lecture « Finance » du diagnostic

> *« Solvia n'a pas un problème de revenus, elle a un problème de discipline financière. L'argent rentre, mais personne ne le pilote. »*

Six défaillances :

1. **Pilotage au chiffre d'affaires, pas à la trésorerie**, avec 1,33 M€ perdus chaque mois.
2. **Aucun contrôle des coûts** : le cloud prend +140 % sans réponse.
3. **Des chiffres non fiables**, en « consolidation manuelle, périmètre déclaratif ».
4. **Pas de gouvernance budgétaire** : 12 lignes sur 23 sans propriétaire.
5. **Un CA de qualité incertaine** : un Score vendu sur des promesses inexactes, un deal sur une fonctionnalité non démarrée.
6. **Des passifs cachés non provisionnés** : la pénalité de février, le devis de certification.
