import sqlite3

#Conectando no BD
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

#Inserindo dados
cursor.execute(
    '''
    INSERT INTO filmes(nome, ano, nota)
    VALUES("Sonic", 2020, 8.0)
    '''
    
)

conexao.commit()
conexao.close()

print('Dados inseridos na tabela')