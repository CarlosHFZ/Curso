

class Motor:
    def __init__(self, num_cilindros, potencia) -> None:
        self.num_cilindros = num_cilindros
        self.potencia = potencia
        self.dados = ""
    def getdata(self):
        self.dados += input('Entrada de dados: ')
        return self.dados
    def printdados(self):
        print(self.dados)

class Veiculo:
    def __init__(self, peso, velo_max, preço) -> None:
        self.peso = peso
        self.velo_max = velo_max
        self.preço = float(preço)
        self.dados = ""
    def getdata(self):
        self.dados += input('Entrada de dados: ')
        return self.dados
    def printdados(self):
        print(self.dados)

class CarroPasseio(Motor, Veiculo):
    def __init__(self, num_cilindros, potencia, peso, velo_max, preço , cor, modelo) -> None:
        super().__init__(num_cilindros, potencia)
        Veiculo.__init__(self, peso, velo_max, preço)
        self.cor = cor
        self.modelo = modelo
        self.dados = ""
    def getdata(self):
        self.dados += input('Entrada de dados: ')
        return self.dados
    def printdados(self):
        print(self.dados)

class Caminhao(Motor, Veiculo):
    def __init__(self, num_cilindros, potencia , peso, velo_max, preço, carga_maxima, altura_max, comprimento_max) -> None:
        super().__init__(num_cilindros, potencia)
        Veiculo.__init__(self, peso, velo_max, preço)
        self.carga_maxima = carga_maxima
        self.altura_max = int(altura_max)
        self.comprimento_max = int(comprimento_max)
        self.dados = ""
    def getdata(self):
        self.dados += input('Entrada de dados: ')
        return self.dados
    def printdados(self):
        print(self.dados)

    
motor = Motor(6,152)
motor.getdata()
motor.printdados()
carro_passeio = CarroPasseio(8,123,500,120,85.580,"Marelo","Valdio")
carro_passeio.getdata()
carro_passeio.printdados()
caminhao = Caminhao(12,630,1.500,95,230.580,3.000,6,13)
caminhao.getdata()
caminhao.printdados( )


