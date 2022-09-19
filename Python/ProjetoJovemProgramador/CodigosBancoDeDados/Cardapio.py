from ProdutosBD import Cardapio

while True:
    card = Cardapio()
    print('Opção 1 - Exibir Cardápio\nOpção 2 - Adicionar Produto ao Cardápio\nOpção 3 - Alterar item do Cardápio\nOpção 4 - Deletar item do Cardápio\nOpção 5 - Sair')
    r = input('Digite: ')
    match r:
        case '1':
                card.mostrarCardapio()
        case '2':
            while True:
                card.adicionar()
                r = input("\nDigite '1' para adicionar mais produtos ou quaquer coisa para sair\n")
                if r != "1":
                    break
        case '3':
            while True:
                card.alterarProduto()
                r = input("\nDigite '1' para alterar mais produtos ou quaquer coisa para sair\n")
                if r != "1":
                    break
        case '4':
            while True:
                card.deletarProdutos()
                r = input("\nDigite '1' para alterar mais produtos ou quaquer coisa para sair\n")
                if r != "1":
                    break
        case '5':
            exit()