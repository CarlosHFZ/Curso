Algoritmo "semnome"

//1 LITRO COBRE 6 METROS
//18 LITROS É UMA LATA
//3,6 litros É UM LATAO
//VALE R$ 80 REAIS UMA LATA
//VALE R$ 25 REAIS UM LATAO
//QUANTAS LATAS VOU PRECISAR E QUANTO VOU PAGAR

Var

metros:inteiro
resposta:caracter
lata:inteiro


Inicio

escreval("Digite o total em metros quadrados a ser pintado: ")
leia(metros)

escreval("Vocé quer comprar somente lata ou latao? ")
leia(resposta)

se resposta = "lata" entao
   se metros > 54 entao
     se metros % 54 <> 0 entao
      lata <- (metros div 54)+1
     fimse
     se metros % 54 = 0 entao
      lata <- (metros div 54)
     fimse
   fimse
   se metros <= 54 entao
    lata <- 1
   fimse
   escreva("voce precisa de ",lata," latas, que da no total de",(lata*80)," reais")
fimse

se resposta = "latao" entao
   se metros > 10.8 entao
     se metros % 10.8 <> 0 entao
      lata <- (metros div 54)+1
     fimse
     se metros % 10.8 = 0 entao
      lata <- (metros div 54)
     fimse
   fimse
   se metros <= 10.8 entao
    lata <- 1
   fimse
   escreva("voce precisa de ",lata," latas, que da no total de",(lata*80)," reais")



Fimalgoritmo