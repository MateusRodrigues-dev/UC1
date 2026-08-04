print("VERIFICAÇÃO DE SEXO")
sexo = input("Digite M para Masculino ou F para Feminino:").strip().upper()
if sexo == "M":
    print("Sexo: Masculino")
elif sexo == "F":
    print("Sexo: Feminino")
else:
    print("Sexo não existe!")