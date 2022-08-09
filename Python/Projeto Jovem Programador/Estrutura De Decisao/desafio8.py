#Faça um programa que pergunte o preço de três produtos e informe 
#qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

pr1 = str(input("Qual o nome desse produto? "))
p1 = float(input("Qual o valor do primeiro produto? "))
pr2 = str(input("Qual o nome desse produto? "))
p2 = float(input("Qual o valor do segundo produto? "))
pr3 = str(input("Qual o nome desse produto? "))
p3 = float(input("Qual o valor do terceiro produto? "))

if p1 < p2 and p1 < p3:
    print(f"O produto {pr1} é o mais barato")
elif p2 < p1 and p2 < p3:
    print(f"O produto  {pr2} é o mais barato")
elif p3 < p2 and p3 < p1:
    print(f"O produto {pr3} é o mais barato")


