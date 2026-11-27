# Serveur du moteur V2

Mis à jour le 27/11/2026 à 07:00 · publication : **EN SERVICE (publie sur le site)**

## 🔴 **À regarder** : demandes des clients non traitées depuis plus de 15 min

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-27 06:29:03  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-26 07:31:13  OK, 719 avis collectés, 365 couples recalculés, 101 republiés en 61.2 min |
| Passe DECP hebdomadaire | 2026-11-21 04:33:49  Passe hebdomadaire DECP 2026-11-21_decp : terminée en 93.8 min, mémoire max 4287 Mo ; 360 couples recalculés, 1 bloqués par la garde (M01_58) ; 352 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-26 07:35:50  Contrôle du 26/11 : vert — 365 couples identiques au site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 1.33 Go sur 7.6 · charge 1.64 · disque 37.4 % · échange 0.08 Go

## Disque

Rythme des 14 derniers jours : +0.7 point(s) par semaine · 80 % dans **60.9 semaine(s)**

```
Mesure du 2026-11-27 05:45 :
  entrepot/sources                            3.57 Go
  entrepot/decp                               2.06 Go
  entrepot/boamp                              1.41 Go
  entrepot/passes                             1.23 Go
  production/controles                        0.72 Go
  entrepot/execution                          0.72 Go
  entrepot/marche                             0.26 Go
  production/publies                          0.24 Go
  entrepot/photographie                       0.23 Go
  entrepot/contrats                           0.19 Go
  entrepot/etiquettes                           38 Mo
  entrepot/referentiel                          16 Mo
  entrepot/avis                                  3 Mo
  entrepot/tmp                                   3 Mo
  production/(fichiers)                          3 Mo
  logs                                           3 Mo
  entrepot/sirene                                2 Mo
  entrepot/mesures.jsonl                         2 Mo
  production/rejeu                               0 Mo
  entrepot/sources_temoin.jsonl                  0 Mo
Croissance par dossier (depuis 2026-11-20, 7.0 j), en Go par semaine :
  entrepot/contrats                             +0.19
  entrepot/passes                               +0.04
  entrepot/decp                                 +0.03
  entrepot/sources                              +0.03
  entrepot/execution                            +0.02
  production/controles                          +0.02
Dernière purge (2026-11-27 05:45) : faite, 2 élément(s), 0.24 Go libérés · fusions 1 (0.0 Go) · photographies_controle 1 (0.24 Go)
```

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 26/11 07:31 | 719 | 365 | 101 | 0 | 61.2 min |
| 25/11 07:30 | 584 | 363 | 113 | 0 | 60.4 min |
| 24/11 07:30 | 586 | 363 | 114 | 0 | 60.2 min |
| 23/11 07:28 | 254 | 355 | 30 | 0 | 58.0 min |
| 22/11 07:29 | 692 | 361 | 100 | 0 | 59.3 min |
| 21/11 07:30 | 878 | 360 | 151 | 0 | 60.1 min |
| 20/11 07:27 | 337 | 343 | 91 | 0 | 57.2 min |
| 19/11 07:29 | 545 | 347 | 111 | 0 | 59.0 min |
| 18/11 07:23 | 362 | 310 | 87 | 0 | 53.6 min |
| 17/11 07:22 | 346 | 306 | 114 | 0 | 52.8 min |

### Passes DECP hebdomadaires

| Passe | Durée des couples | Mémoire max |
|---|---:|---:|
| 2026-11-21_decp | 59.9 min | 2890 Mo |
| 2026-11-14_decp | 50.5 min | 2828 Mo |
| 2026-11-07_decp | 55.7 min | 2686 Mo |
| 2026-10-31_decp | 53.2 min | 2538 Mo |
| 2026-10-24_decp | 33.0 min | 2373 Mo |
| 2026-10-17_decp | 41.8 min | — Mo |

### Demandes des clients aujourd'hui

Aucune pour l'instant.

### Contrôles quotidiens (14 derniers)

```
2026-11-13 07:21  Contrôle du 13/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour
2026-11-14 07:31  Contrôle du 14/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour
2026-11-15 07:23  Contrôle du 15/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour
2026-11-16 07:23  Contrôle du 16/11 : vert — 276 couples identiques au site ; tâches à l'heure, site à jour
2026-11-17 07:26  Contrôle du 17/11 : vert — 318 couples identiques au site ; tâches à l'heure, site à jour
2026-11-18 07:27  Contrôle du 18/11 : vert — 319 couples identiques au site ; tâches à l'heure, site à jour
2026-11-19 07:33  Contrôle du 19/11 : vert — 347 couples identiques au site ; tâches à l'heure, site à jour
2026-11-20 07:31  Contrôle du 20/11 : rouge — 347 couples identiques au site ; tâches à l'heure, site à jour ; CHUTES : C713_75 : opportunites 34 → 16
2026-11-21 07:34  Contrôle du 21/11 : vert — 360 couples identiques au site ; tâches à l'heure, site à jour
2026-11-22 07:33  Contrôle du 22/11 : vert — 361 couples identiques au site ; tâches à l'heure, site à jour
2026-11-23 07:32  Contrôle du 23/11 : vert — 361 couples identiques au site ; tâches à l'heure, site à jour
2026-11-24 07:34  Contrôle du 24/11 : vert — 363 couples identiques au site ; tâches à l'heure, site à jour
2026-11-25 07:34  Contrôle du 25/11 : vert — 363 couples identiques au site ; tâches à l'heure, site à jour
2026-11-26 07:35  Contrôle du 26/11 : vert — 365 couples identiques au site ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                        LEFT LAST                              PASSED UNIT                     ACTIVATES
Sat 2026-11-28 03:00:00 CET  19h Sat 2026-11-21 03:00:00 CET            - tenderhit-hebdo.timer    tenderhit-hebdo.service
Sat 2026-11-28 05:45:00 CET  22h Fri 2026-11-27 05:45:01 CET 1h 15min ago tenderhit-purge.timer    tenderhit-purge.service
-                              - Fri 2026-11-27 06:30:01 CET    30min ago tenderhit-collecte.timer tenderhit-collecte.service
-                              - Fri 2026-11-27 07:00:00 CET       1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                              - Fri 2026-11-27 07:00:00 CET       1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-27 06:55:44    C740_80 : 0 opportunités · inchangé · 5 s
2026-11-27 06:55:50    C740_83 : 0 opportunités · inchangé · 5 s
2026-11-27 06:55:55    C740_84 : 0 opportunités · inchangé · 5 s
2026-11-27 06:56:01    C740_93 : 0 opportunités · inchangé · 6 s
2026-11-27 06:56:07    C741_14 : 0 opportunités · inchangé · 6 s
2026-11-27 06:56:13    C741_22 : 0 opportunités · inchangé · 6 s
2026-11-27 06:56:19    C741_27 : 0 opportunités · inchangé · 6 s
2026-11-27 06:56:26    C741_29 : 0 opportunités · inchangé · 6 s
2026-11-27 06:56:32    C741_35 : 0 opportunités · inchangé · 6 s
2026-11-27 06:56:38    C741_56 : 0 opportunités · inchangé · 6 s
2026-11-27 06:56:45    C741_59 : 0 opportunités · inchangé · 7 s
2026-11-27 06:56:51    C741_60 : 0 opportunités · inchangé · 6 s
2026-11-27 06:56:58    C741_75 : 0 opportunités · inchangé · 7 s
2026-11-27 06:57:04    C741_76 : 0 opportunités · inchangé · 6 s
2026-11-27 06:57:10    C741_80 : 0 opportunités · inchangé · 6 s
2026-11-27 06:57:16    C741_93 : 0 opportunités · inchangé · 6 s
2026-11-27 06:57:21    C742_14 : 0 opportunités · inchangé · 4 s
2026-11-27 06:57:25    C742_22 : 0 opportunités · inchangé · 4 s
2026-11-27 06:57:29    C742_27 : 0 opportunités · inchangé · 4 s
2026-11-27 06:57:34    C742_29 : 0 opportunités · inchangé · 4 s
2026-11-27 06:57:38    C742_35 : 0 opportunités · inchangé · 5 s
2026-11-27 06:57:43    C742_56 : 0 opportunités · inchangé · 4 s
2026-11-27 06:57:52    C742_59 : 0 opportunités · inchangé · 9 s
2026-11-27 06:58:00    C742_60 : 0 opportunités · inchangé · 8 s
2026-11-27 06:58:06    C742_75 : 0 opportunités · inchangé · 5 s
2026-11-27 06:58:10    C742_76 : 0 opportunités · inchangé · 5 s
2026-11-27 06:58:19    C742_80 : 0 opportunités · inchangé · 8 s
2026-11-27 06:58:24    C742_93 : 0 opportunités · inchangé · 5 s
2026-11-27 06:58:31    C747_02 : 22 opportunités · opportunités · 7 s
2026-11-27 06:58:40    C747_59 : 22 opportunités · opportunités · 9 s
2026-11-27 06:58:48    C747_60 : 22 opportunités · opportunités · 8 s
2026-11-27 06:58:56    C747_62 : 22 opportunités · opportunités · 8 s
2026-11-27 06:59:04    C747_80 : 22 opportunités · opportunités · 8 s
2026-11-27 06:59:10    C772_01 : 2 opportunités · opportunités · 6 s
2026-11-27 06:59:16    C772_03 : 0 opportunités · inchangé · 6 s
2026-11-27 06:59:22    C772_07 : 2 opportunités · opportunités · 6 s
2026-11-27 06:59:29    C772_14 : 1 opportunités · opportunités · 6 s
2026-11-27 06:59:35    C772_15 : 0 opportunités · inchangé · 6 s
2026-11-27 06:59:44    C772_21 : 1 opportunités · opportunités · 9 s
2026-11-27 06:59:53    C772_25 : 2 opportunités · opportunités · 9 s
```
