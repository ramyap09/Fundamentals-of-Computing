"""
Implementation of classic arcade video game "Pong". Game starts once the spacebar is pressed.
"""

from tkinter import *
import random

window = Tk()
window.title("Pong : The game")

def ball_move():
    """
    This function executes the ball movement (both position and velocity control)
    with ball reflecting from the top and bottom walls, and also from the paddles.
    """
    global x1, y1, dx, dy, ball_diameter, c_height, c_width, play_status, player, player1_score, player2_score
    if play_status == 1:
        x1 = x1 + dx
        y1 = y1 + dy
        print(x1,y1)
        print("game on")

        if y1 <=0 or y1 >= c_height - ball_diameter :
            dy = -1 * (dy) * 1.2

        if x1 <= (0+20):
            if y1 >= p1_h1 and y1 <= p1_h1+p_height :
                print("Bounced from left paddle")
                dx = -1 * (dx) * 1.2
            else:
                x1 = c_width - (ball_diameter+20)
                y1 = c_height /2
                play_status = 0
                player2_score += 1
                player = 2
                canvas1.itemconfigure(score2, text=player2_score)
                print("Touched left wall. Player 2 scores")

        elif x1 >= c_width- (20 +ball_diameter):
            if y1 >= p2_h1 and y1 <= p2_h1 + p_height :
                print("Bounced from right paddle")
                dx = -1 * (dx) * 1.2
            else:
                x1 = 0+20
                y1 = c_height /2
                play_status = 0
                player1_score += 1
                player = 1
                canvas1.itemconfigure(score1, text=player1_score)
                print("Touched right wall. Player1 scores")
    else:
        pass
    canvas1.coords(circle, x1, y1, x1+ball_diameter,y1+ball_diameter)
    window.after(50, ball_move)



def P1_up_move(event):
    """
    This function sets the up motion of the left paddle (paddle1)
    whenever the Up arrow key on the keyboard is pressed
    """
    global p1_h1, p_speed
    if p1_h1 >= (0 + p_speed) :
        p1_h1 = p1_h1 - p_speed
    canvas1.coords(paddle_1, 0, p1_h1, 20, p1_h1+p_height)


def P1_down_move(event):
    """
    This function sets the down motion of the left paddle (paddle1)
    whenever the Down arrow key on the keyboard is pressed
    """
    global p1_h1, p_speed, p_height, c_height
    if p1_h1 <= (c_height - p_height - p_speed) :
        p1_h1 = p1_h1 + p_speed
    canvas1.coords(paddle_1, 0, p1_h1, 20, p1_h1+p_height)


def P2_move(event):
    """
    This function controls the up and down motion of the right paddle(paddle2)
    with mouse button clicks
    """
    global p2_h1, p_height, c_height
    position = event.y
    if position > 0 and position <= (c_height - p_height) :
        p2_h1 = position
    canvas1.coords(paddle_2, 780, p2_h1, 800,p2_h1+p_height)


def game_start(event):
    """
    This function starts the game when the Space key on keyboard is pressed
    """
    global play_status, dx, dy
    if player == 2:
        dx = random.randrange(-15, -9)
        dy = random.choice([12, -12, 10, -10, 5, -5, 8, -8])
    else:
        dx = random.randrange(10,16)
        dy = random.choice([12,-12, 10, -10, 5, -5, 8, -8])
    play_status = 1

# Initial status flags
play_status = 0
player = 0

# The Space key on the keyboard to start the game
window.bind('<space>', game_start)

# Creating the Canvas
c_width = 800
c_height = 500
canvas1 = Canvas(window, height =c_height , width =c_width , bg ="Black")
canvas1.pack()

# Drawing the Pong Board lines
canvas1.create_line(400,0,400,500, fill="White")
canvas1.create_line(20,0,20,500, fill="White")
canvas1.create_line(780,0,780,500, fill= "White")

# Creating the paddles
p1_h1 = 250
p2_h1 = 250
p_height = 100
p_speed = 25
paddle_1 = canvas1.create_rectangle(0, p1_h1, 20, p1_h1+p_height, fill = "White")
paddle_2 = canvas1.create_rectangle(780, p2_h1, 800, p2_h1+p_height, fill="White")

# Initial position of the ball
x1 = 0+20
y1 = c_height /2

# Initial velocity of the ball
#dx = 10
#dy = 12

# Creating the ball
ball_diameter = 50
circle = canvas1.create_oval(x1,y1,x1+ball_diameter,y1+ball_diameter, fill="Gray")



# Binding the paddle movement to the keyboard keys and the mouse
window.bind('<Up>', P1_up_move)
window.bind('<Down>', P1_down_move)
window.bind('<Motion>',P2_move)


# Initializing the game score board. Player1 is the left side player and Player2 is the right side player
player1_score = 0
player2_score = 0
score1 = canvas1.create_text(100,100, font=("Purisa", 25), text = player1_score, fill = "White")
score2 = canvas1.create_text(700,100, font=("Purisa", 25), text= player2_score, fill = "White")

ball_move()

window.mainloop()
