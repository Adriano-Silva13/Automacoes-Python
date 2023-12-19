import pyautogui
from time import sleep
with open('Arquivos_CSV/ajuste_multiplo2.csv','r') as arquivo:
    for linha in arquivo:
        item = linha.split(';')[0]
        descricao = linha.split(';')[1]
        novaDescricao = linha.split(';')[2]
        pyautogui.doubleClick(219,188,duration=0.5)
        pyautogui.sleep(0.5)
        pyautogui.write(item)
        pyautogui.sleep(0.5) 
        pyautogui.press('enter')
        pyautogui.sleep(0.5)
        pyautogui.press('delete')
        pyautogui.sleep(0.5)
        pyautogui.write(novaDescricao)
        pyautogui.sleep(0.5)
        pyautogui.click(284,212,duration=1)
        pyautogui.sleep(0.5)
        pyautogui.write(descricao) 
        sleep(1)
