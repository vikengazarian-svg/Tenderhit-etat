# Serveur du moteur V2

Mis à jour le 07/11/2026 à 07:00 · publication : **EN SERVICE (publie sur le site)**

## 🔴 **À regarder** : demandes des clients non traitées depuis plus de 15 min

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-07 06:29:05  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-06 07:14:21  OK, 770 avis collectés, 224 couples recalculés, 63 republiés en 44.3 min |
| Passe DECP hebdomadaire | 2026-11-07 04:22:15  Passe hebdomadaire DECP 2026-11-07_decp : terminée avec échecs en 82.2 min, mémoire max 4269 Mo ; 236 couples recalculés, 0 bloqués par la garde, échecs : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; 222 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-06 07:17:01  Contrôle du 06/11 : rouge — 222 couples identiques au site, 349 attributions anciennes gardées par le site ; EN ÉCART : C713_75, M08_81 ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 1.47 Go sur 7.6 · charge 1.78 · disque 36.5 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : +5.4 point(s) par semaine · 80 % dans **8.1 semaine(s)**

```
Mesure du 2026-11-07 05:45 :
  entrepot/sources                            3.50 Go
  entrepot/decp                               1.59 Go
  entrepot/boamp                              1.38 Go
  entrepot/passes                             0.89 Go
  production/controles                        0.72 Go
  entrepot/execution                          0.68 Go
  parallele                                   0.66 Go
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
Dernière purge (2026-11-07 05:45) : faite, 0 élément(s), 0.0 Go libérés
```

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 06/11 07:14 | 770 | 224 | 63 | 0 | 44.3 min |
| 05/11 07:12 | 770 | 223 | 65 | 0 | 42.3 min |
| 04/11 07:11 | 599 | 220 | 66 | 0 | 41.9 min |
| 03/11 07:09 | 315 | 219 | 79 | 0 | 39.6 min |
| 02/11 07:10 | 251 | 219 | 42 | 0 | 40.9 min |
| 01/11 07:13 | 543 | 219 | 219 | 0 | 43.6 min |
| 31/10 07:17 | 410 | 213 | 44 | 0 | 47.0 min |
| 30/10 07:07 | 695 | 172 | 55 | 0 | 37.1 min |
| 29/10 07:07 | 704 | 172 | 51 | 1 | 37.9 min |
| 28/10 07:09 | 640 | 166 | 62 | 0 | 39.0 min |

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
2026-10-26 07:09  Contrôle du 26/10 : vert — 163 couples identiques au site ; tâches à l'heure, site à jour
2026-10-27 07:13  Contrôle du 27/10 : vert — 166 couples identiques au site, 10 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-10-28 07:14  Contrôle du 28/10 : vert — 166 couples identiques au site, 10 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
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
```

## Tâches planifiées
```
NEXT                          LEFT LAST                              PASSED UNIT                     ACTIVATES
Sat 2026-11-07 07:01:00 CET    57s Sat 2026-11-07 07:00:00 CET       1s ago tenderhit-demandes.timer tenderhit-demandes.service
Sun 2026-11-08 05:45:00 CET    22h Sat 2026-11-07 05:45:04 CET 1h 14min ago tenderhit-purge.timer    tenderhit-purge.service
Sat 2026-11-14 03:00:00 CET 6 days Sat 2026-11-07 03:00:00 CET  4h 0min ago tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                - Sat 2026-11-07 06:30:04 CET    29min ago tenderhit-collecte.timer tenderhit-collecte.service
-                                - Sat 2026-11-07 07:00:00 CET       1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-07 06:51:48    M01_71 : 7 opportunités · inchangé · 5 s
2026-11-07 06:51:54    M01_73 : 11 opportunités · inchangé · 6 s
2026-11-07 06:52:00    M01_74 : 21 opportunités · inchangé · 6 s
2026-11-07 06:52:15    M01_75 : 66 opportunités · inchangé · 15 s
2026-11-07 06:52:22    M01_76 : 19 opportunités · inchangé · 7 s
2026-11-07 06:52:30    M01_83 : 21 opportunités · inchangé · 8 s
2026-11-07 06:52:34    M01_89 : 7 opportunités · inchangé · 5 s
2026-11-07 06:52:46    M01_90 : 2 opportunités · rapport et opportunités · 12 s
2026-11-07 06:52:55    M01_92 : 19 opportunités · inchangé · 9 s
2026-11-07 06:53:03    M01_93 : 26 opportunités · inchangé · 8 s
2026-11-07 06:53:11    M01_94 : 15 opportunités · inchangé · 8 s
2026-11-07 06:54:42    M01_FR : 1227 opportunités · rapport et opportunités · 91 s
2026-11-07 06:54:50    M03_76 : 8 opportunités · rapport et opportunités · 8 s
2026-11-07 06:54:58    M04_62 : 14 opportunités · inchangé · 9 s
2026-11-07 06:55:03    M04_76 : 6 opportunités · inchangé · 4 s
2026-11-07 06:55:10    M07_59 : 45 opportunités · rapport et opportunités · 8 s
2026-11-07 06:55:15    M07_76 : 18 opportunités · inchangé · 5 s
2026-11-07 06:55:20    M08_76 : 19 opportunités · inchangé · 4 s
2026-11-07 06:55:28    M08_81 : 0 opportunités · inchangé · 8 s
2026-11-07 06:55:30    M22_01 : 0 opportunités · inchangé · 2 s
2026-11-07 06:55:40    M22_05 : 0 opportunités · inchangé · 10 s
2026-11-07 06:55:56    M22_07 : 1 opportunités · rapport et opportunités · 16 s
2026-11-07 06:56:08    M22_08 : 1 opportunités · rapport et opportunités · 12 s
2026-11-07 06:56:22    M22_10 : 0 opportunités · rapport et opportunités · 15 s
2026-11-07 06:56:37    M22_11 : 0 opportunités · rapport et opportunités · 15 s
2026-11-07 06:56:50    M22_14 : 2 opportunités · inchangé · 13 s
2026-11-07 06:57:05    M22_16 : 0 opportunités · rapport et opportunités · 15 s
2026-11-07 06:57:19    M22_17 : 0 opportunités · rapport et opportunités · 15 s
2026-11-07 06:57:31    M22_21 : 2 opportunités · inchangé · 12 s
2026-11-07 06:57:45    M22_24 : 0 opportunités · rapport et opportunités · 15 s
2026-11-07 06:58:04    M22_26 : 1 opportunités · rapport et opportunités · 19 s
2026-11-07 06:58:16    M22_27 : 1 opportunités · inchangé · 12 s
2026-11-07 06:58:28    M22_37 : 0 opportunités · rapport et opportunités · 12 s
2026-11-07 06:58:36    M22_38 : 7 opportunités · rapport et opportunités · 7 s
2026-11-07 06:58:41    M22_42 : 1 opportunités · inchangé · 6 s
2026-11-07 06:58:58    M22_50 : 1 opportunités · inchangé · 17 s
2026-11-07 06:59:13    M22_51 : 1 opportunités · rapport et opportunités · 15 s
2026-11-07 06:59:27    M22_52 : 0 opportunités · rapport et opportunités · 15 s
2026-11-07 06:59:42    M22_54 : 0 opportunités · rapport et opportunités · 15 s
2026-11-07 06:59:57    M22_55 : 1 opportunités · rapport et opportunités · 15 s
```
