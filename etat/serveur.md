# Serveur du moteur V2

Mis à jour le 10/11/2026 à 05:00 · publication : **EN SERVICE (publie sur le site)**

## 🟢 **Tout va bien**

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-10 04:59:05  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-09 07:16:01  OK, 305 avis collectés, 236 couples recalculés, 59 republiés en 45.9 min |
| Passe DECP hebdomadaire | 2026-11-07 04:22:15  Passe hebdomadaire DECP 2026-11-07_decp : terminée avec échecs en 82.2 min, mémoire max 4269 Mo ; 236 couples recalculés, 0 bloqués par la garde, échecs : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; 222 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-09 07:18:46  Contrôle du 09/11 : rouge — 222 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 0.56 Go sur 7.6 · charge 0.01 · disque 35.5 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : +4.2 point(s) par semaine · 80 % dans **10.5 semaine(s)**

```
Mesure du 2026-11-09 05:45 :
  entrepot/sources                            3.50 Go
  entrepot/decp                               1.59 Go
  entrepot/boamp                              1.38 Go
  entrepot/passes                             0.89 Go
  entrepot/execution                          0.68 Go
  production/controles                        0.67 Go
  entrepot/marche                             0.26 Go
  production/publies                          0.23 Go
  entrepot/photographie                       0.23 Go
  entrepot/etiquettes                           37 Mo
  entrepot/referentiel                          16 Mo
  entrepot/avis                                  4 Mo
  entrepot/tmp                                   2 Mo
  entrepot/sirene                                2 Mo
  production/(fichiers)                          2 Mo
  logs                                           2 Mo
  entrepot/mesures.jsonl                         1 Mo
  production/rejeu                               0 Mo
  entrepot/sources_temoin.jsonl                  0 Mo
  entrepot/manifeste.json                        0 Mo
Croissance par dossier (depuis 2026-11-05, 3.3 j), en Go par semaine :
  entrepot/decp                                 +0.86
  entrepot/passes                               +0.65
  entrepot/execution                            +0.03
  entrepot/boamp                                +0.01
  production/publies                            +0.01
Dernière purge (2026-11-09 05:45) : faite, 4 élément(s), 0.29 Go libérés · fusions 1 (0.0 Go) · photographies_controle 2 (0.28 Go) · tmp 1 (0.0 Go)
```

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 09/11 07:16 | 305 | 236 | 59 | 0 | 46.0 min |
| 08/11 07:16 | 673 | 233 | 90 | 0 | 46.0 min |
| 07/11 07:15 | 519 | 233 | 72 | 0 | 45.7 min |
| 06/11 07:14 | 770 | 224 | 63 | 0 | 44.3 min |
| 05/11 07:12 | 770 | 223 | 65 | 0 | 42.3 min |
| 04/11 07:11 | 599 | 220 | 66 | 0 | 41.9 min |
| 03/11 07:09 | 315 | 219 | 79 | 0 | 39.6 min |
| 02/11 07:10 | 251 | 219 | 42 | 0 | 40.9 min |
| 01/11 07:13 | 543 | 219 | 219 | 0 | 43.6 min |
| 31/10 07:17 | 410 | 213 | 44 | 0 | 47.0 min |

### Passes DECP hebdomadaires

| Passe | Durée des couples | Mémoire max |
|---|---:|---:|
| 2026-11-07_decp | 55.7 min | 2686 Mo |
| 2026-10-31_decp | 53.2 min | 2538 Mo |
| 2026-10-24_decp | 33.0 min | 2373 Mo |
| 2026-10-17_decp | 41.8 min | — Mo |
| essai_pc | 26.3 min | 1616 Mo |
| essai_2026-10-16 | 26.4 min | 1950 Mo |

### Demandes des clients aujourd'hui

Aucune pour l'instant.

### Contrôles quotidiens (14 derniers)

```
2026-10-29 07:13  Contrôle du 29/10 : rouge — 171 couples identiques au site, 10 attributions anciennes gardées par le site ; EN ÉCART : C713_FR ; collecte du matin : 2026-10-29 07:07:57  1 ÉCHEC(S), 704 avis collectés, 172 couples recalculés, 51 republiés en 37.9 min
2026-10-30 07:12  Contrôle du 30/10 : vert — 172 couples identiques au site, 10 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-10-31 07:20  Contrôle du 31/10 : rouge — 215 couples identiques au site, 349 attributions anciennes gardées par le site ; EN ÉCART : M01_04, M01_27, M01_63, M01_71 ; tâches à l'heure, site à jour
2026-10-31 11:33  Contrôle du 31/10 : vert — 219 couples identiques au site, 349 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-11-01 07:17  Contrôle du 01/11 : vert — 219 couples identiques au site, 349 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-11-02 07:14  Contrôle du 02/11 : vert — 219 couples identiques au site, 349 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-11-03 07:12  Contrôle du 03/11 : vert — 219 couples identiques au site, 349 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-11-04 07:15  Contrôle du 04/11 : vert — 220 couples identiques au site, 349 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-11-05 07:15  Contrôle du 05/11 : rouge — photographie du site impossible ou incomplète
2026-11-05 11:03  Contrôle du 05/11 : rouge — photographie du site impossible ou incomplète
2026-11-06 07:17  Contrôle du 06/11 : rouge — 222 couples identiques au site, 349 attributions anciennes gardées par le site ; EN ÉCART : C713_75, M08_81 ; tâches à l'heure, site à jour
2026-11-07 07:18  Contrôle du 07/11 : rouge — 223 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour
2026-11-08 07:18  Contrôle du 08/11 : rouge — 223 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour
2026-11-09 07:18  Contrôle du 09/11 : rouge — 222 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                            LEFT LAST                            PASSED UNIT                     ACTIVATES
Tue 2026-11-10 05:45:00 CET    44min Mon 2026-11-09 05:45:04 CET    23h ago tenderhit-purge.timer    tenderhit-purge.service
Tue 2026-11-10 06:30:00 CET 1h 29min Mon 2026-11-09 06:30:04 CET    22h ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-11-14 03:00:00 CET   3 days Sat 2026-11-07 03:00:00 CET 3 days ago tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                  - Tue 2026-11-10 05:00:04 CET     1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                  - Tue 2026-11-10 05:00:04 CET     1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-09 07:14:03    P1005_22 : 8 opportunités · inchangé · 9 s
2026-11-09 07:14:11    P1005_27 : 3 opportunités · inchangé · 8 s
2026-11-09 07:14:21    P1005_29 : 14 opportunités · rapport et opportunités · 10 s
2026-11-09 07:14:32    P1005_35 : 17 opportunités · rapport et opportunités · 12 s
2026-11-09 07:14:41    P1005_56 : 13 opportunités · inchangé · 9 s
2026-11-09 07:14:57    P1005_59 : 19 opportunités · opportunités · 16 s
2026-11-09 07:15:06    P1005_60 : 3 opportunités · inchangé · 9 s
2026-11-09 07:15:29    P1005_75 : 43 opportunités · rapport et opportunités · 24 s
2026-11-09 07:15:40    P1005_76 : 8 opportunités · inchangé · 11 s
2026-11-09 07:15:49    P1005_80 : 0 opportunités · inchangé · 8 s
2026-11-09 07:16:01    P1005_93 : 13 opportunités · inchangé · 12 s
2026-11-09 07:16:01  OK, 305 avis collectés, 236 couples recalculés, 59 republiés en 45.9 min
2026-11-09 07:18:46  Contrôle du 09/11 : rouge — 222 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour
2026-11-09 17:17:07  M29_01 : demande en attente
2026-11-09 17:17:24    publié (édition 2026-11, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 17 s
2026-11-09 17:17:25  M29_03 : demande en attente
2026-11-09 17:17:40    publié (édition 2026-11, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 15 s
2026-11-09 17:17:40  M29_07 : demande en attente
2026-11-09 17:17:56    publié (édition 2026-11, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 15 s
2026-11-09 17:17:56  M29_15 : demande en attente
2026-11-09 17:18:13    publié (édition 2026-11, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 17 s
2026-11-09 17:18:13  M29_26 : demande en attente
2026-11-09 17:18:31    publié (édition 2026-11, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 18 s
2026-11-09 17:18:31  M29_38 : demande en attente
2026-11-09 17:18:49    publié (édition 2026-11, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 18 s
2026-11-09 17:18:49  M29_42 : demande en attente
2026-11-09 17:19:07    publié (édition 2026-11, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 18 s
2026-11-09 17:19:07  M29_43 : demande en attente
2026-11-09 17:19:24    publié (édition 2026-11, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 17 s
2026-11-09 17:19:24  M29_63 : demande en attente
2026-11-09 17:19:41    publié (édition 2026-11, 1 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 17 s
2026-11-09 17:19:42  M29_69 : demande en attente
2026-11-09 17:19:50    publié (édition 2026-11, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 9 s
2026-11-09 17:19:51  M29_73 : demande en attente
2026-11-09 17:20:09    publié (édition 2026-11, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 18 s
2026-11-09 17:20:09  M29_74 : demande en attente
2026-11-09 17:20:27    publié (édition 2026-11, 1 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 18 s
2026-11-09 17:20:32  tables du marché : 1 activité(s) envoyée(s), 0 inchangée(s), 5198 lignes en 4 paquets
2026-11-09 17:25:06  M29_83 : demande en attente
2026-11-09 17:25:22    publié (édition 2026-11, 2 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 16 s
```
