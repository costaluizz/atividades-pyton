from abc import ABC, abstractmethod

class Planta (ABC):
    def __init__(self,nome_comun,nome_cientifico,umidade,luz):
        self.nome_comun = nome_comun
        self.nome_cientifico = nome_cientifico
        self._umidade = umidade
        self._luz = luz
    @abstractmethod
    def verificar_cuidados (self):
        pass
    def exibir_info(self):
        print(f"O nome comun  da planta é: {self.nome_comun};o nome científico: {self.nome_cientifico}. e {self._umidade}")
        print("-----------------------------")
    
    def get_umidade(self):
        return self._umidade
    
    def set_umidade(self,umidade):
        if umidade > 0 and umidade < 100:
            self._umidade = umidade
        else:
            print("Valores de umidade invalidos")

    def get_luz(self):
        return self._luz
    
    def set_luz(self,luz):
        if  luz > 0 and luz < 100:
            self._luz = luz
        else:
            print("Valores invalidos")

class Cacto(Planta):
    def __init__(self,nome_comun,nome_cientifico,umidade,luz):
        super().__init__( nome_comun,nome_cientifico,umidade,luz)
    
    def verificar_cuidados(self):
        if self._umidade < 30 and self._luz > 70:
            print("A planta está dentro dos parametros corretos: pouca água")
        else:
            print("A planta está fora  do padrao ideal de cuidados")

class Flor(Planta):
    def __init__(self,nome_comun,nome_cientifico,umidade,luz):
        super().__init__( nome_comun,nome_cientifico,umidade,luz)

    def verificar_cuidados (self):
        if self._umidade >= 40 and self._umidade <= 70 and self._luz >= 50 and self._luz <= 80:
            print("A planta está dentro dos cuidados esperados") 
        else:
            print("A planta está fora  do padrao ideal de cuidados")

class PlantaAquatica(Planta):
        def __init__(self,nome_comun,nome_cientifico,umidade,luz):
            super().__init__(nome_comun,nome_cientifico,umidade,luz)
        
        def verificar_cuidados(self):
            if self._umidade > 90 and self._luz < 50:
               print("A planta está dentro dos cuidados esperados: pouca luz")
            else:
                print("A planta está fora  do padrao ideal de cuidados")

nome = str(input("Qual o nome da planta?:  "))
nome_cientifico = str(input("Qual nome cientifico da planta?: "))
tipo = str(input("Qual o tipo da planta: "))
luz = float(input("Qual a quantidade de luz que a planta recebe?:  "))
umidade= float(input("Qual a quantidade de umidade que a planta recebe: "))

plantas = [nome,tipo,luz,umidade]



def monitorar_estufa():

    if tipo == "cacto":
        planta_teste = Cacto(nome,nome_cientifico,umidade,luz)
    elif tipo == "flor":
        planta_teste = Flor(nome,nome_cientifico,umidade,luz)
    elif tipo == "planta aquatica":
        planta_teste = PlantaAquatica(nome,nome_cientifico,umidade,luz)

    planta_teste.exibir_info()

    planta_teste.set_umidade(80)
    planta_teste.set_luz(80)

    planta_teste.exibir_info()
    planta_teste.verificar_cuidados()

               
monitorar_estufa(plantas)