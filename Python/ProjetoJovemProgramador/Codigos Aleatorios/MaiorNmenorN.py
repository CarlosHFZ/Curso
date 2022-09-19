lista_numero = []
lista_maior_numero = []
lista_menor_numero = []


while True:
    numero = int(input('Digite quantos numeros quiser, quando desejar parar digite 0: '))
    if numero == 0:
        break
    lista_numero.append(numero)

lista_maior_numero.extend(lista_numero)
lista_maior_numero.sort(reverse=True)

lista_menor_numero.extend(lista_numero)
lista_menor_numero.sort()
 
print(f'O maior numero digitado é {lista_maior_numero[0]}')
print(f'O menor numero digitado é {lista_menor_numero[0]}')



