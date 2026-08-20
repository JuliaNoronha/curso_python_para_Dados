for avaliacao in range(15):
    nota = int(input("Digite sua nota de 0 a 5: "))
    while nota < 0 or nota > 5:
        nota = int(input("Digite a nota novamente de 0 a 5: "))
