#!/usr/bin/env python

from playsound import playsound
from PIL import Image
import os

while(1):
	alphabet = input("please enter an alphabet : ")
	alphabet=alphabet.upper()

	path = "images\\" + alphabet + ".jpg"

	img = Image.open(path)
	d=display(img)
	alphabet=alphabet.lower()
	path = "sound\\" + alphabet + ".mp3" 
	play=playsound(path)





