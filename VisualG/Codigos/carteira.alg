Algoritmo "Carteira?"

Var

Nome:caracter
Idade:inteiro

Inicio

escreval("")
escreval("Qual o seu nome? ")
leia(nome)
escreval("")
escreval("Qual a sua Idade? ")
leia(idade)
escreval("")

se Idade > 18 entao
   escreval("Você tem",(idade-18)," anos a mais que a idade necessaria para tirar a carteira")
   escreval("")
   escreval("Não perca tempo ",Nome,", vá logo tirar sua carteira!!!")
fimse

se Idade = 18 entao
   escreval("")
   escreval("Não perca tempo ",Nome,", você atingiu a maioridade, vá logo tirar sua carteira!!!")
fimse

se Idade < 18 entao
   escreval(Nome, " Você ainda não pode tirar a carteira.")
   escreval("")
   escreval("Falta",(18-idade)," anos, para completar a maioridade!")
fimse

escreval("")

Fimalgoritmo