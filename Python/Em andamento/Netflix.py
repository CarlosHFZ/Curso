import sqlite3
import random

def Tabela():
    conexao = sqlite3.connect('BancoDB/netflix.db')
    conexao.execute('PRAGMA foreing_keys = ON')
    cursor = conexao.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS contas('
    'email TEXT NOT NULL UNIQUE PRIMARY KEY,'
    'senha TEXT NOT NULL'
    ')')

    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios('
    'email_conta TEXT NOT NULL,'
    'nome TEXT NOT NULL,'
    'favorites TEXT NOT NULL,'
    'FOREIGN KEY (email_conta) REFERENCES contas (email) ON DELETE CASCADE ON UPDATE CASCADE'
    ')')
    conexao.commit()
    cursor.close()
    conexao.close()

def Cadastro():
    e = 0
    c = 0
    while True:       
        if e == 1:
            print('\nE-mail já utilizado\n')
            email = str(input('Digite novamente: '))    
        conexao = sqlite3.connect('BancoDB/netflix.db')
        cursor = conexao.cursor()
        if c == 0:
            email = str(input('E-mail: ')).lower()
        c += 1
        cursor.execute('SELECT email FROM contas')
        for item in cursor.fetchall():
            if email == item[0]:
                e = 1
                break
            
            else:
                e = 2
        print(email)
        if e == 2:
            senha = str(input('Senha: '))
            cursor.execute('INSERT INTO contas(email,senha) VALUES (?,?)',(email,senha))
            conexao.commit()
            cursor.close()
            conexao.close()
            break

# def delete():
#     conexao = sqlite3.connect('BancoDB/netflix.db')
#     conexao.execute('PRAGMA foreign_keys = ON')
#     cursor = conexao.cursor()
#     r = str(input('Digite o e-mail: ')).lower()
#     cursor.execute('DELETE FROM contas WHERE email = ?',(r,))
#     conexao.commit()
#     cursor.close()
#     conexao.close()


def Entrar():
    conexao = sqlite3.connect('BancoDB/netflix.db')
    cursor = conexao.cursor()
    while True:
        print('Opção 1 - Cria Conta\nOpção 2 - Fazer Login\nOpçaõ 3 - Sair')
        r = input('Digite: ')
        match r:
            case "1":
                Cadastro()
            case "2":
                s = 0
                c = 0
                while True:
                    c += 1
                    if s == 1:
                        break
                    if s != 1 and c >= 2:
                        print('\nLogin ou senha incorreto\n')
                    print('\nLogin\n')
                    email = str(input('E-mail: ')).lower()
                    senha = str(input('Senha: '))
                    print('')
                    cursor.execute('SELECT * FROM contas')
                    for item in cursor.fetchall():
                        if email == item[0] and senha == item[1]:
                            s = 1
                lista_email = []
                cursor.execute('SELECT * FROM usuarios')
                for item in cursor.fetchall():
                    lista_email.append(item[0])
                cursor.execute('SELECT * FROM usuarios')
                for item in cursor.fetchall():
                    if email not in lista_email:
                        s = 2
                if s == 2:      
                    usuario = str(input('Digite o nome do primeiro Perfil: '))
                    fav = str(random.randint(1,100))
                    cursor.execute('INSERT INTO usuarios(nome,email_conta,favorites) VALUES (?,?,?)',(usuario,email,fav))
                    conexao.commit()
                while True:
                    print('Opção 1 - Alterar Senha\nOpção 2 - Excluir conta\nOpção 3 - Criar Perfil\nOpção 4 - Alterar nome de perfil\nOpção 5 - Visualizar Perfis\nOpção 6 - Entrar no perfil\nOpção 7 - Excluir um Perfil\nOpção 8 - Voltar ao menu de Login')
                    r = input('Digite: ')

                    match r:
                        case "1":
                            while True:
                                senha_atual = str(input('Digite sua senha atual: '))
                                if senha == senha_atual:
                                    senha_nova = str(input('Digite sua nova senha: '))
                                    cursor.execute('UPDATE contas SET senha = ? WHERE senha = ?',(senha_nova, senha))
                                    conexao.commit()
                                    print('\nSenha alterada com sucesso\n')
                                    senha = senha_nova
                                    break
                                else:
                                    print("\nSenha incorreta\n")
                        case "2":
                            while True:
                                senha_atual = str(input('Digite sua senha: '))
                                if senha_atual == senha:
                                    conexao.execute('PRAGMA foreign_keys = ON')
                                    cursor.execute('DELETE FROM contas WHERE  email 2= ?',(email,))
                                    conexao.commit()
                                    cursor.close()
                                    conexao.close()
                                    print('\nConta excluida\n')
                                    exit()
                                else:
                                    print('\nSenha incorreta\n')
                        case "3":
                            usuario = str(input('Digite o nome do Perfil: '))
                            fav = str(random.randint(1,100))
                            cursor.execute('INSERT INTO usuarios(nome,email_conta,favorites) VALUES (?,?,?)',(usuario,email,fav))
                            conexao.commit()
                        case "4":
                            while True:
                                lista_nome = []
                                nome = str(input('Nome do Usuario a ser mudado: '))
                                cursor.execute('SELECT nome FROM usuarios')
                                for item in cursor.fetchall():
                                    lista_nome.append(item[0])
                                if nome not in lista_nome:
                                    print('Usuario incorreto')
                                else:
                                    novo_nome = str(input('Novo nome do perfil: '))
                                    cursor.execute('UPDATE usuarios SET nome = ? WHERE nome = ?',(novo_nome,nome))
                                    conexao.commit()
                                    break
                        case "5":
                            print('\nUsuarios: \n')
                            cursor.execute('SELECT * FROM usuarios')
                            for item in cursor.fetchall():
                                print(f'Perfil: {item[1]}')
                            print('')
                        case "6":
                            c = 0
                            
                            s = 5
                            while True:
                                if c == 0:
                                    r = str(input('\nDigite o nome do perfil para entrar: '))
                                    c += 1
                                if s == 1:
                                    break
                                cursor.execute('SELECT * FROM usuarios')
                                for item in cursor.fetchall():
                                    if r == item[1]:
                                        s = 1
                                if s == 5:
                                    print('\nUsuario incorreto\n')
                                    r = str(input('Digite novamente: '))
                            print(f'\nOlá, {r}\n')

                            while True:
                                print("Opção 1 - Mostrar Favoritos \nOpção 2 - voltar")
                                resp = str(input('Digite: '))
                                match resp:
                                    case "1":
                                        cursor.execute('SELECT * FROM usuarios')
                                        for item in cursor.fetchall():
                                            if item[1] == r:
                                                print(f'Favoritos: {item[2]}')
                                                break
                                            fav = str(random.randint(1,100)) 
                                            cursor.execute(f'UPDATE usuarios SET favorites = ? WHERE nome = ?', (fav,r))
                                            conexao.commit()
                                    case "2":
                                        break
                                    case _:
                                        print('Opção incorreta')
                        case "7":
                            t = 0
                            while True:
                                if t == 2:
                                    break
                                senha_atual = str(input('\nDigite sua senha: '))
                                if senha_atual == senha:
                                    while True:
                                        nome = str(input('Qual nome do usuario a ser apagado: '))
                                        print('')
                                        cursor.execute('SELECT nome FROM usuarios')
                                        for item in cursor.fetchall():
                                            if item[0] == nome:
                                                cursor.execute('DELETE FROM usuarios WHERE nome = ?',(nome,))
                                                conexao.commit()
                                                t = 1
                                        if t == 0:
                                            print('Usuario incorreto')
                                        if t == 1:
                                            print('Usuario apagado com sucesso\n')
                                            t = 2
                                            break           
                                else:
                                    print('Senha incorreta')
                                    

                        case "8":
                            break
                        case _:
                            print('Opção incorreta')

            case "3":
                cursor.close()
                conexao.close()
                exit()
            case _:
                print('Opção incorreta')

Tabela()
Entrar()

                
                 