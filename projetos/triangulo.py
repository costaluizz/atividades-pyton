valor_1 =float(input("Digite o valor do primeiro lado"))
valor_2 =float(input("Digite o valor do segundo lado "))
valor_3 = float(input("Digite o valor do terceiro lado"))



if valor_1 + valor_2 > valor_3 and valor_1 + valor_3 > valor_2 and valor_2 + valor_3 > valor_1 :
    print("Os valores podem formar um triangulo")
else:
    print("Não é possivel formar um triangulo")
