Algoritmo "semnome"

//Para homens: (72.7*h) - 58
//Para mulheres: (62.1*h) - 44.7

Var

sexo:caracter
altura:real

Inicio

escreval("Vamos calcular o seu peso ideal")
escreval("Qual sua altura?")
leia(altura)
escreval("Voce é h/m? ")
leia(sexo)
   se sexo = "h" entao
    escreval("Seu peso ideal é :",(72.7*altura)-58)
   fimse
   se sexo = "m" entao
    escreval("Seu peso ideal é :",(62.1*altura)-44.7)
   fimse

Fimalgoritmo