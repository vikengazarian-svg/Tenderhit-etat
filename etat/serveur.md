# Serveur du moteur V2

Mis à jour le 27/11/2026 à 23:10 · publication : **EN SERVICE (publie sur le site)**

## 🟢 **Tout va bien**

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-27 23:10:03  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-27 07:54:15  OK, 749 avis collectés, 365 couples recalculés, 257 republiés en 84.2 min |
| Passe DECP hebdomadaire | 2026-11-21 04:33:49  Passe hebdomadaire DECP 2026-11-21_decp : terminée en 93.8 min, mémoire max 4287 Mo ; 360 couples recalculés, 1 bloqués par la garde (M01_58) ; 352 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-27 07:58:57  Contrôle du 27/11 : vert — 365 couples identiques au site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 0.64 Go sur 7.6 · charge 0.52 · disque 39.4 % · échange 0.03 Go

## Disque

Rythme des 14 derniers jours : +1.4 point(s) par semaine · 80 % dans **28.0 semaine(s)**

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
NEXT                            LEFT LAST                         PASSED UNIT                     ACTIVATES
Fri 2026-11-27 23:11:00 CET      26s Fri 2026-11-27 23:10:01 CET 32s ago tenderhit-demandes.timer tenderhit-demandes.service
Sat 2026-11-28 03:00:00 CET 3h 49min Sat 2026-11-21 03:00:00 CET       - tenderhit-hebdo.timer    tenderhit-hebdo.service
Sat 2026-11-28 05:45:00 CET       6h Fri 2026-11-27 05:45:01 CET 17h ago tenderhit-purge.timer    tenderhit-purge.service
Sat 2026-11-28 06:30:00 CET       7h Fri 2026-11-27 06:30:01 CET 16h ago tenderhit-collecte.timer tenderhit-collecte.service
-                                  - Fri 2026-11-27 23:10:01 CET 32s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-27 07:39:10    M29_43 : 0 opportunités · rapport et opportunités · 18 s
2026-11-27 07:39:28    M29_63 : 0 opportunités · rapport et opportunités · 18 s
2026-11-27 07:39:35    M29_69 : 0 opportunités · inchangé · 7 s
2026-11-27 07:39:54    M29_73 : 0 opportunités · rapport et opportunités · 19 s
2026-11-27 07:40:13    M29_74 : 0 opportunités · rapport et opportunités · 20 s
2026-11-27 07:40:30    M29_83 : 1 opportunités · inchangé · 17 s
2026-11-27 07:40:54    M29_93 : 2 opportunités · rapport et opportunités · 24 s
2026-11-27 07:41:03    M30_13 : 7 opportunités · opportunités · 9 s
2026-11-27 07:41:15    M30_69 : 7 opportunités · rapport et opportunités · 12 s
2026-11-27 07:41:21    M33_01 : 8 opportunités · rapport et opportunités · 6 s
2026-11-27 07:41:29    M33_14 : 7 opportunités · rapport et opportunités · 8 s
2026-11-27 07:41:37    M33_27 : 5 opportunités · opportunités · 8 s
2026-11-27 07:41:48    M33_38 : 8 opportunités · rapport et opportunités · 11 s
2026-11-27 07:41:54    M33_42 : 0 opportunités · inchangé · 6 s
2026-11-27 07:42:03    M33_50 : 5 opportunités · rapport et opportunités · 9 s
2026-11-27 07:42:11    M33_61 : 3 opportunités · opportunités · 7 s
2026-11-27 07:42:25    M33_69 : 9 opportunités · opportunités · 14 s
2026-11-27 07:42:33    M33_71 : 5 opportunités · opportunités · 8 s
2026-11-27 07:42:45    M33_76 : 15 opportunités · rapport et opportunités · 11 s
2026-11-27 07:42:53    M33_85 : 4 opportunités · rapport et opportunités · 8 s
2026-11-27 07:50:25    M33_FR : 517 opportunités · rapport et opportunités · 452 s
2026-11-27 07:50:37    M37_13 : 12 opportunités · rapport et opportunités · 12 s
2026-11-27 07:50:55    M39_13 : 14 opportunités · rapport et opportunités · 17 s
2026-11-27 07:51:06    M40_05 : 0 opportunités · inchangé · 11 s
2026-11-27 07:51:13    M40_76 : 1 opportunités · rapport et opportunités · 8 s
2026-11-27 07:51:25    P1005_14 : 2 opportunités · opportunités · 12 s
2026-11-27 07:51:36    P1005_22 : 7 opportunités · opportunités · 11 s
2026-11-27 07:51:46    P1005_27 : 2 opportunités · opportunités · 10 s
2026-11-27 07:51:58    P1005_29 : 8 opportunités · opportunités · 12 s
2026-11-27 07:52:12    P1005_35 : 18 opportunités · opportunités · 15 s
2026-11-27 07:52:24    P1005_56 : 10 opportunités · rapport et opportunités · 12 s
2026-11-27 07:52:45    P1005_59 : 18 opportunités · opportunités · 20 s
2026-11-27 07:52:55    P1005_60 : 2 opportunités · opportunités · 10 s
2026-11-27 07:53:32    P1005_75 : 39 opportunités · rapport et opportunités · 37 s
2026-11-27 07:53:46    P1005_76 : 6 opportunités · opportunités · 3 identifiants DECP raccourcis · 14 s
2026-11-27 07:53:55    P1005_80 : 1 opportunités · opportunités · 9 s
2026-11-27 07:54:10    P1005_93 : 12 opportunités · opportunités · 15 s
2026-11-27 07:54:15    contrats des chaînes : 3071 envoyé(s), 0 retiré(s), 3113 cité(s) au total
2026-11-27 07:54:15  OK, 749 avis collectés, 365 couples recalculés, 257 republiés en 84.2 min
2026-11-27 07:58:57  Contrôle du 27/11 : vert — 365 couples identiques au site ; tâches à l'heure, site à jour
```
