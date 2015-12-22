import sys
import os

error = 0
try:
    import PIL.Image, PIL.ImageTk
except:
    print('Cannot import PIL library')
    error = 1

try:
    from tkinter import *
except:
    print('Cannot import tkinter')
    error = 1

if error:
    sys.exit()

canvas_width = 300
canvas_height = 300

master = Tk()

canvas = Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack()

file_path = os.path.join(os.getcwd(), 'IB.jpg')
img = PIL.Image.open(file_path)
photo = PIL.ImageTk.PhotoImage(img)
canvas.create_image(150, 150, anchor=CENTER, image=photo)

print('You may close the window')
mainloop()
