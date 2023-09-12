import pyautogui
from time import sleep

with open('Arquivos_CSV/cadastros_do_mes_finalizado.csv','r') as arquivo:
    for linha in arquivo:
        itemc = linha.split(';')[1]
        pyautogui.doubleClick(192,195,duration = 0.2)
        pyautogui.write(itemc)
        pyautogui.doubleClick(367,220,duration = 0.2)
        pyautogui.write(itemc)
        pyautogui.sleep(0.2)
        pyautogui.press('F2')
        pyautogui.sleep(0.2)
        pyautogui.press('enter')
        pyautogui.sleep(0.2)
