r = ("Sim")

while r == "Sim":
    x = int(input("Digite o valor de X:"))
    y = int(input("Digite o valor de Y:"))
    if x == y:
        print('O valor de X é igual a Y.')
    elif x > y:
        print('X é maior que Y')
    elif x < y:
        print('X é menor que Y.')
    r = input("Voce deseja digitar novamente? Digite Sim ou Não: ")