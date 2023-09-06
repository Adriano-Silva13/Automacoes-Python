import pyautogui, time


with open('Arquivos_CSV/Multiplo_06_09_2023.csv','r') as arquivo:
    for linha in arquivo:
        item = linha.split(';')[0]
        pyautogui.doubleClick(212,190,duration = 0.5)
        pyautogui.write(item)
        pyautogui.press('enter')
        pyautogui.doubleClick(471,315, duration = 0.5)
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


