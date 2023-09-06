import pyautogui

with open('Arquivos CSV/cadastro colete.csv','r') as arquivo:
    for linha in arquivo:
        item = linha.split(';')[1]
        pyautogui.click(572, 295, duration=0.5)
        pyautogui.write(item)
        pyautogui.click(674, 391,duration=0.5)
        pyautogui.write(item)
        pyautogui.click(767, 492,duration=0.5)
        pyautogui.click(296, 524,duration=0.5)
        pyautogui.click(461, 568,duration=0.5)
        pyautogui.click(733, 476,duration=0.5)

