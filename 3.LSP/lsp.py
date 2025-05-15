class Forma:
    def area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado


#Implementação
retangulo = Retangulo(5, 10)
quadrado = Quadrado(4)

print(f"A área do retângulo é: {retangulo.area()}")
print(f"A área do quadrado é: {quadrado.area()}")