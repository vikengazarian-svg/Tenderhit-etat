# Serveur du moteur V2

Mis à jour le 06/11/2026 à 07:00 · publication : **EN SERVICE (publie sur le site)**

## 🔴 **À regarder** : demandes des clients non traitées depuis plus de 15 min ; disque à 80 % dans 5.0 semaine(s) au rythme des 14 derniers jours

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-06 06:29:01  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-05 07:12:21  OK, 770 avis collectés, 223 couples recalculés, 65 republiés en 42.3 min |
| Passe DECP hebdomadaire | 2026-11-03 16:10:45  Passe hebdomadaire DECP 2026-10-31_decp : terminée en 102.1 min, mémoire max 5747 Mo ; 219 couples recalculés, 0 bloqués par la garde ; 215 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-05 11:03:03  Contrôle du 05/11 : rouge — photographie du site impossible ou incomplète |

**Machine maintenant** : mémoire 2.07 Go sur 7.6 · charge 1.74 · disque 39.2 % · échange 0.0 Go

## Disque

Rythme des 14 derniers jours : +8.1 point(s) par semaine · 80 % dans **5.0 semaine(s)**

```
Mesure du 2026-11-06 05:45 :
  entrepot/sources                            3.50 Go
  production/controles                        2.86 Go
  entrepot/boamp                              1.38 Go
  entrepot/decp                               1.19 Go
  entrepot/execution                          0.66 Go
  parallele                                   0.66 Go
  entrepot/passes                             0.58 Go
  entrepot/marche                             0.26 Go
  entrepot/photographie                       0.23 Go
  production/publies                          0.22 Go
  entrepot/etiquettes                           37 Mo
  entrepot/referentiel                          16 Mo
  entrepot/avis                                  4 Mo
  entrepot/tmp                                   3 Mo
  entrepot/sirene                                2 Mo
  production/(fichiers)                          2 Mo
  logs                                           2 Mo
  entrepot/mesures.jsonl                         1 Mo
  production/rejeu                               0 Mo
  entrepot/sources_temoin.jsonl                  0 Mo
Dernière purge (2026-11-06 05:45) : à blanc, 24 élément(s), 2.16 Go libérables · fusions 6 (0.01 Go) · photographies_controle 16 (2.15 Go) · tmp 2 (0.0 Go)
```

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 05/11 07:12 | 770 | 223 | 65 | 0 | 42.3 min |
| 04/11 07:11 | 599 | 220 | 66 | 0 | 41.9 min |
| 03/11 07:09 | 315 | 219 | 79 | 0 | 39.6 min |
| 02/11 07:10 | 251 | 219 | 42 | 0 | 40.9 min |
| 01/11 07:13 | 543 | 219 | 219 | 0 | 43.6 min |
| 31/10 07:17 | 410 | 213 | 44 | 0 | 47.0 min |
| 30/10 07:07 | 695 | 172 | 55 | 0 | 37.1 min |
| 29/10 07:07 | 704 | 172 | 51 | 1 | 37.9 min |
| 28/10 07:09 | 640 | 166 | 62 | 0 | 39.0 min |
| 27/10 07:08 | 351 | 161 | 63 | 0 | 38.3 min |

### Passes DECP hebdomadaires

| Passe | Durée des couples | Mémoire max |
|---|---:|---:|
| 2026-10-31_decp | 53.2 min | 2538 Mo |
| 2026-10-24_decp | 33.0 min | 2373 Mo |
| 2026-10-17_decp | 41.8 min | — Mo |
| essai_pc | 26.3 min | 1616 Mo |
| essai_2026-10-16 | 26.4 min | 1950 Mo |
| essai_2026-10-16 | 25.6 min | 1950 Mo |

### Demandes des clients aujourd'hui

Aucune pour l'instant.

### Contrôles quotidiens (14 derniers)

```
2026-10-25 07:08  Contrôle du 25/10 : vert — 160 couples identiques au site ; tâches à l'heure, site à jour
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
```

## Tâches planifiées
```
NEXT                        LEFT LAST                              PASSED UNIT                     ACTIVATES
Fri 2026-11-06 07:01:00 CET  58s Fri 2026-11-06 07:00:00 CET       1s ago tenderhit-demandes.timer tenderhit-demandes.service
Sat 2026-11-07 03:00:00 CET  19h Sat 2026-10-31 03:00:04 CET   6 days ago tenderhit-hebdo.timer    tenderhit-hebdo.service
Sat 2026-11-07 05:45:00 CET  22h Fri 2026-11-06 05:45:04 CET 1h 14min ago tenderhit-purge.timer    tenderhit-purge.service
-                              - Fri 2026-11-06 06:30:04 CET    29min ago tenderhit-collecte.timer tenderhit-collecte.service
-                              - Fri 2026-11-06 07:00:00 CET       1s ago tenderhit-relais.timer   tenderhit-relais.service

5 timers listed.
```

## Fin du journal du moteur
```
2026-11-06 06:52:16    M01_63 : 8 opportunités · inchangé · 5 s
2026-11-06 06:52:25    M01_69 : 40 opportunités · opportunités · 9 s
2026-11-06 06:52:36    M01_70 : 2 opportunités · inchangé · 11 s
2026-11-06 06:52:41    M01_71 : 7 opportunités · inchangé · 5 s
2026-11-06 06:52:46    M01_73 : 11 opportunités · inchangé · 6 s
2026-11-06 06:52:52    M01_74 : 21 opportunités · inchangé · 6 s
2026-11-06 06:53:09    M01_75 : 66 opportunités · rapport et opportunités · 16 s
2026-11-06 06:53:16    M01_76 : 19 opportunités · inchangé · 7 s
2026-11-06 06:53:24    M01_83 : 21 opportunités · inchangé · 8 s
2026-11-06 06:53:29    M01_89 : 7 opportunités · inchangé · 5 s
2026-11-06 06:53:39    M01_90 : 2 opportunités · inchangé · 10 s
2026-11-06 06:53:48    M01_92 : 19 opportunités · inchangé · 9 s
2026-11-06 06:53:56    M01_93 : 26 opportunités · inchangé · 8 s
2026-11-06 06:54:04    M01_94 : 15 opportunités · inchangé · 8 s
2026-11-06 06:55:37    M01_FR : 1226 opportunités · rapport et opportunités · 93 s
2026-11-06 06:55:44    M03_76 : 7 opportunités · inchangé · 8 s
2026-11-06 06:55:54    M04_62 : 14 opportunités · rapport et opportunités · 10 s
2026-11-06 06:55:58    M04_76 : 6 opportunités · inchangé · 4 s
2026-11-06 06:56:06    M07_59 : 44 opportunités · rapport et opportunités · 8 s
2026-11-06 06:56:12    M07_76 : 18 opportunités · inchangé · 6 s
2026-11-06 06:56:16    M08_76 : 19 opportunités · inchangé · 4 s
2026-11-06 06:56:25    M08_81 : 0 opportunités · rapport et opportunités · 9 s
2026-11-06 06:56:27    M22_01 : 0 opportunités · inchangé · 2 s
2026-11-06 06:56:38    M22_05 : 0 opportunités · rapport et opportunités · 11 s
2026-11-06 06:56:54    M22_07 : 1 opportunités · rapport et opportunités · 16 s
2026-11-06 06:57:09    M22_11 : 0 opportunités · rapport et opportunités · 16 s
2026-11-06 06:57:22    M22_14 : 2 opportunités · inchangé · 13 s
2026-11-06 06:57:37    M22_16 : 0 opportunités · rapport et opportunités · 15 s
2026-11-06 06:57:52    M22_17 : 0 opportunités · rapport et opportunités · 15 s
2026-11-06 06:58:05    M22_21 : 2 opportunités · inchangé · 12 s
2026-11-06 06:58:20    M22_24 : 0 opportunités · rapport et opportunités · 15 s
2026-11-06 06:58:38    M22_26 : 0 opportunités · rapport et opportunités · 18 s
2026-11-06 06:58:51    M22_27 : 1 opportunités · inchangé · 13 s
2026-11-06 06:59:02    M22_37 : 0 opportunités · inchangé · 11 s
2026-11-06 06:59:10    M22_38 : 6 opportunités · rapport et opportunités · 8 s
2026-11-06 06:59:16    M22_42 : 1 opportunités · inchangé · 6 s
2026-11-06 06:59:30    M22_60 : 0 opportunités · rapport et opportunités · 14 s
2026-11-06 06:59:39    M22_69 : 8 opportunités · rapport et opportunités · 9 s
2026-11-06 06:59:51    M22_71 : 2 opportunités · inchangé · 12 s
2026-11-06 06:59:59    M22_74 : 5 opportunités · rapport et opportunités · 7 s
```
