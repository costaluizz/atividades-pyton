class Produto:
    def __init__(self,nome,preco,quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def vender(self,qtd):
        if self.quantidade_estoque >= qtd:
            self.quantidade_estoque -= qtd
        else:
            print("Sem estoque")
    
    def repor(self,qtd):
        self.quantidade_estoque += qtd

    
    def dados(self):
        print (f"Produto: {self.nome} o preço é R${self.preco:.2f} e a quantidade é: {self.quantidade_estoque}")

nome=str(input("Qual o nome do produto:  "))
qtd=int(input("Informe a quantidade de produtos:  "))
valor=float(input("Informe o valor do produto:  "))
vender=int(input("Insira a quantidade de produtos vendidos:  "))
repor=int(input("Insira a quantidade de produtos que foram repostos:  "))

p =Produto(nome,valor,qtd)
p.vender(vender)
p.repor(repor)
p.dados()