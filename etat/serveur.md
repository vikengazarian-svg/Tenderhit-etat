# Serveur du moteur V2

Mis à jour le 22/10/2026 à 08:00 · publication : **EN SERVICE (publie sur le site)**

## 🔴 **À regarder** : contrôle quotidien rouge

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-10-22 08:00:05  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-10-22 06:59:23  OK, 716 avis collectés, 143 couples recalculés, 38 republiés en 29.3 min |
| Passe DECP hebdomadaire | 2026-10-17 16:00:21  Passe hebdomadaire DECP 2026-10-17_decp : terminée en 69.6 min, mémoire max 0 Mo ; 92 couples recalculés, 2 bloqués par la garde (M22_05, M22_07) ; 88 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-10-22 07:05:06  Contrôle du 22/10 : rouge — 157 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : M04_62 ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 0.5 Go sur 7.6 · charge 0.00 · disque 22.7 % · échange 0.0 Go

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 22/10 06:59 | 716 | 143 | 38 | 0 | 29.3 min |
| 21/10 06:54 | 685 | 96 | 80 | 0 | 24.3 min |
| 20/10 06:47 | 392 | 93 | 30 | 0 | 17.8 min |
| 19/10 06:48 | 540 | 89 | 81 | 0 | 18.3 min |
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

Aucune pour l'instant.

### Contrôles quotidiens (14 derniers)

```
2026-10-19 06:49  Contrôle du 19/10 : rouge — 96 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : C712_69, C712_74, C713_69, C713_74, C713_75, C713_FR, C715_69, C715_74 ; demandes : dernière passe il y a 19 min (attendu : toutes les minutes)
2026-10-20 06:49  Contrôle du 20/10 : rouge — 96 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : C451_42, C712_69, C712_74, C713_69, C713_74, C713_75, C713_FR, C715_69, C715_74, C772_42, M01_42, M01_71 ; demandes : dernière passe il y a 19 min (attendu : toutes les minutes)
2026-10-21 06:55  Contrôle du 21/10 : rouge — 95 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : C451_42, C712_69, C712_74, C713_69, C713_74, C713_75, C713_FR, C715_69, C715_74, C772_42, M01_42, M01_71, M03_76, M33_27, M33_76, M33_FR ; demandes : dernière passe il y a 25 min (attendu : toutes les minutes)
2026-10-22 07:05  Contrôle du 22/10 : rouge — 157 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : M04_62 ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                              LEFT LAST                               PASSED UNIT                     ACTIVATES
Thu 2026-10-22 08:01:00 CEST       54s Thu 2026-10-22 08:00:04 CEST       1s ago tenderhit-demandes.timer tenderhit-demandes.service
Fri 2026-10-23 06:30:00 CEST       22h Thu 2026-10-22 06:30:04 CEST 1h 30min ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-10-24 03:00:00 CEST 1 day 18h Sun 2026-10-18 10:14:39 CEST            - tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                    - Thu 2026-10-22 08:00:04 CEST       1s ago tenderhit-relais.timer   tenderhit-relais.service

4 timers listed.
```

## Fin du journal du moteur
```
2026-10-22 06:49:34    M22_21 : 0 opportunités · rapport et opportunités · 12 s
2026-10-22 06:49:47    M22_24 : 0 opportunités · inchangé · 13 s
2026-10-22 06:49:59    M22_27 : 1 opportunités · rapport et opportunités · 13 s
2026-10-22 06:50:05    M22_74 : 3 opportunités · inchangé · 6 s
2026-10-22 06:50:14    M22_75 : 23 opportunités · opportunités · 9 s
2026-10-22 06:50:28    M22_76 : 8 opportunités · rapport et opportunités · 14 s
2026-10-22 06:50:34    M22_83 : 8 opportunités · inchangé · 6 s
2026-10-22 06:50:47    M22_87 : 1 opportunités · inchangé · 13 s
2026-10-22 06:50:55    M22_92 : 17 opportunités · rapport et opportunités · 7 s
2026-10-22 06:51:01    M22_93 : 11 opportunités · inchangé · 6 s
2026-10-22 06:51:07    M22_94 : 12 opportunités · inchangé · 6 s
2026-10-22 06:51:13    M23_27 : 6 opportunités · inchangé · 6 s
2026-10-22 06:51:21    M23_44 : 8 opportunités · rapport et opportunités · 9 s
2026-10-22 06:51:30    M23_76 : 5 opportunités · rapport et opportunités · 9 s
2026-10-22 06:51:39    M24_69 : 9 opportunités · inchangé · 9 s
2026-10-22 06:51:47    M24_76 : 9 opportunités · rapport et opportunités · 8 s
2026-10-22 06:51:56    M30_69 : 13 opportunités · inchangé · 9 s
2026-10-22 06:52:02    M33_27 : 8 opportunités · inchangé · 6 s
2026-10-22 06:52:09    M33_38 : 14 opportunités · rapport et opportunités · 8 s
2026-10-22 06:52:16    M33_42 : 1 opportunités · rapport et opportunités · 7 s
2026-10-22 06:52:25    M33_69 : 16 opportunités · inchangé · 9 s
2026-10-22 06:52:33    M33_71 : 4 opportunités · rapport et opportunités · 7 s
2026-10-22 06:52:41    M33_76 : 10 opportunités · rapport et opportunités · 8 s
2026-10-22 06:52:47    M33_85 : 3 opportunités · inchangé · 6 s
2026-10-22 06:57:01    M33_FR : 438 opportunités · rapport et opportunités · 254 s
2026-10-22 06:57:07    M40_76 : 2 opportunités · inchangé · 6 s
2026-10-22 06:57:16    P1005_14 : 6 opportunités · inchangé · 9 s
2026-10-22 06:57:24    P1005_22 : 5 opportunités · inchangé · 8 s
2026-10-22 06:57:31    P1005_27 : 6 opportunités · inchangé · 7 s
2026-10-22 06:57:40    P1005_29 : 8 opportunités · inchangé · 8 s
2026-10-22 06:57:50    P1005_35 : 13 opportunités · inchangé · 10 s
2026-10-22 06:57:59    P1005_56 : 10 opportunités · inchangé · 9 s
2026-10-22 06:58:13    P1005_59 : 25 opportunités · inchangé · 15 s
2026-10-22 06:58:22    P1005_60 : 5 opportunités · inchangé · 8 s
2026-10-22 06:58:50    P1005_75 : 30 opportunités · rapport et opportunités · 29 s
2026-10-22 06:59:04    P1005_76 : 5 opportunités · rapport et opportunités · attributions anciennes retirées : non fait (identifiant de plus de 300 caractères dans la DECP) · 13 s
2026-10-22 06:59:12    P1005_80 : 4 opportunités · inchangé · 8 s
2026-10-22 06:59:23    P1005_93 : 7 opportunités · inchangé · 12 s
2026-10-22 06:59:23  OK, 716 avis collectés, 143 couples recalculés, 38 republiés en 29.3 min
2026-10-22 07:05:06  Contrôle du 22/10 : rouge — 157 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : M04_62 ; tâches à l'heure, site à jour
```
