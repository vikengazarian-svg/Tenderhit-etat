# Serveur du moteur V2

Mis à jour le 24/11/2026 à 07:36 · publication : **EN SERVICE (publie sur le site)**

## 🟢 **Tout va bien**

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-24 07:35:03  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-24 07:30:10  OK, 586 avis collectés, 363 couples recalculés, 114 republiés en 60.2 min |
| Passe DECP hebdomadaire | 2026-11-21 04:33:49  Passe hebdomadaire DECP 2026-11-21_decp : terminée en 93.8 min, mémoire max 4287 Mo ; 360 couples recalculés, 1 bloqués par la garde (M01_58) ; 352 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-24 07:34:40  Contrôle du 24/11 : vert — 363 couples identiques au site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 0.56 Go sur 7.6 · charge 0.22 · disque 37.3 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : +0.8 point(s) par semaine · 80 % dans **50.2 semaine(s)**

```
Mesure du 2026-11-24 05:45 :
  entrepot/sources                            3.56 Go
  entrepot/decp                               2.06 Go
  entrepot/boamp                              1.40 Go
  entrepot/passes                             1.23 Go
  production/controles                        0.72 Go
  entrepot/execution                          0.71 Go
  entrepot/marche                             0.26 Go
  production/publies                          0.24 Go
  entrepot/photographie                       0.23 Go
  entrepot/etiquettes                           38 Mo
  entrepot/referentiel                          16 Mo
  entrepot/avis                                  3 Mo
  production/(fichiers)                          3 Mo
  logs                                           3 Mo
  entrepot/sirene                                2 Mo
  entrepot/mesures.jsonl                         2 Mo
  entrepot/tmp                                   1 Mo
  production/rejeu                               0 Mo
  entrepot/sources_temoin.jsonl                  0 Mo
  entrepot/manifeste.json                        0 Mo
Croissance par dossier (depuis 2026-11-17, 7.0 j), en Go par semaine :
  entrepot/passes                               +0.04
  entrepot/decp                                 +0.03
  entrepot/execution                            +0.03
  entrepot/sources                              +0.03
  production/controles                          +0.03
  entrepot/boamp                                +0.01
Dernière purge (2026-11-24 05:45) : faite, 2 élément(s), 0.24 Go libérés · fusions 1 (0.0 Go) · photographies_controle 1 (0.24 Go)
```

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 24/11 07:30 | 586 | 363 | 114 | 0 | 60.2 min |
| 23/11 07:28 | 254 | 355 | 30 | 0 | 58.0 min |
| 22/11 07:29 | 692 | 361 | 100 | 0 | 59.3 min |
| 21/11 07:30 | 878 | 360 | 151 | 0 | 60.1 min |
| 20/11 07:27 | 337 | 343 | 91 | 0 | 57.2 min |
| 19/11 07:29 | 545 | 347 | 111 | 0 | 59.0 min |
| 18/11 07:23 | 362 | 310 | 87 | 0 | 53.6 min |
| 17/11 07:22 | 346 | 306 | 114 | 0 | 52.8 min |
| 16/11 07:19 | 306 | 270 | 61 | 0 | 49.6 min |
| 15/11 07:19 | 430 | 266 | 59 | 0 | 49.1 min |

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
2026-11-22 07:33  Contrôle du 22/11 : vert — 361 couples identiques au site ; tâches à l'heure, site à jour
2026-11-23 07:32  Contrôle du 23/11 : vert — 361 couples identiques au site ; tâches à l'heure, site à jour
2026-11-24 07:34  Contrôle du 24/11 : vert — 363 couples identiques au site ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                          LEFT LAST                              PASSED UNIT                     ACTIVATES
Wed 2026-11-25 05:45:00 CET    22h Tue 2026-11-24 05:45:00 CET 1h 51min ago tenderhit-purge.timer    tenderhit-purge.service
Wed 2026-11-25 06:30:00 CET    22h Tue 2026-11-24 06:30:00 CET  1h 6min ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-11-28 03:00:00 CET 3 days Sat 2026-11-21 03:00:00 CET   3 days ago tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                - Tue 2026-11-24 07:36:00 CET       1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                - Tue 2026-11-24 07:36:00 CET       1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-24 07:19:30    M29_26 : 0 opportunités · rapport et opportunités · 16 s
2026-11-24 07:19:47    M29_38 : 1 opportunités · rapport et opportunités · 17 s
2026-11-24 07:20:04    M29_42 : 0 opportunités · rapport et opportunités · 17 s
2026-11-24 07:20:19    M29_43 : 0 opportunités · rapport et opportunités · 15 s
2026-11-24 07:20:35    M29_63 : 0 opportunités · rapport et opportunités · 16 s
2026-11-24 07:20:42    M29_69 : 0 opportunités · inchangé · 7 s
2026-11-24 07:20:58    M29_73 : 0 opportunités · rapport et opportunités · 16 s
2026-11-24 07:21:15    M29_74 : 0 opportunités · rapport et opportunités · 17 s
2026-11-24 07:21:28    M29_83 : 1 opportunités · rapport et opportunités · 14 s
2026-11-24 07:21:48    M29_93 : 2 opportunités · rapport et opportunités · 20 s
2026-11-24 07:21:58    M30_69 : 7 opportunités · rapport et opportunités · 10 s
2026-11-24 07:22:01    M33_01 : 9 opportunités · inchangé · 3 s
2026-11-24 07:22:09    M33_14 : 6 opportunités · rapport et opportunités · 8 s
2026-11-24 07:22:15    M33_27 : 5 opportunités · inchangé · 6 s
2026-11-24 07:22:23    M33_38 : 8 opportunités · rapport et opportunités · 8 s
2026-11-24 07:22:29    M33_42 : 0 opportunités · inchangé · 6 s
2026-11-24 07:22:36    M33_50 : 4 opportunités · rapport et opportunités · 7 s
2026-11-24 07:22:42    M33_61 : 2 opportunités · inchangé · 5 s
2026-11-24 07:22:52    M33_69 : 10 opportunités · rapport et opportunités · 10 s
2026-11-24 07:23:00    M33_71 : 6 opportunités · rapport et opportunités · 7 s
2026-11-24 07:23:07    M33_76 : 12 opportunités · inchangé · 8 s
2026-11-24 07:23:14    M33_85 : 3 opportunités · inchangé · 7 s
2026-11-24 07:27:25    M33_FR : 481 opportunités · rapport et opportunités · 251 s
2026-11-24 07:27:36    M37_13 : 11 opportunités · rapport et opportunités · 11 s
2026-11-24 07:27:47    M40_05 : 0 opportunités · rapport et opportunités · 11 s
2026-11-24 07:27:53    M40_76 : 0 opportunités · inchangé · 6 s
2026-11-24 07:28:02    P1005_14 : 2 opportunités · inchangé · 9 s
2026-11-24 07:28:12    P1005_22 : 7 opportunités · rapport et opportunités · 10 s
2026-11-24 07:28:20    P1005_27 : 2 opportunités · inchangé · 8 s
2026-11-24 07:28:29    P1005_29 : 8 opportunités · inchangé · 9 s
2026-11-24 07:28:39    P1005_35 : 17 opportunités · inchangé · 11 s
2026-11-24 07:28:48    P1005_56 : 10 opportunités · inchangé · 9 s
2026-11-24 07:29:03    P1005_59 : 18 opportunités · inchangé · 15 s
2026-11-24 07:29:12    P1005_60 : 2 opportunités · inchangé · 9 s
2026-11-24 07:29:37    P1005_75 : 35 opportunités · rapport et opportunités · 24 s
2026-11-24 07:29:49    P1005_76 : 5 opportunités · rapport et opportunités · 3 identifiants DECP raccourcis · 12 s
2026-11-24 07:29:57    P1005_80 : 1 opportunités · inchangé · 9 s
2026-11-24 07:30:10    P1005_93 : 12 opportunités · inchangé · 13 s
2026-11-24 07:30:10  OK, 586 avis collectés, 363 couples recalculés, 114 republiés en 60.2 min
2026-11-24 07:34:40  Contrôle du 24/11 : vert — 363 couples identiques au site ; tâches à l'heure, site à jour
```
