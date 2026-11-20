# Serveur du moteur V2

Mis à jour le 20/11/2026 à 07:00 · publication : **EN SERVICE (publie sur le site)**

## 🔴 **À regarder** : demandes des clients non traitées depuis plus de 15 min

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-20 06:29:03  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-19 07:28:59  OK, 545 avis collectés, 347 couples recalculés, 111 republiés en 59.0 min |
| Passe DECP hebdomadaire | 2026-11-14 04:22:58  Passe hebdomadaire DECP 2026-11-14_decp : terminée en 82.9 min, mémoire max 4234 Mo ; 266 couples recalculés, 0 bloqués par la garde ; 260 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-19 07:33:26  Contrôle du 19/11 : vert — 347 couples identiques au site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 2.82 Go sur 7.6 · charge 1.74 · disque 36.5 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : -1.4 point(s) par semaine · pas de hausse

```
Mesure du 2026-11-20 05:45 :
  entrepot/sources                            3.54 Go
  entrepot/decp                               2.02 Go
  entrepot/boamp                              1.39 Go
  entrepot/passes                             1.19 Go
  entrepot/execution                          0.70 Go
  production/controles                        0.70 Go
  entrepot/marche                             0.26 Go
  production/publies                          0.23 Go
  entrepot/photographie                       0.23 Go
  entrepot/etiquettes                           38 Mo
  entrepot/referentiel                          16 Mo
  entrepot/avis                                  3 Mo
  logs                                           3 Mo
  entrepot/sirene                                2 Mo
  production/(fichiers)                          2 Mo
  entrepot/tmp                                   2 Mo
  entrepot/mesures.jsonl                         1 Mo
  production/rejeu                               0 Mo
  entrepot/sources_temoin.jsonl                  0 Mo
  entrepot/manifeste.json                        0 Mo
Croissance par dossier (depuis 2026-11-12, 8.0 j), en Go par semaine :
  entrepot/decp                                 +0.37
  entrepot/passes                               +0.26
  entrepot/execution                            +0.06
  entrepot/sources                              +0.03
  production/publies                            +0.03
  entrepot/boamp                                +0.01
Dernière purge (2026-11-20 05:45) : faite, 2 élément(s), 0.23 Go libérés · fusions 1 (0.0 Go) · photographies_controle 1 (0.23 Go)
```

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 19/11 07:29 | 545 | 347 | 111 | 0 | 59.0 min |
| 18/11 07:23 | 362 | 310 | 87 | 0 | 53.6 min |
| 17/11 07:22 | 346 | 306 | 114 | 0 | 52.8 min |
| 16/11 07:19 | 306 | 270 | 61 | 0 | 49.6 min |
| 15/11 07:19 | 430 | 266 | 59 | 0 | 49.1 min |
| 14/11 07:27 | 335 | 266 | 49 | 0 | 48.7 min |
| 13/11 07:17 | 471 | 260 | 60 | 0 | 47.9 min |
| 12/11 07:16 | 433 | 249 | 38 | 0 | 46.8 min |
| 11/11 07:18 | 647 | 249 | 176 | 0 | 48.8 min |
| 10/11 07:18 | 343 | 241 | 89 | 0 | 48.4 min |

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
2026-11-17 07:26  Contrôle du 17/11 : vert — 318 couples identiques au site ; tâches à l'heure, site à jour
2026-11-18 07:27  Contrôle du 18/11 : vert — 319 couples identiques au site ; tâches à l'heure, site à jour
2026-11-19 07:33  Contrôle du 19/11 : vert — 347 couples identiques au site ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                        LEFT LAST                              PASSED UNIT                     ACTIVATES
Sat 2026-11-21 03:00:00 CET  19h Sat 2026-11-14 03:00:04 CET            - tenderhit-hebdo.timer    tenderhit-hebdo.service
Sat 2026-11-21 05:45:00 CET  22h Fri 2026-11-20 05:45:00 CET 1h 15min ago tenderhit-purge.timer    tenderhit-purge.service
-                              - Fri 2026-11-20 06:30:00 CET    30min ago tenderhit-collecte.timer tenderhit-collecte.service
-                              - Fri 2026-11-20 07:00:00 CET       1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                              - Fri 2026-11-20 07:00:00 CET       1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-20 06:54:44    C923_91 : 0 opportunités · inchangé · 4 s
2026-11-20 06:54:47    C923_92 : 1 opportunités · inchangé · 4 s
2026-11-20 06:54:51    C923_93 : 1 opportunités · inchangé · 4 s
2026-11-20 06:54:55    C923_94 : 0 opportunités · inchangé · 4 s
2026-11-20 06:54:58    C923_95 : 0 opportunités · inchangé · 3 s
2026-11-20 06:55:01    M01_01 : 5 opportunités · inchangé · 3 s
2026-11-20 06:55:14    M01_03 : 6 opportunités · inchangé · 13 s
2026-11-20 06:55:16    M01_04 : 4 opportunités · inchangé · 2 s
2026-11-20 06:55:29    M01_07 : 3 opportunités · inchangé · 13 s
2026-11-20 06:55:35    M01_14 : 23 opportunités · inchangé · 6 s
2026-11-20 06:55:50    M01_15 : 0 opportunités · inchangé · 15 s
2026-11-20 06:56:03    M01_16 : 6 opportunités · inchangé · 13 s
2026-11-20 06:56:08    M01_17 : 11 opportunités · inchangé · 5 s
2026-11-20 06:56:13    M01_21 : 24 opportunités · inchangé · 5 s
2026-11-20 06:56:26    M01_24 : 1 opportunités · inchangé · 13 s
2026-11-20 06:56:31    M01_25 : 3 opportunités · inchangé · 5 s
2026-11-20 06:56:36    M01_26 : 7 opportunités · inchangé · 5 s
2026-11-20 06:56:41    M01_27 : 4 opportunités · inchangé · 5 s
2026-11-20 06:56:48    M01_35 : 27 opportunités · inchangé · 6 s
2026-11-20 06:56:55    M01_38 : 16 opportunités · inchangé · 7 s
2026-11-20 06:57:06    M01_39 : 7 opportunités · rapport et opportunités · 12 s
2026-11-20 06:57:12    M01_42 : 13 opportunités · inchangé · 6 s
2026-11-20 06:57:27    M01_43 : 4 opportunités · inchangé · 15 s
2026-11-20 06:57:39    M01_58 : 5 opportunités · rapport et opportunités · 12 s
2026-11-20 06:57:48    M01_59 : 62 opportunités · inchangé · 9 s
2026-11-20 06:57:53    M01_63 : 9 opportunités · inchangé · 5 s
2026-11-20 06:58:03    M01_69 : 42 opportunités · inchangé · 9 s
2026-11-20 06:58:14    M01_70 : 2 opportunités · rapport et opportunités · 12 s
2026-11-20 06:58:20    M01_71 : 7 opportunités · inchangé · 5 s
2026-11-20 06:58:26    M01_73 : 27 opportunités · inchangé · 6 s
2026-11-20 06:58:32    M01_74 : 21 opportunités · inchangé · 6 s
2026-11-20 06:58:48    M01_75 : 69 opportunités · rapport et opportunités · 16 s
2026-11-20 06:58:55    M01_76 : 17 opportunités · inchangé · 7 s
2026-11-20 06:59:05    M01_77 : 26 opportunités · inchangé · 10 s
2026-11-20 06:59:13    M01_83 : 21 opportunités · inchangé · 8 s
2026-11-20 06:59:18    M01_89 : 5 opportunités · inchangé · 5 s
2026-11-20 06:59:31    M01_90 : 2 opportunités · rapport et opportunités · 14 s
2026-11-20 06:59:40    M01_92 : 20 opportunités · inchangé · 9 s
2026-11-20 06:59:49    M01_93 : 26 opportunités · inchangé · 8 s
2026-11-20 06:59:56    M01_94 : 17 opportunités · inchangé · 8 s
```
