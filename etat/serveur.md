# Serveur du moteur V2

Mis à jour le 08/11/2026 à 00:00 · publication : **EN SERVICE (publie sur le site)**

## 🟢 **Tout va bien**

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-07 23:59:06  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-07 07:15:42  OK, 519 avis collectés, 233 couples recalculés, 72 republiés en 45.6 min |
| Passe DECP hebdomadaire | 2026-11-07 04:22:15  Passe hebdomadaire DECP 2026-11-07_decp : terminée avec échecs en 82.2 min, mémoire max 4269 Mo ; 236 couples recalculés, 0 bloqués par la garde, échecs : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; 222 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-07 07:18:17  Contrôle du 07/11 : rouge — 223 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 0.57 Go sur 7.6 · charge 0.00 · disque 36.9 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : +5.2 point(s) par semaine · 80 % dans **8.3 semaine(s)**

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
| 07/11 07:15 | 519 | 233 | 72 | 0 | 45.7 min |
| 06/11 07:14 | 770 | 224 | 63 | 0 | 44.3 min |
| 05/11 07:12 | 770 | 223 | 65 | 0 | 42.3 min |
| 04/11 07:11 | 599 | 220 | 66 | 0 | 41.9 min |
| 03/11 07:09 | 315 | 219 | 79 | 0 | 39.6 min |
| 02/11 07:10 | 251 | 219 | 42 | 0 | 40.9 min |
| 01/11 07:13 | 543 | 219 | 219 | 0 | 43.6 min |
| 31/10 07:17 | 410 | 213 | 44 | 0 | 47.0 min |
| 30/10 07:07 | 695 | 172 | 55 | 0 | 37.1 min |
| 29/10 07:07 | 704 | 172 | 51 | 1 | 37.9 min |

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
2026-11-07 07:18  Contrôle du 07/11 : rouge — 223 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                            LEFT LAST                         PASSED UNIT                     ACTIVATES
Sun 2026-11-08 05:45:00 CET 5h 44min Sat 2026-11-07 05:45:04 CET 18h ago tenderhit-purge.timer    tenderhit-purge.service
Sun 2026-11-08 06:30:00 CET       6h Sat 2026-11-07 06:30:04 CET 17h ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-11-14 03:00:00 CET   6 days Sat 2026-11-07 03:00:00 CET 21h ago tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                  - Sun 2026-11-08 00:00:04 CET  1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                  - Sun 2026-11-08 00:00:04 CET  1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-07 07:02:45    M22_91 : 3 opportunités · inchangé · 6 s
2026-11-07 07:02:51    M22_92 : 6 opportunités · inchangé · 6 s
2026-11-07 07:02:58    M22_93 : 3 opportunités · inchangé · 7 s
2026-11-07 07:03:04    M22_94 : 8 opportunités · inchangé · 6 s
2026-11-07 07:03:26    M22_95 : 6 opportunités · rapport et opportunités · 22 s
2026-11-07 07:06:42    M22_FR : 183 opportunités · rapport et opportunités · 196 s
2026-11-07 07:06:48    M23_27 : 5 opportunités · inchangé · 6 s
2026-11-07 07:06:56    M23_44 : 7 opportunités · inchangé · 8 s
2026-11-07 07:07:04    M23_76 : 8 opportunités · inchangé · 8 s
2026-11-07 07:07:13    M24_69 : 8 opportunités · inchangé · 9 s
2026-11-07 07:07:20    M24_76 : 10 opportunités · inchangé · 7 s
2026-11-07 07:07:29    M30_69 : 13 opportunités · inchangé · 9 s
2026-11-07 07:07:32    M33_01 : 3 opportunités · inchangé · 3 s
2026-11-07 07:07:39    M33_14 : 8 opportunités · rapport et opportunités · 8 s
2026-11-07 07:07:46    M33_27 : 5 opportunités · rapport et opportunités · 7 s
2026-11-07 07:07:54    M33_38 : 10 opportunités · rapport et opportunités · 8 s
2026-11-07 07:08:00    M33_42 : 1 opportunités · inchangé · 6 s
2026-11-07 07:08:06    M33_50 : 4 opportunités · inchangé · 6 s
2026-11-07 07:08:12    M33_61 : 2 opportunités · inchangé · 5 s
2026-11-07 07:08:22    M33_69 : 16 opportunités · inchangé · 10 s
2026-11-07 07:08:28    M33_71 : 9 opportunités · inchangé · 6 s
2026-11-07 07:08:37    M33_76 : 15 opportunités · rapport et opportunités · 9 s
2026-11-07 07:08:43    M33_85 : 4 opportunités · inchangé · 7 s
2026-11-07 07:13:09    M33_FR : 597 opportunités · rapport et opportunités · 265 s
2026-11-07 07:13:19    M40_05 : 0 opportunités · rapport et opportunités · 11 s
2026-11-07 07:13:25    M40_76 : 2 opportunités · inchangé · 6 s
2026-11-07 07:13:34    P1005_14 : 0 opportunités · inchangé · 9 s
2026-11-07 07:13:43    P1005_22 : 8 opportunités · inchangé · 9 s
2026-11-07 07:13:51    P1005_27 : 4 opportunités · inchangé · 8 s
2026-11-07 07:14:01    P1005_29 : 14 opportunités · rapport et opportunités · 10 s
2026-11-07 07:14:12    P1005_35 : 17 opportunités · rapport et opportunités · 12 s
2026-11-07 07:14:22    P1005_56 : 12 opportunités · rapport et opportunités · 10 s
2026-11-07 07:14:37    P1005_59 : 20 opportunités · inchangé · 15 s
2026-11-07 07:14:46    P1005_60 : 3 opportunités · inchangé · 9 s
2026-11-07 07:15:10    P1005_75 : 43 opportunités · rapport et opportunités · 24 s
2026-11-07 07:15:22    P1005_76 : 8 opportunités · rapport et opportunités · 3 identifiants DECP raccourcis · 12 s
2026-11-07 07:15:30    P1005_80 : 0 opportunités · inchangé · 8 s
2026-11-07 07:15:42    P1005_93 : 13 opportunités · inchangé · 12 s
2026-11-07 07:15:42  OK, 519 avis collectés, 233 couples recalculés, 72 republiés en 45.6 min
2026-11-07 07:18:17  Contrôle du 07/11 : rouge — 223 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour
```
