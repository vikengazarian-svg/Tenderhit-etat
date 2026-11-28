# Serveur du moteur V2

Mis à jour le 28/11/2026 à 14:47 · publication : **EN SERVICE (publie sur le site)**

## 🟢 **Tout va bien**

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-28 14:47:03  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-28 07:52:05  OK, 449 avis collectés, 365 couples recalculés, 50 republiés en 82.1 min |
| Passe DECP hebdomadaire | 2026-11-28 05:03:36  Passe hebdomadaire DECP 2026-11-28_decp : terminée en 123.6 min, mémoire max 7513 Mo ; 365 couples recalculés, 1 bloqués par la garde (C712_59) ; 344 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-28 07:56:31  Contrôle du 28/11 : vert — 365 couples identiques au site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 0.46 Go sur 7.6 · charge 0.05 · disque 38.8 % · échange 0.03 Go

## Disque

Rythme des 14 derniers jours : +0.8 point(s) par semaine · 80 % dans **48.5 semaine(s)**

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
| 28/11 07:52 | 449 | 365 | 50 | 0 | 82.1 min |
| 27/11 07:54 | 749 | 365 | 257 | 0 | 84.2 min |
| 26/11 07:31 | 719 | 365 | 101 | 0 | 61.2 min |
| 25/11 07:30 | 584 | 363 | 113 | 0 | 60.4 min |
| 24/11 07:30 | 586 | 363 | 114 | 0 | 60.2 min |
| 23/11 07:28 | 254 | 355 | 30 | 0 | 58.0 min |
| 22/11 07:29 | 692 | 361 | 100 | 0 | 59.3 min |
| 21/11 07:30 | 878 | 360 | 151 | 0 | 60.1 min |
| 20/11 07:27 | 337 | 343 | 91 | 0 | 57.2 min |
| 19/11 07:29 | 545 | 347 | 111 | 0 | 59.0 min |

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
2026-11-28 07:56  Contrôle du 28/11 : vert — 365 couples identiques au site ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                          LEFT LAST                              PASSED UNIT                     ACTIVATES
Sat 2026-11-28 14:48:00 CET    13s Sat 2026-11-28 14:47:00 CET      46s ago tenderhit-demandes.timer tenderhit-demandes.service
Sun 2026-11-29 05:45:00 CET    14h Sat 2026-11-28 05:45:01 CET       9h ago tenderhit-purge.timer    tenderhit-purge.service
Sun 2026-11-29 06:30:00 CET    15h Sat 2026-11-28 06:30:01 CET       8h ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-12-05 03:00:00 CET 6 days Sat 2026-11-28 03:00:01 CET      11h ago tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                - Sat 2026-11-28 14:44:01 CET 3min 45s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-28 07:37:15    M29_63 : 0 opportunités · inchangé · 17 s
2026-11-28 07:37:22    M29_69 : 0 opportunités · inchangé · 7 s
2026-11-28 07:37:40    M29_73 : 0 opportunités · inchangé · 18 s
2026-11-28 07:37:58    M29_74 : 0 opportunités · inchangé · 18 s
2026-11-28 07:38:16    M29_83 : 1 opportunités · inchangé · 17 s
2026-11-28 07:38:39    M29_93 : 2 opportunités · rapport et opportunités · 23 s
2026-11-28 07:38:48    M30_13 : 7 opportunités · inchangé · 9 s
2026-11-28 07:39:00    M30_69 : 9 opportunités · rapport et opportunités · 12 s
2026-11-28 07:39:04    M33_01 : 8 opportunités · inchangé · 5 s
2026-11-28 07:39:12    M33_14 : 7 opportunités · inchangé · 7 s
2026-11-28 07:39:19    M33_27 : 5 opportunités · inchangé · 7 s
2026-11-28 07:39:29    M33_38 : 8 opportunités · inchangé · 10 s
2026-11-28 07:39:37    M33_42 : 1 opportunités · rapport et opportunités · 9 s
2026-11-28 07:39:45    M33_50 : 5 opportunités · inchangé · 8 s
2026-11-28 07:39:52    M33_61 : 3 opportunités · inchangé · 7 s
2026-11-28 07:40:07    M33_69 : 10 opportunités · rapport et opportunités · 15 s
2026-11-28 07:40:15    M33_71 : 5 opportunités · inchangé · 8 s
2026-11-28 07:40:26    M33_76 : 14 opportunités · rapport et opportunités · 11 s
2026-11-28 07:40:35    M33_85 : 5 opportunités · rapport et opportunités · 8 s
2026-11-28 07:48:23    M33_FR : 533 opportunités · rapport et opportunités · 469 s
2026-11-28 07:48:34    M37_13 : 12 opportunités · inchangé · 10 s
2026-11-28 07:48:50    M39_13 : 14 opportunités · inchangé · 16 s
2026-11-28 07:49:01    M40_05 : 0 opportunités · inchangé · 11 s
2026-11-28 07:49:07    M40_76 : 1 opportunités · inchangé · 7 s
2026-11-28 07:49:18    P1005_14 : 2 opportunités · inchangé · 11 s
2026-11-28 07:49:30    P1005_22 : 6 opportunités · rapport et opportunités · 11 s
2026-11-28 07:49:39    P1005_27 : 1 opportunités · rapport et opportunités · 9 s
2026-11-28 07:49:50    P1005_29 : 7 opportunités · rapport et opportunités · 11 s
2026-11-28 07:50:05    P1005_35 : 17 opportunités · rapport et opportunités · 15 s
2026-11-28 07:50:16    P1005_56 : 10 opportunités · inchangé · 11 s
2026-11-28 07:50:36    P1005_59 : 18 opportunités · inchangé · 20 s
2026-11-28 07:50:46    P1005_60 : 2 opportunités · inchangé · 10 s
2026-11-28 07:51:23    P1005_75 : 40 opportunités · rapport et opportunités · 37 s
2026-11-28 07:51:38    P1005_76 : 6 opportunités · rapport et opportunités · 3 identifiants DECP raccourcis · 15 s
2026-11-28 07:51:46    P1005_80 : 1 opportunités · inchangé · 9 s
2026-11-28 07:52:01    P1005_93 : 12 opportunités · inchangé · 15 s
2026-11-28 07:52:05    contrats des chaînes : 172 envoyé(s), 10 retiré(s), 3121 cité(s) au total
2026-11-28 07:52:05  OK, 449 avis collectés, 365 couples recalculés, 50 republiés en 82.1 min
2026-11-28 07:56:31  Contrôle du 28/11 : vert — 365 couples identiques au site ; tâches à l'heure, site à jour
2026-11-28 14:47:45  tables du marché : 11 activité(s) envoyée(s), 0 inchangée(s), 361891 lignes en 98 paquets
```
