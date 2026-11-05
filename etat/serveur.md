# Serveur du moteur V2

Mis à jour le 05/11/2026 à 14:34 · publication : **EN SERVICE (publie sur le site)**

## 🔴 **À regarder** : contrôle quotidien rouge

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-11-05 14:30:08  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-11-05 07:12:21  OK, 770 avis collectés, 223 couples recalculés, 65 republiés en 42.3 min |
| Passe DECP hebdomadaire | 2026-11-03 16:10:45  Passe hebdomadaire DECP 2026-10-31_decp : terminée en 102.1 min, mémoire max 5747 Mo ; 219 couples recalculés, 0 bloqués par la garde ; 215 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-11-05 11:03:03  Contrôle du 05/11 : rouge — photographie du site impossible ou incomplète |

**Machine maintenant** : mémoire 0.58 Go sur 7.6 · charge 0.62 · disque 39.1 % · échange 0.0 Go

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
NEXT                             LEFT LAST                              PASSED UNIT                     ACTIVATES
Fri 2026-11-06 06:30:00 CET       15h Thu 2026-11-05 06:30:04 CET       8h ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-11-07 03:00:00 CET 1 day 12h Sat 2026-10-31 03:00:04 CET   5 days ago tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                   - Thu 2026-11-05 14:34:00 CET       3s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                   - Thu 2026-11-05 14:30:04 CET 3min 59s ago tenderhit-relais.timer   tenderhit-relais.service

4 timers listed.
```

## Fin du journal du moteur
```
2026-11-05 07:03:35    M24_69 : 8 opportunités · rapport et opportunités · 10 s
2026-11-05 07:03:43    M24_76 : 10 opportunités · inchangé · 8 s
2026-11-05 07:03:53    M30_69 : 13 opportunités · rapport et opportunités · 10 s
2026-11-05 07:03:56    M33_01 : 3 opportunités · inchangé · 3 s
2026-11-05 07:04:03    M33_14 : 6 opportunités · inchangé · 7 s
2026-11-05 07:04:10    M33_27 : 3 opportunités · inchangé · 6 s
2026-11-05 07:04:17    M33_38 : 9 opportunités · inchangé · 7 s
2026-11-05 07:04:23    M33_42 : 1 opportunités · inchangé · 6 s
2026-11-05 07:04:30    M33_50 : 4 opportunités · inchangé · 7 s
2026-11-05 07:04:35    M33_61 : 2 opportunités · inchangé · 6 s
2026-11-05 07:04:47    M33_69 : 16 opportunités · rapport et opportunités · 11 s
2026-11-05 07:04:53    M33_71 : 9 opportunités · inchangé · 6 s
2026-11-05 07:05:01    M33_76 : 16 opportunités · inchangé · 8 s
2026-11-05 07:05:08    M33_85 : 4 opportunités · inchangé · 7 s
2026-11-05 07:09:43    M33_FR : 571 opportunités · rapport et opportunités · 275 s
2026-11-05 07:09:53    M40_05 : 0 opportunités · inchangé · 10 s
2026-11-05 07:10:00    M40_76 : 2 opportunités · inchangé · 6 s
2026-11-05 07:10:09    P1005_14 : 0 opportunités · inchangé · 9 s
2026-11-05 07:10:17    P1005_22 : 9 opportunités · inchangé · 9 s
2026-11-05 07:10:25    P1005_27 : 4 opportunités · inchangé · 8 s
2026-11-05 07:10:34    P1005_29 : 15 opportunités · inchangé · 9 s
2026-11-05 07:10:47    P1005_35 : 20 opportunités · rapport et opportunités · 13 s
2026-11-05 07:10:57    P1005_56 : 13 opportunités · rapport et opportunités · 10 s
2026-11-05 07:11:14    P1005_59 : 21 opportunités · rapport et opportunités · 17 s
2026-11-05 07:11:23    P1005_60 : 3 opportunités · inchangé · 9 s
2026-11-05 07:11:48    P1005_75 : 44 opportunités · rapport et opportunités · 25 s
2026-11-05 07:11:59    P1005_76 : 7 opportunités · inchangé · 11 s
2026-11-05 07:12:08    P1005_80 : 0 opportunités · inchangé · 9 s
2026-11-05 07:12:21    P1005_93 : 13 opportunités · inchangé · 13 s
2026-11-05 07:12:21  OK, 770 avis collectés, 223 couples recalculés, 65 republiés en 42.3 min
2026-11-05 07:15:46  Contrôle du 05/11 : rouge — photographie du site impossible ou incomplète
2026-11-05 11:03:03  Contrôle du 05/11 : rouge — photographie du site impossible ou incomplète
2026-11-05 12:38:55  tables du marché calculées : 328 activités, 1915144 attributions en 166.1 s, mémoire max 3676 Mo
2026-11-05 13:53:31  tables du marché : 7 activité(s) envoyée(s), 320 inchangée(s), 354911 lignes en 82 paquets
2026-11-05 14:10:24  tables du marché : 1 activité(s) envoyée(s), 0 inchangée(s), 12442 lignes en 4 paquets
2026-11-05 14:27:53  SIRENE : 153268 entreprises et 198793 établissements titulaires extraits (85.4 s)
2026-11-05 14:33:03  SIRENE : fichiers du mois déjà présents, pas de téléchargement
2026-11-05 14:33:18  SIRENE : contrôle impossible (CatalogException)
2026-11-05 14:33:19  tables du marché calculées : 328 activités, 1915144 attributions en 169.6 s, mémoire max 4119 Mo
2026-11-05 14:33:57  tables du marché : 1 activité(s) envoyée(s), 0 inchangée(s), 12442 lignes en 4 paquets
```
