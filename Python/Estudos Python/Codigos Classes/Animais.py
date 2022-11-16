from abc import ABC, abstractmethod


class Mamifero(ABC):
    def __init__(self, nome, peso, cor) -> None:
        self.nome = nome
        self.peso = peso
        self.cor = cor
    @abstractmethod
    def locomoção(self):
        return f"Se movimenta"
    @abstractmethod
    def comunicação(self):
        return f"Se comunica"
    @abstractmethod
    def alimentação(self):
        return f"Se alimenta"
    @abstractmethod
    def habitat_natural(self):
        return f"Habita"

class Cachorro(Mamifero):
    def locomoção(self,):
        return f"Andei por ai com quatro pernas"
    def comunicação(self, nome):
        return f"Conversei com {nome} em latidos"
    def alimentação(self):
        return f"Como qualquer coisa por ai"
    def habitat_natural(self):
        return f"Durmo em qualquer lugar"
class Gato(Mamifero):
    def locomoção(self):
        return f"Caminho tranquilhamente com minha perninhas fofas por ai"
    def comunicação(self, nome):
        return f"Xingo com muito raiva o {nome} com Miu Miu"
    def alimentação(self,nome):
        return f"Tenho uma alimentação regrada, não como qualquer porcaria como o {nome}"
    def habitat_natural(self):
        return f"Deito em qualquer lugar confortavel pra mim"   
class Baleia(Mamifero):
    def locomoção(self):
        return f"Nado de forma bem lenta com a minha gigantesca cauda"
    def comunicação(self, nome):
        return f"Tento conversar com {nome} em baleeis, mas ele nunca me entende"
    def alimentação(self):
        return f"Me alimento de Planctons"
    def habitat_natural(self):
        return f"Vivo no mar"    
class Macaco(Mamifero):
    def locomoção(self):
        return f"Fico pulando igual doido nas arvores"
    def comunicação(self, nome):
        return f"Fico rindo da {nome}, por que ela é lerda Muahahahahaahahaahah"
    def alimentação(self):
        return f"Adoro uma bananona"
    def habitat_natural(self):
        return f"Gosto de viver na selva"
def main():
    while True:
        macaco = Macaco("Covis",18,"Marrom")
        baleia = Baleia("Roberta",890,"Branca")
        gato = Gato("Dolores",8,"Cinza")
        cachorro = Cachorro("Dog",12,"Preto")
        r = input('1 - Cachorro\n2 - Gato\n3 - Baleia\n4 - Macaco\n5 - sair\nDigite: ')
        print('')
        match r:
            case "1":
                print(f'Meu nome é {cachorro.nome}, peso {cachorro.peso} Kilos, sou {cachorro.cor} e eu sou um cachorro. Oque eu fiz hoje: ')               
                print(cachorro.locomoção())
                print(f'{cachorro.comunicação(gato.nome)}')
                print(cachorro.alimentação())
                print(cachorro.habitat_natural())
                print('')
            case "2":
                print(f'Meu nome é {gato.nome}, peso {gato.peso} Kilos, sou {gato.cor} e eu sou um gato. Oque eu fiz hoje: ')              
                print(gato.locomoção())
                print(f'{gato.comunicação(cachorro.nome)}')
                print(gato.alimentação(cachorro.nome))
                print(gato.habitat_natural())
                print('')
            case "3":
                print(f'Meu nome é {baleia.nome}, não vou falar meu peso pois é um assunto delicado. E eu sou uma baleia. Oque eu fiz hoje: ')                
                print(baleia.locomoção())
                print(f'{baleia.comunicação(gato.nome)}')
                print(baleia.alimentação())
                print(baleia.habitat_natural())
                print('')
            case "4":
                print(f'Meu nome é {macaco.nome}, peso {macaco.peso} Kilos, sou {macaco.cor} e eu sou um macaco. Oque eu fiz hoje: ') 
                print(macaco.locomoção())
                print(f'{macaco.comunicação(baleia.nome)}')
                print(macaco.alimentação())
                print(macaco.habitat_natural())
                print('')
            case "5":
                exit()
            case _:
                print('Opção incorreta')

main()