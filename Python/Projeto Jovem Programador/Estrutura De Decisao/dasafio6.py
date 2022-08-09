#Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite outro numero: "))

maior = n1

if maior < n2:
    maior = n2
if maior < n3:
    maior = n3

print(f"O maior numero que voce digitou é {maior}")
    