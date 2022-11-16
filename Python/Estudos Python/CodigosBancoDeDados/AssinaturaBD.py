import sqlite3

conexao = sqlite3.connect('AssinaraBando.db')
cursor = conexao.cursor()

verd = 0


cursor.execute('SELECT * FROM clientes')
for i in cursor.fetchall():
    print(i)
    cursor.execute(f'DELETE FROM clientes WHERE pagamento = {verd}')
    conexao.commit()



cursor.close()
conexao.close()
