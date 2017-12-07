# Fundamentals of Computing Specialization assignments
The assignments in the Fundamentals of Computing Specialization offered by Rice University (Coursera platform) are solved and given here. The specialization has 7 courses including 1 Capstone project. Courses and the corresponding mini-projects are organized in different folders here.

## Course1 : Interactive Programming in Python (Part1)
### RPSLS.py
This is the implementation of the hand game rock-Spock-paper-lizard-scissors usually played by 2 players. Each of the Players get to choose one of these 5 names. When they disclose their choice, the player who happened to choose the dominant one of the two choices wins the game. The dominant one in any pair can be determined based on the following set of rules.

* scissors cuts paper
* scissors decapitates lizard
* paper covers rock
* paper disproves Spock
* rock crushes lizard
* rock crushes scissors
* lizard poisons Spock
* lizard eats paper
* Spock smashes scissors
* Spock vaporizes rock

It is clear that each of the 5 choices wins against two other choices and loses to two other choices. So, if Player1 chooses Spock and Player2 chooses paper,  Player2 wins as paper wins over Spock (paper disproves Spock )

### RPSLS_GUI.py
This is the interactive Graphical Use Interface for the rock-Spock-paper-lizard-scissors game.

### Guess_the_number.py

Guess_the_number.py implements a two player game using a Graphical User Interface. First player (here, the computer) thinks of a secret number and the second player(yourself)  has to guess this number correctly, in 7 attempts or in 10 attempts based on whether the computer's secret number is in the range of (0-100) or of (0-1000) respectively (both the ranges are upper-bound exclusive). After each attempt, the first player has to respond whether his secret number is higher/lower than the current guess if not correct.

### dollar_cent.py

In this simple interactive program, when an amount is entered as a digit, the program will print on canvas, this amount as number of dollars and cents. 

eg.,
* input = 54.56
* output = 54 dollars and 56 cents


