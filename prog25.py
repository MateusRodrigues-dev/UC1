
n1=int(input("Digite um numero: "))
n2=int(input("Digite outro numero: "))
op=print("Escolha a operação: ")
print("1 - Soma")
print("2 - Subtração")
print("3- Multiplicação")
print("4 - Divisão")
op= int(input("Escolha a operação" ))
match op:
    case 1:
        t=n1+n2
    case 2:
        t=n1-n2
    case 3:
        t=n1*n2
    case 4:
        t=n1/n2
    case _:
        t=0
        print("Operação Inválida")
print(f"O resultado da operação é {t}")
print("teste de commit")

