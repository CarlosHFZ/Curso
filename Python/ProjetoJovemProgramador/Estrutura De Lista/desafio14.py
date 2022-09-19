perguntas = ["Telefonou para a vítima? ","Esteve no local do crime? ","Mora perto da vítima? ","Devia para a vítima? ","Já trabalhou com a vítima? "]

sim = 0

c = 0

while True:
    if c == 5:
        break
    if c == 0:
        print("")
        print('Responda Sim ou Não.')
    print("")
    resposta = str(input(perguntas[c])).lower()
    c += 1
    if resposta == 'sim':
        sim += 1
print("")
if sim <= 1:
    print('Não é suspeito')
    print("")
if sim == 2:
    print('Suspeito')
    print("")
if sim > 2 and sim < 4:
    print('Cúmplice')
    print("")
if sim == 5:
    print('Assasino')
    print("")




