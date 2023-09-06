import pyautogui


with open('Arquivos_CSV/cadastros_do_mes_finalizado.csv','r') as arquivo:
    for linha in arquivo:
        item = linha.split(';')[0]
        itemc = linha.split(';')[1]
        descricao = linha.split(';')[2]
        pcorigem = linha.split(';')[3]
        pyautogui.doubleClick(217,101,duration = 0.3)
        pyautogui.write(item)
        pyautogui.press('enter')
        pyautogui.click(662,125,duration = 0.3)
        pyautogui.click(586,227,duration = 0.3)
        pyautogui.write(itemc)
        pyautogui.click(846,466,duration = 0.3)
        pyautogui.click(537,221,duration = 0.3)
        pyautogui.press('enter')
        pyautogui.doubleClick(537,221,duration = 0.3)
        pyautogui.write('4')
        pyautogui.press('tab')
        pyautogui.write('4')
        pyautogui.click(636,378,duration = 0.3)
        pyautogui.write(pcorigem)
        pyautogui.click(855,467, duration = 0.3)
        pyautogui.sleep(0.2)
        for i in range(5):
            pyautogui.press('enter')
            pyautogui.sleep(0.1)
        pyautogui.press('down')
        pyautogui.press('enter')
        for i_2 in range(2):
            pyautogui.sleep(0.1)
            pyautogui.press('enter')
            pyautogui.sleep(0.1)
            pyautogui.press('up')
        for i_3 in range(5):
            pyautogui.press('enter')
        pyautogui.press('up')
        pyautogui.click(848,468,duration = 0.3)
        pyautogui.sleep(0.7)
        pyautogui.press('enter')
        pyautogui.sleep(0.2)
        pyautogui.click(541,474,duration = 0.3)
        pyautogui.doubleClick(217,101, duration = 0.3)
        pyautogui.write(itemc)
        pyautogui.sleep(0.2)
        pyautogui.press('enter')
        pyautogui.sleep(0.2)
        pyautogui.write(descricao)
        pyautogui.click(158,154,duration = 0.3)
        pyautogui.doubleClick(269,251, duration = 0.3)
        pyautogui.write(itemc)
        pyautogui.click(241,152,duration = 0.5)
        pyautogui.doubleClick(597,280,duration = 0.3)
        pyautogui.write('2')
        pyautogui.sleep(0.2)
        pyautogui.press('F2')
        pyautogui.sleep(0.2)
        pyautogui.press('enter')
        pyautogui.sleep(0.2)
        pyautogui.press('right')
        pyautogui.sleep(0.2)
        pyautogui.press('enter')
        pyautogui.sleep(0.2)
        
