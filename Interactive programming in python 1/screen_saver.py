from tkinter import *
import random

window = Tk()
window.title("Simple screen saver")
window.geometry("700x650+600+10")


def start():
    """
    This function moves the default text randomly on the canvas, when the program starts running.
    """
    global STATUS, item
    canvas1.delete("all")
    x,y = random.sample(range(80, 500), 2)
    if STATUS:
        canvas1.create_text(x,y, font=("Purisa", 14), text= "Enter custom message !")
        window.after(1000, start)
    elif STATUS == False and sv.get() != "":
        button_func()
    else:
        STATUS = True
        start()


def status_change():
    """
    This function gets the text entered in to the entry box so as to pass it to the helper functions
    """
    global STATUS, message
    if sv.get() != "":
        message = sv.get()
    else:
        pass
    STATUS = False



def button_func():
    """
    This function moves the user entered text randomly on the canvas.
    """
    global message, STATUS, item
    canvas1.delete("all")
    STATUS = False
    x, y = random.sample(range(80, 500), 2)
    canvas1.create_text(x,y, font=("Purisa", 14), text= message)
    window.after(1000, button_func)


STATUS = True

# Creating the Label
label_1 = Label(window, text="Enter custom message :").pack()

# Creating the Entry box
sv= StringVar()
e1 = Entry(window, textvariable = sv )
e1.pack()

# Creating the Button
button_ok = Button(window, text="OK", command = status_change).pack()

# Creating the Canvas
canvas1 = Canvas(window, height = 500, width=600, bg="White")
canvas1.pack()
start()

window.mainloop()
