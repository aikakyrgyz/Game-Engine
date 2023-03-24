TGME game for "Women in Tech" Group AKA Group 11. The following README contains the instructions needed to run the game engine.

As this project uses a database, there are two ways to run the game after cloning the repository.
- With SQL.
- Without SQL.

To run with SQL, as intended:
1. A database will need to be set-up on your computer. MySQL Workbench 8.0 CE was used to ease the process of setting
up the database while MySQL Shell was used to query and test syntax. A password of 'wit122' (can also be seen in the
code under the database folder) was set for the database, but no other settings were changed. Only two tables were
created, but one ended up not being used in our final version of the code (the games schema was intended to pass the 
list of games dynamically through the GUI, but we were having issues with GUI display). An idea of the set-up is
provided in the images below:
<p align="center">
  <img src="https://i.imgur.com/E2UulYF.png">
</p>

2. After the database is installed, the following two syntax can be run to create the tables needed.

- CREATE TABLE players (Playerid int AUTO_INCREMENT, Username varchar(255) NOT NULL UNIQUE, Dmscore int, Puyoscore int, Totalscore int, PRIMARY KEY (Playerid));
- CREATE TABLE games (Gameid int AUTO_INCREMENT, Gamename varchar(255) NOT NULL UNIQUE, PRIMARY KEY (Gameid));

  The game can then be started from the file "mainmenu.py" under the "interface" directory. Unfortunately, 
  the scoreboard menu is programmed to work if the Players table has more than five entries in it. 
  This code is commented out in this final version, but can be found on lines 129, 152, and 159. They can be
  used if the Players table has more than five entries in it.

3. A choice of a game can be selected by clicking the "Play Game < [Game Name] >" button. The "Profile" menu allows one
to enter a pre-existing username already registered into the system. Once entered, the scores for the player will be
dynamically displayed along with the option to change the username (updated in the database). If the username does not
exist, then nothing will happen.

4. After choosing a game, the GUI moves on to the "Register Players" menu. Here, there are two text buttons available
to receive user input. If only one name is entered, then the chosen game begins in 1P mode. When the game ends in 1P 
mode, the user's score is recorded in the database and the GUI exits.

5. If two names are entered, then the game begins in 2P mode. The first player plays and when the game reaches its end,
the first player's score is entered in the database. Afterwards, the second player must press enter to begin their
turn. Their score is also entered into the database after game completion. Finally, both players' scores are pulled
from the database to compare who the winner is. This will be stated in the terminal itself.

If no SQL:

It is recommended to run the games directly from their files as the GUI is explicitly setup to work with a database as
well as allow 1P/2P mode.
This can be found in the following two respective files.

Run individual games by accessing the corresponding files listed:

Dr. Mario:
- drmario/dmgameplay.py

Puyo Puyo:
- puyopuyo/puyogameplay.py

Run the app through the following file: 
- app.py

Additionally, if the GUI is not working, the game can still be seen and played from the terminal itself.
