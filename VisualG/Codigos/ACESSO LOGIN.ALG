Algoritmo "Acesso LOGIN"

Var

 Nome1,Senha1,Nome2,Senha2:caracter

Inicio

escreval("")
escreva("Digite seu Usuario: ")
leia(Nome1)
escreva("Digite sua senha: ")
leia(Senha1)
escreval("")

escreva("Digite seu Usuario novamente: ")
leia(Nome2)
escreva("Digite sua senha novamente: ")
leia(Senha2)
escreval("")

  se (Nome1 = Nome2) e (Senha1 = Senha2) entao
    escreva("Acesso Autorizado")
  fimse
  se (Nome1 <> Nome2) ou (Senha1 <> Senha2) entao
    escreva("Acesso Negado")
  fimse

escreval("")

Fimalgoritmo