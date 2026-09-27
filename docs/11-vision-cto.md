# 11 · Au-delà de la copie : vision CTO

> Ce document a été écrit **après** la soutenance. Il ne faisait pas partie du rendu noté.
> Il répond à une question simple : *si c'était une vraie entreprise, et qu'on restait après les 90 jours, qu'est-ce qu'on ferait que la grille ne demandait pas ?*

---

## 1. Recadrer le problème : Solvia n'a pas une dette technique, elle a une dette de décision

Toutes les crises du dossier ont la même forme :

| Crise | Quelqu'un savait | Personne n'a décidé |
|---|---|---|
| Panne de février | Le SRE avait chiffré le correctif (40 k€ et un poste) | 👍 sur Slack |
| Facturation | Thomas avait demandé de l'aide 3 fois | « On recrutera un Staff Engineer » |
| Score | Camille avait envoyé une analyse des écarts | Aucune réponse |
| Cluster GPU | Camille pensait qu'il était éteint | Personne n'était propriétaire |
| Cloud +140 % | La DAF avait demandé 3 fois une explication | « C'est la croissance » |

**L'information remontait. Rien ne la transformait en décision.** Le vrai livrable d'un CTO ici n'est pas un plan technique : c'est un **circuit de décision** où une alerte a forcément un propriétaire, une échéance et une réponse écrite.

**Proposition concrète : un « registre des risques signalés »**, visible du comité de direction, où toute alerte d'un salarié reçoit une réponse sous 10 jours ouvrés (accepter, refuser avec justification, ou reporter avec une date). Le coût est quasi nul. L'effet : Marc, Thomas et Camille auraient chacun eu une réponse.

## 2. Transformer la conformité du Score en avantage commercial

Notre position était défensive (audit, suspension conservatoire). Une position offensive est possible :

- Le Score vise des **bailleurs institutionnels**, souvent sociaux ou parapublics, qui ont eux-mêmes des obligations d'égalité d'accès au logement. **Ils ont intérêt à acheter un score qu'ils peuvent justifier.**
- La jurisprudence européenne va dans ce sens : dans l'arrêt **SCHUFA (CJUE, C-634/21, décembre 2023)**, la Cour a jugé que l'établissement d'un score peut constituer en lui-même une *décision automatisée* au sens de l'article 22 du RGPD, dès lors qu'un tiers s'y fie de manière déterminante. Avec **61 % de suivi sans modification**, Solvia est exactement dans ce cas de figure. Il faut le faire confirmer par un juriste, mais c'est un argument de plus pour gouverner le Score maintenant.
- La qualification au regard de l'**AI Act** (système à haut risque ou non) est **à établir** : c'est un chantier de l'audit, pas une conclusion.

**Le repositionnement** : passer d'une « IA propriétaire » à une **« aide à la décision explicable et auditable »** :

- chaque recommandation est accompagnée des **3 facteurs déterminants**, lisibles par l'agence et le candidat ;
- une **justification obligatoire** quand l'agence suit un avis défavorable sans examen ;
- un **rapport d'équité trimestriel** par zone et par profil, remis aux bailleurs ;
- un **canal de recours** pour le candidat.

Ce qui est aujourd'hui un risque (le cas CNAF montre ce qu'il coûte) devient un **argument de vente** que les concurrents « boîte noire » ne peuvent pas offrir.

## 3. Installer une vraie discipline FinOps, pas une coupe ponctuelle

La coupe de 20 % règle le symptôme. La cause, c'est que **12 lignes sur 23 n'ont pas de propriétaire**.

- **Chaque ligne de coût a un propriétaire nommé**, sinon elle est coupée au prochain trimestre.
- **Un tag obligatoire sur chaque ressource cloud** (équipe, projet, date d'expiration pour les expérimentations). Le cluster GPU aurait expiré au bout de 30 jours.
- **Une revue mensuelle de 30 minutes** avec la DAF : écart au budget, top 5 des hausses, décisions.
- **Un coût unitaire** : le cloud par client actif et par dossier scoré. C'est la seule manière de répondre sérieusement à « c'est la croissance » (+140 % de cloud pour +22 % de clients).

## 4. Mesurer le « bus factor » comme un indicateur financier

On a traité la dépendance à Thomas comme un risque RH. C'est d'abord un **risque sur le chiffre d'affaires**.

> **Exposition = CA dépendant du système ÷ nombre de personnes autonomes dessus**

| Système | CA dépendant | Personnes autonomes | Exposition par personne |
|---|---|---|---|
| Facturation | ~933 k€/mois | 1 | **933 k€** |
| Production | 100 % du CA | 1 (Marc) | **tout** |

Présenté comme ça au conseil, un recrutement à 90 k€/an n'est plus une dépense : c'est une **assurance sur ~11 M€ d'ARR**.

## 5. Changer le rapport entre produit et technique

Élodie Prat : *« La technique dit non à tout, tard, et sans expliquer. »*
Claire Lemoine : *« On apprend les engagements commerciaux quand ils sont déjà signés. »*

**Elles décrivent le même problème des deux côtés.** La solution n'est pas de donner raison à l'une ou à l'autre :

- **aucun engagement client sur une fonctionnalité non démarrée sans l'avis écrit de la technique**, qui répond sous 5 jours ;
- en échange, la technique s'engage à donner un **« oui, si »** ou un **« non, parce que »** chiffré, jamais un non sec ;
- une **capacité réservée** (par exemple 20 % du temps) à la fiabilité et à la dette, visible dans la feuille de route, pour qu'elle ne soit plus « ce qui fait déraper les dates ».

## 6. Ce qu'on referait différemment

On le dit franchement, parce que c'est aussi ça, le rôle :

- **On a sous-exploité le calcul.** Les contradictions n° 7 et n° 8 (volume du Score, base du SLA) auraient pu sortir le jour 1 en recalculant chaque chiffre. D'où le script [`outils/verif_calculs.py`](../outils/verif_calculs.py).
- **On aurait dû chiffrer plus tôt le coût de la suspension du Score.** Le plafond de ~1,12 M€ (au plus 10 % de l'ARR) était déductible de P.1 dès le départ.
- **On a d'abord classé 564 k€ en « à trouver ».** C'était honnête, mais faible. La version finale détaille les leviers : c'est la bonne correction, et elle est tracée dans le registre (D-12).
- **La stratégie de rétention de Marc et de Camille** mérite un plan aussi précis que celui de Thomas : ce sont les deux prochains points de rupture.

## 7. Ce que cet exercice dit de notre manière de diriger

1. **On commence par ce qu'on ne sait pas**, parce que c'est là que se cachent les décisions dangereuses.
2. **On chiffre tout**, y compris l'éthique, parce qu'un conseil ne peut arbitrer que ce qu'il peut comparer.
3. **On protège les gens**, parce qu'un plan de continuité qui épuise ses relais recrée la crise.
4. **On dit non à une date, jamais sèchement à un client.**
5. **On change d'avis, et on le trace.**
