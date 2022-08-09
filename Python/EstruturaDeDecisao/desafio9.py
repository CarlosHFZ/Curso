
lista = []


n1 = int(input('Digite um numero: '))
lista.append(n1)
n2 = int(input('Digite outro numero: '))
lista.append(n2)
n3 = int(input('Digite outro numero: '))
lista.append(n3)

lista.sort(reverse=True)

print(f'A ordem decrecente desses numeros é {lista[0]}, {lista[1]} e {lista[2]}')





