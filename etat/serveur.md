# Serveur du moteur V2

Mis à jour le 11/11/2026 à 02:00 · publication : **EN SERVICE (publie sur le site)**

## 🟢 **Tout va bien**

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-11 01:59:05  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-10 07:18:25  OK, 343 avis collectés, 241 couples recalculés, 89 republiés en 48.4 min |
| Passe DECP hebdomadaire | 2026-11-07 04:22:15  Passe hebdomadaire DECP 2026-11-07_decp : terminée avec échecs en 82.2 min, mémoire max 4269 Mo ; 236 couples recalculés, 0 bloqués par la garde, échecs : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; 222 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-10 13:50:59  Contrôle du 10/11 : vert — 249 couples identiques au site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 0.56 Go sur 7.6 · charge 0.00 · disque 36.3 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : +4.5 point(s) par semaine · 80 % dans **9.6 semaine(s)**

```
Mesure du 2026-11-10 05:45 :
  entrepot/sources                            3.50 Go
  entrepot/decp                               1.59 Go
  entrepot/boamp                              1.38 Go
  entrepot/passes                             0.89 Go
  entrepot/execution                          0.69 Go
  production/controles                        0.67 Go
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
  entrepot/tmp                                   0 Mo
Croissance par dossier (depuis 2026-11-05, 4.3 j), en Go par semaine :
  entrepot/decp                                 +0.66
  entrepot/passes                               +0.50
  entrepot/execution                            +0.04
  entrepot/boamp                                +0.01
  production/publies                            +0.01
Dernière purge (2026-11-10 05:45) : faite, 3 élément(s), 0.22 Go libérés · fusions 1 (0.0 Go) · photographies_controle 1 (0.22 Go) · tmp 1 (0.0 Go)
```

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 10/11 07:18 | 343 | 241 | 89 | 0 | 48.4 min |
| 09/11 07:16 | 305 | 236 | 59 | 0 | 46.0 min |
| 08/11 07:16 | 673 | 233 | 90 | 0 | 46.0 min |
| 07/11 07:15 | 519 | 233 | 72 | 0 | 45.7 min |
| 06/11 07:14 | 770 | 224 | 63 | 0 | 44.3 min |
| 05/11 07:12 | 770 | 223 | 65 | 0 | 42.3 min |
| 04/11 07:11 | 599 | 220 | 66 | 0 | 41.9 min |
| 03/11 07:09 | 315 | 219 | 79 | 0 | 39.6 min |
| 02/11 07:10 | 251 | 219 | 42 | 0 | 40.9 min |
| 01/11 07:13 | 543 | 219 | 219 | 0 | 43.6 min |

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
2026-11-10 07:21  Contrôle du 10/11 : rouge — 235 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour
2026-11-10 11:59  Contrôle du 10/11 : rouge — 235 couples identiques au site, 4238 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour ; CHUTES : C451_21 : attributions 585 → 270, C451_42 : attributions 1131 → 535
2026-11-10 13:50  Contrôle du 10/11 : vert — 249 couples identiques au site ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                            LEFT LAST                            PASSED UNIT                     ACTIVATES
Wed 2026-11-11 05:45:00 CET 3h 44min Tue 2026-11-10 05:45:04 CET    20h ago tenderhit-purge.timer    tenderhit-purge.service
Wed 2026-11-11 06:30:00 CET 4h 29min Tue 2026-11-10 06:30:04 CET    19h ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-11-14 03:00:00 CET   3 days Sat 2026-11-07 03:00:00 CET 3 days ago tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                  - Wed 2026-11-11 02:00:04 CET     1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                  - Wed 2026-11-11 02:00:04 CET     1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-10 07:10:57    M33_71 : 9 opportunités · rapport et opportunités · 8 s
2026-11-10 07:11:05    M33_76 : 15 opportunités · inchangé · 8 s
2026-11-10 07:11:12    M33_85 : 3 opportunités · inchangé · 7 s
2026-11-10 07:15:49    M33_FR : 580 opportunités · rapport et opportunités · 277 s
2026-11-10 07:15:59    M40_05 : 0 opportunités · inchangé · 10 s
2026-11-10 07:16:05    M40_76 : 1 opportunités · inchangé · 6 s
2026-11-10 07:16:14    P1005_14 : 0 opportunités · inchangé · 9 s
2026-11-10 07:16:24    P1005_22 : 6 opportunités · rapport et opportunités · 10 s
2026-11-10 07:16:34    P1005_27 : 2 opportunités · rapport et opportunités · 9 s
2026-11-10 07:16:44    P1005_29 : 13 opportunités · rapport et opportunités · 10 s
2026-11-10 07:16:55    P1005_35 : 18 opportunités · rapport et opportunités · 12 s
2026-11-10 07:17:04    P1005_56 : 13 opportunités · inchangé · 9 s
2026-11-10 07:17:19    P1005_59 : 19 opportunités · inchangé · 15 s
2026-11-10 07:17:28    P1005_60 : 3 opportunités · inchangé · 9 s
2026-11-10 07:17:52    P1005_75 : 42 opportunités · rapport et opportunités · 24 s
2026-11-10 07:18:04    P1005_76 : 8 opportunités · inchangé · 11 s
2026-11-10 07:18:12    P1005_80 : 0 opportunités · inchangé · 9 s
2026-11-10 07:18:25    P1005_93 : 13 opportunités · inchangé · 13 s
2026-11-10 07:18:25  OK, 343 avis collectés, 241 couples recalculés, 89 republiés en 48.4 min
2026-11-10 07:21:09  Contrôle du 10/11 : rouge — 235 couples identiques au site, 369 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour
2026-11-10 10:44:04  Rejeu sur le serveur : rouge — 19 couples identiques au PC sur 89 comparés ; en écart ou en échec : C093_69, C451_25, C451_39, C451_69, C451_71, C451_73, C451_FR, C712_74, C713_75, C772_14, C772_76, C772_FR, M01_14, M01_16, M01_24, M01_39, M01_58, M01_59, M01_70, M01_75, M01_83, M01_89, M01_90, M01_FR, M04_62, M07_59, M22_05, M22_07, M22_08, M22_10, M22_21, M22_26, M22_51, M22_52, M22_54, M22_55, M22_57, M22_69, M22_71, M22_83, M22_88, M22_94, M22_95, M22_FR, M23_44, M23_76, M24_69, M24_76, M29_01, M29_03, M29_07, M29_26, M29_38, M29_42, M29_63, M29_69, M29_73, M29_74, M29_83, M30_69, M33_14, M33_38, M33_69, M33_71, M33_FR, P1005_22, P1005_27, P1005_29, P1005_35, P1005_75 ; 9.3 s par couple (médiane), 32 min au total
2026-11-10 11:15:52  Rejeu sur le serveur : rouge — 1 couples identiques au PC sur 16 comparés ; en écart ou en échec : P1005_22, P1005_27, P1005_35, P1005_75, M01_75, M04_62, M07_59, M22_69, M29_69, M33_69, C093_69, C451_69, C451_FR, M22_FR, M01_FR ; 8.9 s par couple (médiane), 8 min au total
2026-11-10 11:22:29  observatoire (commande) : {"avis_ouverts": 7254, "sans_activite": 1363, "a_envoyer": 1500, "a_retirer": 37, "disparues": 37, "envoi": "envoyé", "paquets": 2, "donnees_personnelles_retirees": 0, "duree_s": 21.1}
2026-11-10 11:48:14  C093_69 republié : 3 opportunités, attributions anciennes retirées : None (5 s)
2026-11-10 11:48:19  C093_75 republié : 1 opportunités, attributions anciennes retirées : None (5 s)
2026-11-10 11:48:24  C451_01 republié : 1 opportunités, attributions anciennes retirées : None (5 s)
2026-11-10 11:48:27  C451_03 republié : 0 opportunités, attributions anciennes retirées : None (3 s)
2026-11-10 11:48:30  C451_07 republié : 0 opportunités, attributions anciennes retirées : None (3 s)
2026-11-10 11:48:35  C451_15 republié : 1 opportunités, attributions anciennes retirées : None (4 s)
2026-11-10 11:48:40  C451_21 republié : 0 opportunités, attributions anciennes retirées : None (5 s)
2026-11-10 11:48:46  C451_25 republié : 3 opportunités, attributions anciennes retirées : None (6 s)
2026-11-10 11:48:51  C451_26 republié : 0 opportunités, attributions anciennes retirées : None (5 s)
2026-11-10 11:48:59  C451_38 republié : 4 opportunités, attributions anciennes retirées : None (8 s)
2026-11-10 11:49:04  C451_39 republié : 1 opportunités, attributions anciennes retirées : None (5 s)
2026-11-10 11:49:10  C451_42 republié : 2 opportunités, attributions anciennes retirées : None (6 s)
2026-11-10 11:49:15  C451_43 republié : 0 opportunités, attributions anciennes retirées : None (5 s)
2026-11-10 11:49:20  C451_58 republié : 0 opportunités, attributions anciennes retirées : None (5 s)
2026-11-10 11:59:07  Contrôle du 10/11 : rouge — 235 couples identiques au site, 4238 attributions anciennes gardées par le site ; EN ÉCART : C093_69, C093_75, C451_01, C451_03, C451_07, C451_15, C451_21, C451_25, C451_26, C451_38, C451_39, C451_42, C451_43, C451_58 ; tâches à l'heure, site à jour ; CHUTES : C451_21 : attributions 585 → 270, C451_42 : attributions 1131 → 535
2026-11-10 13:50:59  Contrôle du 10/11 : vert — 249 couples identiques au site ; tâches à l'heure, site à jour
2026-11-10 13:59:11  Rejeu sur le serveur : écarts — 2 couples identiques aux envois du matin sur 6 comparés ; en écart ou en échec : P1005_75, M01_75, M07_59, C451_69 ; 8.9 s par couple (médiane), 1 min au total
```
