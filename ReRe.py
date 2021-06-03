import os
import csv
import re
import shutil
from PIL import Image

def returnEnglishName(JapaneseName):   
    Pokemon1 = []
    Pokemon2 = []

    with open("Pokemon.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            Pokemon1.append(str(row[0]))
            Pokemon2.append(str(row[1]))

    listNumber = Pokemon1.index(JapaneseName)
    EnglishName = Pokemon2[listNumber]

    return EnglishName

def returnPath(filename):
    m = re.search(r"^([^0-9]+)([0-9]*)$",filename)
    JapaneseName = m.group(1)
    NameNumber = m.group(2)
    path = returnEnglishName(JapaneseName)+NameNumber + ".jpg"
    return path

def scale_to_height(img, height):  # アスペクト比を固定して、幅が指定した値になるようリサイズする。
    width = round(img.width * height / img.height)
    return img.resize((width, height))

def Copy_Resize(path,width):
    shutil.copy(OriginalFilePath,path)
    img = Image.open(path)
    img_resize = scale_to_height(img,width)
    img_resize = img_resize.save(path,quality = 95)

filename = input()
OriginalFilePath = "twitter/" + filename + ".jpg"
filepath = "image/" + returnPath(filename)
bigfilepath = "bigimage/" + returnPath(filename)

if os.path.isfile(OriginalFilePath):
    Copy_Resize(bigfilepath,450)
    Copy_Resize(filepath,225)
    print('<a href="' + bigfilepath + '" data-lightbox="poke"><img src="' + filepath + '" alt="' + filename + '"></a>')

else:
    print("存在しないファイルです") 
    

