
#Gasolina = R$5,68 por litro e tem 7.000 litros na bomba
#disel = R$7,89 por litro tem 12.000 litros na bomba
#Etanol = R$4,23 por litro tem 5.000 litros na bomba

# 1 = 5,28, 2,58

class BombaDeCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
        self.valor_a_pagar = 0
    def abastecerPorValor(self, valor):
        litros = (valor/self.valor_litro)
        if self.valor_litro <= valor and self.quantidade_combustivel >= litros:
            self.valor_a_pagar = valor
            self.quantidade_combustivel -= (valor/self.valor_litro)
        if self.valor_litro <= valor and self.quantidade_combustivel >= 1:
            self.quantidade_combustivel -= (1/valor)
        else:
            self.valor_a_pagar = (self.quantidade_combustivel*valor)
            self.quantidade_combustivel = 0
            print('Bomba de Gasolina esgotada')
    def abastecerPorLitro(self, litros):
        if self.quantidade_combustivel >= litros:
            self.valor_a_pagar = (litros * self.valor_litro)
            self.quantidade_combustivel -= litros
        else:
            self.valor_a_pagar = (self.quantidade_combustivel * self.valor_litro)
            self.quantidade_combustivel = 0
            print('Bomba de Gasolina esgotada')
    def alterarValor(self, valor):
        self.valor_litro = valor
    def alterarCombustivel(self, tipo):
        self.tipo_combustivel = tipo
    def alterarQuantidadeCombustivel(self, quantidade):
        self.quantidade_combustivel = quantidade
    def __str__(self):
        return f"Tipo de combustivel: {self.tipo_combustivel:f2}\nQuantidade disponivel: {self.quantidade_combustivel}\nValor P/Litro: {self.valor_litro}"