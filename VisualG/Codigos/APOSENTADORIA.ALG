Algoritmo "Aposentadoria"


Var

Nome:caracter
Sexo:caracter
Idade:inteiro

Inicio

escreval("")
escreval("Qual o seu nome?")
leia(Nome)
escreval("")
escreval("Qual seu sexo (Masculino/Feminino)?")
leia(Sexo)
escreval("")
escreval("Qual sua idade?")
leia(Idade)
escreval("")

   se Sexo = "Masculino" entao
    se Idade < 65 entao
     escreva("Falta", (65-idade)," anos para você se aposentar ",Nome)
    fimse
    se idade >= 65 entao
     escreva("Você ja pode se aposentar ",Nome)
    fimse
   fimse
   
   se Sexo = "Feminino" entao
    se Idade < 60 entao
     escreva("Falta", (60-idade),"  anos para você se aposentar ",Nome)
    fimse
    se idade >= 60 entao
     escreva("Você ja pode se aposentar ",Nome)
    fimse
   fimse
   
escreval("")

Fimalgoritmo