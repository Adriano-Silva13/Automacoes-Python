import pyautogui

# Definir as variáveis globais para armazenar os pontos
ponto1 = None
ponto2 = None

def mapear_ponto():
    global ponto1, ponto2
    print("Mova o cursor para o ponto desejado na tela.")
    print("Pressione Ctrl+C para interromper.")
    try:
        while True:
            x, y = pyautogui.position()
            position_str = f"X: {x}, Y: {y}"
            print(position_str, end="\r")
    except KeyboardInterrupt:
        print("\nPonto mapeado.")
        return x, y

if __name__ == "__main__":
    # Mapear pontos usando a função e atribuir aos pontos globais
    ponto1 = mapear_ponto()
    ponto2 = mapear_ponto()

    # Agora, ponto1 e ponto2 podem ser acessados a qualquer momento no código
    if ponto1:
        print("Coordenadas do ponto 1:", ponto1)
    if ponto2:
        print("Coordenadas do ponto 2:", ponto2)