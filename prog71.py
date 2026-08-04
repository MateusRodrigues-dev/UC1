class Passarinho:
    def __init__(self,raça,cor):
        self.raça = raça 
        self.cor = cor 

    def cantar(self):
        return f'{self.raça} canta na floresta'

passarinho1 = Passarinho("bemtevi","verde")
passarinho2 = Passarinho("arara","azul")

print(f'O passarinho {passarinho1.raça} é da cor {passarinho1.cor}')
print(passarinho2.cantar())