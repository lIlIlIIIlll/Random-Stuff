from pyautogui import *
import pyautogui
import time

cont = 1

while 1:
    if pyautogui.locateOnScreen('imagem.png', confidence=0.7) != None:
        print("Tá dando bom aqui. ["+str(cont)+"]")
        cont +=1
        time.sleep(0.5)
    else:
        print("Deu não patrão. ["+str(cont)+"]")
        cont +=1
        time.sleep(0.5)