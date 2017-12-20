from tkinter import *

window = Tk()
window.title("Stopwatch")
window.geometry("500x500+700+100")
x = 0
y = 0
z = 0



def status_change():
    """
    This function makes the start() function to run, when the Start button is clicked
    """
    global STATUS
    STATUS = True



# The Timer in the format (minutes:seconds: 0.1 seconds)
def start():
    global x, y, z, STATUS
    if STATUS == True:
        z = z+1
        if z == 10:
            z = 0
            y = y +1
        if y == 60:
            y = 0
            x = x +1
        message = "{}:{:02d}:{}".format(x,y,z)
        canvas1.itemconfigure(item, text=message)
    window.after(100, start)



def stop():
    """
    This function stops the timer when the Stop Button is clicked
    """
    global STATUS
    STATUS = False



def reset():
    """
    This function resets the timer when the Reset Button is clicked
    """
    global STATUS, x, y, z
    STATUS = False
    canvas1.itemconfigure(item,text="0:00:0")
    x = 0
    y = 0
    z = 0

# Creating the Buttons
button_start = Button(window, text="Start", command = status_change).pack()
button_stop = Button(window, text="Stop", command = stop).pack()
button_reset = Button(window, text="Reset", command = reset).pack()

# creating the Canvas and the timer-text display
canvas1 = Canvas(window, height =300 , width =300 , bg ="White")
item = canvas1.create_text(150,150, font=("Purisa", 50), text= "0:00:0")
canvas1.pack()
STATUS = False
start()
window.mainloop()
