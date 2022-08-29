from BombaDeCombustivel import BombaDeCombustivel
#Gasolina = R$5,68 por litro e tem 7.000 litros na bomba
#disel = R$7,89 por litro tem 12.000 litros na bomba
#Etanol = R$4,23 por litro tem 5.000 litros na bomba
usuario = []

while True:
    
    op = input('\nOpção 1: Reprogramar Bombona \nOpção 2: Abastecer\nOpção 3: Status da bomba\nOpção 4: Sair\nDigite:')
    match op:
        case "1":
            tipo = input('Qual o tipo de combustivel\nOpção 1: Gasolina\nOpção 2: Dissel\nOpção 3: Etanol\nDigite:')
            match tipo:
                case "1":
                    usuario = BombaDeCombustivel("Gasolina",0,0)
                    preço = float(input('Qual o preço por litro? '))
                    usuario = BombaDeCombustivel("Gasolina",preço,0)
                    quantidade = float(input('Quantidade a abastecer a bombona? '))
                    usuario = BombaDeCombustivel("Gasolina",preço,quantidade)
                case "2":
                    usuario = BombaDeCombustivel("Dissel",0,0)
                    preço = float(input('Qual o preço por litro? '))
                    usuario = BombaDeCombustivel("Dissel",preço,0)
                    quantidade = float(input('Quantidade a abastecer a bombona? '))
                    usuario = BombaDeCombustivel("Dissel",preço,quantidade)
                case "3":
                    usuario = BombaDeCombustivel("Etanol",0,0)
                    preço = float(input('Qual o preço por litro? '))
                    usuario = BombaDeCombustivel("Etanol",preço,0)
                    quantidade = float(input('Quantidade a abastecer a bombona? '))
                    usuario = BombaDeCombustivel("Etanol",preço,quantidade)
                case _:
                    print('Opção incorreta')

        case "2":
            r = input('Opção 1: Pagar por valor monetario\nOpção 2: Pagar por litro\nDigite:')
            match r:
                case "1":
                    r = float(input('Valor: '))
                    usuario.abastecerPorValor(r)
                    print(usuario.valor_a_pagar)
                case '2':
                    r = float(input("Litros: "))
                    usuario.abastecerPorLitro(r)
                    print(usuario.valor_a_pagar)
                case _:
                    print('Opção incorreta')
        case "3":
            print(usuario)
        case "4":
            exit()
        case _:
            print('Opção incorreta')
                
