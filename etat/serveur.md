# Serveur du moteur V2

Mis à jour le 07/11/2026 à 04:24 · publication : **EN SERVICE (publie sur le site)**

## 🟢 **Tout va bien**

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-07 04:23:05  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-06 07:14:21  OK, 770 avis collectés, 224 couples recalculés, 63 republiés en 44.3 min |
| Passe DECP hebdomadaire | 2026-11-07 04:22:15  Passe hebdomadaire DECP 2026-11-07_decp : terminée avec échecs en 82.2 min, mémoire max 4269 Mo ; 236 couples recalculés, 0 bloqués par la garde, échecs : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; 222 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-06 07:17:01  Contrôle du 06/11 : rouge — 222 couples identiques au site, 349 attributions anciennes gardées par le site ; EN ÉCART : C713_75, M08_81 ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 0.57 Go sur 7.6 · charge 0.00 · disque 36.4 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : +5.3 point(s) par semaine · 80 % dans **8.1 semaine(s)**

```
Mesure du 2026-11-07 04:22 :
  entrepot/sources                            3.50 Go
  entrepot/decp                               1.59 Go
  entrepot/boamp                              1.38 Go
  entrepot/passes                             0.89 Go
  production/controles                        0.72 Go
  entrepot/execution                          0.68 Go
  parallele                                   0.66 Go
  entrepot/marche                             0.26 Go
  production/publies                          0.23 Go
  entrepot/photographie                       0.23 Go
  entrepot/etiquettes                           37 Mo
  entrepot/referentiel                          16 Mo
  entrepot/avis                                  4 Mo
  entrepot/sirene                                2 Mo
  production/(fichiers)                          2 Mo
  logs                                           2 Mo
  entrepot/mesures.jsonl                         1 Mo
  production/rejeu                               0 Mo
  entrepot/sources_temoin.jsonl                  0 Mo
  entrepot/manifeste.json                        0 Mo
Dernière purge (2026-11-07 04:22) : faite, 3 élément(s), 0.47 Go libérés · decp_telechargees 1 (0.25 Go) · fusions 1 (0.0 Go) · photographies_controle 1 (0.22 Go)
```

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 06/11 07:14 | 770 | 224 | 63 | 0 | 44.3 min |
| 05/11 07:12 | 770 | 223 | 65 | 0 | 42.3 min |
| 04/11 07:11 | 599 | 220 | 66 | 0 | 41.9 min |
| 03/11 07:09 | 315 | 219 | 79 | 0 | 39.6 min |
| 02/11 07:10 | 251 | 219 | 42 | 0 | 40.9 min |
| 01/11 07:13 | 543 | 219 | 219 | 0 | 43.6 min |
| 31/10 07:17 | 410 | 213 | 44 | 0 | 47.0 min |
| 30/10 07:07 | 695 | 172 | 55 | 0 | 37.1 min |
| 29/10 07:07 | 704 | 172 | 51 | 1 | 37.9 min |
| 28/10 07:09 | 640 | 166 | 62 | 0 | 39.0 min |

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
2026-10-26 07:09  Contrôle du 26/10 : vert — 163 couples identiques au site ; tâches à l'heure, site à jour
2026-10-27 07:13  Contrôle du 27/10 : vert — 166 couples identiques au site, 10 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
2026-10-28 07:14  Contrôle du 28/10 : vert — 166 couples identiques au site, 10 attributions anciennes gardées par le site ; tâches à l'heure, site à jour
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
```

## Tâches planifiées
```
NEXT                            LEFT LAST                              PASSED UNIT                     ACTIVATES
Sat 2026-11-07 05:45:00 CET 1h 20min Fri 2026-11-06 05:45:04 CET      22h ago tenderhit-purge.timer    tenderhit-purge.service
Sat 2026-11-07 06:30:00 CET  2h 5min Fri 2026-11-06 06:30:04 CET      21h ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-11-14 03:00:00 CET   6 days Sat 2026-11-07 03:00:00 CET 1h 24min ago tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                  - Sat 2026-11-07 04:24:04 CET       1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                  - Sat 2026-11-07 04:24:04 CET       1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-06 07:14:21  OK, 770 avis collectés, 224 couples recalculés, 63 republiés en 44.3 min
2026-11-06 07:17:01  Contrôle du 06/11 : rouge — 222 couples identiques au site, 349 attributions anciennes gardées par le site ; EN ÉCART : C713_75, M08_81 ; tâches à l'heure, site à jour
2026-11-06 15:50:07  M22_50 : demande en attente
2026-11-06 15:50:32    publié (édition 2026-11, 1 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 25 s
2026-11-06 15:50:32  M22_61 : demande en attente
2026-11-06 15:50:46    publié (édition 2026-11, 1 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 14 s
2026-11-06 17:48:08  purge du disque faite : 24 élément(s), 2.16 Go libérés — fusions 6 (0.01 Go), photographies_controle 16 (2.15 Go), tmp 2 (0.0 Go)
2026-11-06 20:14:07  M22_08 : demande en attente
2026-11-06 20:14:07    carte du 08 téléchargée
2026-11-06 20:14:21    publié (édition 2026-11, 1 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 14 s
2026-11-06 20:14:21  M22_10 : demande en attente
2026-11-06 20:14:22    carte du 10 téléchargée
2026-11-06 20:14:38    publié (édition 2026-11, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 16 s
2026-11-06 20:14:38  M22_51 : demande en attente
2026-11-06 20:14:38    carte du 51 téléchargée
2026-11-06 20:14:54    publié (édition 2026-11, 1 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 16 s
2026-11-06 20:14:54  M22_52 : demande en attente
2026-11-06 20:14:55    carte du 52 téléchargée
2026-11-06 20:15:10    publié (édition 2026-11, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 16 s
2026-11-06 20:15:11  M22_54 : demande en attente
2026-11-06 20:15:11    carte du 54 téléchargée
2026-11-06 20:15:27    publié (édition 2026-11, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 17 s
2026-11-06 20:15:27  M22_55 : demande en attente
2026-11-06 20:15:28    carte du 55 téléchargée
2026-11-06 20:15:43    publié (édition 2026-11, 1 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 16 s
2026-11-06 20:15:44  M22_57 : demande en attente
2026-11-06 20:15:44    carte du 57 téléchargée
2026-11-06 20:16:00    publié (édition 2026-11, 1 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 16 s
2026-11-06 20:16:00  M22_67 : demande en attente
2026-11-06 20:16:01    carte du 67 téléchargée
2026-11-06 20:16:10    publié (édition 2026-11, 4 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 9 s
2026-11-06 20:16:10  M22_68 : demande en attente
2026-11-06 20:16:10    carte du 68 téléchargée
2026-11-06 20:16:18    publié (édition 2026-11, 3 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 8 s
2026-11-06 20:16:18  M22_88 : demande en attente
2026-11-06 20:16:19    carte du 88 téléchargée
2026-11-06 20:16:34    publié (édition 2026-11, 0 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 16 s
2026-11-07 03:15:05  tables du marché : 244 activité(s) envoyée(s), 41 inchangée(s), 902516 lignes en 428 paquets ; erreurs : M08, M09, M10, M11, M12, M13, M14, M15, M16, M17, M18, M19, M20, M21, M22, M23, M24, M25, M26, M27, M28, M29, M30, M31, M32, M33, M34, M35, M36, M37, M38, M39, M40, M41, M42, M43, M44, M45, P1002, P1003, P1004, P1005
2026-11-07 04:22:15  Passe hebdomadaire DECP 2026-11-07_decp : terminée avec échecs en 82.2 min, mémoire max 4269 Mo ; 236 couples recalculés, 0 bloqués par la garde, échecs : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; 222 couples publiés, tables d'aide publiées
2026-11-07 04:22:15  purge du disque faite : 3 élément(s), 0.47 Go libérés — decp_telechargees 1 (0.25 Go), fusions 1 (0.0 Go), photographies_controle 1 (0.22 Go)
```
