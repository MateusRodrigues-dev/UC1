try:
    numerador = int(input("Digite o numero a ser dividido"))
    denominador = int(input("Digite o valor da divisão"))

    resultado = numerador/ denominador
    print(f'O resultado é {resultado}')
except ValueError:
    print("Digite apenas numeros inteiros")

except ZeroDivisionError:
    print("Não pode dividir por zero")