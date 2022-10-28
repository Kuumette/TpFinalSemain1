1 - A l’aide d’internet, expliquer ce qu’est « crontab ».
Crontab est un outil qui permet de lancer des applications de façon régulière, pratique pour un serveur pour y lancer des scripts de sauvegardes, etc.

2 - Modifier la ligne suivante pour que le script se lance tous les derniers jours de l’année, à 8h du
matin :

```bash
00 08 * * *  /bin/sauvegarde.sh’
```

```bash
#!/bin/bash
ListeDesBDD=$( echo 'show databases' | mysql -u backup --password=< votre mdp >) # Connexion à la base de donnée

for BDD in $ListeDesBDD do # Boucle qui vas parcourrire tout la base de donnée ligne par ligne
    if [[ $BDD != "information_schema" ]] && [[ $BDD != "mysql" ]] && [[ $BDD != "Database" ]]; # Si la ligne n'est pas egale à "information_schema" et à "mysql" et à "Database" alors
    then
        CHEMIN=/home/user/backupBDD/$BDD # Variable du chemain
        mysqldump -u backup --single-transaction --password= $BDD > "$CHEMIN/$BDD.sql" # faire un dump (sauvegarde ) de la base de donnée vers le chemain de la variable chemin/nomDeLaBase.sql
        echo "|La base de données suivante a été sauvegardée : $BDD.sql ";
    fi # fin if
done # Fin for
```
