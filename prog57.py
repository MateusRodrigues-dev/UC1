<<<<<<< HEAD
def verificar_idade(ano_nascimento):
    ano_atual = 2026
    idade = ano_atual - ano_nascimento
    print(f"Idade :{idade} anos")
    if idade < 18:
        print("Menor de idade")
    elif idade >= 65:
        print("Idoso")
    else:
        print("Maior de idade")
ano = int(input("Digite o ano de nascimento: "))
=======
def verificar_idade(ano_nascimento):
    ano_atual = 2026
    idade = ano_atual - ano_nascimento
    print(f"Idade :{idade} anos")
    if idade < 18:
        print("Menor de idade")
    elif idade >= 65:
        print("Idoso")
    else:
        print("Maior de idade")
ano = int(input("Digite o ano de nascimento: "))
>>>>>>> dab6716 (teste commit pc casa)
verificar_idade(ano)