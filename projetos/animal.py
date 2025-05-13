nome_animal=str(input("Qual o nome do animal?:   "))
especie=str(input("Qual a especie do animal?:  "))
peso=float(input("Qual o peso atual do animal?:  "))
qtd=float(input("Qual a quantidade de ração que o animal comeu?: "))

class Animal:
    def __init__(self,nome_animal,especie,peso):
        self.nome_animal = nome_animal
        self.especie = especie
        self.peso = peso

    
    def alimentar(self,quantidade):
        self.peso += quantidade * 0.2
    

    def info (self,quantidade):
        print(self.nome_animal)
        print(self.peso)
        print(self.especie)
        print(f"O nome do animal é : {self.nome_animal}, a espécie é {self.especie} o peso atual: {self.peso}KG a quantidade de ração que o animal comeu foi {quantidade}kg ")

    def verificar_dieta(self):
        if self.peso >= 40:
            print("Animal com Sobrepeso")
        else: 
            print("Animal dentro do peso apropriado")

animal1= Animal(nome_animal,especie,peso)
animal1.alimentar(qtd)
animal1.info(qtd)
animal1.verificar_dieta()

    
    
      
