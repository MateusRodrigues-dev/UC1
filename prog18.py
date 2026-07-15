print("VERIFICADOR DE TEMPERATURA")
temperatura = float(input("Diite a temperatura (°C): "))
if temperatura <18:
    print(f"\n Temperatura:{temperatura} °C")
    print("Está frio!")
elif temperatura >=18 and temperatura <= 30:
    print(f"\n Temperatura:{temperatura} °C")
    print("Clima Agradável!")
else:
    print(f"\n Temperatura:{temperatura} °C")
    print("está calor!")
