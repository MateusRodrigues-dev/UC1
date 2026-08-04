class Biscoito:
    def __init__(self,sabor,gosto):
        self.sabor = sabor 
        self.gosto = gosto 
    
    def croc(self):
        return f'{self.sabor} faz croc croc'

biscoito1 = Biscoito("churrasco","defumado")
biscoito2 = Biscoito("requeijão","queijo")

print(f'O biscoito {biscoito1.sabor} tem o gosto {biscoito1.gosto}')
print(biscoito2.croc())