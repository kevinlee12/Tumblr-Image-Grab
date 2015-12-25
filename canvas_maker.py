from PIL import Image
import os
from random import randint
import datetime

canvas_width = 1000
canvas_height = 790

path = os.path.join(os.getcwd(), 'tumblr_img')
large_size = (200, 200)

# Credits to http://stackoverflow.com/a/23936340:
def image_resize(image):
    """Resizes images to so that it is at most 200 pixels"""
    img = Image.open(image)
    image_w, image_h = img.size
    aspect_ratio = image_w / float(image_h)
    new_height = int(large_size[0] / aspect_ratio)

    if new_height < 200:
        final_width = large_size[0]
        final_height = new_height
    else:
        final_width = int(aspect_ratio * large_size[1])
        final_height = large_size[1]

    imaged = img.resize((final_width, final_height), Image.ANTIALIAS)

    imaged.save(image, quality=100)


# Creating the canvas file
def canvas_file():
    canvas = open('canvas.py', 'w')
    canvas.write('from tkinter import *\n')
    canvas.write('from PIL import Image, ImageTk\n')
    canvas.write('\n')
    canvas.write('master = Tk()\n')
    canvas.write('master.wm_title("Mosaic")\n')
    canvas.write('canvas = Canvas(master, width={0}, height={1})\n'.format(canvas_width, canvas_height))
    canvas.write('canvas.pack()\n')
    canvas.write('\n')

    n = 1
    files = os.listdir(path)
    for f in files:
        file_path = os.path.join(path, f)
        width = randint(0, canvas_width)
        height = randint(0, canvas_height)
        image_resize(file_path)
        canvas.write('img_{0} = Image.open("{1}")\n'.format(n, file_path))
        canvas.write('photo_{0} = ImageTk.PhotoImage(img_{0})\n'.format(n))
        canvas.write('canvas.create_image({0}, {1}, anchor=CENTER, image=photo_{2})\n'.format(width, height, n))
        n += 1

    canvas.write('# Downloaded total of {0} images\n'.format(n))
    today = datetime.datetime.now()
    if today.month == 12 and (today.day == 25 or today.day == 24):
        tree_path = opath = os.path.join(os.getcwd(), 'chlorophyll')
        canvas.write('christmas = Image.open("{0}")\n'.format(os.path.join(tree_path, 'christmas.png')))
        canvas.write('xmas_photo = ImageTk.PhotoImage(christmas)\n')
        canvas.write('canvas.create_image({0}, {1}, anchor=CENTER, image=xmas_photo)\n'.format(canvas_width//2, canvas_height//2))

    canvas.write('\nmainloop()\n')
    canvas.close()
    date_file = open('canvas_date', 'w')
    date_file.write('{0} {1}\n'.format(today.month, today.day))
    date_file.write('# Date canvas prep\n')
    date_file.close()

def main():
    print('Canvas prepping...')
    canvas_file()
