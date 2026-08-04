cf=input("Qual o seu cargo? ").upper()
if cf=="CAIXA":
   s=1500
elif cf=="VENDEDOR":
   s=2400
elif cf=="GERENTE":
   s=4000
else:
   s=0
   print("Cargo não existente")
inss= s*0.12
if s> 2000:
    irrf=s*0.14
else:
    irrf=s*0.08
sf=s - irrf-inss
print(f"O seu cargo de {cf} tem o salário de {s} e os impostos são: ")
print(f"INSS-> {inss}")
print(f"IRRF-> {irrf}")
print(f"Seu salário final é {sf}")