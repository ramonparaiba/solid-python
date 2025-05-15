from abc import ABC, abstractmethod
class Veiculo:
    @abstractmethod
    def andar(self):
        print("Andando")
    @abstractmethod
    def voar(self):
        print("Voando")
    
class Carro(Veiculo):
    def andar(self):
        print("Carro andando")    
    def voar(self):
        raise Exception("Carro não pode voar")