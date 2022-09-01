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
        self.rendimento = 5
        self.valor = 0
    def calcular(self):
        self.saldo += self.saldo*(self.rendimento/100)
        self.valor = self.saldo*(self.rendimento/100)
    
class ContaEspeçial(ContaPoupança):
    def __init__(self, cliente, n_conta, saldo, dia, limite):
        super().__init__(cliente, n_conta, saldo, dia)
        self.limite = float(limite)
    def Sacar_especial(self, valor):
        if valor > self.saldo + self.limite or self.deve + valor > self.limite:
            print(f"{self.cliente} seu saldo é insuficiente!")
        else:
            self.saldo -= valor
            if valor > self.limte:
                self.deve = self.limite
            else:
                self.deve += valor
            
        



    

