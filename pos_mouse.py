# Código para obter posição do mouse
import pyautogui
import time

time.sleep(7)
x, y = pyautogui.position()
print ("x = "+str(x)+" y = "+str(y))