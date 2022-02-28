import sqlite3

conexao = sqlite3.connect('cafe.db')

cursor = conexao.cursor()

sql_string_create = """
CREATE TABLE produto (
    id integer primary key autoincrement,
    nome text,
    descricao text,
    preco real,
    ativo boolean
);
"""

sql_string_insert = """
INSERT INTO produto (nome, descricao, preco, ativo)
values ("espresso", "Café forte, extraído em alta temperatura e pressão", 4.50, 1)
"""
sql_string_select = """
SELECT * from produto
"""

#cursor.execute(sql_string_create)
cursor.execute(sql_string_insert)



#confirma alteraçãoes no banco de dados
conexao.commit()

cursor.execute(sql_string_select)
print(cursor.fetchall())

conexao.close()

