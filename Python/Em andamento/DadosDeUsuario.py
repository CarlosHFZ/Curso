

c = 0
while True:
    if c >= 1:
        resp = str(input('deseja continuar? Digite Sim ou nao: ')).lower()
        if resp == 'nao':
            break 
    senha = str(input('Digite sua senha: '))     
    b_senha = open('BancoSenhas.txt','a')
    b_senha.write(f'{senha} ')
    login = str(input('Digite seu login: '))
    b_login = open('BancoLogins.txt','a')
    b_login.write(f'{login} ')
    c += 1



