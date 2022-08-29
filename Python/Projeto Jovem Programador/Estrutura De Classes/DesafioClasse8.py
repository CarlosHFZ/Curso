
class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.estomago = []
    
    def comer(self, *comida):
        self.comida = comida
        self.estomago.append(self.comida)
        return   

    def ver_estomago(self):
        return(self.estomago)
    
    def digerir(self):
        pass


macaco_1 = Macaco('Cesar')
macaco_2 = Macaco('Putz')


#alimentação
macaco_1.comer('banana')
macaco_1.comer('coco')
macaco_2.comer('abacaxi')
macaco_2.comer('pera')
macaco_2.comer('maça')

macaco_1.comer(macaco_2.estomago, macaco_2.nome)


print(macaco_1.estomago)
print(macaco_2.estomago)