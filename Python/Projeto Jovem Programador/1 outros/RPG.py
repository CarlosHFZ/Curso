raça = ""
classe = ""
strenght = 0
agility = 0
intelligence = 0
charisma = 0
# guerreiro froça +10 agillidade +2 inteligencia +0 carisma
# humano +5 em tudo



print('Escolha uma Raça e uma Classe abaixo: \nRaça: Humano\nRaça: Elfo\nRaça: Orc\n')
print('Classe: Guerreiro\nClasse: Mago\nClasse: Assasino')

r = str(input('Qual raça você escolhe? ').lower())
match r:
    case "humano":
        strenght += 5
        agility += 5
        intelligence = 5
        charisma += 5
        raça = "Humano"
    case "Elfo":
        strenght += 2
        agility += 8
        intelligence = 7
        charisma += 3
        raça = "Elfo"
    case "orc":
        strenght += 11
        agility += 4
        intelligence = 3
        charisma += 2
        raça = "Orc"
    case _:
        print('Essa Raça não existe')

r = str(input('Qual Classe você escolhe? ').lower())
match r:
    case "guerreiro":
        strenght += 7
        agility += 2
        intelligence = 0
        charisma += 1
        classe = "Guerreiro"
    case "mago":
        strenght += 0
        agility += 1
        intelligence = 7
        charisma += 2
        classe = "Mago"
    case "assassino":
        strenght += 1
        agility += 7
        intelligence = 1
        charisma += 1
        classe = "Assassino"
    case _:
        print('Essa Classe não existe')
print(f"Sua Raça é {raça}")
print(f"Sua Classe é {classe}")
print(f'Força: {strenght}')
print(f'Agilidade: {agility}')
print(f'Inteligencia: {intelligence}')
print(f'Charisma: {charisma}')