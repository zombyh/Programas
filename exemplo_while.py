"""
Repetições while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1

    if contador == 5:
        print('Não vou mostrar o 5.')
        continue

    if contador >= 10 and contador <= 20:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 50:
        break


print('Fim')
