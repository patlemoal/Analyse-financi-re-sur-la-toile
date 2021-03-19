# Analyse financière sur la toile

```
objectif : Apprendre à utiliser un outil de web scraping pour récolter des données et les stocker en bdd.
```

# Choix des données et des outils :

dataset : https://www.nasdaq.com/market-activity/stocks/aapl/historical => cours des actions apple sur 1 an 

scrapping : selenium

bdd : mysql 

visualisation des données : grafana

utilisation de docker 

Visualisation des données : 

![image](pagewebscrappée.PNG)

# Construction d'un notebook pour extraire les données .

Le "scapper" choisi l'année dans la page web, et ensuite sélectionne toutes les données en passant d'une page à l'autre.
On injecte les données dans un tableau panda que l'on transforme en csv.
![image](extraction.PNG)



# Base de données:
On importe le fichier CSV dans mysql en intégrant les formats qui nous servirons pour la suite de notre étude.
![image](mamp.PNG)


#Mise en place des containers dans l'invite de commande 

![image](dockercompose.PNG)


# Docker

![image](docker.PNG)

# Visualisation des données sous grafana.
![image](GRAFGRAPHANA.PNG)




