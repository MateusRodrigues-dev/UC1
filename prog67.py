mercado =[]
item = input("Digite um item do mercado (Ou SAIR para encerrar): ").upper()
while item != "SAIR":
    if item in mercado:
        print("item já cadastrado")
    else:
        mercado.append(item)
        print("\nLista de compras:")
        for produto in mercado:
            print(produto)
    item = input("\nDigite outro item (ou SAIR para encerrar): ").upper()
    print("\nLista de final de compras:")
    for produto in mercado:
        print(produto)