def calcula_taxa(rendimento, deducao, pais):
    rendimento_taxavel = rendimento - deducao
    if pais == "India":
        montante_taxado = rendimento_taxavel * 0.3
    elif pais == "US":
        montante_taxado = rendimento_taxavel * 0.25
    elif pais == "UK":
        montante_taxado = rendimento_taxavel * 0.2
    else:
        montante_taxado = 0
    return montante_taxado