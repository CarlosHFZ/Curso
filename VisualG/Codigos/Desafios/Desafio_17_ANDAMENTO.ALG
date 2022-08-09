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
lata:real


Inicio

escreval("Digite o total em metros quadrados a ser pintado: ")
leia(metros)

escreval("Vocé quer comprar somente lata ou latao? ")
leia(resposta)

se resposta = "lata" entao
   se metros > 108 entao
     se metros % 108 <> 0 entao
      lata <- (metros div 108)+1
     fimse
     se metros % 108 = 0 entao
      lata <- (metros div 108)
     fimse
   fimse
   se metros <= 108 entao
    lata <- 1
   fimse
   escreva("voce precisa de ",lata," latas, que da no total de",(lata*80)," reais")
fimse

se resposta = "latao" entao
   se metros > 21.6 entao
     se metros % 21.6 <> 0 entao
      lata <- (metros div 21.6)+1
     fimse
     se metros % 21.6 = 0 entao
      lata <- (metros div 21.6)
     fimse
   fimse
   se metros <= 21.6 entao
    lata <- 1
   fimse
   escreva("voce precisa de ",lata," latoes, que da no total de",(lata*25)," reais")
fimse

Fimalgoritmo
