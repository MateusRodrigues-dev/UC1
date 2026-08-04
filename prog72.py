try:
    idade = int(input("Digite a sua idade"))
    print(f'sua idade é {idade}')
except ValueError:
    print("Digite apenas numeros validos")
    