import glob
import re
from os import mkdir
from PIL import Image

files = [f for f in glob.glob("*.jpg")]
print(files)
if files == []:
    print("no jpg files, aborting")
    exit(1)

try:
    mkdir("result")
    print("Directory result doesn\'t exist, creating one")
except FileExistsError:
    print("Directory result already exists")

for path in files:
    im = Image.open(path)
    print(path + " loaded")
    path = re.sub("\.jpg$", "", path)
    im.thumbnail((512, 512))
    path = path + ".png"
    im.save("result/" + path, "PNG")
    print(path + " saved as png")