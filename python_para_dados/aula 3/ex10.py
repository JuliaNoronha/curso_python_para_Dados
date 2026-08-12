num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
operacao = input("Qual operação quer fazer? escolha entre soma, subtração, multiplicação e divisão ")

operacao = operacao.lower()
resultado = None;

if "soma" in operacao:
    resultado = num1 + num2
    print(f"{resultado}")
elif "subtracao" in operacao:
    resultado = num1 - num2
    print(f"{resultado}")
elif "multiplicacao" in operacao:
    resultado = num1 * num2
    print(f"{resultado}")
elif "divisao" in operacao:
    if num2 == 0:
        print("O denominador não pode ser zero.")
    else:
        resultado = num1 / num2
        print(f"{resultado}")

if resultado is not None:
    if resultado.is_integer():
        print("Número inteiro")

        if (resultado % 2) == 0:
            print("Número par")
        else:
            print("Número ímpar")

        if resultado < 0:
            print("Número negativo.")
        else:
            print("Número positivo.")
    else:
        print("Número decimal")
