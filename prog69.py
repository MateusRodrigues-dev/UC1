class Roupas:
    def __init__(self,tipo,cor):
        self.tipo = tipo 
        self.cor = cor

    def vestir(self):
        return f'{self.cor} caiu bem'

roupa1 = Roupas("camisa","branca")
roupa2 = Roupas("blusa","vermelha")

print(f'Sua {roupa1.tipo} é bonita com a cor {roupa1.cor}')
print(roupa1.vestir())
