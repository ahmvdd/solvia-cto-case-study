# 06 · Personnes et continuité de la facturation

> *« Les gens ne sont pas des ressources interchangeables. Certaines personnes de ce dossier ne peuvent pas être remplacées par une embauche. »* (consignes du rôle Personnes)
> *Plan d'action et analyse du départ de Thomas rédigés par Melvin Becue, adaptés pour ce repo.*

## Le constat

| Fragilité | Personne | Risque | Source |
|---|---|---|---|
| **Facturation** | Thomas Roussel, lead backend | Seul à savoir relancer le batch de prélèvement, sur ~933 k€/mois. Épuisé, 3 demandes d'aide ignorées | P.5, P.6 |
| **Production** | Marc Fontaine, seul SRE | « Si je démissionne, personne ne sait déployer en production » | P.5, P.6 |
| **Score** | Camille Berger, data scientist | Seule à connaître le modèle réel ; alerte ignorée | P.6, P.8 |
| **Encadrement** | Poste d'EM Data et Intégrations | Vacant, « assuré de fait par personne » | P.5 |

Il y a aussi **3 démissions en préavis**, **29 % de turnover**, **3 postes ouverts depuis 7 mois**.

## Injection : Thomas démissionne

Thomas démissionne, en épuisement sévère. Sa décision est irrévocable, et il ne veut pas faire ses 3 mois de préavis.

> **Le départ de Thomas ne crée pas le risque, il le révèle.** Solvia a laissé un module à ~1 M€/mois dépendre d'une seule personne sans documentation, sans suppléant et sans test de reprise.

### Pourquoi Solvia en est arrivée là

1. La criticité économique n'a jamais été traduite en exigences d'organisation.
2. La connaissance tacite a remplacé la documentation : l'entreprise **confondait « ça tourne » et « on maîtrise »**.
3. Le renfort a été promis (un Staff Engineer) mais jamais recruté.
4. **Une boucle de dépendance** : moins il avait de temps, moins il documentait ; moins il documentait, plus il devenait indispensable.

### Le principe

> **Le préavis est un cadre, pas un plan de continuité.** Le plan doit fonctionner même si Thomas devient indisponible demain.

### La passation par preuves

| Échéance | Action | Preuve attendue |
|---|---|---|
| **24 h** | Nommer un binôme Core et un second relais, et leur retirer leurs tâches concurrentes | Temps de passation bloqué dans les agendas |
| **J3** | Inventaire des batchs, accès, secrets, scripts, dépendances et scénarios d'échec | **Aucun accès critique détenu par une seule personne** |
| **J7** | Le binôme exécute le parcours nominal et un scénario d'échec sur des données de test | Première version du runbook |
| **J15** | Le binôme réalise le cycle complet sous le contrôle de la technique et de la Finance | Checklist validée |
| **J30** | Validation de l'autonomie réelle, ajustement du recrutement | **Un batch exécuté sans action de Thomas** |

> *Une présence en formation ne prouve pas l'autonomie. Seul un exercice réussi la valide.*

### Le coût maîtrisé

- **Couche 1** : un binôme interne récupère le minimum vital, sans coût salarial supplémentaire.
- **Couche 2** : Thomas passe d'opérateur unique à transmetteur, avec un périmètre réduit.
- **Couche 3** : le recrutement externe est lancé tout de suite, mais **l'arrivée est calée sur le moment où le socle interne est transféré**, pour éviter trois mois de double salaire.
- **Couche 4** : une deuxième personne assiste aux sessions clés, pour **ne pas recréer un bus factor de 1 avec le remplaçant**.

> Les 18 k€ de cabinet et le chevauchement salarial doivent être comparés aux **933 k€ mensuels exposés**.

### L'entretien avec Thomas

Un rapport de force peut obtenir de la présence, pas une transmission de qualité.

> *« J'ai compris que ta décision est définitive, et je ne vais pas essayer de te faire changer d'avis. Je ne peux pas accepter un départ immédiat sans sécuriser la facturation. Mais je ne te demande pas de continuer dans les mêmes conditions. Je veux retirer tout l'opérationnel non essentiel, te donner un seul binôme et limiter ta mission à une transmission mesurable. Si l'autonomie est atteinte plus tôt, on réévalue la date de sortie avec les RH. Dis-moi ce qu'il faut enlever pour que ce soit tenable. »*

Les questions courtes, pour une personne très fermée :

- Si tu pars demain, qu'est-ce qui casse en premier ?
- Quelles sont les trois connaissances à récupérer cette semaine ?
- Qu'est-ce que tu refuses de continuer à porter ?
- Qui peut apprendre le plus vite avec toi ?
- Qu'est-ce qui prouvera que ton binôme est autonome ?

> ⚠️ **Limite** : l'épuisement relève de la santé au travail. La direction technique ne pose pas de diagnostic et ne fait pas pression. Elle agit avec les RH, la médecine du travail et le cadre juridique.

## Les postes ouverts

| Poste | Décision | Pourquoi |
|---|---|---|
| **SRE** | ✅ Maintenu en priorité | Un seul SRE, une panne de 6 h, 3 quasi-incidents |
| **Renfort facturation** (à la place du Staff Engineer) | ✅ Maintenu en priorité, avec un profil recentré | Le besoin réel est la continuité de la facturation, pas un profil générique |
| **Data Engineer** | ⏸️ Gelé jusqu'au bilan de capacité | Le Score est en audit : on ne construit pas dessus avant de savoir |

## Qui on garde

**Tout le monde.** Aucune coupe de masse salariale. La priorité est de **retenir** Marc (SRE) et Camille (data scientist) : ce sont les deux prochains Thomas si rien ne change.

## La gouvernance à installer

| Livrable | Validateur | Condition de clôture |
|---|---|---|
| Runbook facturation | Binôme et Finance | Une personne autre que Thomas exécute le batch **avec le document seul** |
| Registre des accès et secrets | Direction tech | Aucun compte critique personnel |
| Catalogue des incidents | Équipe backend | Les 5 incidents les plus probables ont un diagnostic et un rollback |
| **Matrice de suppléance** | Direction tech | **Chaque système critique a un titulaire et au moins un suppléant entraîné** |

**Indicateur-clé** : aucun système critique avec un bus factor de 1 à J90.
