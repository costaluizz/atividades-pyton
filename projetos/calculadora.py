print("--------------------Calculadora--------------------")
print("-----1=soma--2=subtração--3=divisão--4=multiplicação-----")
operacao=str(input("Escolha a operação que deseja ser utilizada:   "))
valor1=float(input("Digite o primeiro valor:   "))
valor2=float(input("Digite o segundo valor:    "))

soma = valor1 + valor2
subtracao= valor1-valor2
divisao= valor1 / valor2
multiplicacao= valor1 * valor2

if operacao == "1":
    print(f"O resultado é {soma:,.2f}")
elif operacao == "2":
    print(f"O resultado é {subtracao:,.2f}")
elif operacao == "3":
    print(f"O resultado é {divisao:,.2f}")
elif operacao == "4":
    print(f"O resultado é {multiplicacao:,.2f}")
else:
    print("------Escolha uma opção valida enter 1 a 4-------")
   
