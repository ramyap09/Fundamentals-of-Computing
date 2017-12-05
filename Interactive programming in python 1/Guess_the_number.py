import random
from tkinter import *

window = Tk()
window.geometry("500x300")
window.title("Guess the number - The game")

def range100():
    """
    This function generates a random number in the range of [0-100) and stores it in the variable secret_number
    """
    e1.delete(0,END)
    global maximum, counter, secret_number
    counter =0
    maximum = 7
    print("New game starts... Guess a number in the range [0-100). Maximum of 7 attempts allowed")
    secret_number = random.randrange(0,100)

def range1000():
    """
    This function generates a random number in the range of [0-1000) and stores it in the variable secret_number
    """
    e1.delete(0,END)
    global maximum, counter, secret_number
    maximum = 10
    counter =0
    print("New game starts... Guess a number in the range [0-1000). Maximum of 10 attemts allowed")
    secret_number = random.randrange(0,1000)

def input_guess():
    """
    This function does the appropriate comparisons and prints out whether the random number geneated by the computer
    is higher, lower or equal to the number entered by the user.
    """
    global counter, secret_number, maximum
    counter +=1
    try:
        num = sv.get()
        print("Your guess is {}".format(num))
        if num < secret_number :
            print("Answer is higher than your guess")
        elif num > secret_number :
            print("Answer is lower than your guess")
        elif num == secret_number and maximum == 7:
            print("Your guess is Correct!")
            range100()
        elif num == secret_number and maximum == 10 :
            print("Your guess is Correct!")
            range1000()
        else:
            pass

        if counter == maximum and maximum == 7:
            print("Game Over. No attempts left")
            range100()
        elif counter == maximum and maximum == 10:
            print("Game Over. No attempts left")
            range1000()
        else:
            pass
    except:
        if maximum == 7:
            range100()
        else:
            range1000()

Label(window, text="Select the range of numbers : ").grid(row=0, column=0, sticky=E)
button_range100 = Button(window, text='Range [0-100)', command=range100).grid(row=0, column=1)
button_range1000 = Button(window, text="Range [0-1000)", command = range1000).grid(row=0, column=2)
Label(window, text="Enter your Guess. Default range is [0-100) : ").grid(row=5, column=0)
sv = IntVar()
e1 = Entry(window, textvariable = sv)
e1.grid(row=5, column=1)
button_ok = Button(window, text = "OK", command= input_guess).grid(row=6, column=1)
#button_quit = Button(window, text="QUIT", fg="red", width=25, command=quit).grid(row=7, column=2, sticky=W, pady=4)
e1.delete(0,END)
range100()
window.mainloop()
