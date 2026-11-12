# Serveur du moteur V2

Mis à jour le 12/11/2026 à 15:00 · publication : **EN SERVICE (publie sur le site)**

## 🟢 **Tout va bien**

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-12 14:59:06  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-12 07:16:52  OK, 433 avis collectés, 249 couples recalculés, 38 republiés en 46.8 min |
| Passe DECP hebdomadaire | 2026-11-07 04:22:15  Passe hebdomadaire DECP 2026-11-07_decp : terminée avec échecs en 82.2 min, mémoire max 4269 Mo ; 236 couples recalculés, 0 bloqués par la garde, échecs : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; 222 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-12 07:20:08  Contrôle du 12/11 : vert — 249 couples identiques au site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 0.57 Go sur 7.6 · charge 0.00 · disque 36.5 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : +4.4 point(s) par semaine · 80 % dans **9.9 semaine(s)**

```
Mesure du 2026-11-12 05:45 :
  entrepot/sources                            3.50 Go
  entrepot/decp                               1.59 Go
  entrepot/boamp                              1.39 Go
  production/controles                        1.13 Go
  entrepot/passes                             0.89 Go
  entrepot/execution                          0.63 Go
  entrepot/marche                             0.26 Go
  entrepot/photographie                       0.23 Go
  production/publies                          0.20 Go
  entrepot/etiquettes                           37 Mo
  entrepot/referentiel                          16 Mo
  entrepot/avis                                  4 Mo
  entrepot/sirene                                2 Mo
  entrepot/tmp                                   2 Mo
  logs                                           2 Mo
  production/(fichiers)                          2 Mo
  entrepot/mesures.jsonl                         1 Mo
  production/rejeu                               0 Mo
  entrepot/sources_temoin.jsonl                  0 Mo
  entrepot/manifeste.json                        0 Mo
Croissance par dossier (depuis 2026-11-05, 6.3 j), en Go par semaine :
  entrepot/decp                                 +0.45
  entrepot/passes                               +0.34
  entrepot/boamp                                +0.01
Dernière purge (2026-11-12 05:45) : faite, 2 élément(s), 0.23 Go libérés · fusions 1 (0.0 Go) · photographies_controle 1 (0.22 Go)
```

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 12/11 07:16 | 433 | 249 | 38 | 0 | 46.8 min |
| 11/11 07:18 | 647 | 249 | 176 | 0 | 48.8 min |
| 10/11 07:18 | 343 | 241 | 89 | 0 | 48.4 min |
| 09/11 07:16 | 305 | 236 | 59 | 0 | 46.0 min |
| 08/11 07:16 | 673 | 233 | 90 | 0 | 46.0 min |
| 07/11 07:15 | 519 | 233 | 72 | 0 | 45.7 min |
| 06/11 07:14 | 770 | 224 | 63 | 0 | 44.3 min |
| 05/11 07:12 | 770 | 223 | 65 | 0 | 42.3 min |
| 04/11 07:11 | 599 | 220 | 66 | 0 | 41.9 min |
| 03/11 07:09 | 315 | 219 | 79 | 0 | 39.6 min |

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

- 10:18 : (édition 2026-11, 7 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 6 s
- 10:18 : (édition 2026-11, 3 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 6 s
- 10:18 : (édition 2026-11, 1 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 24 s
- 10:26 : (édition 2026-11, 7 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 6 s
- 10:26 : (édition 2026-11, 4 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 4 s
- 10:26 : (édition 2026-11, 1 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 18 s
- 10:26 : (édition 2026-11, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 17 s
- 10:27 : (édition 2026-11, 7 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 6 s
- 10:27 : (édition 2026-11, 10 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 7 s
- 10:27 : (édition 2026-11, 6 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 6 s
- 10:27 : (édition 2026-11, 2 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 17 s
- 10:27 : (édition 2026-11, 2 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 7 s
- 10:27 : (édition 2026-11, 21 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 8 s
- 10:27 : (édition 2026-11, 7 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 6 s
- 10:28 : (édition 2026-11, 9 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 7 s
- 10:28 : (édition 2026-11, 17 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 8 s
- 10:28 : (édition 2026-11, 23 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 8 s

### Contrôles quotidiens (14 derniers)

```
2026-11-02 07:14  Contrôle du 02/11 : vert — 219 couples identiques au site, 349 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
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
```

## Tâches planifiées
```
NEXT                             LEFT LAST                            PASSED UNIT                     ACTIVATES
Fri 2026-11-13 05:45:00 CET       14h Thu 2026-11-12 05:45:04 CET     9h ago tenderhit-purge.timer    tenderhit-purge.service
Fri 2026-11-13 06:30:00 CET       15h Thu 2026-11-12 06:30:04 CET     8h ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-11-14 03:00:00 CET 1 day 11h Sat 2026-11-07 03:00:00 CET 5 days ago tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                   - Thu 2026-11-12 15:00:00 CET     1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                   - Thu 2026-11-12 15:00:00 CET     1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-12 07:16:39    P1005_80 : 0 opportunités · inchangé · 8 s
2026-11-12 07:16:52    P1005_93 : 11 opportunités · inchangé · 12 s
2026-11-12 07:16:52  OK, 433 avis collectés, 249 couples recalculés, 38 republiés en 46.8 min
2026-11-12 07:20:08  Contrôle du 12/11 : vert — 249 couples identiques au site ; tâches à l'heure, site à jour
2026-11-12 10:18:08  C772_83 : demande en attente
2026-11-12 10:18:14    publié (édition 2026-11, 7 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 6 s
2026-11-12 10:18:14  C772_93 : demande en attente
2026-11-12 10:18:19    publié (édition 2026-11, 3 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 6 s
2026-11-12 10:18:19  M29_93 : demande en attente
2026-11-12 10:18:44    publié (édition 2026-11, 1 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 24 s
2026-11-12 10:26:08  M12_01 : demande en attente
2026-11-12 10:26:14    publié (édition 2026-11, 7 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 6 s
2026-11-12 10:26:14  M12_03 : demande en attente
2026-11-12 10:26:18    publié (édition 2026-11, 4 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 4 s
2026-11-12 10:26:19  M12_07 : demande en attente
2026-11-12 10:26:36    publié (édition 2026-11, 1 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 18 s
2026-11-12 10:26:36  M12_15 : demande en attente
2026-11-12 10:26:53    publié (édition 2026-11, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 17 s
2026-11-12 10:26:54  M12_26 : demande en attente
2026-11-12 10:27:00    publié (édition 2026-11, 7 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 6 s
2026-11-12 10:27:00  M12_38 : demande en attente
2026-11-12 10:27:07    publié (édition 2026-11, 10 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 7 s
2026-11-12 10:27:08  M12_42 : demande en attente
2026-11-12 10:27:14    publié (édition 2026-11, 6 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 6 s
2026-11-12 10:27:14  M12_43 : demande en attente
2026-11-12 10:27:31    publié (édition 2026-11, 2 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 17 s
2026-11-12 10:27:32  M12_63 : demande en attente
2026-11-12 10:27:38    publié (édition 2026-11, 2 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 7 s
2026-11-12 10:27:38  M12_69 : demande en attente
2026-11-12 10:27:47    publié (édition 2026-11, 21 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 8 s
2026-11-12 10:27:47  M12_73 : demande en attente
2026-11-12 10:27:53    publié (édition 2026-11, 7 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 6 s
2026-11-12 10:27:54  M12_74 : demande en attente
2026-11-12 10:28:01    publié (édition 2026-11, 9 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 7 s
2026-11-12 10:28:01  M12_83 : demande en attente
2026-11-12 10:28:08    publié (édition 2026-11, 17 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 8 s
2026-11-12 10:28:09  M12_93 : demande en attente
2026-11-12 10:28:16    publié (édition 2026-11, 23 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 8 s
2026-11-12 10:28:31  tables du marché : 1 activité(s) envoyée(s), 0 inchangée(s), 31572 lignes en 8 paquets
2026-11-12 11:10:50  Rejeu sur le serveur : vert — 6 couples identiques aux envois du matin sur 6 comparés ; 6.1 s par couple (médiane), 1 min au total
```
