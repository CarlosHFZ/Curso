Algoritmo "semnome"

//salário bruto.
//quanto pagou ao INSS.
//quanto pagou ao sindicato.
//o salário líquido.
//calcule os descontos e o salário líquido, conforme a tabela abaixo

Var

h1,h2:real
salario:real
inss:real
sindicato:real
IR:real

Inicio

escreva("quanto você ganha por hora? ")
leia(h1)
escreva("Quantas horas você trabalha por mês? ")
leia(h2)
escreval("Respectivo valores abaixo:")
escreval("")

salario <- h1*h2
inss <- h1*h2*0.08
sindicato <- h1*h2*0.05
IR <- h1*h2*0.11

Escreval("Seu salario bruto: R$",salario)
Escreval("Voce pagou ao INSS: R$",inss)
Escreval("Voce pagou ao sindicato: R$",sindicato)
Escreval("Voce pagou de imposto de renda R$",IR)
Escreval("Salario liquido total R$:",salario-inss-sindicato-IR)

Fimalgoritmo