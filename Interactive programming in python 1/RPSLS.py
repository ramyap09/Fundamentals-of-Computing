from tkinter import *
import random


window = Tk()
window.geometry("500x200")
window.title("rock-paper-scissors-lizard-Spock : The game")


def name_to_number(name):
    """
    Returns a unique number for each name, given the name as input.
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        label1.config(text= "invalid input. Try again")
        label2.config(text="")
        label3.config(text="")
        return None



def number_to_name(number):
    """
    Returns the name coresponding the number, given the number as input
    """
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        pass


def rpsls():
    """
    Given a name, this function prints out who wins the game (you or the computer) based on the the game rules
    """
    choice = sv.get()
    player_number = name_to_number(choice)
    comp_number = random.randrange(0,5)
    if player_number != None:
        label1.config(text="Player chooses {}".format(number_to_name(player_number)))
        label2.config(text="Computer chooses {}".format(number_to_name(comp_number)))
        diff = (player_number - comp_number) % 5
        if diff == +1 or diff == +2:
            label3.config(text="Player wins")
        elif diff == +3 or diff == +4:
            label3.config(text="Computer wins")
        else:
            label3.config(text="Player Computer tie !")
    else:
        e1.delete(0,END)


# Creating Labels, Button, and Entry box
Label(window, text="Entre your choice (rock/paper/scissors/lizard/Spock) : ").grid(row=0, column=0, pady=(20, 10), padx=(20,0))
button_ok = Button(window, text='OK', command=rpsls).grid(row=1, column=1)
sv = StringVar()
e1 = Entry(window, textvariable = sv)
e1.grid(row=0, column=1)
label1 = Label(window, text="")
label1.grid(row=4, column=0)
label2 = Label(window, text="")
label2.grid(row=5, column=0)
label3 = Label(window, text="")
label3.grid(row=6, column=0)

window.mainloop()
