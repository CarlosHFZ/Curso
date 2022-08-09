Algoritmo "semnome"

//maximo 50 kg
//multa po kg execedente é 4,00

Var

kg:real

Inicio

escreval("Digite o peso do peixe: ")
leia(kg)

   se kg > 50 entao
     escreval("Peso permitido ultrapassado")
     escreval(("A multa por peso exedente é de R$"),(kg-50)*4.00)
   fimse


Fimalgoritmo