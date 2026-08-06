percentual = float(input("Digite o percentual de crescimento: "))

if percentual > 0:
    print("Houve crescimento")
elif percentual < 0:
    print("Houve um decrescimento")
else:
    print("Não houve mudança.")