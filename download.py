import urllib.request as req
import re
from random import randint
import os
import datetime


img_pattern = re.compile(r'http://[0-9]+.media.tumblr.com/\w+/\w+.jpg')
jpg_pattern = re.compile(r'[a-zA-Z0-9_]+.jpg')
link_patt = re.compile(r'http://\w+.tumblr.com/post/[0-9]+/photoset_iframe/\w+/\w+/[0-9]+/false')


def get_page_images_and_iframes(link, images, iframes):
    """Grabs images and iframes, will not throw any errors."""

    try:
        html = req.urlopen(link)
    except:
        return True

    lines = str(html.read()).split('\\n')
    img_count = 0
    iframes_count = 0
    for line in lines:
        line = line.strip()
        if re.search(img_pattern, line):  # Checking for images
            images.add(re.search(img_pattern, line).group(0))
            img_count += 1
        elif re.search(link_patt, line):  # Checking iframes
            iframes.add(re.search(link_patt, line).group(0))
            iframes_count += 1
    return img_count > 3 or iframes_count > 3


def download_image(link):
    """Downloads images to the tumblr_img folder in the current folder.
       Will create a tumblr_img folder if it does not exist.
    """
    path = os.path.join(os.getcwd(), 'tumblr_img')
    if not os.path.exists(path):
        os.makedirs(path)
    img_name = re.search(jpg_pattern, link).group(0)
    path = os.path.join(path, img_name)
    req.urlretrieve(link, path)
    return True


def main(tumblr_name):
    retval = True
    page_number = 1
    end_page = 7

    print('Fetching images from {0}'.format(tumblr_name))

    images = set()
    iframes = set()

    while page_number < end_page and retval:
        link = 'http://{0}.tumblr.com/page/{1}'.format(tumblr_name, page_number)
        print("Grabbing page {0}".format(page_number))
        retval = get_page_images_and_iframes(link, images, iframes)
        while len(iframes):
            link = iframes.pop()
            print('Grabbing iframe {0}'.format(link))
            get_page_images_and_iframes(link, images, set())
        page_number += 1

    print('Downloading images')

    while images:
        download_image(images.pop())

    today = datetime.datetime.now()
    date_file = open('download_date', 'w')
    date_file.write('{0} {1}\n'.format(today.month, today.day))
    date_file.write('# Date downloaded\n')
    date_file.close()

    # Clean stuff
    req.urlcleanup()
