from abc import ABC, abstractmethod
import sqlite3


class Pessoa:
    @abstractmethod
    def __init__(self, nome, idade) -> None:
        self.__nome = nome
        self.__idade = idade
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade

class Cliente(Pessoa):
    @abstractmethod
    def __init__(self, nome, idade, conta) -> None:
        super().__init__(nome, idade)
        self.__conta = conta
    @property
    def conta(self):
        return self.__conta
    @conta.setter
    def conta(self, conta):
        self.__conta = conta

class Conta(Cliente):
    def __init__(self, nome, idade, conta, agencia, saldo) -> None:
        super().__init__(nome, idade, conta)
        self.saldo = saldo
        self.agencia = agencia
    @abstractmethod
    def deposito(self, valor):
        self.saldo += valor
    @abstractmethod
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente para saque")

class ContaPopança(Conta):
    def __init__(self, nome, idade, conta, agencia, saldo, rendimento, dia) -> None:
        super().__init__(nome, idade, conta, agencia, saldo)
        self.rendimento = rendimento
        self.dia = dia
    def deposito(self, valor):
        return super().deposito(valor)
    def saque(self, valor):
        return super().saque(valor)
    def juros(self):
        self.saldo += self.saldo*(self.rendimento/100)
        valor = self.saldo*(self.rendimento/100)
        print(f'Seu dinheiro rendeu R${valor} esse mes')
        
class ContaCorrente(Conta):
    def __init__(self, nome, idade, conta, agencia, saldo, limite) -> None:
        super().__init__(nome, idade, conta, agencia, saldo)
        self.saldo = saldo
        self.limite = limite
    def saqueComLimite(self, valor):
        if (self.saldo + self.limite) >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente para saque")
    def saque(self, valor):
        return super().saque(valor)
    def deposito(self, valor):
        return super().deposito(valor)

class Banco(Conta):
    def __init__(self, nome, idade, conta, agencia, saldo) -> None:
        super().__init__(nome, idade, conta, agencia, saldo)
    
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
        # print("Opção 1 = Poupança\nOpção 2 = Corrente")
        # r = input("Digite: ")
        #  match r:
        #      case "1":
        #          tipo = "Conta Poupança"
        #      case "2":
        #          tipo = "Conta Corrente"
                

        cursor.execute('INSERT INTO clientes(nome,saldo,numeroConta,agencia) VALUES (?,?,?,?,?)',(nome,saldo,num_conta,agencia))
        conexao.commit()
        cursor.close()
        conexao.close()

    # def ExibirClientes():
    #     conexao = sqlite3.connect("bancoDeDados.db")
    #     cursor = conexao.cursor()
    #     cursor.execute('SELECT * FROM clientes')
    #     for linha in cursor.fetchall():
    #         print(linha)
    #     cursor.close()
    #     conexao.close()


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
        cursor.close()
        conexao.close()



