valor = float(input("Digite o valor do produto:  "))

soma_valor = 0
quantidade = 0

while valor != 0:
     quantidade = quantidade + 1
     soma_valor = valor + soma_valor

     valor = float(input("Digite o valor do produto:  "))

        
print(f"O valor das soma dos produtos é : {soma_valor:.2f}")
print(f"A quantidade de produtos é: {quantidade}")