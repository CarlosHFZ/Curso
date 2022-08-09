# M = BOM DIA
# V = BOA TARDE
# N = NOTURNO

print('Em qual turno você esta estudando? \n M para Matutino \n V para Vespertino \n N para norturno ')
r = str(input('Digite: ')).lower()

if r != 'm' and r != 'v' and r != 'n':
    print('Turno incorreto')
else:
    if r == 'm':
        print('Bom dia, seja bem vindo')
    if r == 'v':
        print('Boa tarde, seja bem vindo')
    if r == 'n':
        print('Boa noite, seja bem vindo')