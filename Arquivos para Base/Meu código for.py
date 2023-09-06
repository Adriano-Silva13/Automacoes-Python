import pyautogui
with open('BRACAD.csv','r') as arquivo:
    for linha in arquivo:
        item = linha.split(';')[0]
        descricao = linha.split(';')[1]
        novaDescricao = linha.split(';')[2]
