import pyautogui
import time

with open('Arquivos_CSV\INATIVAR 11-10-23.csv','r') as arquivo:
        for linha in arquivo:
            item = linha.split(';')[0]
            pyautogui.doubleClick(180, 239,duration=0.2)
            pyautogui.write(item)
            pyautogui.press('enter')
            pyautogui.click(229, 502,duration=0.2)
            



