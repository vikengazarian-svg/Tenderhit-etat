# Serveur du moteur V2

Mis à jour le 16/11/2026 à 07:00 · publication : **EN SERVICE (publie sur le site)**

## 🔴 **À regarder** : demandes des clients non traitées depuis plus de 15 min

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-16 06:29:03  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-15 07:19:05  OK, 430 avis collectés, 266 couples recalculés, 59 republiés en 49.1 min |
| Passe DECP hebdomadaire | 2026-11-14 04:22:58  Passe hebdomadaire DECP 2026-11-14_decp : terminée en 82.9 min, mémoire max 4234 Mo ; 266 couples recalculés, 0 bloqués par la garde ; 260 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-15 07:23:10  Contrôle du 15/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 1.86 Go sur 7.6 · charge 1.51 · disque 36.6 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : +2.6 point(s) par semaine · 80 % dans **16.4 semaine(s)**

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
| 15/11 07:19 | 430 | 266 | 59 | 0 | 49.1 min |
| 14/11 07:27 | 335 | 266 | 49 | 0 | 48.7 min |
| 13/11 07:17 | 471 | 260 | 60 | 0 | 47.9 min |
| 12/11 07:16 | 433 | 249 | 38 | 0 | 46.8 min |
| 11/11 07:18 | 647 | 249 | 176 | 0 | 48.8 min |
| 10/11 07:18 | 343 | 241 | 89 | 0 | 48.4 min |
| 09/11 07:16 | 305 | 236 | 59 | 0 | 46.0 min |
| 08/11 07:16 | 673 | 233 | 90 | 0 | 46.0 min |
| 07/11 07:15 | 519 | 233 | 72 | 0 | 45.7 min |
| 06/11 07:14 | 770 | 224 | 63 | 0 | 44.3 min |

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
2026-11-14 07:31  Contrôle du 14/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour
2026-11-15 07:23  Contrôle du 15/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                          LEFT LAST                              PASSED UNIT                     ACTIVATES
Mon 2026-11-16 07:01:00 CET    58s Mon 2026-11-16 07:00:00 CET       1s ago tenderhit-demandes.timer tenderhit-demandes.service
Tue 2026-11-17 05:45:00 CET    22h Mon 2026-11-16 05:45:00 CET 1h 15min ago tenderhit-purge.timer    tenderhit-purge.service
Sat 2026-11-21 03:00:00 CET 4 days Sat 2026-11-14 03:00:04 CET            - tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                - Mon 2026-11-16 06:30:00 CET    30min ago tenderhit-collecte.timer tenderhit-collecte.service
-                                - Mon 2026-11-16 07:00:00 CET       1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-16 06:52:52    M01_94 : 17 opportunités · inchangé · 7 s
2026-11-16 06:54:23    M01_FR : 1254 opportunités · rapport et opportunités · 91 s
2026-11-16 06:54:34    M02_59 : 7 opportunités · opportunités · 11 s
2026-11-16 06:54:44    M02_62 : 3 opportunités · opportunités · 10 s
2026-11-16 06:54:52    M03_76 : 7 opportunités · inchangé · 8 s
2026-11-16 06:55:01    M04_62 : 11 opportunités · opportunités · 9 s
2026-11-16 06:55:05    M04_76 : 5 opportunités · inchangé · 4 s
2026-11-16 06:55:12    M07_59 : 29 opportunités · inchangé · 6 s
2026-11-16 06:55:17    M07_76 : 8 opportunités · inchangé · 5 s
2026-11-16 06:55:21    M08_76 : 10 opportunités · inchangé · 4 s
2026-11-16 06:55:29    M08_81 : 0 opportunités · opportunités · 8 s
2026-11-16 06:55:31    M12_01 : 7 opportunités · inchangé · 2 s
2026-11-16 06:55:33    M12_03 : 4 opportunités · inchangé · 2 s
2026-11-16 06:55:43    M12_07 : 1 opportunités · inchangé · 10 s
2026-11-16 06:55:53    M12_15 : 0 opportunités · inchangé · 11 s
2026-11-16 06:55:57    M12_26 : 7 opportunités · inchangé · 4 s
2026-11-16 06:56:02    M12_38 : 11 opportunités · inchangé · 5 s
2026-11-16 06:56:06    M12_42 : 6 opportunités · inchangé · 4 s
2026-11-16 06:56:18    M12_43 : 2 opportunités · inchangé · 11 s
2026-11-16 06:56:22    M12_63 : 2 opportunités · inchangé · 4 s
2026-11-16 06:56:28    M12_69 : 23 opportunités · inchangé · 6 s
2026-11-16 06:56:32    M12_73 : 7 opportunités · inchangé · 4 s
2026-11-16 06:56:36    M12_74 : 9 opportunités · inchangé · 5 s
2026-11-16 06:56:41    M12_83 : 16 opportunités · inchangé · 5 s
2026-11-16 06:56:46    M12_93 : 24 opportunités · inchangé · 5 s
2026-11-16 06:56:49    M22_01 : 3 opportunités · inchangé · 2 s
2026-11-16 06:57:04    M22_07 : 1 opportunités · rapport et opportunités · 15 s
2026-11-16 06:57:16    M22_08 : 1 opportunités · rapport et opportunités · 12 s
2026-11-16 06:57:31    M22_10 : 0 opportunités · rapport et opportunités · 15 s
2026-11-16 06:57:45    M22_11 : 0 opportunités · opportunités · 15 s
2026-11-16 06:57:59    M22_14 : 2 opportunités · rapport et opportunités · 14 s
2026-11-16 06:58:14    M22_16 : 0 opportunités · rapport et opportunités · 15 s
2026-11-16 06:58:29    M22_17 : 1 opportunités · rapport et opportunités · 15 s
2026-11-16 06:58:41    M22_21 : 2 opportunités · inchangé · 12 s
2026-11-16 06:58:56    M22_24 : 0 opportunités · rapport et opportunités · 15 s
2026-11-16 06:59:14    M22_26 : 1 opportunités · rapport et opportunités · 18 s
2026-11-16 06:59:28    M22_27 : 1 opportunités · rapport et opportunités · 13 s
2026-11-16 06:59:39    M22_37 : 0 opportunités · inchangé · 12 s
2026-11-16 06:59:46    M22_38 : 7 opportunités · inchangé · 6 s
2026-11-16 06:59:52    M22_42 : 1 opportunités · inchangé · 6 s
```
