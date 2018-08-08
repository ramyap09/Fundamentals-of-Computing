"""
This simple code implements one GUI, the background colour of the canvas on it can be toggled between 'White' and "Red" by pressing the button provided.
"""

from tkinter import *
window = Tk()
window.title("Background color toggler")
window.geometry("500x500+700+100")



def color_toggler():
    """
    This function implements the togging between the two chosen colors.
    """
    global color
    if color == "White":
        color = "Red"
        # window.configure(background='black')
        canvas1.config(bg="Red")
    else:
        color = "White"
        canvas1.config(bg = "White")

# Creating the button
button_toggle = Button(window, text="Toggle Color", command =color_toggler).pack()

color = "White"

# Creating the Canvas
canvas1 = Canvas(window, height = 300, width=300, bg=color)
canvas1.pack()

window.mainloop()
