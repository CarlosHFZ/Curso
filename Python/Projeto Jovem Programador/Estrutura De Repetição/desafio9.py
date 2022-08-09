#Faça um Programa que leia três números e mostre-os em ordem decrescente



numeros = []


for i in range(0,3):
    n = input('Digite um numero: ')
    numeros.append(n)
    
numeros.sort(reverse=True)

print(f'a ordem decrecente desses numeros é{numeros}')









