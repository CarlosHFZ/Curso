



class Cardapio:          
    def adicionar(self):
        import sqlite3
        conexao = sqlite3.connect('ProdutosBanco.db')
        cursor = conexao.cursor()
        pro = input('Nome do Produto: ').upper()
        pre = float(input('Preço do Produto: '))
        cursor.execute('INSERT INTO produtos(nome,preço) VALUES (?,?)',(pro,pre))
        conexao.commit()
        cursor.close()
        conexao.close()

    def alterarProduto(self):
        import sqlite3
        conexao = sqlite3.connect('ProdutosBanco.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM produtos')
        for i in cursor.fetchall():
            print(i)
        id = int(input('ID do produto a ser mudado: '))
        proN = input('Nome do Produto: ').upper()
        preN = float(input('Preço do Produto: '))
        cursor.execute('UPDATE produtos SET nome = ?, preço = ?  WHERE id = ?',(proN,preN,id))
        conexao.commit()
        cursor.close()
        conexao.close()
    def deletarProdutos(self):
        import sqlite3
        conexao = sqlite3.connect('ProdutosBanco.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM produtos')
        list = []
        remov = []
        for i in cursor.fetchall():
            print(i)
            list.append(i[0])
        r = 0
        while True:
            r = int(input('Digite o ID para deleter o produto: '))
            if r not in list:
                print('ID não existe')
            else:
                remov.append(r)
                break
        for list in remov:
            cursor.execute(f'DELETE FROM produtos WHERE id = {list}')
            conexao.commit()
        cursor.close()
        conexao.close()
    def mostrarCardapio(self):
        import sqlite3
        conexao = sqlite3.connect('ProdutosBanco.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM produtos')
        print('\n Cardapio \n ')
        for i in cursor.fetchall():
            print(f'{i[1]} \ R$ {i[2]}')
        print('')
        cursor.close()
        conexao.close()









                

            
