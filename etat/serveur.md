# Serveur du moteur V2

Mis à jour le 31/10/2026 à 01:00 · publication : **EN SERVICE (publie sur le site)**

## 🟢 **Tout va bien**

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-10-31 00:59:05  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-10-30 07:07:12  OK, 695 avis collectés, 172 couples recalculés, 55 republiés en 37.1 min |
| Passe DECP hebdomadaire | 2026-10-24 04:16:45  Passe hebdomadaire DECP 2026-10-24_decp : terminée en 76.7 min, mémoire max 3721 Mo ; 160 couples recalculés, 2 bloqués par la garde (M22_05, M22_07) ; 153 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-10-30 07:12:10  Contrôle du 30/10 : vert — 172 couples identiques au site, 10 attributions anciennes gardées par le site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 0.54 Go sur 7.6 · charge 0.03 · disque 28.0 % · échange 0.0 Go

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 30/10 07:07 | 695 | 172 | 55 | 0 | 37.1 min |
| 29/10 07:07 | 704 | 172 | 51 | 1 | 37.9 min |
| 28/10 07:09 | 640 | 166 | 62 | 0 | 39.0 min |
| 27/10 07:08 | 351 | 161 | 63 | 0 | 38.3 min |
| 26/10 07:05 | 533 | 163 | 49 | 0 | 35.1 min |
| 25/10 07:03 | 138 | 160 | 15 | 0 | 33.7 min |
| 24/10 15:18 | 3 | 155 | 78 | 0 | 38.2 min |
| 24/10 07:03 | 478 | 160 | 50 | 0 | 33.7 min |
| 23/10 06:58 | 672 | 143 | 41 | 0 | 28.0 min |
| 22/10 06:59 | 716 | 143 | 38 | 0 | 29.3 min |

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
2026-10-25 07:08  Contrôle du 25/10 : vert — 160 couples identiques au site ; tâches à l'heure, site à jour
2026-10-26 07:09  Contrôle du 26/10 : vert — 163 couples identiques au site ; tâches à l'heure, site à jour
2026-10-27 07:13  Contrôle du 27/10 : vert — 166 couples identiques au site, 10 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-10-28 07:14  Contrôle du 28/10 : vert — 166 couples identiques au site, 10 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-10-29 07:13  Contrôle du 29/10 : rouge — 171 couples identiques au site, 10 attributions anciennes gardées par le site ; EN ÉCART : C713_FR ; collecte du matin : 2026-10-29 07:07:57  1 ÉCHEC(S), 704 avis collectés, 172 couples recalculés, 51 republiés en 37.9 min
2026-10-30 07:12  Contrôle du 30/10 : vert — 172 couples identiques au site, 10 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                            LEFT LAST                             PASSED UNIT                     ACTIVATES
Sat 2026-10-31 03:00:00 CET 1h 59min Sat 2026-10-24 03:00:04 CEST 6 days ago tenderhit-hebdo.timer    tenderhit-hebdo.service
Sat 2026-10-31 06:30:00 CET 5h 29min Fri 2026-10-30 06:30:04 CET     18h ago tenderhit-collecte.timer tenderhit-collecte.service
-                                  - Sat 2026-10-31 01:00:04 CET      1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                  - Sat 2026-10-31 01:00:04 CET      1s ago tenderhit-relais.timer   tenderhit-relais.service

4 timers listed.
```

## Fin du journal du moteur
```
2026-10-30 10:40:29  C772_58 : demande en attente
2026-10-30 10:40:37    publié (édition 2026-10, 2 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 8 s
2026-10-30 10:40:37  C772_70 : demande en attente
2026-10-30 10:40:45    publié (édition 2026-10, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 7 s
2026-10-30 10:40:45  C772_89 : demande en attente
2026-10-30 10:40:54    publié (édition 2026-10, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 9 s
2026-10-30 10:40:54  C772_90 : demande en attente
2026-10-30 10:41:02    publié (édition 2026-10, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 8 s
2026-10-30 10:41:02  M01_21 : demande en attente
2026-10-30 10:41:10    publié (édition 2026-10, 24 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 8 s
2026-10-30 10:41:11  M01_25 : demande en attente
2026-10-30 10:41:18    publié (édition 2026-10, 3 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 8 s
2026-10-30 10:41:19  M01_39 : demande en attente
2026-10-30 10:41:32    publié (édition 2026-10, 8 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 13 s
2026-10-30 10:41:32  M01_58 : demande en attente
2026-10-30 10:41:45    publié (édition 2026-10, 1 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 13 s
2026-10-30 10:41:46  M01_70 : demande en attente
2026-10-30 10:41:58    publié (édition 2026-10, 2 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 13 s
2026-10-30 10:41:59  M01_89 : demande en attente
2026-10-30 10:42:06    publié (édition 2026-10, 7 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 8 s
2026-10-30 10:42:06  M01_90 : demande en attente
2026-10-30 10:42:20    publié (édition 2026-10, 2 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 13 s
2026-10-30 10:50:06  M22_01 : demande en attente
2026-10-30 10:50:13    publié (édition 2026-10, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 7 s
2026-10-30 10:50:13  M22_26 : demande en attente
2026-10-30 10:50:35    publié (édition 2026-10, 1 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 22 s
2026-10-30 10:50:35  M22_42 : demande en attente
2026-10-30 10:50:44    publié (édition 2026-10, 2 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 9 s
2026-10-30 10:50:44  M22_69 : demande en attente
2026-10-30 10:50:57    publié (édition 2026-10, 10 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 13 s
2026-10-30 10:50:58  M22_71 : demande en attente
2026-10-30 10:51:14    publié (édition 2026-10, 2 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 16 s
2026-10-30 12:25:06  C772_14 : demande en attente
2026-10-30 12:25:15    publié (édition 2026-10, 1 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 8 s
2026-10-30 12:25:15  C772_76 : demande en attente
2026-10-30 12:25:23    publié (édition 2026-10, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 8 s
2026-10-30 12:25:23  M22_14 : demande en attente
2026-10-30 12:25:38    publié (édition 2026-10, 2 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 15 s
2026-10-30 12:25:38  M22_38 : demande en attente
2026-10-30 12:25:47    publié (édition 2026-10, 6 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 9 s
```
