"""
Creating a polyline with the mouse clicks on the canvas.
"""
from tkinter import *

window = Tk()
#window.geometry("500x300")
window.title("polyline")

def first_point(event):
    """
    This function draws the lines when mouse is clicked on the canvas
    """
    (x1, y1) = (event.x, event.y)
    x_coords.append(x1)
    y_coords.append(y1)
    if len(y_coords) > 1:
        x1 = x_coords[-2]
        y1 = y_coords[-2]
        x2 = x_coords[-1]
        y2 = y_coords[-1]
        #print(x1,y1,x2,y2)
        canvas1.create_line(x1,y1,x2,y2, fill="Black")
    else:
        point = canvas1.create_oval(x1,y1,x1,y1, fill="Black")




def clear_page():
    """
    This function clears the canvas and the lists x_coords and y_coords once the CLEAR button is pressed
    """
    global x_coords, y_coords
    x_coords = []
    y_coords = []
    canvas1.delete("all")


# Creating the button
button1 = Button(window, text='CLEAR', command=clear_page).pack()

# Creating the canvas
c_width = 500
c_height = 300
canvas1 = Canvas(window, height =c_height , width =c_width , bg ="White")
canvas1.pack()

# Binding the canvas with the mouse click
canvas1.bind("<Button-1>", first_point)

# Initializing empy lists
x_coords = []
y_coords = []



window.mainloop()
