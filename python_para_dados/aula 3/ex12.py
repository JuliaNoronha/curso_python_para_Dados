quantidade_de_litros = float(input("Quantos litros você quer? "))
tipo = input("Qual combustível você quer? E - etanol, D - diesel: ")

tipo = tipo.upper()
preco_diesel = 2.00
preco_etanol = 1.70

if "E" == tipo:
    if quantidade_de_litros <= 15:
        desconto = preco_etanol * quantidade_de_litros * 0.02
        valor_pago = preco_etanol * quantidade_de_litros - desconto
        print(f"{valor_pago}")
    else:
        desconto = preco_etanol * quantidade_de_litros * 0.04
        valor_pago = preco_etanol * quantidade_de_litros - desconto
        print(f"{valor_pago}")

elif "D" == tipo:
    if quantidade_de_litros <= 15:
        desconto = preco_diesel * quantidade_de_litros * 0.03
        valor_pago = preco_diesel * quantidade_de_litros - desconto
        print(f"{valor_pago}")
    else:
        desconto = preco_diesel * quantidade_de_litros * 0.05
        valor_pago = preco_diesel * quantidade_de_litros - desconto
        print(f"{valor_pago}")

else:
        print("Tipo de combustível inválido.")