from abc import ABC, abstractmethod


class FormaGeometrica:
    @abstractmethod
    def perimetro(self):
        pass
    @abstractmethod
    def area(self):
        pass

class Quadrado(FormaGeometrica):
    def __init__(self, lado) -> None:
        self.lado = lado
    
    def perimetro(self):
        return self.lado * 4
    def area(self):
        return self.lado ** 2

class Triagulo(FormaGeometrica):
    def __init__(self, lado, altura) -> None:
        self.lado = lado
        self.altura = altura

    def perimetro(self):
        return self.lado * 3
    def area(self):
        return self.lado * self.altura/2

class Circulo(FormaGeometrica):
    def __init__(self, raio) -> None:
        self.raio = raio
    
    def perimetro(self):
        return self.raio * 3.14 * 2
    def area(self):
        return (self.raio**2) * 3.14

class Pentagono(FormaGeometrica):
    def __init__(self, lado, apotema) -> None:
        self.lado = lado
        self.apotema = apotema
    
    def perimetro(self):
        return self.lado * 5
    def area(self):
        return self.lado * self.apotema / 2

l = int(input('Digite o valor do lado: '))
a = int(input('Digite o valor da altura: '))
quadrado = Quadrado(l)
triangulo = Triagulo(l,a)
circulo = Circulo(l)
pentagono = Pentagono(l,a)
print("")

print(f"Area do Quadrado: {quadrado.area()}")
print(f"Perimetro do Quadrado {quadrado.perimetro()}")
print(f"Area do Triangulo: {triangulo.area()}")
print(f"Perimetro do Triangulo: {triangulo.perimetro()}")
print(f"Area do circulo {circulo.area()}")
print(f"Perimetro do circulo {circulo.perimetro()}")
print(f"Area do Pentagono: {pentagono.area()}")
print(f"Perimetro do Pentagono: {pentagono.perimetro()}")



