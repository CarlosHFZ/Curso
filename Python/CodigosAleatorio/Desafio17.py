
#1 litro de tinte cobre 6 metros
#latas é 18 litros e custa R$80
#galoes é 3,6 litros e custa R$25

#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

#if
#else
#elif


from math import ceil


area = float(input("Digite a area a ser pintada: "))
area = area*1.1 #Folga de 10%
rlata = (18*6) #O tanto que a lata cobre em metros 
rgalao = (3.6*6) #O tanto que o galao cobre em metros

print("")
if area % rlata != 0 : 
    lata = (area // rlata) + 1 
else:
    lata = (area / rlata)

if area % rgalao != 0 :
    galao = (area // rgalao) + 1
else:
    galao = (area / rgalao)

if area < rlata :
    lt = 0
    if area % rgalao != 0 :
        gl = (area // rgalao) + 1
    else:
        gl = (area / rgalao)
else:
    lt = (area // rlata)
    if (area % rlata) % rgalao != 0 :
        gl = ((area % rlata) // rgalao) + 1
    else: 
        gl = (area % rlata) / rgalao

gl = ceil(gl)
lt = ceil(lt)
lata = ceil(lata)
galao = ceil(galao)


print("Se for comprar em latas, terá que comprar:",lata,"latas que custurá R$",lata*80)
print("Se for comprar em galao, terá que comprar:",galao,"galoes que custurá R$",galao*25)
print("Se quiser enconimizar e sem disperdiçar tinta, você pode comprar:",lt,"latas e",gl,"galoes dando um de Total R$",(lt*80)+(gl*25))
print("")

