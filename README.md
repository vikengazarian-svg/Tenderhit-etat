# Tenderhit — état du serveur du moteur V2 et commandes

Dépôt de relais entre le serveur OVH du moteur V2 et Claude (option 1, décidée par Viken le 17/10/2026). Le serveur
n'accepte aucune connexion entrante à part celle de Viken. Toutes les 2 minutes, il récupère ce dépôt avec sa propre
clé de déploiement, exécute les commandes autorisées et y dépose ses comptes rendus.

- `commandes/<nom>.txt` : une commande par fichier, déposée par Claude ou Viken ;
- `resultats/<nom>.txt` : la réponse du serveur ;
- `etat/serveur.md` : l'état du serveur, mis à jour chaque heure et après chaque commande.

Commandes autorisées (toute autre est refusée) : `etat`, `controle`, `diagnostic`, `journal [lignes]`,
`rejouer [couples]`, `publier <couples>`, `collecte`, `mettre_a_jour`.
Aucun secret ni donnée de client dans ce dépôt. Code du relais : `serveur/relais.py` du dépôt tenderhit-moteur.
