# Serveur du moteur V2

Mis à jour le 15/11/2026 à 18:00 · publication : **EN SERVICE (publie sur le site)**

## 🟢 **Tout va bien**

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-15 17:59:04  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-15 07:19:05  OK, 430 avis collectés, 266 couples recalculés, 59 republiés en 49.1 min |
| Passe DECP hebdomadaire | 2026-11-14 04:22:58  Passe hebdomadaire DECP 2026-11-14_decp : terminée en 82.9 min, mémoire max 4234 Mo ; 266 couples recalculés, 0 bloqués par la garde ; 260 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-15 07:23:10  Contrôle du 15/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 0.46 Go sur 7.6 · charge 0.00 · disque 37.1 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : +2.9 point(s) par semaine · 80 % dans **14.8 semaine(s)**

```
Mesure du 2026-11-15 05:45 :
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
  entrepot/avis                                  3 Mo
  entrepot/sirene                                2 Mo
  logs                                           2 Mo
  production/(fichiers)                          2 Mo
  entrepot/mesures.jsonl                         1 Mo
  entrepot/tmp                                   1 Mo
  production/rejeu                               0 Mo
  entrepot/sources_temoin.jsonl                  0 Mo
  entrepot/manifeste.json                        0 Mo
Croissance par dossier (depuis 2026-11-07, 8.0 j), en Go par semaine :
  entrepot/decp                                 +0.37
  entrepot/passes                               +0.26
  entrepot/sources                              +0.03
  entrepot/boamp                                +0.01
Dernière purge (2026-11-15 05:45) : faite, 2 élément(s), 0.23 Go libérés · fusions 1 (0.0 Go) · photographies_controle 1 (0.22 Go)
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

- 09:52 : (édition 2026-11, 9 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None, 3 identifiants DECP raccourcis) en 9 s
- 11:42 : (édition 2026-11, 26 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 10 s
- 11:42 : (édition 2026-11, 26 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 12 s
- 11:46 : (édition 2026-11, 7 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 14 s
- 11:46 : (édition 2026-11, 3 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 12 s
- 12:04 : (édition 2026-11, 21 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 11 s
- 12:04 : (édition 2026-11, 21 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 9 s
- 15:33 : (édition 2026-11, 21 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 10 s
- 15:33 : (édition 2026-11, 21 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 9 s
- 15:33 : (édition 2026-11, 21 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 9 s

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
NEXT                          LEFT LAST                         PASSED UNIT                     ACTIVATES
Mon 2026-11-16 05:45:00 CET    11h Sun 2026-11-15 05:45:00 CET 12h ago tenderhit-purge.timer    tenderhit-purge.service
Mon 2026-11-16 06:30:00 CET    12h Sun 2026-11-15 06:30:00 CET 11h ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-11-21 03:00:00 CET 5 days Sat 2026-11-14 03:00:04 CET       - tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                - Sun 2026-11-15 18:00:00 CET  1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                - Sun 2026-11-15 18:00:00 CET  1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-15 07:16:50    M40_76 : 0 opportunités · rapport et opportunités · 7 s
2026-11-15 07:16:59    P1005_14 : 1 opportunités · inchangé · 9 s
2026-11-15 07:17:07    P1005_22 : 8 opportunités · inchangé · 8 s
2026-11-15 07:17:15    P1005_27 : 1 opportunités · inchangé · 8 s
2026-11-15 07:17:24    P1005_29 : 9 opportunités · inchangé · 9 s
2026-11-15 07:17:35    P1005_35 : 20 opportunités · inchangé · 11 s
2026-11-15 07:17:44    P1005_56 : 12 opportunités · inchangé · 9 s
2026-11-15 07:17:59    P1005_59 : 19 opportunités · inchangé · 15 s
2026-11-15 07:18:09    P1005_60 : 2 opportunités · rapport et opportunités · 10 s
2026-11-15 07:18:32    P1005_75 : 37 opportunités · inchangé · 23 s
2026-11-15 07:18:43    P1005_76 : 6 opportunités · rapport et opportunités · 3 identifiants DECP raccourcis · 12 s
2026-11-15 07:18:52    P1005_80 : 0 opportunités · inchangé · 9 s
2026-11-15 07:19:05    P1005_93 : 10 opportunités · rapport et opportunités · 13 s
2026-11-15 07:19:05  OK, 430 avis collectés, 266 couples recalculés, 59 republiés en 49.1 min
2026-11-15 07:23:10  Contrôle du 15/11 : vert — 266 couples identiques au site ; tâches à l'heure, site à jour
2026-11-15 09:52:04  C713_30 : demande en attente
2026-11-15 09:52:05    carte du 30 téléchargée
2026-11-15 09:52:13    publié (édition 2026-11, 9 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None, 3 identifiants DECP raccourcis) en 9 s
2026-11-15 11:42:04  M01_35 : demande en attente
2026-11-15 11:42:14    publié (édition 2026-11, 26 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 10 s
2026-11-15 11:42:14  M01_77 : demande en attente
2026-11-15 11:42:15    carte du 77 téléchargée
2026-11-15 11:42:27    publié (édition 2026-11, 26 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 12 s
2026-11-15 11:46:05  M02_59 : demande en attente
2026-11-15 11:46:19    publié (édition 2026-11, 7 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 14 s
2026-11-15 11:46:19  M02_62 : demande en attente
2026-11-15 11:46:31    publié (édition 2026-11, 3 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 12 s
2026-11-15 11:46:35  tables du marché : 1 activité(s) envoyée(s), 0 inchangée(s), 4758 lignes en 4 paquets
2026-11-15 12:04:03  C747_59 : demande en attente
2026-11-15 12:04:14    publié (édition 2026-11, 21 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 11 s
2026-11-15 12:04:14  C747_62 : demande en attente
2026-11-15 12:04:23    publié (édition 2026-11, 21 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 9 s
2026-11-15 12:04:25  tables du marché : 1 activité(s) envoyée(s), 0 inchangée(s), 905 lignes en 4 paquets
2026-11-15 15:33:05  C747_02 : demande en attente
2026-11-15 15:33:05    carte du 02 téléchargée
2026-11-15 15:33:15    publié (édition 2026-11, 21 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 10 s
2026-11-15 15:33:15  C747_60 : demande en attente
2026-11-15 15:33:24    publié (édition 2026-11, 21 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 9 s
2026-11-15 15:33:24  C747_80 : demande en attente
2026-11-15 15:33:34    publié (édition 2026-11, 21 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 9 s
```
