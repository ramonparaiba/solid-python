class Funcionario:
    def calcular_pagamento(self):
        pass

class Horista(Funcionario):
    def calcular_pagamento(self, horas_trabalhadas, valor_por_hora):
        return horas_trabalhadas * valor_por_hora

class Estagiario(Funcionario):
    def calcular_pagamento(self):
        print("Estagiário não tem pagamento definido.")
        return 0

# Implementação
horista = Horista()
estagiario = Estagiario()
horista_pagamento = horista.calcular_pagamento(40, 15)
estagiario_pagamento = estagiario.calcular_pagamento()
print(f"Pagamento do horista: R$ {horista_pagamento}")
print(f"Pagamento do estagiário: R$ {estagiario_pagamento}")

# O código acima é um exemplo de violação do Princípio da Substituição de Liskov (LSP).
