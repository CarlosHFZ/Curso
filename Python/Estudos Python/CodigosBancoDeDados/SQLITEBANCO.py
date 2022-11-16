# Crie um algoritmo onde um banco possa criar uma tabela de clientes e adiciona-los
# Cliente deve ter ID, Nome, Saldo, Numero de Conta e Agencia.
# O algoritmo deve ser capaz de adicionar uma pessoa diferente a cada execução.
# E deve imprimir uma lista com todos os clientes, mostrando nome, numero de conta  e saldo.

import sqlite3


def CadastroCLientes():
    conexao = sqlite3.connect("bancoDeDados.db")
    cursor = conexao.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'nome TEXT,'
    'saldo FLOAT,'
    'numeroConta TEXT,'
    'agencia TEXT'
    ')')
    nome = input("Nome do Cliente: ")
    saldo = float(input("Saldo inicial do cliente: "))
    num_conta = input('Numero da conta: ')
    agencia = input('Qual agencia: ')

    cursor.execute('INSERT INTO clientes(nome,saldo,numeroConta,agencia) VALUES (?,?,?,?)',(nome,saldo,num_conta,agencia))
    conexao.commit()
    cursor.close()
    conexao.close()

def ExibirClientes():
    conexao = sqlite3.connect("bancoDeDados.db")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM clientes')
    for linha in cursor.fetchall():
        print(linha)
    cursor.close()
    conexao.close()
def verificar(ver_nome, ver_conta, ver_agencia):
    c = 0
    conexao = sqlite3.connect("bancoDeDados.db")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM clientes')
    for i in cursor.fetchall():
        if ver_nome == i[1] and ver_conta == i[3] and ver_agencia == i[4] :
            c += 1
    if c == 1:
        print("Cliente cadastrado")
    else:
        print("Cliente não cadastrado no banco de dados")
