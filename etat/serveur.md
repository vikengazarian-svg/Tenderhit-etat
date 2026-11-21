# Serveur du moteur V2

Mis à jour le 22/11/2026 à 00:00 · publication : **EN SERVICE (publie sur le site)**

## 🟢 **Tout va bien**

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-21 23:59:03  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-21 07:30:04  OK, 878 avis collectés, 360 couples recalculés, 151 republiés en 60.1 min |
| Passe DECP hebdomadaire | 2026-11-21 04:33:49  Passe hebdomadaire DECP 2026-11-21_decp : terminée en 93.8 min, mémoire max 4287 Mo ; 360 couples recalculés, 1 bloqués par la garde (M01_58) ; 352 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-21 07:34:34  Contrôle du 21/11 : vert — 360 couples identiques au site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 0.55 Go sur 7.6 · charge 0.01 · disque 37.2 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : +0.1 point(s) par semaine · 80 % dans **285.3 semaine(s)**

```
Mesure du 2026-11-21 05:45 :
  entrepot/sources                            3.56 Go
  entrepot/decp                               2.06 Go
  entrepot/boamp                              1.40 Go
  entrepot/passes                             1.23 Go
  entrepot/execution                          0.71 Go
  production/controles                        0.71 Go
  entrepot/marche                             0.26 Go
  production/publies                          0.24 Go
  entrepot/photographie                       0.23 Go
  entrepot/etiquettes                           38 Mo
  entrepot/referentiel                          16 Mo
  entrepot/avis                                  3 Mo
  logs                                           3 Mo
  entrepot/sirene                                2 Mo
  production/(fichiers)                          2 Mo
  entrepot/mesures.jsonl                         2 Mo
  entrepot/tmp                                   1 Mo
  production/rejeu                               0 Mo
  entrepot/sources_temoin.jsonl                  0 Mo
  entrepot/manifeste.json                        0 Mo
Croissance par dossier (depuis 2026-11-14, 7.1 j), en Go par semaine :
  entrepot/execution                            +0.06
  entrepot/passes                               +0.04
  entrepot/decp                                 +0.03
  entrepot/sources                              +0.03
  production/controles                          +0.03
  production/publies                            +0.03
Dernière purge (2026-11-21 05:45) : faite, 0 élément(s), 0.0 Go libérés
```

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 21/11 07:30 | 878 | 360 | 151 | 0 | 60.1 min |
| 20/11 07:27 | 337 | 343 | 91 | 0 | 57.2 min |
| 19/11 07:29 | 545 | 347 | 111 | 0 | 59.0 min |
| 18/11 07:23 | 362 | 310 | 87 | 0 | 53.6 min |
| 17/11 07:22 | 346 | 306 | 114 | 0 | 52.8 min |
| 16/11 07:19 | 306 | 270 | 61 | 0 | 49.6 min |
| 15/11 07:19 | 430 | 266 | 59 | 0 | 49.1 min |
| 14/11 07:27 | 335 | 266 | 49 | 0 | 48.7 min |
| 13/11 07:17 | 471 | 260 | 60 | 0 | 47.9 min |
| 12/11 07:16 | 433 | 249 | 38 | 0 | 46.8 min |

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
2026-11-10 07:21  Contrôle du 10/11 : rouge — 235 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour
2026-11-10 11:59  Contrôle du 10/11 : rouge — 235 couples identiques au site, 4238 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour ; CHUTES : C451_21 : attributions 585 → 270, C451_42 : attributions 1131 → 535
2026-11-10 13:50  Contrôle du 10/11 : vert — 249 couples identiques au site ; tâches à l'heure, site à jour
2026-11-11 07:22  Contrôle du 11/11 : rouge — 249 couples identiques au site ; tâches à l'heure, site à jour ; CHUTES : C451_69 : opportunites 18 → 8, C451_FR : opportunites 564 → 181, M07_76 : opportunites 19 → 8
2026-11-12 07:20  Contrôle du 12/11 : vert — 249 couples identiques au site ; tâches à l'heure, site à jour
2026-11-13 07:21  Contrôle du 13/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour
2026-11-14 07:31  Contrôle du 14/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour
2026-11-15 07:23  Contrôle du 15/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour
2026-11-16 07:23  Contrôle du 16/11 : vert — 276 couples identiques au site ; tâches à l'heure, site à jour
2026-11-17 07:26  Contrôle du 17/11 : vert — 318 couples identiques au site ; tâches à l'heure, site à jour
2026-11-18 07:27  Contrôle du 18/11 : vert — 319 couples identiques au site ; tâches à l'heure, site à jour
2026-11-19 07:33  Contrôle du 19/11 : vert — 347 couples identiques au site ; tâches à l'heure, site à jour
2026-11-20 07:31  Contrôle du 20/11 : rouge — 347 couples identiques au site ; tâches à l'heure, site à jour ; CHUTES : C713_75 : opportunites 34 → 16
2026-11-21 07:34  Contrôle du 21/11 : vert — 360 couples identiques au site ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                            LEFT LAST                         PASSED UNIT                     ACTIVATES
Sun 2026-11-22 05:45:00 CET 5h 44min Sat 2026-11-21 05:45:00 CET 18h ago tenderhit-purge.timer    tenderhit-purge.service
Sun 2026-11-22 06:30:00 CET       6h Sat 2026-11-21 06:30:00 CET 17h ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-11-28 03:00:00 CET   6 days Sat 2026-11-21 03:00:00 CET 21h ago tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                  - Sun 2026-11-22 00:00:00 CET  1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                  - Sun 2026-11-22 00:00:00 CET  1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-21 07:20:11    M29_43 : 0 opportunités · rapport et opportunités · 15 s
2026-11-21 07:20:26    M29_63 : 0 opportunités · rapport et opportunités · 15 s
2026-11-21 07:20:33    M29_69 : 0 opportunités · inchangé · 7 s
2026-11-21 07:20:49    M29_73 : 0 opportunités · rapport et opportunités · 16 s
2026-11-21 07:21:06    M29_74 : 0 opportunités · rapport et opportunités · 17 s
2026-11-21 07:21:19    M29_83 : 1 opportunités · rapport et opportunités · 13 s
2026-11-21 07:21:39    M29_93 : 1 opportunités · rapport et opportunités · 20 s
2026-11-21 07:21:49    M30_69 : 11 opportunités · rapport et opportunités · 10 s
2026-11-21 07:21:52    M33_01 : 7 opportunités · inchangé · 3 s
2026-11-21 07:21:59    M33_14 : 5 opportunités · rapport et opportunités · 8 s
2026-11-21 07:22:05    M33_27 : 5 opportunités · inchangé · 6 s
2026-11-21 07:22:13    M33_38 : 8 opportunités · rapport et opportunités · 8 s
2026-11-21 07:22:20    M33_42 : 0 opportunités · inchangé · 6 s
2026-11-21 07:22:26    M33_50 : 3 opportunités · inchangé · 6 s
2026-11-21 07:22:32    M33_61 : 2 opportunités · rapport et opportunités · 6 s
2026-11-21 07:22:42    M33_69 : 12 opportunités · rapport et opportunités · 10 s
2026-11-21 07:22:49    M33_71 : 7 opportunités · rapport et opportunités · 7 s
2026-11-21 07:22:58    M33_76 : 12 opportunités · rapport et opportunités · 8 s
2026-11-21 07:23:06    M33_85 : 4 opportunités · rapport et opportunités · 8 s
2026-11-21 07:27:17    M33_FR : 509 opportunités · rapport et opportunités · 252 s
2026-11-21 07:27:28    M37_13 : 13 opportunités · rapport et opportunités · 11 s
2026-11-21 07:27:38    M40_05 : 0 opportunités · rapport et opportunités · 11 s
2026-11-21 07:27:45    M40_76 : 0 opportunités · inchangé · 6 s
2026-11-21 07:27:55    P1005_14 : 2 opportunités · rapport et opportunités · 10 s
2026-11-21 07:28:04    P1005_22 : 7 opportunités · rapport et opportunités · 9 s
2026-11-21 07:28:12    P1005_27 : 2 opportunités · inchangé · 8 s
2026-11-21 07:28:22    P1005_29 : 7 opportunités · rapport et opportunités · 10 s
2026-11-21 07:28:34    P1005_35 : 17 opportunités · rapport et opportunités · 12 s
2026-11-21 07:28:43    P1005_56 : 10 opportunités · rapport et opportunités · 10 s
2026-11-21 07:28:59    P1005_59 : 19 opportunités · inchangé · 15 s
2026-11-21 07:29:08    P1005_60 : 2 opportunités · inchangé · 9 s
2026-11-21 07:29:31    P1005_75 : 36 opportunités · rapport et opportunités · 24 s
2026-11-21 07:29:43    P1005_76 : 6 opportunités · rapport et opportunités · 3 identifiants DECP raccourcis · 12 s
2026-11-21 07:29:52    P1005_80 : 1 opportunités · inchangé · 8 s
2026-11-21 07:30:04    P1005_93 : 12 opportunités · inchangé · 13 s
2026-11-21 07:30:04  OK, 878 avis collectés, 360 couples recalculés, 151 republiés en 60.1 min
2026-11-21 07:34:34  Contrôle du 21/11 : vert — 360 couples identiques au site ; tâches à l'heure, site à jour
2026-11-21 07:35:03  M28_34 : demande en attente
2026-11-21 07:35:13    publié (édition 2026-11, 4 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 10 s
2026-11-21 07:35:33  tables du marché : 1 activité(s) envoyée(s), 0 inchangée(s), 73167 lignes en 17 paquets
```
