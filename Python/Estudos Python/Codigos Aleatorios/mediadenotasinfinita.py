qt = int(input('Quantas notas voce quer calcular? '))

c = 0
notas = 0

while True:  
    notas += int(input('Quais são as notas: '))
    c += 1
    if c == qt:
        print(f"A media dessas nota é {notas/c}")
        break
      