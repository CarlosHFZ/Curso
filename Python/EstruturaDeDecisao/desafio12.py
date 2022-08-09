

hora = float(input('Qual o valor da sua hora? '))
qt = float(input('Qual a quantidade de horas a ser calculada? '))

salario = qt * hora
ir5 = salario*0.05
ir10 = salario*0.10
ir15 = salario*0.15
ir20 = salario*0.20
inss = salario*0.10
fgts = salario*0.11
sindicato = salario*0.03



print(f'Salário Bruto:         :R$ {salario} \n IR (5%)         :R$ {ir5} \n INSS (10%)         :R$ {inss} \n FGTS (11%)         :R$ {fgts} \n Total de Descontos         :R$ {ir5 + inss} \n Salário Liquido         :R$ {salario - ir5 - inss - sindicato}')