class Veiculo:
    def __init__(self,modelo,_combustivel):
        self.modelo=modelo
        self._combustivel= _combustivel

    def abastecer(self,litros):
        if litros > 0 :
            self._combustivel += litros
        else:
            print("Valor Invalido")

    def get_combustivel(self):
        return self._combustivel
    
    def exibir_info(self):
        print(self.modelo)
        print(self._combustivel)

class Carro(Veiculo):
    def abastecer (self,litros):
        print(f"O carro {self.modelo} foi abastecido")
        return super().abastecer(litros)

class Moto(Veiculo):
    def abastecer(self, litros):
            print(f"A moto {self.modelo} foi abastecida")
            return super().abastecer(litros)

veiculo1=Carro("HILUX",10)
veiculo2=Moto("cb",5)

veiculo1.abastecer(5)
veiculo2.abastecer(5)
veiculo1.exibir_info()
veiculo2.exibir_info()

        