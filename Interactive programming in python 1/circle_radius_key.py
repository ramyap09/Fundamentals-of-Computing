"""
This implements a GUI which pictures a circle, whose radius can be increased or decreased interactively by pressing the Up arrow key
and Down arrow key of the keyboard respectively.
"""

from tkinter import *
window = Tk()
window.title("The changing circle")


def kpress(event):
    """
    This function implements the increase and decrease in the radius of the circle when the Up arrow key and Down arrow key in the keyboard is pressed
    respectively
    """
    global X0, Y0, X1, Y1
    if event.keysym == 'Up':
        if X0 > 0 and Y0 > 0 :
            X0 = X0-2
            Y0 = Y0-2
            X1 = X1+2
            Y1 = Y1+2
            canvas1.coords(circle, X0,Y0,X1,Y1)
        else:
            pass
    elif event.keysym == "Down" :
        if X1 > 150 and  Y1 > 150 :
            X0 = X0+2
            Y0 = Y0+2
            X1 = X1-2
            Y1 = Y1-2
            canvas1.coords(circle,X0,Y0,X1,Y1)
        else:
            pass
    else:
        pass


window.bind_all('<KeyPress>', kpress)
#window.bind_all('<KeyRelease>', krel)

# Defining the initial coordinates of the circle
X0 = 130
Y0 = 130
X1 = 170
Y1 = 170

# Creating the canvas
canvas1 = Canvas(window, height =300 , width =300, bg = "White" )
canvas1.pack()

# Drawing the circle
circle = canvas1.create_oval(X0,Y0,X1,Y1,outline="gray", fill="gray", width=2 )

window.mainloop()
