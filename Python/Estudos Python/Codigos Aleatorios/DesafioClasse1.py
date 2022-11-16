


class Bola:
    def __init__(self, cor,tamanho,material ):
        self.cor = cor
        self.circuferente = tamanho
        self.material = material
    
    def Trocar_Cor(self , novaCor):
        self.cor = str(input('Que cor vc deseja definir? '))
    def Mostrar_Cor(self):
        return self.cor