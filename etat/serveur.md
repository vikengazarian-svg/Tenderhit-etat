# Serveur du moteur V2

Mis à jour le 19/11/2026 à 20:00 · publication : **EN SERVICE (publie sur le site)**

## 🟢 **Tout va bien**

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-19 19:59:03  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-19 07:28:59  OK, 545 avis collectés, 347 couples recalculés, 111 republiés en 59.0 min |
| Passe DECP hebdomadaire | 2026-11-14 04:22:58  Passe hebdomadaire DECP 2026-11-14_decp : terminée en 82.9 min, mémoire max 4234 Mo ; 266 couples recalculés, 0 bloqués par la garde ; 260 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-19 07:33:26  Contrôle du 19/11 : vert — 347 couples identiques au site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 0.51 Go sur 7.6 · charge 0.00 · disque 37.0 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : -1.1 point(s) par semaine · pas de hausse

```
Mesure du 2026-11-19 05:45 :
  entrepot/sources                            3.54 Go
  entrepot/decp                               2.02 Go
  entrepot/boamp                              1.39 Go
  entrepot/passes                             1.19 Go
  entrepot/execution                          0.70 Go
  production/controles                        0.69 Go
  entrepot/marche                             0.26 Go
  production/publies                          0.23 Go
  entrepot/photographie                       0.23 Go
  entrepot/etiquettes                           38 Mo
  entrepot/referentiel                          16 Mo
  entrepot/avis                                  3 Mo
  logs                                           3 Mo
  entrepot/sirene                                2 Mo
  production/(fichiers)                          2 Mo
  entrepot/mesures.jsonl                         1 Mo
  production/rejeu                               0 Mo
  entrepot/sources_temoin.jsonl                  0 Mo
  entrepot/manifeste.json                        0 Mo
  production/dce                                 0 Mo
Croissance par dossier (depuis 2026-11-11, 8.0 j), en Go par semaine :
  entrepot/decp                                 +0.37
  entrepot/passes                               +0.26
  entrepot/execution                            +0.06
  entrepot/sources                              +0.03
  entrepot/boamp                                +0.01
  production/publies                            +0.01
Dernière purge (2026-11-19 05:45) : faite, 3 élément(s), 0.23 Go libérés · fusions 1 (0.0 Go) · photographies_controle 1 (0.23 Go) · tmp 1 (0.0 Go)
```

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 19/11 07:29 | 545 | 347 | 111 | 0 | 59.0 min |
| 18/11 07:23 | 362 | 310 | 87 | 0 | 53.6 min |
| 17/11 07:22 | 346 | 306 | 114 | 0 | 52.8 min |
| 16/11 07:19 | 306 | 270 | 61 | 0 | 49.6 min |
| 15/11 07:19 | 430 | 266 | 59 | 0 | 49.1 min |
| 14/11 07:27 | 335 | 266 | 49 | 0 | 48.7 min |
| 13/11 07:17 | 471 | 260 | 60 | 0 | 47.9 min |
| 12/11 07:16 | 433 | 249 | 38 | 0 | 46.8 min |
| 11/11 07:18 | 647 | 249 | 176 | 0 | 48.8 min |
| 10/11 07:18 | 343 | 241 | 89 | 0 | 48.4 min |

### Passes DECP hebdomadaires

| Passe | Durée des couples | Mémoire max |
|---|---:|---:|
| 2026-11-14_decp | 50.5 min | 2828 Mo |
| 2026-11-07_decp | 55.7 min | 2686 Mo |
| 2026-10-31_decp | 53.2 min | 2538 Mo |
| 2026-10-24_decp | 33.0 min | 2373 Mo |
| 2026-10-17_decp | 41.8 min | — Mo |
| essai_pc | 26.3 min | 1616 Mo |

### Demandes des clients aujourd'hui

Aucune pour l'instant.

### Contrôles quotidiens (14 derniers)

```
2026-11-08 07:18  Contrôle du 08/11 : rouge — 223 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour
2026-11-09 07:18  Contrôle du 09/11 : rouge — 222 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour
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
```

## Tâches planifiées
```
NEXT                            LEFT LAST                         PASSED UNIT                     ACTIVATES
Fri 2026-11-20 05:45:00 CET       9h Thu 2026-11-19 05:45:00 CET 14h ago tenderhit-purge.timer    tenderhit-purge.service
Fri 2026-11-20 06:30:00 CET      10h Thu 2026-11-19 06:30:00 CET 13h ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-11-21 03:00:00 CET 1 day 6h Sat 2026-11-14 03:00:04 CET       - tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                  - Thu 2026-11-19 20:00:00 CET  1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                  - Thu 2026-11-19 20:00:00 CET  1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-19 07:18:15    M29_26 : 0 opportunités · rapport et opportunités · 16 s
2026-11-19 07:18:31    M29_38 : 1 opportunités · rapport et opportunités · 17 s
2026-11-19 07:18:47    M29_42 : 0 opportunités · rapport et opportunités · 16 s
2026-11-19 07:19:02    M29_43 : 0 opportunités · rapport et opportunités · 15 s
2026-11-19 07:19:18    M29_63 : 0 opportunités · rapport et opportunités · 15 s
2026-11-19 07:19:24    M29_69 : 0 opportunités · inchangé · 7 s
2026-11-19 07:19:41    M29_73 : 0 opportunités · rapport et opportunités · 16 s
2026-11-19 07:19:57    M29_74 : 0 opportunités · rapport et opportunités · 16 s
2026-11-19 07:20:11    M29_83 : 1 opportunités · rapport et opportunités · 14 s
2026-11-19 07:20:31    M29_93 : 1 opportunités · rapport et opportunités · 21 s
2026-11-19 07:20:40    M30_69 : 14 opportunités · inchangé · 9 s
2026-11-19 07:20:43    M33_01 : 6 opportunités · inchangé · 3 s
2026-11-19 07:20:50    M33_14 : 6 opportunités · inchangé · 7 s
2026-11-19 07:20:56    M33_27 : 5 opportunités · inchangé · 6 s
2026-11-19 07:21:05    M33_38 : 8 opportunités · rapport et opportunités · 8 s
2026-11-19 07:21:12    M33_42 : 0 opportunités · rapport et opportunités · 7 s
2026-11-19 07:21:19    M33_50 : 2 opportunités · rapport et opportunités · 7 s
2026-11-19 07:21:24    M33_61 : 3 opportunités · inchangé · 6 s
2026-11-19 07:21:35    M33_69 : 15 opportunités · rapport et opportunités · 10 s
2026-11-19 07:21:41    M33_71 : 10 opportunités · inchangé · 6 s
2026-11-19 07:21:48    M33_76 : 8 opportunités · inchangé · 8 s
2026-11-19 07:21:58    M33_85 : 4 opportunités · rapport et opportunités · 9 s
2026-11-19 07:26:15    M33_FR : 498 opportunités · rapport et opportunités · 257 s
2026-11-19 07:26:25    M37_13 : 16 opportunités · rapport et opportunités · 10 s
2026-11-19 07:26:36    M40_05 : 0 opportunités · rapport et opportunités · 11 s
2026-11-19 07:26:42    M40_76 : 0 opportunités · inchangé · 6 s
2026-11-19 07:26:51    P1005_14 : 2 opportunités · inchangé · 9 s
2026-11-19 07:26:59    P1005_22 : 8 opportunités · inchangé · 8 s
2026-11-19 07:27:07    P1005_27 : 2 opportunités · inchangé · 8 s
2026-11-19 07:27:17    P1005_29 : 9 opportunités · inchangé · 9 s
2026-11-19 07:27:27    P1005_35 : 19 opportunités · inchangé · 11 s
2026-11-19 07:27:37    P1005_56 : 8 opportunités · rapport et opportunités · 10 s
2026-11-19 07:27:53    P1005_59 : 19 opportunités · rapport et opportunités · 16 s
2026-11-19 07:28:02    P1005_60 : 2 opportunités · inchangé · 9 s
2026-11-19 07:28:26    P1005_75 : 38 opportunités · rapport et opportunités · 24 s
2026-11-19 07:28:38    P1005_76 : 5 opportunités · rapport et opportunités · 3 identifiants DECP raccourcis · 12 s
2026-11-19 07:28:47    P1005_80 : 0 opportunités · inchangé · 8 s
2026-11-19 07:28:59    P1005_93 : 11 opportunités · inchangé · 12 s
2026-11-19 07:28:59  OK, 545 avis collectés, 347 couples recalculés, 111 republiés en 59.0 min
2026-11-19 07:33:26  Contrôle du 19/11 : vert — 347 couples identiques au site ; tâches à l'heure, site à jour
```
