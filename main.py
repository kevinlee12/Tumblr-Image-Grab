#!/usr/bin/python3
""" Grabs images from a specified website and shows it on the desktop """

import sys
import download
import canvas_maker
import os
import datetime

assert len(sys.argv) > 1, 'Please specify a tumblr username!'

if sys.argv[1] != '-v':
    sys.stdout = None
assert sys.argv[-1] != '-v', 'Please specify a tumblr username!'
assert len(sys.argv) < 4, 'Too many arguments!'

tumblr_username = sys.argv[-1]

today = datetime.datetime.now()

download_skip = 0
try:
    date_file = open('download_date', 'r')
    date = date_file.readline()
    date = date.split()
    if int(date[0]) == today.month and int(date[1]) == today.day:
        download_skip = 1
except FileNotFoundError:
    pass

canvas_skip = 0
try:
    date_file = open('canvas_date', 'r')
    date = date_file.readline()
    date = date.split()
    if int(date[0]) == today.month and int(date[1]) == today.day:
        canvas_skip = 1
except FileNotFoundError:
    pass

if not download_skip:
    print('Starting Download')
    download.main(tumblr_username)
if not canvas_skip or not os.path.isfile('canvas.py'):
    print('Preparing file')
    canvas_maker.main()
