class Livro:
    def __init__(self, nome, qtdpag, autor, preco):
        self.nome = nome
        self.qtdpag = qtdpag
        self.autor = autor
        self.preco = preco

    def definir_preco(self,preco):
        self.preco = preco

    def ver_preco(self):
        print(self.preco)

livro_1 = Livro('Lusiadas', '800', 'Camões', '0')
livro_1.definir_preco(500)
livro_1.ver_preco()
