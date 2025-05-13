nome_produto = str(input("Informe o nome do produto"))
quantidade = int(input("Informe a quantidade vendida de produtos"))
preco_produto = float(input("Informe o preço unitario do produto"))

calcular = 0
mais_vendido = ""
quantidade_mais_vendida = 0



while nome_produto != 0 or quantidade != 0 or preco_produto != 0:

    nome_produto = str(input("Informe o nome do produto"))
    quantidade = int(input("Informe a quantidade vendida de produtos"))
    preco_produto = float(input("Informe o preço unitario do produto"))

    
    calcular = quantidade * preco_produto

    if quantidade > quantidade_mais_vendida:
        mais_vendido = nome_produto
        quantidade_mais_vendida = quantidade
        

print(f"O produto mais vendido é:  {nome_produto}")
print(f"A quantidade vendida do produto é: {quantidade} ")
print(f"O preço unitario do produto mais vendido é :{preco_produto}")
