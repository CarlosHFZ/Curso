

class Carro:
    def __init__(self, peso, motor, carcaça, roda, bancos, modelo, marca):
        self.peso = peso
        self.motor = motor
        self.carcaça = carcaça
        self.roda = roda
        self.bancos = bancos
        self.medelo = modelo
        self.marca = marca


carro_caracteristicas = Carro('523kg','chats', 'calpsu', '4 rodas', '2 bancos', 'dogge', 'chevrolete')



print(carro_caracteristicas.bancos)


