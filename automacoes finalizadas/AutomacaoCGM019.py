import pyautogui
from time import sleep
with open('csv/INATIVAR 15 08 23.csv','r') as arquivo:
    for linha in arquivo:
        item = linha.split(';')[0]
        descricao = linha.split(';')[1]
        novaDescricao = linha.split(';')[3]
        pyautogui.doubleClick(207, 189, duration=0.6)
        pyautogui.write(item) 
        pyautogui.sleep(0.6)
        pyautogui.press('enter')
        pyautogui.sleep(0.6)
        pyautogui.press('delete')
        pyautogui.sleep(0.6)
        pyautogui.doubleClick(603, 396,duration=0.6)
        pyautogui.write(descricao) 
        pyautogui.doubleClick(548, 210,duration=0.6)
        pyautogui.write(novaDescricao)
        pyautogui.sleep(0.6)
        pyautogui.press('F2')
        pyautogui.sleep(0.6)
        pyautogui.press('enter')
        pyautogui.sleep(0.6)
        pyautogui.press('right')
        pyautogui.sleep(0.6)
        pyautogui.press('enter')
        pyautogui.sleep(0.6)
