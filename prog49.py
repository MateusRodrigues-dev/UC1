print("===Comanda do Garçom===")
total = 0 
valor = float(input("Digite o valor do item(0 para finalizar) "))
while valor != 0:
    total = total + valor 
    valor = float(input("Digite o valor do próximo item (0 para finalizar): "))
taxa = total *0.10 
total_final = total + taxa 
print("====Conta====")
print(f"Total dos itens: R$ {total:.2f}")
print(f"Taxa de serviço (10%): R$ {taxa:.2f}")
print(f"Total a pagar: R${total_final:.2f}")
