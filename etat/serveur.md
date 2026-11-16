# Serveur du moteur V2

Mis à jour le 16/11/2026 à 10:00 · publication : **EN SERVICE (publie sur le site)**

## 🟢 **Tout va bien**

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-16 09:59:03  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-16 07:19:37  OK, 306 avis collectés, 270 couples recalculés, 61 republiés en 49.6 min |
| Passe DECP hebdomadaire | 2026-11-14 04:22:58  Passe hebdomadaire DECP 2026-11-14_decp : terminée en 82.9 min, mémoire max 4234 Mo ; 266 couples recalculés, 0 bloqués par la garde ; 260 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-16 07:23:43  Contrôle du 16/11 : vert — 276 couples identiques au site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 0.48 Go sur 7.6 · charge 0.00 · disque 37.1 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : +2.7 point(s) par semaine · 80 % dans **15.9 semaine(s)**

```
Mesure du 2026-11-16 05:45 :
  entrepot/sources                            3.53 Go
  entrepot/decp                               2.02 Go
  entrepot/boamp                              1.39 Go
  entrepot/passes                             1.19 Go
  production/controles                        0.69 Go
  entrepot/execution                          0.65 Go
  entrepot/marche                             0.26 Go
  entrepot/photographie                       0.23 Go
  production/publies                          0.21 Go
  entrepot/etiquettes                           37 Mo
  entrepot/referentiel                          16 Mo
  entrepot/avis                                  3 Mo
  logs                                           3 Mo
  entrepot/sirene                                2 Mo
  production/(fichiers)                          2 Mo
  entrepot/mesures.jsonl                         1 Mo
  production/rejeu                               0 Mo
  entrepot/sources_temoin.jsonl                  0 Mo
  entrepot/manifeste.json                        0 Mo
  entrepot/tmp                                   0 Mo
Croissance par dossier (depuis 2026-11-08, 8.0 j), en Go par semaine :
  entrepot/decp                                 +0.37
  entrepot/passes                               +0.26
  entrepot/sources                              +0.03
  entrepot/boamp                                +0.01
Dernière purge (2026-11-16 05:45) : faite, 4 élément(s), 0.23 Go libérés · fusions 1 (0.0 Go) · photographies_controle 1 (0.22 Go) · tmp 2 (0.0 Go)
```

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 16/11 07:19 | 306 | 270 | 61 | 0 | 49.6 min |
| 15/11 07:19 | 430 | 266 | 59 | 0 | 49.1 min |
| 14/11 07:27 | 335 | 266 | 49 | 0 | 48.7 min |
| 13/11 07:17 | 471 | 260 | 60 | 0 | 47.9 min |
| 12/11 07:16 | 433 | 249 | 38 | 0 | 46.8 min |
| 11/11 07:18 | 647 | 249 | 176 | 0 | 48.8 min |
| 10/11 07:18 | 343 | 241 | 89 | 0 | 48.4 min |
| 09/11 07:16 | 305 | 236 | 59 | 0 | 46.0 min |
| 08/11 07:16 | 673 | 233 | 90 | 0 | 46.0 min |
| 07/11 07:15 | 519 | 233 | 72 | 0 | 45.7 min |

### Passes DECP hebdomadaires

| Passe | Durée des couples | Mémoire max |
|---|---:|---:|
| 2026-11-14_decp | 50.5 min | 2828 Mo |
| 2026-11-07_decp | 55.7 min | 2686 Mo |
| 2026-10-31_decp | 53.2 min | 2538 Mo |
| 2026-10-24_decp | 33.0 min | 2373 Mo |
| 2026-10-17_decp | 41.8 min | — Mo |
| essai_pc | 26.3 min | 1616 Mo |

### Demandes des clients aujourd'hui

Aucune pour l'instant.

### Contrôles quotidiens (14 derniers)

```
2026-11-05 11:03  Contrôle du 05/11 : rouge — photographie du site impossible ou incomplète
2026-11-06 07:17  Contrôle du 06/11 : rouge — 222 couples identiques au site, 349 attributions anciennes gardées par le site ; EN ÉCART : C713_75, M08_81 ; tâches à l'heure, site à jour
2026-11-07 07:18  Contrôle du 07/11 : rouge — 223 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour
2026-11-08 07:18  Contrôle du 08/11 : rouge — 223 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour
2026-11-09 07:18  Contrôle du 09/11 : rouge — 222 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour
2026-11-10 07:21  Contrôle du 10/11 : rouge — 235 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour
2026-11-10 11:59  Contrôle du 10/11 : rouge — 235 couples identiques au site, 4238 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour ; CHUTES : C451_21 : attributions 585 → 270, C451_42 : attributions 1131 → 535
2026-11-10 13:50  Contrôle du 10/11 : vert — 249 couples identiques au site ; tâches à l'heure, site à jour
2026-11-11 07:22  Contrôle du 11/11 : rouge — 249 couples identiques au site ; tâches à l'heure, site à jour ; CHUTES : C451_69 : opportunites 18 → 8, C451_FR : opportunites 564 → 181, M07_76 : opportunites 19 → 8
2026-11-12 07:20  Contrôle du 12/11 : vert — 249 couples identiques au site ; tâches à l'heure, site à jour
2026-11-13 07:21  Contrôle du 13/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour
2026-11-14 07:31  Contrôle du 14/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour
2026-11-15 07:23  Contrôle du 15/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour
2026-11-16 07:23  Contrôle du 16/11 : vert — 276 couples identiques au site ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                          LEFT LAST                              PASSED UNIT                     ACTIVATES
Tue 2026-11-17 05:45:00 CET    19h Mon 2026-11-16 05:45:00 CET 4h 15min ago tenderhit-purge.timer    tenderhit-purge.service
Tue 2026-11-17 06:30:00 CET    20h Mon 2026-11-16 06:30:00 CET 3h 30min ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-11-21 03:00:00 CET 4 days Sat 2026-11-14 03:00:04 CET            - tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                - Mon 2026-11-16 10:00:00 CET       1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                - Mon 2026-11-16 10:00:00 CET       1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-16 07:09:21    M29_15 : 0 opportunités · inchangé · 14 s
2026-11-16 07:09:35    M29_26 : 0 opportunités · inchangé · 15 s
2026-11-16 07:09:51    M29_38 : 0 opportunités · inchangé · 15 s
2026-11-16 07:10:05    M29_42 : 0 opportunités · inchangé · 15 s
2026-11-16 07:10:19    M29_43 : 0 opportunités · inchangé · 14 s
2026-11-16 07:10:34    M29_63 : 0 opportunités · inchangé · 14 s
2026-11-16 07:10:40    M29_69 : 0 opportunités · inchangé · 6 s
2026-11-16 07:10:55    M29_73 : 0 opportunités · inchangé · 15 s
2026-11-16 07:11:11    M29_74 : 0 opportunités · inchangé · 16 s
2026-11-16 07:11:23    M29_83 : 1 opportunités · inchangé · 12 s
2026-11-16 07:11:43    M29_93 : 1 opportunités · rapport et opportunités · 20 s
2026-11-16 07:11:52    M30_69 : 13 opportunités · inchangé · 9 s
2026-11-16 07:11:55    M33_01 : 6 opportunités · inchangé · 3 s
2026-11-16 07:12:03    M33_14 : 7 opportunités · rapport et opportunités · 8 s
2026-11-16 07:12:09    M33_27 : 7 opportunités · inchangé · 6 s
2026-11-16 07:12:16    M33_38 : 6 opportunités · inchangé · 7 s
2026-11-16 07:12:22    M33_42 : 0 opportunités · inchangé · 6 s
2026-11-16 07:12:29    M33_50 : 4 opportunités · rapport et opportunités · 7 s
2026-11-16 07:12:34    M33_61 : 3 opportunités · inchangé · 5 s
2026-11-16 07:12:44    M33_69 : 14 opportunités · inchangé · 9 s
2026-11-16 07:12:50    M33_71 : 8 opportunités · inchangé · 6 s
2026-11-16 07:12:57    M33_76 : 9 opportunités · inchangé · 7 s
2026-11-16 07:13:04    M33_85 : 3 opportunités · inchangé · 7 s
2026-11-16 07:17:13    M33_FR : 524 opportunités · rapport et opportunités · 249 s
2026-11-16 07:17:19    M40_76 : 0 opportunités · inchangé · 6 s
2026-11-16 07:17:29    P1005_14 : 2 opportunités · rapport et opportunités · 10 s
2026-11-16 07:17:37    P1005_22 : 8 opportunités · inchangé · 9 s
2026-11-16 07:17:46    P1005_27 : 2 opportunités · rapport et opportunités · 9 s
2026-11-16 07:17:56    P1005_29 : 10 opportunités · rapport et opportunités · 10 s
2026-11-16 07:18:08    P1005_35 : 19 opportunités · rapport et opportunités · 12 s
2026-11-16 07:18:17    P1005_56 : 12 opportunités · inchangé · 9 s
2026-11-16 07:18:33    P1005_59 : 20 opportunités · rapport et opportunités · 16 s
2026-11-16 07:18:42    P1005_60 : 2 opportunités · inchangé · 9 s
2026-11-16 07:19:05    P1005_75 : 37 opportunités · inchangé · 23 s
2026-11-16 07:19:16    P1005_76 : 6 opportunités · inchangé · 11 s
2026-11-16 07:19:25    P1005_80 : 0 opportunités · inchangé · 9 s
2026-11-16 07:19:37    P1005_93 : 10 opportunités · inchangé · 12 s
2026-11-16 07:19:37  OK, 306 avis collectés, 270 couples recalculés, 61 republiés en 49.6 min
2026-11-16 07:23:43  Contrôle du 16/11 : vert — 276 couples identiques au site ; tâches à l'heure, site à jour
2026-11-16 09:16:50  Rejeu sur le serveur : vert — 4 couples identiques aux envois du matin sur 4 comparés ; 10.1 s par couple (médiane), 1 min au total
```
