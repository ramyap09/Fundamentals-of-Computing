"""
Display the image from  URL
"""

from tkinter import *
import io
from PIL import Image, ImageTk
from urllib.request import urlopen

window = Tk()
window.geometry("500x300")
window.title("show image from URL")

# assign the URL string to the variable pic_url below.
pic_url = "Give the URL of the image here"

# Reading the image from the URL
page = urlopen(pic_url)

# create an image file object
pic_file = io.BytesIO(page.read())

# use PIL to open image formats like .jpg  .png  .gif  etc.
pil_img = Image.open(pic_file)

# convert to an image Tkinter can use
tk_img = ImageTk.PhotoImage(pil_img)

label_img = Label(window, image=tk_img)
label_img.pack(padx=10, pady=10)


window.mainloop()
