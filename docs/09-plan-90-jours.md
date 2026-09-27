# 09 · Plan à 90 jours

> Il ne promet pas zéro risque. **Il transforme des déclarations en preuves.**

```mermaid
flowchart LR
    S["<b>J0 → J7</b><br/>SÉCURISER<br/>accès, binômes,<br/>budget gelé,<br/>réponse commerciale,<br/>garanties Score"]
    T["<b>J8 → J30</b><br/>TESTER<br/>batch par le binôme,<br/>restauration, astreinte,<br/>audit Score,<br/>économies signées"]
    D["<b>J31 → J60</b><br/>DÉPLOYER<br/>haute disponibilité,<br/>documentation,<br/>suivi des incidents,<br/>renforts"]
    P["<b>J61 → J90</b><br/>PROUVER<br/>exercices répétés,<br/>conformité documentée,<br/>budget réalisé,<br/>revue du conseil"]
    S --> T --> D --> P
```

## Les 72 premières heures

| Quand | Action | Preuve |
|---|---|---|
| **H+4** | Cellule de crise CTO, Finance, RH et exploitation. Gel des changements non essentiels sur la facturation et le Score | Décisions consignées |
| **J1** | Inventaire des accès, secrets, batchs et dépendances. Binôme nommé | Aucun accès critique exclusif |
| **J1** | Extinction du cluster GPU | 24 k€/mois stoppés |
| **J2** | Le binôme exécute le parcours nominal, Thomas commente | Runbook v0 |
| **J2** | Préparation du prochain prélèvement avec la Finance | Checklist avant et après exécution |
| **J2** | Recherche des garanties du Score (AIPD, contrat, base légale) | Constat écrit au conseil |
| **J3** | Test d'un scénario d'échec, de la restauration et des alertes | Lacunes classées |

## Les indicateurs de pilotage

| Indicateur | Cible |
|---|---|
| Accès critiques partagés et validés | 100 % à J3 |
| Batchs exécutés sans action de Thomas | ≥ 1 avant son départ |
| Personnes capables d'exécuter le batch (hors Thomas) | 2 à J90 |
| Temps d'acquittement d'une alerte critique | < 10 min |
| Bascule de la base testée en exercice | Réussie à J60 |
| Économies contractualisées / 1 099 400 € | 100 % à J60 |
| Recommandations du Score suivies sans justification | En baisse mesurable après l'audit |
| Candidats informés du traitement, avec un recours | 100 % après mise en conformité |
| Systèmes critiques avec un bus factor de 1 | **0** à J90 |

## Le critère de succès à J90

> **Solvia peut démontrer qui décide, sur quelle preuve, avec quel coût et quel résultat.**

## Les trois validations demandées au conseil

1. **Valider** le plafond de 4 397 600 € et les coupes à contractualiser.
2. **Autoriser** les mesures conservatoires sur le Score et l'audit sous 48 h.
3. **Protéger** les relais facturation et production dans le plan de charge.

> *« Nous reviendrons avec des preuves, pas avec une nouvelle assurance non vérifiée. »*
