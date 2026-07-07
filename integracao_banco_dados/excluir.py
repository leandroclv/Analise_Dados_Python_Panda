import sqlite3

#Conectando no banco de dados
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

#exclusão de dados
id = (1,2)
cursor.execute(
    '''
        DELETE FROM filmes
        WHERE ID in (?,?)
    ''',
    id
)

conexao.commit()
print('Dados excluídos com sucesso')