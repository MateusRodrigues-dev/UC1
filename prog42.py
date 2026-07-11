carros = {}
for i in range(2):
    carro = input("Carro: ")
    marca = input("Marca: ")
    valor = float(input("Valor: "))
    carros[carro] = {
        "marca":marca,
        "valor": valor
    }
print(f"Lista de carros: {carros}")