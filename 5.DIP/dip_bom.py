from abc import ABC, abstractmethod

class MeioDeEnvio:
    @abstractmethod
    def enviar(self):
        pass

class Email(MeioDeEnvio):
    def enviar(self):
        print("Enviando email")
        
class SMS(MeioDeEnvio):
    def enviar(self):
        print("Enviando SMS")

class Notificacao:
    def __init__(self, meio_de_envio: MeioDeEnvio):
        self.meio_de_envio = meio_de_envio

    def enviar_notificacao(self):
        self.meio_de_envio.enviar()