import pyautogui
from time import sleep

with open('automacoes finalizadas/Automacao processo fibra/csv/cad colete.csv','r') as arquivo:
    for linha in arquivo:
        itemc = linha.split(';')[1]
        pyautogui.doubleClick(247,211,0.5)
        pyautogui.write(itemc)
        pyautogui.doubleClick(519,236,0.5)
        pyautogui.write(itemc)
        pyautogui.sleep(0.5)
        pyautogui.press('F2')
        pyautogui.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.sleep(0.5)
