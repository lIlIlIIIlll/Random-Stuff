from pyautogui import *
import pyautogui as pya
import time
import keyboard
import random
import win32api as win
import win32con as win2

r1x = 664
y = 670
r2x = 575
r3x = 488
r4x = 403




def clique(x,y):
    win.SetCursorPos((x,y))
    win.mouse_event(win2.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win.mouse_event(win2.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pya.pixel(r1x,y)[0] == 0:
        click(r1x,y)
    if pya.pixel(r2x,y)[0] == 0:
        click(r2x,y)
    if pya.pixel(r3x,y)[0] == 0:
        click(r3x,y)
    if pya.pixel(r4x,y)[0] == 0:
        click(r4x,y)