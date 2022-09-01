

class Veiculo:
    def __init__(self, nome) -> None:
        self.nome = nome

class Carro(Veiculo):
    def locomoção(self):
        return f"terrestre com motor sobre 4 rodas"
    def capacidade(self):
        return f"1 á 8 passageiros"
    def caracteristica(self):
        return f'Carro e uma forma de locomoção mais confortavel de facil acesso hoje em dia'
class Aviao(Veiculo):
    def locomoção(self):
        return f"Aéria com turbinas e Hélices"
    def capacidade(self):
        return f"1 á 320 passageiros"
    def caracteristica(self):
        return f'Aviao é a forma de locomoção mais rapida e confortavel existente até o momento, mas de dificl acesso'        
class Barco(Veiculo):
    def locomoção(self):
        return f"Aquatica com motor e Hélice"
    def capacidade(self):
        return f"1 á 1500 passageiros"
    def caracteristica(self):
        return f'Dependendo do barco, e uma forma de locomoção confortavel, más de é a mais lenta.'    
class Bicicleta(Veiculo):
    def locomoção(self):
        return f"Terrestre com pedaladas sobre 2 rodas"
    def capacidade(self):
        return f"somente 1 passageiro"
    def caracteristica(self):
        return f'Bicicleta é o meio de locomoção de mais facil acesso até o momento'   
class Onibus(Veiculo):
    def locomoção(self):
        return f"Terrestre sobre 4 rodas ou mais"
    def capacidade(self):
        return f"1 á 80 passageiros"
    def caracteristica(self):
        return f'Busao é o pior meio de locomoção existente...........................'
def main():
    carro = Carro("Carros")   
    aviao = Aviao("Avioes")   
    barco = Barco("Barcos")   
    bicicleta = Bicicleta("Bicicletas")   
    onibus = Onibus("Onibus")
    print(f"Sobre {carro.nome}: \n ")
    print(f'{carro.locomoção()}')
    print(f'{carro.capacidade()}')
    print(f'{carro.caracteristica()}')
    print('')
    print(f"Sobre {aviao.nome}: \n ")
    print(f'{aviao.locomoção()}')
    print(f'{aviao.capacidade()}')
    print(f'{aviao.caracteristica()}')
    print('')
    print(f"Sobre {barco.nome}: \n ")
    print(f'{barco.locomoção()}')
    print(f'{barco.capacidade()}')
    print(f'{barco.caracteristica()}')
    print('')
    print(f"Sobre {bicicleta.nome}: \n ")
    print(f'{bicicleta.locomoção()}')
    print(f'{bicicleta.capacidade()}')
    print(f'{bicicleta.caracteristica()}')
    print('')
    print(f"Sobre {onibus.nome}: \n ")
    print(f'{onibus.locomoção()}')
    print(f'{onibus.capacidade()}')
    print(f'{onibus.caracteristica()}')
main()