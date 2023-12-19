import pyautogui

with open('Arquivos_CSV/INCLUIR COLETE.csv','r') as arquivo:
    for linha in arquivo:
        item = linha.split(';')[0]
        pyautogui.doubleClick(207,274,duration = 0.5)
        pyautogui.sleep(0.5)
        pyautogui.write(item)
        pyautogui.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.sleep(0.5)
        pyautogui.doubleClick(589,344,duration=0.5)
        pyautogui.sleep(0.5)
        pyautogui.write('6201')
        pyautogui.sleep(0.5)
        pyautogui.press('F2')
        pyautogui.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.sleep(1)

