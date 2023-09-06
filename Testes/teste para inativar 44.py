import pyautogui
from time import sleep


'''img9 = pyautogui.locateOnScreen('automacoes finalizadas/Automacao processo fibra/Imagens mapeadas/comportamento.png')
edit_but9 = pyautogui.center(img9)
pyautogui.moveTo(edit_but9,duration=0.5)
pyautogui.click()
pyautogui.sleep(0.6)
img10 = pyautogui.locateOnScreen('automacoes finalizadas/Automacao processo fibra/Imagens mapeadas/configuracao.png')
edit_but10 = pyautogui.center(img10)
pyautogui.moveTo(edit_but10,duration=0.5)
pyautogui.doubleClick()
pyautogui.write('2')
pyautogui.press('F2')
pyautogui.sleep(0.8)
pyautogui.press('enter')
pyautogui.sleep(0.8)
pyautogui.press('right')
pyautogui.sleep(0.8)
pyautogui.press('enter')
pyautogui.sleep(0.8)
pyautogui.press('enter')
pyautogui.sleep(0.8)
pyautogui.press('delete')
pyautogui.write('POSTO DB - COLETE GOLA RED - MALHA DRY 3160 AMAR')
pyautogui.sleep(0.8)
pyautogui.press('F2')
pyautogui.sleep(0.8)
pyautogui.press('enter')
pyautogui.sleep(0.8)
pyautogui.press('right')
pyautogui.sleep(0.8)
pyautogui.press('enter')
img11 = pyautogui.locateOnScreen('automacoes finalizadas/Automacao processo fibra/Imagens mapeadas/agrupamentos.png')
edit_but11 = pyautogui.center(img11)
pyautogui.moveTo(edit_but11,duration=0.5)
pyautogui.doubleClick()
pyautogui.doubleClick()'''


with open('automacoes finalizadas/Automacao processo fibra/csv/cad colete.csv','r') as arquivo:
    for linha in arquivo:
        item = linha.split(';')[0]
        itemc = linha.split(';')[1]
        descricao = linha.split(';')[2]
        pcorigem = linha.split(';')[3]
        print(descricao)
