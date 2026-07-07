import sqlite3

#Conectando no BD
conexao = sqlite3.connect('titulo.bd')
cursor = conexao.cursor()

#Leitura de dados
dados = cursor.execute('SELECT * FROM filmes')

print(dados)