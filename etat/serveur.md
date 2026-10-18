# Serveur du moteur V2

Mis à jour le 19/10/2026 à 00:18 · publication : **EN SERVICE (publie sur le site)**

## 🟢 **Tout va bien**

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-10-19 00:18:06  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-10-17 12:47:03  OK, 1148 avis collectés, 73 couples recalculés, 73 republiés en 26.6 min |
| Passe DECP hebdomadaire | 2026-10-17 16:00:21  Passe hebdomadaire DECP 2026-10-17_decp : terminée en 69.6 min, mémoire max 0 Mo ; 92 couples recalculés, 2 bloqués par la garde (M22_05, M22_07) ; 88 couples publiés, tables d'aide publiées |
| Contrôle quotidien | jamais |

**Machine maintenant** : mémoire 0.55 Go sur 7.6 · charge 0.12 · disque 21.3 % · échange 0.0 Go

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 17/10 12:47 | 1148 | 73 | 73 | 0 | 26.6 min |

### Passes DECP hebdomadaires

| Passe | Durée des couples | Mémoire max |
|---|---:|---:|
| 2026-10-17_decp | 41.8 min | — Mo |
| essai_pc | 26.3 min | 1616 Mo |
| essai_2026-10-16 | 26.4 min | 1950 Mo |
| essai_2026-10-16 | 25.6 min | 1950 Mo |
| essai_2026-10-16 | 23.9 min | 1950 Mo |
| essai_2026-10-16 | 21.9 min | 1950 Mo |

### Demandes des clients aujourd'hui

- 00:02 : (édition 2026-10, 366 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : non fait (identifiant de plus de 300 caractères dans la DECP)) en 132 s

### Contrôles quotidiens (14 derniers)

```
(absent)
```

## Tâches planifiées
```
NEXT                           LEFT LAST                         PASSED UNIT                     ACTIVATES
Mon 2026-10-19 00:19:00 CEST    49s Mon 2026-10-19 00:18:04 CEST 5s ago tenderhit-demandes.timer tenderhit-demandes.service
Mon 2026-10-19 06:30:00 CEST     6h Sun 2026-10-18 10:14:39 CEST      - tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-10-24 03:00:00 CEST 5 days Sun 2026-10-18 10:14:39 CEST      - tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                 - Mon 2026-10-19 00:18:04 CEST 5s ago tenderhit-relais.timer   tenderhit-relais.service

4 timers listed.
```

## Fin du journal du moteur
```
2026-10-17 12:47:03    M40_76 : 1 opportunités · rapport et opportunités · attributions anciennes retirées : 17 · 14 s
2026-10-17 12:47:03  OK, 1148 avis collectés, 73 couples recalculés, 73 republiés en 26.6 min
2026-10-17 12:51:02  C451_74 : demande en attente
2026-10-17 12:51:28    publié (édition 2026-10, 1 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 26 s
2026-10-17 12:51:28  C772_74 : demande en attente
2026-10-17 12:51:37    publié (édition 2026-10, 3 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 9 s
2026-10-17 16:00:21  Passe hebdomadaire DECP 2026-10-17_decp : terminée en 69.6 min, mémoire max 0 Mo ; 92 couples recalculés, 2 bloqués par la garde (M22_05, M22_07) ; 88 couples publiés, tables d'aide publiées
2026-10-17 18:36:08  Rejeu sur le serveur : rouge — 89 couples identiques au PC sur 90 comparés ; en écart ou en échec : C713_75 ; 6.2 s par couple (médiane), 12 min au total
2026-10-17 20:53:32  Rejeu sur le serveur : rouge — 89 couples identiques au PC sur 90 comparés ; en écart ou en échec : C713_75 ; 6.1 s par couple (médiane), 11 min au total
2026-10-18 10:18:02  C451_26 : demande en attente
2026-10-18 10:18:02    carte du 26 téléchargée
2026-10-18 10:18:11    publié (édition 2026-10, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 9 s
2026-10-18 10:18:11  C451_38 : demande en attente
2026-10-18 10:18:27    publié (édition 2026-10, 2 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 16 s
2026-10-18 10:18:27  C772_26 : demande en attente
2026-10-18 10:18:37    publié (édition 2026-10, 4 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 9 s
2026-10-18 10:18:37  C772_38 : demande en attente
2026-10-18 10:18:47    publié (édition 2026-10, 3 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 9 s
2026-10-18 10:39:05  M01_26 : demande en attente
2026-10-18 10:39:15    publié (édition 2026-10, 12 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 10 s
2026-10-18 14:32:18  tables du marché calculées : 327 activités, 1808816 attributions en 134.8 s, mémoire max 3497 Mo
2026-10-18 14:32:57  tables du marché : 2 activité(s) envoyée(s), 0 inchangée(s), 80617 lignes en 19 paquets
2026-10-18 16:18:15  tables du marché : 1 activité(s) envoyée(s), 0 inchangée(s), 17249 lignes en 5 paquets
2026-10-18 16:28:27  tables du marché : 323 activité(s) envoyée(s), 3 inchangée(s), 577760 lignes en 426 paquets
2026-10-18 17:58:46  tables du marché : 22 activité(s) envoyée(s), 304 inchangée(s), 993956 lignes en 251 paquets
2026-10-18 23:54:06  C712_69 : demande en attente
2026-10-18 23:54:15    publié (édition 2026-10, 2 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 8 s
2026-10-18 23:54:15  C713_69 : demande en attente
2026-10-18 23:54:25    publié (édition 2026-10, 11 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 10 s
2026-10-18 23:54:25  C715_69 : demande en attente
2026-10-18 23:54:31    publié (édition 2026-10, 1 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 5 s
2026-10-18 23:56:07  C712_74 : demande en attente
2026-10-18 23:56:15    publié (édition 2026-10, 3 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 8 s
2026-10-18 23:56:15  C713_74 : demande en attente
2026-10-18 23:56:23    publié (édition 2026-10, 10 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 9 s
2026-10-18 23:56:24  C715_74 : demande en attente
2026-10-18 23:56:31    publié (édition 2026-10, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 7 s
2026-10-19 00:00:04  C713_FR : demande en attente
2026-10-19 00:02:16    publié (édition 2026-10, 366 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : non fait (identifiant de plus de 300 caractères dans la DECP)) en 132 s
2026-10-19 00:18:09  Rejeu sur le serveur : rouge — 0 couples identiques au PC sur 0 comparés
```
