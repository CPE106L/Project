MAZE RUNNER

This project is made by Group 4.
The members of this group are as follows:
- Patricia Reann S. Cavalida
- Ray Daniel G. Giron
- Kyle Christian A. Estrellan

______

User Specifications:
This is a single player game with the main objective by simply solving the 
maze by starting at the point in the maze then going through a collection of 
paths then going to the end point of the maze in shortest time possible.

The rules of the game act as an initial specification of the problem.

- Only one user for each game can play.
- The game will be played by the generated maze created by the running code.
- Each player has a goal, which is to level up their ranks by earning wins.
- The ranks are consisted of Novice, Master and Legend, and will be 
based by the following number of wins: (1) Novice (0-17), (2) Legend 
(18-35) and lastly, Legend (36 and above).
- To win the game, the player must find the exit of the maze within the 
allotted time, which will also be traced in accordance with the ranking 
of the player. It is of note that as the ranking of the player is high, the 
allocated time will gradually be shortened. To be precise, Novice have
10 minutes, Master have 5 minutes and Legend have 3 minutes.
- In the game, the player will start in an area inside of the maze that will 
act as a starting point of the game.
- The player needs to navigate the generated maze by simply clicking or 
typing on where he intends to go.
- To finish the game the player needs to simply find the end point of the 
maze through navigating the collection of paths and through the finish 
line.
- If the allotted time has already passed and the player was not able to 
find the exit, this will be considered a loss. Otherwise, if the player was 
able to find the exit and finish the game, this will be regarded as a win.
- In any case, the player can choose to restart the game, otherwise to 
quit.
- From here, the database will consist of username, password, rank, wins, 
and loss of each player, which is either taken initially or by playing.
___________________________________________________________________________________

The identified nouns and verbs present in the specification are the demands 
to identify the concepts and objects of the program, in which are shown as 
follows:
- maze, quit, countdown, game, entrance, 
wins, timer, play, exit, loss, 
run, start, find, rank, player, 
quit, try, number, enter, user, 
username, password, help, generation, 
randomized, collection of paths
___________________________________________________________________________________

Relationships between Concepts:

- A game has one player inside a maze.
- A player must find the exit within the maze.
- A maze has one entrance and one exit.


![ds](https://user-images.githubusercontent.com/57428743/118364732-46c1e480-b5cc-11eb-9f3e-c0fac22096f0.png)

___________________________________________________________________________________

How To Play the Game using GitHub:

1. Open Command Prompt/Anaconda Prompt/Ubuntu.
2. Prompt 'git config --global user.name "Your GitHub username" and "git config --global user.email "Your e-mail"
3. Initialize the git
4. Copy the URL to clone the repository.
   - The URL can be seen in 'Code'.
6. Install pygame by using the command 'pip install pygame' or 'conda install -c cogsci pygame'
7. Prompt 'python main.py'

Enjoy the game!

![image](https://user-images.githubusercontent.com/57428743/118305426-87612580-b51a-11eb-954f-a586a6f7cecb.png)
___________________________________________________________________________________

ADDITIONAL NOTES:

- Users can have the same username and password.
- Users does not have to create login.db in order to run the file. Creation of login.db is automatic.
- Improvements will be added later on.
