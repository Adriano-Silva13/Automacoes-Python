import pyautogui
import time
vezespressionado=3
vezespressionado2=8
pyautogui.click(63, 500,duration=3)
time.sleep(0.5)
pyautogui.write('16418')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
for _ in range(vezespressionado):
    pyautogui.write('918')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
pyautogui.write('S',)
for _ in range(vezespressionado2):
        pyautogui.press('enter')
