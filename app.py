#!/usr/bin/env python
import math
import glob
import re
from os import mkdir
from PIL import Image

tg_size = 512
files_jpg = [f for f in glob.glob("*.jpg")]
files_png = [f for f in glob.glob("*.png")]
files = files_jpg + files_png
print("Files found in CWD:", end=" ")
print(", ".join(files))
if files == []:
    print("No image files found in CWD, aborting")
    exit(0)

try:
    mkdir("result")
    print("Directory \'result\' doesn\'t exist, creating one")
except FileExistsError:
    print("Directory \'result\' already exists")

for path in files:
    im = Image.open(path)
    print(path, "loaded,", end=" ")
    if max(im.size[0], im.size[1]) < 512:
        print("upscaled, and", end=" ")
        sizeq = math.ceil(512 / max(im.size[0], im.size[1]))
        im = im.resize((im.size[0] * sizeq, im.size[1] * sizeq))
    im.thumbnail((tg_size, tg_size), Image.ANTIALIAS)
    path = re.sub("\.jpg$|\.png$", "", path)
    path = path + ".png"
    im.save("result/" + path, "PNG")
    print("saved as png")

print("Done!")
    