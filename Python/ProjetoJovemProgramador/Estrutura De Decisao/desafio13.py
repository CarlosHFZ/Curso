dias_da_semana = {'1':'Segunda-Feira','2':'Terça-Feira','3':'Quarta-Feira','4':'Quinta-Feira','5':'Sexta-Feira'}

r = str(input('Digite um numero de 1 a 5: '))

if r != '1' and r != '2' and r != '3' and r != '4' and r != '5':
    print('Numero incorreto') 
else:
    print(dias_da_semana[r])