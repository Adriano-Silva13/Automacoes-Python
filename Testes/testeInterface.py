import tkinter as tk

root = tk.Tk()
root.title("Minha Interface")

label = tk.Label(root, text="Bom dia !")
button = tk.Button(root, text="Defina os pontos de mapeamento")

# Use o gerenciador de layout para organizar os widgets na janela
label.pack()
button.pack()






root.mainloop()

