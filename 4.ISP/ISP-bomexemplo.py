from abc import ABC, abstractmethod

class Movel:
    @abstractmethod
    def andar(self):
        print("Andando")

class Voador:
    @abstractmethod
    def voar(self):
        print("Voando")

class Carro(Movel):
    def andar(self):
        print("Carro andando")
    
class Bimotor(Movel, Voador):
    def andar(self):
        print("Bimotor taxeando")
    
    def voar(self):
        print("Bimotor voando")