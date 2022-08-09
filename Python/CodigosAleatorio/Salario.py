#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo
#importo de renda é 11%
#inss é 8%
#sindicato 5%

h1 = float(input('Quanto você ganha por hora trabalhada? '))
h2 = float(input('Quantas horas trabalhadas para ser calculada? '))
print('Resultado Calculado Abaixo: ')

salario = (h1 * h2)
inss = (h1 * h2 * 0.08)
ir = (h1 * h2 * 0.11)
sindicato = (h1 * h2 * 0.05)

print("Salário bruto por",h2,"horas trabalhadas: R$",salario)
print("Desconto do INSS: R$",inss)
print("Desconto do Imposto de Renda: R$",ir)
print("Desconto do sindicato: R$",sindicato)
print("Sálario liquido a ser recebido: R$",(salario - inss - ir - sindicato))

