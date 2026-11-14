# Serveur du moteur V2

Mis à jour le 14/11/2026 à 05:00 · publication : **EN SERVICE (publie sur le site)**

## 🟢 **Tout va bien**

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-14 04:59:04  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-13 07:17:57  OK, 471 avis collectés, 260 couples recalculés, 60 republiés en 47.9 min |
| Passe DECP hebdomadaire | 2026-11-14 04:22:58  Passe hebdomadaire DECP 2026-11-14_decp : terminée en 82.9 min, mémoire max 4234 Mo ; 266 couples recalculés, 0 bloqués par la garde ; 260 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-13 07:21:04  Contrôle du 13/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 0.44 Go sur 7.6 · charge 0.00 · disque 36.6 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : +3.3 point(s) par semaine · 80 % dans **13.2 semaine(s)**

```
Mesure du 2026-11-14 04:22 :
  entrepot/sources                            3.53 Go
  entrepot/decp                               2.02 Go
  entrepot/boamp                              1.39 Go
  entrepot/passes                             1.19 Go
  production/controles                        0.68 Go
  entrepot/execution                          0.65 Go
  entrepot/marche                             0.26 Go
  entrepot/photographie                       0.23 Go
  production/publies                          0.21 Go
  entrepot/etiquettes                           37 Mo
  entrepot/referentiel                          16 Mo
  entrepot/avis                                  4 Mo
  entrepot/sirene                                2 Mo
  logs                                           2 Mo
  production/(fichiers)                          2 Mo
  entrepot/tmp                                   2 Mo
  entrepot/mesures.jsonl                         1 Mo
  production/rejeu                               0 Mo
  entrepot/sources_temoin.jsonl                  0 Mo
  entrepot/manifeste.json                        0 Mo
Croissance par dossier (depuis 2026-11-07, 7.0 j), en Go par semaine :
  entrepot/decp                                 +0.43
  entrepot/passes                               +0.30
  entrepot/sources                              +0.03
  entrepot/boamp                                +0.01
Dernière purge (2026-11-14 04:22) : faite, 5 élément(s), 0.93 Go libérés · decp_telechargees 1 (0.26 Go) · fusions 1 (0.0 Go) · photographies_controle 3 (0.68 Go)
```

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 13/11 07:17 | 471 | 260 | 60 | 0 | 47.9 min |
| 12/11 07:16 | 433 | 249 | 38 | 0 | 46.8 min |
| 11/11 07:18 | 647 | 249 | 176 | 0 | 48.8 min |
| 10/11 07:18 | 343 | 241 | 89 | 0 | 48.4 min |
| 09/11 07:16 | 305 | 236 | 59 | 0 | 46.0 min |
| 08/11 07:16 | 673 | 233 | 90 | 0 | 46.0 min |
| 07/11 07:15 | 519 | 233 | 72 | 0 | 45.7 min |
| 06/11 07:14 | 770 | 224 | 63 | 0 | 44.3 min |
| 05/11 07:12 | 770 | 223 | 65 | 0 | 42.3 min |
| 04/11 07:11 | 599 | 220 | 66 | 0 | 41.9 min |

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
2026-11-03 07:12  Contrôle du 03/11 : vert — 219 couples identiques au site, 349 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-11-04 07:15  Contrôle du 04/11 : vert — 220 couples identiques au site, 349 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-11-05 07:15  Contrôle du 05/11 : rouge — photographie du site impossible ou incomplète
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
```

## Tâches planifiées
```
NEXT                            LEFT LAST                        PASSED UNIT                     ACTIVATES
Sat 2026-11-14 05:45:00 CET    44min Fri 2026-11-13 05:45:04 CET      - tenderhit-purge.timer    tenderhit-purge.service
Sat 2026-11-14 06:30:00 CET 1h 29min Fri 2026-11-13 06:30:04 CET      - tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-11-21 03:00:00 CET   6 days Sat 2026-11-14 03:00:04 CET      - tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                  - Sat 2026-11-14 05:00:02 CET 2s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                  - Sat 2026-11-14 05:00:02 CET 2s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-13 07:08:13    M29_42 : 0 opportunités · inchangé · 15 s
2026-11-13 07:08:27    M29_43 : 0 opportunités · inchangé · 14 s
2026-11-13 07:08:41    M29_63 : 0 opportunités · inchangé · 14 s
2026-11-13 07:08:49    M29_69 : 0 opportunités · rapport et opportunités · 7 s
2026-11-13 07:09:04    M29_73 : 0 opportunités · inchangé · 15 s
2026-11-13 07:09:19    M29_74 : 0 opportunités · inchangé · 16 s
2026-11-13 07:09:32    M29_83 : 1 opportunités · inchangé · 12 s
2026-11-13 07:09:51    M29_93 : 1 opportunités · inchangé · 19 s
2026-11-13 07:10:00    M30_69 : 13 opportunités · rapport et opportunités · 10 s
2026-11-13 07:10:03    M33_01 : 5 opportunités · inchangé · 3 s
2026-11-13 07:10:10    M33_14 : 8 opportunités · inchangé · 7 s
2026-11-13 07:10:16    M33_27 : 7 opportunités · inchangé · 6 s
2026-11-13 07:10:24    M33_38 : 6 opportunités · rapport et opportunités · 8 s
2026-11-13 07:10:30    M33_42 : 1 opportunités · inchangé · 6 s
2026-11-13 07:10:36    M33_50 : 3 opportunités · inchangé · 6 s
2026-11-13 07:10:41    M33_61 : 2 opportunités · inchangé · 6 s
2026-11-13 07:10:52    M33_69 : 14 opportunités · rapport et opportunités · 10 s
2026-11-13 07:10:58    M33_71 : 9 opportunités · inchangé · 6 s
2026-11-13 07:11:05    M33_76 : 14 opportunités · inchangé · 8 s
2026-11-13 07:11:12    M33_85 : 3 opportunités · inchangé · 7 s
2026-11-13 07:15:26    M33_FR : 532 opportunités · rapport et opportunités · 254 s
2026-11-13 07:15:36    M40_05 : 0 opportunités · inchangé · 9 s
2026-11-13 07:15:42    M40_76 : 1 opportunités · inchangé · 6 s
2026-11-13 07:15:51    P1005_14 : 1 opportunités · inchangé · 9 s
2026-11-13 07:15:59    P1005_22 : 6 opportunités · inchangé · 8 s
2026-11-13 07:16:07    P1005_27 : 1 opportunités · inchangé · 8 s
2026-11-13 07:16:17    P1005_29 : 12 opportunités · rapport et opportunités · 10 s
2026-11-13 07:16:28    P1005_35 : 20 opportunités · inchangé · 10 s
2026-11-13 07:16:37    P1005_56 : 11 opportunités · rapport et opportunités · 10 s
2026-11-13 07:16:52    P1005_59 : 19 opportunités · inchangé · 15 s
2026-11-13 07:17:01    P1005_60 : 3 opportunités · inchangé · 9 s
2026-11-13 07:17:25    P1005_75 : 37 opportunités · rapport et opportunités · 24 s
2026-11-13 07:17:36    P1005_76 : 7 opportunités · inchangé · 11 s
2026-11-13 07:17:45    P1005_80 : 0 opportunités · inchangé · 8 s
2026-11-13 07:17:57    P1005_93 : 11 opportunités · inchangé · 12 s
2026-11-13 07:17:57  OK, 471 avis collectés, 260 couples recalculés, 60 republiés en 47.9 min
2026-11-13 07:21:04  Contrôle du 13/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour
2026-11-14 03:12:58  tables du marché : 279 activité(s) envoyée(s), 27 inchangée(s), 1006913 lignes en 493 paquets ; erreurs : C712, C713, C714, C715, C717, C718, C719, C720, C721, C722, C723, C724, C725, C726, C727, C728, C731, C732, C740, C741, C742
2026-11-14 04:22:58  Passe hebdomadaire DECP 2026-11-14_decp : terminée en 82.9 min, mémoire max 4234 Mo ; 266 couples recalculés, 0 bloqués par la garde ; 260 couples publiés, tables d'aide publiées
2026-11-14 04:22:58  purge du disque faite : 5 élément(s), 0.93 Go libérés — decp_telechargees 1 (0.26 Go), fusions 1 (0.0 Go), photographies_controle 3 (0.68 Go)
```
