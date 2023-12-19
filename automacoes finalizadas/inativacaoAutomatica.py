import pyautogui
from time import sleep
with open('Arquivos_CSV\INATIVAR 11-10-23.csv','r') as arquivo:
    for linha in arquivo:
        item = linha.split(';')[0]
        descricao = linha.split(';')[1]
        itemc = linha.split(';')[2]
        mensagem_descricao = linha.split(';')[3]
        pyautogui.doubleClick(223,190,duration=0.2)
        pyautogui.sleep(0.2)
        pyautogui.write(item)
        pyautogui.sleep(0.2) 
        pyautogui.press('enter')
        pyautogui.sleep(0.2)
        pyautogui.press('delete')
        pyautogui.sleep(0.2)
        pyautogui.write(mensagem_descricao)
        pyautogui.sleep(0.2)
        pyautogui.doubleClick(662,307,duration=0.2)
        pyautogui.sleep(0.2)
        pyautogui.press('tab')
        pyautogui.write(descricao)
        pyautogui.sleep(0.2)
        pyautogui.press('tab')
        pyautogui.sleep(0.2)
        pyautogui.press('F2')
        pyautogui.sleep(0.2)
        pyautogui.press('enter')
        pyautogui.sleep(0.2)
        pyautogui.press('right')
        pyautogui.sleep(0.2)
        pyautogui.press('enter')
        sleep(0.2)
