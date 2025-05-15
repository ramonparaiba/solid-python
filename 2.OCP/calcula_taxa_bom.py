class calcula_taxa:
    def calcula_taxa(self, rendimento, deducao):
        rendimento_taxavel = rendimento - deducao
        return rendimento_taxavel
    
class calcula_taxa_India(calcula_taxa):
    def calcula_taxa(self, rendimento, deducao):
        rendimento_taxavel = rendimento - deducao
        return rendimento_taxavel * 0.3
    
class calcula_taxa_US(calcula_taxa):
    def calcula_taxa(self, rendimento, deducao):
        rendimento_taxavel = rendimento - deducao
        return rendimento_taxavel * 0.25
class calcula_taxa_UK(calcula_taxa):
    def calcula_taxa(self, rendimento, deducao):
        rendimento_taxavel = rendimento - deducao
        return rendimento_taxavel * 0.2

class default_taxa(calcula_taxa):
    def calcula_taxa(self, rendimento, deducao):
        return 0

# Test the classes
calculo_india = calcula_taxa_India()
print(calculo_india.calcula_taxa(1000, 200))  # Output: 240.0
calculo_us = calcula_taxa_US()
print(calculo_us.calcula_taxa(1000, 200))  # Output: 200.0
calculo_uk = calcula_taxa_UK()
print(calculo_uk.calcula_taxa(1000, 200))  # Output: 160.0
calculo_default = default_taxa()
print(calculo_default.calcula_taxa(1000, 200))  # Output: 0
