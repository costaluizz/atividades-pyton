peso = float(input("Digite o Peso: "))
altura = float(input("Digite a altura: "))

imc = peso / (altura * 2)

if imc <= 18.5:
    print("Abaixo do Peso")

if imc >= 18.5 and imc <= 24.9:
    print("Peso Normal")

if imc >= 25 and imc <= 29.9:  
    print("Sobrepeso")

if imc >= 30:
    print("Obesidade")  
    