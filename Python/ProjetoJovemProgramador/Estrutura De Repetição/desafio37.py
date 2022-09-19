#mais alta
#mais baixo
#mais gordo
#mais magro

  #perguntar 
#seu codigo
#seu peso
#sua altura
#para finalizar digitar 0
#deve ser informados os códigos e valores do clente mais alto
#do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes


from dataclasses import replace


code = 0
alt = 0
peso = 0

cod_mais_alto = 0
mais_alto = 0

cod_mais_gordo = 0
mais_gordo = 0


mais_baixo = 1000000
cod_mais_baixo = 1000000

mais_magro = 100000000
cod_mais_baixo = 1000000

media_peso = 0
media_altura = 0

c = 0

while True:
  if c == 0:
    print("Se deseja finalizar digite 0. ")
  code = int(input('Digite o codigo do aluno: '))
  if code == 0:
    break
  c += 1 
  alt = float(input('Digite a altura do aluno: '))
  
  media_altura += alt
  peso = float(input('Digite o peso do cliente: ')) 

  media_peso =+ peso

  if alt > mais_alto:
    mais_alto = alt
    cod_mais_alto = code

  if alt < mais_baixo:
    mais_baixo = alt
    cod_mais_baixo = code 

  if peso > mais_gordo:
    mais_gordo = peso
    cod_mais_gordo = code

  if peso < mais_magro:
    mais_magro = peso
    cod_mais_magro = code

print(f'O aluno {cod_mais_alto} é o mais alto com {mais_alto} de altura. ')
print(f'O aluno {cod_mais_baixo} é o mais baixo com {mais_baixo} de altura. ')
print(f'O aluno {cod_mais_gordo} é o mais gordo com {mais_gordo} de peso. ')
print(f'O aluno {cod_mais_magro} é o mais magro com {mais_magro} de peso. ')
print(f'A media de peso é {media_peso/c:.2f}')
print(f'A media de altura é {media_altura/c:.2f}')

  
  
    






