nome = str(input('Qual o nome do piloto? '))
km_h = 0
velo_maxima = 0
c = 0

def acelerar():
    global km_h
    km_h += 5
    if km_h > 100:
        print('')
        print('Velocidade acima do permitido, desacelerando veiculo. ')
        print('')
        km_h -= 5
def desacelerar():
    global km_h
    km_h -= 5
    if km_h <= 0:
        km_h = 0
        print('')
        print('O veiculo está parado! ')
        print('')
def info():
    global km_h, nome, c
    c -= 1
    print('')
    print(f'Nome do piloto é {nome} \nVelocidade Atual do veiculo: {km_h}km/h \nHoras rodadas: {c} horas')
    print('')
    return
def maxima():
    global km_h, velo_maxima
    if km_h > velo_maxima:
        velo_maxima = km_h
def simular():
    global c, km_h, velo_maxima, nome
    while True:
        c += 1
        print('')
        print('Digite de 1 a 4 para qual ação deseja fazer: ')
        print('1 - Acelerar \n2 - Desacelerar \n3 - Mostrar informações \n4 - Finalizar Corrida')
        print('')
        r = str(input('Oque deseja fazer? '))
        maxima()
        if r == "1":
            acelerar()
        elif r == "2":
            desacelerar()
        elif r == "3":
            info()
        elif r == "4":
            print('')
            print('Corrida finalizada.')
            print(f'Velocidade maxima atingida: {velo_maxima}km/h \nTotal de horas rodadas: {c} horas')
            print(f'Programa encerrado, Bom descanso {nome}')
            break
        else:
            
            print('Opção incorreta, digite novamente')
            c -= 1
            
simular()


