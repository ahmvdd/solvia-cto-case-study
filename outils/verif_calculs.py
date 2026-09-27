"""
Vérification reproductible des chiffres du cas Solvia.

Écrit APRÈS l'exercice (qui interdisait toute production de code) :
chaque montant cité dans le dossier doit pouvoir être recalculé.

Usage : python3 outils/verif_calculs.py
"""

# --- Données du dossier (pièce entre parenthèses) --------------------------
TRESORERIE = 18_600_000          # P.1
BURN_MENSUEL = 1_330_000         # P.1
ARR = 11_200_000                 # P.1
PART_GESTION_CA = 0.90           # P.1
DOSSIERS_SCORE_MOIS = 28_000     # P.1
DOSSIERS_ANALYSE_P8 = 214_000    # P.8, sur 6 mois

FACTURE_CLOUD_MOIS = {           # P.3
    "compute_prod": 38_000, "bdd_prod": 21_000, "stockage": 9_000,
    "trafic": 7_000, "cluster_ml_exp": 24_000, "preprod": 11_000, "divers": 3_000,
}
BUDGET = {                       # P.4
    "masse_salariale": 3_040_000, "cloud": 1_356_000,
    "licences_saas": 421_000, "prestations": 680_000,
}
SIEGES = [                       # P.4 : (coût annuel, facturés, actifs)
    ("gestion de projet", 31_000, 210, 96),
    ("plateforme de code", 22_000, 60, 41),
    ("design", 14_000, 40, 6),
]
FIABILISATION = {                # budget révisé
    "infra_astreinte": 40_000, "sre": 80_000, "recrutement_facturation": 18_000,
    "salaire_facturation": 90_000, "analyse_rgpd": 40_000,
}
COUPES = {                       # budget révisé
    "cluster_gpu": 288_000, "sieges_saas": 35_700, "entrepot": 50_000,
    "outils_divers": 93_000, "cloud_prestations": 632_700,
}
PANNE_H = 6 + 8 / 60             # P.7 : 6 h 08


def eur(x):
    return f"{x:,.0f} €".replace(",", " ")


def section(titre):
    print(f"\n=== {titre} " + "=" * (60 - len(titre)))


def check(label, calcule, attendu, tol=1):
    ok = abs(calcule - attendu) <= tol
    print(f"{'OK ' if ok else '!! '} {label}: calculé {calcule:,.2f} / annoncé {attendu:,.2f}")
    return ok


section("Finances de l'entreprise")
check("Runway (mois)", TRESORERIE / BURN_MENSUEL, 14, tol=0.1)
print(f"    CA mensuel récurrent ≈ {eur(ARR / 12)} (dépend de la facturation)")
print(f"    Plafond ARR du Score (≤ 10 % du CA) ≈ {eur(ARR * (1 - PART_GESTION_CA))}")

section("Cloud")
total_cloud = sum(FACTURE_CLOUD_MOIS.values())
check("Facture cloud mensuelle", total_cloud, 113_000)
check("Cloud annuel = ligne budget", total_cloud * 12, BUDGET["cloud"])
print(f"    Hausse cloud 12 mois : {113_000 / 47_000 - 1:.0%} vs +22 % de clients")

section("Budget et coupe de 20 %")
budget = sum(BUDGET.values())
check("Budget total", budget, 5_497_000)
coupe = budget * 0.20
check("Coupe de 20 %", coupe, 1_099_400)
print(f"    Plafond : {eur(budget - coupe)}")

sieges = sum(cout * (fact - act) / fact for _, cout, fact, act in SIEGES)
check("Sièges inutilisés", sieges, 35_700, tol=10)
check("Total des coupes", sum(COUPES.values()), 1_099_400)
prouve = COUPES["cluster_gpu"] + COUPES["sieges_saas"]
check("Économies prouvées", prouve, 323_700)
check("À contractualiser", sum(COUPES.values()) - prouve, 775_700)

fiab = sum(FIABILISATION.values())
check("Fiabilisation", fiab, 268_000)
net = coupe - fiab
print(f"    Réduction nette (scénario B) : {eur(net)} = {net / budget:.1%}")
print(f"    Coupe brute nécessaire pour -20 % net (C) : {eur(coupe + fiab)}")
for nom, eco in [("brut", coupe), ("net", net)]:
    runway = TRESORERIE / (BURN_MENSUEL - eco / 12)
    print(f"    Runway avec économie {nom} : {runway:.2f} mois")

section("SLA de février (P.7)")
for jours in (28, 30, 31):
    dispo = 100 - PANNE_H / (jours * 24) * 100
    print(f"    Sur {jours} jours : {dispo:.3f} %")
print("    -> 99,15 % annoncé ne tient que sur un mois de 30 jours (février en compte 28)")
tranches = (99.9 - 99.15) / 0.1
print(f"    Tranches de 0,1 % manquantes : {tranches:.1f} -> pénalité {tranches * 5:.1f} % "
      "de la redevance mensuelle (35 à 40 % selon l'arrondi)")

section("Solvia Score")
mensuel_p8 = DOSSIERS_ANALYSE_P8 / 6
print(f"    P.8 : {mensuel_p8:,.0f} dossiers/mois vs {DOSSIERS_SCORE_MOIS:,} annoncés en P.1 "
      f"(+{mensuel_p8 / DOSSIERS_SCORE_MOIS - 1:.0%}) -> à rapprocher de la facturation")
print(f"    Écart de refus QPV / Paris : x{33.9 / 12.1:.1f}")
check("Deal en % de l'ARR (3,5 %)", ARR * 0.035, 392_000)
