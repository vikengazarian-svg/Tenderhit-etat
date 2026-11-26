# Serveur du moteur V2

Mis à jour le 26/11/2026 à 05:00 · publication : **EN SERVICE (publie sur le site)**

## 🟢 **Tout va bien**

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-26 04:59:03  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-25 07:30:25  OK, 584 avis collectés, 363 couples recalculés, 113 republiés en 60.4 min |
| Passe DECP hebdomadaire | 2026-11-21 04:33:49  Passe hebdomadaire DECP 2026-11-21_decp : terminée en 93.8 min, mémoire max 4287 Mo ; 360 couples recalculés, 1 bloqués par la garde (M01_58) ; 352 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-25 07:34:56  Contrôle du 25/11 : vert — 363 couples identiques au site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 0.44 Go sur 7.6 · charge 0.00 · disque 37.4 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : +0.6 point(s) par semaine · 80 % dans **77.4 semaine(s)**

```
Mesure du 2026-11-25 05:45 :
  entrepot/sources                            3.56 Go
  entrepot/decp                               2.06 Go
  entrepot/boamp                              1.40 Go
  entrepot/passes                             1.23 Go
  production/controles                        0.72 Go
  entrepot/execution                          0.71 Go
  entrepot/marche                             0.26 Go
  production/publies                          0.24 Go
  entrepot/photographie                       0.23 Go
  entrepot/etiquettes                           38 Mo
  entrepot/referentiel                          16 Mo
  entrepot/avis                                  3 Mo
  logs                                           3 Mo
  production/(fichiers)                          2 Mo
  entrepot/sirene                                2 Mo
  entrepot/mesures.jsonl                         2 Mo
  production/rejeu                               0 Mo
  entrepot/sources_temoin.jsonl                  0 Mo
  entrepot/manifeste.json                        0 Mo
  production/dce                                 0 Mo
Croissance par dossier (depuis 2026-11-18, 7.0 j), en Go par semaine :
  entrepot/passes                               +0.04
  entrepot/decp                                 +0.03
  entrepot/execution                            +0.03
  entrepot/sources                              +0.03
  production/controles                          +0.03
  entrepot/boamp                                +0.01
Dernière purge (2026-11-25 05:45) : faite, 3 élément(s), 0.24 Go libérés · fusions 1 (0.0 Go) · photographies_controle 1 (0.24 Go) · tmp 1 (0.0 Go)
```

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 25/11 07:30 | 584 | 363 | 113 | 0 | 60.4 min |
| 24/11 07:30 | 586 | 363 | 114 | 0 | 60.2 min |
| 23/11 07:28 | 254 | 355 | 30 | 0 | 58.0 min |
| 22/11 07:29 | 692 | 361 | 100 | 0 | 59.3 min |
| 21/11 07:30 | 878 | 360 | 151 | 0 | 60.1 min |
| 20/11 07:27 | 337 | 343 | 91 | 0 | 57.2 min |
| 19/11 07:29 | 545 | 347 | 111 | 0 | 59.0 min |
| 18/11 07:23 | 362 | 310 | 87 | 0 | 53.6 min |
| 17/11 07:22 | 346 | 306 | 114 | 0 | 52.8 min |
| 16/11 07:19 | 306 | 270 | 61 | 0 | 49.6 min |

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
2026-11-12 07:20  Contrôle du 12/11 : vert — 249 couples identiques au site ; tâches à l'heure, site à jour
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
```

## Tâches planifiées
```
NEXT                             LEFT LAST                        PASSED UNIT                     ACTIVATES
Thu 2026-11-26 05:45:00 CET     44min Wed 2026-11-25 05:45:00 CET      - tenderhit-purge.timer    tenderhit-purge.service
Thu 2026-11-26 06:30:00 CET  1h 29min Wed 2026-11-25 06:30:00 CET      - tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-11-28 03:00:00 CET 1 day 21h Sat 2026-11-21 03:00:00 CET      - tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                   - Thu 2026-11-26 05:00:01 CET 1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                   - Thu 2026-11-26 05:00:01 CET 1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-25 07:21:26    M29_74 : 0 opportunités · rapport et opportunités · 17 s
2026-11-25 07:21:39    M29_83 : 1 opportunités · inchangé · 13 s
2026-11-25 07:22:00    M29_93 : 2 opportunités · rapport et opportunités · 21 s
2026-11-25 07:22:09    M30_69 : 7 opportunités · inchangé · 9 s
2026-11-25 07:22:12    M33_01 : 9 opportunités · inchangé · 3 s
2026-11-25 07:22:19    M33_14 : 6 opportunités · inchangé · 7 s
2026-11-25 07:22:25    M33_27 : 5 opportunités · inchangé · 6 s
2026-11-25 07:22:33    M33_38 : 8 opportunités · rapport et opportunités · 8 s
2026-11-25 07:22:40    M33_42 : 0 opportunités · rapport et opportunités · 7 s
2026-11-25 07:22:47    M33_50 : 4 opportunités · inchangé · 6 s
2026-11-25 07:22:53    M33_61 : 3 opportunités · rapport et opportunités · 6 s
2026-11-25 07:23:04    M33_69 : 9 opportunités · rapport et opportunités · 11 s
2026-11-25 07:23:11    M33_71 : 6 opportunités · rapport et opportunités · 7 s
2026-11-25 07:23:19    M33_76 : 13 opportunités · rapport et opportunités · 8 s
2026-11-25 07:23:27    M33_85 : 3 opportunités · rapport et opportunités · 8 s
2026-11-25 07:27:39    M33_FR : 489 opportunités · rapport et opportunités · 252 s
2026-11-25 07:27:49    M37_13 : 12 opportunités · rapport et opportunités · 10 s
2026-11-25 07:28:00    M40_05 : 0 opportunités · rapport et opportunités · 11 s
2026-11-25 07:28:07    M40_76 : 0 opportunités · inchangé · 6 s
2026-11-25 07:28:15    P1005_14 : 2 opportunités · inchangé · 9 s
2026-11-25 07:28:24    P1005_22 : 7 opportunités · inchangé · 8 s
2026-11-25 07:28:32    P1005_27 : 2 opportunités · inchangé · 8 s
2026-11-25 07:28:41    P1005_29 : 8 opportunités · inchangé · 9 s
2026-11-25 07:28:53    P1005_35 : 18 opportunités · rapport et opportunités · 12 s
2026-11-25 07:29:02    P1005_56 : 11 opportunités · rapport et opportunités · 10 s
2026-11-25 07:29:17    P1005_59 : 18 opportunités · inchangé · 15 s
2026-11-25 07:29:26    P1005_60 : 2 opportunités · inchangé · 9 s
2026-11-25 07:29:51    P1005_75 : 38 opportunités · rapport et opportunités · 24 s
2026-11-25 07:30:04    P1005_76 : 6 opportunités · rapport et opportunités · 3 identifiants DECP raccourcis · 13 s
2026-11-25 07:30:12    P1005_80 : 1 opportunités · inchangé · 9 s
2026-11-25 07:30:25    P1005_93 : 12 opportunités · inchangé · 13 s
2026-11-25 07:30:25  OK, 584 avis collectés, 363 couples recalculés, 113 republiés en 60.4 min
2026-11-25 07:34:56  Contrôle du 25/11 : vert — 363 couples identiques au site ; tâches à l'heure, site à jour
2026-11-25 11:24:04  M30_13 : demande en attente
2026-11-25 11:24:14    publié (édition 2026-11, 6 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 11 s
2026-11-25 11:30:05  M39_13 : demande en attente
2026-11-25 11:30:30    publié (édition 2026-11, 15 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 25 s
2026-11-25 11:31:51  tables du marché : 1 activité(s) envoyée(s), 0 inchangée(s), 204230 lignes en 43 paquets
2026-11-25 15:05:53  retrait DCE (retraits) impossible : dce_en_attente : ReadTimeout : HTTPSConnectionPool(host='tenhit.fr', port=443): Read timed out. (read timeout=30)
2026-11-25 15:08:15  retrait DCE (retraits) impossible : dce_en_attente : ReadTimeout : HTTPSConnectionPool(host='tenhit.fr', port=443): Read timed out. (read timeout=30)
```
