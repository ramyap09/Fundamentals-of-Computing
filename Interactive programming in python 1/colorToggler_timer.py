"""
This simple code implements one GUI, the background colour of the canvas on it toggles between "Red" and "Green" in fixed time intervals.

"""


from tkinter import *
window = Tk()
window.title("Background color toggler")
window.geometry("500x500+700+100")


def color_toggler():
    """
    This function implements the automatic toggling between the chosen colours.
    """

    global color
    if color == "Green":
        color = "Red"
        # window.configure(background='black')
        canvas1.config(bg="Red")
    else:
        color = "Green"
        canvas1.config(bg = "Green")
    window.after(3000, color_toggler)


color = "Green"

# Creating the canvas
canvas1 = Canvas(window, height = 300, width=300, bg=color)
canvas1.pack(pady=(30,0))

color_toggler()

window.mainloop()
