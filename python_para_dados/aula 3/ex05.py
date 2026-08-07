macarrao = float(input("Preço do macarrão: "))
trigo = float(input("Preço do trigo: "))
arroz = float(input("Preço do arroz: "))

if macarrao == trigo == arroz:
    print(f"Os 3 são do mesmo valor")
elif macarrao == trigo < arroz:
    print(f"Produtos mais baratos são o macarrão e trigo.")
elif macarrao == arroz < trigo:
    print(f"Produtos mais baratos são o macarrão e o arroz.")
elif trigo == arroz < macarrao:
    print(f"Produtos mais baratos são o trigo e o arroz.")
elif macarrao < arroz and macarrao < trigo:
    print("Macarrão é o mais barato.")
elif arroz < macarrao and arroz < trigo:
    print("Arroz é o mais barato.")
elif trigo < macarrao and trigo < arroz:
    print("Trigo é o mais barato.")
