#!/usr/bin/env python

from playsound import playsound
user=input("please enter an alphabet : ")
user=user.upper()
from PIL import Image
import os
path=user
suffix=".jpg"
word=os.path.join(path+suffix)
#print(word)
img = Image.open(word)
d=display(img)
user=user.lower()
path=user
suffix=".mp3"
sound=os.path.join(path+suffix)
play=playsound(sound)





