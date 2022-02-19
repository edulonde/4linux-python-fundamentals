livros = {}
livros = {
    "id_0001": ["Nome_autor", "Titulo_da_obra"],
    "id_0002": ["Dostoiévsky", "Os Demônios"],
    "id_0003": ["Oscar Wilde", "O Retrato de Dorian Gray"],
    "id_0004": ["Dostoiévsky", "Os Demônios"],
}

livros["id_0005"]=['Nietzsche', 'O Anticristo']

print(livros)
print(f"{livros.get('id_0002')}")

copia_livros = livros.copy()
print("Segue cópia atualizada: ",copia_livros)

lista_de_chaves = livros.keys()
print(lista_de_chaves)
print(type(lista_de_chaves))

itens = livros.items()
print(itens)
print(type(itens))

livros.pop("id_0001")
print(livros)
livros.popitem()
print(livros.get("id_0002"))

print(livros.values())