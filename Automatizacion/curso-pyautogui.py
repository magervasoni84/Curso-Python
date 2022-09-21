import pyautogui 
import time
import os

""" 
# Devuelve las dimensiones de la pantalla
ancho, alto = pyautogui.size()
# Devuelve la posición actual
Xactual, Yactual = pyautogui.position()
# Mover a coordenadas (pixels)
pyautogui.moveTo(100, 150) 
# Clickear
pyautogui.click() 
# Tipear con delay
pyautogui.write('Hello world!', interval=0.25)  
# Apretar una tecla
pyautogui.press('esc') 
pyautogui.hotkey('ctrl', 'c')
pyautogui.locateOnScreen()

pyautogui.move(x, y, duracion)
pyautogui.drag(x, y, duracion)
 """

def abrir_pagina():
    url = r"https://www.lapoliticaonline.com/"
    os.system("start firefox.exe")
    time.sleep(2)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(2)
    pyautogui.write(url)
    time.sleep(2)
    pyautogui.press('enter')


