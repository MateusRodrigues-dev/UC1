for i in range(4):
    print(F"Cadastro do {i +1}° aluno")
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    nota3 = float(input("Digite a 3ª nota: "))
    media =(nota1 + nota2 + nota3)/ 3
    if media >=7:
        situação = "Aprovado"
    elif media >=5:
        situação = "Recuperação"
    else:
        situação = "Reprovado"
    print("Resultado")
    print("Nome:", nome)
    print("Nota 1:", nota1)
    print("Nota 2:", nota2)
    print("Nota 3:", nota3)
    print(f"Média: {media:.2f}")
    print("Situação:",situação)