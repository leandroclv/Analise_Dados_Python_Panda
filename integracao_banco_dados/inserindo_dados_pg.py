from conexao_post import conn

cursor_obj = conn.cursor()

games = [
    ('Star Wars Survivor', 2023, 9.0),
    ('Luigis Mansion 3', 2019, 9.0)
]

for game in games:
    cursor_obj.execute(
        '''
            INSERT INTO game(name, year, score)
            VALUES (%S, %S, %S)
        ''', game
        
    )
conn.commit()
print('Dados inserios com sucesso')
conn.close()