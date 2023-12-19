import pyautogui

with open('Arquivos_CSV/INCLUIR COLETE.csv','r') as arquivo:
    for linha in arquivo:
        item = linha.split(';')[0]
        grupo = linha.split(';')[4]
        subgrupo = linha.split(';')[5]
        pyautogui.doubleClick(213,190,duration = 0.2)
        pyautogui.sleep(0.5)
        pyautogui.write(item)
        pyautogui.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.sleep(0.5)
        pyautogui.write(grupo)
        pyautogui.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.sleep(0.5)
        pyautogui.write(subgrupo)
        pyautogui.sleep(0.5)
        pyautogui.press('F2')
        pyautogui.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.sleep(0.5)
        pyautogui.press('right')
        pyautogui.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.sleep(1)

