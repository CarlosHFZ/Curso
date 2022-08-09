
a = ("S")
while a == "S":
    r = str(input("Voce é homen ou mulher? ")).lower()

    if r == "homen":
        print("Você se aposenta aos 65 anos")
    elif r == "mulher":
        print("Você se aposenta aos 60 anos")
    else:
        print('Incorreto')
    a = str(input('Voce deseja continuar S/N? '))
