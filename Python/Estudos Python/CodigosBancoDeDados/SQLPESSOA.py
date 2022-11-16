import sqlite3

# nome, idade, peso, sexo e classe social




# Altere o peso e classe social de pelo menos 3 pessoas com idade acima de 60 anos.

def cadastro():
    conexao = sqlite3.connect("BancoNovoPessoas.db")
    cursor = conexao.cursor()
    nome = input("Nome: ").capitalize()
    idade = int(input("idade: "))
    peso = float(input('Peso: '))
    sexo = input('Sexo: ').capitalize()
    classe = input("Classe Social: ").capitalize()

    cursor.execute('INSERT INTO Pessoas(NOME,IDADE,PESO,SEXO,CLASSE) VALUES (?,?,?,?,?)',(nome,idade,peso,sexo,classe))
    conexao.commit()
    cursor.close()
    conexao.close()
def Categoria():
    conexao = sqlite3.connect("BancoNovoPessoas.db")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM Pessoas')

    print("Pessoas com o peso acima de 60\n ")
    for i in cursor.fetchall():
        if i[3] >= 60:
            print(F'ID:{i[0]} \nNome:{i[1]} \nIdade: {i[2]} \nPeso:{i[3]} \nSexo:{i[4]} \nClasse Social:{i[5]}\n  ')

    print('')
    cursor.execute('SELECT * FROM Pessoas')
    print('Pessoas do sexo Feminino')   
    for i in cursor.fetchall():
        if i[4] == 'Feminino':
            print(F'ID:{i[0]} \nNome:{i[1]} \nIdade: {i[2]} \nPeso:{i[3]} \nSexo:{i[4]} \nClasse Social:{i[5]}\n  ')

    print('')
    cursor.execute('SELECT * FROM Pessoas')  
    print('Pessoas da Classe Social Alta')
    for i in cursor.fetchall():
        if i[5] == 'Alta':
            print(F'ID:{i[0]} \nNome:{i[1]} \nIdade: {i[2]} \nPeso:{i[3]} \nSexo:{i[4]} \nClasse Social:{i[5]}\n  ')

    print('')
    cursor.execute('SELECT * FROM Pessoas')
    print('Pessoas com o peso acima de 60, maiores de 18 anos, do sexo Feminino e de Classe Social Alta')   
    for i in cursor.fetchall():
        if i[3] >= 60 and i[2] >= 18 and i[4] == 'Feminino' and i[5] == 'Alta':
            print(F'ID:{i[0]} \nNome:{i[1]} \nIdade: {i[2]} \nPeso:{i[3]} \nSexo:{i[4]} \nClasse Social:{i[5]}\n  ')

                
    cursor.close()
    conexao.close()
def Mudar():
    conexao = sqlite3.connect("BancoNovoPessoas.db")
    cursor = conexao.cursor()
    ide = int(input('Qual ID para fazer a mudança: '))
    peso = float(input('Peso: '))
    classe = input("Classe Social: ")
    cursor.execute('UPDATE Pessoas SET (PESO,CLASSE) = (?,?) WHERE ID = ? ',(peso,classe,ide))
    conexao.commit()
    cursor.close()
    conexao.close


Categoria()


