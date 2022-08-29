
# os quatro paradigmas

# Abstração
# Polimorfismo
# Encapsulamento
# Herança

#POO

# celular

# Caracteristicas

# tam_tela
# antena
# memoria
# Camera
# processador

# Funçoes

# fazer_ligação
# enviar/receber mensagens
# bater foto




# class Celular:
#     def __init__(self, camera, memoria, bateria, modelo):
#         self.camera = camera
#         self.memoria = memoria
#         self.bateria = bateria
#         self.modelo = modelo


# celular_1 = Celular('50mpx','2gb', '3000mah', 'Lg k10') # o celular_1 vai ser o self

# print(celular_1.camera)
# print(celular_1.memoria)
# print(celular_1.bateria)
# print(celular_1.modelo)


# celular_2 = Celular('10mpx','500mb', '7000mah', 'NokiaaT')

# print(celular_2.camera)
# print(celular_2.memoria)
# print(celular_2.bateria)
# print(celular_2.modelo)


class Usuario:
    def __init__(self, nome, email, idade, senha):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.senha = senha

    def add_user(self):
        return('Usuario adicionado com sucesso')


usuario_1 = Usuario('Wildson', 'W@gmail.com', '22', '123')

print(usuario_1.add_user())


