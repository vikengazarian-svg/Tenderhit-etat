# Serveur du moteur V2

Mis à jour le 26/11/2026 à 10:39 · publication : **EN SERVICE (publie sur le site)**

## 🟢 **Tout va bien**

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-26 10:39:03  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-26 07:31:13  OK, 719 avis collectés, 365 couples recalculés, 101 republiés en 61.2 min |
| Passe DECP hebdomadaire | 2026-11-21 04:33:49  Passe hebdomadaire DECP 2026-11-21_decp : terminée en 93.8 min, mémoire max 4287 Mo ; 360 couples recalculés, 1 bloqués par la garde (M01_58) ; 352 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-26 07:35:50  Contrôle du 26/11 : vert — 365 couples identiques au site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 0.58 Go sur 7.6 · charge 1.12 · disque 37.8 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : +0.7 point(s) par semaine · 80 % dans **64.9 semaine(s)**

```
Mesure du 2026-11-26 05:45 :
  entrepot/sources                            3.57 Go
  entrepot/decp                               2.06 Go
  entrepot/boamp                              1.40 Go
  entrepot/passes                             1.23 Go
  production/controles                        0.72 Go
  entrepot/execution                          0.72 Go
  entrepot/marche                             0.26 Go
  production/publies                          0.24 Go
  entrepot/photographie                       0.23 Go
  entrepot/etiquettes                           38 Mo
  entrepot/referentiel                          16 Mo
  entrepot/avis                                  3 Mo
  logs                                           3 Mo
  production/(fichiers)                          3 Mo
  entrepot/sirene                                2 Mo
  entrepot/tmp                                   2 Mo
  entrepot/mesures.jsonl                         2 Mo
  production/rejeu                               0 Mo
  entrepot/sources_temoin.jsonl                  0 Mo
  entrepot/manifeste.json                        0 Mo
Croissance par dossier (depuis 2026-11-19, 7.0 j), en Go par semaine :
  entrepot/passes                               +0.04
  entrepot/decp                                 +0.03
  entrepot/sources                              +0.03
  production/controles                          +0.03
  entrepot/boamp                                +0.01
  entrepot/execution                            +0.01
Dernière purge (2026-11-26 05:45) : faite, 2 élément(s), 0.24 Go libérés · fusions 1 (0.0 Go) · photographies_controle 1 (0.24 Go)
```

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 26/11 07:31 | 719 | 365 | 101 | 0 | 61.2 min |
| 25/11 07:30 | 584 | 363 | 113 | 0 | 60.4 min |
| 24/11 07:30 | 586 | 363 | 114 | 0 | 60.2 min |
| 23/11 07:28 | 254 | 355 | 30 | 0 | 58.0 min |
| 22/11 07:29 | 692 | 361 | 100 | 0 | 59.3 min |
| 21/11 07:30 | 878 | 360 | 151 | 0 | 60.1 min |
| 20/11 07:27 | 337 | 343 | 91 | 0 | 57.2 min |
| 19/11 07:29 | 545 | 347 | 111 | 0 | 59.0 min |
| 18/11 07:23 | 362 | 310 | 87 | 0 | 53.6 min |
| 17/11 07:22 | 346 | 306 | 114 | 0 | 52.8 min |

### Passes DECP hebdomadaires

| Passe | Durée des couples | Mémoire max |
|---|---:|---:|
| 2026-11-21_decp | 59.9 min | 2890 Mo |
| 2026-11-14_decp | 50.5 min | 2828 Mo |
| 2026-11-07_decp | 55.7 min | 2686 Mo |
| 2026-10-31_decp | 53.2 min | 2538 Mo |
| 2026-10-24_decp | 33.0 min | 2373 Mo |
| 2026-10-17_decp | 41.8 min | — Mo |

### Demandes des clients aujourd'hui

Aucune pour l'instant.

### Contrôles quotidiens (14 derniers)

```
2026-11-13 07:21  Contrôle du 13/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour
2026-11-14 07:31  Contrôle du 14/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour
2026-11-15 07:23  Contrôle du 15/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour
2026-11-16 07:23  Contrôle du 16/11 : vert — 276 couples identiques au site ; tâches à l'heure, site à jour
2026-11-17 07:26  Contrôle du 17/11 : vert — 318 couples identiques au site ; tâches à l'heure, site à jour
2026-11-18 07:27  Contrôle du 18/11 : vert — 319 couples identiques au site ; tâches à l'heure, site à jour
2026-11-19 07:33  Contrôle du 19/11 : vert — 347 couples identiques au site ; tâches à l'heure, site à jour
2026-11-20 07:31  Contrôle du 20/11 : rouge — 347 couples identiques au site ; tâches à l'heure, site à jour ; CHUTES : C713_75 : opportunites 34 → 16
2026-11-21 07:34  Contrôle du 21/11 : vert — 360 couples identiques au site ; tâches à l'heure, site à jour
2026-11-22 07:33  Contrôle du 22/11 : vert — 361 couples identiques au site ; tâches à l'heure, site à jour
2026-11-23 07:32  Contrôle du 23/11 : vert — 361 couples identiques au site ; tâches à l'heure, site à jour
2026-11-24 07:34  Contrôle du 24/11 : vert — 363 couples identiques au site ; tâches à l'heure, site à jour
2026-11-25 07:34  Contrôle du 25/11 : vert — 363 couples identiques au site ; tâches à l'heure, site à jour
2026-11-26 07:35  Contrôle du 26/11 : vert — 365 couples identiques au site ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                             LEFT LAST                              PASSED UNIT                     ACTIVATES
Thu 2026-11-26 10:40:00 CET        5s Thu 2026-11-26 10:39:00 CET      54s ago tenderhit-demandes.timer tenderhit-demandes.service
Fri 2026-11-27 05:45:00 CET       19h Thu 2026-11-26 05:45:01 CET 4h 54min ago tenderhit-purge.timer    tenderhit-purge.service
Fri 2026-11-27 06:30:00 CET       19h Thu 2026-11-26 06:30:01 CET  4h 9min ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-11-28 03:00:00 CET 1 day 16h Sat 2026-11-21 03:00:00 CET            - tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                   - Thu 2026-11-26 10:39:50 CET       4s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-26 07:22:24    M29_93 : 2 opportunités · rapport et opportunités · 20 s
2026-11-26 07:22:33    M30_13 : 7 opportunités · rapport et opportunités · 9 s
2026-11-26 07:22:43    M30_69 : 6 opportunités · rapport et opportunités · 10 s
2026-11-26 07:22:46    M33_01 : 9 opportunités · inchangé · 3 s
2026-11-26 07:22:54    M33_14 : 7 opportunités · rapport et opportunités · 8 s
2026-11-26 07:23:00    M33_27 : 5 opportunités · inchangé · 6 s
2026-11-26 07:23:07    M33_38 : 8 opportunités · inchangé · 7 s
2026-11-26 07:23:14    M33_42 : 0 opportunités · rapport et opportunités · 7 s
2026-11-26 07:23:21    M33_50 : 4 opportunités · rapport et opportunités · 7 s
2026-11-26 07:23:27    M33_61 : 3 opportunités · inchangé · 6 s
2026-11-26 07:23:37    M33_69 : 9 opportunités · rapport et opportunités · 10 s
2026-11-26 07:23:45    M33_71 : 5 opportunités · rapport et opportunités · 8 s
2026-11-26 07:23:53    M33_76 : 14 opportunités · rapport et opportunités · 9 s
2026-11-26 07:24:02    M33_85 : 4 opportunités · rapport et opportunités · 9 s
2026-11-26 07:28:14    M33_FR : 509 opportunités · rapport et opportunités · 252 s
2026-11-26 07:28:25    M37_13 : 13 opportunités · rapport et opportunités · 11 s
2026-11-26 07:28:39    M39_13 : 15 opportunités · rapport et opportunités · 13 s
2026-11-26 07:28:49    M40_05 : 0 opportunités · inchangé · 10 s
2026-11-26 07:28:55    M40_76 : 0 opportunités · inchangé · 6 s
2026-11-26 07:29:04    P1005_14 : 2 opportunités · inchangé · 9 s
2026-11-26 07:29:14    P1005_22 : 7 opportunités · rapport et opportunités · 10 s
2026-11-26 07:29:22    P1005_27 : 2 opportunités · inchangé · 8 s
2026-11-26 07:29:31    P1005_29 : 8 opportunités · inchangé · 9 s
2026-11-26 07:29:42    P1005_35 : 18 opportunités · rapport et opportunités · 12 s
2026-11-26 07:29:51    P1005_56 : 11 opportunités · inchangé · 9 s
2026-11-26 07:30:07    P1005_59 : 18 opportunités · inchangé · 15 s
2026-11-26 07:30:16    P1005_60 : 2 opportunités · inchangé · 9 s
2026-11-26 07:30:41    P1005_75 : 39 opportunités · rapport et opportunités · 25 s
2026-11-26 07:30:52    P1005_76 : 6 opportunités · inchangé · 11 s
2026-11-26 07:31:00    P1005_80 : 1 opportunités · inchangé · 9 s
2026-11-26 07:31:13    P1005_93 : 12 opportunités · inchangé · 12 s
2026-11-26 07:31:13  OK, 719 avis collectés, 365 couples recalculés, 101 republiés en 61.2 min
2026-11-26 07:35:50  Contrôle du 26/11 : vert — 365 couples identiques au site ; tâches à l'heure, site à jour
2026-11-26 09:44:45  contrats : 1606315 contrats préparés en 40 s
2026-11-26 09:45:47  contrats : chaînage, 500000 contrats lus (61 s)
2026-11-26 09:46:24  contrats : chaînage, 1000000 contrats lus (98 s)
2026-11-26 09:47:45  contrats : chaînage, 1500000 contrats lus (179 s)
2026-11-26 09:48:18  contrats : 1606315 contrats (294454 doublons fusionnés), chaînage {'aucun': 890476, 'probable': 332080, 'sur': 383759} en 252.6 s
2026-11-26 09:50:46  Rejeu sur le serveur : vert — 3 couples identiques aux envois du matin sur 3 comparés ; 9.6 s par couple (médiane), 1 min au total
2026-11-26 10:38:29  Rejeu sur le serveur : écarts — 100 couples identiques aux envois du matin sur 101 comparés ; en écart ou en échec : C713_75 ; 12.4 s par couple (médiane), 36 min au total
```
