try:
    hora = int(input("Digite a hora do dia: "))
    if hora >= 0 and hora <= 11:
        print(f"Bom dia!")
    elif hora >= 12 and hora <= 17:
        print(f"Boa tarde!")
    elif hora >= 18 and hora <= 24:
        print(f"Boa noite!")
    else:
        print(f"O valor digitado é invalido!")
except ValueError:
    print("O valor digitado é invalido!")
