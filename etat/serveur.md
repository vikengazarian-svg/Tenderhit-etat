# Serveur du moteur V2

Mis à jour le 31/10/2026 à 08:00 · publication : **EN SERVICE (publie sur le site)**

## 🔴 **À regarder** : contrôle quotidien rouge

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-10-31 07:59:06  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-10-31 07:17:03  OK, 410 avis collectés, 213 couples recalculés, 44 republiés en 47.0 min |
| Passe DECP hebdomadaire | 2026-10-24 04:16:45  Passe hebdomadaire DECP 2026-10-24_decp : terminée en 76.7 min, mémoire max 3721 Mo ; 160 couples recalculés, 2 bloqués par la garde (M22_05, M22_07) ; 153 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-10-31 07:20:05  Contrôle du 31/10 : rouge — 215 couples identiques au site, 349 attributions anciennes gardées par le site ; EN ÉCART : M01_04, M01_27, M01_63, M01_71 ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 0.55 Go sur 7.6 · charge 0.00 · disque 30.4 % · échange 0.0 Go

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 31/10 07:17 | 410 | 213 | 44 | 0 | 47.0 min |
| 30/10 07:07 | 695 | 172 | 55 | 0 | 37.1 min |
| 29/10 07:07 | 704 | 172 | 51 | 1 | 37.9 min |
| 28/10 07:09 | 640 | 166 | 62 | 0 | 39.0 min |
| 27/10 07:08 | 351 | 161 | 63 | 0 | 38.3 min |
| 26/10 07:05 | 533 | 163 | 49 | 0 | 35.1 min |
| 25/10 07:03 | 138 | 160 | 15 | 0 | 33.7 min |
| 24/10 15:18 | 3 | 155 | 78 | 0 | 38.2 min |
| 24/10 07:03 | 478 | 160 | 50 | 0 | 33.7 min |
| 23/10 06:58 | 672 | 143 | 41 | 0 | 28.0 min |

### Passes DECP hebdomadaires

| Passe | Durée des couples | Mémoire max |
|---|---:|---:|
| 2026-10-31_decp | 53.2 min | 2538 Mo |
| 2026-10-24_decp | 33.0 min | 2373 Mo |
| 2026-10-17_decp | 41.8 min | — Mo |
| essai_pc | 26.3 min | 1616 Mo |
| essai_2026-10-16 | 26.4 min | 1950 Mo |
| essai_2026-10-16 | 25.6 min | 1950 Mo |

### Demandes des clients aujourd'hui

Aucune pour l'instant.

### Contrôles quotidiens (14 derniers)

```
2026-10-19 06:49  Contrôle du 19/10 : rouge — 96 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : C712_69, C712_74, C713_69, C713_74, C713_75, C713_FR, C715_69, C715_74 ; demandes : dernière passe il y a 19 min (attendu : toutes les minutes)
2026-10-20 06:49  Contrôle du 20/10 : rouge — 96 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : C451_42, C712_69, C712_74, C713_69, C713_74, C713_75, C713_FR, C715_69, C715_74, C772_42, M01_42, M01_71 ; demandes : dernière passe il y a 19 min (attendu : toutes les minutes)
2026-10-21 06:55  Contrôle du 21/10 : rouge — 95 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : C451_42, C712_69, C712_74, C713_69, C713_74, C713_75, C713_FR, C715_69, C715_74, C772_42, M01_42, M01_71, M03_76, M33_27, M33_76, M33_FR ; demandes : dernière passe il y a 25 min (attendu : toutes les minutes)
2026-10-22 07:05  Contrôle du 22/10 : rouge — 157 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : M04_62 ; tâches à l'heure, site à jour
2026-10-23 07:03  Contrôle du 23/10 : rouge — 157 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : M04_62 ; tâches à l'heure, site à jour
2026-10-24 07:06  Contrôle du 24/10 : rouge — 47 couples identiques au site, 175 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_26, C451_38, C451_69, C451_71, C451_74, C451_FR, C642_FR, C710_14, C710_22, C710_27, C710_29, C710_35, C710_56, C710_59, C710_60, C710_75, C710_76, C710_80, C710_93, C715_04, C715_05, C715_06, C715_13, C715_75, C715_83, C715_84, C728_69, C728_75, C741_14, C741_22, C741_27, C741_29, C741_35, C741_56, C741_59, C741_60, C741_75, C741_76, C741_80, C741_93, C772_01, C772_26, C772_38, C772_69, C772_71, C772_74, C772_FR, C794_FR, C805_34, M01_01, M01_14, M01_16, M01_24, M01_38, M01_59, M01_69, M01_73, M01_74, M01_75, M01_76, M01_83, M01_92, M01_93, M01_94, M01_FR, M03_76, M04_62, M04_76, M07_59, M07_76, M08_76, M08_81, M22_05, M22_07, M22_16, M22_17, M22_21, M22_24, M22_74, M22_75, M22_83, M22_87, M22_92, M22_93, M23_27, M23_44, M23_76, M24_69, M24_76, M30_69, M33_01, M33_38, M33_42, M33_69, M33_71, M33_85, M40_05, M40_76, P1005_14, P1005_22, P1005_27, P1005_29, P1005_35, P1005_56, P1005_59, P1005_60, P1005_75, P1005_76, P1005_80, P1005_93 ; tâches à l'heure, site à jour
2026-10-25 07:08  Contrôle du 25/10 : vert — 160 couples identiques au site ; tâches à l'heure, site à jour
2026-10-26 07:09  Contrôle du 26/10 : vert — 163 couples identiques au site ; tâches à l'heure, site à jour
2026-10-27 07:13  Contrôle du 27/10 : vert — 166 couples identiques au site, 10 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-10-28 07:14  Contrôle du 28/10 : vert — 166 couples identiques au site, 10 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-10-29 07:13  Contrôle du 29/10 : rouge — 171 couples identiques au site, 10 attributions anciennes gardées par le site ; EN ÉCART : C713_FR ; collecte du matin : 2026-10-29 07:07:57  1 ÉCHEC(S), 704 avis collectés, 172 couples recalculés, 51 republiés en 37.9 min
2026-10-30 07:12  Contrôle du 30/10 : vert — 172 couples identiques au site, 10 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-10-31 07:20  Contrôle du 31/10 : rouge — 215 couples identiques au site, 349 attributions anciennes gardées par le site ; EN ÉCART : M01_04, M01_27, M01_63, M01_71 ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                          LEFT LAST                              PASSED UNIT                     ACTIVATES
Sun 2026-11-01 06:30:00 CET    22h Sat 2026-10-31 06:30:04 CET 1h 30min ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-11-07 03:00:00 CET 6 days Sat 2026-10-31 03:00:04 CET  5h 0min ago tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                - Sat 2026-10-31 08:00:03 CET       1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                - Sat 2026-10-31 08:00:03 CET       1s ago tenderhit-relais.timer   tenderhit-relais.service

4 timers listed.
```

## Fin du journal du moteur
```
2026-10-31 07:04:45    M22_83 : 6 opportunités · inchangé · 7 s
2026-10-31 07:04:59    M22_87 : 1 opportunités · inchangé · 14 s
2026-10-31 07:05:06    M22_91 : 4 opportunités · inchangé · 6 s
2026-10-31 07:05:12    M22_92 : 8 opportunités · inchangé · 7 s
2026-10-31 07:05:19    M22_93 : 3 opportunités · inchangé · 7 s
2026-10-31 07:05:27    M22_94 : 8 opportunités · rapport et opportunités · 8 s
2026-10-31 07:05:48    M22_95 : 6 opportunités · rapport et opportunités · 22 s
2026-10-31 07:05:54    M23_27 : 6 opportunités · inchangé · 6 s
2026-10-31 07:06:03    M23_44 : 9 opportunités · rapport et opportunités · 9 s
2026-10-31 07:06:13    M23_76 : 8 opportunités · rapport et opportunités · 10 s
2026-10-31 07:06:22    M24_69 : 11 opportunités · inchangé · 9 s
2026-10-31 07:06:31    M24_76 : 11 opportunités · rapport et opportunités · 9 s
2026-10-31 07:06:41    M30_69 : 14 opportunités · rapport et opportunités · 10 s
2026-10-31 07:06:46    M33_01 : 2 opportunités · rapport et opportunités · 5 s
2026-10-31 07:06:55    M33_14 : 7 opportunités · rapport et opportunités · 9 s
2026-10-31 07:07:01    M33_27 : 6 opportunités · inchangé · 6 s
2026-10-31 07:07:08    M33_38 : 12 opportunités · inchangé · 7 s
2026-10-31 07:07:14    M33_42 : 1 opportunités · inchangé · 6 s
2026-10-31 07:07:20    M33_50 : 4 opportunités · inchangé · 6 s
2026-10-31 07:07:26    M33_61 : 3 opportunités · inchangé · 5 s
2026-10-31 07:07:35    M33_69 : 19 opportunités · inchangé · 10 s
2026-10-31 07:07:44    M33_71 : 10 opportunités · rapport et opportunités · 8 s
2026-10-31 07:07:54    M33_76 : 16 opportunités · rapport et opportunités · 10 s
2026-10-31 07:08:03    M33_85 : 5 opportunités · rapport et opportunités · 9 s
2026-10-31 07:14:17    M33_FR : 605 opportunités · rapport et opportunités · 375 s
2026-10-31 07:14:23    M40_76 : 2 opportunités · inchangé · 6 s
2026-10-31 07:14:32    P1005_14 : 1 opportunités · inchangé · 9 s
2026-10-31 07:14:41    P1005_22 : 11 opportunités · inchangé · 9 s
2026-10-31 07:14:49    P1005_27 : 4 opportunités · inchangé · 8 s
2026-10-31 07:14:58    P1005_29 : 16 opportunités · inchangé · 9 s
2026-10-31 07:15:16    P1005_35 : 22 opportunités · rapport et opportunités · 18 s
2026-10-31 07:15:28    P1005_56 : 11 opportunités · rapport et opportunités · 12 s
2026-10-31 07:15:44    P1005_59 : 21 opportunités · inchangé · 15 s
2026-10-31 07:15:53    P1005_60 : 4 opportunités · inchangé · 9 s
2026-10-31 07:16:25    P1005_75 : 47 opportunités · rapport et opportunités · 32 s
2026-10-31 07:16:36    P1005_76 : 9 opportunités · inchangé · 11 s
2026-10-31 07:16:46    P1005_80 : 0 opportunités · rapport et opportunités · 11 s
2026-10-31 07:17:03    P1005_93 : 14 opportunités · rapport et opportunités · 16 s
2026-10-31 07:17:03  OK, 410 avis collectés, 213 couples recalculés, 44 republiés en 47.0 min
2026-10-31 07:20:05  Contrôle du 31/10 : rouge — 215 couples identiques au site, 349 attributions anciennes gardées par le site ; EN ÉCART : M01_04, M01_27, M01_63, M01_71 ; tâches à l'heure, site à jour
```
