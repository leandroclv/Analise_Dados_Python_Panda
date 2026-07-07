import sqlite3

#Conectar no BD
def conecta_bd():
    conexao = sqlite3.connect('titulo.db')
    return conexao

#Inserir dados
def insere_dados(nome, ano, nota):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute(
    '''
        INSERT INTO filmes (nome, ano, nota)
        VALUES(?, ?, ?)
    ''', (nome, ano, nota)
    )

    conexao.commit()
    conexao.close()
    
#Listagem de dados
def obter_dados():
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM filmes')
    dados = cursor.fetchall()
    return dados