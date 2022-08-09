Algoritmo "Hipotenusa"

Var

catA,catB,hipo,hipo2:real

Inicio

escreval("Digite o valor do Cateto A")
leia(catA)
escreval("Digite o varlor do Cateto B")
leia(catB)

hipo2<-(catA*catA)+(catB*catB)
hipo<-raizq(hipo2)
escreval("")                                         //hipo<-(catA^2+catB^2)^(1/2)
escreval("O resultado da Hipotenusa é ",hipo)

Fimalgoritmo