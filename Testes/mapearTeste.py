import time,pyautogui
def verificarposicao(wait_time=3):
    time.sleep(wait_time)
    x, y = pyautogui.position()
    return x, y
def mapear_pontos():
    pontos_mapeados = {}  # Inicializa um dicionário para armazenar os pontos mapeados
    
    print("Comece o mapeamento. Pressione 'q' para parar.")

    while True:
        ponto = input("Digite as coordenadas do ponto (x y): ")
        
        if ponto == 'q':
            break  # Sai do loop quando 'q' é pressionado
        
        try:
            x, y = map(int, ponto.split())
            pontos_mapeados[(x, y)] = True  # Armazena o ponto no dicionário
            print("Ponto mapeado:", (x, y))
        except ValueError:
            print("Entrada inválida. Digite as coordenadas no formato 'x y'.")

    print("\nPontos mapeados:")
    for ponto, _ in pontos_mapeados.items():
        print("Coordenadas:", ponto)

if __name__ == "__main__":
    mapear_pontos()






