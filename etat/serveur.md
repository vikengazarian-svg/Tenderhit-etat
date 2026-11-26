# Serveur du moteur V2

Mis à jour le 26/11/2026 à 07:00 · publication : **EN SERVICE (publie sur le site)**

## 🔴 **À regarder** : demandes des clients non traitées depuis plus de 15 min

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-26 06:29:03  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-25 07:30:25  OK, 584 avis collectés, 363 couples recalculés, 113 republiés en 60.4 min |
| Passe DECP hebdomadaire | 2026-11-21 04:33:49  Passe hebdomadaire DECP 2026-11-21_decp : terminée en 93.8 min, mémoire max 4287 Mo ; 360 couples recalculés, 1 bloqués par la garde (M01_58) ; 352 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-25 07:34:56  Contrôle du 25/11 : vert — 363 couples identiques au site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 2.93 Go sur 7.6 · charge 1.58 · disque 37.4 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : +0.8 point(s) par semaine · 80 % dans **56.8 semaine(s)**

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
| 25/11 07:30 | 584 | 363 | 113 | 0 | 60.4 min |
| 24/11 07:30 | 586 | 363 | 114 | 0 | 60.2 min |
| 23/11 07:28 | 254 | 355 | 30 | 0 | 58.0 min |
| 22/11 07:29 | 692 | 361 | 100 | 0 | 59.3 min |
| 21/11 07:30 | 878 | 360 | 151 | 0 | 60.1 min |
| 20/11 07:27 | 337 | 343 | 91 | 0 | 57.2 min |
| 19/11 07:29 | 545 | 347 | 111 | 0 | 59.0 min |
| 18/11 07:23 | 362 | 310 | 87 | 0 | 53.6 min |
| 17/11 07:22 | 346 | 306 | 114 | 0 | 52.8 min |
| 16/11 07:19 | 306 | 270 | 61 | 0 | 49.6 min |

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
2026-11-25 07:34  Contrôle du 25/11 : vert — 363 couples identiques au site ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                             LEFT LAST                              PASSED UNIT                     ACTIVATES
Fri 2026-11-27 05:45:00 CET       22h Thu 2026-11-26 05:45:01 CET 1h 15min ago tenderhit-purge.timer    tenderhit-purge.service
Sat 2026-11-28 03:00:00 CET 1 day 19h Sat 2026-11-21 03:00:00 CET            - tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                   - Thu 2026-11-26 06:30:01 CET    30min ago tenderhit-collecte.timer tenderhit-collecte.service
-                                   - Thu 2026-11-26 07:00:00 CET       1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                   - Thu 2026-11-26 07:00:00 CET       1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-26 06:54:42    C923_30 : 1 opportunités · inchangé · 4 s
2026-11-26 06:54:46    C923_34 : 1 opportunités · inchangé · 4 s
2026-11-26 06:54:52    C923_75 : 3 opportunités · rapport et opportunités · 6 s
2026-11-26 06:54:56    C923_77 : 0 opportunités · inchangé · 4 s
2026-11-26 06:55:05    C923_78 : 1 opportunités · rapport et opportunités · 9 s
2026-11-26 06:55:13    C923_84 : 0 opportunités · inchangé · 8 s
2026-11-26 06:55:17    C923_91 : 0 opportunités · inchangé · 4 s
2026-11-26 06:55:21    C923_92 : 1 opportunités · inchangé · 4 s
2026-11-26 06:55:25    C923_93 : 1 opportunités · inchangé · 4 s
2026-11-26 06:55:28    C923_94 : 0 opportunités · inchangé · 4 s
2026-11-26 06:55:32    C923_95 : 0 opportunités · inchangé · 4 s
2026-11-26 06:55:35    M01_01 : 5 opportunités · inchangé · 3 s
2026-11-26 06:55:48    M01_03 : 6 opportunités · inchangé · 13 s
2026-11-26 06:55:51    M01_04 : 4 opportunités · inchangé · 3 s
2026-11-26 06:56:04    M01_07 : 3 opportunités · inchangé · 13 s
2026-11-26 06:56:10    M01_14 : 23 opportunités · inchangé · 6 s
2026-11-26 06:56:27    M01_15 : 0 opportunités · inchangé · 16 s
2026-11-26 06:56:41    M01_16 : 6 opportunités · rapport et opportunités · 15 s
2026-11-26 06:56:48    M01_17 : 11 opportunités · inchangé · 7 s
2026-11-26 06:56:54    M01_21 : 13 opportunités · inchangé · 6 s
2026-11-26 06:57:08    M01_24 : 1 opportunités · rapport et opportunités · 15 s
2026-11-26 06:57:14    M01_25 : 3 opportunités · inchangé · 6 s
2026-11-26 06:57:20    M01_26 : 7 opportunités · inchangé · 5 s
2026-11-26 06:57:26    M01_27 : 4 opportunités · inchangé · 6 s
2026-11-26 06:57:33    M01_35 : 27 opportunités · inchangé · 7 s
2026-11-26 06:57:41    M01_38 : 16 opportunités · inchangé · 8 s
2026-11-26 06:57:54    M01_39 : 6 opportunités · rapport et opportunités · 13 s
2026-11-26 06:58:02    M01_42 : 13 opportunités · inchangé · 8 s
2026-11-26 06:58:17    M01_43 : 4 opportunités · inchangé · 16 s
2026-11-26 06:58:22    M01_58 : 6 opportunités · inchangé · 5 s
2026-11-26 06:58:33    M01_59 : 58 opportunités · rapport et opportunités · 11 s
2026-11-26 06:58:39    M01_63 : 6 opportunités · inchangé · 5 s
2026-11-26 06:58:48    M01_69 : 43 opportunités · inchangé · 9 s
2026-11-26 06:59:01    M01_70 : 2 opportunités · rapport et opportunités · 13 s
2026-11-26 06:59:07    M01_71 : 6 opportunités · rapport et opportunités · 6 s
2026-11-26 06:59:14    M01_73 : 30 opportunités · inchangé · 6 s
2026-11-26 06:59:20    M01_74 : 20 opportunités · inchangé · 6 s
2026-11-26 06:59:37    M01_75 : 61 opportunités · rapport et opportunités · 17 s
2026-11-26 06:59:45    M01_76 : 13 opportunités · rapport et opportunités · 9 s
2026-11-26 06:59:57    M01_77 : 27 opportunités · rapport et opportunités · 11 s
```
