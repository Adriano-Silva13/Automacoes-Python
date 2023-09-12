import pyautogui

with open('Arquivos_CSV/cadastros_do_mes_finalizado.csv','r') as arquivo:
    for linha in arquivo:
        item = linha.split(';')[1]
        pyautogui.click(577, 264, duration=0.2)
        pyautogui.write(item)
        pyautogui.click(668, 358,duration=0.2)
        pyautogui.write(item)
        pyautogui.click(762, 458,duration=0.2)
        pyautogui.click(315, 521,duration=0.2)
        pyautogui.click(467, 558,duration=0.2)
        pyautogui.click(736, 472,duration=0.2)

