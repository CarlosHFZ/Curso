
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

delta = (b**2)-4*(a*c)
x_1 = (-b+delta**(1/2))/(2*a)
x_2 = (-b-delta**(1/2))/(2*a)

if a == 0:
    print('A equação não pe de segundo grau. ')
elif delta < 0:
    print('A equação não possui raizes reais. ')
elif delta == 0:
    print(f"A raiz da equação é {x_1}")
elif delta > 0 :
    print(f"As raizes são: x1={x_1}, x2={x_2}")
