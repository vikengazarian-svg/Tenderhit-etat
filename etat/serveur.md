# Serveur du moteur V2

Mis à jour le 21/10/2026 à 03:00 · publication : **EN SERVICE (publie sur le site)**

## 🟢 **Tout va bien**

| Passe | Dernier résultat |
|---|---|
| Demandes des clients | 2026-10-21 02:59:05  connexion OK, 0 couple(s) en attente : aucun |
| Collecte des appels d'offres | 2026-10-20 06:47:52  OK, 392 avis collectés, 93 couples recalculés, 30 republiés en 17.8 min |
| Passe DECP hebdomadaire | 2026-10-17 16:00:21  Passe hebdomadaire DECP 2026-10-17_decp : terminée en 69.6 min, mémoire max 0 Mo ; 92 couples recalculés, 2 bloqués par la garde (M22_05, M22_07) ; 88 couples publiés, tables d'aide publiées |
| Contrôle quotidien | 2026-10-20 06:49:02  Contrôle du 20/10 : rouge — 96 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : C451_42, C712_69, C712_74, C713_69, C713_74, C713_75, C713_FR, C715_69, C715_74, C772_42, M01_42, M01_71 ; demandes : dernière passe il y a 19 min (attendu : toutes les minutes) |

**Machine maintenant** : mémoire 0.49 Go sur 7.6 · charge 0.00 · disque 22.0 % · échange 0.0 Go

## Performances

![Durée des collectes](graphiques/collectes.svg)

![Temps par couple](graphiques/temps_couple.svg)

![Mémoire](graphiques/memoire.svg)

Les mesures d'avant la bascule viennent du PC ; celles d'après, du serveur.

### 10 dernières collectes

| Quand | Avis | Couples recalculés | Republiés | Échecs | Durée |
|---|---:|---:|---:|---:|---:|
| 20/10 06:47 | 392 | 93 | 30 | 0 | 17.8 min |
| 19/10 06:48 | 540 | 89 | 81 | 0 | 18.3 min |
| 17/10 12:47 | 1148 | 73 | 73 | 0 | 26.6 min |

### Passes DECP hebdomadaires

| Passe | Durée des couples | Mémoire max |
|---|---:|---:|
| 2026-10-17_decp | 41.8 min | — Mo |
| essai_pc | 26.3 min | 1616 Mo |
| essai_2026-10-16 | 26.4 min | 1950 Mo |
| essai_2026-10-16 | 25.6 min | 1950 Mo |
| essai_2026-10-16 | 23.9 min | 1950 Mo |
| essai_2026-10-16 | 21.9 min | 1950 Mo |

### Demandes des clients aujourd'hui

Aucune pour l'instant.

### Contrôles quotidiens (14 derniers)

```
2026-10-19 06:49  Contrôle du 19/10 : rouge — 96 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : C712_69, C712_74, C713_69, C713_74, C713_75, C713_FR, C715_69, C715_74 ; demandes : dernière passe il y a 19 min (attendu : toutes les minutes)
2026-10-20 06:49  Contrôle du 20/10 : rouge — 96 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : C451_42, C712_69, C712_74, C713_69, C713_74, C713_75, C713_FR, C715_69, C715_74, C772_42, M01_42, M01_71 ; demandes : dernière passe il y a 19 min (attendu : toutes les minutes)
```

## Tâches planifiées
```
NEXT                             LEFT LAST                          PASSED UNIT                     ACTIVATES
Wed 2026-10-21 06:30:00 CEST 3h 29min Tue 2026-10-20 06:30:04 CEST 20h ago tenderhit-collecte.timer tenderhit-collecte.service
Sat 2026-10-24 03:00:00 CEST   2 days Sun 2026-10-18 10:14:39 CEST       - tenderhit-hebdo.timer    tenderhit-hebdo.service
-                                   - Wed 2026-10-21 03:00:04 CEST  1s ago tenderhit-demandes.timer tenderhit-demandes.service
-                                   - Wed 2026-10-21 03:00:04 CEST  1s ago tenderhit-relais.timer   tenderhit-relais.service

4 timers listed.
```

## Fin du journal du moteur
```
2026-10-20 06:44:31    M22_16 : 1 opportunités · rapport et opportunités · 14 s
2026-10-20 06:44:45    M22_17 : 1 opportunités · rapport et opportunités · 14 s
2026-10-20 06:44:57    M22_21 : 0 opportunités · rapport et opportunités · 12 s
2026-10-20 06:45:10    M22_24 : 0 opportunités · rapport et opportunités · 14 s
2026-10-20 06:45:23    M22_27 : 0 opportunités · rapport et opportunités · 12 s
2026-10-20 06:45:29    M22_74 : 3 opportunités · rapport et opportunités · 7 s
2026-10-20 06:45:37    M22_75 : 22 opportunités · inchangé · 8 s
2026-10-20 06:45:50    M22_76 : 8 opportunités · inchangé · 13 s
2026-10-20 06:45:56    M22_83 : 6 opportunités · inchangé · 6 s
2026-10-20 06:46:10    M22_87 : 1 opportunités · rapport et opportunités · 14 s
2026-10-20 06:46:16    M22_92 : 16 opportunités · inchangé · 6 s
2026-10-20 06:46:22    M22_93 : 8 opportunités · inchangé · 6 s
2026-10-20 06:46:28    M22_94 : 11 opportunités · inchangé · 6 s
2026-10-20 06:46:33    M23_27 : 0 opportunités · inchangé · 5 s
2026-10-20 06:46:41    M23_44 : 3 opportunités · inchangé · 7 s
2026-10-20 06:46:48    M23_76 : 2 opportunités · inchangé · 7 s
2026-10-20 06:46:56    M24_69 : 2 opportunités · inchangé · 8 s
2026-10-20 06:47:04    M24_76 : 3 opportunités · rapport et opportunités · 8 s
2026-10-20 06:47:12    M30_69 : 2 opportunités · inchangé · 8 s
2026-10-20 06:47:20    M33_38 : 4 opportunités · rapport et opportunités · 7 s
2026-10-20 06:47:25    M33_42 : 1 opportunités · inchangé · 6 s
2026-10-20 06:47:34    M33_69 : 5 opportunités · inchangé · 9 s
2026-10-20 06:47:40    M33_71 : 0 opportunités · inchangé · 6 s
2026-10-20 06:47:46    M33_85 : 1 opportunités · inchangé · 6 s
2026-10-20 06:47:52    M40_76 : 1 opportunités · inchangé · 6 s
2026-10-20 06:47:52  OK, 392 avis collectés, 93 couples recalculés, 30 republiés en 17.8 min
2026-10-20 06:49:02  Contrôle du 20/10 : rouge — 96 couples identiques au site, 2 pas encore republiés par le V2, 124 attributions anciennes gardées par le site ; EN ÉCART : C451_42, C712_69, C712_74, C713_69, C713_74, C713_75, C713_FR, C715_69, C715_74, C772_42, M01_42, M01_71 ; demandes : dernière passe il y a 19 min (attendu : toutes les minutes)
2026-10-20 18:08:06  M33_27 : demande en attente
2026-10-20 18:08:14    publié (édition 2026-10, 1 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 8 s
2026-10-20 18:08:15  M33_76 : demande en attente
2026-10-20 18:08:24    publié (édition 2026-10, 5 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 9 s
2026-10-20 19:31:21  Rejeu sur le serveur : rouge — 2 couples identiques au PC sur 32 comparés ; en écart ou en échec : C451_38, C451_FR, C642_FR, C712_75, C712_84, C713_75, C713_FR, C772_FR, C794_FR, M01_14, M01_16, M01_24, M01_59, M01_75, M01_FR, M04_62, M07_59, M07_76, M08_76, M22_16, M22_17, M22_21, M22_24, M22_27, M22_74, M22_87, M24_76, M33_27, M33_38, M33_76 ; 10.7 s par couple (médiane), 11 min au total
2026-10-20 19:31:40  M33_76 republié : 11 opportunités, attributions anciennes retirées : None (9 s)
2026-10-20 23:11:07  M33_FR : demande en attente
2026-10-20 23:15:14    ÉCHEC 1/3 : dépôt du rapport : erreur 400 — Requête invalide · {"formErrors": [], "fieldErrors": {"echeances": ["Array must contain at most 2000 element(s)"]}}
2026-10-20 23:15:17  M33_FR : demande en attente
2026-10-20 23:19:23    ÉCHEC 2/3 : dépôt du rapport : erreur 400 — Requête invalide · {"formErrors": [], "fieldErrors": {"echeances": ["Array must contain at most 2000 element(s)"]}}
2026-10-20 23:19:27  M33_FR : demande en attente
2026-10-20 23:23:40    publié (édition 2026-10, 428 opportunités, 1 demande(s) livrée(s), attributions anciennes retirées : None) en 253 s
2026-10-20 23:23:44  débloqués (retentés à la prochaine passe) : aucun
```
