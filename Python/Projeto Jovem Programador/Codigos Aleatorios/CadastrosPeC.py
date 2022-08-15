#data = open('teste.txt','r') #o a e para adicionar e o w e para sobrescrever e r para leitura

resp = str(input('Quer cadastrar produtos ou clientes? ')).lower()
print('')

if resp == 'produtos':
    while True:
        produtos = str(input('Digite o nome do produto: '))
        print('')

        n_produtos = open('N_produtos.txt','a')
        n_produtos.write(f'{produtos} \n')

        valor = float(input('Digite o valor do produto: R$:'))

        v_produtos = open('V_produtos.txt','a')
        v_produtos.write(f'R$:{valor} \n')
        r = input('Se deseja encerrar aperte ENTER ou continuar apertando digitando qualquer tecla: ')
        if  r == "":
            break



if resp == 'clientes':
    while True:
        cliente = str(input('Digite o nome do cliente: '))
        print('')

        n_cliente = open('N_Cliente.txt','a')
        n_cliente.write(f'{cliente} \n')

        email = str(input('Digite o e-mail do cliente: '))

        e_cliente = open('E_Cliente.txt','a')
        e_cliente.write(f'{email} \n')
        r = input('Se deseja encerrar aperte ENTER ou continuar apertando digitando qualquer tecla: ')
        if  r == "":
            break






