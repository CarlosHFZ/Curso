

c = 0
while True:
    if c >= 2:
        a = input('Aperter ENTER para encerar, ou digite novamnte para continuar: ')
        if a == "":
            break
    c += 1
    if c == 1:
        a = input('Escreva qualquer coisa: ')
    print(f'Seu tipo primitivo é {type(a)}') # Mostra qual é o tipo da informação.
    print(f'So tem espaços? {a.isspace()}') # Verifica se há somente espaços
    print(f'So tem numeros? {a.isnumeric()}') # Verifica se há somente numeros
    print(f'è alfabetico? {a.isalpha()}') # Verifica se há somente letras do alfabeto
    print(f'é alfa numerico? {a.isalnum()}') # Verifica se há numeros e letras do alfabeto
    print(f'Estão em maiuscula? {a.isupper()}') # Verifica se há somente letras do alfabeto em maiusculo
    print(f'Estão em minuscula? {a.islower()}') # Verifica se há somente letras do alfabeto em minusculo
    print(f'Esta capitalizda? {a.istitle()}') # Verifica Se a primeira letra e maiuscula
    