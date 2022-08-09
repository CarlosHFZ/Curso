
    ##Tipos de variavel

#str -> caracter
#int -> inteiro
#float -> real
#bool -> boleano

    ##Atribuição

#nome = 'caio'
#print(nome)

#leia
#numero = int(input("Digite um Número "))


    ##Operadores Aritméticos

#a = 10
#b = 2

#print(a+b)
#print(a-b)
#print(a*b)
#print(a/b)
#print(a%b)
#print(a//b)
#print(a**b)

    ##manipulação de string - podem ser utilizados em conjunto

#nome = 'esTou nO joVem PrOGRAmador'

#maiusculo
#print(nome.upper())

#minusculo
#print(nome.lower())

#Primeiras letras Maiculas
#print(nome.title())

#So primeira letra maiuscula
#print(nome.capitalize())

#Limpar espaços vazios
#print(nome.strip())

#Ler numero de letras
#print(len(nome))

                #Retirar casa decimais

#x = 10
#y = 3

#divisao = x / y

#print(f"a divisap de {x} e {y} e igual a {divisao:.0f}")



#x = True
#while x == True:

    #idade = int(input('Qual a sua idade?'))

    #if idade < 18:
        #print("Usuario não pode tirar a carteira.")
   # else:
       # print('Já pode tirar a carteira, , meus parabens!!!')
        #x = False


    #Repetição

#resposta_certa = 10+5

#resposta_usuario = int(input('Quanto é 10 + 5? '))

#while resposta_usuario != resposta_certa:
    #print('Quanto é 10 + 5? ')
    #resposta_usuario = int(input('A resposta errada, tente novamente. '))

#print('Você acertou. ')

#resposta_certa = 10+5

#while True:
   #resposta_usuario = int(input('Quanto é 10 + 5? '))
    #if resposta_certa == resposta_usuario:
       # print('Você acertou')
       # break


               #transforma spring em valor numerico

#x = 10
#y = 5

#resultado = eval(f'{x}+{y}')

#print(resultado)

#n1 = int(int('Numero 1'))
#expressao = str(input(' + para somar \n - para subtrair \n * para multiplicar \n / para divisão'))
#n2 = int(int('Numero 2'))
#print(f'O resultado de {n1}{expressao}{n2} é igual a {resultado}. ')

         #Como usar o for #utilizado para colocar quantidade de veses qye ira repitir
#for i in range(0,100):
    #print(i)

       #pular numeros
#for lista in range(0,101,10):
    #print(lista)


#notas = int(input('Quantas notas deseja calcular? '))
#media = 0

#for i in range(1,notas+1):
    #nota = float(input(f'Digite a nota {i}: '))
    #media += nota
#print(f"a média é {media/nota:.1f}")


                 #Manipulaçoes de strings
#x = 'Python'

#print(x[-1])

              #lista ou array

#eletronicos = ['ps4','iphone','xbox']

#for item in eletronicos:
    #print(item)

#max e min para achar valores do mais alto e o mais baixo


#eval tranforma em valores aritimeticos

#x = eval('10+(5/5)')
#print(x)




