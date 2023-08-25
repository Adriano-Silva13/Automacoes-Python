import pyautogui
from time import sleep
with open('BRACAD.csv','r') as arquivo:
    for linha in arquivo:
        item = linha.split(';')[0]
        descricao = linha.split(';')[1]
        novaDescricao = linha.split(';')[2]
        pyautogui.doubleClick(141,193,1)
        pyautogui.write(item) 
        pyautogui.press('enter')
        pyautogui.press('delete')
        pyautogui.click(103, 396, 1)
        pyautogui.write(descricao) 
        pyautogui.click(284,212,1)
        pyautogui.write(novaDescricao) 
        sleep(1)
