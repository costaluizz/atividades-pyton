class Retangulo:
    def __init__(self,largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return 2 * (self.largura + self.altura)
    
retangulo1 = Retangulo(4,6)
retangulo2 = Retangulo(24,16)
retangulo3 = Retangulo(3,2)

print(f"Área do retângulo: {retangulo1.area()}")
print(f"Perimetro do retângulo: {retangulo3.perimetro()}")