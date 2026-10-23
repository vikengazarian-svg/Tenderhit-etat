# Serveur du moteur V2

Mis à jour le 23/10/2026 à 07:00 · publication : **EN SERVICE (publie sur le site)**

## 🔴 **À regarder** : demandes des clients non traitées depuis plus de 15 min

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-10-23 06:29:05  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-10-23 06:58:02  OK, 672 avis collectés, 143 couples recalculés, 41 republiés en 28.0 min |
| Passe DECP hebdomadaire | 2026-10-17 16:00:21  Passe hebdomadaire DECP 2026-10-17_decp : terminée en 69.6 min, mémoire max 0 Mo ; 92 couples recalculés, 2 bloqués par la garde (M22_05, M22_07) ; 88 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-10-22 07:05:06  Contrôle du 22/10 : rouge — 157 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : M04_62 ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 1.42 Go sur 7.6 · charge 1.06 · disque 23.0 % · échange 0.0 Go

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
NEXT                         LEFT LAST                            PASSED UNIT                     ACTIVATES
Sat 2026-10-24 03:00:00 CEST  19h Sun 2026-10-18 10:14:39 CEST         - tenderhit-hebdo.timer    tenderhit-hebdo.service
-                               - Fri 2026-10-23 06:30:04 CEST 29min ago tenderhit-collecte.timer tenderhit-collecte.service
-                               - Fri 2026-10-23 07:00:00 CEST    1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                               - Fri 2026-10-23 07:00:00 CEST    1s ago tenderhit-relais.timer   tenderhit-relais.service

4 timers listed.
```

## Fin du journal du moteur
```
2026-10-23 06:48:13    M22_17 : 1 opportunités · inchangé · 13 s
2026-10-23 06:48:25    M22_21 : 0 opportunités · rapport et opportunités · 12 s
2026-10-23 06:48:38    M22_24 : 0 opportunités · inchangé · 13 s
2026-10-23 06:48:50    M22_27 : 1 opportunités · rapport et opportunités · 12 s
2026-10-23 06:48:57    M22_74 : 3 opportunités · rapport et opportunités · 7 s
2026-10-23 06:49:06    M22_75 : 23 opportunités · rapport et opportunités · 9 s
2026-10-23 06:49:20    M22_76 : 7 opportunités · rapport et opportunités · 14 s
2026-10-23 06:49:26    M22_83 : 8 opportunités · inchangé · 6 s
2026-10-23 06:49:39    M22_87 : 1 opportunités · inchangé · 13 s
2026-10-23 06:49:45    M22_92 : 17 opportunités · inchangé · 6 s
2026-10-23 06:49:52    M22_93 : 11 opportunités · inchangé · 6 s
2026-10-23 06:49:59    M22_94 : 12 opportunités · rapport et opportunités · 7 s
2026-10-23 06:50:04    M23_27 : 6 opportunités · inchangé · 6 s
2026-10-23 06:50:13    M23_44 : 7 opportunités · rapport et opportunités · 9 s
2026-10-23 06:50:20    M23_76 : 5 opportunités · inchangé · 7 s
2026-10-23 06:50:29    M24_69 : 10 opportunités · rapport et opportunités · 9 s
2026-10-23 06:50:36    M24_76 : 9 opportunités · inchangé · 7 s
2026-10-23 06:50:46    M30_69 : 14 opportunités · rapport et opportunités · 10 s
2026-10-23 06:50:53    M33_27 : 7 opportunités · rapport et opportunités · 6 s
2026-10-23 06:51:00    M33_38 : 13 opportunités · rapport et opportunités · 7 s
2026-10-23 06:51:06    M33_42 : 1 opportunités · inchangé · 6 s
2026-10-23 06:51:16    M33_69 : 16 opportunités · rapport et opportunités · 10 s
2026-10-23 06:51:22    M33_71 : 4 opportunités · inchangé · 6 s
2026-10-23 06:51:29    M33_76 : 10 opportunités · inchangé · 7 s
2026-10-23 06:51:35    M33_85 : 3 opportunités · inchangé · 6 s
2026-10-23 06:55:40    M33_FR : 443 opportunités · rapport et opportunités · 245 s
2026-10-23 06:55:45    M40_76 : 2 opportunités · inchangé · 6 s
2026-10-23 06:55:54    P1005_14 : 6 opportunités · inchangé · 8 s
2026-10-23 06:56:02    P1005_22 : 5 opportunités · inchangé · 8 s
2026-10-23 06:56:09    P1005_27 : 6 opportunités · inchangé · 8 s
2026-10-23 06:56:17    P1005_29 : 8 opportunités · inchangé · 8 s
2026-10-23 06:56:27    P1005_35 : 13 opportunités · inchangé · 10 s
2026-10-23 06:56:36    P1005_56 : 10 opportunités · inchangé · 8 s
2026-10-23 06:56:56    P1005_59 : 25 opportunités · rapport et opportunités · 20 s
2026-10-23 06:57:04    P1005_60 : 5 opportunités · inchangé · 8 s
2026-10-23 06:57:32    P1005_75 : 31 opportunités · rapport et opportunités · 27 s
2026-10-23 06:57:42    P1005_76 : 5 opportunités · inchangé · 10 s
2026-10-23 06:57:50    P1005_80 : 4 opportunités · inchangé · 8 s
2026-10-23 06:58:02    P1005_93 : 7 opportunités · inchangé · 12 s
2026-10-23 06:58:02  OK, 672 avis collectés, 143 couples recalculés, 41 republiés en 28.0 min
```
