import random

pc = random.randint(1, 100)

contador = 0

numero = int(input('O computador pensou em um numero de 1 a 100, tente acertar, voce tem 5 chances, digite um numero: '))

while True:
    if numero != pc:
        if numero > pc:
            print("")
            print("O numero que voce digitou e maior que o numero no qual o computador pensou")
        else:
            print("")
            print("O numero que voce digitou e menor que o numero no qual o computador pensou")
        contador += 1
        numero = int(input(f"essa foi a tentativa {contador}, digite um numero novamente: "))
        if contador == 5:
            print("")
            print(f'o numero era {pc}, voce perdeu')
            break
    elif numero == pc:
        print("")
        print(f'o numero era {pc},!!!!Voce ganhou!!!!')
        break

