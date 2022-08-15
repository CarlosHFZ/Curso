
from random import choice

palavras = ('CARRO','MOTO','MOTOSSERRA','MOTEL','FUTEBOL','RAPOSA')

print('Esse é um jogo da forca, você tem 5 chances de descobrir a palavra.\nVocê deve digitar as letras separadamente \nOu você pode escrever a palavra a qualquer momento .')
print('')
print('Estarei sempre mostrando as palavras que vc acerta,')
print('')

resposta = choice(palavras)
resposta_separada = list(resposta)

palavra = []
chute = []
chutes = ""

for i in range(0,len(resposta_separada)):
    palavra.append('-')


print(f'A palavra contem {len(resposta)} letras. ')
print('')

c = 0

while True:
    c += 1
    if c == 5:
        print('!!!Essa e sua ultima chance, chute a palavra!!!')
    if c > 5:
        print(f'Suas {c-1} chances acabaram, a palavra era "{resposta}" você perdeu.'),
        break
    chute.clear()
    r = str(input('Digite uma letra ou a palavra: ')).upper()
    chute.append(r)
    
    if r != resposta:
        for i in range(0,len(resposta_separada)):
            if chute[0] == resposta_separada[i]:
                palavra[i] = chute[0]

    if len(r) == 1:
        chutes += (f'{r}, ')

    if r == '':
        chutes += 'Sem chute, '     
    
    if r != resposta:
        print('')         
        print(f'Forca:  {palavra}') 
        print('')   
        if chutes == "":
            print('Nenhuma letra chutada')
        else:
            print(f'Letras chutadas: {chutes}')
            print('')
            

    if len(r) > 1 and r != resposta:
        print(f'Não é a palavra {r} ')
        print('')

    if palavra == resposta_separada or r == resposta:
        print('')
        print('!!!Voce acertou a palavra!!!')
        print(f'A palavra era "{resposta}"')
        break
        






    
        
