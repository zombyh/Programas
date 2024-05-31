nome = "Marcelo Rocha"
indice = 0
tamanho = len(nome)
novo_nome = ""

while indice < tamanho:
    letra = nome[indice]
    novo_nome += f'|{letra}'
    indice += 1
    print(novo_nome)

novo_nome += '|'
print(novo_nome)
