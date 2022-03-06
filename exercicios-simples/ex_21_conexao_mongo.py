from pymongo import MongoClient

conexao = MongoClient()
print(conexao)
db = conexao.cafe
print(db)
produto = db.produto
pedido = db.pedido
print(produto)
print(pedido)

registro = {
    'nome': 'Café',
    'descricao': 'Café preto',
    'preco': 4.50
}

produto.insert_one(registro)

print(produto.find_one())
for produto in produto.find():
    print("-"*5)
    print("Nome: ", produto['nome'])
    print("Descrição: ", produto['descricao'] )
    print("Preço: ", produto['preco'])