import pyautogui
from time import sleep

with open('Arquivos_CSV/cadastros_do_mes_finalizado.csv','r') as arquivo:
    for linha in arquivo:
        item = linha.split(';')[1]
        referencia = linha.split(';')[4]
        pyautogui.doubleClick(178,331, duration=0.2)
        pyautogui.write(referencia)
        pyautogui.click(682, 410, duration = 0.2)
        pyautogui.write(item)
        pyautogui.click(749,505, duration=0.2)
        pyautogui.write(item)
        pyautogui.click(841,602, duration =0.2)
        pyautogui.click(308,428,duration = 0.2)
        pyautogui.click(456,471,duration=0.2)
        sleep(0.2)
        pyautogui.press('left')
        sleep(0.2)
        pyautogui.press('enter')
        sleep(0.2)
        pyautogui.press('enter')
        sleep(0.2)


