turno = input("Olá, você estuda em qual turno? (responda: manhã, tarde ou noite)")

turnoEstudado = turno.lower()

if turnoEstudado == "manhã":
    print(f"Bom Dia!")
elif turnoEstudado == "tarde":
    print(f"Boa Tarde!")
elif turnoEstudado == "noite":
    print(f"Boa Noite!")
else:
    print(f"Valor Inválido!")