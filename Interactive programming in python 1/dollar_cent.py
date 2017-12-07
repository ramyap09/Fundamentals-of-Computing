from tkinter import *
window = Tk()
window.title("Dollar Cent converter")
window.geometry("450x500+800+50")

def conversion_doll(doll):
    """
    This function returns the properly formatted dollar part of the output
    """
    if doll == 1:
        x = str(doll) + " "  + "dollar"
    else:
        x = str(doll) + " "  + "dollars"
    return x

def conversion_cent(cent):
    """
    This function returns the properly formatted cent part of the output
    """
    if cent == 1:
        y = str(cent) + " " + "cent"
    else:
        y = str(cent) + " " + "cents"
    return y

def converter():
    """
    This function prints on the canvas, the dollars and cents
    """
    canvas1.delete("all")
    try:
        amount = sv.get()
        doll = int(amount)
        cent = round(amount - int(amount), 2)
        cent = int(cent*100)
        if doll == 0 and cent ==0:
            ans = "Broke !"
        elif doll ==0:
            ans = conversion_cent(cent)
        elif cent ==0:
            ans = conversion_doll(doll)
        else:
            ans = conversion_doll(doll) + " and " + conversion_cent(cent)
        canvas1.create_text(150,150, font=("Purisa", 14), text= ans)
    except:
        canvas1.create_text(150,0, font=("Purisa", 14), text= "Enter a valid input ", anchor=N)

# Creating Label, Button and Canvas
label_1 = Label(window, text="Enter the number :").pack()
sv= DoubleVar()
e1 = Entry(window, textvariable = sv)
e1.pack()
e1.delete(0, END)
button_ok = Button(window, text = "OK", command = converter).pack()
canvas1 = Canvas(window, height = 300, width=300, bg="White")
canvas1.pack()

window.mainloop()
