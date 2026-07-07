import sqlite3

#Conectando no banco de dados
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

#Atualizando dados
id=1
cursor.execute(
    '''
        UPDATE filmes SET nome = ?
        WHERE id=?
    ''',
    (8.5, id)
)

conexao.commit()
print('Dados atualizados')