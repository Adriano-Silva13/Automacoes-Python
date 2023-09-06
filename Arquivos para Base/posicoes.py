import pyautogui
import time
import keyboard

pontos = []
print("Defina os Pontos a Ser Mapeados")
def mapear_ponto():
    while True:
        if keyboard.is_pressed('esc'):  # Pode ser a tecla que você quiser
            x, y = pyautogui.position()
            pontos.append((x, y))
            time.sleep(0.5)
            print("Ponto Mapeado, Vá para o Próximo !")
            break
        elif keyboard.is_pressed('ctrl+space'):
            break


for _ in range(100):
    mapear_ponto()

    
for posi in pontos:
    print(f"Esta é a posição mapeada X: {posi[0]} Y: {posi[1]}")