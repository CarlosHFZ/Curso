# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. 
# Obs: Por padrão,a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.


nome = "Carlos"
idade = 18
peso = 52.68
altura = 1.63

class Pessoa:
    global nome, idade, peso, altura, nova_idade, novo_peso, nova_altura
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def crescer(self):
        if self.idade < 21:
            self.altura += ((nova_idade - self.idade) * 0.05)
            return
    def envelhecer(self):
        self.idade = nova_idade
        return
    def engordar(self):
        self.peso = novo_peso
        return
    def emagrecer(self):
        self.peso = novo_peso
        return

informaçoes = Pessoa(nome, idade, peso, altura)
print(f'Essa é sua forma fisica atual {informaçoes.nome}')
print('')
print(f'Idade atual: {informaçoes.idade}')
print(f'Peso atual: {informaçoes.peso}')
print(f'Altura atual : {informaçoes.altura}')
print('')

r = str(input('Quer atualizar seus dados? Só responder Sim: ')).lower()
if r == "sim":
    nova_idade = int(input('Qual sua idade atual? '))
    informaçoes.crescer()
    informaçoes.envelhecer()
    novo_peso = float(input('Qual seu peso atual? '))
    if novo_peso > peso:
        informaçoes.engordar()
    elif novo_peso < peso:
        informaçoes.emagrecer()
    print('')
    print(f'Idade atual: {informaçoes.idade}')
    print(f'Peso atual: {informaçoes.peso}')
    print(f'Altura atual : {informaçoes.altura}')
    print('')
else:
    print('Programa finalizado')

