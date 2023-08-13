from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import os
import shutil
from PIL import Image as Im
from PIL import ImageTk
from math import floor


image_filename = None
mark_filename = None
location = None


def get_image():
    image = fd.askopenfilename(title="Select an image", filetypes=[("All files", "*.*")])
    global image_filename
    image_filename = image
    print(image_filename)


def get_mark():
    mark = fd.askopenfilename(title="Select a marker", filetypes=[("All files", "*.*")])
    global mark_filename
    mark_filename = mark
    print(mark_filename)


def get_location(event):
    global location
    location = location_listbox.get(location_listbox.curselection())
    print(location)


def process_image():
    im1 = Im.open(image_filename)
    im2 = Im.open(mark_filename)
    w, h = im1.size
    w2, h2 = im2.size
    if location == "Top Left":
        mark_region = (0, 0)
    elif location == "Top Right":
        mark_region = (w-w2, 0)
    elif location == "Bottom Left":
        mark_region = (0, h-h2)
    elif location == "Bottom Right":
        mark_region = (w-w2, h-h2)
    elif location == "Top":
        mark_region = (floor(w/2-w2/2), 0)
    elif location == "Bottom":
        mark_region = (floor(w/2-w2/2), h-h2)
    else:
        mark_region = (floor(w/2-w2/2), floor(h/2-h2/2))
    im1.paste(im2, mark_region)

    is_ok = mb.askokcancel(title="Watermark Added", message="The watermark has been added to your image. You can now save it. Click OK to proceed.")
    if is_ok:
        im1.show()
        window.destroy()



window = Tk()
window.title("Image Watermarking App")
window.minsize(500, 500)
window.config(padx=50, pady=50)


image_button = Button(text="Add Image", command=get_image)
image_button.grid(row=1, column=1)

mark_button = Button(text="Add Marker", command=get_mark)
mark_button.grid(row=1, column=2)

location_label = Label(text="Choose location for watermark:", font=("Arial", 15, "normal"))
location_label.grid(row=2, column=1, columnspan=2)
location_listbox = Listbox(height=6)
locations = ["Top", "Bottom", "Top Left", "Top Right", "Bottom Right", "Bottom Left"]
for loc in locations:
    location_listbox.insert(locations.index(loc), loc)
location_listbox.bind("<<ListboxSelect>>", get_location)
location_listbox.grid(row=3, column=1)

confirm_label = Label(text="Press to get image.", font=("Arial", 15, "normal"))
confirm_label.grid(row=4, column=1, columnspan=2)

confirm_button = Button(text="Confirm", command=process_image)
confirm_button.grid(row=5, column=1)

window.mainloop()