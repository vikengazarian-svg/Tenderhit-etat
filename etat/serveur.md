# Serveur du moteur V2

Mis à jour le 21/10/2026 à 06:56 · publication : **EN SERVICE (publie sur le site)**

## 🔴 **À regarder** : contrôle quotidien rouge ; demandes des clients non traitées depuis plus de 15 min

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-10-21 06:29:05  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-10-21 06:54:19  OK, 685 avis collectés, 96 couples recalculés, 80 republiés en 24.2 min |
| Passe DECP hebdomadaire | 2026-10-17 16:00:21  Passe hebdomadaire DECP 2026-10-17_decp : terminée en 69.6 min, mémoire max 0 Mo ; 92 couples recalculés, 2 bloqués par la garde (M22_05, M22_07) ; 88 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-10-21 06:55:34  Contrôle du 21/10 : rouge — 95 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : C451_42, C712_69, C712_74, C713_69, C713_74, C713_75, C713_FR, C715_69, C715_74, C772_42, M01_42, M01_71, M03_76, M33_27, M33_76, M33_FR ; demandes : dernière passe il y a 25 min (attendu : toutes les minutes) |

**Machine maintenant** : mémoire 0.49 Go sur 7.6 · charge 0.26 · disque 22.2 % · échange 0.0 Go

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
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
```

## Tâches planifiées
```
NEXT                           LEFT LAST                            PASSED UNIT                     ACTIVATES
Thu 2026-10-22 06:30:00 CEST    23h Wed 2026-10-21 06:30:04 CEST 26min ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-10-24 03:00:00 CEST 2 days Sun 2026-10-18 10:14:39 CEST         - tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                 - Wed 2026-10-21 06:56:04 CEST    1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                 - Wed 2026-10-21 06:56:04 CEST    1s ago tenderhit-relais.timer   tenderhit-relais.service

4 timers listed.
```

## Fin du journal du moteur
```
2026-10-21 06:43:40    M01_93 : 21 opportunités · inchangé · 8 s
2026-10-21 06:43:49    M01_94 : 16 opportunités · rapport et opportunités · 9 s
2026-10-21 06:45:07    M01_FR : 1461 opportunités · rapport et opportunités · 78 s
2026-10-21 06:45:14    M03_76 : 2 opportunités · opportunités · 7 s
2026-10-21 06:45:23    M04_62 : 15 opportunités · rapport et opportunités · 9 s
2026-10-21 06:45:27    M04_76 : 12 opportunités · inchangé · 4 s
2026-10-21 06:45:34    M07_59 : 48 opportunités · rapport et opportunités · 7 s
2026-10-21 06:45:40    M07_76 : 16 opportunités · rapport et opportunités · 6 s
2026-10-21 06:45:45    M08_76 : 13 opportunités · rapport et opportunités · 5 s
2026-10-21 06:45:53    M08_81 : 2 opportunités · rapport et opportunités · 8 s
2026-10-21 06:46:07    M22_16 : 1 opportunités · rapport et opportunités · 14 s
2026-10-21 06:46:21    M22_17 : 1 opportunités · rapport et opportunités · 14 s
2026-10-21 06:46:33    M22_21 : 0 opportunités · rapport et opportunités · 12 s
2026-10-21 06:46:47    M22_24 : 0 opportunités · rapport et opportunités · 14 s
2026-10-21 06:46:59    M22_27 : 1 opportunités · rapport et opportunités · 13 s
2026-10-21 06:47:07    M22_74 : 3 opportunités · rapport et opportunités · 7 s
2026-10-21 06:47:16    M22_75 : 24 opportunités · rapport et opportunités · 9 s
2026-10-21 06:47:30    M22_76 : 9 opportunités · rapport et opportunités · 14 s
2026-10-21 06:47:37    M22_83 : 8 opportunités · rapport et opportunités · 7 s
2026-10-21 06:47:51    M22_87 : 1 opportunités · rapport et opportunités · 14 s
2026-10-21 06:47:59    M22_92 : 16 opportunités · rapport et opportunités · 7 s
2026-10-21 06:48:06    M22_93 : 11 opportunités · rapport et opportunités · 8 s
2026-10-21 06:48:14    M22_94 : 12 opportunités · rapport et opportunités · 7 s
2026-10-21 06:48:20    M23_27 : 6 opportunités · rapport et opportunités · 6 s
2026-10-21 06:48:29    M23_44 : 9 opportunités · rapport et opportunités · 8 s
2026-10-21 06:48:37    M23_76 : 6 opportunités · rapport et opportunités · 8 s
2026-10-21 06:48:47    M24_69 : 9 opportunités · rapport et opportunités · 10 s
2026-10-21 06:48:55    M24_76 : 10 opportunités · rapport et opportunités · 8 s
2026-10-21 06:49:04    M30_69 : 13 opportunités · rapport et opportunités · 9 s
2026-10-21 06:49:11    M33_27 : 8 opportunités · rapport et opportunités · 7 s
2026-10-21 06:49:18    M33_38 : 14 opportunités · rapport et opportunités · 8 s
2026-10-21 06:49:25    M33_42 : 2 opportunités · rapport et opportunités · 7 s
2026-10-21 06:49:35    M33_69 : 16 opportunités · rapport et opportunités · 10 s
2026-10-21 06:49:42    M33_71 : 3 opportunités · rapport et opportunités · 7 s
2026-10-21 06:49:50    M33_76 : 11 opportunités · inchangé · 7 s
2026-10-21 06:49:57    M33_85 : 3 opportunités · rapport et opportunités · 8 s
2026-10-21 06:54:12    M33_FR : 429 opportunités · rapport et opportunités · 255 s
2026-10-21 06:54:19    M40_76 : 2 opportunités · rapport et opportunités · 7 s
2026-10-21 06:54:19  OK, 685 avis collectés, 96 couples recalculés, 80 republiés en 24.2 min
2026-10-21 06:55:34  Contrôle du 21/10 : rouge — 95 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : C451_42, C712_69, C712_74, C713_69, C713_74, C713_75, C713_FR, C715_69, C715_74, C772_42, M01_42, M01_71, M03_76, M33_27, M33_76, M33_FR ; demandes : dernière passe il y a 25 min (attendu : toutes les minutes)
```
