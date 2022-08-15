import random

while True:

    r = str(input('Digite oque desejar embaralhar: '))
    print('')

    if r == '':
        print('Voce não digitou nada, digite novamente ')
        print('')
    
    if len(r) == 1:
        print('Voce digitou apenas um caractere, digite no minimo dois caracteres para o programa fazer sentido *_* ')
        print('')

    if r != '' and len(r) > 1:
        break
    

r = random.sample(r,len(r))


r = ''.join(r)
print(f'Oque foi escrito foi embaralhado assim: {r}')
