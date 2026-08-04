def verificar_media (n1,n2,n3,n4):
    media =(n1 + n2 + n3 + n4)/4 
    print(F"\nMédia do aluno: {media:.2f}")
    if media >=7:
        print("Situação: Aprovado")
    elif media >=5:
        print("Situação: Recuperação")
    elif media <= 4:
        print("Situação: Reprovado")
nota1 = float(input("Digite a 1º nota: "))
nota2 = float(input("Digite a 2º nota: "))
nota3 = float(input("Digite a 3º nota: "))
nota4 = float(input("Digite a 4º nota: "))
verificar_media(nota1,nota2,nota3,nota4)