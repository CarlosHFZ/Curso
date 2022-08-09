n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite outro numero: "))

maior = n1
menor = n3

if maior < n2:
    maior = n2
if maior < n3:
    maior = n3

if menor > n1:
    menor = n1
if menor > n2:
    menor = n2

print(f"O maior numero que voce digitou é {maior} e o menor é {menor}")