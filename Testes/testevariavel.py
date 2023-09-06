import tkinter as tk

def mostrar_valor():
    valor = entrada.get()  # Obtém o valor do campo de entrada
    label_resultado.config(text=f"Você inseriu: {valor}")

janela = tk.Tk()
janela.title("Recebendo Variável")

# Cria um campo de entrada de texto
entrada = tk.Entry(janela)
entrada.pack(padx=10, pady=10)

# Cria um botão que chama a função mostrar_valor
botao = tk.Button(janela, text="Mostrar Valor", command=mostrar_valor)
botao.pack(padx=10, pady=10)

# Cria o rótulo vazio para exibir o resultado
label_resultado = tk.Label(janela, text="")
label_resultado.pack(padx=10, pady=10)

janela.mainloop()