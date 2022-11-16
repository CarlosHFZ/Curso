



class Humano:
    def __init__(self, nome, idade) -> None:
        self.__nome = nome
        self.__idade = idade
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade

class Inseto:
    def __init__(self, nome, venenoso, alado) -> None:
        self.__nome = nome
        self.__venenoso = bool(venenoso)
        self.__alado = bool(alado)
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    @property
    def venenoso(self):
        return self.__venenoso
    @venenoso.setter
    def venenoso(self, novo_venenoso):
        self.__venenoso = novo_venenoso
    @property
    def alado(self):
        return self.__alado
    @alado.setter
    def alado(self, novo_alado):
        self.__alado = novo_alado

class SuperHeroi(Humano, Inseto):
    def __init__(self, nome, idade, codinome, poderes, venenoso, alado) -> None:
        super().__init__(nome, idade)
        Inseto.__init__(self, nome, venenoso, alado)
        self.__codinome = codinome
        self.__poderes = poderes
    @property
    def codinome(self):
        return self.__codinome
    @codinome.setter
    def codinome(self, novo_codinome):
        self.__codinome = novo_codinome
    @property
    def poderes(self):
        return self.__poderes
    @poderes.setter
    def poderes(self, novo_poderes):
        self.__poderes = novo_poderes

    def heroi(self):
        return print(f"Idade: {self.idade}\nNome: {self.nome} \nCodinome: {self.codinome} \nPoderes: {self.poderes} \nVenenoso: {self.venenoso}\nAlado: {self.alado}")


heroi = SuperHeroi("Jubileu",18,"Cruzcredo",["Alahuakiba","Soco Parrudo","Barrigada Colossal","Guspe da Morte"], True, False)
inseto = Inseto("Barata",False,True)
heroi.heroi()