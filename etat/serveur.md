# Serveur du moteur V2

Mis à jour le 24/10/2026 à 07:00 · publication : **EN SERVICE (publie sur le site)**

## 🔴 **À regarder** : demandes des clients non traitées depuis plus de 15 min

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-10-24 06:29:04  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-10-23 06:58:02  OK, 672 avis collectés, 143 couples recalculés, 41 republiés en 28.0 min |
| Passe DECP hebdomadaire | 2026-10-24 04:16:45  Passe hebdomadaire DECP 2026-10-24_decp : terminée en 76.7 min, mémoire max 3721 Mo ; 160 couples recalculés, 2 bloqués par la garde (M22_05, M22_07) ; 153 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-10-23 07:03:17  Contrôle du 23/10 : rouge — 157 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : M04_62 ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 2.01 Go sur 7.6 · charge 1.04 · disque 25.7 % · échange 0.0 Go

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 23/10 06:58 | 672 | 143 | 41 | 0 | 28.0 min |
| 22/10 06:59 | 716 | 143 | 38 | 0 | 29.3 min |
| 21/10 06:54 | 685 | 96 | 80 | 0 | 24.3 min |
| 20/10 06:47 | 392 | 93 | 30 | 0 | 17.8 min |
| 19/10 06:48 | 540 | 89 | 81 | 0 | 18.3 min |
| 17/10 12:47 | 1148 | 73 | 73 | 0 | 26.6 min |

### Passes DECP hebdomadaires

| Passe | Durée des couples | Mémoire max |
|---|---:|---:|
| 2026-10-24_decp | 33.0 min | 2373 Mo |
| 2026-10-17_decp | 41.8 min | — Mo |
| essai_pc | 26.3 min | 1616 Mo |
| essai_2026-10-16 | 26.4 min | 1950 Mo |
| essai_2026-10-16 | 25.6 min | 1950 Mo |
| essai_2026-10-16 | 23.9 min | 1950 Mo |

### Demandes des clients aujourd'hui

Aucune pour l'instant.

### Contrôles quotidiens (14 derniers)

```
2026-10-19 06:49  Contrôle du 19/10 : rouge — 96 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : C712_69, C712_74, C713_69, C713_74, C713_75, C713_FR, C715_69, C715_74 ; demandes : dernière passe il y a 19 min (attendu : toutes les minutes)
2026-10-20 06:49  Contrôle du 20/10 : rouge — 96 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : C451_42, C712_69, C712_74, C713_69, C713_74, C713_75, C713_FR, C715_69, C715_74, C772_42, M01_42, M01_71 ; demandes : dernière passe il y a 19 min (attendu : toutes les minutes)
2026-10-21 06:55  Contrôle du 21/10 : rouge — 95 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : C451_42, C712_69, C712_74, C713_69, C713_74, C713_75, C713_FR, C715_69, C715_74, C772_42, M01_42, M01_71, M03_76, M33_27, M33_76, M33_FR ; demandes : dernière passe il y a 25 min (attendu : toutes les minutes)
2026-10-22 07:05  Contrôle du 22/10 : rouge — 157 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : M04_62 ; tâches à l'heure, site à jour
2026-10-23 07:03  Contrôle du 23/10 : rouge — 157 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : M04_62 ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                           LEFT LAST                               PASSED UNIT                     ACTIVATES
Sat 2026-10-24 07:01:00 CEST    58s Sat 2026-10-24 07:00:00 CEST       1s ago tenderhit-demandes.timer tenderhit-demandes.service
Sat 2026-10-31 03:00:00 CET  6 days Sat 2026-10-24 03:00:04 CEST 3h 59min ago tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                 - Sat 2026-10-24 06:30:04 CEST    29min ago tenderhit-collecte.timer tenderhit-collecte.service
-                                 - Sat 2026-10-24 07:00:00 CEST       1s ago tenderhit-relais.timer   tenderhit-relais.service

4 timers listed.
```

## Fin du journal du moteur
```
2026-10-24 06:50:38    M01_92 : 27 opportunités · inchangé · 8 s
2026-10-24 06:50:46    M01_93 : 21 opportunités · inchangé · 8 s
2026-10-24 06:50:53    M01_94 : 16 opportunités · inchangé · 7 s
2026-10-24 06:52:10    M01_FR : 1458 opportunités · rapport et opportunités · 76 s
2026-10-24 06:52:16    M03_76 : 2 opportunités · inchangé · 7 s
2026-10-24 06:52:25    M04_62 : 16 opportunités · inchangé · 8 s
2026-10-24 06:52:28    M04_76 : 12 opportunités · inchangé · 4 s
2026-10-24 06:52:37    M07_59 : 46 opportunités · rapport et opportunités · 9 s
2026-10-24 06:52:44    M07_76 : 15 opportunités · rapport et opportunités · 7 s
2026-10-24 06:52:49    M08_76 : 11 opportunités · rapport et opportunités · 5 s
2026-10-24 06:52:57    M08_81 : 2 opportunités · rapport et opportunités · 8 s
2026-10-24 06:53:07    M22_05 : 0 opportunités · rapport et opportunités · 10 s
2026-10-24 06:53:22    M22_07 : 1 opportunités · rapport et opportunités · 15 s
2026-10-24 06:53:35    M22_16 : 1 opportunités · inchangé · 13 s
2026-10-24 06:53:48    M22_17 : 1 opportunités · inchangé · 13 s
2026-10-24 06:54:01    M22_21 : 0 opportunités · rapport et opportunités · 13 s
2026-10-24 06:54:14    M22_24 : 0 opportunités · inchangé · 13 s
2026-10-24 06:54:26    M22_27 : 1 opportunités · rapport et opportunités · 13 s
2026-10-24 06:54:32    M22_74 : 3 opportunités · inchangé · 6 s
2026-10-24 06:54:40    M22_75 : 23 opportunités · inchangé · 8 s
2026-10-24 06:54:54    M22_76 : 6 opportunités · rapport et opportunités · 14 s
2026-10-24 06:55:02    M22_83 : 7 opportunités · rapport et opportunités · 8 s
2026-10-24 06:55:15    M22_87 : 1 opportunités · inchangé · 13 s
2026-10-24 06:55:21    M22_92 : 17 opportunités · inchangé · 6 s
2026-10-24 06:55:28    M22_93 : 11 opportunités · rapport et opportunités · 7 s
2026-10-24 06:55:34    M22_94 : 12 opportunités · inchangé · 6 s
2026-10-24 06:55:40    M23_27 : 6 opportunités · inchangé · 6 s
2026-10-24 06:55:47    M23_44 : 7 opportunités · inchangé · 7 s
2026-10-24 06:55:56    M23_76 : 4 opportunités · rapport et opportunités · 9 s
2026-10-24 06:56:06    M24_69 : 11 opportunités · rapport et opportunités · 10 s
2026-10-24 06:56:14    M24_76 : 7 opportunités · rapport et opportunités · 8 s
2026-10-24 06:56:23    M30_69 : 15 opportunités · rapport et opportunités · 9 s
2026-10-24 06:56:26    M33_01 : 0 opportunités · inchangé · 3 s
2026-10-24 06:56:31    M33_27 : 7 opportunités · inchangé · 6 s
2026-10-24 06:56:38    M33_38 : 13 opportunités · inchangé · 7 s
2026-10-24 06:56:43    M33_42 : 1 opportunités · inchangé · 6 s
2026-10-24 06:56:53    M33_69 : 17 opportunités · rapport et opportunités · 10 s
2026-10-24 06:56:59    M33_71 : 4 opportunités · inchangé · 6 s
2026-10-24 06:57:06    M33_76 : 10 opportunités · inchangé · 7 s
2026-10-24 06:57:14    M33_85 : 4 opportunités · rapport et opportunités · 7 s
```
