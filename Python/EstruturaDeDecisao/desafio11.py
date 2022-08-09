#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario = float(input("qual o salario do colaborador? "))

s5 = 1.05 #5%
s10 = 1.10 #10%
s15 = 1.15 #15%
s20 = 1.20 #20%

if salario > 1500:
    print(f"Salario atual de R${salario}, teve um aumento de 5% (R${salario*(s5-1):.2f}), então o salario novo fica R${salario*s5:.2f}")
elif salario > 700:
    print(f"Salario atual de R${salario}, teve um aumento de 10% (R${salario*(s10-1):.2f}), então o salario novo fica R${salario*s10:.2f}")
elif salario > 280:
    print(f"Salario atual de R${salario}, teve um aumento de 15% (R${salario*(s15-1):.2f}), então o salario novo fica R${salario*s15:.2f}")
elif salario < 280:
    print(f"Salario atual de R${salario}, teve um aumento de 20% (R${salario*(s20-1):.2f}), então o salario novo fica R${salario*s20:.2f}")

