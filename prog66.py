carros = []
contador = 1 
while contador <= 3:
    carro = input(f"Digite o nome do {contador}° carro: ")
    carros.append(carro)
    print("\nLista de carros:")
    for item in carros:
        print(item)
    contador += 1 