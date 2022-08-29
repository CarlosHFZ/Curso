



class Pedido:
    def __init__(self):
        self.valor_total = 0
        self.compras = []
          
    def adicionar(self, Produto, quantidade):
        self.compras.append(ItemPedido(Produto, quantidade))
        
    def total(self):
        for item in self.compras:
            valor = item.produto.valor
            quantidade = item.quantidade
            self.valor_total += (quantidade * valor)
        return self.valor_total
    def __str__(self):
        return f"Total da compra: R${self.valor_total}"
    
            
class ItemPedido:
    def __init__(self, Produto, quantidade):
        self.quantidade = quantidade
        self.produto = Produto
    
            
class Produto:
    def __init__(self, codigo, valor, descrição):
        self.codigo = codigo
        self.valor = valor
        self.descrição = descrição







# chapeu = Produto(2520, 38, "Chápeu")
# fone = Produto(2020, 90, "Fone de Ouvido da Samsung")
# mesa = Produto(2025, 580, "Mesa de marmore massiço")

# pedido1 = Pedido()
# pedido1.adicionar(chapeu, 3)
# pedido1.adicionar(fone, 2)
# pedido1.adicionar(mesa, 1)
# pedido1.total()
# print(pedido1)

# for i in range(len(pedido1.compras)):
#     print(i)


    