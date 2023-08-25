import pyautogui
from time import sleep
with open('Arquivos CSV/cadastro colete.csv','r') as arquivo:
    for linha in arquivo:
        item = linha.split(';')[1]
        referencia = linha.split(';')[3]
        pyautogui.doubleClick(162,312, duration=0.5)
        pyautogui.write(referencia)
        pyautogui.click(667, 391, duration = 0.5)
        pyautogui.write(item)
        pyautogui.click(730, 486, duration=0.5)
        pyautogui.write(item)
        pyautogui.click(827, 584, duration =0.5)
        pyautogui.click(301, 516,duration = 0.5)
        pyautogui.click(468, 560,duration=0.5)
        sleep(0.5)
        pyautogui.press('left')
        sleep(0.5)
        pyautogui.press('enter')
        sleep(0.5)
        pyautogui.press('enter')
        sleep(0.5)


