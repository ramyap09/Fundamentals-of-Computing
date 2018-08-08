"""
This implements a GUI which pictures a circle and two buttons to change the radius (increase/decrease) of the circle interactively.
"""

from tkinter import *

window = Tk()
window.geometry("400x400+800+100")
window.title("Change the radius of the Circle")

# defining the initial coordinates of the circle.
X0 = 130
Y0 = 130
X1 = 170
Y1 = 170



def rad_increase():
    """
    This function implements the increases in the size of the circle, when the corresponding button on the GUI is pressed.
    """
    global X0, Y0, X1, Y1
    if X0 > 0 and Y0 > 0 :
        X0 = X0-2
        Y0 = Y0-2
        X1 = X1+2
        Y1 = Y1+2
        canvas1.coords(item,X0,Y0,X1,Y1)
    else:
        pass


def rad_decrease():
    """
    This function implements the decrease in the size of the circle, when the corresponding button on the GUI is pressed.
    """
    global X0, Y0, X1, Y1
    if X1 > 150 and  Y1 > 150 :
        X0 = X0+2
        Y0 = Y0+2
        X1 = X1-2
        Y1 = Y1-2
        canvas1.coords(item, X0,Y0,X1,Y1)
    else:
        pass

# Creating the buttons
button_in = Button(window, text = "Increase radius", command = rad_increase).pack()
button_de = Button(window, text="Decrease radius", command = rad_decrease).pack()

# Creating the canvas in the window
canvas1 = Canvas(window, height = 300, width=300, bg="White")

# Drawing the circle
item = canvas1.create_oval(X0, Y0, X1, Y1, outline="gray", fill="gray", width=2)
canvas1.pack()

window.mainloop()
