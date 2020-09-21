# League of Legends Recommender
Create a recommender that take users last played champions and recommends new ones to play. (in progress)

## The Data
This project has three main datasets; the Champion information, User Names, and User Data. The Champion data was available through RIOT Games, the user names was collected through the RIOT API using match id's from a dataset of the 2020 NA Ranked games. I chose to only look at ranked users for my recommender as to try and limit the number of new users that may have less information. Once the User Names were collected (about 1 million) the data on the users were scraped through na.op.gg and put into a User Data data set.

## Research

### Quick Overview of the game
League of Legends is a online team based game, with five players on each team the goal is to get to the other teams base and destroy the bases' Nexus during each match. Each player chooses from 150 diffrent Champions to play and typically chooses a position to play, these postions indicate where on the map they should be placed and what they should be doing. The bases provide minions that will attack the other players, their turrets, minions and nexus; the bases also allow a player to buy items that will help them during the game. Players can gain gold to buy items by killing other players, their minions and turrets. Games typically last 25-40 mins and about 80 million people play the game world wide.

### Features
Because I had never played this game before a lot of reseach was required to understand how it worked and what went into a user picking a champion.

During my research of this game I found that the best way to be able to make accurate recommendations using a User-User recommender would be to look at the type of character a User was playing. There are class tags associated with each champion in the dataset (Tank, Fighter, Mage, Assassin, Support, Marksman), while what lane a user plays does affect the type of champion they would play, this is not always the case and the best way to make a good recommendation is to primarily base the recommender on these characteristics and how it is to be evaluated. The class of a chmpion also affects the items

## EDA


## Recommenders and Results

Two recommenders were tested both where User-User based, one looked at similarites in the champions played while another looked at the class type the user played along with stats on the player (Kill, Death, Assist and Win Rate). Because there are so many chmpions the class type of the recommended and original were evaluted to see if simialr classes were recommended rather than trying to use a (not sure whats it called when I try to predict a champion I not). Below is the scores for each recommender tested. Because of the computing power required to run these recommenders only

## Next Steps

Next Steps would be to create a filtering function that could filter out champions based on the difficulty of that champion to play and taking into account what percentage of games and the win rate were played with each charater.

Continuing on this project next would be to make a web app that could pull data on a user from there summoner name and recommend Champions to try out and play. Along with the recommendations would be to ask Users to rate how well they believe the recommender works. During my research I found that Champion selection is biased and varies from user to user, to get a better sence of how well the recommender works would be to ask the User.
