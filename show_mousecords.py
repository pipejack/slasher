import pyautogui as pag
import os, os.path
import pyscreeze

path = "Reference_images\Spotify"
playButton = os.path.join(path,"play_button.png")
while(True):
    test = pag.position()
    print(test)
#if isinstance(, ImageNotFoundException):
    #print("not found")
