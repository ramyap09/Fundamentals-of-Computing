"""
Building the card game named memory
"""

import random
from tkinter import *

window = Tk()
window.title("Game - Memory")



def newgame():
    """
     This function draws the all the 16 cards on the canvas
    """
    global lst
    x1,y1,x2,y2 = 10, 10, 60, 110
    for index, item in enumerate(lst):
        id = canvas1.create_rectangle(x1, y1, x2, y2, fill = "White", tags="rectangle")   # Draw these rectangles only once, otherwise id will get altered
        x1 = x1 + 50
        x2 = x2 + 50




def reset():
    """
     This function initializes all the list variables and other variables and hence starts new game.
    """
    global exposed, clicked_num_index_lst, text_id, clicked_num_lst, state, turns, lst
    exposed = [False]*16
    clicked_num_index_lst = []
    canvas1.delete('numbers')  # Here deleted all the objects with the tag "numbers"
    text_id=[]
    clicked_num_lst=[]
    state=0
    turns=0
    label_turns.config(text = "Turns = 0 ")
    lst1 = list(range(8))
    lst2 = list(range(8))
    lst = lst1 + lst2
    random.shuffle(lst)


# Creating button, label and canvas
button_reset = Button(window, text='RESET', command=reset).grid(row=0, column=0)
label_turns = Label(window, text="Turns = ")
label_turns.grid(row=1, column=0)
canvas1 = Canvas(window, height = 120, width = 820, bg ="White")
canvas1.grid(row=0, column = 5)


def click(event):
    """
     This function executes the game logic each time there is a click on the cards.
    """
    global exposed, state, clicked_num_index_lst, turns, lst, clicked_num_lst
    # If we click exactly on the already displayed number on the card, .find_closest() will find the number object instead of the
    #rectanlge(ie., the card) leading to error. So we put it as try-except. clicking on the number wont do do anything to the
    # game except the error.
    try:
        c = canvas1.find_closest(event.x,event.y)[0]  # Here we get to know which box is clicked (c is the id of the box clicked)
        #print(canvas1.gettags(c))
        m = canvas1.coords(c)   # m is the coodinates of the box clicked
        if exposed[c-1] == False:
            t_id = canvas1.create_text(m[0]+25, m[1]+50, fill = "Black", text=lst[c-1], tags="numbers")
            #print(canvas1.gettags(t_id))
            text_id.append(t_id)
            clicked_num_lst.append(lst[c-1])
            state +=1
            exposed[c-1] = True
            clicked_num_index_lst.append(c-1)
            if state == 2:
                turns += 1
                label_turns.config(text = "Turns = {} ".format(turns))
            elif state == 3 and  clicked_num_lst[0] == clicked_num_lst[1] :
                del text_id[0:2]
                del clicked_num_lst[0:2]
                del clicked_num_index_lst[0:2]
                state = 1
            elif state == 3 and clicked_num_lst[0] != clicked_num_lst[1] :
                exposed[clicked_num_index_lst[0]]= False
                exposed[clicked_num_index_lst[1]] = False
                del clicked_num_index_lst[0:2]
                canvas1.delete(text_id[0])
                canvas1.delete(text_id[1])
                del text_id[0:2]
                del clicked_num_lst[0:2]
                state = 1
    except:
        # This portion is executed when you click on the already displayed number on the card.
        pass


canvas1.bind("<Button-1>", click)
reset()
newgame()
window.mainloop()
