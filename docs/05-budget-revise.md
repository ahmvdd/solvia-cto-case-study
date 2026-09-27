# 05 · Budget technique révisé : injection A (−20 %)

> *Signé par le rôle Finance (Ahmed Sayeh).*
> Consigne du rôle : *« Le réflexe budgétaire coupe d'abord le futur (prestataires, recrutement, fiabilisation). Économiser aujourd'hui en payant plus cher dans six mois n'est pas une économie. »*

## 1. Le cadre imposé

| | Montant |
|---|---|
| Budget technique actuel (P.4) | **5 497 000 €** |
| Réduction imposée (injection A) | 20 %, avec effet immédiat |
| **À couper sur 12 mois** | **1 099 400 €** |
| **Nouveau plafond** | **4 397 600 €** |

Le principe n'est pas discutable, **seule la répartition l'est**, et chaque ligne doit être justifiée par une pièce.

## 2. Le point de départ

| Poste | Annuel | Détail |
|---|---|---|
| Masse salariale technique | 3 040 000 € | 36 CDI, 4 prestataires, 2 alternants (P.5) |
| Cloud | 1 356 000 € | 113 k€/mois × 12, dont le cluster GPU à 288 k€ (P.3) |
| Licences SaaS | 421 000 € | Dont Datadog 96 k€, entrepôt de données 118 k€, 17 outils divers 93 k€ (P.4) |
| Prestations externes | 680 000 € | **Non détaillées dans le dossier** (P.4) |

## 3. Le plan de coupe (1 099 400 €)

| Poste | Actuel | Coupe | Pièce | Échéance | Statut |
|---|---|---|---|---|---|
| **Cluster GPU solvia-ml-exp** | 288 000 | **288 000** | P.3 | Semaine 1 | ✅ Prouvé, immédiat. 3 % d'usage, censé être éteint, aucun impact produit |
| **Sièges SaaS inutilisés** (3 outils) | 67 000 | **35 700** | P.4 | 30 j | ✅ Prouvé. Sièges facturés supérieurs aux sièges actifs |
| Entrepôt de données (coupe partielle) | 118 000 | 50 000 | P.4 | 30 j | 🔍 À auditer : réduction de taille et de rétention, on garde le reporting DAF |
| 17 outils divers | 93 000 | 93 000 | P.4 | 30 j | 🔍 À auditer : sans propriétaire, doublons probables |
| Cloud hors cluster et prestations | 1 748 000 | 632 700 | P.3/4/9 | 30-60 j | 📝 Leviers identifiés, à contractualiser |
| **Total** | | **1 099 400** | | | |

**Calcul des sièges inutilisés** : 31 000 × 114/210 + 22 000 × 19/60 + 14 000 × 34/40 = 16 829 + 6 967 + 11 900 ≈ **35 700 €**.

### Les leviers de la ligne 5 (632 700 €)

| Levier | Gain estimé | Pièce |
|---|---|---|
| Arrêt des prestations non prioritaires (migration du monolithe non démarrée, connecteur n° 3) | 250 à 340 k€ | P.4, P.9 |
| Engagement sur 1 an du compute et de la base (réservations et plans d'économies, ~25 % sur 708 k€) | 150 à 200 k€ | P.3 |
| Préproductions de 4 à 2, et extinction la nuit et le week-end | ~66 k€ | P.3, P.6 |
| Ajustement de taille : trafic, stockage, divers | solde | P.3 |

### Honnêteté sur la solidité des chiffres

| Catégorie | Montant | Ce que ça veut dire |
|---|---|---|
| **Prouvé et immédiat** | **323 700 €** | Acquis dès maintenant, preuve par pièce |
| Identifié, à auditer | 143 000 € | La ligne existe, le montant exact reste à confirmer |
| À contractualiser | 632 700 € | Leviers réels, **pas encore signés, donc pas comptés comme acquis** |

## 4. Ce qu'on refuse de couper

| Poste préservé | Montant | Pourquoi |
|---|---|---|
| **Masse salariale** | 3 040 000 € | Un départ clé coûterait plus que l'économie (turnover de 29 %, 18 k€ par recrutement) |
| Sécurité et conformité | 47 000 € | Risque RGPD sur le Score |
| Datadog (observabilité) | 96 000 € | Indispensable après février. **L'alerte a fonctionné, c'est la réponse qui a manqué** |
| Prestations critiques | à trier | Tri contrat par contrat avant de couper |

## 5. La fiabilisation qu'on réinvestit (an 1)

| Poste | Montant | Pièce | Justification |
|---|---|---|---|
| Infrastructure et astreinte | 40 000 € | P.6, P.7 | Le chiffrage du SRE, ignoré en mars |
| Poste SRE (coût chargé estimé) | 80 000 € | P.5, P.6 | Si Marc part, plus personne ne sait déployer |
| Renfort facturation : recrutement | 18 000 € | P.5 | Coût moyen constaté en cabinet |
| Renfort facturation : salaire (estimé) | 90 000 € | P.6 | Bus factor de 1 sur ~933 k€/mois |
| Analyse d'impact RGPD (estimée) | 40 000 € | P.6, P.8 | 28 000 décisions/mois sans aucune analyse |
| **Total** | **268 000 €** | | |

> **Le message central** : **nos ~324 k€ d'économies prouvées financent nos 268 k€ de fiabilisation.** Les risques mortels sont couverts sans creuser le burn.

## 6. Provisions et risques (exposés, non décaissés)

| Risque | Exposition | Action |
|---|---|---|
| Pénalités de l'incident de février | **Non chiffrable** : 37,5 % de la redevance mensuelle × 11 bailleurs, redevances absentes | Réclamer les redevances |
| Deal Score v2 (392 à 400 k€) | Fonctionnalité non démarrée | **Ne pas le compter en revenu** |
| Litige commercial sur le Score | Non chiffrable | Écart entre la plaquette et la réalité, à évaluer avec un juriste |
| Certification de sécurité | Devis signé, montant absent | Obtenir le montant et le provisionner |

## 7. Effet sur la trésorerie

- La coupe brute allège le burn d'environ **91 600 €/mois**, et la coupe nette de la fiabilisation d'environ **69 300 €/mois**.
- Le runway passe de **14,0 mois à ~14,75 mois** (scénario B) ou ~15,0 mois (scénario C).
- **On gagne quelques semaines de runway**, sans dégrader la fiabilité ni l'encaissement. Le vrai levier de survie reste le CA et la Série C, pas le budget tech seul.

## 8. L'arbitrage soumis au conseil

| Scénario | Coupe brute | Fiabilisation | Réduction nette | % réel |
|---|---|---|---|---|
| A. −20 % brut, fiabilisation reportée | 1 099 400 € | 0 € | 1 099 400 € | 20,0 % ❌ *on coupe le futur* |
| B. −20 % brut, fiabilisation financée | 1 099 400 € | 268 000 € | 831 400 € | **15,1 %** |
| **C. −20 % net, fiabilisation financée (recommandé)** | **1 367 400 €** | 268 000 € | 1 099 400 € | **20,0 %** |

> **Le piège qu'on a évité** : annoncer « −20 % » alors qu'une fois la fiabilisation réinvestie, la réduction nette n'est que de 15,1 %. **On le dit au conseil plutôt que de le laisser découvrir.**

## 9. Calendrier

- **Semaine 1** : extinction du cluster GPU, gel des nouvelles dépenses SaaS.
- **J+30** : résiliation des sièges inutilisés, réduction de l'entrepôt de données, rationalisation des 17 outils, lancement de l'analyse RGPD et du recrutement du renfort facturation.
- **J+60** : contractualisation des leviers cloud et prestations, provisions pour la pénalité de février et la certification.

## 10. Hypothèses et données manquantes

- **Estimations à confirmer** : coûts chargés du SRE (~80 k€) et du renfort facturation (~90 k€), analyse RGPD (~40 k€), gain des engagements cloud (~25 %).
- **Données à réclamer** : redevance par bailleur, montant du devis de certification, détail des 680 k€ de prestations, part du deal déjà comptée dans l'ARR.
- **Source budgétaire fragile** : « consolidation manuelle, périmètre déclaratif » (P.4).
