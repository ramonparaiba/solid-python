class Produto:
    def __init__(self, preco):
        self.preco = preco

class RegraDesconto:
    def calcular(self, produto):
        return produto.preco

class DescontoLivro(RegraDesconto):
    def calcular(self, produto):
        return produto.preco * 0.9

class DescontoComida(RegraDesconto):
    def calcular(self, produto):
        return produto.preco * 0.95
    

#Criando produtos
livro = Produto(100)
comida = Produto(50)
outro = Produto(200)

#Criando regras de desconto
desconto_livro = DescontoLivro()
desconto_comida = DescontoComida()
sem_desconto = RegraDesconto()

#Calculando preços com desconto
print(f"O Preço do Livro com desconto é: {desconto_livro.calcular(livro)}")
print(f"O Preço da Comida com desconto é: {desconto_comida.calcular(comida)}")
print(f"O Preço do Outro produto sem desconto é: {sem_desconto.calcular(outro)}") 
