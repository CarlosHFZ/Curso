lista = []
par = []
impar = []

print('Vamos montas 3 listas para voce: \n uma com todos os numeros numeros. \n uma com somente os numeros pares. \n uma com somente os numeos impáres.')
print('')
n1 = int(input('Digite o primeiro numero da lista "So pode ser numero inteiro": '))
n2 = int(input('Digite o ultimo numero da lista "So pode ser numero inteiro": '))


   
for i in range(n1,n2+1):
    lista.append(i)
    if (i % 2) == 0:        
        par.append(i)

for i in range(n1,n2+1):
    if (i % 2) != 0:        
        impar.append(i)

print(f'lista de todos os numeros \n {lista}')
print("")
print(f'lista dos numeros pares \n {par}')
print("")
print(f'lista dos numeros impares \n {impar}')
print("")
    



