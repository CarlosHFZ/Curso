class Pessoa:
    def __init__(self, nome, vida, energia, mana, fome,) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__energia = energia
        self.__mana = mana
        self.__fome = fome
        self.__vida_maxima = 50
        self.__energia_maxima = 30
        self.__mana_maxima = 20
        self.__fome_maxima = 50
        self.__nivel = 1
     
    @property
    def nivel(self):
        return self.__nivel
    @nivel.setter
    def nivel(self, novo_nivel):
        self.__nivel = novo_nivel
    @property
    def vida_maxima(self):
        return self.__vida_maxima
    @vida_maxima.setter
    def vida_maxima(self, nova_vida_maxima):
        self.__vida_maxima = nova_vida_maxima
    @property
    def energia_maxima(self):
        return self.__energia_maxima
    @energia_maxima.setter
    def energia_maxima(self, energia_maxima):
        self.__energia_maxima = energia_maxima
    @property
    def mana_maxima(self):
        return self.__mana_maxima
    @mana_maxima.setter
    def mana_maxima(self, nova_mana_maxima):
        self.__mana_maxima = nova_mana_maxima
    @property
    def fome_maxima(self):
        return self.__fome_maxima
    @fome_maxima.setter
    def fome_maxima(self, nova_fome_maxima):
        self.__fome_maxima = nova_fome_maxima
    
    @property
    def nome(self):
        return self.__nome

    @property
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self,nova_vida):
        self.__vida = nova_vida
    @property
    def energia(self):
        return self.__energia
    @energia.setter
    def energia(self,nova_energia):
        self.__energia = nova_energia
    @property
    def mana(self):
        return self.__mana
    @mana.setter
    def mana(self,nova_mana):
        self.__mana = nova_mana
    @property
    def fome(self):
        return self.__fome
    @fome.setter
    def fome(self,nova_fome):
        self.__fome = nova_fome

    def Perder_fome(self):
        self.fome -= 1
        if self.fome <= 0:
            self.fome = 0       
    def Comer(self):
        self.fome += 30
        if self.fome >= 50:
            self.fome = 50
        if self.fome <= 0:
            self.fome = 0       
    def Correr(self):
        self.energia -= 5
        if self.energia <= 0:
            self.energia = 0   
    def Dormir(self):
        self.energia = self.energia_maxima
        self.mana = self.mana_maxima
        self.vida = self.vida_maxima
    def Soltar_Feitiço(self):
        self.mana -= 3
        if self.mana >= self.mana_maxima:
            self.mana = self.mana_maxima
        if self.mana <= 0:
            self.mana = 0
    def Tomar_Dano(self):
        self.vida -= 1
        if self.vida <= 0:
            self.vida = 0
    def Nivel(self):
        self.nivel += 1
        self.mana_maxima += 10
        self.vida_maxima += 20
        self.energia_maxima += 5

    def __str__(self):
        return f"Nome: {self.nome}\nNivel: {self.nivel} \nVida: {self.vida}/{self.vida_maxima}\nMana: {self.mana}/{self.mana_maxima}\nEnergia: {self.energia}/{self.energia_maxima}\nFome: {self.fome}/{self.fome_maxima}"

    

    