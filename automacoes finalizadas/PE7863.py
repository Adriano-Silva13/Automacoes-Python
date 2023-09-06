import pyautogui
import time

with open('csv/INATIVAR 15 08 23.csv','r') as arquivo:
        for linha in arquivo:
            item = linha.split(';')[0]
            pyautogui.doubleClick(203, 255,duration=1)
            pyautogui.write(item)
            pyautogui.press('enter')
            pyautogui.click(254, 518,duration=1)
            



