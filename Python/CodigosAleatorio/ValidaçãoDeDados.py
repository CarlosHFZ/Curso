


nome = str(input('Digite seu nome "Mais de 3 caracteres:" '))

print(f'')

while len(nome) < 3:
    print("Numero de caracteres não atendido!!!")
    nome = str(input('Digite um nome com mais de 3 caracteres: '))
    break

idade = int(input('Qual sua idade, voce tem que ter menos de 70 anos: '))

print(f'')

while idade > 70 or idade < 0:
    print('Idade não suportada')
    idade = int(input('Digite novamente a idade requirida: '))

print(f'')

salario = float(input('Qual o seu salario? '))

print(f'')

while salario <= 0:
    print('Salario tem que ser maior que zero, favor digitar corretamente')
    salario = float(input('Digite seu salario novamente: '))
print(f'')

sexo = str(input("Qual sua idade? digite f para femninino e m para masculino: ")).lower()

print(f'')

while sexo != "f" and sexo != "m":
    sexo = str(input('Sexo invalido, favor digitar novamente: ')).lower() 
    
print(f'')

estado_civil = str(input('qual o seu estado civil? s,c,v ou d? ')).lower()

print(f'')

while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
    estado_civil = str(input('estado civil invalido, digite novamente: ')).lower()

print(f'')
print(f'O nome foi validado')
print(f'a idade foi validada')
print(f'o salário foi validado')
print(f'o estado civil foi validado')




