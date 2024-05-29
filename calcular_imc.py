# Calculadora de IMC por Marcelo Rocha
try:
    nome = input('Digite seu nome? ')
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite sua altura: "))
    imc = peso / (altura * altura)
    print(imc)
    if imc < 18.5:
        print(f'{nome} você está abaixo do peso')
    elif 18.5 <= imc < 25.0:
        print(f'{nome} você está no peso ideal')
    elif 25.0 <= imc < 30.0:
        print(f'{nome} você está com sobrepeso')
    elif 30.0 <= imc < 40.0:
        print(f'{nome} você está com obesidade')
except ValueError:
    print('Valor inválido!')
