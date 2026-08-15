vendas_2022 = int(input("Qual a quantidade de vendas no ano de 2022?: "))
vendas_2023 = int(input("Qual a quantidade de vendas no ano de 2023?: "))

diferenca_vendas = vendas_2023 - vendas_2022

if vendas_2022 == 0:
    print("Valor de vendas de 2022 é zero, não dá pra fazer a variação percentual.")
else:
    variacao = (diferenca_vendas/vendas_2022) * 100
    if variacao > 20:
        print(f"{variacao}")
        print("Bonificação para o time de vendas.")
    elif 2 <= variacao <= 20:
        print(f"{variacao}")
        print("Pequena bonificação para o time de vendas.")
    elif -10 <= variacao < 2:
        print(f"{variacao}")
        print("Planejamento de políticas de incentivo às vendas.")
    else:
        print(f"{variacao}")
        print("Corte de gastos.")