# Serveur du moteur V2

Mis à jour le 10/11/2026 à 07:20 · publication : **EN SERVICE (publie sur le site)**

## 🔴 **À regarder** : demandes des clients non traitées depuis plus de 15 min

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-10 06:29:06  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-10 07:18:25  OK, 343 avis collectés, 241 couples recalculés, 89 republiés en 48.4 min |
| Passe DECP hebdomadaire | 2026-11-07 04:22:15  Passe hebdomadaire DECP 2026-11-07_decp : terminée avec échecs en 82.2 min, mémoire max 4269 Mo ; 236 couples recalculés, 0 bloqués par la garde, échecs : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; 222 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-09 07:18:46  Contrôle du 09/11 : rouge — 222 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 1.03 Go sur 7.6 · charge 0.46 · disque 35.4 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : +4.1 point(s) par semaine · 80 % dans **10.9 semaine(s)**

```
Mesure du 2026-11-10 05:45 :
  entrepot/sources                            3.50 Go
  entrepot/decp                               1.59 Go
  entrepot/boamp                              1.38 Go
  entrepot/passes                             0.89 Go
  entrepot/execution                          0.69 Go
  production/controles                        0.67 Go
  entrepot/marche                             0.26 Go
  production/publies                          0.23 Go
  entrepot/photographie                       0.23 Go
  entrepot/etiquettes                           37 Mo
  entrepot/referentiel                          16 Mo
  entrepot/avis                                  4 Mo
  entrepot/sirene                                2 Mo
  production/(fichiers)                          2 Mo
  logs                                           2 Mo
  entrepot/mesures.jsonl                         1 Mo
  production/rejeu                               0 Mo
  entrepot/sources_temoin.jsonl                  0 Mo
  entrepot/manifeste.json                        0 Mo
  entrepot/tmp                                   0 Mo
Croissance par dossier (depuis 2026-11-05, 4.3 j), en Go par semaine :
  entrepot/decp                                 +0.66
  entrepot/passes                               +0.50
  entrepot/execution                            +0.04
  entrepot/boamp                                +0.01
  production/publies                            +0.01
Dernière purge (2026-11-10 05:45) : faite, 3 élément(s), 0.22 Go libérés · fusions 1 (0.0 Go) · photographies_controle 1 (0.22 Go) · tmp 1 (0.0 Go)
```

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 10/11 07:18 | 343 | 241 | 89 | 0 | 48.4 min |
| 09/11 07:16 | 305 | 236 | 59 | 0 | 46.0 min |
| 08/11 07:16 | 673 | 233 | 90 | 0 | 46.0 min |
| 07/11 07:15 | 519 | 233 | 72 | 0 | 45.7 min |
| 06/11 07:14 | 770 | 224 | 63 | 0 | 44.3 min |
| 05/11 07:12 | 770 | 223 | 65 | 0 | 42.3 min |
| 04/11 07:11 | 599 | 220 | 66 | 0 | 41.9 min |
| 03/11 07:09 | 315 | 219 | 79 | 0 | 39.6 min |
| 02/11 07:10 | 251 | 219 | 42 | 0 | 40.9 min |
| 01/11 07:13 | 543 | 219 | 219 | 0 | 43.6 min |

### Passes DECP hebdomadaires

| Passe | Durée des couples | Mémoire max |
|---|---:|---:|
| 2026-11-07_decp | 55.7 min | 2686 Mo |
| 2026-10-31_decp | 53.2 min | 2538 Mo |
| 2026-10-24_decp | 33.0 min | 2373 Mo |
| 2026-10-17_decp | 41.8 min | — Mo |
| essai_pc | 26.3 min | 1616 Mo |
| essai_2026-10-16 | 26.4 min | 1950 Mo |

### Demandes des clients aujourd'hui

Aucune pour l'instant.

### Contrôles quotidiens (14 derniers)

```
2026-10-29 07:13  Contrôle du 29/10 : rouge — 171 couples identiques au site, 10 attributions anciennes gardées par le site ; EN ÉCART : C713_FR ; collecte du matin : 2026-10-29 07:07:57  1 ÉCHEC(S), 704 avis collectés, 172 couples recalculés, 51 republiés en 37.9 min
2026-10-30 07:12  Contrôle du 30/10 : vert — 172 couples identiques au site, 10 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-10-31 07:20  Contrôle du 31/10 : rouge — 215 couples identiques au site, 349 attributions anciennes gardées par le site ; EN ÉCART : M01_04, M01_27, M01_63, M01_71 ; tâches à l'heure, site à jour
2026-10-31 11:33  Contrôle du 31/10 : vert — 219 couples identiques au site, 349 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-11-01 07:17  Contrôle du 01/11 : vert — 219 couples identiques au site, 349 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-11-02 07:14  Contrôle du 02/11 : vert — 219 couples identiques au site, 349 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-11-03 07:12  Contrôle du 03/11 : vert — 219 couples identiques au site, 349 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-11-04 07:15  Contrôle du 04/11 : vert — 220 couples identiques au site, 349 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-11-05 07:15  Contrôle du 05/11 : rouge — photographie du site impossible ou incomplète
2026-11-05 11:03  Contrôle du 05/11 : rouge — photographie du site impossible ou incomplète
2026-11-06 07:17  Contrôle du 06/11 : rouge — 222 couples identiques au site, 349 attributions anciennes gardées par le site ; EN ÉCART : C713_75, M08_81 ; tâches à l'heure, site à jour
2026-11-07 07:18  Contrôle du 07/11 : rouge — 223 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour
2026-11-08 07:18  Contrôle du 08/11 : rouge — 223 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour
2026-11-09 07:18  Contrôle du 09/11 : rouge — 222 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                          LEFT LAST                              PASSED UNIT                     ACTIVATES
Tue 2026-11-10 07:21:00 CET    58s Tue 2026-11-10 07:20:00 CET       1s ago tenderhit-demandes.timer tenderhit-demandes.service
Wed 2026-11-11 05:45:00 CET    22h Tue 2026-11-10 05:45:04 CET 1h 34min ago tenderhit-purge.timer    tenderhit-purge.service
Sat 2026-11-14 03:00:00 CET 3 days Sat 2026-11-07 03:00:00 CET   3 days ago tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                - Tue 2026-11-10 06:30:04 CET    49min ago tenderhit-collecte.timer tenderhit-collecte.service
-                                - Tue 2026-11-10 07:20:00 CET       1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-10 07:07:06    M24_76 : 11 opportunités · rapport et opportunités · 8 s
2026-11-10 07:07:20    M29_01 : 0 opportunités · rapport et opportunités · 14 s
2026-11-10 07:07:33    M29_03 : 0 opportunités · rapport et opportunités · 13 s
2026-11-10 07:07:46    M29_07 : 0 opportunités · rapport et opportunités · 13 s
2026-11-10 07:08:02    M29_26 : 0 opportunités · rapport et opportunités · 16 s
2026-11-10 07:08:19    M29_38 : 0 opportunités · rapport et opportunités · 17 s
2026-11-10 07:08:35    M29_42 : 0 opportunités · rapport et opportunités · 16 s
2026-11-10 07:08:51    M29_63 : 1 opportunités · rapport et opportunités · 16 s
2026-11-10 07:08:59    M29_69 : 0 opportunités · rapport et opportunités · 7 s
2026-11-10 07:09:15    M29_73 : 0 opportunités · rapport et opportunités · 17 s
2026-11-10 07:09:32    M29_74 : 1 opportunités · rapport et opportunités · 17 s
2026-11-10 07:09:46    M29_83 : 1 opportunités · rapport et opportunités · 14 s
2026-11-10 07:09:56    M30_69 : 13 opportunités · rapport et opportunités · 10 s
2026-11-10 07:09:59    M33_01 : 5 opportunités · inchangé · 3 s
2026-11-10 07:10:07    M33_14 : 8 opportunités · rapport et opportunités · 8 s
2026-11-10 07:10:13    M33_27 : 5 opportunités · inchangé · 6 s
2026-11-10 07:10:21    M33_38 : 9 opportunités · rapport et opportunités · 8 s
2026-11-10 07:10:27    M33_42 : 1 opportunités · inchangé · 6 s
2026-11-10 07:10:34    M33_50 : 4 opportunités · inchangé · 6 s
2026-11-10 07:10:39    M33_61 : 2 opportunités · inchangé · 5 s
2026-11-10 07:10:50    M33_69 : 14 opportunités · rapport et opportunités · 11 s
2026-11-10 07:10:57    M33_71 : 9 opportunités · rapport et opportunités · 8 s
2026-11-10 07:11:05    M33_76 : 15 opportunités · inchangé · 8 s
2026-11-10 07:11:12    M33_85 : 3 opportunités · inchangé · 7 s
2026-11-10 07:15:49    M33_FR : 580 opportunités · rapport et opportunités · 277 s
2026-11-10 07:15:59    M40_05 : 0 opportunités · inchangé · 10 s
2026-11-10 07:16:05    M40_76 : 1 opportunités · inchangé · 6 s
2026-11-10 07:16:14    P1005_14 : 0 opportunités · inchangé · 9 s
2026-11-10 07:16:24    P1005_22 : 6 opportunités · rapport et opportunités · 10 s
2026-11-10 07:16:34    P1005_27 : 2 opportunités · rapport et opportunités · 9 s
2026-11-10 07:16:44    P1005_29 : 13 opportunités · rapport et opportunités · 10 s
2026-11-10 07:16:55    P1005_35 : 18 opportunités · rapport et opportunités · 12 s
2026-11-10 07:17:04    P1005_56 : 13 opportunités · inchangé · 9 s
2026-11-10 07:17:19    P1005_59 : 19 opportunités · inchangé · 15 s
2026-11-10 07:17:28    P1005_60 : 3 opportunités · inchangé · 9 s
2026-11-10 07:17:52    P1005_75 : 42 opportunités · rapport et opportunités · 24 s
2026-11-10 07:18:04    P1005_76 : 8 opportunités · inchangé · 11 s
2026-11-10 07:18:12    P1005_80 : 0 opportunités · inchangé · 9 s
2026-11-10 07:18:25    P1005_93 : 13 opportunités · inchangé · 13 s
2026-11-10 07:18:25  OK, 343 avis collectés, 241 couples recalculés, 89 republiés en 48.4 min
```
