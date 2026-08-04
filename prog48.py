total = 0 
print("=== TABELA DE PRODUTOS===")
print("001 -> Arroz (R$ 4.00)")
print("002 -> Feijão (R$ 7.00)")
print("003 -> Macarrão (R$ 5.00)")
print("Digite 0 para encerrar.")
codigo = input("Digite o código do produto: ")
while codigo != "0":
    if codigo == "001":
        print("Produto adiciondo: Arroz")
        total += 4 
    elif codigo == "002":
        print("Produto adicionado: Feijão")
        total += 7 
    elif codigo == "003":
        print("Produto adicionado: Macarrão")
        total += 5
    else:
        print("Código Inválido!")
    codigo = input("Digite outro código: ")
print("Compra finalizada")
print(f"Total da Compra: R${total:.2f}")