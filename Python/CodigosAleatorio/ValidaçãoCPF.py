cpf = []

t1 = 0

while True:
    if t1 == 11:
        break
    r = str(input('Digite o numero do CPF separadamente para validação individual de cada numero: '))
    if r != '1' and r != '2' and r != '3' and r != '4' and r != '5' and r != '6' and r != '7' and r != '8' and r != '9' and r != '0':
        print('Digito incorreto, execute o programa novamente.')
        break
    r = int(r)
    cpf.append(r)
    t1 += 1

if t1 == 11:
    if cpf[0] == cpf[1] and cpf[0] == cpf[2] and cpf[0] == cpf[3] and cpf[0] == cpf[4] and cpf[0] == cpf[5] and cpf[0] == cpf[6] and cpf[0] == cpf[7] and cpf[0] == cpf[8] and cpf[0] == cpf[9] and cpf[0] == cpf[10]:
        print(f'O CPF {cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]} é invalido')  
    else:

        m = 0
        total = 0
        c = 10

        while True:
            if c == 1:
                break 
            total += cpf[m]*c
            m += 1
            c += -1
        
        total = ((total*10)%11)
        if total == 10:
            total = 0

        if total == cpf[-2]:    
            c1 = 11
            total2 = 0
            m1 = 0

            while True:
                if c1 == 1:
                    break 
                total2 += cpf[m1]*c1
                m1 += 1
                c1 += -1

            total = ((total2*10)%11)
            if total == 10:
                total = 0

            if total == cpf[-1]:
                print(f'O CPF {cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]} é Válido')
            else:
                print(f'O CPF {cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]} é inválido')
        else:
            print(f'O CPF {cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]} é inválido')   
    



