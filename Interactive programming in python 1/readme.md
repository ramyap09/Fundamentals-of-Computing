
All the following codes give the Graphical User Interface (GUI) implementation making use of the Tkinter package.

### Guess_the_number.py

Guess_the_number.py implements a two player game using a Graphical User Interface. First player (here, the computer) thinks of a secret number and the second player(yourself)  has to guess this number correctly, in 7 attempts or in 10 attempts based on whether the computer's secret number is in the range of (0-100) or of (0-1000) respectively (both the ranges are upper-bound exclusive). After each attempt, the first player has to respond whether his secret number is higher/lower than the current guess if not correct.

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

### circle_radius_button.py

This implements a GUI which pictures a circle and two buttons to change the radius (increase/decrease) of the circle interactively.


### circle_radius_key.py

This implements a GUI which pictures a circle, whose radius can be increased or decreased interactively by pressing the Up arrow key
and Down arrow key of the keyboard respectively.

### colorToggler_button.py

This simple code implements a GUI, the background colour of the canvas on it can be toggled between 'White' and "Red" by pressing the button provided.


### colorToggler_timer.py

This simple code implements one GUI, the background colour of the canvas on it toggles between "Red" and "Green" in fixed time intervals.


### dollar_cent.py

In this simple interactive program, when an amount is entered as a digit, the program will print on canvas, this amount as number of dollars and cents. 

eg.,
* input = 54.56
* output = 54 dollars and 56 cents

### pong.py

This is the implementation of the classic arcade video game 'pong' whch is an electronic tennis game played by two players. Both the players move their respective paddles to strike the ball, and when one player misses the strike the other player scores the point.

### screen_saver.py

This is the implementation of a simple screen saver with a custom message, which you can choose to change usng the entry box and button provided in the GUI.

### stopwatch.py

This is the implementation of a stopwatch
