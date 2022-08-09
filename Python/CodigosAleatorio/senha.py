from random import choice

qt = int(input('Quantas letras você quer na sua senha? '))

letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%¨&*()_=+[]|\-/{};:,.'

senha = ''

for i in range(qt):
    senha += choice(letras)
print(f'Sua senha é : {senha}')

