# Serveur du moteur V2

Mis à jour le 18/11/2026 à 03:00 · publication : **EN SERVICE (publie sur le site)**

## 🟢 **Tout va bien**

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-18 02:59:03  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-17 07:22:50  OK, 346 avis collectés, 306 couples recalculés, 114 republiés en 52.8 min |
| Passe DECP hebdomadaire | 2026-11-14 04:22:58  Passe hebdomadaire DECP 2026-11-14_decp : terminée en 82.9 min, mémoire max 4234 Mo ; 266 couples recalculés, 0 bloqués par la garde ; 260 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-17 07:26:53  Contrôle du 17/11 : vert — 318 couples identiques au site ; tâches à l'heure, site à jour |

**Machine maintenant** : mémoire 0.5 Go sur 7.6 · charge 0.00 · disque 37.2 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : +2.5 point(s) par semaine · 80 % dans **17.1 semaine(s)**

```
Mesure du 2026-11-17 05:45 :
  entrepot/sources                            3.53 Go
  entrepot/decp                               2.02 Go
  entrepot/boamp                              1.39 Go
  entrepot/passes                             1.19 Go
  production/controles                        0.69 Go
  entrepot/execution                          0.68 Go
  entrepot/marche                             0.26 Go
  entrepot/photographie                       0.23 Go
  production/publies                          0.22 Go
  entrepot/etiquettes                           38 Mo
  entrepot/referentiel                          16 Mo
  entrepot/avis                                  3 Mo
  logs                                           3 Mo
  entrepot/sirene                                2 Mo
  production/(fichiers)                          2 Mo
  entrepot/tmp                                   2 Mo
  entrepot/mesures.jsonl                         1 Mo
  production/rejeu                               0 Mo
  entrepot/sources_temoin.jsonl                  0 Mo
  entrepot/manifeste.json                        0 Mo
Croissance par dossier (depuis 2026-11-09, 8.0 j), en Go par semaine :
  entrepot/decp                                 +0.37
  entrepot/passes                               +0.26
  entrepot/sources                              +0.03
  production/controles                          +0.02
  entrepot/boamp                                +0.01
Dernière purge (2026-11-17 05:45) : faite, 2 élément(s), 0.23 Go libérés · fusions 1 (0.0 Go) · photographies_controle 1 (0.23 Go)
```

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 17/11 07:22 | 346 | 306 | 114 | 0 | 52.8 min |
| 16/11 07:19 | 306 | 270 | 61 | 0 | 49.6 min |
| 15/11 07:19 | 430 | 266 | 59 | 0 | 49.1 min |
| 14/11 07:27 | 335 | 266 | 49 | 0 | 48.7 min |
| 13/11 07:17 | 471 | 260 | 60 | 0 | 47.9 min |
| 12/11 07:16 | 433 | 249 | 38 | 0 | 46.8 min |
| 11/11 07:18 | 647 | 249 | 176 | 0 | 48.8 min |
| 10/11 07:18 | 343 | 241 | 89 | 0 | 48.4 min |
| 09/11 07:16 | 305 | 236 | 59 | 0 | 46.0 min |
| 08/11 07:16 | 673 | 233 | 90 | 0 | 46.0 min |

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

Aucune pour l'instant.

### Contrôles quotidiens (14 derniers)

```
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
2026-11-16 07:23  Contrôle du 16/11 : vert — 276 couples identiques au site ; tâches à l'heure, site à jour
2026-11-17 07:26  Contrôle du 17/11 : vert — 318 couples identiques au site ; tâches à l'heure, site à jour
```

## Tâches planifiées
```
NEXT                            LEFT LAST                         PASSED UNIT                     ACTIVATES
Wed 2026-11-18 05:45:00 CET 2h 44min Tue 2026-11-17 05:45:00 CET 21h ago tenderhit-purge.timer    tenderhit-purge.service
Wed 2026-11-18 06:30:00 CET 3h 29min Tue 2026-11-17 06:30:00 CET 20h ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-11-21 03:00:00 CET   2 days Sat 2026-11-14 03:00:04 CET       - tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                  - Wed 2026-11-18 03:00:00 CET  1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                  - Wed 2026-11-18 03:00:00 CET  1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-17 07:13:33    M29_69 : 0 opportunités · rapport et opportunités · 7 s
2026-11-17 07:13:48    M29_73 : 0 opportunités · rapport et opportunités · 16 s
2026-11-17 07:14:05    M29_74 : 0 opportunités · rapport et opportunités · 16 s
2026-11-17 07:14:18    M29_83 : 1 opportunités · rapport et opportunités · 13 s
2026-11-17 07:14:38    M29_93 : 1 opportunités · rapport et opportunités · 20 s
2026-11-17 07:14:47    M30_69 : 13 opportunités · rapport et opportunités · 10 s
2026-11-17 07:14:50    M33_01 : 6 opportunités · inchangé · 3 s
2026-11-17 07:14:58    M33_14 : 7 opportunités · rapport et opportunités · 8 s
2026-11-17 07:15:05    M33_27 : 6 opportunités · rapport et opportunités · 7 s
2026-11-17 07:15:13    M33_38 : 5 opportunités · rapport et opportunités · 8 s
2026-11-17 07:15:19    M33_42 : 0 opportunités · inchangé · 6 s
2026-11-17 07:15:26    M33_50 : 3 opportunités · rapport et opportunités · 7 s
2026-11-17 07:15:32    M33_61 : 3 opportunités · inchangé · 5 s
2026-11-17 07:15:42    M33_69 : 14 opportunités · rapport et opportunités · 11 s
2026-11-17 07:15:49    M33_71 : 9 opportunités · rapport et opportunités · 7 s
2026-11-17 07:15:58    M33_76 : 8 opportunités · rapport et opportunités · 8 s
2026-11-17 07:16:05    M33_85 : 3 opportunités · inchangé · 7 s
2026-11-17 07:20:17    M33_FR : 483 opportunités · rapport et opportunités · 252 s
2026-11-17 07:20:27    M40_05 : 0 opportunités · rapport et opportunités · 11 s
2026-11-17 07:20:34    M40_76 : 0 opportunités · rapport et opportunités · 7 s
2026-11-17 07:20:43    P1005_14 : 2 opportunités · inchangé · 9 s
2026-11-17 07:20:52    P1005_22 : 8 opportunités · inchangé · 8 s
2026-11-17 07:20:59    P1005_27 : 2 opportunités · inchangé · 8 s
2026-11-17 07:21:09    P1005_29 : 9 opportunités · rapport et opportunités · 10 s
2026-11-17 07:21:20    P1005_35 : 19 opportunités · inchangé · 11 s
2026-11-17 07:21:30    P1005_56 : 9 opportunités · rapport et opportunités · 10 s
2026-11-17 07:21:46    P1005_59 : 19 opportunités · rapport et opportunités · 16 s
2026-11-17 07:21:55    P1005_60 : 2 opportunités · inchangé · 9 s
2026-11-17 07:22:19    P1005_75 : 36 opportunités · rapport et opportunités · 24 s
2026-11-17 07:22:29    P1005_76 : 6 opportunités · inchangé · 11 s
2026-11-17 07:22:38    P1005_80 : 0 opportunités · inchangé · 8 s
2026-11-17 07:22:50    P1005_93 : 10 opportunités · inchangé · 12 s
2026-11-17 07:22:50  OK, 346 avis collectés, 306 couples recalculés, 114 republiés en 52.8 min
2026-11-17 07:26:53  Contrôle du 17/11 : vert — 318 couples identiques au site ; tâches à l'heure, site à jour
2026-11-17 18:10:38  Rejeu sur le serveur : vert — 3 couples identiques aux envois du matin sur 3 comparés ; 7.5 s par couple (médiane), 1 min au total
2026-11-17 18:14:29  observatoire (commande) : {"avis_ouverts": 8079, "sans_activite": 1490, "a_envoyer": 8079, "a_retirer": 293, "disparues": 293, "compteurs": {"ao_ouverts": 8079, "avis_ouverts": 10285, "lots_ouverts": 22815}, "autres_sources": 1694, "fusion": "2026-11-17", "duree_tri_autres_s": 8.2, "autres_sans_activite": 255, "redirections": 0, "envoi": "essai, rien n'est envoyé", "duree_s": 24.9}
2026-11-17 18:46:38  observatoire (commande) : {"avis_ouverts": 8078, "sans_activite": 1490, "a_envoyer": 8078, "a_retirer": 294, "disparues": 294, "compteurs": {"ao_ouverts": 8078, "avis_ouverts": 10284, "lots_ouverts": 22814}, "autres_sources": 1694, "fusion": "2026-11-17", "duree_tri_autres_s": 8.0, "autres_sans_activite": 255, "redirections": 0, "envoi": "envoyé", "paquets": 9, "donnees_personnelles_retirees": 0, "duree_s": 33.9}
2026-11-17 19:05:05  M37_13 : demande en attente
2026-11-17 19:05:23    publié (édition 2026-11, 16 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : 0) en 18 s
2026-11-17 19:06:00  tables du marché : 1 activité(s) envoyée(s), 0 inchangée(s), 113466 lignes en 25 paquets
```
