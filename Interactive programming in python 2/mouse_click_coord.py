"""
For each mouse click, print the position of the mouse click to the console. Note that x,y = 0, 0  at the top left corner of the window.
"""
from tkinter import *

window = Tk()
window.geometry("500x300")
window.title("print the mouse click coordinates")



def click_pos(event):
    """
    This function prints the the x and y coordinates of the mouse click
    """
    print ("Clicked at", event.x, event.y)


# binding the mouse click to the function "click_pos" given above
window.bind("<Button-1>", click_pos)

window.mainloop()
