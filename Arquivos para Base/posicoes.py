import pyautogui
import time
import keyboard

quantidade_chamadas = 5
pontos = []

def mapear_ponto():
    print("Pressione uma tecla para mapear o ponto...")
    while True:
        if keyboard.is_pressed('esc'):  # Pode ser a tecla que você quiser
            x, y = pyautogui.position()
            pontos.append((x, y))
            time.sleep(0.5)
            break
for _ in range(quantidade_chamadas):
    mapear_ponto()

for posi in pontos:
    print(f"Esta é a posição mapeada {posi}")