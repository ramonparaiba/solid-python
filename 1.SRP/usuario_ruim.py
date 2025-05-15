class Usuario: 
    def salvar_usuario(self, nome):
        print(f"Salvando o usuário {nome} no banco de dados")

    def enviar_email(self, email):
        print(f"Enviando email para {email}")

#inicializando a classe
usuario = Usuario()
#chamando os métodos
usuario.salvar_usuario("João")
usuario.enviar_email("maria@gmail.com")

