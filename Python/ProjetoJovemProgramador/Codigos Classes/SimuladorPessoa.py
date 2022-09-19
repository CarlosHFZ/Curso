from ClassePessoa import Pessoa


pessoa = Pessoa("Carlos",50,30,20,50 )


print('Esse é um simulador RPG, você tem as seguintes açoes abaixo: \nOpção 1: Correr\nOpção 2: Dormir\nOpção 3: Comer\nOpção 4: Soltar Feitiço\nOpção 5: Encerrar')
print('')
print(pessoa)
c = 0
while True:
    if c == 10:
        pessoa.Nivel()
    if pessoa.vida == 0:
        print('Voce morreu')
        break
    c += 1
    if c == 2:
        print('\nOpção 1: Correr\nOpção 2: Dormir\nOpção 3: Comer\nOpção 4: Soltar Feitiço\nOpção 5: Encerrar')
    print('')
    r = int(input('oque deseja fazer? '))
    if r == 5:
        break
    if r == 1:
        pessoa.Correr()
        if pessoa.Correr() == 0:
            print('Sem energia')
    if r == 2:
        pessoa.Dormir()
    if r == 3:
        pessoa.Comer()
        if pessoa.fome >= pessoa.fome_maxima:
            print('Você ja está de barriga cheia')

            
    if r == 4:
        pessoa.Soltar_Feitiço()

    for i in range(10):
        pessoa.Perder_fome()
    
    if pessoa.fome <= 0:
        for i in range(15):
            pessoa.Tomar_Dano()
        print('Você esta morrendo de fome')
    print(pessoa)
