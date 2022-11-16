

import sqlite3


class agenda():
    def inserir(self):
        import sqlite3
        conexao = sqlite3.connect('BancoDB/Adenda.db')
        cursor = conexao.cursor()
        nome = input('Nome: ').capitalize()
        telefone = int(input('Telefone: '))                          
        endereço = str(input('Endereço: ')).capitalize()
        cpf = [] 
        t1 = 0
        c = 0
        while True:
            conexao = sqlite3.connect('BancoDB/Adenda.db')
            cursor = conexao.cursor()
            if c == 0:
                print('\nDigite separadamente para validação individual de cada numero: \n')
            c += 1
            r = str(input('Digite: '))
            if r != '1' and r != '2' and r != '3' and r != '4' and r != '5' and r != '6' and r != '7' and r != '8' and r != '9' and r != '0':
                print('\nDigito incorreto\n')
            if r == '1' or r == '2' or r == '3' or r == '4' or r == '5' or r == '6' or r == '7' or r == '8' or r == '9' or r == '0':  
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
                            cpf = f'{str(cpf[0])}{str(cpf[1])}{str(cpf[2])}.{str(cpf[3])}{str(cpf[4])}{str(cpf[5])}.{str(cpf[6])}{str(cpf[7])}{str(cpf[8])}-{str(cpf[9])}{str(cpf[10])}'
                            cursor.execute('INSERT INTO agenda(nome,telefone,endereço,cpf) VALUES (?,?,?,?)', (nome,telefone,endereço,cpf))
                            conexao.commit()
                            print('\nCadastro concluido\n')
                            break
                        else:
                            print(f'\nO CPF {cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]} é inválido, digite novamente\n')
                    else:
                        print(f'\nO CPF {cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]} é inválido, digite novamente\n')
            cursor.close()
            conexao.close()   
    def alterar(self):
        import sqlite3
        conexao = sqlite3.connect('BancoDB/Adenda.db')
        cursor = conexao.cursor()
        while True:
            print('Opção 1 - Nome\nOpção 2 - telefone\nOpção 3 - Endereço\nOpcão 4 - CPF\nOpção 5 - Sair')
            r = input('Digite: ')
            match r:
                case '1':
                    conexao = sqlite3.connect('BancoDB/Adenda.db')
                    cursor = conexao.cursor()
                    id = int(input('Numero do ID: '))
                    nome = input('Novo nome: ')
                    cursor.execute('UPDATE agenda SET nome = ? WHERE id = ?',(nome,id))
                    conexao.commit()
                case '2':
                    conexao = sqlite3.connect('BancoDB/Adenda.db')
                    cursor = conexao.cursor()
                    id = int(input('Numero do ID: '))
                    telefone = int(input('Telefone: '))
                    cursor.execute('UPDATE agenda SET telefone = ? WHERE id = ?',(telefone,id))
                    conexao.commit()
                case '3':
                    conexao = sqlite3.connect('BancoDB/Adenda.db')
                    cursor = conexao.cursor()
                    id = int(input('Numero do ID: '))
                    endereço = str(input('Novo endereço: '))
                    cursor.execute('UPDATE agenda SET endereço = ? WHERE id = ?',(endereço,id))
                    conexao.commit()
                case '4':
                    conexao = sqlite3.connect('BancoDB/Adenda.db')
                    cursor = conexao.cursor()
                    id = int(input('Numero do ID: '))
                    import sqlite3
                    conexao = sqlite3.connect('BancoDB/Adenda.db')
                    cursor = conexao.cursor()
                    cpf = [] 
                    t1 = 0
                    c = 0
                    while True:
                        conexao = sqlite3.connect('BancoDB/Adenda.db')
                        cursor = conexao.cursor()
                        if c == 0:
                            print('\nDigite separadamente para validação individual de cada numero: \n')
                        c += 1
                        r = str(input('Digite: '))
                        if r != '1' and r != '2' and r != '3' and r != '4' and r != '5' and r != '6' and r != '7' and r != '8' and r != '9' and r != '0':
                            print('\nDigito incorreto\n')
                        if r == '1' or r == '2' or r == '3' or r == '4' or r == '5' or r == '6' or r == '7' or r == '8' or r == '9' or r == '0':  
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
                                        cpf = f'{str(cpf[0])}{str(cpf[1])}{str(cpf[2])}.{str(cpf[3])}{str(cpf[4])}{str(cpf[5])}.{str(cpf[6])}{str(cpf[7])}{str(cpf[8])}-{str(cpf[9])}{str(cpf[10])}'
                                        cursor.execute('UPDATE agenda SET cpf = ? WHERE id = ?',(cpf,id))
                                        conexao.commit()
                                        print('\nCadastro concluido\n')
                                        break
                                    else:
                                        print(f'\nO CPF {cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]} é inválido, digite novamente\n')
                                else:
                                    print(f'\nO CPF {cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]} é inválido, digite novamente\n')
                case '5':
                    cursor.close()
                    conexao.close() 
                    exit()

    def delete(self):
        import sqlite3
        conexao = sqlite3.connect('BancoDB/Adenda.db')
        cursor = conexao.cursor()
        id = int(input('Numero do ID: '))
        cursor.execute(f'DELETE FROM agenda WHERE ID = {id}')
        conexao.commit()
        cursor.close()
        conexao.close()
    
    def lista(self):
        import sqlite3
        conexao = sqlite3.connect('BancoDB/Adenda.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM agenda')   
        for item in cursor.fetchall():
            print(item)
        cursor.close()
        conexao.close()

agend = agenda()


agend.lista()


        