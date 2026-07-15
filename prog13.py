nome = input("Digite seu nome: ")
nota1 = float(input("Digite a 1º nota: "))
nota2 = float(input("Digite a 2º nota: "))
nota3 = float(input("Digite a 3º nota: "))
nota4 = float(input("Digite a 4º nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"{nome}, sua média é {media:.2f}")
if media >= 6:
    print("Aprovado")
else:
    print("Recuperação")
