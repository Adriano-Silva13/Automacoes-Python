import tkinter as tk
import pyautogui
import time

def verificarposicao(wait_time=3):
    time.sleep(wait_time)
    x, y = pyautogui.position()
    return x, y

def exibir_resultado():
    resultado = verificarposicao()
    label_resultado.config(text=f"Cordenada 1 : {resultado}")


janela = tk.Tk()
janela.title("Minha Interface")

# Cria um rótulo (label) para exibir texto
label = tk.Label(janela, text="Clique no Botão para definir as posições a serem setadas")
label.pack(padx=10, pady=10)

label_resultado = tk.Label(janela, text="")
label_resultado.pack(padx=10, pady=10)

botao_calcular = tk.Button(janela, text="setar ponto", command=exibir_resultado)
botao_calcular.pack(padx=10, pady=10)
























janela.mainloop()