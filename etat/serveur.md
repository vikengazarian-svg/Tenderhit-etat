# Serveur du moteur V2

Mis à jour le 14/11/2026 à 07:00 · publication : **EN SERVICE (publie sur le site)**

## 🔴 **À regarder** : demandes des clients non traitées depuis plus de 15 min

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-14 06:29:04  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-13 07:17:57  OK, 471 avis collectés, 260 couples recalculés, 60 republiés en 47.9 min |
| Passe DECP hebdomadaire | 2026-11-14 04:22:58  Passe hebdomadaire DECP 2026-11-14_decp : terminée en 82.9 min, mémoire max 4234 Mo ; 266 couples recalculés, 0 bloqués par la garde ; 260 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-13 07:21:04  Contrôle du 13/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 2.56 Go sur 7.6 · charge 1.76 · disque 36.7 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : +3.4 point(s) par semaine · 80 % dans **12.9 semaine(s)**

```
Mesure du 2026-11-14 05:45 :
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
Croissance par dossier (depuis 2026-11-07, 7.1 j), en Go par semaine :
  entrepot/decp                                 +0.42
  entrepot/passes                               +0.29
  entrepot/sources                              +0.03
  entrepot/boamp                                +0.01
Dernière purge (2026-11-14 05:45) : faite, 0 élément(s), 0.0 Go libérés
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
NEXT                          LEFT LAST                              PASSED UNIT                     ACTIVATES
Sun 2026-11-15 05:45:00 CET    22h Sat 2026-11-14 05:45:02 CET 1h 14min ago tenderhit-purge.timer    tenderhit-purge.service
Sun 2026-11-15 06:30:00 CET    23h Sat 2026-11-14 06:30:02 CET    29min ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-11-21 03:00:00 CET 6 days Sat 2026-11-14 03:00:04 CET            - tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                - Sat 2026-11-14 07:00:00 CET       1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                - Sat 2026-11-14 07:00:00 CET       1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-14 06:53:13    C772_70 : 0 opportunités · inchangé · 5 s
2026-11-14 06:53:18    C772_71 : 0 opportunités · inchangé · 5 s
2026-11-14 06:53:21    C772_73 : 1 opportunités · inchangé · 3 s
2026-11-14 06:53:24    C772_74 : 3 opportunités · inchangé · 3 s
2026-11-14 06:53:30    C772_76 : 0 opportunités · inchangé · 5 s
2026-11-14 06:53:33    C772_83 : 7 opportunités · inchangé · 4 s
2026-11-14 06:53:38    C772_89 : 0 opportunités · inchangé · 5 s
2026-11-14 06:53:43    C772_90 : 0 opportunités · inchangé · 5 s
2026-11-14 06:53:46    C772_93 : 3 opportunités · inchangé · 4 s
2026-11-14 06:55:43    C772_FR : 189 opportunités · rapport et opportunités · 117 s
2026-11-14 06:55:57    C794_FR : 96 opportunités · rapport et opportunités · 1 identifiant DECP raccourci · 14 s
2026-11-14 06:56:01    C805_34 : 0 opportunités · inchangé · 4 s
2026-11-14 06:56:04    M01_01 : 5 opportunités · inchangé · 3 s
2026-11-14 06:56:18    M01_03 : 6 opportunités · rapport et opportunités · 14 s
2026-11-14 06:56:21    M01_04 : 4 opportunités · inchangé · 3 s
2026-11-14 06:56:35    M01_07 : 3 opportunités · rapport et opportunités · 14 s
2026-11-14 06:56:40    M01_14 : 23 opportunités · inchangé · 6 s
2026-11-14 06:56:56    M01_15 : 0 opportunités · rapport et opportunités · 15 s
2026-11-14 06:57:09    M01_16 : 6 opportunités · inchangé · 13 s
2026-11-14 06:57:14    M01_17 : 5 opportunités · inchangé · 5 s
2026-11-14 06:57:19    M01_21 : 23 opportunités · inchangé · 5 s
2026-11-14 06:57:31    M01_24 : 1 opportunités · inchangé · 12 s
2026-11-14 06:57:36    M01_25 : 3 opportunités · inchangé · 5 s
2026-11-14 06:57:41    M01_26 : 7 opportunités · inchangé · 5 s
2026-11-14 06:57:47    M01_27 : 3 opportunités · inchangé · 5 s
2026-11-14 06:57:54    M01_38 : 16 opportunités · inchangé · 7 s
2026-11-14 06:58:04    M01_39 : 8 opportunités · inchangé · 11 s
2026-11-14 06:58:10    M01_42 : 12 opportunités · inchangé · 6 s
2026-11-14 06:58:26    M01_43 : 4 opportunités · rapport et opportunités · 16 s
2026-11-14 06:58:36    M01_58 : 5 opportunités · inchangé · 11 s
2026-11-14 06:58:45    M01_59 : 65 opportunités · inchangé · 9 s
2026-11-14 06:58:51    M01_63 : 9 opportunités · inchangé · 5 s
2026-11-14 06:59:00    M01_69 : 40 opportunités · rapport et opportunités · 10 s
2026-11-14 06:59:11    M01_70 : 2 opportunités · inchangé · 11 s
2026-11-14 06:59:16    M01_71 : 7 opportunités · inchangé · 5 s
2026-11-14 06:59:22    M01_73 : 26 opportunités · inchangé · 6 s
2026-11-14 06:59:28    M01_74 : 21 opportunités · inchangé · 6 s
2026-11-14 06:59:44    M01_75 : 72 opportunités · rapport et opportunités · 16 s
2026-11-14 06:59:51    M01_76 : 17 opportunités · inchangé · 7 s
2026-11-14 06:59:59    M01_83 : 21 opportunités · inchangé · 8 s
```
