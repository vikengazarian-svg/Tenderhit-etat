# Serveur du moteur V2

Mis à jour le 28/11/2026 à 07:00 · publication : **EN SERVICE (publie sur le site)**

## 🔴 **À regarder** : demandes des clients non traitées depuis plus de 15 min

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-28 06:29:03  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-27 07:54:15  OK, 749 avis collectés, 365 couples recalculés, 257 republiés en 84.2 min |
| Passe DECP hebdomadaire | 2026-11-28 05:03:36  Passe hebdomadaire DECP 2026-11-28_decp : terminée en 123.6 min, mémoire max 7513 Mo ; 365 couples recalculés, 1 bloqués par la garde (C712_59) ; 344 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-27 07:58:57  Contrôle du 27/11 : vert — 365 couples identiques au site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 1.33 Go sur 7.6 · charge 1.52 · disque 38.3 % · échange 0.13 Go

## Disque

Rythme des 14 derniers jours : +0.8 point(s) par semaine · 80 % dans **52.1 semaine(s)**

```
Mesure du 2026-11-28 05:45 :
  entrepot/sources                            3.57 Go
  entrepot/decp                               2.09 Go
  entrepot/boamp                              1.41 Go
  entrepot/passes                             1.25 Go
  entrepot/execution                          0.73 Go
  production/controles                        0.73 Go
  parallele                                   0.35 Go
  entrepot/marche                             0.26 Go
  production/publies                          0.25 Go
  entrepot/photographie                       0.23 Go
  entrepot/contrats                           0.19 Go
  entrepot/etiquettes                           38 Mo
  entrepot/referentiel                          16 Mo
  entrepot/avis                                  3 Mo
  production/(fichiers)                          3 Mo
  logs                                           3 Mo
  entrepot/sirene                                2 Mo
  entrepot/mesures.jsonl                         2 Mo
  production/rejeu                               0 Mo
  entrepot/sources_temoin.jsonl                  0 Mo
Croissance par dossier (depuis 2026-11-21, 7.0 j), en Go par semaine :
  parallele                                     +0.35
  entrepot/contrats                             +0.19
  entrepot/decp                                 +0.04
  entrepot/passes                               +0.03
  entrepot/execution                            +0.02
  production/controles                          +0.02
Dernière purge (2026-11-28 05:45) : faite, 0 élément(s), 0.0 Go libérés
```

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 27/11 07:54 | 749 | 365 | 257 | 0 | 84.2 min |
| 26/11 07:31 | 719 | 365 | 101 | 0 | 61.2 min |
| 25/11 07:30 | 584 | 363 | 113 | 0 | 60.4 min |
| 24/11 07:30 | 586 | 363 | 114 | 0 | 60.2 min |
| 23/11 07:28 | 254 | 355 | 30 | 0 | 58.0 min |
| 22/11 07:29 | 692 | 361 | 100 | 0 | 59.3 min |
| 21/11 07:30 | 878 | 360 | 151 | 0 | 60.1 min |
| 20/11 07:27 | 337 | 343 | 91 | 0 | 57.2 min |
| 19/11 07:29 | 545 | 347 | 111 | 0 | 59.0 min |
| 18/11 07:23 | 362 | 310 | 87 | 0 | 53.6 min |

### Passes DECP hebdomadaires

| Passe | Durée des couples | Mémoire max |
|---|---:|---:|
| 2026-11-28_decp | 83.1 min | 7513 Mo |
| 2026-11-21_decp | 59.9 min | 2890 Mo |
| 2026-11-14_decp | 50.5 min | 2828 Mo |
| 2026-11-07_decp | 55.7 min | 2686 Mo |
| 2026-10-31_decp | 53.2 min | 2538 Mo |
| 2026-10-24_decp | 33.0 min | 2373 Mo |

### Demandes des clients aujourd'hui

Aucune pour l'instant.

### Contrôles quotidiens (14 derniers)

```
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
2026-11-27 07:58  Contrôle du 27/11 : vert — 365 couples identiques au site ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                          LEFT LAST                              PASSED UNIT                     ACTIVATES
Sat 2026-11-28 07:01:00 CET    57s Sat 2026-11-28 07:00:00 CET       2s ago tenderhit-demandes.timer tenderhit-demandes.service
Sun 2026-11-29 05:45:00 CET    22h Sat 2026-11-28 05:45:01 CET 1h 15min ago tenderhit-purge.timer    tenderhit-purge.service
Sat 2026-12-05 03:00:00 CET 6 days Sat 2026-11-28 03:00:01 CET  4h 0min ago tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                - Sat 2026-11-28 06:30:01 CET    30min ago tenderhit-collecte.timer tenderhit-collecte.service
-                                - Sat 2026-11-28 07:00:00 CET       2s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-28 06:55:43    C741_56 : 0 opportunités · inchangé · 6 s
2026-11-28 06:55:50    C741_59 : 0 opportunités · inchangé · 6 s
2026-11-28 06:55:56    C741_60 : 0 opportunités · inchangé · 6 s
2026-11-28 06:56:03    C741_75 : 0 opportunités · inchangé · 7 s
2026-11-28 06:56:09    C741_76 : 0 opportunités · inchangé · 6 s
2026-11-28 06:56:15    C741_80 : 0 opportunités · inchangé · 6 s
2026-11-28 06:56:22    C741_93 : 0 opportunités · inchangé · 6 s
2026-11-28 06:56:26    C742_14 : 0 opportunités · inchangé · 4 s
2026-11-28 06:56:30    C742_22 : 0 opportunités · inchangé · 4 s
2026-11-28 06:56:35    C742_27 : 0 opportunités · inchangé · 4 s
2026-11-28 06:56:39    C742_29 : 0 opportunités · inchangé · 4 s
2026-11-28 06:56:44    C742_35 : 0 opportunités · inchangé · 5 s
2026-11-28 06:56:48    C742_56 : 0 opportunités · inchangé · 4 s
2026-11-28 06:56:57    C742_59 : 0 opportunités · inchangé · 9 s
2026-11-28 06:57:06    C742_60 : 0 opportunités · inchangé · 9 s
2026-11-28 06:57:12    C742_75 : 0 opportunités · inchangé · 6 s
2026-11-28 06:57:16    C742_76 : 0 opportunités · inchangé · 5 s
2026-11-28 06:57:25    C742_80 : 0 opportunités · inchangé · 8 s
2026-11-28 06:57:30    C742_93 : 0 opportunités · inchangé · 5 s
2026-11-28 06:57:36    C747_02 : 22 opportunités · inchangé · 7 s
2026-11-28 06:57:45    C747_59 : 22 opportunités · inchangé · 8 s
2026-11-28 06:57:52    C747_60 : 22 opportunités · inchangé · 8 s
2026-11-28 06:58:00    C747_62 : 22 opportunités · inchangé · 8 s
2026-11-28 06:58:08    C747_80 : 22 opportunités · inchangé · 7 s
2026-11-28 06:58:14    C772_01 : 2 opportunités · inchangé · 6 s
2026-11-28 06:58:20    C772_03 : 0 opportunités · inchangé · 6 s
2026-11-28 06:58:26    C772_07 : 2 opportunités · inchangé · 6 s
2026-11-28 06:58:31    C772_14 : 1 opportunités · inchangé · 6 s
2026-11-28 06:58:38    C772_15 : 0 opportunités · inchangé · 6 s
2026-11-28 06:58:46    C772_21 : 1 opportunités · inchangé · 9 s
2026-11-28 06:58:55    C772_25 : 2 opportunités · inchangé · 9 s
2026-11-28 06:59:02    C772_26 : 2 opportunités · inchangé · 7 s
2026-11-28 06:59:09    C772_38 : 5 opportunités · inchangé · 8 s
2026-11-28 06:59:17    C772_39 : 3 opportunités · inchangé · 8 s
2026-11-28 06:59:25    C772_42 : 4 opportunités · inchangé · 7 s
2026-11-28 06:59:31    C772_43 : 0 opportunités · inchangé · 6 s
2026-11-28 06:59:39    C772_58 : 1 opportunités · inchangé · 8 s
2026-11-28 06:59:46    C772_63 : 3 opportunités · inchangé · 7 s
2026-11-28 06:59:50    C772_69 : 2 opportunités · inchangé · 4 s
2026-11-28 06:59:58    C772_70 : 1 opportunités · inchangé · 8 s
```
