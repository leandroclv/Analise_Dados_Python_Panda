import sqlite3

#Conectando no BD
conexao = sqlite3.connect('titulo.db')

#Criando o cursor
cursor = conexao.cursor()

#Criando a tabela
cursor.execute(
    '''
        CREATE TABLE filmes(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOt NULL,
            nota,  REAL NOT NULL,
        );
    '''
)

#Fecha conexão
conexao.close()
print('Tabela foi criada')