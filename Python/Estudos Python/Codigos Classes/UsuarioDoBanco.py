from ClasseBanco import Banco, ContaCorrente, ContaPopança
import sqlite3

from SQLITEBANCO import CadastroCLientes


while True:
    print('Opção 1 - Cadastro de Cliente\nOpção 2 - Ver dados atuais\nOpção 3 - Depositar\nOpção 4 - Sacar\nOpção 5 - Sair ')
    print('')
    r = input("Digite: ")
    match r:
        case '1':
            CadastroCLientes()
        case '2':
            pass

