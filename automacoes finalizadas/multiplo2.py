import pyautogui, time


with open('Arquivos_CSV/teste.csv','r') as arquivo:
    for linha in arquivo:
        item = linha.split(';')[0]
        #CODIGO PRODUTO
        pyautogui.doubleClick(218,189,duration = 0.5)
        pyautogui.write(item)
        pyautogui.press('enter')
        #VENDA MULTIPLA
        pyautogui.doubleClick(466,314, duration = 0.5)
        pyautogui.write('2')
        time.sleep(0.2)
        pyautogui.press('F2')
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(0.2)
        pyautogui.press('right')
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(0.2)


