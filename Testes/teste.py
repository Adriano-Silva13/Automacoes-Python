import pyautogui


img11 = pyautogui.locateOnScreen('automacoes finalizadas/Automacao processo fibra/Imagens mapeadas/complemento.png')
edit_but11 = pyautogui.center(img11)
pyautogui.moveTo(edit_but11,duration=0.5)
pyautogui.click()
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.write('item')
img11 = pyautogui.locateOnScreen('automacoes finalizadas/Automacao processo fibra/Imagens mapeadas/comportamento.png')
edit_but11 = pyautogui.center(img11)
pyautogui.moveTo(edit_but11,duration=0.5)
pyautogui.click()
pyautogui.sleep(0.6)
img11 = pyautogui.locateOnScreen('automacoes finalizadas/Automacao processo fibra/Imagens mapeadas/configuracao.png')
edit_but11 = pyautogui.center(img11)
pyautogui.moveTo(edit_but11,duration=0.5)
pyautogui.doubleClick()
pyautogui.write('2')
pyautogui.press('F2')
pyautogui.press('enter')
pyautogui.press('right')
pyautogui.press('enter')
img11 = pyautogui.locateOnScreen('automacoes finalizadas/Automacao processo fibra/Imagens mapeadas/agrupamentos.png')
edit_but11 = pyautogui.center(img11)
pyautogui.moveTo(edit_but11,duration=0.5)
pyautogui.click()



