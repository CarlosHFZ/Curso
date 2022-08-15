n = int(input('Digite um numero: '))

ant = n - 1
suce = n + 1
d = n*2
t = n*3
r = n**(1/2)

print(f'o numero que foi digitado é {n}, \nseu sucessor é {suce} \nseu antecessor é {ant}')
print(f'O dobro desse numero è {d}, \nseu triplo é {t} \nsua raiz quadrada é {r:.2f}')