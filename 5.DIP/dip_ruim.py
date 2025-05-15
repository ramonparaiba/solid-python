class Email:
    def enviar(self, mensagem):
        print(f"Enviando email: {mensagem}")

class Notificacao:
    def __init__(self):
        self.email = Email()

    def enviar_notificacao(self, mensagem):
        self.email.enviar(mensagem)