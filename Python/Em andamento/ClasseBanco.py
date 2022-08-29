#0,05 rendimento

class ContaBancaria():
    def __init__(self, cliente,n_conta,saldo):
        self.cliente = cliente
        self.n_conta = n_conta
        self.saldo = saldo
        self.deve = 0
    def sacar(self, valor):
        self.saldo -= valor
    def deposito(self, valor):
        self.saldo += valor
    def __str__(self):
        return f"Nome do Cliente: {self.cliente}\nNumero da Conta: {self.n_conta}\nSaldo atual da conta: R${self.saldo}\nDivida: R${self.deve}"
class ContaPoupança(ContaBancaria):
    def __init__(self, cliente, n_conta, saldo, dia,):
        super().__init__(cliente, n_conta, saldo)
        self.dia = int(dia)
        self.rendimento = 0.005
        self.valor = 0
    def calcular(self):
        self.saldo += ((self.rendimento * self.saldo) - self.saldo)
        self.valor = ((self.rendimento * self.saldo) - self.saldo) 
    
class ContaEspeçial(ContaPoupança):
    def __init__(self, cliente, n_conta, saldo, dia, limite):
        super().__init__(cliente, n_conta, saldo, dia)
        self.limite = float(limite)
    def Sacar_especial(self, valor):
        self.limite -= float(valor)
        self.deve += float(valor)
        
        



    

