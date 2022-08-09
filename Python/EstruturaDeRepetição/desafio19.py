




print('Qual o melhor Sistema Operacional para uso em servidores?')
print("")
print("As possíveis respostas são:")
print("")
print(" 1 - Windows Server \n 2 - Unix \n 3 - Linux \n 4 - Netware \n 5 - Mac OS \n 6 - Outro")
print("")

sistemas = []
windows = []
unix = []
linux = []
netware = []
mac = []
outro = []
total = -1
resposta = 0
#.isnumeric()

while True:
    total += 1 
    resposta = input('Digite: ')
    if resposta != "0" and resposta != "1" and resposta != "2" and resposta != "3" and resposta != "4" and resposta != "5" and resposta != "6":
        print('Digito incorrreto, favor digitar novamete: ')
        total += -1
    if resposta == "0":
        break  
    if resposta == "1":
        windows.append(1)
        sistemas.append('Windows Server')
    if resposta == "2":
        unix.append(2)
        sistemas.append('Unix')
    if resposta == "3":
        linux.append(3)
        sistemas.append('Linux')
    if resposta == "4":
        netware.append(4)
        sistemas.append('Netware')
    if resposta == "5":
        mac.append(5)
        sistemas.append('Mac OS')
    if resposta == "6":
       outro.append(6)
       sistemas.append('Outro')
print('')
if resposta == "0":
    print(f'Windows Server recebeu {windows.count(1)} votos, dando um total de {windows.count(1)*(100/total):.0f}% dos votos')
    print(f'Unix recebeu {unix.count(2)} votos, dando um total de {unix.count(2)*(100/total):.0f}% dos votos')
    print(f'Linux recebeu {linux.count(3)} votos, dando um total de {linux.count(3)*(100/total):.0f}% dos votos')
    print(f'Netware recebeu {netware.count(4)} votos, dando um total de {netware.count(4)*(100/total):.0f}% dos votos')
    print(f'Mac OS recebeu {mac.count(5)} votos, dando um total de {mac.count(5)*(100/total):.0f}% dos votos')
    print(f'Outro recebeu {outro.count(6)} votos, dando um total de {outro.count(6)*(100/total):.0f}% dos votos')
    print("")
    print(f'Total de {total} votos')

nomes = ["Windows Server","Unix","Linux","Netware","Mac OS","Outro"]
print('')
if sistemas.count("Windows Server") > sistemas.count("Unix") and sistemas.count("Windows Server") > sistemas.count("Linux") and sistemas.count("Windows Server") > sistemas.count("Netware") and sistemas.count("Windows Server") > sistemas.count("Mac OS") and sistemas.count("Windows Server") > sistemas.count("outros"):
    print(f"O sistema operacional mais votado foi {nomes[0]}, com um total de {windows.count(1)} votos, correpondendo a {windows.count(1)*(100/total):.0f}% dos votos ")

if sistemas.count("Unix") > sistemas.count("Windows Server") and sistemas.count("Unix")  > sistemas.count("Linux") and sistemas.count("Unix") > sistemas.count("Netware") and sistemas.count("Unix") > sistemas.count("Mac OS") and sistemas.count("Unix") > sistemas.count("outros"):
    print(f"O sistema operacional mais votado foi {nomes[1]}, com um total de {unix.count(2)} votos, correpondendo a {unix.count(2)*(100/total):.0f}% dos votos ")

if sistemas.count("Linux") > sistemas.count("Windows Server") and sistemas.count("Linux") > sistemas.count("Unix") and sistemas.count("Linux") > sistemas.count("Netware") and sistemas.count("Linux") > sistemas.count("Mac OS") and sistemas.count("Linux") > sistemas.count("outros"):
    print(f"O sistema operacional mais votado foi {nomes[2]}, com um total de {linux.count(3)} votos, correpondendo a {linux.count(3)*(100/total):.0f}% dos votos ")

if sistemas.count("Netware") > sistemas.count("Unix") and sistemas.count("Netware") > sistemas.count("Linux") and sistemas.count("Netware") > sistemas.count("Windows Server") and sistemas.count("Netware") > sistemas.count("Mac OS") and sistemas.count("Netware") > sistemas.count("outros"):
    print(f"O sistema operacional mais votado foi {nomes[3]}, com um total de {netware.count(4)} votos, correpondendo a {netware.count(4)*(100/total):.0f}% dos votos ")

if sistemas.count("Mac OS") > sistemas.count("Unix") and sistemas.count("Mac OS") > sistemas.count("Linux") and sistemas.count("Mac OS") > sistemas.count("Netware") and sistemas.count("Mac OS") > sistemas.count("Windows Server") and sistemas.count("Mac OS") > sistemas.count("outros"):
    print(f"O sistema operacional mais votado foi {nomes[4]}, com um total de {mac.count(5)} votos, correpondendo a {mac.count(5)*(100/total):.0f}% dos votos ")

if sistemas.count("Outro") > sistemas.count("Unix") and sistemas.count("Outro") > sistemas.count("Linux") and sistemas.count("Outro") > sistemas.count("Netware") and sistemas.count("Outro") > sistemas.count("Mac OS") and sistemas.count("Outro") > sistemas.count("Windows Server"):
    print(f"O sistema operacional mais votado foi {nomes[5]}, com um total de {outro.count(6)} votos, correpondendo a {outro.count(6)*(100/total):.0f}% dos votos ")



    


    




