n1 = int(input('Digite um numero: '))
resposta = str(input('Como voce deseja calcular? Digite um desses sinais "+" "-" "*" "/": '))
n2 = int(input('Digite outro numero: '))


while resposta == "+":
    print(f'a SOMA desses dois numeros é: {n1 + n2}')
    resposta = input("Se deseja continuar digite novamente um dos sinais, se não, aperte enter: ")     

while resposta == "-":
    print(f'a SUBTRAÇAO desses dois numeros é: {n1 - n2}')
    resposta = input("Se deseja continuar digite novamente um dos sinais, se não, aperte enter: ") 

while resposta == "*":
    print(f'a MULTIPLICAÇÃO desses dois numeros é: {n1 * n2}')
    resposta = input("Se deseja continuar digite novamente um dos sinais, se não, aperte enter: ") 

while resposta == "/":
    print(f'a DIVISÃO desses dois numeros é: {n1 / n2}')
    resposta = input("Se deseja continuar digite novamente um dos sinais, se não, aperte enter: ")
else:
    print('Expressão invalida')


        

