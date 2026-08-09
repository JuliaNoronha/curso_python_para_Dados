num1 = int(input("Escreva um número: "))
num2 = int(input("Escreva um segundo número: "))
num3 = int(input("Escreva um terceiro número: "))

if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
elif num3 >= num1 and num3 >= num2:
    maior = num3

if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
elif num3 <= num1 and num3 <= num2:
    menor = num3

meio = num1 + num2 + num3 - menor - maior

print(f"Números em ordem decrescente: {maior}, {meio}, {menor}")