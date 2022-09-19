numero = int(input('Digite um numero inteiro: '))
ini = int(input('Digite por onde começar na tabuada: '))
fim = int(input('Digite até onde vai a tabuada: '))


if fim < ini:
    print('Voce digitou o fim menor que o inicio, execute o programa novamente. ')
else:
    for i in range(ini,fim+1): 
        re = numero*i 
        print(f'{numero} x {i} = {re}')
