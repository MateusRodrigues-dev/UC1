while True:
    try:
        numero = int(input("Digite um número inteiro para saber a metade: "))
        metade = numero / 2 
        print(f'A metade de {numero} é {metade}')

        break
    
    except ValueError: 
        print("Erro: Você digitou letras. Por favor, digite um numero inteiro!")
        