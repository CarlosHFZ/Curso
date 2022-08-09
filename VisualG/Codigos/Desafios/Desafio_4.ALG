Algoritmo "Média de Notas"

Var

Aluno:caracter
Nota1,Nota2,Nota3,Nota4:real
M:real

Inicio

escreval("Digite o nome do aluno")
leia(Aluno)
escreval("")
escreval("Muito bem, informe as 5 notas do ",Aluno)
escreval("")
escreva("Nota 1: ")
leia(nota1)
escreva("Nota 2: ")
leia(nota2)
escreva("Nota 3: ")
leia(nota3)
escreva("Nota 4: ")
leia(nota4)
M <- (Nota1+Nota2+Nota3+Nota4)/4)
escreval("")
escreval("A média do Aluno ", Aluno," é ",M)
escreval("")
   Se M >= 7 entao
    escreva(Aluno," foi aprovado")
   fimse
   Se M < 7 entao
    escreva(Aluno," Foi reprovado")
   fimse
   
escreval("")
Fimalgoritmo