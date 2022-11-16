import sqlite3

conexao = sqlite3.connect("dataBase.db")
cursor = conexao.cursor()

nome = []

cursor.execute("SELECT * FROM clientes")
for i in cursor.fetchall():
    if i[1] not in nome:
        nome.append(i[1])
print(nome)

for i in nome:
    cursor.execute(f"SELECT * FROM clientes WHERE nome = '{i}' ")
    ids = []
    for linha in cursor.fetchall():
        print(linha)
        ids.append(linha[0])
    op = 0
    while True:
        if op not in ids:
            op = int(input('Qual id deseja manter? '))
        else:
            ids.remove(op)
            break
    for id in ids:           
        cursor.execute(f'DELETE FROM clientes WHERE id = {id}')
        conexao.commit()
cursor.close()
conexao.close()
        
    



