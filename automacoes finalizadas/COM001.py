import pyautogui
import time


pyautogui.click(68, 590,duration=2)
with open('csv/INSERIR COM001 B.csv','r') as arquivo:
    for linha in arquivo:
        sequencia = linha.split(';')[0]
        item = linha.split(';')[1]
        vezesPressionado = 3
        vezesPressionado2 = 8
        time.sleep(0.5)
        pyautogui.write(sequencia)
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)
        for _ in range(vezesPressionado):
            pyautogui.write(item)
            time.sleep(0.5)
        pyautogui.write('S',)
        for _ in range(vezesPressionado2):
            pyautogui.press('enter')




        