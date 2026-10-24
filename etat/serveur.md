# Serveur du moteur V2

Mis à jour le 24/10/2026 à 15:00 · publication : **EN SERVICE (publie sur le site)**

## 🔴 **À regarder** : contrôle quotidien rouge ; demandes des clients non traitées depuis plus de 15 min

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-10-24 14:40:05  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-10-24 07:03:47  OK, 478 avis collectés, 160 couples recalculés, 50 republiés en 33.7 min |
| Passe DECP hebdomadaire | 2026-10-24 04:16:45  Passe hebdomadaire DECP 2026-10-24_decp : terminée en 76.7 min, mémoire max 3721 Mo ; 160 couples recalculés, 2 bloqués par la garde (M22_05, M22_07) ; 153 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-10-24 07:06:51  Contrôle du 24/10 : rouge — 47 couples identiques au site, 175 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_26, C451_38, C451_69, C451_71, C451_74, C451_FR, C642_FR, C710_14, C710_22, C710_27, C710_29, C710_35, C710_56, C710_59, C710_60, C710_75, C710_76, C710_80, C710_93, C715_04, C715_05, C715_06, C715_13, C715_75, C715_83, C715_84, C728_69, C728_75, C741_14, C741_22, C741_27, C741_29, C741_35, C741_56, C741_59, C741_60, C741_75, C741_76, C741_80, C741_93, C772_01, C772_26, C772_38, C772_69, C772_71, C772_74, C772_FR, C794_FR, C805_34, M01_01, M01_14, M01_16, M01_24, M01_38, M01_59, M01_69, M01_73, M01_74, M01_75, M01_76, M01_83, M01_92, M01_93, M01_94, M01_FR, M03_76, M04_62, M04_76, M07_59, M07_76, M08_76, M08_81, M22_05, M22_07, M22_16, M22_17, M22_21, M22_24, M22_74, M22_75, M22_83, M22_87, M22_92, M22_93, M23_27, M23_44, M23_76, M24_69, M24_76, M30_69, M33_01, M33_38, M33_42, M33_69, M33_71, M33_85, M40_05, M40_76, P1005_14, P1005_22, P1005_27, P1005_29, P1005_35, P1005_56, P1005_59, P1005_60, P1005_75, P1005_76, P1005_80, P1005_93 ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 1.52 Go sur 7.6 · charge 1.33 · disque 26.5 % · échange 0.0 Go

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 24/10 07:03 | 478 | 160 | 50 | 0 | 33.7 min |
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
2026-10-24 07:06  Contrôle du 24/10 : rouge — 47 couples identiques au site, 175 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_26, C451_38, C451_69, C451_71, C451_74, C451_FR, C642_FR, C710_14, C710_22, C710_27, C710_29, C710_35, C710_56, C710_59, C710_60, C710_75, C710_76, C710_80, C710_93, C715_04, C715_05, C715_06, C715_13, C715_75, C715_83, C715_84, C728_69, C728_75, C741_14, C741_22, C741_27, C741_29, C741_35, C741_56, C741_59, C741_60, C741_75, C741_76, C741_80, C741_93, C772_01, C772_26, C772_38, C772_69, C772_71, C772_74, C772_FR, C794_FR, C805_34, M01_01, M01_14, M01_16, M01_24, M01_38, M01_59, M01_69, M01_73, M01_74, M01_75, M01_76, M01_83, M01_92, M01_93, M01_94, M01_FR, M03_76, M04_62, M04_76, M07_59, M07_76, M08_76, M08_81, M22_05, M22_07, M22_16, M22_17, M22_21, M22_24, M22_74, M22_75, M22_83, M22_87, M22_92, M22_93, M23_27, M23_44, M23_76, M24_69, M24_76, M30_69, M33_01, M33_38, M33_42, M33_69, M33_71, M33_85, M40_05, M40_76, P1005_14, P1005_22, P1005_27, P1005_29, P1005_35, P1005_56, P1005_59, P1005_60, P1005_75, P1005_76, P1005_80, P1005_93 ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                           LEFT LAST                          PASSED UNIT                     ACTIVATES
Sat 2026-10-24 15:01:00 CEST    58s Sat 2026-10-24 15:00:00 CEST  1s ago tenderhit-demandes.timer tenderhit-demandes.service
Sun 2026-10-25 06:30:00 CET     16h Sat 2026-10-24 06:30:04 CEST  8h ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-10-31 03:00:00 CET  6 days Sat 2026-10-24 03:00:04 CEST 11h ago tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                 - Sat 2026-10-24 15:00:00 CEST  1s ago tenderhit-relais.timer   tenderhit-relais.service

4 timers listed.
```

## Fin du journal du moteur
```
2026-10-24 14:47:05    C712_35 : 17 opportunités · rapport et opportunités · 19 s
2026-10-24 14:47:13    C712_56 : 5 opportunités · rapport et opportunités · 8 s
2026-10-24 14:47:30    C712_59 : 8 opportunités · rapport et opportunités · 17 s
2026-10-24 14:47:35    C712_60 : 5 opportunités · inchangé · 4 s
2026-10-24 14:47:52    C712_69 : 8 opportunités · rapport et opportunités · 18 s
2026-10-24 14:47:57    C712_74 : 5 opportunités · inchangé · 5 s
2026-10-24 14:48:18    C712_75 : 25 opportunités · rapport et opportunités · 21 s
2026-10-24 14:48:23    C712_76 : 7 opportunités · inchangé · 5 s
2026-10-24 14:48:29    C712_80 : 4 opportunités · rapport et opportunités · 6 s
2026-10-24 14:48:34    C712_83 : 2 opportunités · inchangé · 5 s
2026-10-24 14:48:38    C712_84 : 2 opportunités · inchangé · 4 s
2026-10-24 14:48:51    C712_93 : 8 opportunités · rapport et opportunités · 13 s
2026-10-24 14:48:53    C713_04 : 0 opportunités · inchangé · 2 s
2026-10-24 14:48:57    C713_06 : 0 opportunités · inchangé · 4 s
2026-10-24 14:49:20    C713_13 : 21 opportunités · rapport et opportunités · 23 s
2026-10-24 14:49:38    C713_69 : 11 opportunités · rapport et opportunités · 18 s
2026-10-24 14:49:44    C713_74 : 12 opportunités · inchangé · 6 s
2026-10-24 14:50:17    C713_75 : 47 opportunités · rapport et opportunités · 33 s
2026-10-24 14:50:30    C713_83 : 22 opportunités · rapport et opportunités · 13 s
2026-10-24 14:50:35    C713_84 : 1 opportunités · inchangé · 4 s
2026-10-24 14:58:16    C713_FR : 620 opportunités · rapport et opportunités · attributions anciennes retirées : non fait (identifiant de plus de 300 caractères dans la DECP) · 461 s
2026-10-24 14:58:19    C715_04 : 0 opportunités · inchangé · 3 s
2026-10-24 14:58:23    C715_06 : 0 opportunités · inchangé · 4 s
2026-10-24 14:58:28    C715_13 : 1 opportunités · inchangé · 5 s
2026-10-24 14:58:32    C715_69 : 1 opportunités · inchangé · 3 s
2026-10-24 14:58:37    C715_74 : 0 opportunités · inchangé · 5 s
2026-10-24 14:58:43    C715_75 : 2 opportunités · rapport et opportunités · 6 s
2026-10-24 14:58:48    C715_83 : 0 opportunités · inchangé · 5 s
2026-10-24 14:58:52    C715_84 : 0 opportunités · inchangé · 5 s
2026-10-24 14:58:56    C722_76 : 17 opportunités · inchangé · 4 s
2026-10-24 14:59:05    C728_69 : 4 opportunités · rapport et opportunités · 9 s
2026-10-24 14:59:14    C728_75 : 4 opportunités · rapport et opportunités · 9 s
2026-10-24 14:59:19    C741_14 : 0 opportunités · inchangé · 6 s
2026-10-24 14:59:24    C741_22 : 0 opportunités · inchangé · 5 s
2026-10-24 14:59:30    C741_27 : 0 opportunités · inchangé · 5 s
2026-10-24 14:59:35    C741_29 : 0 opportunités · inchangé · 5 s
2026-10-24 14:59:41    C741_35 : 0 opportunités · inchangé · 6 s
2026-10-24 14:59:46    C741_56 : 0 opportunités · inchangé · 5 s
2026-10-24 14:59:52    C741_59 : 0 opportunités · inchangé · 6 s
2026-10-24 14:59:57    C741_60 : 0 opportunités · inchangé · 6 s
```
