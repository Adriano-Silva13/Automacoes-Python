with open('Arquivos CSV/arquivo_extracao.csv','r') as arquivo:
    for linha in arquivo:
        item = linha.split(';')[0]
        string_original = str(item)
        posicao = string_original.find("-")
        texto_apos_hifen = string_original[:posicao]
        texto_contatenado = str(texto_apos_hifen) + "ZZ"
        print(texto_contatenado)